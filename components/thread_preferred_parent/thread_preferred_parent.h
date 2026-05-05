#pragma once

#include "esphome/core/component.h"
#include "esphome/core/hal.h"
#include "esphome/core/log.h"
#include "esphome/components/openthread/openthread.h"

#include <openthread/error.h>
#include <openthread/instance.h>
#include <openthread/thread.h>

#include <cstdio>
#include <cstdint>
#include <cstring>
#include <string>

// These symbols are intentionally weak. The ESPHome component can compile
// against an unpatched OpenThread build, but it will log a clear runtime error
// until the OpenThread selected-parent hook is linked in.
extern "C" {

// Callback type used by the OpenThread patch to publish every MLE Parent Response
// to the ESPHome component.
typedef void (*thread_preferred_parent_parent_response_callback_t)(
    const otThreadParentResponseInfo *aInfo,
    void *aContext
);

void thread_preferred_parent_ot_register_parent_response_callback(
    thread_preferred_parent_parent_response_callback_t aCallback,
    void *aContext
) __attribute__((weak));

// Preferred symbol exported by scripts/apply-openthread-selected-parent-hook.py.
bool thread_preferred_parent_ot_request_selected_parent_attach(
    otInstance *aInstance,
    const otExtAddress *aPreferredExtAddress
) __attribute__((weak));

// Compatibility with ESPHome-biparental-ED if that patch is already applied.
bool biparental_ot_request_selected_parent_attach(
    otInstance *aInstance,
    const otExtAddress *aPreferredExtAddress
) __attribute__((weak));

// Optional backwards-compatible symbols from the earlier response-filtering patch.
otError otThreadSetPreferredParentRloc16(otInstance *aInstance, uint16_t aRloc16) __attribute__((weak));
otError otThreadSetPreferredParentExtAddress(otInstance *aInstance, const otExtAddress *aExtAddress) __attribute__((weak));
void otThreadClearPreferredParent(otInstance *aInstance) __attribute__((weak));
void otThreadClearPreferredParentRloc16(otInstance *aInstance) __attribute__((weak));
otError otThreadSearchForPreferredParentRloc16(otInstance *aInstance, uint16_t aRloc16) __attribute__((weak));
otError otThreadSearchForPreferredParentExtAddress(otInstance *aInstance, const otExtAddress *aExtAddress) __attribute__((weak));
otError otThreadSearchForPreferredParent(otInstance *aInstance, uint16_t aRloc16) __attribute__((weak));
}

namespace esphome {
namespace thread_preferred_parent {

class ThreadPreferredParentComponent : public Component {
 public:
  void setup() override;
  void loop() override;
  void dump_config() override;

  void set_parent_rloc16(uint16_t rloc16);
  void set_parent_rloc(uint16_t rloc16) { this->set_parent_rloc16(rloc16); }
  bool set_parent_extaddr(const std::string &extaddr);
  bool set_parent_extaddr(const char *extaddr) { return this->set_parent_extaddr(std::string(extaddr)); }

  void set_max_attempts(uint8_t attempts) { this->max_attempts_ = attempts; }
  void set_retry_interval(uint32_t retry_interval_ms) { this->retry_interval_ms_ = retry_interval_ms; }
  void set_require_selected_parent_hook(bool required) { this->require_selected_parent_hook_ = required; }
  void set_log_parent_responses(bool enabled) { this->log_parent_responses_ = enabled; }

  // Call from a Home Assistant/ESPHome template button using the configured target.
  void request_switch();

  // Call from lambdas if the target is supplied dynamically.
  void request_switch(uint16_t rloc16);
  void request_switch(const std::string &extaddr);
  void request_switch(const char *extaddr) { this->request_switch(std::string(extaddr)); }

  void clear_target();

 protected:
  enum class TargetType : uint8_t {
    NONE,
    RLOC16,
    EXTADDR,
  };

  enum class Status : uint8_t {
    IDLE,
    WAITING,
    SUCCESS,
    FAILED,
    API_MISSING,
    NOT_CHILD,
    BUSY,
    INVALID_TARGET,
    RLOC_UNRESOLVED,
  };

  static const char *status_to_string_(Status status);
  static const char *target_type_to_string_(TargetType type);
  static const char *ot_error_to_string_(otError error);
  static int hex_to_nibble_(char c);
  static void parent_response_callback_(const otThreadParentResponseInfo *info, void *context);

  bool current_parent_matches_(otInstance *instance) const;
  bool is_child_(otInstance *instance) const;
  bool parse_extaddr_(const std::string &text, otExtAddress *out) const;
  bool extaddr_matches_(const otExtAddress &a, const otExtAddress &b) const;
  bool resolve_rloc16_to_extaddr_(otInstance *instance, uint16_t rloc16, otExtAddress *out) const;
  bool request_selected_parent_attach_(otInstance *instance, const otExtAddress &extaddr) const;
  bool selected_parent_hook_available_() const;
  std::string extaddr_to_string_(const otExtAddress &addr) const;
  std::string target_to_string_() const;
  otError start_preferred_parent_search_(otInstance *instance);
  void clear_preferred_parent_in_ot_(otInstance *instance);
  void begin_switch_();
  void set_status_(Status status);
  void handle_parent_response_(const otThreadParentResponseInfo *info);

  TargetType target_type_{TargetType::NONE};
  uint16_t target_rloc16_{0xFFFE};
  otExtAddress target_extaddr_{};
  uint8_t max_attempts_{5};
  uint8_t attempts_{0};
  uint32_t retry_interval_ms_{8000};
  uint32_t next_attempt_ms_{0};
  bool active_{false};
  bool require_selected_parent_hook_{true};
  bool log_parent_responses_{true};
  bool parent_response_callback_registered_{false};
  uint32_t parent_response_count_{0};
  Status status_{Status::IDLE};
};

}  // namespace thread_preferred_parent
}  // namespace esphome
