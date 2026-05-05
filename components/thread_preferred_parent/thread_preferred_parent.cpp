#include "thread_preferred_parent.h"

namespace esphome {
namespace thread_preferred_parent {

static const char *const TAG = "thread_preferred_parent";

void ThreadPreferredParentComponent::setup() {
  ESP_LOGI(TAG, "Thread preferred-parent component initialized");
}

void ThreadPreferredParentComponent::dump_config() {
  ESP_LOGCONFIG(TAG, "Thread preferred parent:");
  ESP_LOGCONFIG(TAG, "  Target type: %s", target_type_to_string_(this->target_type_));
  ESP_LOGCONFIG(TAG, "  Target: %s", this->target_to_string_().c_str());
  ESP_LOGCONFIG(TAG, "  Max attempts: %u", this->max_attempts_);
  ESP_LOGCONFIG(TAG, "  Retry interval: %u ms", this->retry_interval_ms_);
  ESP_LOGCONFIG(TAG, "  Status: %s", status_to_string_(this->status_));
}

void ThreadPreferredParentComponent::set_parent_rloc16(uint16_t rloc16) {
  this->target_type_ = TargetType::RLOC16;
  this->target_rloc16_ = rloc16;
  ESP_LOGI(TAG, "Configured preferred parent by RLOC16: 0x%04x", this->target_rloc16_);
}

bool ThreadPreferredParentComponent::set_parent_extaddr(const std::string &extaddr) {
  otExtAddress parsed{};
  if (!this->parse_extaddr_(extaddr, &parsed)) {
    ESP_LOGW(TAG, "Invalid preferred-parent extended address: %s", extaddr.c_str());
    this->set_status_(Status::INVALID_TARGET);
    return false;
  }

  this->target_type_ = TargetType::EXTADDR;
  this->target_extaddr_ = parsed;
  ESP_LOGI(TAG, "Configured preferred parent by extended address: %s", this->extaddr_to_string_(this->target_extaddr_).c_str());
  return true;
}

void ThreadPreferredParentComponent::request_switch() {
  if (this->target_type_ == TargetType::NONE) {
    ESP_LOGW(TAG, "Refusing preferred-parent switch without a configured target identifier");
    this->set_status_(Status::INVALID_TARGET);
    return;
  }

  if (this->target_type_ == TargetType::RLOC16 && (this->target_rloc16_ == 0xFFFF || this->target_rloc16_ == 0xFFFE)) {
    ESP_LOGW(TAG, "Refusing preferred-parent switch with invalid RLOC16 0x%04x", this->target_rloc16_);
    this->set_status_(Status::INVALID_TARGET);
    return;
  }

  this->begin_switch_();
  ESP_LOGI(TAG, "Requested Thread parent switch to %s", this->target_to_string_().c_str());
}

void ThreadPreferredParentComponent::request_switch(uint16_t rloc16) {
  this->set_parent_rloc16(rloc16);
  this->request_switch();
}

void ThreadPreferredParentComponent::request_switch(const std::string &extaddr) {
  if (!this->set_parent_extaddr(extaddr)) {
    return;
  }
  this->request_switch();
}

void ThreadPreferredParentComponent::begin_switch_() {
  this->attempts_ = 0;
  this->active_ = true;
  this->next_attempt_ms_ = 0;
  this->set_status_(Status::WAITING);
}

void ThreadPreferredParentComponent::clear_target() {
  this->target_type_ = TargetType::NONE;
  this->target_rloc16_ = 0xFFFE;
  std::memset(&this->target_extaddr_, 0, sizeof(this->target_extaddr_));
  this->active_ = false;
  this->attempts_ = 0;
  this->set_status_(Status::IDLE);

  auto lock = esphome::openthread::InstanceLock::try_acquire(0);
  if (lock.has_value()) {
    this->clear_preferred_parent_in_ot_(lock->get_instance());
  }
}

void ThreadPreferredParentComponent::loop() {
  if (!this->active_) {
    return;
  }

  auto lock = esphome::openthread::InstanceLock::try_acquire(0);
  if (!lock.has_value()) {
    return;
  }

  otInstance *instance = lock->get_instance();

  if (!this->is_child_(instance)) {
    ESP_LOGW(TAG, "Preferred-parent switch requires the Thread role to be CHILD");
    this->active_ = false;
    this->clear_preferred_parent_in_ot_(instance);
    this->set_status_(Status::NOT_CHILD);
    return;
  }

  if (this->current_parent_matches_(instance)) {
    ESP_LOGI(TAG, "Thread parent switch succeeded; current parent is %s", this->target_to_string_().c_str());
    this->active_ = false;
    this->clear_preferred_parent_in_ot_(instance);
    this->set_status_(Status::SUCCESS);
    return;
  }

  const uint32_t now = millis();
  if (this->next_attempt_ms_ != 0 && static_cast<int32_t>(now - this->next_attempt_ms_) < 0) {
    return;
  }

  if (this->attempts_ >= this->max_attempts_) {
    ESP_LOGW(TAG, "Preferred parent %s was not selected after %u attempts", this->target_to_string_().c_str(),
             this->attempts_);
    this->active_ = false;
    this->clear_preferred_parent_in_ot_(instance);
    this->set_status_(Status::FAILED);
    return;
  }

  this->attempts_++;
  ESP_LOGI(TAG, "Preferred-parent search attempt %u/%u for %s", this->attempts_, this->max_attempts_,
           this->target_to_string_().c_str());

  otError error = this->start_preferred_parent_search_(instance);
  if (error == OT_ERROR_NONE) {
    this->next_attempt_ms_ = now + this->retry_interval_ms_;
    this->set_status_(Status::WAITING);
    return;
  }

  ESP_LOGW(TAG, "Preferred-parent search could not start: %s", ot_error_to_string_(error));
  if (error == OT_ERROR_NOT_IMPLEMENTED) {
    this->active_ = false;
    this->set_status_(Status::API_MISSING);
  } else if (error == OT_ERROR_BUSY) {
    this->next_attempt_ms_ = now + this->retry_interval_ms_;
    this->set_status_(Status::BUSY);
  } else {
    this->next_attempt_ms_ = now + this->retry_interval_ms_;
  }
}

bool ThreadPreferredParentComponent::is_child_(otInstance *instance) const {
  return otThreadGetDeviceRole(instance) == OT_DEVICE_ROLE_CHILD;
}

bool ThreadPreferredParentComponent::current_parent_matches_(otInstance *instance) const {
  otRouterInfo parent_info{};
  if (otThreadGetParentInfo(instance, &parent_info) != OT_ERROR_NONE) {
    return false;
  }

  switch (this->target_type_) {
    case TargetType::RLOC16:
      return parent_info.mRloc16 == this->target_rloc16_;
    case TargetType::EXTADDR:
      return this->extaddr_matches_(parent_info.mExtAddress, this->target_extaddr_);
    case TargetType::NONE:
      return false;
  }
  return false;
}

otError ThreadPreferredParentComponent::start_preferred_parent_search_(otInstance *instance) {
  switch (this->target_type_) {
    case TargetType::RLOC16:
      if (otThreadSearchForPreferredParentRloc16 != nullptr) {
        return otThreadSearchForPreferredParentRloc16(instance, this->target_rloc16_);
      }
      if (otThreadSearchForPreferredParent != nullptr) {
        return otThreadSearchForPreferredParent(instance, this->target_rloc16_);
      }
      if (otThreadSetPreferredParentRloc16 != nullptr) {
        otError error = otThreadSetPreferredParentRloc16(instance, this->target_rloc16_);
        if (error != OT_ERROR_NONE) {
          return error;
        }
        return otThreadSearchForBetterParent(instance);
      }
      break;

    case TargetType::EXTADDR:
      if (otThreadSearchForPreferredParentExtAddress != nullptr) {
        return otThreadSearchForPreferredParentExtAddress(instance, &this->target_extaddr_);
      }
      if (otThreadSetPreferredParentExtAddress != nullptr) {
        otError error = otThreadSetPreferredParentExtAddress(instance, &this->target_extaddr_);
        if (error != OT_ERROR_NONE) {
          return error;
        }
        return otThreadSearchForBetterParent(instance);
      }
      break;

    case TargetType::NONE:
      return OT_ERROR_INVALID_ARGS;
  }

  return OT_ERROR_NOT_IMPLEMENTED;
}

void ThreadPreferredParentComponent::clear_preferred_parent_in_ot_(otInstance *instance) {
  if (otThreadClearPreferredParent != nullptr) {
    otThreadClearPreferredParent(instance);
    return;
  }

  // Backwards-compatible cleanup for the first starter patch revision.
  if (otThreadClearPreferredParentRloc16 != nullptr) {
    otThreadClearPreferredParentRloc16(instance);
  }
}

bool ThreadPreferredParentComponent::parse_extaddr_(const std::string &text, otExtAddress *out) const {
  char hex[16];
  size_t count = 0;
  size_t start = 0;

  if (text.size() >= 2 && text[0] == '0' && (text[1] == 'x' || text[1] == 'X')) {
    start = 2;
  }

  for (size_t i = start; i < text.size(); i++) {
    const char c = text[i];
    if (c == ':' || c == '-' || c == '_' || c == ' ') {
      continue;
    }
    if (hex_to_nibble_(c) < 0 || count >= sizeof(hex)) {
      return false;
    }
    hex[count++] = c;
  }

  if (count != sizeof(hex)) {
    return false;
  }

  for (size_t i = 0; i < sizeof(out->m8); i++) {
    int high = hex_to_nibble_(hex[i * 2]);
    int low = hex_to_nibble_(hex[i * 2 + 1]);
    if (high < 0 || low < 0) {
      return false;
    }
    out->m8[i] = static_cast<uint8_t>((high << 4) | low);
  }

  return true;
}

bool ThreadPreferredParentComponent::extaddr_matches_(const otExtAddress &a, const otExtAddress &b) const {
  return std::memcmp(a.m8, b.m8, sizeof(a.m8)) == 0;
}

std::string ThreadPreferredParentComponent::extaddr_to_string_(const otExtAddress &addr) const {
  static const char *const hex = "0123456789abcdef";
  std::string out;
  out.reserve(16);
  for (uint8_t byte : addr.m8) {
    out.push_back(hex[(byte >> 4) & 0x0f]);
    out.push_back(hex[byte & 0x0f]);
  }
  return out;
}

std::string ThreadPreferredParentComponent::target_to_string_() const {
  char buffer[32];
  switch (this->target_type_) {
    case TargetType::RLOC16:
      std::snprintf(buffer, sizeof(buffer), "RLOC16 0x%04x", this->target_rloc16_);
      return buffer;
    case TargetType::EXTADDR:
      return "ExtAddr " + this->extaddr_to_string_(this->target_extaddr_);
    case TargetType::NONE:
      return "none";
  }
  return "unknown";
}

void ThreadPreferredParentComponent::set_status_(Status status) {
  if (this->status_ != status) {
    this->status_ = status;
    ESP_LOGD(TAG, "Status changed to %s", status_to_string_(status));
  }
}

const char *ThreadPreferredParentComponent::target_type_to_string_(TargetType type) {
  switch (type) {
    case TargetType::NONE:
      return "none";
    case TargetType::RLOC16:
      return "rloc16";
    case TargetType::EXTADDR:
      return "extaddr";
  }
  return "unknown";
}

const char *ThreadPreferredParentComponent::status_to_string_(Status status) {
  switch (status) {
    case Status::IDLE:
      return "idle";
    case Status::WAITING:
      return "waiting";
    case Status::SUCCESS:
      return "success";
    case Status::FAILED:
      return "failed";
    case Status::API_MISSING:
      return "patched OpenThread API missing";
    case Status::NOT_CHILD:
      return "not child";
    case Status::BUSY:
      return "busy";
    case Status::INVALID_TARGET:
      return "invalid target";
  }
  return "unknown";
}

const char *ThreadPreferredParentComponent::ot_error_to_string_(otError error) {
  switch (error) {
    case OT_ERROR_NONE:
      return "OT_ERROR_NONE";
    case OT_ERROR_FAILED:
      return "OT_ERROR_FAILED";
    case OT_ERROR_INVALID_ARGS:
      return "OT_ERROR_INVALID_ARGS";
    case OT_ERROR_INVALID_STATE:
      return "OT_ERROR_INVALID_STATE";
    case OT_ERROR_NO_BUFS:
      return "OT_ERROR_NO_BUFS";
    case OT_ERROR_BUSY:
      return "OT_ERROR_BUSY";
    case OT_ERROR_NOT_IMPLEMENTED:
      return "OT_ERROR_NOT_IMPLEMENTED";
    default:
      return "OT_ERROR_OTHER";
  }
}

int ThreadPreferredParentComponent::hex_to_nibble_(char c) {
  if (c >= '0' && c <= '9') {
    return c - '0';
  }
  if (c >= 'a' && c <= 'f') {
    return c - 'a' + 10;
  }
  if (c >= 'A' && c <= 'F') {
    return c - 'A' + 10;
  }
  return -1;
}

}  // namespace thread_preferred_parent
}  // namespace esphome
