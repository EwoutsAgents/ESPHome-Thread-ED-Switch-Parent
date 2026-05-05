#include "thread_preferred_parent.h"

namespace esphome {
namespace thread_preferred_parent {

static const char *const TAG = "thread_preferred_parent";

void ThreadPreferredParentComponent::setup() {
  ESP_LOGI(TAG, "Thread preferred-parent component initialized");

  if (thread_preferred_parent_ot_register_parent_response_callback != nullptr) {
    thread_preferred_parent_ot_register_parent_response_callback(
        &ThreadPreferredParentComponent::parent_response_callback_, this);
    this->parent_response_callback_registered_ = true;
    ESP_LOGI(TAG, "OpenThread Parent Response reporting hook registered");
  } else {
    ESP_LOGW(TAG, "OpenThread Parent Response reporting hook is not available; patch script may not be applied yet");
  }
}

void ThreadPreferredParentComponent::dump_config() {
  ESP_LOGCONFIG(TAG, "Thread preferred parent:");
  ESP_LOGCONFIG(TAG, "  Target type: %s", target_type_to_string_(this->target_type_));
  ESP_LOGCONFIG(TAG, "  Target: %s", this->target_to_string_().c_str());
  ESP_LOGCONFIG(TAG, "  Max attempts: %u", this->max_attempts_);
  ESP_LOGCONFIG(TAG, "  Retry interval: %u ms", this->retry_interval_ms_);
  ESP_LOGCONFIG(TAG, "  Selected attach timeout: %u ms", this->selected_attach_timeout_ms_);
  ESP_LOGCONFIG(TAG, "  Require selected-parent hook: %s", YESNO(this->require_selected_parent_hook_));
  ESP_LOGCONFIG(TAG, "  Discovery hook available: %s", YESNO(this->discovery_hook_available_()));
  ESP_LOGCONFIG(TAG, "  Selected-parent hook available: %s", YESNO(this->selected_parent_hook_available_()));
  ESP_LOGCONFIG(TAG, "  Parent Response reporting hook registered: %s", YESNO(this->parent_response_callback_registered_));
  ESP_LOGCONFIG(TAG, "  Log Parent Responses: %s", YESNO(this->log_parent_responses_));
  ESP_LOGCONFIG(TAG, "  Status: %s", status_to_string_(this->status_));
}

void ThreadPreferredParentComponent::set_parent_rloc16(uint16_t rloc16) {
  this->target_type_ = TargetType::RLOC16;
  this->target_rloc16_ = rloc16;
  std::memset(&this->target_extaddr_, 0, sizeof(this->target_extaddr_));
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
  this->target_rloc16_ = 0xFFFE;
  this->target_extaddr_ = parsed;
  ESP_LOGI(TAG, "Configured preferred parent by extended address: %s",
           this->extaddr_to_string_(this->target_extaddr_).c_str());
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

void ThreadPreferredParentComponent::reset_parent_response_tracking_() {
  this->parent_response_count_ = 0;
  this->parent_response_last_dumped_count_ = 0;
  this->parent_response_target_count_ = 0;
  this->parent_response_buffer_head_ = 0;
  this->current_attempt_start_ms_ = millis();
  this->best_target_rssi_valid_ = false;
  this->best_target_rssi_ = -128;
  this->best_target_rloc16_ = 0xFFFE;
  for (auto &entry : this->parent_response_buffer_) {
    entry = BufferedParentResponse{};
  }
}

void ThreadPreferredParentComponent::begin_switch_() {
  this->attempts_ = 0;
  this->active_ = true;
  this->phase_ = SwitchPhase::DISCOVERING;
  this->phase_deadline_ms_ = 0;
  this->attach_start_ms_ = 0;
  this->target_observed_this_attempt_ = false;
  std::memset(&this->observed_target_extaddr_, 0, sizeof(this->observed_target_extaddr_));
  this->reset_parent_response_tracking_();
  this->set_status_(Status::DISCOVERING);
}

void ThreadPreferredParentComponent::clear_target() {
  this->target_type_ = TargetType::NONE;
  this->target_rloc16_ = 0xFFFE;
  std::memset(&this->target_extaddr_, 0, sizeof(this->target_extaddr_));
  std::memset(&this->observed_target_extaddr_, 0, sizeof(this->observed_target_extaddr_));
  this->active_ = false;
  this->phase_ = SwitchPhase::IDLE;
  this->attempts_ = 0;
  this->set_status_(Status::IDLE);

  auto lock = esphome::openthread::InstanceLock::try_acquire(0);
  if (lock.has_value()) {
    this->clear_preferred_parent_in_ot_(lock->get_instance());
  }
}

void ThreadPreferredParentComponent::loop() {
  const uint32_t now = millis();

  if (!this->active_) {
    return;
  }

  auto lock = esphome::openthread::InstanceLock::try_acquire(0);
  if (!lock.has_value()) {
    return;
  }

  otInstance *instance = lock->get_instance();

  if (this->current_parent_matches_(instance)) {
    const uint32_t attach_elapsed_ms = this->attach_start_ms_ == 0 ? 0 : now - this->attach_start_ms_;
    ESP_LOGI(TAG, "Thread parent switch succeeded; current parent is %s", this->target_to_string_().c_str());
    ESP_LOGI(TAG, "Attach result: success after %lu ms; %s selected",
             static_cast<unsigned long>(attach_elapsed_ms), this->target_to_string_().c_str());
    this->dump_buffered_parent_responses_("success target replay", ReplayMode::INFO_TARGET_ONLY);
    this->active_ = false;
    this->phase_ = SwitchPhase::IDLE;
    this->clear_preferred_parent_in_ot_(instance);
    this->set_status_(Status::SUCCESS);
    return;
  }

  switch (this->phase_) {
    case SwitchPhase::DISCOVERING: {
      if (this->phase_deadline_ms_ != 0 && static_cast<int32_t>(now - this->phase_deadline_ms_) < 0) {
        return;
      }

      if (this->phase_deadline_ms_ != 0) {
        this->log_discovery_summary_("discovery window complete");

        if (this->target_observed_this_attempt_) {
          ESP_LOGI(TAG, "Preferred parent %s was observed; starting selected-parent attach", this->target_to_string_().c_str());
          otError attach_error = this->start_selected_parent_attach_(instance);
          if (attach_error == OT_ERROR_NONE) {
            this->phase_ = SwitchPhase::ATTACHING;
            this->attach_start_ms_ = millis();
            this->phase_deadline_ms_ = now + this->selected_attach_timeout_ms_;
            this->set_status_(Status::ATTACHING);
            return;
          }

          ESP_LOGW(TAG, "Selected-parent attach could not start after discovery: %s", ot_error_to_string_(attach_error));
          if (attach_error == OT_ERROR_NOT_IMPLEMENTED) {
            this->active_ = false;
            this->phase_ = SwitchPhase::IDLE;
            this->set_status_(Status::API_MISSING);
            return;
          }
        } else {
          ESP_LOGW(TAG, "Preferred parent %s was not observed during discovery attempt %u/%u",
                   this->target_to_string_().c_str(), this->attempts_, this->max_attempts_);
        }

        this->phase_deadline_ms_ = 0;
      }

      if (this->attempts_ >= this->max_attempts_) {
        this->dump_buffered_parent_responses_("failure replay", ReplayMode::INFO_ALL);
        ESP_LOGW(TAG, "Attach result: failed after %u discovery attempts; %s was not selected",
                 this->attempts_, this->target_to_string_().c_str());
        this->active_ = false;
        this->phase_ = SwitchPhase::IDLE;
        this->clear_preferred_parent_in_ot_(instance);
        this->set_status_(Status::FAILED);
        return;
      }

      this->attempts_++;
      this->target_observed_this_attempt_ = false;
      std::memset(&this->observed_target_extaddr_, 0, sizeof(this->observed_target_extaddr_));
      this->reset_parent_response_tracking_();

      const otDeviceRole role = otThreadGetDeviceRole(instance);
      ESP_LOGI(TAG, "Thread role before discovery: %s", device_role_to_string_(role));
      otRouterInfo current_parent{};
      if (otThreadGetParentInfo(instance, &current_parent) == OT_ERROR_NONE) {
        ESP_LOGI(TAG, "Current parent before discovery: RLOC16 0x%04x ExtAddr %s", current_parent.mRloc16,
                 this->extaddr_to_string_(current_parent.mExtAddress).c_str());
      } else {
        ESP_LOGI(TAG, "Current parent before discovery: none");
      }

      ESP_LOGI(TAG, "Parent discovery attempt %u/%u for %s", this->attempts_, this->max_attempts_,
               this->target_to_string_().c_str());
      otError discovery_error = this->start_parent_discovery_(instance);
      if (discovery_error == OT_ERROR_NONE) {
        this->phase_deadline_ms_ = now + this->retry_interval_ms_;
        this->set_status_(Status::DISCOVERING);
        return;
      }

      ESP_LOGW(TAG, "Parent discovery could not start: %s", ot_error_to_string_(discovery_error));
      if (discovery_error == OT_ERROR_NOT_IMPLEMENTED) {
        this->active_ = false;
        this->phase_ = SwitchPhase::IDLE;
        this->set_status_(Status::API_MISSING);
      } else if (discovery_error == OT_ERROR_BUSY) {
        this->phase_deadline_ms_ = now + this->retry_interval_ms_;
        this->set_status_(Status::BUSY);
      } else {
        this->phase_deadline_ms_ = now + this->retry_interval_ms_;
      }
      return;
    }

    case SwitchPhase::ATTACHING:
      if (this->phase_deadline_ms_ != 0 && static_cast<int32_t>(now - this->phase_deadline_ms_) < 0) {
        return;
      }
      {
        const otDeviceRole role = otThreadGetDeviceRole(instance);
        otRouterInfo parent_info{};
        if (otThreadGetParentInfo(instance, &parent_info) == OT_ERROR_NONE) {
          ESP_LOGW(TAG,
                   "Attach result: timed out after %lu ms for %s; role=%s current_parent=0x%04x/%s; returning to discovery",
                   static_cast<unsigned long>(now - this->attach_start_ms_), this->target_to_string_().c_str(),
                   device_role_to_string_(role), parent_info.mRloc16,
                   this->extaddr_to_string_(parent_info.mExtAddress).c_str());
        } else {
          ESP_LOGW(TAG, "Attach result: timed out after %lu ms for %s; role=%s current_parent=none; returning to discovery",
                   static_cast<unsigned long>(now - this->attach_start_ms_), this->target_to_string_().c_str(),
                   device_role_to_string_(role));
        }
      }
      this->phase_ = SwitchPhase::DISCOVERING;
      this->phase_deadline_ms_ = 0;
      this->set_status_(Status::DISCOVERING);
      return;

    case SwitchPhase::IDLE:
      return;
  }
}

void ThreadPreferredParentComponent::parent_response_callback_(const otThreadParentResponseInfo *info, void *context) {
  if (context == nullptr) {
    return;
  }
  static_cast<ThreadPreferredParentComponent *>(context)->handle_parent_response_(info);
}

bool ThreadPreferredParentComponent::parent_response_matches_target_(const otThreadParentResponseInfo &info) const {
  switch (this->target_type_) {
    case TargetType::RLOC16:
      return info.mRloc16 == this->target_rloc16_;
    case TargetType::EXTADDR:
      return this->extaddr_matches_(info.mExtAddr, this->target_extaddr_);
    case TargetType::NONE:
      return false;
  }
  return false;
}

void ThreadPreferredParentComponent::handle_parent_response_(const otThreadParentResponseInfo *info) {
  if (info == nullptr) {
    return;
  }

  this->parent_response_count_++;
  const bool target_match = this->parent_response_matches_target_(*info);

  if (target_match) {
    this->target_observed_this_attempt_ = true;
    this->observed_target_extaddr_ = info->mExtAddr;
    this->parent_response_target_count_++;
    if (!this->best_target_rssi_valid_ || info->mRssi > this->best_target_rssi_) {
      this->best_target_rssi_valid_ = true;
      this->best_target_rssi_ = info->mRssi;
      this->best_target_rloc16_ = info->mRloc16;
    }
  }

  const uint32_t now = millis();
  BufferedParentResponse &entry = this->parent_response_buffer_[this->parent_response_buffer_head_];
  entry.valid = true;
  entry.sequence = this->parent_response_count_;
  entry.timestamp_ms = now - this->current_attempt_start_ms_;
  entry.info = *info;
  entry.target_match = target_match;
  this->parent_response_buffer_head_ = (this->parent_response_buffer_head_ + 1) % PARENT_RESPONSE_BUFFER_SIZE;

  if (this->log_parent_responses_) {
    this->log_parent_response_vv_(entry, "live");
  }
}

void ThreadPreferredParentComponent::log_parent_response_info_(const BufferedParentResponse &entry, const char *prefix) const {
  const otThreadParentResponseInfo &info = entry.info;
  ESP_LOGI(TAG,
           "Parent Response %s #%lu attempt_t+%lums: ExtAddr %s RLOC16 0x%04x RSSI %d priority %d "
           "LQ3/LQ2/LQ1 %u/%u/%u device_attached=%s target_match=%s",
           prefix, static_cast<unsigned long>(entry.sequence), static_cast<unsigned long>(entry.timestamp_ms),
           this->extaddr_to_string_(info.mExtAddr).c_str(), info.mRloc16, info.mRssi, info.mPriority,
           info.mLinkQuality3, info.mLinkQuality2, info.mLinkQuality1, YESNO(info.mIsAttached),
           YESNO(entry.target_match));
}

void ThreadPreferredParentComponent::log_parent_response_vv_(const BufferedParentResponse &entry, const char *prefix) const {
  const otThreadParentResponseInfo &info = entry.info;
  ESP_LOGVV(TAG,
            "Parent Response %s #%lu attempt_t+%lums: ExtAddr %s RLOC16 0x%04x RSSI %d priority %d "
            "LQ3/LQ2/LQ1 %u/%u/%u device_attached=%s target_match=%s",
            prefix, static_cast<unsigned long>(entry.sequence), static_cast<unsigned long>(entry.timestamp_ms),
            this->extaddr_to_string_(info.mExtAddr).c_str(), info.mRloc16, info.mRssi, info.mPriority,
            info.mLinkQuality3, info.mLinkQuality2, info.mLinkQuality1, YESNO(info.mIsAttached),
            YESNO(entry.target_match));
}

void ThreadPreferredParentComponent::log_discovery_summary_(const char *reason) const {
  if (this->best_target_rssi_valid_) {
    ESP_LOGI(TAG,
             "Discovery summary (%s): %lu Parent Responses, %lu target match(es), best target RLOC16 0x%04x RSSI %d",
             reason, static_cast<unsigned long>(this->parent_response_count_),
             static_cast<unsigned long>(this->parent_response_target_count_), this->best_target_rloc16_,
             this->best_target_rssi_);
  } else {
    ESP_LOGI(TAG, "Discovery summary (%s): %lu Parent Responses, 0 target matches", reason,
             static_cast<unsigned long>(this->parent_response_count_));
  }
}

void ThreadPreferredParentComponent::dump_buffered_parent_responses_(const char *reason, ReplayMode mode) {
  if (!this->log_parent_responses_) {
    return;
  }

  if (this->parent_response_count_ == this->parent_response_last_dumped_count_) {
    ESP_LOGI(TAG, "Parent Response replay (%s): no new responses", reason);
    return;
  }

  const bool target_only = mode == ReplayMode::INFO_TARGET_ONLY;
  uint32_t shown_count = 0;

  const uint32_t first_sequence =
      this->parent_response_count_ > PARENT_RESPONSE_BUFFER_SIZE ? this->parent_response_count_ - PARENT_RESPONSE_BUFFER_SIZE + 1 : 1;

  for (uint32_t sequence = first_sequence; sequence <= this->parent_response_count_; sequence++) {
    for (const auto &entry : this->parent_response_buffer_) {
      if (!entry.valid || entry.sequence != sequence || entry.sequence <= this->parent_response_last_dumped_count_) {
        continue;
      }
      if (target_only && !entry.target_match) {
        continue;
      }
      shown_count++;
    }
  }

  if (shown_count == 0) {
    ESP_LOGI(TAG, "Parent Response replay (%s): no matching responses to show", reason);
    this->parent_response_last_dumped_count_ = this->parent_response_count_;
    return;
  }

  ESP_LOGI(TAG, "Parent Response replay (%s): showing %lu buffered response(s)", reason,
           static_cast<unsigned long>(shown_count));

  for (uint32_t sequence = first_sequence; sequence <= this->parent_response_count_; sequence++) {
    for (const auto &entry : this->parent_response_buffer_) {
      if (!entry.valid || entry.sequence != sequence || entry.sequence <= this->parent_response_last_dumped_count_) {
        continue;
      }
      if (target_only && !entry.target_match) {
        continue;
      }
      this->log_parent_response_info_(entry, "replay");
    }
  }

  this->parent_response_last_dumped_count_ = this->parent_response_count_;
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

otError ThreadPreferredParentComponent::start_parent_discovery_(otInstance *instance) {
  if (thread_preferred_parent_ot_start_parent_discovery != nullptr) {
    ESP_LOGI(TAG, "Starting non-disruptive multicast Parent Request discovery for %s", this->target_to_string_().c_str());
    return thread_preferred_parent_ot_start_parent_discovery(instance);
  }

  // Fallback: OpenThread public API. This may switch to a better parent on its
  // own, so the patched discovery-only hook is strongly preferred.
  ESP_LOGW(TAG, "Discovery-only OpenThread hook missing; falling back to otThreadSearchForBetterParent()");
  return otThreadSearchForBetterParent(instance);
}

otError ThreadPreferredParentComponent::start_selected_parent_attach_(otInstance *instance) {
  otExtAddress selected{};

  if (this->target_observed_this_attempt_) {
    selected = this->observed_target_extaddr_;
  } else if (this->target_type_ == TargetType::EXTADDR) {
    selected = this->target_extaddr_;
  } else if (!this->resolve_rloc16_to_extaddr_(instance, this->target_rloc16_, &selected)) {
    ESP_LOGW(TAG, "RLOC16 0x%04x is not resolved to an ExtAddr", this->target_rloc16_);
    return OT_ERROR_NOT_FOUND;
  }

  if (this->selected_parent_hook_available_()) {
    ESP_LOGI(TAG, "Starting selected-parent attach to ExtAddr %s", this->extaddr_to_string_(selected).c_str());
    const bool accepted = this->request_selected_parent_attach_(instance, selected);
    ESP_LOGI(TAG, "Selected-parent attach hook returned %s", YESNO(accepted));
    return accepted ? OT_ERROR_NONE : OT_ERROR_FAILED;
  }

  if (this->require_selected_parent_hook_) {
    return OT_ERROR_NOT_IMPLEMENTED;
  }

  switch (this->target_type_) {
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
    case TargetType::NONE:
      return OT_ERROR_INVALID_ARGS;
  }

  return OT_ERROR_NOT_IMPLEMENTED;
}

bool ThreadPreferredParentComponent::selected_parent_hook_available_() const {
  return thread_preferred_parent_ot_request_selected_parent_attach != nullptr ||
         biparental_ot_request_selected_parent_attach != nullptr;
}

bool ThreadPreferredParentComponent::discovery_hook_available_() const {
  return thread_preferred_parent_ot_start_parent_discovery != nullptr;
}

bool ThreadPreferredParentComponent::request_selected_parent_attach_(otInstance *instance, const otExtAddress &extaddr) const {
  if (thread_preferred_parent_ot_request_selected_parent_attach != nullptr) {
    return thread_preferred_parent_ot_request_selected_parent_attach(instance, &extaddr);
  }
  if (biparental_ot_request_selected_parent_attach != nullptr) {
    return biparental_ot_request_selected_parent_attach(instance, &extaddr);
  }
  return false;
}

bool ThreadPreferredParentComponent::resolve_rloc16_to_extaddr_(otInstance *instance, uint16_t rloc16, otExtAddress *out) const {
  otNeighborInfoIterator iterator = OT_NEIGHBOR_INFO_ITERATOR_INIT;
  otNeighborInfo neighbor_info{};

  while (otThreadGetNextNeighborInfo(instance, &iterator, &neighbor_info) == OT_ERROR_NONE) {
    if (neighbor_info.mRloc16 == rloc16) {
      *out = neighbor_info.mExtAddress;
      return true;
    }
  }

  return false;
}

void ThreadPreferredParentComponent::clear_preferred_parent_in_ot_(otInstance *instance) {
  if (otThreadClearPreferredParent != nullptr) {
    otThreadClearPreferredParent(instance);
    return;
  }

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

const char *ThreadPreferredParentComponent::device_role_to_string_(otDeviceRole role) {
  switch (role) {
    case OT_DEVICE_ROLE_DISABLED:
      return "disabled";
    case OT_DEVICE_ROLE_DETACHED:
      return "detached";
    case OT_DEVICE_ROLE_CHILD:
      return "child";
    case OT_DEVICE_ROLE_ROUTER:
      return "router";
    case OT_DEVICE_ROLE_LEADER:
      return "leader";
  }
  return "unknown";
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
    case Status::DISCOVERING:
      return "discovering parents";
    case Status::ATTACHING:
      return "selected-parent attach in progress";
    case Status::WAITING:
      return "waiting";
    case Status::SUCCESS:
      return "success";
    case Status::FAILED:
      return "failed";
    case Status::API_MISSING:
      return "OpenThread hook missing";
    case Status::NOT_CHILD:
      return "not child";
    case Status::BUSY:
      return "busy";
    case Status::INVALID_TARGET:
      return "invalid target";
    case Status::RLOC_UNRESOLVED:
      return "rloc16 not resolved to extaddr";
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
    case OT_ERROR_NOT_FOUND:
      return "OT_ERROR_NOT_FOUND";
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
