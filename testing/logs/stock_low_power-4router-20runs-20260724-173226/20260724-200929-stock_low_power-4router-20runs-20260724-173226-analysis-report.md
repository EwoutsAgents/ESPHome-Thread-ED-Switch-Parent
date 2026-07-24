# Child Log Analysis

## stock_child

Files analyzed: **20**

- batch folders: `stock_low_power-4router-20runs-20260724-173226`

### PCAP-complete child attach summary

| Attach | Metric | M (SD), ms | n |
| --- | --- | ---: | ---: |
| 1 | Request -> Response | 165.48 (138.57) | 20 |
| 1 | Request -> Response minus Random Delay | 10.13 (1.37) | 20 |
| 1 | Response -> Child ID Request | 584.29 (140.38) | 20 |
| 1 | Child ID Request -> Response | 13.94 (0.88) | 20 |
| 1 | Full Attach | 763.72 (5.74) | 20 |
| 2 | Request -> Response | 324.42 (139.53) | 20 |
| 2 | Request -> Response minus Random Delay | 9.47 (1.56) | 20 |
| 2 | Response -> Child ID Request | 426.67 (139.81) | 20 |
| 2 | Child ID Request -> Response | 13.71 (0.83) | 20 |
| 2 | Full Attach | 764.80 (1.56) | 20 |

| Metric | M (SD) | n |
| --- | ---: | ---: |
| Failed TX Attempts per Log | 0.00 (0.00) | 20 |
| Log-only or Partial Sequences per Log | 0.00 (0.00) | 20 |

### `stock_child_20260724-173453-run01.log`

- manifest status: `completed`
- child extaddr: `4241e108db5e02cc`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `cbdc29c83a0a0fab31d5249a922e7633d6099dbf8029866afc776a235bb514d5` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `eac6ad4d9175a4e4`
- parent rloc16: `n/a`
- child extaddr: `4241e108db5e02cc`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **64.292 ms**
- selected-parent logged random delay: **55 ms**
- random-delay source router: `router2`
- random-delay source log time: `17:38:13.098`
- Request -> Response minus Random Delay: **9.292 ms**
- Response -> Child ID Request: **684.681 ms**
- Child ID Request -> Response: **14.423 ms**
- Full Attach: **763.396 ms**
- pcap parent request: `17:38:13.116` (frame 622)
- pcap parent response: `17:38:13.180` (frame 623)
- pcap child id request: `17:38:13.865` (frame 632)
- pcap child id response: `17:38:13.879` (frame 634)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `9ec0a76b0eb740b5`
- parent rloc16: `n/a`
- child extaddr: `4241e108db5e02cc`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **375.623 ms**
- selected-parent logged random delay: **366 ms**
- random-delay source router: `router1`
- random-delay source log time: `17:42:13.329`
- Request -> Response minus Random Delay: **9.623 ms**
- Response -> Child ID Request: **378.117 ms**
- Child ID Request -> Response: **13.91 ms**
- Full Attach: **767.65 ms**
- pcap parent request: `17:42:13.356` (frame 933)
- pcap parent response: `17:42:13.732` (frame 938)
- pcap child id request: `17:42:14.110` (frame 940)
- pcap child id response: `17:42:14.124` (frame 942)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-174235-run02.log`

- manifest status: `completed`
- child extaddr: `c6906b9e8079b8c4`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `cbdc29c83a0a0fab31d5249a922e7633d6099dbf8029866afc776a235bb514d5` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `8a9d521c7ac724b0`
- parent rloc16: `n/a`
- child extaddr: `c6906b9e8079b8c4`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **122.708 ms**
- selected-parent logged random delay: **110 ms**
- random-delay source router: `router2`
- random-delay source log time: `17:45:55.721`
- Request -> Response minus Random Delay: **12.708 ms**
- Response -> Child ID Request: **629.292 ms**
- Child ID Request -> Response: **14.805 ms**
- Full Attach: **766.805 ms**
- pcap parent request: `17:45:55.738` (frame 790)
- pcap parent response: `17:45:55.861` (frame 795)
- pcap child id request: `17:45:56.490` (frame 829)
- pcap child id response: `17:45:56.505` (frame 831)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `622c4e2c474d1842`
- parent rloc16: `n/a`
- child extaddr: `c6906b9e8079b8c4`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **217.06 ms**
- selected-parent logged random delay: **208 ms**
- random-delay source router: `router1`
- random-delay source log time: `17:49:56.250`
- Request -> Response minus Random Delay: **9.06 ms**
- Response -> Child ID Request: **533.959 ms**
- Child ID Request -> Response: **13.102 ms**
- Full Attach: **764.121 ms**
- pcap parent request: `17:49:56.276` (frame 1122)
- pcap parent response: `17:49:56.493` (frame 1123)
- pcap child id request: `17:49:57.027` (frame 1129)
- pcap child id response: `17:49:57.040` (frame 1131)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-175017-run03.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `d6c61a1dcddf7301`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `cbdc29c83a0a0fab31d5249a922e7633d6099dbf8029866afc776a235bb514d5` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `4ae5e48b6d0c52c4`
- parent rloc16: `n/a`
- child extaddr: `d6c61a1dcddf7301`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **60.146 ms**
- selected-parent logged random delay: **50 ms**
- random-delay source router: `router1`
- random-delay source log time: `17:53:38.424`
- Request -> Response minus Random Delay: **10.146 ms**
- Response -> Child ID Request: **690.848 ms**
- Child ID Request -> Response: **12.399 ms**
- Full Attach: **763.393 ms**
- pcap parent request: `17:53:38.441` (frame 331)
- pcap parent response: `17:53:38.501` (frame 334)
- pcap child id request: `17:53:39.191` (frame 340)
- pcap child id response: `17:53:39.204` (frame 342)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `3ab54eb4a5a9f7c4`
- parent rloc16: `n/a`
- child extaddr: `d6c61a1dcddf7301`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **56.055 ms**
- selected-parent logged random delay: **46 ms**
- random-delay source router: `router2`
- random-delay source log time: `17:57:38.595`
- Request -> Response minus Random Delay: **10.055 ms**
- Response -> Child ID Request: **695.947 ms**
- Child ID Request -> Response: **14.092 ms**
- Full Attach: **766.094 ms**
- pcap parent request: `17:57:38.620` (frame 674)
- pcap parent response: `17:57:38.676` (frame 675)
- pcap child id request: `17:57:39.372` (frame 683)
- pcap child id response: `17:57:39.387` (frame 685)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-175800-run04.log`

- manifest status: `completed`
- child extaddr: `8e96b5b0bf9f60d5`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `cbdc29c83a0a0fab31d5249a922e7633d6099dbf8029866afc776a235bb514d5` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `1a8e8732a52ed216`
- parent rloc16: `n/a`
- child extaddr: `8e96b5b0bf9f60d5`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **386.876 ms**
- selected-parent logged random delay: **376 ms**
- random-delay source router: `router2`
- random-delay source log time: `18:01:21.493`
- Request -> Response minus Random Delay: **10.876 ms**
- Response -> Child ID Request: **365.133 ms**
- Child ID Request -> Response: **14.878 ms**
- Full Attach: **766.887 ms**
- pcap parent request: `18:01:21.510` (frame 131)
- pcap parent response: `18:01:21.897` (frame 134)
- pcap child id request: `18:01:22.262` (frame 140)
- pcap child id response: `18:01:22.277` (frame 142)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `baec719fd32ae10c`
- parent rloc16: `n/a`
- child extaddr: `8e96b5b0bf9f60d5`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **375.503 ms**
- selected-parent logged random delay: **368 ms**
- random-delay source router: `router1`
- random-delay source log time: `18:05:21.728`
- Request -> Response minus Random Delay: **7.503 ms**
- Response -> Child ID Request: **377.256 ms**
- Child ID Request -> Response: **12.205 ms**
- Full Attach: **764.964 ms**
- pcap parent request: `18:05:21.754` (frame 416)
- pcap parent response: `18:05:22.129` (frame 421)
- pcap child id request: `18:05:22.507` (frame 423)
- pcap child id response: `18:05:22.519` (frame 425)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-180543-run05.log`

- manifest status: `completed`
- child extaddr: `1e2dd2100e4c5111`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `cbdc29c83a0a0fab31d5249a922e7633d6099dbf8029866afc776a235bb514d5` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `225a69be05b31a16`
- parent rloc16: `n/a`
- child extaddr: `1e2dd2100e4c5111`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **275.088 ms**
- selected-parent logged random delay: **264 ms**
- random-delay source router: `router2`
- random-delay source log time: `18:09:04.039`
- Request -> Response minus Random Delay: **11.088 ms**
- Response -> Child ID Request: **473.915 ms**
- Child ID Request -> Response: **13.492 ms**
- Full Attach: **762.495 ms**
- pcap parent request: `18:09:04.057` (frame 628)
- pcap parent response: `18:09:04.332` (frame 635)
- pcap child id request: `18:09:04.806` (frame 637)
- pcap child id response: `18:09:04.819` (frame 639)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `52d6c1caf73ca4b5`
- parent rloc16: `n/a`
- child extaddr: `1e2dd2100e4c5111`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **269.325 ms**
- selected-parent logged random delay: **258 ms**
- random-delay source router: `router1`
- random-delay source log time: `18:13:04.698`
- Request -> Response minus Random Delay: **11.325 ms**
- Response -> Child ID Request: **480.695 ms**
- Child ID Request -> Response: **12.536 ms**
- Full Attach: **762.556 ms**
- pcap parent request: `18:13:04.725` (frame 918)
- pcap parent response: `18:13:04.994` (frame 921)
- pcap child id request: `18:13:05.475` (frame 925)
- pcap child id response: `18:13:05.487` (frame 927)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-181326-run06.log`

- manifest status: `completed`
- child extaddr: `a6162940dc4ef01e`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `cbdc29c83a0a0fab31d5249a922e7633d6099dbf8029866afc776a235bb514d5` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `b634cf34834bc548`
- parent rloc16: `n/a`
- child extaddr: `a6162940dc4ef01e`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **301.698 ms**
- selected-parent logged random delay: **293 ms**
- random-delay source router: `router2`
- random-delay source log time: `18:16:46.705`
- Request -> Response minus Random Delay: **8.698 ms**
- Response -> Child ID Request: **449.295 ms**
- Child ID Request -> Response: **14.987 ms**
- Full Attach: **765.98 ms**
- pcap parent request: `18:16:46.722` (frame 147)
- pcap parent response: `18:16:47.024` (frame 148)
- pcap child id request: `18:16:47.473` (frame 156)
- pcap child id response: `18:16:47.488` (frame 158)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `aed2b2333a35f457`
- parent rloc16: `n/a`
- child extaddr: `a6162940dc4ef01e`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **355.146 ms**
- selected-parent logged random delay: **345 ms**
- random-delay source router: `router1`
- random-delay source log time: `18:20:47.098`
- Request -> Response minus Random Delay: **10.146 ms**
- Response -> Child ID Request: **397.602 ms**
- Child ID Request -> Response: **13.409 ms**
- Full Attach: **766.157 ms**
- pcap parent request: `18:20:47.124` (frame 431)
- pcap parent response: `18:20:47.480` (frame 432)
- pcap child id request: `18:20:47.877` (frame 438)
- pcap child id response: `18:20:47.891` (frame 440)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-182108-run07.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `9653672b5e84f070`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `cbdc29c83a0a0fab31d5249a922e7633d6099dbf8029866afc776a235bb514d5` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `1a7b25293aecdf28`
- parent rloc16: `n/a`
- child extaddr: `9653672b5e84f070`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **51.541 ms**
- selected-parent logged random delay: **41 ms**
- random-delay source router: `router1`
- random-delay source log time: `18:24:30.004`
- Request -> Response minus Random Delay: **10.541 ms**
- Response -> Child ID Request: **698.246 ms**
- Child ID Request -> Response: **14.801 ms**
- Full Attach: **764.588 ms**
- pcap parent request: `18:24:30.022` (frame 154)
- pcap parent response: `18:24:30.074` (frame 155)
- pcap child id request: `18:24:30.772` (frame 163)
- pcap child id response: `18:24:30.787` (frame 165)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `ce7ba201aa74dda6`
- parent rloc16: `n/a`
- child extaddr: `9653672b5e84f070`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **104.946 ms**
- selected-parent logged random delay: **96 ms**
- random-delay source router: `router2`
- random-delay source log time: `18:28:30.480`
- Request -> Response minus Random Delay: **8.946 ms**
- Response -> Child ID Request: **647.927 ms**
- Child ID Request -> Response: **14.166 ms**
- Full Attach: **767.039 ms**
- pcap parent request: `18:28:30.508` (frame 504)
- pcap parent response: `18:28:30.612` (frame 505)
- pcap child id request: `18:28:31.260` (frame 511)
- pcap child id response: `18:28:31.275` (frame 513)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-182851-run08.log`

- manifest status: `completed`
- child extaddr: `52ba17fe24028bbd`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `cbdc29c83a0a0fab31d5249a922e7633d6099dbf8029866afc776a235bb514d5` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `c2be103865629c78`
- parent rloc16: `n/a`
- child extaddr: `52ba17fe24028bbd`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **20.373 ms**
- selected-parent logged random delay: **12 ms**
- random-delay source router: `router1`
- random-delay source log time: `18:32:12.404`
- Request -> Response minus Random Delay: **8.373 ms**
- Response -> Child ID Request: **731.629 ms**
- Child ID Request -> Response: **14.531 ms**
- Full Attach: **766.533 ms**
- pcap parent request: `18:32:12.423` (frame 619)
- pcap parent response: `18:32:12.443` (frame 620)
- pcap child id request: `18:32:13.175` (frame 628)
- pcap child id response: `18:32:13.190` (frame 630)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `1a8acee2bac0edc0`
- parent rloc16: `n/a`
- child extaddr: `52ba17fe24028bbd`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **305.184 ms**
- selected-parent logged random delay: **296 ms**
- random-delay source router: `router2`
- random-delay source log time: `18:36:12.663`
- Request -> Response minus Random Delay: **9.184 ms**
- Response -> Child ID Request: **443.007 ms**
- Child ID Request -> Response: **15.08 ms**
- Full Attach: **763.271 ms**
- pcap parent request: `18:36:12.691` (frame 904)
- pcap parent response: `18:36:12.996` (frame 905)
- pcap child id request: `18:36:13.439` (frame 911)
- pcap child id response: `18:36:13.454` (frame 913)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-183634-run09.log`

- manifest status: `completed`
- child extaddr: `b6e1c04a802cf936`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `cbdc29c83a0a0fab31d5249a922e7633d6099dbf8029866afc776a235bb514d5` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `725415b0128339f6`
- parent rloc16: `n/a`
- child extaddr: `b6e1c04a802cf936`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **63.157 ms**
- selected-parent logged random delay: **54 ms**
- random-delay source router: `router2`
- random-delay source log time: `18:39:55.277`
- Request -> Response minus Random Delay: **9.157 ms**
- Response -> Child ID Request: **686.597 ms**
- Child ID Request -> Response: **14.568 ms**
- Full Attach: **764.322 ms**
- pcap parent request: `18:39:55.296` (frame 247)
- pcap parent response: `18:39:55.359` (frame 248)
- pcap child id request: `18:39:56.046` (frame 256)
- pcap child id response: `18:39:56.060` (frame 258)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `ba9a8be05a068a65`
- parent rloc16: `n/a`
- child extaddr: `b6e1c04a802cf936`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **133.607 ms**
- selected-parent logged random delay: **124 ms**
- random-delay source router: `router1`
- random-delay source log time: `18:43:55.392`
- Request -> Response minus Random Delay: **9.607 ms**
- Response -> Child ID Request: **617.376 ms**
- Child ID Request -> Response: **13.654 ms**
- Full Attach: **764.637 ms**
- pcap parent request: `18:43:55.420` (frame 515)
- pcap parent response: `18:43:55.554` (frame 518)
- pcap child id request: `18:43:56.171` (frame 522)
- pcap child id response: `18:43:56.185` (frame 524)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-184417-run10.log`

- manifest status: `completed`
- child extaddr: `724fe3e3980367ba`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `cbdc29c83a0a0fab31d5249a922e7633d6099dbf8029866afc776a235bb514d5` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `3e2e9def2f6050fb`
- parent rloc16: `n/a`
- child extaddr: `724fe3e3980367ba`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **196.408 ms**
- selected-parent logged random delay: **187 ms**
- random-delay source router: `router2`
- random-delay source log time: `18:47:37.911`
- Request -> Response minus Random Delay: **9.408 ms**
- Response -> Child ID Request: **554.544 ms**
- Child ID Request -> Response: **13.493 ms**
- Full Attach: **764.445 ms**
- pcap parent request: `18:47:37.930` (frame 141)
- pcap parent response: `18:47:38.126` (frame 144)
- pcap child id request: `18:47:38.681` (frame 150)
- pcap child id response: `18:47:38.694` (frame 152)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `226753e3d34fd0dd`
- parent rloc16: `n/a`
- child extaddr: `724fe3e3980367ba`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **485.186 ms**
- selected-parent logged random delay: **476 ms**
- random-delay source router: `router1`
- random-delay source log time: `18:51:38.309`
- Request -> Response minus Random Delay: **9.186 ms**
- Response -> Child ID Request: **265.818 ms**
- Child ID Request -> Response: **12.417 ms**
- Full Attach: **763.421 ms**
- pcap parent request: `18:51:38.338` (frame 425)
- pcap parent response: `18:51:38.823` (frame 430)
- pcap child id request: `18:51:39.089` (frame 433)
- pcap child id response: `18:51:39.101` (frame 435)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-185159-run11.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `7ae969f5f3d2f9d0`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `cbdc29c83a0a0fab31d5249a922e7633d6099dbf8029866afc776a235bb514d5` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `b2f55e1cd6015e3e`
- parent rloc16: `n/a`
- child extaddr: `7ae969f5f3d2f9d0`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **16.983 ms**
- selected-parent logged random delay: **8 ms**
- random-delay source router: `router1`
- random-delay source log time: `18:55:20.781`
- Request -> Response minus Random Delay: **8.983 ms**
- Response -> Child ID Request: **736.145 ms**
- Child ID Request -> Response: **13.006 ms**
- Full Attach: **766.134 ms**
- pcap parent request: `18:55:20.800` (frame 164)
- pcap parent response: `18:55:20.817` (frame 165)
- pcap child id request: `18:55:21.553` (frame 173)
- pcap child id response: `18:55:21.566` (frame 175)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `cedc1fd66c370a38`
- parent rloc16: `n/a`
- child extaddr: `7ae969f5f3d2f9d0`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **481.555 ms**
- selected-parent logged random delay: **472 ms**
- random-delay source router: `router2`
- random-delay source log time: `18:59:20.923`
- Request -> Response minus Random Delay: **9.555 ms**
- Response -> Child ID Request: **270.457 ms**
- Child ID Request -> Response: **14.542 ms**
- Full Attach: **766.554 ms**
- pcap parent request: `18:59:20.950` (frame 527)
- pcap parent response: `18:59:21.431` (frame 532)
- pcap child id request: `18:59:21.702` (frame 534)
- pcap child id response: `18:59:21.716` (frame 536)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-185942-run12.log`

- manifest status: `completed`
- child extaddr: `126fcf2a280116e8`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `cbdc29c83a0a0fab31d5249a922e7633d6099dbf8029866afc776a235bb514d5` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `6a9edc6d886a5e15`
- parent rloc16: `n/a`
- child extaddr: `126fcf2a280116e8`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **165.856 ms**
- selected-parent logged random delay: **155 ms**
- random-delay source router: `router2`
- random-delay source log time: `19:03:03.643`
- Request -> Response minus Random Delay: **10.856 ms**
- Response -> Child ID Request: **587.199 ms**
- Child ID Request -> Response: **13.071 ms**
- Full Attach: **766.126 ms**
- pcap parent request: `19:03:03.661` (frame 329)
- pcap parent response: `19:03:03.827` (frame 332)
- pcap child id request: `19:03:04.414` (frame 338)
- pcap child id response: `19:03:04.427` (frame 340)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `e2cace90ec762c74`
- parent rloc16: `n/a`
- child extaddr: `126fcf2a280116e8`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **498.102 ms**
- selected-parent logged random delay: **489 ms**
- random-delay source router: `router3`
- random-delay source log time: `19:07:04.237`
- Request -> Response minus Random Delay: **9.102 ms**
- Response -> Child ID Request: **251.204 ms**
- Child ID Request -> Response: **14.767 ms**
- Full Attach: **764.073 ms**
- pcap parent request: `19:07:04.264` (frame 1318)
- pcap parent response: `19:07:04.762` (frame 1323)
- pcap child id request: `19:07:05.013` (frame 1325)
- pcap child id response: `19:07:05.028` (frame 1327)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-190725-run13.log`

- manifest status: `completed`
- child extaddr: `7e7e4d6772f3f6ec`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `cbdc29c83a0a0fab31d5249a922e7633d6099dbf8029866afc776a235bb514d5` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `0678329ff3834080`
- parent rloc16: `n/a`
- child extaddr: `7e7e4d6772f3f6ec`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **139.093 ms**
- selected-parent logged random delay: **129 ms**
- random-delay source router: `router2`
- random-delay source log time: `19:10:46.528`
- Request -> Response minus Random Delay: **10.093 ms**
- Response -> Child ID Request: **614.97 ms**
- Child ID Request -> Response: **12.293 ms**
- Full Attach: **766.356 ms**
- pcap parent request: `19:10:46.548` (frame 141)
- pcap parent response: `19:10:46.687` (frame 142)
- pcap child id request: `19:10:47.302` (frame 152)
- pcap child id response: `19:10:47.314` (frame 154)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `aaf9c0b2023bf399`
- parent rloc16: `n/a`
- child extaddr: `7e7e4d6772f3f6ec`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **360.987 ms**
- selected-parent logged random delay: **353 ms**
- random-delay source router: `router1`
- random-delay source log time: `19:14:46.762`
- Request -> Response minus Random Delay: **7.987 ms**
- Response -> Child ID Request: **389.934 ms**
- Child ID Request -> Response: **14.323 ms**
- Full Attach: **765.244 ms**
- pcap parent request: `19:14:46.791` (frame 427)
- pcap parent response: `19:14:47.152` (frame 432)
- pcap child id request: `19:14:47.542` (frame 435)
- pcap child id response: `19:14:47.556` (frame 437)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-191508-run14.log`

- manifest status: `completed`
- child extaddr: `323d4a9c2e1386bf`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `cbdc29c83a0a0fab31d5249a922e7633d6099dbf8029866afc776a235bb514d5` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `e28d35f0b6b1f6f5`
- parent rloc16: `n/a`
- child extaddr: `323d4a9c2e1386bf`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **342.768 ms**
- selected-parent logged random delay: **329 ms**
- random-delay source router: `router2`
- random-delay source log time: `19:18:29.341`
- Request -> Response minus Random Delay: **13.768 ms**
- Response -> Child ID Request: **384.351 ms**
- Child ID Request -> Response: **12.965 ms**
- Full Attach: **740.084 ms**
- pcap parent request: `19:18:29.361` (frame 590)
- pcap parent response: `19:18:29.703` (frame 628)
- pcap child id request: `19:18:30.088` (frame 637)
- pcap child id response: `19:18:30.101` (frame 639)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `2e95b038b1b29ea6`
- parent rloc16: `n/a`
- child extaddr: `323d4a9c2e1386bf`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **395.708 ms**
- selected-parent logged random delay: **388 ms**
- random-delay source router: `router1`
- random-delay source log time: `19:22:29.269`
- Request -> Response minus Random Delay: **7.708 ms**
- Response -> Child ID Request: **356.289 ms**
- Child ID Request -> Response: **12.859 ms**
- Full Attach: **764.856 ms**
- pcap parent request: `19:22:29.297` (frame 1039)
- pcap parent response: `19:22:29.692` (frame 1044)
- pcap child id request: `19:22:30.049` (frame 1046)
- pcap child id response: `19:22:30.061` (frame 1048)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-192251-run15.log`

- manifest status: `completed`
- child extaddr: `02f6166109418739`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `cbdc29c83a0a0fab31d5249a922e7633d6099dbf8029866afc776a235bb514d5` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `26de034d6bbf58d9`
- parent rloc16: `n/a`
- child extaddr: `02f6166109418739`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **459.846 ms**
- selected-parent logged random delay: **451 ms**
- random-delay source router: `router2`
- random-delay source log time: `19:26:11.912`
- Request -> Response minus Random Delay: **8.846 ms**
- Response -> Child ID Request: **291.167 ms**
- Child ID Request -> Response: **14.843 ms**
- Full Attach: **765.856 ms**
- pcap parent request: `19:26:11.932` (frame 636)
- pcap parent response: `19:26:12.392` (frame 657)
- pcap child id request: `19:26:12.683` (frame 661)
- pcap child id response: `19:26:12.698` (frame 663)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `6a89263ea867794b`
- parent rloc16: `n/a`
- child extaddr: `02f6166109418739`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **459.128 ms**
- selected-parent logged random delay: **450 ms**
- random-delay source router: `router1`
- random-delay source log time: `19:30:12.239`
- Request -> Response minus Random Delay: **9.128 ms**
- Response -> Child ID Request: **291.856 ms**
- Child ID Request -> Response: **14.507 ms**
- Full Attach: **765.491 ms**
- pcap parent request: `19:30:12.268` (frame 1342)
- pcap parent response: `19:30:12.727` (frame 1346)
- pcap child id request: `19:30:13.019` (frame 1350)
- pcap child id response: `19:30:13.034` (frame 1352)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-193033-run16.log`

- manifest status: `completed`
- child extaddr: `cabed937ea19bddb`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `cbdc29c83a0a0fab31d5249a922e7633d6099dbf8029866afc776a235bb514d5` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `229dd4857a5cd575`
- parent rloc16: `n/a`
- child extaddr: `cabed937ea19bddb`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **22.706 ms**
- selected-parent logged random delay: **14 ms**
- random-delay source router: `router2`
- random-delay source log time: `19:33:54.430`
- Request -> Response minus Random Delay: **8.706 ms**
- Response -> Child ID Request: **728.284 ms**
- Child ID Request -> Response: **14.748 ms**
- Full Attach: **765.738 ms**
- pcap parent request: `19:33:54.450` (frame 150)
- pcap parent response: `19:33:54.473` (frame 151)
- pcap child id request: `19:33:55.201` (frame 160)
- pcap child id response: `19:33:55.216` (frame 162)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `1eaac4074ffffbd7`
- parent rloc16: `n/a`
- child extaddr: `cabed937ea19bddb`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **138.013 ms**
- selected-parent logged random delay: **128 ms**
- random-delay source router: `router1`
- random-delay source log time: `19:37:54.691`
- Request -> Response minus Random Delay: **10.013 ms**
- Response -> Child ID Request: **613.996 ms**
- Child ID Request -> Response: **14.047 ms**
- Full Attach: **766.056 ms**
- pcap parent request: `19:37:54.719` (frame 434)
- pcap parent response: `19:37:54.857` (frame 437)
- pcap child id request: `19:37:55.471` (frame 441)
- pcap child id response: `19:37:55.485` (frame 443)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-193816-run17.log`

- manifest status: `completed`
- child extaddr: `aa546d89f9a428a2`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `cbdc29c83a0a0fab31d5249a922e7633d6099dbf8029866afc776a235bb514d5` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `f259310bef345cff`
- parent rloc16: `n/a`
- child extaddr: `aa546d89f9a428a2`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **352.203 ms**
- selected-parent logged random delay: **342 ms**
- random-delay source router: `router2`
- random-delay source log time: `19:41:37.223`
- Request -> Response minus Random Delay: **10.203 ms**
- Response -> Child ID Request: **396.618 ms**
- Child ID Request -> Response: **14.423 ms**
- Full Attach: **763.244 ms**
- pcap parent request: `19:41:37.243` (frame 568)
- pcap parent response: `19:41:37.595` (frame 571)
- pcap child id request: `19:41:37.992` (frame 577)
- pcap child id response: `19:41:38.006` (frame 579)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `22f5231663006e30`
- parent rloc16: `n/a`
- child extaddr: `aa546d89f9a428a2`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **216.963 ms**
- selected-parent logged random delay: **207 ms**
- random-delay source router: `router1`
- random-delay source log time: `19:45:37.793`
- Request -> Response minus Random Delay: **9.963 ms**
- Response -> Child ID Request: **532.059 ms**
- Child ID Request -> Response: **12.968 ms**
- Full Attach: **761.99 ms**
- pcap parent request: `19:45:37.822` (frame 1011)
- pcap parent response: `19:45:38.039` (frame 1014)
- pcap child id request: `19:45:38.571` (frame 1018)
- pcap child id response: `19:45:38.584` (frame 1020)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-194559-run18.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `92a5f49ed82927a8`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `cbdc29c83a0a0fab31d5249a922e7633d6099dbf8029866afc776a235bb514d5` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `5a241995bb8b6555`
- parent rloc16: `n/a`
- child extaddr: `92a5f49ed82927a8`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **110.002 ms**
- selected-parent logged random delay: **99 ms**
- random-delay source router: `router1`
- random-delay source log time: `19:49:19.766`
- Request -> Response minus Random Delay: **11.002 ms**
- Response -> Child ID Request: **640.896 ms**
- Child ID Request -> Response: **14.147 ms**
- Full Attach: **765.045 ms**
- pcap parent request: `19:49:19.786` (frame 153)
- pcap parent response: `19:49:19.896` (frame 154)
- pcap child id request: `19:49:20.537` (frame 162)
- pcap child id response: `19:49:20.551` (frame 164)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `ea2cddfc7e7468e9`
- parent rloc16: `n/a`
- child extaddr: `92a5f49ed82927a8`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **371.348 ms**
- selected-parent logged random delay: **363 ms**
- random-delay source router: `router2`
- random-delay source log time: `19:53:20.350`
- Request -> Response minus Random Delay: **8.348 ms**
- Response -> Child ID Request: **379.648 ms**
- Child ID Request -> Response: **14.542 ms**
- Full Attach: **765.538 ms**
- pcap parent request: `19:53:20.378` (frame 510)
- pcap parent response: `19:53:20.749` (frame 512)
- pcap child id request: `19:53:21.129` (frame 518)
- pcap child id response: `19:53:21.144` (frame 520)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-195341-run19.log`

- manifest status: `completed`
- child extaddr: `c6f19aaf39866ade`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `cbdc29c83a0a0fab31d5249a922e7633d6099dbf8029866afc776a235bb514d5` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `d694dec4d452a2e6`
- parent rloc16: `n/a`
- child extaddr: `c6f19aaf39866ade`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **114.345 ms**
- selected-parent logged random delay: **104 ms**
- random-delay source router: `router2`
- random-delay source log time: `19:57:02.668`
- Request -> Response minus Random Delay: **10.345 ms**
- Response -> Child ID Request: **636.656 ms**
- Child ID Request -> Response: **13.386 ms**
- Full Attach: **764.387 ms**
- pcap parent request: `19:57:02.687` (frame 140)
- pcap parent response: `19:57:02.801` (frame 143)
- pcap child id request: `19:57:03.438` (frame 149)
- pcap child id response: `19:57:03.451` (frame 151)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `fe8ec676f5b9e8e8`
- parent rloc16: `n/a`
- child extaddr: `c6f19aaf39866ade`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **513.821 ms**
- selected-parent logged random delay: **499 ms**
- random-delay source router: `router1`
- random-delay source log time: `20:01:02.729`
- Request -> Response minus Random Delay: **14.821 ms**
- Response -> Child ID Request: **235.475 ms**
- Child ID Request -> Response: **13.606 ms**
- Full Attach: **762.902 ms**
- pcap parent request: `20:01:02.757` (frame 422)
- pcap parent response: `20:01:03.270` (frame 427)
- pcap child id request: `20:01:03.506` (frame 429)
- pcap child id response: `20:01:03.519` (frame 431)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-200124-run20.log`

- manifest status: `completed`
- child extaddr: `82019968f3f62f64`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `cbdc29c83a0a0fab31d5249a922e7633d6099dbf8029866afc776a235bb514d5` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `227168ec38d17911`
- parent rloc16: `n/a`
- child extaddr: `82019968f3f62f64`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **43.567 ms**
- selected-parent logged random delay: **34 ms**
- random-delay source router: `router2`
- random-delay source log time: `20:04:45.494`
- Request -> Response minus Random Delay: **9.567 ms**
- Response -> Child ID Request: **705.408 ms**
- Child ID Request -> Response: **13.631 ms**
- Full Attach: **762.606 ms**
- pcap parent request: `20:04:45.513` (frame 162)
- pcap parent response: `20:04:45.556` (frame 163)
- pcap child id request: `20:04:46.262` (frame 171)
- pcap child id response: `20:04:46.275` (frame 173)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `b6c60ed27577323d`
- parent rloc16: `n/a`
- child extaddr: `82019968f3f62f64`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **375.147 ms**
- selected-parent logged random delay: **367 ms**
- random-delay source router: `router1`
- random-delay source log time: `20:08:45.957`
- Request -> Response minus Random Delay: **8.147 ms**
- Response -> Child ID Request: **374.859 ms**
- Child ID Request -> Response: **13.417 ms**
- Full Attach: **763.423 ms**
- pcap parent request: `20:08:45.985` (frame 445)
- pcap parent response: `20:08:46.360` (frame 450)
- pcap child id request: `20:08:46.735` (frame 452)
- pcap child id response: `20:08:46.748` (frame 454)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**
