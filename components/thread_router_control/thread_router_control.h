#pragma once

#include "esphome/core/component.h"
#include "esphome/components/openthread/openthread.h"

#include <openthread/error.h>
#include <openthread/instance.h>
#include <openthread/ip6.h>
#include <openthread/link.h>
#include <openthread/thread.h>

#include <string>
#include <optional>

namespace esphome {
namespace thread_router_control {

class ThreadRouterControlComponent : public Component {
 public:
  void setup() override;
  void dump_config() override;
  void loop() override;

  void set_command_echo(bool command_echo) { this->command_echo_ = command_echo; }
  void set_default_off_timeout_ms(uint32_t default_off_timeout_ms) {
    this->default_off_timeout_ms_ = default_off_timeout_ms;
  }

 protected:
  static constexpr const char *TAG = "thread_router_ctl";

  bool command_echo_{true};
  bool stdin_ready_{false};
  bool auto_restore_pending_{false};
  uint32_t auto_restore_at_ms_{0};
  uint32_t default_off_timeout_ms_{60000};
  std::string rx_line_;

  void process_line_(const std::string &line);
  bool apply_thread_enabled_(bool enabled, const char *log_action);
  bool get_thread_enabled_(bool *enabled, otDeviceRole *role = nullptr);
  void arm_auto_restore_(uint32_t timeout_ms);
  void cancel_auto_restore_();
  static std::optional<uint32_t> parse_timeout_seconds_(const std::string &value);
  static std::string trim_(const std::string &value);
  static std::string lowercase_(const std::string &value);
  static const char *role_to_string_(otDeviceRole role);
  static const char *error_to_string_(otError error);
};

}  // namespace thread_router_control
}  // namespace esphome
