"""ESPHome glue for OpenThread Parent Response delay diagnostics."""

import os

import esphome.codegen as cg
import esphome.config_validation as cv

DEPENDENCIES = ["openthread"]

CONF_ENABLED = "enabled"

SCRIPT_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "apply-openthread-parent-response-delay-log.py")
)

CONFIG_SCHEMA = cv.Schema(
    {
        cv.Optional(CONF_ENABLED, default=True): cv.boolean,
    }
).extend(cv.COMPONENT_SCHEMA)


async def to_code(config):
    """Register the OpenThread source instrumentation when enabled."""

    if config[CONF_ENABLED]:
        cg.add_platformio_option("extra_scripts", [f"pre:{SCRIPT_PATH}"])
