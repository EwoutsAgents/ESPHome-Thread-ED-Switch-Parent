import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.const import CONF_ID
from esphome.core import TimePeriod

DEPENDENCIES = ["openthread"]

thread_router_control_ns = cg.esphome_ns.namespace("thread_router_control")
ThreadRouterControlComponent = thread_router_control_ns.class_(
    "ThreadRouterControlComponent", cg.Component
)

CONF_COMMAND_ECHO = "command_echo"
CONF_DEFAULT_OFF_TIMEOUT = "default_off_timeout"

CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(): cv.declare_id(ThreadRouterControlComponent),
        cv.Optional(CONF_COMMAND_ECHO, default=True): cv.boolean,
        cv.Optional(CONF_DEFAULT_OFF_TIMEOUT, default="60s"): cv.positive_time_period_seconds,
    }
).extend(cv.COMPONENT_SCHEMA)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    cg.add(var.set_command_echo(config[CONF_COMMAND_ECHO]))
    timeout = config[CONF_DEFAULT_OFF_TIMEOUT]
    cg.add(var.set_default_off_timeout_ms(int(timeout.total_milliseconds)))
