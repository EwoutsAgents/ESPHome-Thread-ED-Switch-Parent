#pragma once

#include "esphome/core/component.h"
#include "esphome/core/hal.h"
#include "esphome/core/log.h"
#include "esphome/components/openthread/openthread.h"

#include <openthread/error.h>
#include <openthread/instance.h>
#include <openthread/thread.h>

#include <cstdint>
#include <cstring>
#include <string>

extern "C" {

typedef void (*thread_stock_observer_parent_response_callback_t)(
    const otThreadParentResponseInfo *aInfo,
    void *aContext
);

void thread_stock_observer_ot_register_parent_response_callback(
    thread_stock_observer_parent_response_callback_t aCallback,
    void *aContext
) __attribute__((weak));

}

namespace esphome {
namespace thread_stock_observer {

class ThreadStockObserverComponent : public Component {
 public:
  void setup() override;
  void loop() override;
  void dump_config() override;

  void set_target_parent_extaddr(const std::string &value);
  void set_observe_timeout(uint32_t timeout_ms) { this->observe_timeout_ms_ = timeout_ms; }
  void set_log_parent_responses(bool enabled) { this->log_parent_responses_ = enabled; }

  void start_stock_search();
  void prepare_stock_search();
  void start_prepared_stock_search();

 protected:
  static constexpr const char *TAG = "thread_stock_observer";

  static void parent_response_callback_(const otThreadParentResponseInfo *info, void *context);
  void handle_parent_response_(const otThreadParentResponseInfo *info);

  bool parse_extaddr_(const std::string &text, otExtAddress *out) const;
  bool extaddr_matches_(const otExtAddress &a, const otExtAddress &b) const;
  std::string extaddr_to_string_(const otExtAddress &addr) const;
  bool current_parent_matches_target_(otInstance *instance, otRouterInfo *out_parent);
  bool current_parent_matches_initial_(const otRouterInfo &parent) const;
  const char *timeout_classification_(bool parent_available, const otRouterInfo &parent) const;

  void reset_run_state_();
  bool prepare_stock_search_internal_(bool current_parent_off_mode);
  void start_observation_after_search_(otError err, bool current_parent_off_mode);

  bool active_{false};
  bool callback_registered_{false};
  bool target_configured_{false};
  bool log_parent_responses_{true};

  uint32_t t0_ms_{0};
  uint32_t observe_timeout_ms_{16000};

  otExtAddress target_extaddr_{};
  uint16_t initial_parent_rloc16_{0xFFFE};
  otExtAddress initial_parent_extaddr_{};

  bool logged_first_parent_response_{false};
  bool logged_target_parent_response_{false};
  bool logged_parent_changed_{false};
  bool logged_target_reached_{false};
  bool logged_post_target_non_target_response_{false};
  bool logged_post_target_repeat_response_{false};
  bool prepared_{false};

  uint32_t so3_ms_{0};
  uint32_t last_post_so3_status_log_ms_{0};
  uint32_t total_parent_response_count_{0};
  uint32_t total_target_parent_response_count_{0};
  uint32_t post_so3_parent_response_count_{0};
  uint32_t post_so3_target_parent_response_count_{0};
  uint32_t post_so3_non_target_parent_response_count_{0};
};

}  // namespace thread_stock_observer
}  // namespace esphome
