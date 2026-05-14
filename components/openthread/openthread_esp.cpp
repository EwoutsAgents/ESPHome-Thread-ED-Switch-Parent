#include "esphome/core/defines.h"
#if defined(USE_OPENTHREAD) && defined(USE_ESP32)
#include <openthread/logging.h>
#include <openthread/dataset_ftd.h>
#include "openthread.h"

#include "esp_log.h"
#include "esp_openthread.h"
#include "esp_openthread_lock.h"

#include "esp_task_wdt.h"
#include "esp_rom_sys.h"
#include "esphome/core/hal.h"
#include "esphome/core/helpers.h"
#include "esphome/core/log.h"

#include "esp_err.h"
#include "esp_event.h"
#include "esp_netif.h"
#include "esp_netif_types.h"
#include "esp_openthread_cli.h"
#include "esp_openthread_netif_glue.h"
#include "esp_vfs_eventfd.h"
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "nvs_flash.h"

static const char *const TAG = "openthread";

namespace esphome::openthread {

static int hex_digit_to_int(char hex) {
  if ('A' <= hex && hex <= 'F') return 10 + hex - 'A';
  if ('a' <= hex && hex <= 'f') return 10 + hex - 'a';
  if ('0' <= hex && hex <= '9') return hex - '0';
  return -1;
}

static size_t hex_string_to_binary(const char *hex_string, uint8_t *buf, size_t buf_size) {
  if (hex_string[0] == '0' && (hex_string[1] == 'x' || hex_string[1] == 'X')) {
    hex_string += 2;
  }
  int num_char = strlen(hex_string);
  if (num_char != static_cast<int>(buf_size * 2)) return 0;
  for (size_t i = 0; i < static_cast<size_t>(num_char); i += 2) {
    int digit0 = hex_digit_to_int(hex_string[i]);
    int digit1 = hex_digit_to_int(hex_string[i + 1]);
    if (digit0 < 0 || digit1 < 0) return 0;
    buf[i / 2] = (digit0 << 4) + digit1;
  }
  return buf_size;
}

void OpenThreadComponent::setup() {
  esp_vfs_eventfd_config_t eventfd_config = {
      .max_fds = 4,
  };
  ESP_ERROR_CHECK(nvs_flash_init());
  ESP_ERROR_CHECK(esp_event_loop_create_default());
  ESP_ERROR_CHECK(esp_netif_init());
  ESP_ERROR_CHECK(esp_vfs_eventfd_register(&eventfd_config));

  xTaskCreate(
      [](void *arg) {
        static_cast<OpenThreadComponent *>(arg)->ot_main();
        vTaskDelete(nullptr);
      },
      "ot_main", 10240, this, 5, nullptr);
}

static esp_netif_t *init_openthread_netif(const esp_openthread_platform_config_t *config) {
  esp_netif_config_t cfg = ESP_NETIF_DEFAULT_OPENTHREAD();
  esp_netif_t *netif = esp_netif_new(&cfg);
  assert(netif != nullptr);
  ESP_ERROR_CHECK(esp_netif_attach(netif, esp_openthread_netif_glue_init(config)));
  return netif;
}

void OpenThreadComponent::ot_main() {
  esp_openthread_platform_config_t config = {
      .radio_config =
          {
              .radio_mode = RADIO_MODE_NATIVE,
              .radio_uart_config = {},
          },
      .host_config =
          {
          },
      .port_config =
          {
              .storage_partition_name = "nvs",
              .netif_queue_size = 10,
              .task_queue_size = 10,
          },
  };

  ESP_ERROR_CHECK(esp_openthread_init(&config));
  this->lock_initialized_ = true;
  otInstance *instance = esp_openthread_get_instance();

#if CONFIG_OPENTHREAD_STATE_INDICATOR_ENABLE
  ESP_ERROR_CHECK(esp_openthread_state_indicator_init(instance));
#endif

#if CONFIG_OPENTHREAD_LOG_LEVEL_DYNAMIC
  (void) otLoggingSetLevel(CONFIG_LOG_DEFAULT_LEVEL);
#endif
#if CONFIG_OPENTHREAD_CLI
  esp_openthread_cli_init();
#endif

  esp_netif_t *openthread_netif = init_openthread_netif(&config);
  esp_netif_set_default_netif(openthread_netif);

#if CONFIG_OPENTHREAD_CLI_ESP_EXTENSION
  esp_cli_custom_command_init();
#endif

  esp_openthread_lock_acquire(portMAX_DELAY);

  ESP_LOGD(TAG, "Thread Version: %" PRIu16, otThreadGetVersion());
  otInstanceErasePersistentInfo(instance);

  otExtAddress factory_eui64{};
  otLinkGetFactoryAssignedIeeeEui64(instance, &factory_eui64);
  otError extaddr_err = otLinkSetExtendedAddress(instance, &factory_eui64);
  if (extaddr_err != OT_ERROR_NONE) {
    ESP_LOGE(TAG, "Failed to set factory IEEE EUI-64 as Thread extaddr: %s (%d)",
             otThreadErrorToString(extaddr_err), static_cast<int>(extaddr_err));
    esp_openthread_lock_release();
    return;
  }

  otOperationalDatasetTlvs dataset_tlvs = {};
#ifndef USE_OPENTHREAD_FORCE_DATASET
  otError error = otDatasetGetActiveTlvs(instance, &dataset_tlvs);
  if (error != OT_ERROR_NONE) {
    dataset_tlvs.mLength = 0;
  } else {
    ESP_LOGI(TAG, "Found existing dataset, ignoring config (force_dataset: true to override)");
  }
#endif

#ifdef USE_OPENTHREAD_TLVS
  if (dataset_tlvs.mLength == 0) {
    size_t len = (sizeof(USE_OPENTHREAD_TLVS) - 1) / 2;
    if (len > sizeof(dataset_tlvs.mTlvs)) {
      ESP_LOGW(TAG, "TLV buffer too small, truncating");
      len = sizeof(dataset_tlvs.mTlvs);
    }
    parse_hex(USE_OPENTHREAD_TLVS, sizeof(USE_OPENTHREAD_TLVS) - 1, dataset_tlvs.mTlvs, len);
    dataset_tlvs.mLength = len;
  }
#endif

  if (dataset_tlvs.mLength > 0) {
    otError tlv_err = otDatasetSetActiveTlvs(instance, &dataset_tlvs);
    if (tlv_err != OT_ERROR_NONE) {
      ESP_LOGE(TAG, "Failed to set active TLVs: %s", otThreadErrorToString(tlv_err));
      esp_openthread_lock_release();
      return;
    }
  } else {
    otOperationalDataset dataset = {};
#if CONFIG_OPENTHREAD_FTD
    otDatasetCreateNewNetwork(instance, &dataset);
#endif
    dataset.mActiveTimestamp.mSeconds = 1;
    dataset.mActiveTimestamp.mTicks = 0;
    dataset.mActiveTimestamp.mAuthoritative = false;
    dataset.mComponents.mIsActiveTimestampPresent = true;
    dataset.mChannel = CONFIG_OPENTHREAD_NETWORK_CHANNEL;
    dataset.mComponents.mIsChannelPresent = true;
    dataset.mPanId = CONFIG_OPENTHREAD_NETWORK_PANID;
    dataset.mComponents.mIsPanIdPresent = true;
    size_t len = strlen(CONFIG_OPENTHREAD_NETWORK_NAME);
    memcpy(dataset.mNetworkName.m8, CONFIG_OPENTHREAD_NETWORK_NAME, len + 1);
    dataset.mComponents.mIsNetworkNamePresent = true;
    len = hex_string_to_binary(CONFIG_OPENTHREAD_NETWORK_EXTPANID, dataset.mExtendedPanId.m8,
                               sizeof(dataset.mExtendedPanId.m8));
    if (len != sizeof(dataset.mExtendedPanId.m8)) {
      ESP_LOGE(TAG, "Cannot convert extended pan id '%s' (len=%u expected=%u)",
               CONFIG_OPENTHREAD_NETWORK_EXTPANID, static_cast<unsigned>(len),
               static_cast<unsigned>(sizeof(dataset.mExtendedPanId.m8)));
      esp_openthread_lock_release();
      return;
    }
    dataset.mComponents.mIsExtendedPanIdPresent = true;
    otIp6Prefix prefix;
    memset(&prefix, 0, sizeof(prefix));
    otError prefix_err = otIp6PrefixFromString(CONFIG_OPENTHREAD_MESH_LOCAL_PREFIX, &prefix);
    if (prefix_err == OT_ERROR_NONE) {
      memcpy(dataset.mMeshLocalPrefix.m8, prefix.mPrefix.mFields.m8, sizeof(dataset.mMeshLocalPrefix.m8));
      dataset.mComponents.mIsMeshLocalPrefixPresent = true;
    }
    len = hex_string_to_binary(CONFIG_OPENTHREAD_NETWORK_MASTERKEY, dataset.mNetworkKey.m8,
                               sizeof(dataset.mNetworkKey.m8));
    if (len != sizeof(dataset.mNetworkKey.m8)) {
      ESP_LOGE(TAG, "Cannot convert master key '%s' (len=%u expected=%u)", CONFIG_OPENTHREAD_NETWORK_MASTERKEY,
               static_cast<unsigned>(len), static_cast<unsigned>(sizeof(dataset.mNetworkKey.m8)));
      esp_openthread_lock_release();
      return;
    }
    dataset.mComponents.mIsNetworkKeyPresent = true;
    len = hex_string_to_binary(CONFIG_OPENTHREAD_NETWORK_PSKC, dataset.mPskc.m8, sizeof(dataset.mPskc.m8));
    if (len != sizeof(dataset.mPskc.m8)) {
      ESP_LOGE(TAG, "Cannot convert pskc '%s' (len=%u expected=%u)", CONFIG_OPENTHREAD_NETWORK_PSKC,
               static_cast<unsigned>(len), static_cast<unsigned>(sizeof(dataset.mPskc.m8)));
      esp_openthread_lock_release();
      return;
    }
    dataset.mComponents.mIsPskcPresent = true;
    otError set_err = otDatasetSetActive(instance, &dataset);
    if (set_err != OT_ERROR_NONE) {
      ESP_LOGE(TAG, "Failed to set active dataset: %s (%d)", otThreadErrorToString(set_err), static_cast<int>(set_err));
      esp_openthread_lock_release();
      return;
    }
  }

  otError ip6_err = otIp6SetEnabled(instance, true);
  if (ip6_err != OT_ERROR_NONE) {
    ESP_LOGE(TAG, "Failed to enable IPv6: %s (%d)", otThreadErrorToString(ip6_err), static_cast<int>(ip6_err));
    esp_openthread_lock_release();
    return;
  }

  otLinkModeConfig link_mode_config{};
#if CONFIG_OPENTHREAD_FTD
  link_mode_config.mRxOnWhenIdle = true;
  link_mode_config.mDeviceType = true;
  link_mode_config.mNetworkData = true;
#elif CONFIG_OPENTHREAD_MTD
  if (this->poll_period_ > 0) {
    if (otLinkSetPollPeriod(instance, this->poll_period_) != OT_ERROR_NONE) {
      ESP_LOGE(TAG, "Failed to set pollperiod");
    }
    ESP_LOGD(TAG, "Link Polling Period: %" PRIu32, otLinkGetPollPeriod(instance));
  }
  link_mode_config.mRxOnWhenIdle = this->poll_period_ == 0;
  link_mode_config.mDeviceType = false;
  link_mode_config.mNetworkData = false;
#endif

  otError link_mode_err = otThreadSetLinkMode(instance, link_mode_config);
  if (link_mode_err != OT_ERROR_NONE) {
    ESP_LOGE(TAG, "Failed to set linkmode (%d)", static_cast<int>(link_mode_err));
    esp_openthread_lock_release();
    return;
  }
#ifdef ESPHOME_LOG_HAS_DEBUG
  link_mode_config = otThreadGetLinkMode(instance);
  ESP_LOGD(TAG, "Link Mode Device Type: %s, Network Data: %s, RX On When Idle: %s",
           TRUEFALSE(link_mode_config.mDeviceType), TRUEFALSE(link_mode_config.mNetworkData),
           TRUEFALSE(link_mode_config.mRxOnWhenIdle));
#endif

  otError thread_enable_err = otThreadSetEnabled(instance, true);
  if (thread_enable_err != OT_ERROR_NONE) {
    ESP_LOGE(TAG, "Failed to enable Thread: %s (%d)", otThreadErrorToString(thread_enable_err),
             static_cast<int>(thread_enable_err));
    esp_openthread_lock_release();
    return;
  }

  if (this->output_power_.has_value()) {
    if (const auto err = otPlatRadioSetTransmitPower(instance, *this->output_power_); err != OT_ERROR_NONE) {
      ESP_LOGE(TAG, "Failed to set power: %s", otThreadErrorToString(err));
    }
  }

  otSetStateChangedCallback(instance, OpenThreadComponent::on_state_changed_, this);
  esp_openthread_lock_release();

#if CONFIG_OPENTHREAD_CLI
  esp_openthread_cli_create_task();
#endif
  esp_openthread_launch_mainloop();

  this->lock_initialized_ = false;
  esp_openthread_deinit();
  esp_openthread_netif_glue_deinit();
  esp_netif_destroy(openthread_netif);
  esp_vfs_eventfd_unregister();
  this->teardown_complete_ = true;
  vTaskDelete(NULL);
}

int OpenThreadComponent::openthread_stop_() { return esp_openthread_mainloop_exit(); }

network::IPAddresses OpenThreadComponent::get_ip_addresses() {
  network::IPAddresses addresses;
  struct esp_ip6_addr if_ip6s[CONFIG_LWIP_IPV6_NUM_ADDRESSES];
  uint8_t count = 0;
  esp_netif_t *netif = esp_netif_get_default_netif();
  count = esp_netif_get_all_ip6(netif, if_ip6s);
  assert(count <= CONFIG_LWIP_IPV6_NUM_ADDRESSES);
  assert(count < addresses.size());
  for (int i = 0; i < count; i++) {
    addresses[i + 1] = network::IPAddress(&if_ip6s[i]);
  }
  return addresses;
}

otInstance *OpenThreadComponent::get_openthread_instance_() { return esp_openthread_get_instance(); }

std::optional<InstanceLock> InstanceLock::try_acquire(int delay) {
  if (!global_openthread_component->is_lock_initialized()) {
    return {};
  }
  if (esp_openthread_lock_acquire(delay)) {
    return InstanceLock();
  }
  return {};
}

InstanceLock InstanceLock::acquire() {
  constexpr uint32_t lock_init_timeout_ms = 10000;
  uint32_t start = millis();
  while (!global_openthread_component->is_lock_initialized()) {
    if (millis() - start > lock_init_timeout_ms) {
      ESP_LOGE(TAG, "OpenThread lock not initialized after %" PRIu32 "ms, aborting", lock_init_timeout_ms);
      abort();
    }
    delay(10);
    esp_task_wdt_reset();
  }
  while (!esp_openthread_lock_acquire(100)) {
    esp_task_wdt_reset();
  }
  return InstanceLock();
}

otInstance *InstanceLock::get_instance() { return esp_openthread_get_instance(); }

InstanceLock::~InstanceLock() { esp_openthread_lock_release(); }

}  // namespace esphome::openthread
#endif
