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
  ESP_LOGI(TAG, "THREAD_CTL ready on UART0; commands: 'thread on', 'thread off', 'thread status', 'thread suspend <ms>'");
}

void ThreadRouterControlComponent::dump_config() {
  ESP_LOGCONFIG(TAG, "Thread router control:");
  ESP_LOGCONFIG(TAG, "  stdin command control: %s", YESNO(this->stdin_ready_));
  ESP_LOGCONFIG(TAG, "  command echo: %s", YESNO(this->command_echo_));
}

void ThreadRouterControlComponent::loop() {
  if (this->auto_restore_pending_ && static_cast<int32_t>(millis() - this->auto_restore_at_ms_) >= 0) {
    this->auto_restore_pending_ = false;
    this->apply_thread_enabled_(true, "auto_restore");
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
    ESP_LOGI(TAG, "THREAD_CTL rx command=%s", trimmed.c_str());
  }

  if (cmd == "thread on" || cmd == "thread enable") {
    this->auto_restore_pending_ = false;
    this->apply_thread_enabled_(true, "command_on");
    return;
  }

  if (cmd == "thread off" || cmd == "thread disable") {
    this->auto_restore_pending_ = false;
    this->apply_thread_enabled_(false, "command_off");
    return;
  }

  if (cmd == "thread status") {
    bool enabled = false;
    otDeviceRole role = OT_DEVICE_ROLE_DISABLED;
    if (!this->get_thread_enabled_(&enabled, &role)) {
      ESP_LOGW(TAG, "THREAD_CTL status result=lock_unavailable");
      return;
    }
    ESP_LOGI(TAG, "THREAD_CTL status thread_enabled=%s role=%s", YESNO(enabled), role_to_string_(role));
    return;
  }

  constexpr const char prefix[] = "thread suspend ";
  if (cmd.rfind(prefix, 0) == 0) {
    const char *arg = trimmed.c_str() + std::strlen(prefix);
    char *end = nullptr;
    errno = 0;
    const unsigned long duration_ms = std::strtoul(arg, &end, 10);
    const std::string trailing = trim_(std::string(end != nullptr ? end : ""));
    if (errno != 0 || end == arg || !trailing.empty()) {
      ESP_LOGW(TAG, "THREAD_CTL ack result=invalid_argument command=%s", trimmed.c_str());
      return;
    }
    this->apply_thread_enabled_(false, "command_suspend");
    this->auto_restore_pending_ = true;
    this->auto_restore_at_ms_ = millis() + static_cast<uint32_t>(duration_ms);
    ESP_LOGI(TAG, "THREAD_CTL ack result=ok command=suspend duration_ms=%lu", duration_ms);
    return;
  }

  ESP_LOGW(TAG, "THREAD_CTL ack result=unknown_command command=%s", trimmed.c_str());
}

void ThreadRouterControlComponent::apply_thread_enabled_(bool enabled, const char *reason) {
  auto lock = esphome::openthread::InstanceLock::try_acquire(0);
  if (!lock.has_value()) {
    ESP_LOGW(TAG, "THREAD_CTL ack result=lock_unavailable reason=%s requested=%s", reason, YESNO(enabled));
    return;
  }

  otInstance *instance = lock->get_instance();
  otError err = OT_ERROR_NONE;

  if (enabled) {
    err = otIp6SetEnabled(instance, true);
    if (err == OT_ERROR_NONE) {
      err = otThreadSetEnabled(instance, true);
    }
  } else {
    err = otThreadSetEnabled(instance, false);
  }

  bool active = false;
  otDeviceRole role = OT_DEVICE_ROLE_DISABLED;
  this->get_thread_enabled_(&active, &role);

  ESP_LOGI(TAG,
           "THREAD_CTL ack result=%s reason=%s requested=%s thread_enabled=%s role=%s err=%d",
           err == OT_ERROR_NONE ? "ok" : "error", reason, YESNO(enabled), YESNO(active), role_to_string_(role),
           static_cast<int>(err));
}

bool ThreadRouterControlComponent::get_thread_enabled_(bool *enabled, otDeviceRole *role) {
  auto lock = esphome::openthread::InstanceLock::try_acquire(0);
  if (!lock.has_value()) {
    return false;
  }

  otInstance *instance = lock->get_instance();
  const otDeviceRole current_role = otThreadGetDeviceRole(instance);
  if (enabled != nullptr) {
    *enabled = current_role != OT_DEVICE_ROLE_DISABLED;
  }
  if (role != nullptr) {
    *role = current_role;
  }
  return true;
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

}  // namespace thread_router_control
}  // namespace esphome
