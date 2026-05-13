#include "thread_router_control.h"

#include <cerrno>
#include <cctype>
#include <cstdint>
#include <cstdio>
#include <cstring>
#include <driver/uart.h>

namespace esphome {
namespace thread_router_control {

void ThreadRouterControlComponent::setup() {
  this->stdin_ready_ = true;
  ESP_LOGI(TAG, "USB_CTL ready on UART0; commands: 'thread off <seconds>', 'thread on', 'thread state'");
}

void ThreadRouterControlComponent::dump_config() {
  ESP_LOGCONFIG(TAG, "Thread router control:");
  ESP_LOGCONFIG(TAG, "  usb serial command control: %s", YESNO(this->stdin_ready_));
  ESP_LOGCONFIG(TAG, "  command echo: %s", YESNO(this->command_echo_));
  ESP_LOGCONFIG(TAG, "  default off timeout: %u ms", static_cast<unsigned>(this->default_off_timeout_ms_));
}

void ThreadRouterControlComponent::loop() {
  if (this->auto_restore_pending_ && static_cast<int32_t>(millis() - this->auto_restore_at_ms_) >= 0) {
    this->auto_restore_pending_ = false;
    ESP_LOGI(TAG, "USB_CTL failsafe re-enable fired");
    this->apply_thread_enabled_(true, "thread on");
  }

  if (!this->stdin_ready_) {
    return;
  }

  size_t buffered = 0;
  if (uart_get_buffered_data_len(UART_NUM_0, &buffered) != ESP_OK || buffered == 0) {
    return;
  }

  uint8_t buffer[64];
  while (buffered > 0) {
    const int to_read = static_cast<int>(buffered > sizeof(buffer) ? sizeof(buffer) : buffered);
    const int count = uart_read_bytes(UART_NUM_0, buffer, to_read, 0);
    if (count <= 0) {
      break;
    }
    buffered -= static_cast<size_t>(count);
    for (int i = 0; i < count; i++) {
      const char ch = buffer[i];
      if (ch == '\r' || ch == '\n') {
        if (!this->rx_line_.empty()) {
          this->process_line_(this->rx_line_);
          this->rx_line_.clear();
        }
        continue;
      }
      if (std::isprint(static_cast<unsigned char>(ch))) {
        this->rx_line_.push_back(ch);
        if (this->rx_line_.size() > 120) {
          this->rx_line_.erase(0, this->rx_line_.size() - 120);
        }
      }
    }
  }
}

void ThreadRouterControlComponent::process_line_(const std::string &line) {
  const std::string trimmed = trim_(line);
  if (trimmed.empty()) {
    return;
  }

  const std::string cmd = lowercase_(trimmed);
  if (this->command_echo_) {
    ESP_LOGI(TAG, "USB_CTL rx command=%s", trimmed.c_str());
  }

  if (cmd == "thread on" || cmd == "thread enable") {
    this->cancel_auto_restore_();
    ESP_LOGI(TAG, "USB_CTL thread on requested");
    this->apply_thread_enabled_(true, "thread on");
    return;
  }

  if (cmd == "thread state" || cmd == "thread status") {
    bool enabled = false;
    otDeviceRole role = OT_DEVICE_ROLE_DISABLED;
    if (!this->get_thread_enabled_(&enabled, &role)) {
      ESP_LOGW(TAG, "USB_CTL thread state lock_unavailable");
      return;
    }
    auto lock = esphome::openthread::InstanceLock::try_acquire(100);
    if (!lock.has_value()) {
      ESP_LOGI(TAG, "USB_CTL thread state enabled=%s role=%s", enabled ? "true" : "false", role_to_string_(role));
      return;
    }
    otInstance *instance = lock->get_instance();
    ESP_LOGI(TAG, "USB_CTL thread state enabled=%s role=%s ip6=%s link=%s",
             enabled ? "true" : "false", role_to_string_(role),
             otIp6IsEnabled(instance) ? "true" : "false",
             otLinkIsEnabled(instance) ? "true" : "false");
    return;
  }

  constexpr const char prefix[] = "thread off";
  if (cmd.rfind(prefix, 0) == 0) {
    std::string arg = trim_(trimmed.substr(std::strlen(prefix)));
    uint32_t timeout_ms = this->default_off_timeout_ms_;
    if (!arg.empty()) {
      auto seconds = parse_timeout_seconds_(arg);
      if (!seconds.has_value()) {
        ESP_LOGW(TAG, "USB_CTL invalid thread off timeout arg=%s", arg.c_str());
        return;
      }
      timeout_ms = *seconds * 1000U;
    }
    ESP_LOGI(TAG, "USB_CTL thread off requested timeout=%lus", static_cast<unsigned long>(timeout_ms / 1000U));
    if (this->apply_thread_enabled_(false, "thread off")) {
      this->arm_auto_restore_(timeout_ms);
    }
    return;
  }

  constexpr const char suspend_prefix[] = "thread suspend ";
  if (cmd.rfind(suspend_prefix, 0) == 0) {
    std::string arg = trim_(trimmed.substr(std::strlen(suspend_prefix)));
    auto seconds = parse_timeout_seconds_(arg);
    if (!seconds.has_value()) {
      ESP_LOGW(TAG, "USB_CTL invalid thread suspend arg=%s", arg.c_str());
      return;
    }
    const uint32_t timeout_ms = *seconds * 1000U;
    ESP_LOGI(TAG, "USB_CTL thread off requested timeout=%lus", static_cast<unsigned long>(timeout_ms / 1000U));
    if (this->apply_thread_enabled_(false, "thread off")) {
      this->arm_auto_restore_(timeout_ms);
    }
    return;
  }

  ESP_LOGW(TAG, "USB_CTL unknown command=%s", trimmed.c_str());
}

bool ThreadRouterControlComponent::apply_thread_enabled_(bool enabled, const char *log_action) {
  auto lock = esphome::openthread::InstanceLock::try_acquire(100);
  if (!lock.has_value()) {
    ESP_LOGW(TAG, "USB_CTL could not acquire OpenThread lock");
    return false;
  }

  otInstance *instance = lock->get_instance();
  otError err = OT_ERROR_NONE;

  if (enabled) {
    err = otLinkSetEnabled(instance, true);
    if (err == OT_ERROR_NONE) {
      err = otIp6SetEnabled(instance, true);
    }
    if (err == OT_ERROR_NONE) {
      err = otThreadSetEnabled(instance, true);
    }
  } else {
    err = otThreadSetEnabled(instance, false);
    if (err == OT_ERROR_NONE) {
      err = otIp6SetEnabled(instance, false);
    }
    if (err == OT_ERROR_NONE) {
      err = otLinkSetEnabled(instance, false);
    }
  }

  const bool ip6_enabled = otIp6IsEnabled(instance);
  const bool link_enabled = otLinkIsEnabled(instance);
  const otDeviceRole role = otThreadGetDeviceRole(instance);
  const bool enabled_effective = ip6_enabled && link_enabled && role != OT_DEVICE_ROLE_DISABLED;

  if (enabled && err == OT_ERROR_INVALID_STATE && enabled_effective) {
    ESP_LOGI(TAG,
             "USB_CTL %s -> %s (treated as success; stack already enabled: ip6=%s link=%s role=%s)",
             log_action, error_to_string_(err), ip6_enabled ? "true" : "false",
             link_enabled ? "true" : "false", role_to_string_(role));
    return true;
  }

  ESP_LOGI(TAG, "USB_CTL %s -> %s (ip6=%s link=%s role=%s)", log_action, error_to_string_(err),
           ip6_enabled ? "true" : "false", link_enabled ? "true" : "false", role_to_string_(role));
  return err == OT_ERROR_NONE;
}

bool ThreadRouterControlComponent::get_thread_enabled_(bool *enabled, otDeviceRole *role) {
  auto lock = esphome::openthread::InstanceLock::try_acquire(100);
  if (!lock.has_value()) {
    return false;
  }

  otInstance *instance = lock->get_instance();
  const bool ip6_enabled = otIp6IsEnabled(instance);
  const bool link_enabled = otLinkIsEnabled(instance);
  otDeviceRole current_role = otThreadGetDeviceRole(instance);
  if (!ip6_enabled || !link_enabled) {
    current_role = OT_DEVICE_ROLE_DISABLED;
  }
  if (enabled != nullptr) {
    *enabled = ip6_enabled && link_enabled && current_role != OT_DEVICE_ROLE_DISABLED;
  }
  if (role != nullptr) {
    *role = current_role;
  }
  return true;
}

void ThreadRouterControlComponent::arm_auto_restore_(uint32_t timeout_ms) {
  this->auto_restore_pending_ = true;
  this->auto_restore_at_ms_ = millis() + timeout_ms;
}

void ThreadRouterControlComponent::cancel_auto_restore_() {
  this->auto_restore_pending_ = false;
}

std::optional<uint32_t> ThreadRouterControlComponent::parse_timeout_seconds_(const std::string &value) {
  if (value.empty()) {
    return std::nullopt;
  }
  char *end = nullptr;
  errno = 0;
  const unsigned long parsed = std::strtoul(value.c_str(), &end, 10);
  const std::string trailing = trim_(std::string(end != nullptr ? end : ""));
  if (errno != 0 || end == value.c_str() || !trailing.empty()) {
    return std::nullopt;
  }
  return static_cast<uint32_t>(parsed);
}

std::string ThreadRouterControlComponent::trim_(const std::string &value) {
  size_t start = 0;
  while (start < value.size() && std::isspace(static_cast<unsigned char>(value[start]))) {
    start++;
  }
  size_t end = value.size();
  while (end > start && std::isspace(static_cast<unsigned char>(value[end - 1]))) {
    end--;
  }
  return value.substr(start, end - start);
}

std::string ThreadRouterControlComponent::lowercase_(const std::string &value) {
  std::string out = value;
  for (char &ch : out) {
    ch = static_cast<char>(std::tolower(static_cast<unsigned char>(ch)));
  }
  return out;
}

const char *ThreadRouterControlComponent::role_to_string_(otDeviceRole role) {
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
    default:
      return "unknown";
  }
}

const char *ThreadRouterControlComponent::error_to_string_(otError error) {
  if (error == OT_ERROR_NONE) {
    return "OT_ERROR_NONE";
  }
  return otThreadErrorToString(error);
}

}  // namespace thread_router_control
}  // namespace esphome
