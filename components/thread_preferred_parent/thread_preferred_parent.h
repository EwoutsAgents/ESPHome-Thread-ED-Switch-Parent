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

extern "C" {

/**
 * Function pointer type used to receive parsed Parent Response callbacks.
 *
 * @param aInfo Parsed Parent Response information supplied by OpenThread.
 * @param aContext Opaque callback context provided at registration time.
 */
typedef void (*thread_preferred_parent_parent_response_callback_t)(
    const otThreadParentResponseInfo *aInfo,
    void *aContext
);

/**
 * Register a callback for Parent Response notifications emitted by the patch.
 *
 * @param aCallback Callback invoked for each parsed Parent Response.
 * @param aContext Opaque context forwarded back to `aCallback`.
 */
void thread_preferred_parent_ot_register_parent_response_callback(
    thread_preferred_parent_parent_response_callback_t aCallback,
    void *aContext
) __attribute__((weak));

/**
 * Start a non-disruptive multicast Parent Request discovery pass.
 *
 * @param aInstance Active OpenThread instance.
 * @return OpenThread status describing whether discovery started successfully.
 */
otError thread_preferred_parent_ot_start_parent_discovery(otInstance *aInstance) __attribute__((weak));

/**
 * Start a non-disruptive unicast Parent Request discovery pass.
 *
 * @param aInstance Active OpenThread instance.
 * @param aPreferredExtAddress Extended address of the preferred parent target.
 * @return OpenThread status describing whether discovery started successfully.
 */
otError thread_preferred_parent_ot_start_parent_discovery_unicast(
    otInstance *aInstance,
    const otExtAddress *aPreferredExtAddress
) __attribute__((weak));

/**
 * Request a targeted selected-parent attach through the preferred hook symbol.
 *
 * @param aInstance Active OpenThread instance.
 * @param aPreferredExtAddress Extended address of the preferred parent target.
 * @return `true` when the attach request was accepted.
 */
bool thread_preferred_parent_ot_request_selected_parent_attach(
    otInstance *aInstance,
    const otExtAddress *aPreferredExtAddress
) __attribute__((weak));

/**
 * Request a targeted selected-parent attach through the compatibility hook.
 *
 * @param aInstance Active OpenThread instance.
 * @param aPreferredExtAddress Extended address of the preferred parent target.
 * @return `true` when the attach request was accepted.
 */
bool biparental_ot_request_selected_parent_attach(
    otInstance *aInstance,
    const otExtAddress *aPreferredExtAddress
) __attribute__((weak));

/**
 * Store a preferred parent RLOC16 inside OpenThread.
 *
 * @param aInstance Active OpenThread instance.
 * @param aRloc16 Preferred parent RLOC16.
 * @return OpenThread status describing whether the value was accepted.
 */
otError otThreadSetPreferredParentRloc16(otInstance *aInstance, uint16_t aRloc16) __attribute__((weak));

/**
 * Store a preferred parent extended address inside OpenThread.
 *
 * @param aInstance Active OpenThread instance.
 * @param aExtAddress Preferred parent extended address.
 * @return OpenThread status describing whether the value was accepted.
 */
otError otThreadSetPreferredParentExtAddress(otInstance *aInstance, const otExtAddress *aExtAddress) __attribute__((weak));

/**
 * Clear any stored preferred-parent hint inside OpenThread.
 *
 * @param aInstance Active OpenThread instance.
 */
void otThreadClearPreferredParent(otInstance *aInstance) __attribute__((weak));

/**
 * Clear any stored preferred-parent RLOC16 inside OpenThread.
 *
 * @param aInstance Active OpenThread instance.
 */
void otThreadClearPreferredParentRloc16(otInstance *aInstance) __attribute__((weak));

/**
 * Ask OpenThread to search for a preferred parent by RLOC16.
 *
 * @param aInstance Active OpenThread instance.
 * @param aRloc16 Preferred parent RLOC16.
 * @return OpenThread status describing whether the search started successfully.
 */
otError otThreadSearchForPreferredParentRloc16(otInstance *aInstance, uint16_t aRloc16) __attribute__((weak));

/**
 * Ask OpenThread to search for a preferred parent by extended address.
 *
 * @param aInstance Active OpenThread instance.
 * @param aExtAddress Preferred parent extended address.
 * @return OpenThread status describing whether the search started successfully.
 */
otError otThreadSearchForPreferredParentExtAddress(otInstance *aInstance, const otExtAddress *aExtAddress) __attribute__((weak));

/**
 * Ask OpenThread to search for a preferred parent through the legacy API.
 *
 * @param aInstance Active OpenThread instance.
 * @param aRloc16 Preferred parent RLOC16.
 * @return OpenThread status describing whether the search started successfully.
 */
otError otThreadSearchForPreferredParent(otInstance *aInstance, uint16_t aRloc16) __attribute__((weak));
}

namespace esphome {
namespace thread_preferred_parent {

// Coordinates a two-phase preferred-parent handoff:
//   1. discover candidate Parent Responses without detaching first
//   2. start a targeted selected-parent attach once the requested parent is seen
class ThreadPreferredParentComponent : public Component {
 public:
  /**
   * Initialize the component and register optional OpenThread hooks.
   */
  void setup() override;

  /**
   * Advance the preferred-parent discovery and attach state machine.
   */
  void loop() override;

  /**
   * Log the current component configuration and runtime capabilities.
   */
  void dump_config() override;

  /**
   * Set the preferred parent target by RLOC16.
   *
   * @param rloc16 Preferred parent RLOC16.
   */
  void set_parent_rloc16(uint16_t rloc16);

  /**
   * Parse and set the preferred parent target from an RLOC16 string.
   *
   * @param rloc16 Preferred parent RLOC16 in hexadecimal string form.
   * @return `true` when the target was accepted or cleared successfully.
   */
  bool set_parent_rloc16(const std::string &rloc16);

  /**
   * Parse and set the preferred parent target from a C-string RLOC16.
   *
   * @param rloc16 Preferred parent RLOC16 in hexadecimal string form.
   * @return `true` when the target was accepted or cleared successfully.
   */
  bool set_parent_rloc16(const char *rloc16) { return this->set_parent_rloc16(std::string(rloc16)); }

  /**
   * Alias for `set_parent_rloc16(uint16_t)`.
   *
   * @param rloc16 Preferred parent RLOC16.
   */
  void set_parent_rloc(uint16_t rloc16) { this->set_parent_rloc16(rloc16); }

  /**
   * Alias for `set_parent_rloc16(const std::string &)`.
   *
   * @param rloc16 Preferred parent RLOC16 in hexadecimal string form.
   * @return `true` when the target was accepted or cleared successfully.
   */
  bool set_parent_rloc(const std::string &rloc16) { return this->set_parent_rloc16(rloc16); }

  /**
   * Alias for `set_parent_rloc16(const char *)`.
   *
   * @param rloc16 Preferred parent RLOC16 in hexadecimal string form.
   * @return `true` when the target was accepted or cleared successfully.
   */
  bool set_parent_rloc(const char *rloc16) { return this->set_parent_rloc16(std::string(rloc16)); }

  /**
   * Parse and set the preferred parent target from an extended address string.
   *
   * @param extaddr Preferred parent extended address.
   * @return `true` when the target was accepted successfully.
   */
  bool set_parent_extaddr(const std::string &extaddr);

  /**
   * Parse and set the preferred parent target from a C-string extended address.
   *
   * @param extaddr Preferred parent extended address.
   * @return `true` when the target was accepted successfully.
   */
  bool set_parent_extaddr(const char *extaddr) { return this->set_parent_extaddr(std::string(extaddr)); }

  /**
   * Set the maximum number of discovery attempts before failure.
   *
   * @param attempts Maximum number of attempts.
   */
  void set_max_attempts(uint8_t attempts) { this->max_attempts_ = attempts; }

  /**
   * Set the delay between discovery attempts.
   *
   * @param retry_interval_ms Retry interval in milliseconds.
   */
  void set_retry_interval(uint32_t retry_interval_ms) { this->retry_interval_ms_ = retry_interval_ms; }

  /**
   * Set the timeout for the selected-parent attach phase.
   *
   * @param selected_attach_timeout_ms Attach timeout in milliseconds.
   */
  void set_selected_attach_timeout(uint32_t selected_attach_timeout_ms) { this->selected_attach_timeout_ms_ = selected_attach_timeout_ms; }

  /**
   * Set whether the dedicated selected-parent hook is required.
   *
   * @param required `true` to reject fallback APIs when the hook is missing.
   */
  void set_require_selected_parent_hook(bool required) { this->require_selected_parent_hook_ = required; }

  /**
   * Enable or disable Parent Response logging.
   *
   * @param enabled `true` to log Parent Responses.
   */
  void set_log_parent_responses(bool enabled) { this->log_parent_responses_ = enabled; }

  /**
   * Enable or disable unicast Parent Request discovery.
   *
   * @param enabled `true` to prefer unicast discovery.
   */
  void set_parent_request_unicast(bool enabled) { this->parent_request_unicast_ = enabled; }

  /**
   * Enable or disable early attach once the target is observed.
   *
   * @param enabled `true` to arm the early-attach path.
   */
  void set_early_attach_on_target(bool enabled) { this->early_attach_on_target_ = enabled; }

  /**
   * Set the debounce delay used before early attach begins.
   *
   * @param early_attach_delay_ms Early-attach delay in milliseconds.
   */
  void set_early_attach_delay(uint32_t early_attach_delay_ms) { this->early_attach_delay_ms_ = early_attach_delay_ms; }

  /**
   * Start a preferred-parent switch using the currently configured target.
   */
  void request_switch();

  /**
   * Set an RLOC16 target and immediately request a parent switch.
   *
   * @param rloc16 Preferred parent RLOC16.
   */
  void request_switch(uint16_t rloc16);

  /**
   * Set an extended-address target and immediately request a parent switch.
   *
   * @param extaddr Preferred parent extended address.
   */
  void request_switch(const std::string &extaddr);

  /**
   * Set a C-string extended-address target and immediately request a parent switch.
   *
   * @param extaddr Preferred parent extended address.
   */
  void request_switch(const char *extaddr) { this->request_switch(std::string(extaddr)); }

  /**
   * Clear the configured target and return the component to its idle state.
   */
  void clear_target();

  /**
   * Start a discovery-only probe for the configured target.
   *
   * The probe sends a non-disruptive Parent Request and records Parent
   * Responses, but it never proceeds into selected-parent attach.
   */
  void start_parent_response_probe();

  /// `true` while a discovery-only probe is still running.
  bool probe_active() const { return this->probe_active_; }

  /// `true` once the latest discovery-only probe finished.
  bool probe_completed() const { return this->probe_completed_; }

  /// Number of Parent Responses captured during the latest probe.
  uint32_t probe_parent_response_count() const { return this->probe_parent_response_count_; }

  /// Number of target-matching Parent Responses captured during the latest probe.
  uint32_t probe_target_parent_response_count() const { return this->probe_target_parent_response_count_; }

  /// Best-effort non-target responder captured during the latest probe.
  std::string probe_non_target_extaddr() const { return this->extaddr_to_string_(this->probe_non_target_extaddr_); }

 protected:
  // How the preferred parent is identified by the user configuration.
  enum class TargetType : uint8_t {
    NONE,
    RLOC16,
    EXTADDR,
  };

  // High-level state for a single preferred-parent switch attempt.
  enum class SwitchPhase : uint8_t {
    IDLE,
    DISCOVERING,
    ATTACHING,
  };

  // User-visible status values surfaced through logging and dump_config().
  enum class Status : uint8_t {
    IDLE,
    DISCOVERING,
    ATTACHING,
    WAITING,
    SUCCESS,
    FAILED,
    API_MISSING,
    NOT_CHILD,
    BUSY,
    INVALID_TARGET,
    RLOC_UNRESOLVED,
  };

  // Controls whether replay logging shows all buffered Parent Responses or only
  // the responses that matched the configured target.
  enum class ReplayMode : uint8_t {
    INFO_ALL,
    INFO_TARGET_ONLY,
  };

  // Small ring-buffer entry used to preserve recent Parent Responses for later
  // replay when a discovery or attach attempt succeeds or fails.
  struct BufferedParentResponse {
    bool valid{false};
    uint32_t sequence{0};
    uint32_t timestamp_ms{0};
    otThreadParentResponseInfo info{};
    bool target_match{false};
  };

  /**
   * Convert a component status to a log-friendly string.
   *
   * @param status Component status to format.
   * @return String name for `status`.
   */
  static const char *status_to_string_(Status status);

  /**
   * Convert an internal switch phase to a log-friendly string.
   *
   * @param phase Switch phase to format.
   * @return String name for `phase`.
   */
  static const char *phase_to_string_(SwitchPhase phase);

  /**
   * Convert a target type to a log-friendly string.
   *
   * @param type Target type to format.
   * @return String name for `type`.
   */
  static const char *target_type_to_string_(TargetType type);

  /**
   * Convert an OpenThread error code to a log-friendly string.
   *
   * @param error OpenThread error code.
   * @return String name for `error`.
   */
  static const char *ot_error_to_string_(otError error);

  /**
   * Convert an OpenThread device role to a log-friendly string.
   *
   * @param role OpenThread device role.
   * @return String name for `role`.
   */
  static const char *device_role_to_string_(otDeviceRole role);

  /**
   * Convert one hexadecimal digit to its numeric nibble value.
   *
   * @param c Hexadecimal character to convert.
   * @return Nibble value in the range 0-15, or `-1` when `c` is invalid.
   */
  static int hex_to_nibble_(char c);

  /**
   * Forward a Parent Response callback from the C hook into the component.
   *
   * @param info Parsed Parent Response information from OpenThread.
   * @param context Opaque pointer to the owning component instance.
   */
  static void parent_response_callback_(const otThreadParentResponseInfo *info, void *context);

  /**
   * Check whether the current OpenThread parent matches the requested target.
   *
   * @param instance Active OpenThread instance.
   * @return `true` when the current parent is the preferred parent target.
   */
  bool current_parent_matches_(otInstance *instance) const;

  /**
   * Check whether the current Thread role is child.
   *
   * @param instance Active OpenThread instance.
   * @return `true` when the device is currently attached as a child.
   */
  bool is_child_(otInstance *instance) const;

  /**
   * Parse a hexadecimal RLOC16 string.
   *
   * @param text Text to parse.
   * @param out Output buffer for the parsed RLOC16.
   * @return `true` when `text` contains a valid 16-bit hexadecimal value.
   */
  static bool parse_rloc16_(const std::string &text, uint16_t *out);

  /**
   * Parse an extended address string into an `otExtAddress`.
   *
   * @param text Text to parse.
   * @param out Output buffer for the parsed extended address.
   * @return `true` when `text` contains a valid IEEE 802.15.4 extended address.
   */
  bool parse_extaddr_(const std::string &text, otExtAddress *out) const;

  /**
   * Compare two extended addresses for equality.
   *
   * @param a First extended address.
   * @param b Second extended address.
   * @return `true` when `a` and `b` are byte-for-byte equal.
   */
  bool extaddr_matches_(const otExtAddress &a, const otExtAddress &b) const;

  /**
   * Resolve a neighbor RLOC16 into its extended address.
   *
   * @param instance Active OpenThread instance.
   * @param rloc16 Neighbor RLOC16 to resolve.
   * @param out Output buffer for the resolved extended address.
   * @return `true` when the RLOC16 was found in the current neighbor table.
   */
  bool resolve_rloc16_to_extaddr_(otInstance *instance, uint16_t rloc16, otExtAddress *out) const;

  /**
   * Invoke the best available selected-parent attach hook.
   *
   * @param instance Active OpenThread instance.
   * @param extaddr Preferred parent extended address.
   * @return `true` when the hook accepted the attach request.
   */
  bool request_selected_parent_attach_(otInstance *instance, const otExtAddress &extaddr) const;

  /**
   * Check whether any selected-parent attach hook is available.
   *
   * @return `true` when a compatible selected-parent hook symbol is present.
   */
  bool selected_parent_hook_available_() const;

  /**
   * Check whether the multicast discovery-only hook is available.
   *
   * @return `true` when the discovery-only hook symbol is present.
   */
  bool discovery_hook_available_() const;

  /**
   * Check whether the unicast discovery-only hook is available.
   *
   * @return `true` when the unicast discovery hook symbol is present.
   */
  bool discovery_unicast_hook_available_() const;

  /**
   * Check whether a Parent Response matches the configured target.
   *
   * @param info Parent Response information to inspect.
   * @return `true` when `info` identifies the requested parent.
   */
  bool parent_response_matches_target_(const otThreadParentResponseInfo &info) const;

  /**
   * Convert an extended address to compact lowercase hexadecimal text.
   *
   * @param addr Extended address to format.
   * @return Lowercase hexadecimal string representation of `addr`.
   */
  std::string extaddr_to_string_(const otExtAddress &addr) const;

  /**
   * Format the currently configured target for logging.
   *
   * @return Human-readable description of the configured target.
   */
  std::string target_to_string_() const;

  /**
   * Start a Parent Request discovery pass for the configured target.
   *
   * @param instance Active OpenThread instance.
   * @return OpenThread status describing whether discovery started successfully.
   */
  otError start_parent_discovery_(otInstance *instance);

  /**
   * Start a unicast Parent Request discovery pass to a specific extended address.
   *
   * @param instance Active OpenThread instance.
   * @param extaddr Preferred parent extended address.
   * @return OpenThread status describing whether discovery started successfully.
   */
  otError start_parent_discovery_unicast_(otInstance *instance, const otExtAddress &extaddr);

  /**
   * Start a targeted selected-parent attach for the configured target.
   *
   * @param instance Active OpenThread instance.
   * @return OpenThread status describing whether attach startup succeeded.
   */
  otError start_selected_parent_attach_(otInstance *instance);

  /**
   * Clear any preferred-parent hints stored inside the OpenThread instance.
   *
   * @param instance Active OpenThread instance.
   */
  void clear_preferred_parent_in_ot_(otInstance *instance);

  /**
   * Reset state and enter the discovery phase for a new switch attempt.
   */
  void begin_switch_();

  /**
   * Reset all per-attempt Parent Response tracking state.
   */
  void reset_parent_response_tracking_();

  /**
   * Update the component status and log real transitions.
   *
   * @param status New component status.
   */
  void set_status_(Status status);

  /**
   * Record and react to a Parent Response observed during discovery.
   *
   * @param info Parsed Parent Response information from OpenThread.
   */
  void handle_parent_response_(const otThreadParentResponseInfo *info);

  /**
   * Log one buffered Parent Response at INFO level.
   *
   * @param entry Buffered Parent Response entry to log.
   * @param prefix Prefix describing the replay or live-log context.
   */
  void log_parent_response_info_(const BufferedParentResponse &entry, const char *prefix) const;

  /**
   * Log one buffered Parent Response at very-verbose level.
   *
   * @param entry Buffered Parent Response entry to log.
   * @param prefix Prefix describing the replay or live-log context.
   */
  void log_parent_response_vv_(const BufferedParentResponse &entry, const char *prefix) const;

  /**
   * Log a one-line summary of the current discovery attempt.
   *
   * @param reason Short label describing why the summary is being emitted.
   */
  void log_discovery_summary_(const char *reason) const;

  /**
   * Replay buffered Parent Responses into the log.
   *
   * @param reason Short label describing why the replay is being emitted.
   * @param mode Controls whether all responses or only target matches are shown.
   */
  void dump_buffered_parent_responses_(const char *reason, ReplayMode mode);

  // Keep a short history so failures can still be explained without spamming
  // the live log at INFO level for every response.
  static constexpr uint8_t PARENT_RESPONSE_BUFFER_SIZE = 16;

  TargetType target_type_{TargetType::NONE};
  SwitchPhase phase_{SwitchPhase::IDLE};
  uint16_t target_rloc16_{0xFFFE};
  otExtAddress target_extaddr_{};
  otExtAddress observed_target_extaddr_{};
  bool target_observed_this_attempt_{false};
  uint8_t max_attempts_{5};
  uint8_t attempts_{0};
  uint32_t retry_interval_ms_{8000};
  uint32_t selected_attach_timeout_ms_{16000};
  uint32_t phase_deadline_ms_{0};
  bool active_{false};
  bool require_selected_parent_hook_{true};
  bool log_parent_responses_{true};
  bool parent_request_unicast_{false};
  bool parent_response_callback_registered_{false};
  uint32_t parent_response_count_{0};
  uint32_t parent_response_last_dumped_count_{0};
  uint32_t parent_response_target_count_{0};
  uint32_t current_attempt_start_ms_{0};
  uint32_t attach_start_ms_{0};
  uint32_t discovery_target_observed_ms_{0};
  bool early_attach_on_target_{true};
  bool early_attach_pending_{false};
  uint32_t early_attach_delay_ms_{250};
  bool probe_active_{false};
  bool probe_completed_{false};
  uint32_t probe_parent_response_count_{0};
  uint32_t probe_target_parent_response_count_{0};
  otExtAddress probe_non_target_extaddr_{};
  bool best_target_rssi_valid_{false};
  int8_t best_target_rssi_{-128};
  uint16_t best_target_rloc16_{0xFFFE};
  uint8_t parent_response_buffer_head_{0};
  BufferedParentResponse parent_response_buffer_[PARENT_RESPONSE_BUFFER_SIZE]{};
  Status status_{Status::IDLE};
};

}  // namespace thread_preferred_parent
}  // namespace esphome
