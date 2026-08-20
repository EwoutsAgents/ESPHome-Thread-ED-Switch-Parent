"""Isolated ESPHome integration for OpenThread PR #13121 Fast Attach."""

import os

import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.const import CONF_ID

DEPENDENCIES = ["openthread"]

thread_fast_attach_ns = cg.esphome_ns.namespace("thread_fast_attach")
ThreadFastAttachComponent = thread_fast_attach_ns.class_("ThreadFastAttachComponent", cg.Component)

CONF_ARM_AFTER_PARENT_LOSS = "arm_after_parent_loss"
SCRIPT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "apply-openthread-fast-attach.py"))

CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(): cv.declare_id(ThreadFastAttachComponent),
        cv.Optional(CONF_ARM_AFTER_PARENT_LOSS, default=False): cv.boolean,
    }
).extend(cv.COMPONENT_SCHEMA)


async def to_code(config):
    # The framework package is installed/updated during PlatformIO's pre phase,
    # so patch only after package resolution has completed.
    cg.add_platformio_option("extra_scripts", [f"post:{SCRIPT_PATH}"])
    cg.add_build_flag("-DOPENTHREAD_CONFIG_MLE_FAST_ATTACH_ENABLE=1")

    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    cg.add(var.set_arm_after_parent_loss(config[CONF_ARM_AFTER_PARENT_LOSS]))
