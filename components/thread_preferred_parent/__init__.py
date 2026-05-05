import os

import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.const import CONF_ID

DEPENDENCIES = ["openthread"]

thread_preferred_parent_ns = cg.esphome_ns.namespace("thread_preferred_parent")
ThreadPreferredParentComponent = thread_preferred_parent_ns.class_(
    "ThreadPreferredParentComponent", cg.Component
)

CONF_PARENT_RLOC = "parent_rloc"
CONF_PARENT_EXTADDR = "parent_extaddr"
CONF_MAX_ATTEMPTS = "max_attempts"
CONF_RETRY_INTERVAL = "retry_interval"
CONF_SELECTED_ATTACH_TIMEOUT = "selected_attach_timeout"
CONF_REQUIRE_SELECTED_PARENT_HOOK = "require_selected_parent_hook"
CONF_LOG_PARENT_RESPONSES = "log_parent_responses"
CONF_PARENT_REQUEST_UNICAST = "parent_request_unicast"

SCRIPT_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "apply-openthread-selected-parent-hook.py")
)


def validate_rloc16(value):
    """Validate an RLOC16 as either 0x1234 / 1234 hex string or integer."""
    if isinstance(value, int):
        return cv.int_range(min=0x0000, max=0xFFFD)(value)

    value = cv.string_strict(value).strip().lower()
    if value.startswith("0x"):
        value = value[2:]

    try:
        parsed = int(value, 16)
    except ValueError as err:
        raise cv.Invalid("RLOC16 must be a 16-bit hex value, e.g. 0x5800 or 5800") from err

    return cv.int_range(min=0x0000, max=0xFFFD)(parsed)


def validate_extaddr(value):
    """Validate and normalize an IEEE 802.15.4 extended address.

    Accepted formats:
      * 00124b0001abcdef
      * 00:12:4b:00:01:ab:cd:ef
      * 00-12-4b-00-01-ab-cd-ef
      * 0x00124b0001abcdef
    """
    value = cv.string_strict(value).strip().lower()
    if value.startswith("0x"):
        value = value[2:]

    compact = "".join(ch for ch in value if ch not in ":- _")
    if len(compact) != 16:
        raise cv.Invalid("Extended address must contain exactly 8 bytes / 16 hex digits")

    try:
        int(compact, 16)
    except ValueError as err:
        raise cv.Invalid("Extended address must be hexadecimal, e.g. 00124b0001abcdef") from err

    return compact


def validate_identifier(config):
    has_rloc = CONF_PARENT_RLOC in config
    has_extaddr = CONF_PARENT_EXTADDR in config
    if has_rloc and has_extaddr:
        raise cv.Invalid("Specify only one of parent_rloc or parent_extaddr")
    return config


CONFIG_SCHEMA = cv.All(
    cv.Schema(
        {
            cv.GenerateID(): cv.declare_id(ThreadPreferredParentComponent),
            cv.Optional(CONF_PARENT_RLOC): validate_rloc16,
            cv.Optional(CONF_PARENT_EXTADDR): validate_extaddr,
            cv.Optional(CONF_MAX_ATTEMPTS, default=5): cv.int_range(min=1, max=20),
            cv.Optional(CONF_RETRY_INTERVAL, default="8s"): cv.positive_time_period_milliseconds,
            cv.Optional(CONF_SELECTED_ATTACH_TIMEOUT, default="16s"): cv.positive_time_period_milliseconds,
            cv.Optional(CONF_REQUIRE_SELECTED_PARENT_HOOK, default=True): cv.boolean,
            cv.Optional(CONF_LOG_PARENT_RESPONSES, default=True): cv.boolean,
            cv.Optional(CONF_PARENT_REQUEST_UNICAST, default=False): cv.boolean,
        }
    ).extend(cv.COMPONENT_SCHEMA),
    validate_identifier,
)


async def to_code(config):
    # Register the PlatformIO pre-build script automatically. This lets Home
    # Assistant ESPHome add-on users consume the external component directly
    # without manually copying scripts into /config/esphome/scripts.
    cg.add_platformio_option("extra_scripts", [f"pre:{SCRIPT_PATH}"])

    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)

    if CONF_PARENT_RLOC in config:
        cg.add(var.set_parent_rloc16(config[CONF_PARENT_RLOC]))
    if CONF_PARENT_EXTADDR in config:
        cg.add(var.set_parent_extaddr(config[CONF_PARENT_EXTADDR]))

    cg.add(var.set_max_attempts(config[CONF_MAX_ATTEMPTS]))
    cg.add(var.set_retry_interval(config[CONF_RETRY_INTERVAL].total_milliseconds))
    cg.add(var.set_selected_attach_timeout(config[CONF_SELECTED_ATTACH_TIMEOUT].total_milliseconds))
    cg.add(var.set_require_selected_parent_hook(config[CONF_REQUIRE_SELECTED_PARENT_HOOK]))
    cg.add(var.set_log_parent_responses(config[CONF_LOG_PARENT_RESPONSES]))
    cg.add(var.set_parent_request_unicast(config[CONF_PARENT_REQUEST_UNICAST]))
