"""ESPHome configuration glue for the fast unicast Parent Response patch.

This component is intentionally router-side only. When enabled, it registers a
pre-build script that patches ESP-IDF's vendored OpenThread sources.
"""

import os

import esphome.codegen as cg
import esphome.config_validation as cv

DEPENDENCIES = ["openthread"]

CONF_ENABLED = "enabled"

SCRIPT_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "apply-openthread-fast-unicast-parent-response.py")
)


CONFIG_SCHEMA = cv.Schema(
    {
        cv.Optional(CONF_ENABLED, default=True): cv.boolean,
    }
).extend(cv.COMPONENT_SCHEMA)


async def to_code(config):
    """Register the router-side OpenThread patcher when enabled."""

    if not config[CONF_ENABLED]:
        return

    cg.add_platformio_option("extra_scripts", [f"pre:{SCRIPT_PATH}"])
