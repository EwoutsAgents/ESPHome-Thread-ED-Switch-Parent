import os

import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.const import CONF_ID

DEPENDENCIES = ["openthread"]

thread_stock_observer_ns = cg.esphome_ns.namespace("thread_stock_observer")
ThreadStockObserverComponent = thread_stock_observer_ns.class_(
    "ThreadStockObserverComponent", cg.Component
)

CONF_TARGET_PARENT_EXTADDR = "target_parent_extaddr"
CONF_OBSERVE_TIMEOUT = "observe_timeout"
CONF_LOG_PARENT_RESPONSES = "log_parent_responses"

SCRIPT_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "thread_preferred_parent",
        "apply-openthread-selected-parent-hook.py",
    )
)


def validate_extaddr(value):
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


CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(): cv.declare_id(ThreadStockObserverComponent),
        cv.Required(CONF_TARGET_PARENT_EXTADDR): validate_extaddr,
        cv.Optional(CONF_OBSERVE_TIMEOUT, default="16s"): cv.positive_time_period_milliseconds,
        cv.Optional(CONF_LOG_PARENT_RESPONSES, default=True): cv.boolean,
    }
).extend(cv.COMPONENT_SCHEMA)


async def to_code(config):
    cg.add_platformio_option("extra_scripts", [f"pre:{SCRIPT_PATH}"])

    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)

    cg.add(var.set_target_parent_extaddr(config[CONF_TARGET_PARENT_EXTADDR]))
    cg.add(var.set_observe_timeout(config[CONF_OBSERVE_TIMEOUT].total_milliseconds))
    cg.add(var.set_log_parent_responses(config[CONF_LOG_PARENT_RESPONSES]))
