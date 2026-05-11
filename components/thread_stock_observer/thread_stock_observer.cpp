#include "thread_stock_observer.h"

#include <cctype>

namespace esphome {
namespace thread_stock_observer {

static int hex_to_nibble_(char c) {
  if (c >= '0' && c <= '9') return c - '0';
  if (c >= 'a' && c <= 'f') return c - 'a' + 10;
  if (c >= 'A' && c <= 'F') return c - 'A' + 10;
  return -1;
}

void ThreadStockObserverComponent::setup() {
  if (thread_stock_observer_ot_register_parent_response_callback != nullptr) {
    thread_stock_observer_ot_register_parent_response_callback(
        &ThreadStockObserverComponent::parent_response_callback_, this);
    this->callback_registered_ = true;
    ESP_LOGI(TAG, "OpenThread Parent Response reporting hook registered for stock observation");
  } else {
    ESP_LOGW(TAG, "OpenThread Parent Response reporting hook is not available");
  }
}

void ThreadStockObserverComponent::dump_config() {
  ESP_LOGCONFIG(TAG, "Thread stock observer:");
  ESP_LOGCONFIG(TAG, "  Target configured: %s", YESNO(this->target_configured_));
  ESP_LOGCONFIG(TAG, "  Target ExtAddr: %s", this->extaddr_to_string_(this->target_extaddr_).c_str());
  ESP_LOGCONFIG(TAG, "  Observe timeout: %u ms", this->observe_timeout_ms_);
  ESP_LOGCONFIG(TAG, "  Log Parent Responses: %s", YESNO(this->log_parent_responses_));
  ESP_LOGCONFIG(TAG, "  Parent Response hook registered: %s", YESNO(this->callback_registered_));
}

void ThreadStockObserverComponent::set_target_parent_extaddr(const std::string &value) {
  otExtAddress parsed{};
  if (!this->parse_extaddr_(value, &parsed)) {
    ESP_LOGW(TAG, "Invalid target parent extaddr: %s", value.c_str());
    this->target_configured_ = false;
    return;
  }

  this->target_extaddr_ = parsed;
  this->target_configured_ = true;
  ESP_LOGI(TAG, "Configured target parent ExtAddr %s", this->extaddr_to_string_(this->target_extaddr_).c_str());
}

void ThreadStockObserverComponent::reset_run_state_() {
  this->active_ = false;
  this->prepared_ = false;
  this->logged_first_parent_response_ = false;
  this->logged_target_parent_response_ = false;
  this->logged_parent_changed_ = false;
  this->logged_target_reached_ = false;
}

bool ThreadStockObserverComponent::prepare_stock_search_internal_(bool current_parent_off_mode) {
  if (!this->target_configured_) {
    ESP_LOGW(TAG, "SO0 request ignored; target parent extaddr is not configured");
    return false;
  }

  if (!this->callback_registered_) {
    ESP_LOGW(TAG,
             "SO6 failure; invalid instrumentation; Parent Response hook unavailable "
             "(trial not valid for stock-observed interpretation)");
    return false;
  }

  auto lock = esphome::openthread::InstanceLock::try_acquire(0);
  if (!lock.has_value()) {
    ESP_LOGW(TAG, "SO0 request ignored; could not lock OpenThread instance");
    return false;
  }

  otInstance *instance = lock->get_instance();

  this->reset_run_state_();
  this->t0_ms_ = millis();

  const std::string target_text = this->extaddr_to_string_(this->target_extaddr_);
  if (current_parent_off_mode) {
    ESP_LOGI(TAG, "SO0 current-parent-off prepare; target=%s", target_text.c_str());
  } else {
    ESP_LOGI(TAG, "SO0 request; target=%s", target_text.c_str());
  }

  otRouterInfo parent{};
  if (otThreadGetParentInfo(instance, &parent) == OT_ERROR_NONE) {
    this->initial_parent_rloc16_ = parent.mRloc16;
    this->initial_parent_extaddr_ = parent.mExtAddress;

    ESP_LOGI(TAG, "SO0 initial parent: RLOC16 0x%04x ExtAddr %s", parent.mRloc16,
             this->extaddr_to_string_(parent.mExtAddress).c_str());
    if (current_parent_off_mode) {
      ESP_LOGI(TAG, "SO0 current parent selected for shutdown: RLOC16 0x%04x ExtAddr %s", parent.mRloc16,
               this->extaddr_to_string_(parent.mExtAddress).c_str());
      ESP_LOGI(TAG, "SO0 waiting for current-parent-off action");
    }
  } else {
    this->initial_parent_rloc16_ = 0xFFFE;
    std::memset(&this->initial_parent_extaddr_, 0, sizeof(this->initial_parent_extaddr_));
    ESP_LOGI(TAG, "SO0 request; target=%s; initial parent unavailable", target_text.c_str());
  }

  this->prepared_ = true;
  return true;
}

void ThreadStockObserverComponent::start_observation_after_search_(otError err, bool current_parent_off_mode) {
  if (current_parent_off_mode) {
    ESP_LOGI(TAG, "SO1 current-parent-off action complete; starting stock search");
  }
  ESP_LOGI(TAG, "SO1 search started; status=%d", static_cast<int>(err));

  if (err != OT_ERROR_NONE) {
    ESP_LOGW(TAG, "SO6 failure; otThreadSearchForBetterParent status=%d", static_cast<int>(err));
    return;
  }

  this->active_ = true;
}

void ThreadStockObserverComponent::start_stock_search() {
  if (!this->prepare_stock_search_internal_(false)) {
    return;
  }

  auto lock = esphome::openthread::InstanceLock::try_acquire(0);
  if (!lock.has_value()) {
    ESP_LOGW(TAG, "SO6 failure; could not lock OpenThread instance for better-parent search");
    return;
  }

  otInstance *instance = lock->get_instance();

  otError err = otThreadSearchForBetterParent(instance);
  this->prepared_ = false;
  this->start_observation_after_search_(err, false);
}

void ThreadStockObserverComponent::prepare_stock_search() {
  this->prepare_stock_search_internal_(true);
}

void ThreadStockObserverComponent::start_prepared_stock_search() {
  if (!this->prepared_) {
    ESP_LOGW(TAG, "SO6 failure; start_prepared_stock_search called without prepared state");
    return;
  }

  auto lock = esphome::openthread::InstanceLock::try_acquire(0);
  if (!lock.has_value()) {
    ESP_LOGW(TAG, "SO6 failure; could not lock OpenThread instance for better-parent search");
    return;
  }

  otInstance *instance = lock->get_instance();
  otError err = otThreadSearchForBetterParent(instance);
  this->prepared_ = false;
  this->start_observation_after_search_(err, true);
}

void ThreadStockObserverComponent::parent_response_callback_(const otThreadParentResponseInfo *info, void *context) {
  if (context == nullptr) {
    return;
  }
  static_cast<ThreadStockObserverComponent *>(context)->handle_parent_response_(info);
}

void ThreadStockObserverComponent::handle_parent_response_(const otThreadParentResponseInfo *info) {
  if (info == nullptr || !this->active_) {
    return;
  }

  const uint32_t elapsed_ms = millis() - this->t0_ms_;
  const bool target_match = this->extaddr_matches_(info->mExtAddr, this->target_extaddr_);
  const std::string extaddr_text = this->extaddr_to_string_(info->mExtAddr);

  if (!this->logged_first_parent_response_) {
    this->logged_first_parent_response_ = true;
    ESP_LOGI(TAG,
             "SO2 parent response observed after %lu ms; ExtAddr %s RLOC16 0x%04x RSSI %d target_match=%s",
             static_cast<unsigned long>(elapsed_ms), extaddr_text.c_str(), info->mRloc16, info->mRssi,
             YESNO(target_match));
  } else if (this->log_parent_responses_) {
    ESP_LOGI(TAG,
             "SO2 parent response observed after %lu ms; ExtAddr %s RLOC16 0x%04x RSSI %d target_match=%s",
             static_cast<unsigned long>(elapsed_ms), extaddr_text.c_str(), info->mRloc16, info->mRssi,
             YESNO(target_match));
  }

  if (target_match && !this->logged_target_parent_response_) {
    this->logged_target_parent_response_ = true;
    ESP_LOGI(TAG,
             "SO3 target parent response observed after %lu ms; ExtAddr %s RLOC16 0x%04x RSSI %d",
             static_cast<unsigned long>(elapsed_ms), extaddr_text.c_str(), info->mRloc16, info->mRssi);
  }
}

bool ThreadStockObserverComponent::current_parent_matches_target_(otInstance *instance, otRouterInfo *out_parent) {
  otRouterInfo parent{};
  if (otThreadGetParentInfo(instance, &parent) != OT_ERROR_NONE) {
    return false;
  }
  if (out_parent != nullptr) {
    *out_parent = parent;
  }
  return this->extaddr_matches_(parent.mExtAddress, this->target_extaddr_);
}

void ThreadStockObserverComponent::loop() {
  if (!this->active_) {
    return;
  }

  auto lock = esphome::openthread::InstanceLock::try_acquire(0);
  if (!lock.has_value()) {
    return;
  }

  otInstance *instance = lock->get_instance();
  const uint32_t now = millis();
  const uint32_t elapsed_ms = now - this->t0_ms_;

  otRouterInfo parent{};
  const otError parent_err = otThreadGetParentInfo(instance, &parent);

  if (parent_err == OT_ERROR_NONE) {
    const std::string parent_extaddr = this->extaddr_to_string_(parent.mExtAddress);

    if (!this->logged_parent_changed_ && this->initial_parent_rloc16_ != 0xFFFE &&
        parent.mRloc16 != this->initial_parent_rloc16_) {
      this->logged_parent_changed_ = true;
      ESP_LOGI(TAG,
               "SO4 parent changed after %lu ms; previous RLOC16 0x%04x current RLOC16 0x%04x current ExtAddr %s",
               static_cast<unsigned long>(elapsed_ms), this->initial_parent_rloc16_, parent.mRloc16,
               parent_extaddr.c_str());
    }

    if (!this->logged_target_reached_ && this->extaddr_matches_(parent.mExtAddress, this->target_extaddr_)) {
      this->logged_target_reached_ = true;
      this->active_ = false;
      ESP_LOGI(TAG, "SO5 target parent reached after %lu ms; current parent RLOC16 0x%04x ExtAddr %s",
               static_cast<unsigned long>(elapsed_ms), parent.mRloc16, parent_extaddr.c_str());
      return;
    }
  }

  if (elapsed_ms >= this->observe_timeout_ms_) {
    this->active_ = false;

    if (parent_err == OT_ERROR_NONE) {
      ESP_LOGW(TAG,
               "SO6 timeout after %lu ms; target parent not reached; current parent RLOC16 0x%04x ExtAddr %s",
               static_cast<unsigned long>(elapsed_ms), parent.mRloc16,
               this->extaddr_to_string_(parent.mExtAddress).c_str());
    } else {
      ESP_LOGW(TAG, "SO6 timeout after %lu ms; target parent not reached; current parent unavailable",
               static_cast<unsigned long>(elapsed_ms));
    }
  }
}

bool ThreadStockObserverComponent::parse_extaddr_(const std::string &text, otExtAddress *out) const {
  if (out == nullptr) {
    return false;
  }

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
    hex[count++] = static_cast<char>(tolower(static_cast<unsigned char>(c)));
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

bool ThreadStockObserverComponent::extaddr_matches_(const otExtAddress &a, const otExtAddress &b) const {
  return std::memcmp(a.m8, b.m8, sizeof(a.m8)) == 0;
}

std::string ThreadStockObserverComponent::extaddr_to_string_(const otExtAddress &addr) const {
  static const char *const hex = "0123456789abcdef";
  std::string out;
  out.reserve(16);
  for (uint8_t byte : addr.m8) {
    out.push_back(hex[(byte >> 4) & 0x0f]);
    out.push_back(hex[byte & 0x0f]);
  }
  return out;
}

}  // namespace thread_stock_observer
}  // namespace esphome
