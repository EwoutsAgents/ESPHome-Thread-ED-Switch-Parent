#pragma once

#include "esphome/core/component.h"
#include "esphome/components/openthread/openthread.h"

#include <openthread/error.h>
#include <openthread/instance.h>
#include <openthread/ip6.h>
#include <openthread/thread.h>

#include <string>

namespace esphome {
namespace thread_router_control {

class ThreadRouterControlComponent : public Component {
 public:
  void setup() override;
  void dump_config() override;
  void loop() override;

  void set_command_echo(bool command_echo) { this->command_echo_ = command_echo; }

 protected:
  static constexpr const char *TAG = "thread_router_ctl";

  bool command_echo_{true};
  bool stdin_ready_{false};
  bool auto_restore_pending_{false};
  uint32_t auto_restore_at_ms_{0};
  std::string rx_line_;

  void process_line_(const std::string &line);
  void apply_thread_enabled_(bool enabled, const char *reason);
  bool get_thread_enabled_(bool *enabled, otDeviceRole *role = nullptr);
  static std::string trim_(const std::string &value);
  static std::string lowercase_(const std::string &value);
  static const char *role_to_string_(otDeviceRole role);
};

}  // namespace thread_router_control
}  // namespace esphome
