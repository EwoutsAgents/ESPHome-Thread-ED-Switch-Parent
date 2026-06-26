"""ESPHome configuration glue for the fast unicast Parent Response patch.

This component is intentionally router-side only. It registers a pre-build
script that patches ESP-IDF's vendored OpenThread sources and emits the
compile-time define used by that patch.
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
    """Register the router-side OpenThread patcher and build flag."""

    cg.add_platformio_option("extra_scripts", [f"pre:{SCRIPT_PATH}"])
    cg.add_platformio_option(
        "build_flags",
        [
            "-DOPENTHREAD_CONFIG_EXPERIMENTAL_UNICAST_PARENT_RESPONSE_FASTPATH_ENABLE="
            f"{1 if config[CONF_ENABLED] else 0}"
        ],
    )
