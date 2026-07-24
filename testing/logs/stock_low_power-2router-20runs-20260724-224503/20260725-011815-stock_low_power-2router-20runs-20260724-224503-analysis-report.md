# Child Log Analysis

## stock_child

Files analyzed: **20**

- batch folders: `stock_low_power-2router-20runs-20260724-224503`

### PCAP-complete child attach summary

| Attach | Metric | M (SD), ms | n |
| --- | --- | ---: | ---: |
| 1 | Request -> Response | 178.25 (138.89) | 20 |
| 1 | Request -> Response minus Random Delay | 9.50 (1.06) | 20 |
| 1 | Response -> Child ID Request | 573.06 (138.92) | 20 |
| 1 | Child ID Request -> Response | 14.16 (0.88) | 20 |
| 1 | Full Attach | 765.46 (1.57) | 20 |
| 2 | Request -> Response | 309.58 (148.59) | 20 |
| 2 | Request -> Response minus Random Delay | 9.58 (1.19) | 20 |
| 2 | Response -> Child ID Request | 441.41 (148.96) | 20 |
| 2 | Child ID Request -> Response | 13.87 (0.78) | 20 |
| 2 | Full Attach | 764.86 (1.50) | 20 |

| Metric | M (SD) | n |
| --- | ---: | ---: |
| Failed TX Attempts per Log | 0.00 (0.00) | 20 |
| Log-only or Partial Sequences per Log | 0.00 (0.00) | 20 |

### `stock_child_20260724-224700-run01.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `46b4bad1209bbeda`

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
- parent extaddr: `8acb766e240f8c25`
- parent rloc16: `n/a`
- child extaddr: `46b4bad1209bbeda`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **73.339 ms**
- selected-parent logged random delay: **63 ms**
- random-delay source router: `router1`
- random-delay source log time: `22:50:11.302`
- Request -> Response minus Random Delay: **10.339 ms**
- Response -> Child ID Request: **680.798 ms**
- Child ID Request -> Response: **12.479 ms**
- Full Attach: **766.616 ms**
- pcap parent request: `22:50:11.323` (frame 56)
- pcap parent response: `22:50:11.396` (frame 57)
- pcap child id request: `22:50:12.077` (frame 61)
- pcap child id response: `22:50:12.089` (frame 63)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `4e7cffaa4fc5d9a4`
- parent rloc16: `n/a`
- child extaddr: `46b4bad1209bbeda`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **357.592 ms**
- selected-parent logged random delay: **348 ms**
- random-delay source router: `router2`
- random-delay source log time: `22:54:11.926`
- Request -> Response minus Random Delay: **9.592 ms**
- Response -> Child ID Request: **393.43 ms**
- Child ID Request -> Response: **13.609 ms**
- Full Attach: **764.631 ms**
- pcap parent request: `22:54:11.955` (frame 214)
- pcap parent response: `22:54:12.313` (frame 215)
- pcap child id request: `22:54:12.706` (frame 217)
- pcap child id response: `22:54:12.720` (frame 219)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-225433-run02.log`

- manifest status: `completed`
- child extaddr: `326169bfd8524e20`

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
- parent extaddr: `b2953a3e3e86d0b7`
- parent rloc16: `n/a`
- child extaddr: `326169bfd8524e20`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **65.723 ms**
- selected-parent logged random delay: **55 ms**
- random-delay source router: `router2`
- random-delay source log time: `22:57:44.500`
- Request -> Response minus Random Delay: **10.723 ms**
- Response -> Child ID Request: **684.173 ms**
- Child ID Request -> Response: **13.864 ms**
- Full Attach: **763.76 ms**
- pcap parent request: `22:57:44.519` (frame 49)
- pcap parent response: `22:57:44.585` (frame 50)
- pcap child id request: `22:57:45.269` (frame 54)
- pcap child id response: `22:57:45.283` (frame 56)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `96d8d577521e8eec`
- parent rloc16: `n/a`
- child extaddr: `326169bfd8524e20`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **338.247 ms**
- selected-parent logged random delay: **327 ms**
- random-delay source router: `router1`
- random-delay source log time: `23:01:44.799`
- Request -> Response minus Random Delay: **11.247 ms**
- Response -> Child ID Request: **411.766 ms**
- Child ID Request -> Response: **14.254 ms**
- Full Attach: **764.267 ms**
- pcap parent request: `23:01:44.827` (frame 195)
- pcap parent response: `23:01:45.165` (frame 196)
- pcap child id request: `23:01:45.577` (frame 198)
- pcap child id response: `23:01:45.591` (frame 200)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-230206-run03.log`

- manifest status: `completed`
- child extaddr: `8e8a465a3aabb8ea`

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
- parent extaddr: `121766b4522722bb`
- parent rloc16: `n/a`
- child extaddr: `8e8a465a3aabb8ea`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **28.808 ms**
- selected-parent logged random delay: **20 ms**
- random-delay source router: `router2`
- random-delay source log time: `23:05:17.162`
- Request -> Response minus Random Delay: **8.808 ms**
- Response -> Child ID Request: **721.195 ms**
- Child ID Request -> Response: **16.081 ms**
- Full Attach: **766.084 ms**
- pcap parent request: `23:05:17.181` (frame 48)
- pcap parent response: `23:05:17.210` (frame 49)
- pcap child id request: `23:05:17.931` (frame 53)
- pcap child id response: `23:05:17.947` (frame 55)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `6285b9c68dad7d70`
- parent rloc16: `n/a`
- child extaddr: `8e8a465a3aabb8ea`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **492.358 ms**
- selected-parent logged random delay: **482 ms**
- random-delay source router: `router1`
- random-delay source log time: `23:09:17.282`
- Request -> Response minus Random Delay: **10.358 ms**
- Response -> Child ID Request: **258.661 ms**
- Child ID Request -> Response: **14.373 ms**
- Full Attach: **765.392 ms**
- pcap parent request: `23:09:17.310` (frame 193)
- pcap parent response: `23:09:17.802` (frame 195)
- pcap child id request: `23:09:18.061` (frame 197)
- pcap child id response: `23:09:18.075` (frame 199)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-230939-run04.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `720bfaa8ccd61b47`

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
- parent extaddr: `2e33f9df8e0f18da`
- parent rloc16: `n/a`
- child extaddr: `720bfaa8ccd61b47`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **235.535 ms**
- selected-parent logged random delay: **226 ms**
- random-delay source router: `router1`
- random-delay source log time: `23:12:49.502`
- Request -> Response minus Random Delay: **9.535 ms**
- Response -> Child ID Request: **515.459 ms**
- Child ID Request -> Response: **13.555 ms**
- Full Attach: **764.549 ms**
- pcap parent request: `23:12:49.522` (frame 49)
- pcap parent response: `23:12:49.757` (frame 50)
- pcap child id request: `23:12:50.272` (frame 54)
- pcap child id response: `23:12:50.286` (frame 56)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `3e0f135b7d6e07e8`
- parent rloc16: `n/a`
- child extaddr: `720bfaa8ccd61b47`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **38.915 ms**
- selected-parent logged random delay: **29 ms**
- random-delay source router: `router2`
- random-delay source log time: `23:16:49.961`
- Request -> Response minus Random Delay: **9.915 ms**
- Response -> Child ID Request: **713.11 ms**
- Child ID Request -> Response: **13.18 ms**
- Full Attach: **765.205 ms**
- pcap parent request: `23:16:49.989` (frame 208)
- pcap parent response: `23:16:50.028` (frame 209)
- pcap child id request: `23:16:50.741` (frame 211)
- pcap child id response: `23:16:50.755` (frame 213)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-231711-run05.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `46fdd64575cf12e0`

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
- parent extaddr: `f6fe8d359ce0e11b`
- parent rloc16: `n/a`
- child extaddr: `46fdd64575cf12e0`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **75.059 ms**
- selected-parent logged random delay: **65 ms**
- random-delay source router: `router1`
- random-delay source log time: `23:20:22.562`
- Request -> Response minus Random Delay: **10.059 ms**
- Response -> Child ID Request: **674.848 ms**
- Child ID Request -> Response: **14.177 ms**
- Full Attach: **764.084 ms**
- pcap parent request: `23:20:22.582` (frame 51)
- pcap parent response: `23:20:22.657` (frame 52)
- pcap child id request: `23:20:23.332` (frame 56)
- pcap child id response: `23:20:23.346` (frame 58)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `7eedfbee164521f8`
- parent rloc16: `n/a`
- child extaddr: `46fdd64575cf12e0`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **266.507 ms**
- selected-parent logged random delay: **258 ms**
- random-delay source router: `router2`
- random-delay source log time: `23:24:22.911`
- Request -> Response minus Random Delay: **8.507 ms**
- Response -> Child ID Request: **484.631 ms**
- Child ID Request -> Response: **14.523 ms**
- Full Attach: **765.661 ms**
- pcap parent request: `23:24:22.940` (frame 210)
- pcap parent response: `23:24:23.206` (frame 211)
- pcap child id request: `23:24:23.691` (frame 213)
- pcap child id response: `23:24:23.706` (frame 215)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-232444-run06.log`

- manifest status: `completed`
- child extaddr: `4afeb720a5266ced`

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
- parent extaddr: `de943d588d2ad77e`
- parent rloc16: `n/a`
- child extaddr: `4afeb720a5266ced`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **92.389 ms**
- selected-parent logged random delay: **81 ms**
- random-delay source router: `router2`
- random-delay source log time: `23:27:55.354`
- Request -> Response minus Random Delay: **11.389 ms**
- Response -> Child ID Request: **659.615 ms**
- Child ID Request -> Response: **14.423 ms**
- Full Attach: **766.427 ms**
- pcap parent request: `23:27:55.373` (frame 49)
- pcap parent response: `23:27:55.465` (frame 50)
- pcap child id request: `23:27:56.125` (frame 54)
- pcap child id response: `23:27:56.139` (frame 56)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `a6f124e617aeb68d`
- parent rloc16: `n/a`
- child extaddr: `4afeb720a5266ced`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **311.752 ms**
- selected-parent logged random delay: **304 ms**
- random-delay source router: `router1`
- random-delay source log time: `23:31:55.614`
- Request -> Response minus Random Delay: **7.752 ms**
- Response -> Child ID Request: **437.503 ms**
- Child ID Request -> Response: **14.675 ms**
- Full Attach: **763.93 ms**
- pcap parent request: `23:31:55.641` (frame 195)
- pcap parent response: `23:31:55.952` (frame 196)
- pcap child id request: `23:31:56.390` (frame 198)
- pcap child id response: `23:31:56.404` (frame 200)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-233217-run07.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `f6001b87ad57a31e`

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
- parent extaddr: `02baa91d99bd1acf`
- parent rloc16: `n/a`
- child extaddr: `f6001b87ad57a31e`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **20.037 ms**
- selected-parent logged random delay: **11 ms**
- random-delay source router: `router1`
- random-delay source log time: `23:35:28.417`
- Request -> Response minus Random Delay: **9.037 ms**
- Response -> Child ID Request: **730.96 ms**
- Child ID Request -> Response: **15.233 ms**
- Full Attach: **766.23 ms**
- pcap parent request: `23:35:28.437` (frame 53)
- pcap parent response: `23:35:28.457` (frame 54)
- pcap child id request: `23:35:29.188` (frame 58)
- pcap child id response: `23:35:29.203` (frame 60)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `06fb12f9a277dc1b`
- parent rloc16: `n/a`
- child extaddr: `f6001b87ad57a31e`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **142.418 ms**
- selected-parent logged random delay: **135 ms**
- random-delay source router: `router2`
- random-delay source log time: `23:39:28.681`
- Request -> Response minus Random Delay: **7.418 ms**
- Response -> Child ID Request: **605.787 ms**
- Child ID Request -> Response: **14.51 ms**
- Full Attach: **762.715 ms**
- pcap parent request: `23:39:28.709` (frame 212)
- pcap parent response: `23:39:28.851` (frame 213)
- pcap child id request: `23:39:29.457` (frame 215)
- pcap child id response: `23:39:29.472` (frame 217)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-233950-run08.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `167ae8fc569b2b26`

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
- parent extaddr: `06626fc45ae349c7`
- parent rloc16: `n/a`
- child extaddr: `167ae8fc569b2b26`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **391.629 ms**
- selected-parent logged random delay: **384 ms**
- random-delay source router: `router1`
- random-delay source log time: `23:43:01.025`
- Request -> Response minus Random Delay: **7.629 ms**
- Response -> Child ID Request: **357.217 ms**
- Child ID Request -> Response: **13.934 ms**
- Full Attach: **762.78 ms**
- pcap parent request: `23:43:01.043` (frame 55)
- pcap parent response: `23:43:01.434` (frame 56)
- pcap child id request: `23:43:01.792` (frame 60)
- pcap child id response: `23:43:01.806` (frame 62)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `32952ac45b62843d`
- parent rloc16: `n/a`
- child extaddr: `167ae8fc569b2b26`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **364.31 ms**
- selected-parent logged random delay: **353 ms**
- random-delay source router: `router2`
- random-delay source log time: `23:47:01.281`
- Request -> Response minus Random Delay: **11.31 ms**
- Response -> Child ID Request: **386.634 ms**
- Child ID Request -> Response: **12.667 ms**
- Full Attach: **763.611 ms**
- pcap parent request: `23:47:01.305` (frame 212)
- pcap parent response: `23:47:01.669` (frame 214)
- pcap child id request: `23:47:02.056` (frame 216)
- pcap child id response: `23:47:02.069` (frame 218)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-234722-run09.log`

- manifest status: `completed`
- child extaddr: `1ef53f605979a88e`

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
- parent extaddr: `32d19568baef365f`
- parent rloc16: `n/a`
- child extaddr: `1ef53f605979a88e`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **473.669 ms**
- selected-parent logged random delay: **464 ms**
- random-delay source router: `router2`
- random-delay source log time: `23:50:33.930`
- Request -> Response minus Random Delay: **9.669 ms**
- Response -> Child ID Request: **279.434 ms**
- Child ID Request -> Response: **14.594 ms**
- Full Attach: **767.697 ms**
- pcap parent request: `23:50:33.948` (frame 51)
- pcap parent response: `23:50:34.422` (frame 52)
- pcap child id request: `23:50:34.701` (frame 56)
- pcap child id response: `23:50:34.716` (frame 58)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `fe664f5a9399ee77`
- parent rloc16: `n/a`
- child extaddr: `1ef53f605979a88e`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **398.565 ms**
- selected-parent logged random delay: **388 ms**
- random-delay source router: `router1`
- random-delay source log time: `23:54:33.993`
- Request -> Response minus Random Delay: **10.565 ms**
- Response -> Child ID Request: **350.645 ms**
- Child ID Request -> Response: **12.617 ms**
- Full Attach: **761.827 ms**
- pcap parent request: `23:54:34.020` (frame 197)
- pcap parent response: `23:54:34.418` (frame 198)
- pcap child id request: `23:54:34.769` (frame 200)
- pcap child id response: `23:54:34.782` (frame 202)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-235455-run10.log`

- manifest status: `completed`
- child extaddr: `5eaa676811b9870b`

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
- parent extaddr: `b27caaa1439f25ca`
- parent rloc16: `n/a`
- child extaddr: `5eaa676811b9870b`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **99.03 ms**
- selected-parent logged random delay: **88 ms**
- random-delay source router: `router1`
- random-delay source log time: `00:02:06.244`
- Request -> Response minus Random Delay: **11.03 ms**
- Response -> Child ID Request: **654.757 ms**
- Child ID Request -> Response: **14.275 ms**
- Full Attach: **768.062 ms**
- pcap parent request: `00:02:06.271` (frame 200)
- pcap parent response: `00:02:06.370` (frame 201)
- pcap child id request: `00:02:07.025` (frame 203)
- pcap child id response: `00:02:07.039` (frame 205)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `163ec08ba3cbc682`
- parent rloc16: `n/a`
- child extaddr: `5eaa676811b9870b`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **80.359 ms**
- selected-parent logged random delay: **71 ms**
- random-delay source router: `router2`
- random-delay source log time: `23:58:06.296`
- Request -> Response minus Random Delay: **9.359 ms**
- Response -> Child ID Request: **670.641 ms**
- Child ID Request -> Response: **14.498 ms**
- Full Attach: **765.498 ms**
- pcap parent request: `23:58:06.314` (frame 53)
- pcap parent response: `23:58:06.395` (frame 54)
- pcap child id request: `23:58:07.065` (frame 58)
- pcap child id response: `23:58:07.080` (frame 60)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260725-000228-run11.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `3ecfb5d05175ea74`

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
- parent extaddr: `3a29144b805d2ffb`
- parent rloc16: `n/a`
- child extaddr: `3ecfb5d05175ea74`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **93.211 ms**
- selected-parent logged random delay: **84 ms**
- random-delay source router: `router1`
- random-delay source log time: `00:05:39.376`
- Request -> Response minus Random Delay: **9.211 ms**
- Response -> Child ID Request: **658.754 ms**
- Child ID Request -> Response: **14.358 ms**
- Full Attach: **766.323 ms**
- pcap parent request: `00:05:39.394` (frame 50)
- pcap parent response: `00:05:39.487` (frame 51)
- pcap child id request: `00:05:40.146` (frame 55)
- pcap child id response: `00:05:40.160` (frame 57)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `bec2f1f05e6c7d82`
- parent rloc16: `n/a`
- child extaddr: `3ecfb5d05175ea74`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **356.819 ms**
- selected-parent logged random delay: **348 ms**
- random-delay source router: `router2`
- random-delay source log time: `00:09:40.018`
- Request -> Response minus Random Delay: **8.819 ms**
- Response -> Child ID Request: **392.537 ms**
- Child ID Request -> Response: **14.49 ms**
- Full Attach: **763.846 ms**
- pcap parent request: `00:09:40.045` (frame 208)
- pcap parent response: `00:09:40.402` (frame 209)
- pcap child id request: `00:09:40.794` (frame 211)
- pcap child id response: `00:09:40.809` (frame 213)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260725-001001-run12.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `8a050e1d5216bb5e`

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
- parent extaddr: `8ebf69e8c25585d1`
- parent rloc16: `n/a`
- child extaddr: `8a050e1d5216bb5e`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **334.209 ms**
- selected-parent logged random delay: **324 ms**
- random-delay source router: `router1`
- random-delay source log time: `00:13:12.110`
- Request -> Response minus Random Delay: **10.209 ms**
- Response -> Child ID Request: **417.802 ms**
- Child ID Request -> Response: **14.226 ms**
- Full Attach: **766.237 ms**
- pcap parent request: `00:13:12.128` (frame 53)
- pcap parent response: `00:13:12.463` (frame 54)
- pcap child id request: `00:13:12.880` (frame 58)
- pcap child id response: `00:13:12.895` (frame 60)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `c6d80700f64d9066`
- parent rloc16: `n/a`
- child extaddr: `8a050e1d5216bb5e`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **509.03 ms**
- selected-parent logged random delay: **499 ms**
- random-delay source router: `router2`
- random-delay source log time: `00:17:12.266`
- Request -> Response minus Random Delay: **10.03 ms**
- Response -> Child ID Request: **241.153 ms**
- Child ID Request -> Response: **14.87 ms**
- Full Attach: **765.053 ms**
- pcap parent request: `00:17:12.293` (frame 212)
- pcap parent response: `00:17:12.802` (frame 213)
- pcap child id request: `00:17:13.044` (frame 215)
- pcap child id response: `00:17:13.058` (frame 217)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260725-001733-run13.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `d65c81e9292aded2`

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
- parent extaddr: `be75d97fecb29449`
- parent rloc16: `n/a`
- child extaddr: `d65c81e9292aded2`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **291.187 ms**
- selected-parent logged random delay: **281 ms**
- random-delay source router: `router1`
- random-delay source log time: `00:20:44.387`
- Request -> Response minus Random Delay: **10.187 ms**
- Response -> Child ID Request: **458.817 ms**
- Child ID Request -> Response: **13.215 ms**
- Full Attach: **763.219 ms**
- pcap parent request: `00:20:44.406` (frame 53)
- pcap parent response: `00:20:44.697` (frame 54)
- pcap child id request: `00:20:45.156` (frame 58)
- pcap child id response: `00:20:45.169` (frame 60)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `5204322ce6b8f148`
- parent rloc16: `n/a`
- child extaddr: `d65c81e9292aded2`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **485.743 ms**
- selected-parent logged random delay: **477 ms**
- random-delay source router: `router2`
- random-delay source log time: `00:24:44.638`
- Request -> Response minus Random Delay: **8.743 ms**
- Response -> Child ID Request: **266.256 ms**
- Child ID Request -> Response: **13.231 ms**
- Full Attach: **765.23 ms**
- pcap parent request: `00:24:44.665` (frame 211)
- pcap parent response: `00:24:45.150` (frame 213)
- pcap child id request: `00:24:45.417` (frame 215)
- pcap child id response: `00:24:45.430` (frame 217)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260725-002506-run14.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `3e594ec65439f52a`

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
- parent extaddr: `9efb1f9e41913cd5`
- parent rloc16: `n/a`
- child extaddr: `3e594ec65439f52a`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **203.441 ms**
- selected-parent logged random delay: **195 ms**
- random-delay source router: `router1`
- random-delay source log time: `00:28:17.537`
- Request -> Response minus Random Delay: **8.441 ms**
- Response -> Child ID Request: **547.57 ms**
- Child ID Request -> Response: **14.619 ms**
- Full Attach: **765.63 ms**
- pcap parent request: `00:28:17.555` (frame 52)
- pcap parent response: `00:28:17.758` (frame 53)
- pcap child id request: `00:28:18.306` (frame 57)
- pcap child id response: `00:28:18.321` (frame 59)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `ba3d84897e584c2c`
- parent rloc16: `n/a`
- child extaddr: `3e594ec65439f52a`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **227.2 ms**
- selected-parent logged random delay: **219 ms**
- random-delay source router: `router2`
- random-delay source log time: `00:32:18.208`
- Request -> Response minus Random Delay: **8.2 ms**
- Response -> Child ID Request: **524.82 ms**
- Child ID Request -> Response: **13.411 ms**
- Full Attach: **765.431 ms**
- pcap parent request: `00:32:18.235` (frame 211)
- pcap parent response: `00:32:18.462` (frame 212)
- pcap child id request: `00:32:18.987` (frame 214)
- pcap child id response: `00:32:19.000` (frame 216)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260725-003239-run15.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `3edaedd5a9fe333c`

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
- parent extaddr: `b64210a63a546a6f`
- parent rloc16: `n/a`
- child extaddr: `3edaedd5a9fe333c`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **115.889 ms**
- selected-parent logged random delay: **107 ms**
- random-delay source router: `router1`
- random-delay source log time: `00:35:50.013`
- Request -> Response minus Random Delay: **8.889 ms**
- Response -> Child ID Request: **635.117 ms**
- Child ID Request -> Response: **12.31 ms**
- Full Attach: **763.316 ms**
- pcap parent request: `00:35:50.032` (frame 48)
- pcap parent response: `00:35:50.147` (frame 49)
- pcap child id request: `00:35:50.783` (frame 54)
- pcap child id response: `00:35:50.795` (frame 56)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `8e96c8a828ea531f`
- parent rloc16: `n/a`
- child extaddr: `3edaedd5a9fe333c`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **360.96 ms**
- selected-parent logged random delay: **353 ms**
- random-delay source router: `router2`
- random-delay source log time: `00:39:50.218`
- Request -> Response minus Random Delay: **7.96 ms**
- Response -> Child ID Request: **390.052 ms**
- Child ID Request -> Response: **14.161 ms**
- Full Attach: **765.173 ms**
- pcap parent request: `00:39:50.246` (frame 206)
- pcap parent response: `00:39:50.607` (frame 207)
- pcap child id request: `00:39:50.997` (frame 209)
- pcap child id response: `00:39:51.011` (frame 211)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260725-004011-run16.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `0a2a82956bdc2488`

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
- parent extaddr: `fe898a15f5a0f1c1`
- parent rloc16: `n/a`
- child extaddr: `0a2a82956bdc2488`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **250.344 ms**
- selected-parent logged random delay: **240 ms**
- random-delay source router: `router1`
- random-delay source log time: `00:43:22.448`
- Request -> Response minus Random Delay: **10.344 ms**
- Response -> Child ID Request: **500.612 ms**
- Child ID Request -> Response: **14.425 ms**
- Full Attach: **765.381 ms**
- pcap parent request: `00:43:22.466` (frame 45)
- pcap parent response: `00:43:22.716` (frame 46)
- pcap child id request: `00:43:23.217` (frame 50)
- pcap child id response: `00:43:23.231` (frame 52)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `ae37efbbc4381819`
- parent rloc16: `n/a`
- child extaddr: `0a2a82956bdc2488`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **161.768 ms**
- selected-parent logged random delay: **152 ms**
- random-delay source router: `router2`
- random-delay source log time: `00:47:22.808`
- Request -> Response minus Random Delay: **9.768 ms**
- Response -> Child ID Request: **591.982 ms**
- Child ID Request -> Response: **13.318 ms**
- Full Attach: **767.068 ms**
- pcap parent request: `00:47:22.834` (frame 204)
- pcap parent response: `00:47:22.996` (frame 205)
- pcap child id request: `00:47:23.588` (frame 207)
- pcap child id response: `00:47:23.601` (frame 209)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260725-004744-run17.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `9643996eaf2f2b20`

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
- parent extaddr: `0ea844b4e066c2b6`
- parent rloc16: `n/a`
- child extaddr: `9643996eaf2f2b20`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **26.824 ms**
- selected-parent logged random delay: **18 ms**
- random-delay source router: `router1`
- random-delay source log time: `00:50:55.133`
- Request -> Response minus Random Delay: **8.824 ms**
- Response -> Child ID Request: **723.175 ms**
- Child ID Request -> Response: **13.864 ms**
- Full Attach: **763.863 ms**
- pcap parent request: `00:50:55.152` (frame 51)
- pcap parent response: `00:50:55.179` (frame 52)
- pcap child id request: `00:50:55.902` (frame 57)
- pcap child id response: `00:50:55.916` (frame 59)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `faa86a5d273396e9`
- parent rloc16: `n/a`
- child extaddr: `9643996eaf2f2b20`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **476.442 ms**
- selected-parent logged random delay: **466 ms**
- random-delay source router: `router2`
- random-delay source log time: `00:54:55.612`
- Request -> Response minus Random Delay: **10.442 ms**
- Response -> Child ID Request: **275.319 ms**
- Child ID Request -> Response: **12.96 ms**
- Full Attach: **764.721 ms**
- pcap parent request: `00:54:55.640` (frame 212)
- pcap parent response: `00:54:56.116` (frame 213)
- pcap child id request: `00:54:56.392` (frame 215)
- pcap child id response: `00:54:56.405` (frame 217)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260725-005517-run18.log`

- manifest status: `completed`
- child extaddr: `52d96eb8b5451e6e`

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
- parent extaddr: `1ac80eb800d3e829`
- parent rloc16: `n/a`
- child extaddr: `52d96eb8b5451e6e`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **60.75 ms**
- selected-parent logged random delay: **51 ms**
- random-delay source router: `router2`
- random-delay source log time: `00:58:28.212`
- Request -> Response minus Random Delay: **9.75 ms**
- Response -> Child ID Request: **692.354 ms**
- Child ID Request -> Response: **13.687 ms**
- Full Attach: **766.791 ms**
- pcap parent request: `00:58:28.229` (frame 48)
- pcap parent response: `00:58:28.290` (frame 49)
- pcap child id request: `00:58:28.983` (frame 53)
- pcap child id response: `00:58:28.996` (frame 55)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `92452a15e27e3764`
- parent rloc16: `n/a`
- child extaddr: `52d96eb8b5451e6e`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **242.872 ms**
- selected-parent logged random delay: **233 ms**
- random-delay source router: `router1`
- random-delay source log time: `01:02:28.355`
- Request -> Response minus Random Delay: **9.872 ms**
- Response -> Child ID Request: **510.878 ms**
- Child ID Request -> Response: **14.151 ms**
- Full Attach: **767.901 ms**
- pcap parent request: `01:02:28.381` (frame 195)
- pcap parent response: `01:02:28.624` (frame 196)
- pcap child id request: `01:02:29.134` (frame 198)
- pcap child id response: `01:02:29.149` (frame 200)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260725-010249-run19.log`

- manifest status: `completed`
- child extaddr: `26fccd755195ea43`

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
- parent extaddr: `6a631f6f3160c51e`
- parent rloc16: `n/a`
- child extaddr: `26fccd755195ea43`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **371.193 ms**
- selected-parent logged random delay: **363 ms**
- random-delay source router: `router2`
- random-delay source log time: `01:06:00.700`
- Request -> Response minus Random Delay: **8.193 ms**
- Response -> Child ID Request: **381.138 ms**
- Child ID Request -> Response: **14.999 ms**
- Full Attach: **767.33 ms**
- pcap parent request: `01:06:00.719` (frame 50)
- pcap parent response: `01:06:01.090` (frame 51)
- pcap child id request: `01:06:01.471` (frame 55)
- pcap child id response: `01:06:01.486` (frame 57)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `0e61852b1ec06f6e`
- parent rloc16: `n/a`
- child extaddr: `26fccd755195ea43`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **488.636 ms**
- selected-parent logged random delay: **478 ms**
- random-delay source router: `router1`
- random-delay source log time: `01:10:00.717`
- Request -> Response minus Random Delay: **10.636 ms**
- Response -> Child ID Request: **261.389 ms**
- Child ID Request -> Response: **12.813 ms**
- Full Attach: **762.838 ms**
- pcap parent request: `01:10:00.744` (frame 197)
- pcap parent response: `01:10:01.232` (frame 198)
- pcap child id request: `01:10:01.494` (frame 200)
- pcap child id response: `01:10:01.507` (frame 202)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260725-011022-run20.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `9a3490f2cda777f4`

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
- parent extaddr: `4a204d0845fec162`
- parent rloc16: `n/a`
- child extaddr: `9a3490f2cda777f4`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **262.657 ms**
- selected-parent logged random delay: **255 ms**
- random-delay source router: `router1`
- random-delay source log time: `01:13:33.530`
- Request -> Response minus Random Delay: **7.657 ms**
- Response -> Child ID Request: **487.35 ms**
- Child ID Request -> Response: **14.856 ms**
- Full Attach: **764.863 ms**
- pcap parent request: `01:13:33.547` (frame 49)
- pcap parent response: `01:13:33.810` (frame 50)
- pcap child id request: `01:13:34.297` (frame 54)
- pcap child id response: `01:13:34.312` (frame 56)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `1eeb8e50b29f16f4`
- parent rloc16: `n/a`
- child extaddr: `9a3490f2cda777f4`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **91.063 ms**
- selected-parent logged random delay: **80 ms**
- random-delay source router: `router2`
- random-delay source log time: `01:17:33.781`
- Request -> Response minus Random Delay: **11.063 ms**
- Response -> Child ID Request: **661.004 ms**
- Child ID Request -> Response: **15.045 ms**
- Full Attach: **767.112 ms**
- pcap parent request: `01:17:33.806` (frame 207)
- pcap parent response: `01:17:33.897` (frame 208)
- pcap child id request: `01:17:34.558` (frame 210)
- pcap child id response: `01:17:34.574` (frame 212)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**
