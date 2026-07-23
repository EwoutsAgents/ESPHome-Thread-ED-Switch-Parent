# Child Log Analysis

## stock_child

Files analyzed: **50**

- batch folders: `stock_low_power-4router-50runs-20260723-192223`

### PCAP-complete child attach summary

| Attach | Metric | M (SD), ms | n |
| --- | --- | ---: | ---: |
| 1 | Request -> Response | 189.29 (124.17) | 50 |
| 1 | Response -> Child ID Request | 561.91 (124.53) | 50 |
| 1 | Child ID Request -> Response | 13.88 (1.11) | 50 |
| 1 | Full Attach | 765.08 (1.85) | 50 |
| 2 | Request -> Response | 240.97 (145.92) | 50 |
| 2 | Response -> Child ID Request | 510.79 (145.62) | 50 |
| 2 | Child ID Request -> Response | 14.06 (1.18) | 50 |
| 2 | Full Attach | 765.82 (2.40) | 50 |

| Metric | M (SD) | n |
| --- | ---: | ---: |
| Failed TX Attempts per Log | 0.00 (0.00) | 50 |
| Log-only or Partial Sequences per Log | 0.00 (0.00) | 50 |

### `stock_child_20260723-192524-run01.log`

- manifest status: `completed`
- child extaddr: `aa0afc61e6264f9f`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `2f7071c89b0230d98eb36bdea1089514467b0ca5849d9a0bf1ff802e5253fa8b` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `da08fe08cad4c685`
- parent rloc16: `n/a`
- child extaddr: `aa0afc61e6264f9f`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **186.764 ms**
- Response -> Child ID Request: **563.264 ms**
- Child ID Request -> Response: **12.965 ms**
- Full Attach: **762.993 ms**
- pcap parent request: `19:28:43.822` (frame 811)
- pcap parent response: `19:28:44.009` (frame 814)
- pcap child id request: `19:28:44.572` (frame 820)
- pcap child id response: `19:28:44.585` (frame 822)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `06c36d66ba9b88be`
- parent rloc16: `n/a`
- child extaddr: `aa0afc61e6264f9f`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **20.241 ms**
- Response -> Child ID Request: **730.763 ms**
- Child ID Request -> Response: **13.279 ms**
- Full Attach: **764.283 ms**
- pcap parent request: `19:32:44.507` (frame 1133)
- pcap parent response: `19:32:44.527` (frame 1134)
- pcap child id request: `19:32:45.258` (frame 1141)
- pcap child id response: `19:32:45.271` (frame 1143)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260723-193306-run02.log`

- manifest status: `completed`
- child extaddr: `3a001c1142c6b457`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `2f7071c89b0230d98eb36bdea1089514467b0ca5849d9a0bf1ff802e5253fa8b` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `8e22ba7549f90a2c`
- parent rloc16: `n/a`
- child extaddr: `3a001c1142c6b457`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **123.007 ms**
- Response -> Child ID Request: **627.985 ms**
- Child ID Request -> Response: **14.047 ms**
- Full Attach: **765.039 ms**
- pcap parent request: `19:36:26.460` (frame 310)
- pcap parent response: `19:36:26.583` (frame 313)
- pcap child id request: `19:36:27.211` (frame 319)
- pcap child id response: `19:36:27.225` (frame 321)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `2e274e9cf3417ded`
- parent rloc16: `n/a`
- child extaddr: `3a001c1142c6b457`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **12.704 ms**
- Response -> Child ID Request: **738.313 ms**
- Child ID Request -> Response: **12.979 ms**
- Full Attach: **763.996 ms**
- pcap parent request: `19:40:26.949` (frame 592)
- pcap parent response: `19:40:26.962` (frame 593)
- pcap child id request: `19:40:27.700` (frame 599)
- pcap child id response: `19:40:27.713` (frame 601)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260723-194048-run03.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `b60122c408017c50`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `2f7071c89b0230d98eb36bdea1089514467b0ca5849d9a0bf1ff802e5253fa8b` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `227202cca4737b07`
- parent rloc16: `n/a`
- child extaddr: `b60122c408017c50`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **199.163 ms**
- Response -> Child ID Request: **553.98 ms**
- Child ID Request -> Response: **14.055 ms**
- Full Attach: **767.198 ms**
- pcap parent request: `19:44:09.522` (frame 165)
- pcap parent response: `19:44:09.721` (frame 168)
- pcap child id request: `19:44:10.275` (frame 174)
- pcap child id response: `19:44:10.289` (frame 176)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `56dacd1b351512a6`
- parent rloc16: `n/a`
- child extaddr: `b60122c408017c50`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **372.225 ms**
- Response -> Child ID Request: **379.753 ms**
- Child ID Request -> Response: **14.281 ms**
- Full Attach: **766.259 ms**
- pcap parent request: `19:48:09.811` (frame 517)
- pcap parent response: `19:48:10.183` (frame 523)
- pcap child id request: `19:48:10.563` (frame 525)
- pcap child id response: `19:48:10.577` (frame 527)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260723-194831-run04.log`

- manifest status: `completed`
- child extaddr: `0e7d87f9fb3f4dd8`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `2f7071c89b0230d98eb36bdea1089514467b0ca5849d9a0bf1ff802e5253fa8b` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `3a3f3899bcf9f5b1`
- parent rloc16: `n/a`
- child extaddr: `0e7d87f9fb3f4dd8`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **52.913 ms**
- Response -> Child ID Request: **698.088 ms**
- Child ID Request -> Response: **13.334 ms**
- Full Attach: **764.335 ms**
- pcap parent request: `19:51:51.940` (frame 701)
- pcap parent response: `19:51:51.993` (frame 702)
- pcap child id request: `19:51:52.691` (frame 714)
- pcap child id response: `19:51:52.705` (frame 716)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `de150edc630eb2c4`
- parent rloc16: `n/a`
- child extaddr: `0e7d87f9fb3f4dd8`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **330.635 ms**
- Response -> Child ID Request: **420.556 ms**
- Child ID Request -> Response: **14.481 ms**
- Full Attach: **765.672 ms**
- pcap parent request: `19:55:52.357` (frame 1178)
- pcap parent response: `19:55:52.688` (frame 1182)
- pcap child id request: `19:55:53.109` (frame 1186)
- pcap child id response: `19:55:53.123` (frame 1188)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260723-195613-run05.log`

- manifest status: `completed`
- child extaddr: `caeb7e172d9f027e`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `2f7071c89b0230d98eb36bdea1089514467b0ca5849d9a0bf1ff802e5253fa8b` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `6628be880ae05ed2`
- parent rloc16: `n/a`
- child extaddr: `caeb7e172d9f027e`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **252.134 ms**
- Response -> Child ID Request: **494.726 ms**
- Child ID Request -> Response: **14.312 ms**
- Full Attach: **761.172 ms**
- pcap parent request: `19:59:34.046` (frame 159)
- pcap parent response: `19:59:34.299` (frame 162)
- pcap child id request: `19:59:34.793` (frame 168)
- pcap child id response: `19:59:34.808` (frame 170)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `e66e460a2038e23b`
- parent rloc16: `n/a`
- child extaddr: `caeb7e172d9f027e`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **29.407 ms**
- Response -> Child ID Request: **722.62 ms**
- Child ID Request -> Response: **12.7 ms**
- Full Attach: **764.727 ms**
- pcap parent request: `20:03:34.318` (frame 440)
- pcap parent response: `20:03:34.347` (frame 443)
- pcap child id request: `20:03:35.070` (frame 447)
- pcap child id response: `20:03:35.082` (frame 449)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260723-200356-run06.log`

- manifest status: `completed`
- child extaddr: `6ec59e393097bb16`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `2f7071c89b0230d98eb36bdea1089514467b0ca5849d9a0bf1ff802e5253fa8b` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `5edd3bee9fb7f561`
- parent rloc16: `n/a`
- child extaddr: `6ec59e393097bb16`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **214.599 ms**
- Response -> Child ID Request: **538.691 ms**
- Child ID Request -> Response: **13.343 ms**
- Full Attach: **766.633 ms**
- pcap parent request: `20:07:16.712` (frame 237)
- pcap parent response: `20:07:16.926` (frame 238)
- pcap child id request: `20:07:17.465` (frame 246)
- pcap child id response: `20:07:17.478` (frame 248)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `66e57fbb5e6e1b23`
- parent rloc16: `n/a`
- child extaddr: `6ec59e393097bb16`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **206.019 ms**
- Response -> Child ID Request: **545.978 ms**
- Child ID Request -> Response: **13.061 ms**
- Full Attach: **765.058 ms**
- pcap parent request: `20:11:17.026` (frame 520)
- pcap parent response: `20:11:17.232` (frame 523)
- pcap child id request: `20:11:17.778` (frame 528)
- pcap child id response: `20:11:17.791` (frame 530)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260723-201138-run07.log`

- manifest status: `completed`
- child extaddr: `aa47f30c3fd6ac8f`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `2f7071c89b0230d98eb36bdea1089514467b0ca5849d9a0bf1ff802e5253fa8b` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `f62ca43c98ce766c`
- parent rloc16: `n/a`
- child extaddr: `aa47f30c3fd6ac8f`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **150.137 ms**
- Response -> Child ID Request: **600.844 ms**
- Child ID Request -> Response: **14.243 ms**
- Full Attach: **765.224 ms**
- pcap parent request: `20:15:00.028` (frame 509)
- pcap parent response: `20:15:00.178` (frame 514)
- pcap child id request: `20:15:00.779` (frame 518)
- pcap child id response: `20:15:00.793` (frame 520)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `7262f0635c3412e3`
- parent rloc16: `n/a`
- child extaddr: `aa47f30c3fd6ac8f`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **221.719 ms**
- Response -> Child ID Request: **535.18 ms**
- Child ID Request -> Response: **19.793 ms**
- Full Attach: **776.692 ms**
- pcap parent request: `20:19:00.645` (frame 1450)
- pcap parent response: `20:19:00.867` (frame 1453)
- pcap child id request: `20:19:01.402` (frame 1471)
- pcap child id response: `20:19:01.422` (frame 1474)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260723-201921-run08.log`

- manifest status: `completed`
- child extaddr: `be3a304d877fac2d`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `2f7071c89b0230d98eb36bdea1089514467b0ca5849d9a0bf1ff802e5253fa8b` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `7e9c4202ff88863d`
- parent rloc16: `n/a`
- child extaddr: `be3a304d877fac2d`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **123.465 ms**
- Response -> Child ID Request: **628.435 ms**
- Child ID Request -> Response: **12.804 ms**
- Full Attach: **764.704 ms**
- pcap parent request: `20:22:42.438` (frame 708)
- pcap parent response: `20:22:42.562` (frame 709)
- pcap child id request: `20:22:43.190` (frame 717)
- pcap child id response: `20:22:43.203` (frame 719)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `1a1301b28d0a51b5`
- parent rloc16: `n/a`
- child extaddr: `be3a304d877fac2d`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **145.4 ms**
- Response -> Child ID Request: **603.624 ms**
- Child ID Request -> Response: **14.423 ms**
- Full Attach: **763.447 ms**
- pcap parent request: `20:26:42.718` (frame 1725)
- pcap parent response: `20:26:42.864` (frame 1726)
- pcap child id request: `20:26:43.468` (frame 1732)
- pcap child id response: `20:26:43.482` (frame 1734)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260723-202704-run09.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `022311b96af8b806`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `2f7071c89b0230d98eb36bdea1089514467b0ca5849d9a0bf1ff802e5253fa8b` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `1e1325b63911479e`
- parent rloc16: `n/a`
- child extaddr: `022311b96af8b806`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **160.529 ms**
- Response -> Child ID Request: **588.492 ms**
- Child ID Request -> Response: **13.555 ms**
- Full Attach: **762.576 ms**
- pcap parent request: `20:30:25.181` (frame 172)
- pcap parent response: `20:30:25.341` (frame 176)
- pcap child id request: `20:30:25.930` (frame 182)
- pcap child id response: `20:30:25.943` (frame 184)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `1a8931653bc1fc61`
- parent rloc16: `n/a`
- child extaddr: `022311b96af8b806`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **476.441 ms**
- Response -> Child ID Request: **275.554 ms**
- Child ID Request -> Response: **14.469 ms**
- Full Attach: **766.464 ms**
- pcap parent request: `20:34:25.472` (frame 530)
- pcap parent response: `20:34:25.948` (frame 535)
- pcap child id request: `20:34:26.224` (frame 537)
- pcap child id response: `20:34:26.238` (frame 539)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260723-203446-run10.log`

- manifest status: `completed`
- child extaddr: `b28bb479b96de9a7`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `2f7071c89b0230d98eb36bdea1089514467b0ca5849d9a0bf1ff802e5253fa8b` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `e2c0c8bb3924444f`
- parent rloc16: `n/a`
- child extaddr: `b28bb479b96de9a7`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **58.762 ms**
- Response -> Child ID Request: **692.237 ms**
- Child ID Request -> Response: **15.131 ms**
- Full Attach: **766.13 ms**
- pcap parent request: `20:38:07.828` (frame 143)
- pcap parent response: `20:38:07.887` (frame 144)
- pcap child id request: `20:38:08.579` (frame 152)
- pcap child id response: `20:38:08.594` (frame 154)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `f68faf0a418f1088`
- parent rloc16: `n/a`
- child extaddr: `b28bb479b96de9a7`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **260.798 ms**
- Response -> Child ID Request: **492.953 ms**
- Child ID Request -> Response: **13.088 ms**
- Full Attach: **766.839 ms**
- pcap parent request: `20:42:08.148` (frame 428)
- pcap parent response: `20:42:08.409` (frame 433)
- pcap child id request: `20:42:08.902` (frame 435)
- pcap child id response: `20:42:08.915` (frame 437)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260723-204229-run11.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `fabde422a271c1b3`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `2f7071c89b0230d98eb36bdea1089514467b0ca5849d9a0bf1ff802e5253fa8b` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `4a83aa55ba5c5768`
- parent rloc16: `n/a`
- child extaddr: `fabde422a271c1b3`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **175.866 ms**
- Response -> Child ID Request: **575.146 ms**
- Child ID Request -> Response: **14.889 ms**
- Full Attach: **765.901 ms**
- pcap parent request: `20:45:50.136` (frame 162)
- pcap parent response: `20:45:50.312` (frame 166)
- pcap child id request: `20:45:50.887` (frame 172)
- pcap child id response: `20:45:50.902` (frame 174)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `8e1f5d935582ca14`
- parent rloc16: `n/a`
- child extaddr: `fabde422a271c1b3`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **43.149 ms**
- Response -> Child ID Request: **707.867 ms**
- Child ID Request -> Response: **13.538 ms**
- Full Attach: **764.554 ms**
- pcap parent request: `20:49:50.767` (frame 539)
- pcap parent response: `20:49:50.810` (frame 540)
- pcap child id request: `20:49:51.518` (frame 546)
- pcap child id response: `20:49:51.531` (frame 548)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260723-205012-run12.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `1255f858f8fcb4f6`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `2f7071c89b0230d98eb36bdea1089514467b0ca5849d9a0bf1ff802e5253fa8b` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `7aa6270469cffa23`
- parent rloc16: `n/a`
- child extaddr: `1255f858f8fcb4f6`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **41.918 ms**
- Response -> Child ID Request: **711.244 ms**
- Child ID Request -> Response: **14.194 ms**
- Full Attach: **767.356 ms**
- pcap parent request: `20:53:32.992` (frame 180)
- pcap parent response: `20:53:33.034` (frame 181)
- pcap child id request: `20:53:33.745` (frame 189)
- pcap child id response: `20:53:33.759` (frame 191)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `c6b920b7fea563c7`
- parent rloc16: `n/a`
- child extaddr: `1255f858f8fcb4f6`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **312.991 ms**
- Response -> Child ID Request: **436.041 ms**
- Child ID Request -> Response: **14.991 ms**
- Full Attach: **764.023 ms**
- pcap parent request: `20:57:33.107` (frame 521)
- pcap parent response: `20:57:33.420` (frame 526)
- pcap child id request: `20:57:33.856` (frame 528)
- pcap child id response: `20:57:33.871` (frame 530)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260723-205755-run13.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `a69997724a5800f3`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `2f7071c89b0230d98eb36bdea1089514467b0ca5849d9a0bf1ff802e5253fa8b` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `4a9d07eba6d76027`
- parent rloc16: `n/a`
- child extaddr: `a69997724a5800f3`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **214.224 ms**
- Response -> Child ID Request: **537.771 ms**
- Child ID Request -> Response: **12.49 ms**
- Full Attach: **764.485 ms**
- pcap parent request: `21:01:15.432` (frame 144)
- pcap parent response: `21:01:15.646` (frame 147)
- pcap child id request: `21:01:16.184` (frame 153)
- pcap child id response: `21:01:16.196` (frame 155)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `765902efedc044c8`
- parent rloc16: `n/a`
- child extaddr: `a69997724a5800f3`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **80.214 ms**
- Response -> Child ID Request: **669.793 ms**
- Child ID Request -> Response: **13.26 ms**
- Full Attach: **763.267 ms**
- pcap parent request: `21:05:16.105` (frame 506)
- pcap parent response: `21:05:16.186` (frame 509)
- pcap child id request: `21:05:16.855` (frame 513)
- pcap child id response: `21:05:16.869` (frame 515)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260723-210537-run14.log`

- manifest status: `completed`
- child extaddr: `3aa16b8ebb9487f5`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `2f7071c89b0230d98eb36bdea1089514467b0ca5849d9a0bf1ff802e5253fa8b` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `42d88266adc90ec2`
- parent rloc16: `n/a`
- child extaddr: `3aa16b8ebb9487f5`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **276.432 ms**
- Response -> Child ID Request: **476.548 ms**
- Child ID Request -> Response: **14.479 ms**
- Full Attach: **767.459 ms**
- pcap parent request: `21:08:57.984` (frame 582)
- pcap parent response: `21:08:58.261` (frame 587)
- pcap child id request: `21:08:58.737` (frame 591)
- pcap child id response: `21:08:58.752` (frame 593)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `52452f6d37fd45df`
- parent rloc16: `n/a`
- child extaddr: `3aa16b8ebb9487f5`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **315.775 ms**
- Response -> Child ID Request: **436.21 ms**
- Child ID Request -> Response: **14.828 ms**
- Full Attach: **766.813 ms**
- pcap parent request: `21:12:58.102` (frame 1085)
- pcap parent response: `21:12:58.418` (frame 1088)
- pcap child id request: `21:12:58.854` (frame 1092)
- pcap child id response: `21:12:58.869` (frame 1094)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260723-211320-run15.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `2af44bb90c0c8aaa`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `2f7071c89b0230d98eb36bdea1089514467b0ca5849d9a0bf1ff802e5253fa8b` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `8e81051481d86f38`
- parent rloc16: `n/a`
- child extaddr: `2af44bb90c0c8aaa`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **190.848 ms**
- Response -> Child ID Request: **559.11 ms**
- Child ID Request -> Response: **14.916 ms**
- Full Attach: **764.874 ms**
- pcap parent request: `21:16:40.986` (frame 162)
- pcap parent response: `21:16:41.177` (frame 166)
- pcap child id request: `21:16:41.736` (frame 172)
- pcap child id response: `21:16:41.751` (frame 174)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `024b0e381a7af875`
- parent rloc16: `n/a`
- child extaddr: `2af44bb90c0c8aaa`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **248.372 ms**
- Response -> Child ID Request: **505.395 ms**
- Child ID Request -> Response: **15.017 ms**
- Full Attach: **768.784 ms**
- pcap parent request: `21:20:41.225` (frame 511)
- pcap parent response: `21:20:41.474` (frame 516)
- pcap child id request: `21:20:41.979` (frame 518)
- pcap child id response: `21:20:41.994` (frame 520)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260723-212103-run16.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `5246a89b976661ce`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `2f7071c89b0230d98eb36bdea1089514467b0ca5849d9a0bf1ff802e5253fa8b` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `c2b6c06c56ef6c27`
- parent rloc16: `n/a`
- child extaddr: `5246a89b976661ce`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **292.118 ms**
- Response -> Child ID Request: **460.997 ms**
- Child ID Request -> Response: **12.249 ms**
- Full Attach: **765.364 ms**
- pcap parent request: `21:24:23.761` (frame 206)
- pcap parent response: `21:24:24.053` (frame 209)
- pcap child id request: `21:24:24.514` (frame 215)
- pcap child id response: `21:24:24.526` (frame 217)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `a2de95c019c2580a`
- parent rloc16: `n/a`
- child extaddr: `5246a89b976661ce`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **415.746 ms**
- Response -> Child ID Request: **335.17 ms**
- Child ID Request -> Response: **14.138 ms**
- Full Attach: **765.054 ms**
- pcap parent request: `21:28:24.059` (frame 573)
- pcap parent response: `21:28:24.475` (frame 578)
- pcap child id request: `21:28:24.810` (frame 580)
- pcap child id response: `21:28:24.824` (frame 582)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260723-212845-run17.log`

- manifest status: `completed`
- child extaddr: `92d78ffc94420c1c`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `2f7071c89b0230d98eb36bdea1089514467b0ca5849d9a0bf1ff802e5253fa8b` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `6a4d29b33f5c44c3`
- parent rloc16: `n/a`
- child extaddr: `92d78ffc94420c1c`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **353.097 ms**
- Response -> Child ID Request: **395.906 ms**
- Child ID Request -> Response: **12.599 ms**
- Full Attach: **761.602 ms**
- pcap parent request: `21:32:06.590` (frame 274)
- pcap parent response: `21:32:06.943` (frame 275)
- pcap child id request: `21:32:07.339` (frame 283)
- pcap child id response: `21:32:07.352` (frame 285)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `e21434bc82b81192`
- parent rloc16: `n/a`
- child extaddr: `92d78ffc94420c1c`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **446.906 ms**
- Response -> Child ID Request: **306.974 ms**
- Child ID Request -> Response: **13.436 ms**
- Full Attach: **767.316 ms**
- pcap parent request: `21:36:07.213` (frame 558)
- pcap parent response: `21:36:07.660` (frame 563)
- pcap child id request: `21:36:07.967` (frame 565)
- pcap child id response: `21:36:07.981` (frame 567)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260723-213628-run18.log`

- manifest status: `completed`
- child extaddr: `ced1ae8aa9523ffc`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `2f7071c89b0230d98eb36bdea1089514467b0ca5849d9a0bf1ff802e5253fa8b` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `12f7e273ad0f2f06`
- parent rloc16: `n/a`
- child extaddr: `ced1ae8aa9523ffc`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **404.708 ms**
- Response -> Child ID Request: **344.99 ms**
- Child ID Request -> Response: **15.034 ms**
- Full Attach: **764.732 ms**
- pcap parent request: `21:39:49.754` (frame 355)
- pcap parent response: `21:39:50.158` (frame 360)
- pcap child id request: `21:39:50.503` (frame 364)
- pcap child id response: `21:39:50.518` (frame 366)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `2e1f2fa94623f370`
- parent rloc16: `n/a`
- child extaddr: `ced1ae8aa9523ffc`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **160.396 ms**
- Response -> Child ID Request: **590.614 ms**
- Child ID Request -> Response: **14.425 ms**
- Full Attach: **765.435 ms**
- pcap parent request: `21:43:49.917` (frame 1219)
- pcap parent response: `21:43:50.077` (frame 1220)
- pcap child id request: `21:43:50.668` (frame 1226)
- pcap child id response: `21:43:50.682` (frame 1228)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260723-214411-run19.log`

- manifest status: `completed`
- child extaddr: `66b90c753a24e4ff`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `2f7071c89b0230d98eb36bdea1089514467b0ca5849d9a0bf1ff802e5253fa8b` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `ea1e7a935fed87b8`
- parent rloc16: `n/a`
- child extaddr: `66b90c753a24e4ff`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **236.239 ms**
- Response -> Child ID Request: **514.755 ms**
- Child ID Request -> Response: **14.256 ms**
- Full Attach: **765.25 ms**
- pcap parent request: `21:47:31.787` (frame 187)
- pcap parent response: `21:47:32.023` (frame 188)
- pcap child id request: `21:47:32.538` (frame 196)
- pcap child id response: `21:47:32.552` (frame 198)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `fe6ce6e6c098ca2f`
- parent rloc16: `n/a`
- child extaddr: `66b90c753a24e4ff`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **162.051 ms**
- Response -> Child ID Request: **589.955 ms**
- Child ID Request -> Response: **14.094 ms**
- Full Attach: **766.1 ms**
- pcap parent request: `21:51:32.284` (frame 471)
- pcap parent response: `21:51:32.446` (frame 472)
- pcap child id request: `21:51:33.036` (frame 478)
- pcap child id response: `21:51:33.050` (frame 480)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260723-215154-run20.log`

- manifest status: `completed`
- child extaddr: `4e08ce218a875693`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `2f7071c89b0230d98eb36bdea1089514467b0ca5849d9a0bf1ff802e5253fa8b` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `fa522528da7f5dbb`
- parent rloc16: `n/a`
- child extaddr: `4e08ce218a875693`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **223.907 ms**
- Response -> Child ID Request: **526.093 ms**
- Child ID Request -> Response: **13.171 ms**
- Full Attach: **763.171 ms**
- pcap parent request: `21:55:14.565` (frame 668)
- pcap parent response: `21:55:14.789` (frame 671)
- pcap child id request: `21:55:15.315` (frame 677)
- pcap child id response: `21:55:15.328` (frame 679)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `d2b77a973b4b0fe7`
- parent rloc16: `n/a`
- child extaddr: `4e08ce218a875693`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **280.076 ms**
- Response -> Child ID Request: **471.011 ms**
- Child ID Request -> Response: **15.03 ms**
- Full Attach: **766.117 ms**
- pcap parent request: `21:59:14.580` (frame 1385)
- pcap parent response: `21:59:14.860` (frame 1388)
- pcap child id request: `21:59:15.331` (frame 1392)
- pcap child id response: `21:59:15.346` (frame 1394)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260723-215936-run21.log`

- manifest status: `completed`
- child extaddr: `665cc168a1354558`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `2f7071c89b0230d98eb36bdea1089514467b0ca5849d9a0bf1ff802e5253fa8b` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `6e6d0cfc2083fd48`
- parent rloc16: `n/a`
- child extaddr: `665cc168a1354558`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **27.233 ms**
- Response -> Child ID Request: **722.73 ms**
- Child ID Request -> Response: **13.317 ms**
- Full Attach: **763.28 ms**
- pcap parent request: `22:02:57.432` (frame 160)
- pcap parent response: `22:02:57.459` (frame 161)
- pcap child id request: `22:02:58.182` (frame 169)
- pcap child id response: `22:02:58.195` (frame 171)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `c60e8e711732309f`
- parent rloc16: `n/a`
- child extaddr: `665cc168a1354558`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **455.317 ms**
- Response -> Child ID Request: **299.419 ms**
- Child ID Request -> Response: **14.614 ms**
- Full Attach: **769.35 ms**
- pcap parent request: `22:06:58.048` (frame 442)
- pcap parent response: `22:06:58.503` (frame 447)
- pcap child id request: `22:06:58.803` (frame 449)
- pcap child id response: `22:06:58.817` (frame 451)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260723-220719-run22.log`

- manifest status: `completed`
- child extaddr: `7ad75ccccb351ce0`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `2f7071c89b0230d98eb36bdea1089514467b0ca5849d9a0bf1ff802e5253fa8b` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `c251b08e28f9be5a`
- parent rloc16: `n/a`
- child extaddr: `7ad75ccccb351ce0`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **21.9 ms**
- Response -> Child ID Request: **727.069 ms**
- Child ID Request -> Response: **14.32 ms**
- Full Attach: **763.289 ms**
- pcap parent request: `22:10:40.117` (frame 250)
- pcap parent response: `22:10:40.139` (frame 251)
- pcap child id request: `22:10:40.866` (frame 259)
- pcap child id response: `22:10:40.880` (frame 261)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `96ef3718059ff136`
- parent rloc16: `n/a`
- child extaddr: `7ad75ccccb351ce0`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **358.12 ms**
- Response -> Child ID Request: **392.893 ms**
- Child ID Request -> Response: **12.731 ms**
- Full Attach: **763.744 ms**
- pcap parent request: `22:14:40.479` (frame 531)
- pcap parent response: `22:14:40.837` (frame 536)
- pcap child id request: `22:14:41.230` (frame 539)
- pcap child id response: `22:14:41.243` (frame 541)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260723-221502-run23.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `026cbef589711ef6`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `2f7071c89b0230d98eb36bdea1089514467b0ca5849d9a0bf1ff802e5253fa8b` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `0e73ad86c346b297`
- parent rloc16: `n/a`
- child extaddr: `026cbef589711ef6`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **163.687 ms**
- Response -> Child ID Request: **587.379 ms**
- Child ID Request -> Response: **18.591 ms**
- Full Attach: **769.657 ms**
- pcap parent request: `22:18:22.795` (frame 282)
- pcap parent response: `22:18:22.958` (frame 285)
- pcap child id request: `22:18:23.546` (frame 292)
- pcap child id response: `22:18:23.564` (frame 294)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `e60df3437e2664a5`
- parent rloc16: `n/a`
- child extaddr: `026cbef589711ef6`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **183.026 ms**
- Response -> Child ID Request: **569.946 ms**
- Child ID Request -> Response: **14.105 ms**
- Full Attach: **767.077 ms**
- pcap parent request: `22:22:23.342` (frame 644)
- pcap parent response: `22:22:23.525` (frame 645)
- pcap child id request: `22:22:24.095` (frame 651)
- pcap child id response: `22:22:24.109` (frame 653)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260723-222244-run24.log`

- manifest status: `completed`
- child extaddr: `ce7fd29fecb46e14`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `2f7071c89b0230d98eb36bdea1089514467b0ca5849d9a0bf1ff802e5253fa8b` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `d27bdadd4f6f02d9`
- parent rloc16: `n/a`
- child extaddr: `ce7fd29fecb46e14`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **339.423 ms**
- Response -> Child ID Request: **411.572 ms**
- Child ID Request -> Response: **14.83 ms**
- Full Attach: **765.825 ms**
- pcap parent request: `22:26:05.250` (frame 262)
- pcap parent response: `22:26:05.589` (frame 267)
- pcap child id request: `22:26:06.001` (frame 271)
- pcap child id response: `22:26:06.016` (frame 273)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `d2accce4e83389d1`
- parent rloc16: `n/a`
- child extaddr: `ce7fd29fecb46e14`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **286.175 ms**
- Response -> Child ID Request: **466.568 ms**
- Child ID Request -> Response: **14.473 ms**
- Full Attach: **767.216 ms**
- pcap parent request: `22:30:05.527` (frame 543)
- pcap parent response: `22:30:05.813` (frame 548)
- pcap child id request: `22:30:06.280` (frame 550)
- pcap child id response: `22:30:06.294` (frame 552)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260723-223027-run25.log`

- manifest status: `completed`
- child extaddr: `622ca6fbbd8997c5`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `2f7071c89b0230d98eb36bdea1089514467b0ca5849d9a0bf1ff802e5253fa8b` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `269182df51dc9717`
- parent rloc16: `n/a`
- child extaddr: `622ca6fbbd8997c5`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **79.302 ms**
- Response -> Child ID Request: **673.826 ms**
- Child ID Request -> Response: **13.54 ms**
- Full Attach: **766.668 ms**
- pcap parent request: `22:33:48.674` (frame 311)
- pcap parent response: `22:33:48.754` (frame 314)
- pcap child id request: `22:33:49.427` (frame 321)
- pcap child id response: `22:33:49.441` (frame 323)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `de8cdefeeb13906c`
- parent rloc16: `n/a`
- child extaddr: `622ca6fbbd8997c5`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **90.419 ms**
- Response -> Child ID Request: **659.712 ms**
- Child ID Request -> Response: **12.536 ms**
- Full Attach: **762.667 ms**
- pcap parent request: `22:37:49.085` (frame 595)
- pcap parent response: `22:37:49.176` (frame 596)
- pcap child id request: `22:37:49.836` (frame 603)
- pcap child id response: `22:37:49.848` (frame 605)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260723-223810-run26.log`

- manifest status: `completed`
- child extaddr: `7aa98d12a7db6c62`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `2f7071c89b0230d98eb36bdea1089514467b0ca5849d9a0bf1ff802e5253fa8b` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `3a21ea68feda8204`
- parent rloc16: `n/a`
- child extaddr: `7aa98d12a7db6c62`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **495.474 ms**
- Response -> Child ID Request: **255.577 ms**
- Child ID Request -> Response: **15.445 ms**
- Full Attach: **766.496 ms**
- pcap parent request: `22:41:31.043` (frame 617)
- pcap parent response: `22:41:31.539` (frame 624)
- pcap child id request: `22:41:31.794` (frame 626)
- pcap child id response: `22:41:31.810` (frame 628)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `be925771ed969366`
- parent rloc16: `n/a`
- child extaddr: `7aa98d12a7db6c62`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **155.398 ms**
- Response -> Child ID Request: **595.891 ms**
- Child ID Request -> Response: **12.608 ms**
- Full Attach: **763.897 ms**
- pcap parent request: `22:45:31.065` (frame 1575)
- pcap parent response: `22:45:31.221` (frame 1583)
- pcap child id request: `22:45:31.817` (frame 1598)
- pcap child id response: `22:45:31.829` (frame 1600)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260723-224553-run27.log`

- manifest status: `completed`
- child extaddr: `1a451e4f2651b7da`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `2f7071c89b0230d98eb36bdea1089514467b0ca5849d9a0bf1ff802e5253fa8b` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `1ad82c489b2cef78`
- parent rloc16: `n/a`
- child extaddr: `1a451e4f2651b7da`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **84.666 ms**
- Response -> Child ID Request: **667.171 ms**
- Child ID Request -> Response: **13.2 ms**
- Full Attach: **765.037 ms**
- pcap parent request: `22:49:14.062` (frame 201)
- pcap parent response: `22:49:14.146` (frame 202)
- pcap child id request: `22:49:14.813` (frame 210)
- pcap child id response: `22:49:14.827` (frame 212)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `3eec45d0fa8e878c`
- parent rloc16: `n/a`
- child extaddr: `1a451e4f2651b7da`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **109.504 ms**
- Response -> Child ID Request: **640.52 ms**
- Child ID Request -> Response: **14.527 ms**
- Full Attach: **764.551 ms**
- pcap parent request: `22:53:14.303` (frame 485)
- pcap parent response: `22:53:14.412` (frame 488)
- pcap child id request: `22:53:15.053` (frame 492)
- pcap child id response: `22:53:15.067` (frame 494)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260723-225335-run28.log`

- manifest status: `completed`
- child extaddr: `3acb41fdf5e57401`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `2f7071c89b0230d98eb36bdea1089514467b0ca5849d9a0bf1ff802e5253fa8b` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `e2db8cd617c35080`
- parent rloc16: `n/a`
- child extaddr: `3acb41fdf5e57401`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **179.108 ms**
- Response -> Child ID Request: **572.656 ms**
- Child ID Request -> Response: **12.566 ms**
- Full Attach: **764.33 ms**
- pcap parent request: `22:56:56.209` (frame 677)
- pcap parent response: `22:56:56.388` (frame 680)
- pcap child id request: `22:56:56.960` (frame 686)
- pcap child id response: `22:56:56.973` (frame 688)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `f68d3415db3f6b46`
- parent rloc16: `n/a`
- child extaddr: `3acb41fdf5e57401`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **320.187 ms**
- Response -> Child ID Request: **433.547 ms**
- Child ID Request -> Response: **13.928 ms**
- Full Attach: **767.662 ms**
- pcap parent request: `23:00:56.784` (frame 1502)
- pcap parent response: `23:00:57.104` (frame 1507)
- pcap child id request: `23:00:57.538` (frame 1509)
- pcap child id response: `23:00:57.552` (frame 1511)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260723-230118-run29.log`

- manifest status: `completed`
- child extaddr: `5eb47ab7c1d7b312`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `2f7071c89b0230d98eb36bdea1089514467b0ca5849d9a0bf1ff802e5253fa8b` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `a2ab20cee388f102`
- parent rloc16: `n/a`
- child extaddr: `5eb47ab7c1d7b312`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **330.265 ms**
- Response -> Child ID Request: **420.737 ms**
- Child ID Request -> Response: **13.303 ms**
- Full Attach: **764.305 ms**
- pcap parent request: `23:04:39.253` (frame 613)
- pcap parent response: `23:04:39.583` (frame 628)
- pcap child id request: `23:04:40.004` (frame 637)
- pcap child id response: `23:04:40.017` (frame 639)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `0a6d350a88125dca`
- parent rloc16: `n/a`
- child extaddr: `5eb47ab7c1d7b312`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **475.519 ms**
- Response -> Child ID Request: **273.667 ms**
- Child ID Request -> Response: **13.571 ms**
- Full Attach: **762.757 ms**
- pcap parent request: `23:08:39.342` (frame 1650)
- pcap parent response: `23:08:39.817` (frame 1655)
- pcap child id request: `23:08:40.091` (frame 1658)
- pcap child id response: `23:08:40.105` (frame 1660)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260723-230901-run30.log`

- manifest status: `completed`
- child extaddr: `fe2bac6f520d4356`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `2f7071c89b0230d98eb36bdea1089514467b0ca5849d9a0bf1ff802e5253fa8b` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `ceaae380c08c25c0`
- parent rloc16: `n/a`
- child extaddr: `fe2bac6f520d4356`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **212.999 ms**
- Response -> Child ID Request: **538.992 ms**
- Child ID Request -> Response: **13.394 ms**
- Full Attach: **765.385 ms**
- pcap parent request: `23:12:22.098` (frame 502)
- pcap parent response: `23:12:22.311` (frame 507)
- pcap child id request: `23:12:22.850` (frame 511)
- pcap child id response: `23:12:22.863` (frame 513)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `fef5e766a8cdc04c`
- parent rloc16: `n/a`
- child extaddr: `fe2bac6f520d4356`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **354.122 ms**
- Response -> Child ID Request: **396.206 ms**
- Child ID Request -> Response: **13.018 ms**
- Full Attach: **763.346 ms**
- pcap parent request: `23:16:22.423` (frame 1066)
- pcap parent response: `23:16:22.777` (frame 1071)
- pcap child id request: `23:16:23.173` (frame 1073)
- pcap child id response: `23:16:23.186` (frame 1075)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260723-231644-run31.log`

- manifest status: `completed`
- child extaddr: `a2ce4de755e2f50d`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `2f7071c89b0230d98eb36bdea1089514467b0ca5849d9a0bf1ff802e5253fa8b` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `da4577d2bddad202`
- parent rloc16: `n/a`
- child extaddr: `a2ce4de755e2f50d`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **20.636 ms**
- Response -> Child ID Request: **730.359 ms**
- Child ID Request -> Response: **12.894 ms**
- Full Attach: **763.889 ms**
- pcap parent request: `23:20:04.935` (frame 601)
- pcap parent response: `23:20:04.955` (frame 602)
- pcap child id request: `23:20:05.686` (frame 610)
- pcap child id response: `23:20:05.699` (frame 612)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `6214da6f478df854`
- parent rloc16: `n/a`
- child extaddr: `a2ce4de755e2f50d`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **114.445 ms**
- Response -> Child ID Request: **635.859 ms**
- Child ID Request -> Response: **12.365 ms**
- Full Attach: **762.669 ms**
- pcap parent request: `23:24:05.091` (frame 893)
- pcap parent response: `23:24:05.205` (frame 894)
- pcap child id request: `23:24:05.841` (frame 900)
- pcap child id response: `23:24:05.853` (frame 902)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260723-232427-run32.log`

- manifest status: `completed`
- child extaddr: `c6ffccfd21c27b46`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `2f7071c89b0230d98eb36bdea1089514467b0ca5849d9a0bf1ff802e5253fa8b` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `969852679da7b7f3`
- parent rloc16: `n/a`
- child extaddr: `c6ffccfd21c27b46`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **77.567 ms**
- Response -> Child ID Request: **675.489 ms**
- Child ID Request -> Response: **13.882 ms**
- Full Attach: **766.938 ms**
- pcap parent request: `23:27:47.707` (frame 602)
- pcap parent response: `23:27:47.785` (frame 603)
- pcap child id request: `23:27:48.460` (frame 612)
- pcap child id response: `23:27:48.474` (frame 614)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `daa7e0b8540c1405`
- parent rloc16: `n/a`
- child extaddr: `c6ffccfd21c27b46`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **487.671 ms**
- Response -> Child ID Request: **262.514 ms**
- Child ID Request -> Response: **14.759 ms**
- Full Attach: **764.944 ms**
- pcap parent request: `23:31:47.987` (frame 1620)
- pcap parent response: `23:31:48.475` (frame 1625)
- pcap child id request: `23:31:48.737` (frame 1627)
- pcap child id response: `23:31:48.752` (frame 1629)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260723-233209-run33.log`

- manifest status: `completed`
- child extaddr: `e62ba6fc9c1ed83f`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `2f7071c89b0230d98eb36bdea1089514467b0ca5849d9a0bf1ff802e5253fa8b` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `16bc56d65a2285bd`
- parent rloc16: `n/a`
- child extaddr: `e62ba6fc9c1ed83f`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **179.13 ms**
- Response -> Child ID Request: **571.925 ms**
- Child ID Request -> Response: **14.173 ms**
- Full Attach: **765.228 ms**
- pcap parent request: `23:35:30.730` (frame 231)
- pcap parent response: `23:35:30.909` (frame 237)
- pcap child id request: `23:35:31.481` (frame 242)
- pcap child id response: `23:35:31.495` (frame 244)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `b200a745a5a9ab25`
- parent rloc16: `n/a`
- child extaddr: `e62ba6fc9c1ed83f`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **78.58 ms**
- Response -> Child ID Request: **670.611 ms**
- Child ID Request -> Response: **13.433 ms**
- Full Attach: **762.624 ms**
- pcap parent request: `23:39:31.174` (frame 515)
- pcap parent response: `23:39:31.253` (frame 516)
- pcap child id request: `23:39:31.923` (frame 522)
- pcap child id response: `23:39:31.937` (frame 524)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260723-233952-run34.log`

- manifest status: `completed`
- child extaddr: `9e95e902453e307a`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `2f7071c89b0230d98eb36bdea1089514467b0ca5849d9a0bf1ff802e5253fa8b` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `9a8198ce92330346`
- parent rloc16: `n/a`
- child extaddr: `9e95e902453e307a`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **284.252 ms**
- Response -> Child ID Request: **465.675 ms**
- Child ID Request -> Response: **12.555 ms**
- Full Attach: **762.482 ms**
- pcap parent request: `23:43:13.383` (frame 522)
- pcap parent response: `23:43:13.668` (frame 527)
- pcap child id request: `23:43:14.133` (frame 531)
- pcap child id response: `23:43:14.146` (frame 533)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `ba9d8b9450fbe8fb`
- parent rloc16: `n/a`
- child extaddr: `9e95e902453e307a`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **98.646 ms**
- Response -> Child ID Request: **654.355 ms**
- Child ID Request -> Response: **12.884 ms**
- Full Attach: **765.885 ms**
- pcap parent request: `23:47:13.346` (frame 1210)
- pcap parent response: `23:47:13.445` (frame 1211)
- pcap child id request: `23:47:14.099` (frame 1217)
- pcap child id response: `23:47:14.112` (frame 1219)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260723-234735-run35.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `de0b04e6a48f0a77`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `2f7071c89b0230d98eb36bdea1089514467b0ca5849d9a0bf1ff802e5253fa8b` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `ea2df585397660e5`
- parent rloc16: `n/a`
- child extaddr: `de0b04e6a48f0a77`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **23.882 ms**
- Response -> Child ID Request: **729.121 ms**
- Child ID Request -> Response: **12.927 ms**
- Full Attach: **765.93 ms**
- pcap parent request: `23:50:56.580` (frame 292)
- pcap parent response: `23:50:56.604` (frame 293)
- pcap child id request: `23:50:57.333` (frame 301)
- pcap child id response: `23:50:57.346` (frame 303)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `86bdc70e71454fa5`
- parent rloc16: `n/a`
- child extaddr: `de0b04e6a48f0a77`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **172.402 ms**
- Response -> Child ID Request: **580.595 ms**
- Child ID Request -> Response: **13.716 ms**
- Full Attach: **766.713 ms**
- pcap parent request: `23:54:56.773` (frame 626)
- pcap parent response: `23:54:56.945` (frame 627)
- pcap child id request: `23:54:57.526` (frame 631)
- pcap child id response: `23:54:57.540` (frame 633)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260723-235518-run36.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `46befce169968840`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `2f7071c89b0230d98eb36bdea1089514467b0ca5849d9a0bf1ff802e5253fa8b` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `3208c7828773847c`
- parent rloc16: `n/a`
- child extaddr: `46befce169968840`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **330.771 ms**
- Response -> Child ID Request: **421.218 ms**
- Child ID Request -> Response: **15.085 ms**
- Full Attach: **767.074 ms**
- pcap parent request: `00:02:39.285` (frame 500)
- pcap parent response: `00:02:39.616` (frame 501)
- pcap child id request: `00:02:40.037` (frame 505)
- pcap child id response: `00:02:40.052` (frame 507)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `aefe536551d8bc23`
- parent rloc16: `n/a`
- child extaddr: `46befce169968840`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **395.473 ms**
- Response -> Child ID Request: **356.669 ms**
- Child ID Request -> Response: **12.572 ms**
- Full Attach: **764.714 ms**
- pcap parent request: `23:58:39.172` (frame 163)
- pcap parent response: `23:58:39.567` (frame 168)
- pcap child id request: `23:58:39.924` (frame 172)
- pcap child id response: `23:58:39.937` (frame 174)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-000301-run37.log`

- manifest status: `completed`
- child extaddr: `b2ee3fc86e62275e`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `2f7071c89b0230d98eb36bdea1089514467b0ca5849d9a0bf1ff802e5253fa8b` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `3255e18e83d6761b`
- parent rloc16: `n/a`
- child extaddr: `b2ee3fc86e62275e`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **104.897 ms**
- Response -> Child ID Request: **646.104 ms**
- Child ID Request -> Response: **13.944 ms**
- Full Attach: **764.945 ms**
- pcap parent request: `00:06:22.115` (frame 423)
- pcap parent response: `00:06:22.220` (frame 426)
- pcap child id request: `00:06:22.866` (frame 432)
- pcap child id response: `00:06:22.880` (frame 434)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `7e2262caaa151eb4`
- parent rloc16: `n/a`
- child extaddr: `b2ee3fc86e62275e`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **410.706 ms**
- Response -> Child ID Request: **342.057 ms**
- Child ID Request -> Response: **13.967 ms**
- Full Attach: **766.73 ms**
- pcap parent request: `00:10:22.338` (frame 710)
- pcap parent response: `00:10:22.749` (frame 713)
- pcap child id request: `00:10:23.091` (frame 717)
- pcap child id response: `00:10:23.105` (frame 719)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-001044-run38.log`

- manifest status: `completed`
- child extaddr: `262cd19dcdd409df`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `2f7071c89b0230d98eb36bdea1089514467b0ca5849d9a0bf1ff802e5253fa8b` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `663546b5f48638bb`
- parent rloc16: `n/a`
- child extaddr: `262cd19dcdd409df`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **99.022 ms**
- Response -> Child ID Request: **653.972 ms**
- Child ID Request -> Response: **12.587 ms**
- Full Attach: **765.581 ms**
- pcap parent request: `00:14:04.981` (frame 457)
- pcap parent response: `00:14:05.080` (frame 460)
- pcap child id request: `00:14:05.734` (frame 466)
- pcap child id response: `00:14:05.747` (frame 468)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `c26744a252874bf5`
- parent rloc16: `n/a`
- child extaddr: `262cd19dcdd409df`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **99.849 ms**
- Response -> Child ID Request: **652.149 ms**
- Child ID Request -> Response: **14.882 ms**
- Full Attach: **766.88 ms**
- pcap parent request: `00:18:05.174` (frame 739)
- pcap parent response: `00:18:05.274` (frame 740)
- pcap child id request: `00:18:05.926` (frame 746)
- pcap child id response: `00:18:05.941` (frame 748)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-001827-run39.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `66b416586b4de28e`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `2f7071c89b0230d98eb36bdea1089514467b0ca5849d9a0bf1ff802e5253fa8b` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `6adfdef4260ecbca`
- parent rloc16: `n/a`
- child extaddr: `66b416586b4de28e`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **77.538 ms**
- Response -> Child ID Request: **673.467 ms**
- Child ID Request -> Response: **13.567 ms**
- Full Attach: **764.572 ms**
- pcap parent request: `00:21:48.263` (frame 292)
- pcap parent response: `00:21:48.340` (frame 295)
- pcap child id request: `00:21:49.014` (frame 301)
- pcap child id response: `00:21:49.027` (frame 303)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `1e95b34f09dab5ef`
- parent rloc16: `n/a`
- child extaddr: `66b416586b4de28e`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **25.099 ms**
- Response -> Child ID Request: **726.071 ms**
- Child ID Request -> Response: **14.34 ms**
- Full Attach: **765.51 ms**
- pcap parent request: `00:25:48.406` (frame 654)
- pcap parent response: `00:25:48.431` (frame 655)
- pcap child id request: `00:25:49.157` (frame 661)
- pcap child id response: `00:25:49.171` (frame 663)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-002609-run40.log`

- manifest status: `completed`
- child extaddr: `0e19acdced9fa133`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `2f7071c89b0230d98eb36bdea1089514467b0ca5849d9a0bf1ff802e5253fa8b` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `e646401c6d8cf78b`
- parent rloc16: `n/a`
- child extaddr: `0e19acdced9fa133`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **101.82 ms**
- Response -> Child ID Request: **649.189 ms**
- Child ID Request -> Response: **12.404 ms**
- Full Attach: **763.413 ms**
- pcap parent request: `00:29:31.015` (frame 209)
- pcap parent response: `00:29:31.117` (frame 210)
- pcap child id request: `00:29:31.766` (frame 218)
- pcap child id response: `00:29:31.779` (frame 220)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `7292c91a8385dfc5`
- parent rloc16: `n/a`
- child extaddr: `0e19acdced9fa133`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **212.317 ms**
- Response -> Child ID Request: **538.669 ms**
- Child ID Request -> Response: **14.363 ms**
- Full Attach: **765.349 ms**
- pcap parent request: `00:33:31.116` (frame 492)
- pcap parent response: `00:33:31.329` (frame 493)
- pcap child id request: `00:33:31.867` (frame 499)
- pcap child id response: `00:33:31.882` (frame 501)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-003352-run41.log`

- manifest status: `completed`
- child extaddr: `b27e9cde234090c6`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `2f7071c89b0230d98eb36bdea1089514467b0ca5849d9a0bf1ff802e5253fa8b` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `a667d52bf611614b`
- parent rloc16: `n/a`
- child extaddr: `b27e9cde234090c6`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **251.998 ms**
- Response -> Child ID Request: **495.274 ms**
- Child ID Request -> Response: **13.185 ms**
- Full Attach: **760.457 ms**
- pcap parent request: `00:37:13.170` (frame 232)
- pcap parent response: `00:37:13.422` (frame 235)
- pcap child id request: `00:37:13.917` (frame 241)
- pcap child id response: `00:37:13.930` (frame 243)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `faf59535e867796f`
- parent rloc16: `n/a`
- child extaddr: `b27e9cde234090c6`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **44.338 ms**
- Response -> Child ID Request: **708.386 ms**
- Child ID Request -> Response: **14.667 ms**
- Full Attach: **767.391 ms**
- pcap parent request: `00:41:13.848` (frame 517)
- pcap parent response: `00:41:13.893` (frame 518)
- pcap child id request: `00:41:14.601` (frame 524)
- pcap child id response: `00:41:14.616` (frame 526)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-004135-run42.log`

- manifest status: `completed`
- child extaddr: `b29668eb3bdc867d`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `2f7071c89b0230d98eb36bdea1089514467b0ca5849d9a0bf1ff802e5253fa8b` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `d66c9620e5149ea7`
- parent rloc16: `n/a`
- child extaddr: `b29668eb3bdc867d`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **348.337 ms**
- Response -> Child ID Request: **401.555 ms**
- Child ID Request -> Response: **14.786 ms**
- Full Attach: **764.678 ms**
- pcap parent request: `00:44:56.211` (frame 154)
- pcap parent response: `00:44:56.559` (frame 160)
- pcap child id request: `00:44:56.961` (frame 164)
- pcap child id response: `00:44:56.976` (frame 166)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `c65060593859209f`
- parent rloc16: `n/a`
- child extaddr: `b29668eb3bdc867d`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **125.786 ms**
- Response -> Child ID Request: **626.196 ms**
- Child ID Request -> Response: **14.841 ms**
- Full Attach: **766.823 ms**
- pcap parent request: `00:48:56.188` (frame 420)
- pcap parent response: `00:48:56.314` (frame 421)
- pcap child id request: `00:48:56.940` (frame 427)
- pcap child id response: `00:48:56.955` (frame 429)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-004918-run43.log`

- manifest status: `completed`
- child extaddr: `82528634cfe74b65`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `2f7071c89b0230d98eb36bdea1089514467b0ca5849d9a0bf1ff802e5253fa8b` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `6e90d104d2655849`
- parent rloc16: `n/a`
- child extaddr: `82528634cfe74b65`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **439.865 ms**
- Response -> Child ID Request: **310.118 ms**
- Child ID Request -> Response: **14.906 ms**
- Full Attach: **764.889 ms**
- pcap parent request: `00:52:39.098` (frame 752)
- pcap parent response: `00:52:39.538` (frame 759)
- pcap child id request: `00:52:39.848` (frame 761)
- pcap child id response: `00:52:39.863` (frame 763)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `c60b6419de250aaa`
- parent rloc16: `n/a`
- child extaddr: `82528634cfe74b65`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **232.643 ms**
- Response -> Child ID Request: **517.367 ms**
- Child ID Request -> Response: **13.678 ms**
- Full Attach: **763.688 ms**
- pcap parent request: `00:56:39.094` (frame 1056)
- pcap parent response: `00:56:39.327` (frame 1060)
- pcap child id request: `00:56:39.844` (frame 1065)
- pcap child id response: `00:56:39.858` (frame 1067)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-005701-run44.log`

- manifest status: `completed`
- child extaddr: `9eb52d2e106d636d`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `2f7071c89b0230d98eb36bdea1089514467b0ca5849d9a0bf1ff802e5253fa8b` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `569995253d52fc8e`
- parent rloc16: `n/a`
- child extaddr: `9eb52d2e106d636d`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **296.594 ms**
- Response -> Child ID Request: **454.406 ms**
- Child ID Request -> Response: **14.638 ms**
- Full Attach: **765.638 ms**
- pcap parent request: `01:00:22.133` (frame 565)
- pcap parent response: `01:00:22.430` (frame 568)
- pcap child id request: `01:00:22.884` (frame 574)
- pcap child id response: `01:00:22.899` (frame 576)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `2adbbb7221142216`
- parent rloc16: `n/a`
- child extaddr: `9eb52d2e106d636d`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **419.373 ms**
- Response -> Child ID Request: **331.641 ms**
- Child ID Request -> Response: **14.385 ms**
- Full Attach: **765.399 ms**
- pcap parent request: `01:04:22.732` (frame 875)
- pcap parent response: `01:04:23.152` (frame 878)
- pcap child id request: `01:04:23.483` (frame 882)
- pcap child id response: `01:04:23.498` (frame 884)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-010443-run45.log`

- manifest status: `completed`
- child extaddr: `12b14e45a09c6646`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `2f7071c89b0230d98eb36bdea1089514467b0ca5849d9a0bf1ff802e5253fa8b` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `721aaaf19b7ba310`
- parent rloc16: `n/a`
- child extaddr: `12b14e45a09c6646`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **145.469 ms**
- Response -> Child ID Request: **606.529 ms**
- Child ID Request -> Response: **14.749 ms**
- Full Attach: **766.747 ms**
- pcap parent request: `01:08:04.313` (frame 180)
- pcap parent response: `01:08:04.458` (frame 185)
- pcap child id request: `01:08:05.065` (frame 189)
- pcap child id response: `01:08:05.080` (frame 191)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `2eec48cdebd7f0d4`
- parent rloc16: `n/a`
- child extaddr: `12b14e45a09c6646`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **311.275 ms**
- Response -> Child ID Request: **442.503 ms**
- Child ID Request -> Response: **14.514 ms**
- Full Attach: **768.292 ms**
- pcap parent request: `01:12:04.575` (frame 463)
- pcap parent response: `01:12:04.886` (frame 466)
- pcap child id request: `01:12:05.329` (frame 470)
- pcap child id response: `01:12:05.344` (frame 472)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-011226-run46.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `0258a5d3d1077712`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `2f7071c89b0230d98eb36bdea1089514467b0ca5849d9a0bf1ff802e5253fa8b` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `46092598088c48e6`
- parent rloc16: `n/a`
- child extaddr: `0258a5d3d1077712`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **19.362 ms**
- Response -> Child ID Request: **731.568 ms**
- Child ID Request -> Response: **13.679 ms**
- Full Attach: **764.609 ms**
- pcap parent request: `01:15:46.868` (frame 233)
- pcap parent response: `01:15:46.888` (frame 234)
- pcap child id request: `01:15:47.619` (frame 240)
- pcap child id response: `01:15:47.633` (frame 242)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `ea8fa9394e7244e0`
- parent rloc16: `n/a`
- child extaddr: `0258a5d3d1077712`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **83.971 ms**
- Response -> Child ID Request: **667.038 ms**
- Child ID Request -> Response: **14.01 ms**
- Full Attach: **765.019 ms**
- pcap parent request: `01:19:46.845` (frame 605)
- pcap parent response: `01:19:46.929` (frame 606)
- pcap child id request: `01:19:47.596` (frame 612)
- pcap child id response: `01:19:47.610` (frame 614)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-012009-run47.log`

- manifest status: `completed`
- child extaddr: `56b08e721f5fd932`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `2f7071c89b0230d98eb36bdea1089514467b0ca5849d9a0bf1ff802e5253fa8b` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `c6c92296075ad140`
- parent rloc16: `n/a`
- child extaddr: `56b08e721f5fd932`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **98.108 ms**
- Response -> Child ID Request: **652.883 ms**
- Child ID Request -> Response: **13.165 ms**
- Full Attach: **764.156 ms**
- pcap parent request: `01:23:30.317` (frame 333)
- pcap parent response: `01:23:30.415` (frame 334)
- pcap child id request: `01:23:31.068` (frame 342)
- pcap child id response: `01:23:31.081` (frame 344)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `46997e41a95017d0`
- parent rloc16: `n/a`
- child extaddr: `56b08e721f5fd932`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **460.623 ms**
- Response -> Child ID Request: **289.569 ms**
- Child ID Request -> Response: **14.45 ms**
- Full Attach: **764.642 ms**
- pcap parent request: `01:27:30.467` (frame 614)
- pcap parent response: `01:27:30.927` (frame 619)
- pcap child id request: `01:27:31.217` (frame 621)
- pcap child id response: `01:27:31.231` (frame 623)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-012752-run48.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `da3c14127ba26371`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `2f7071c89b0230d98eb36bdea1089514467b0ca5849d9a0bf1ff802e5253fa8b` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `aa735e96cad3a6d5`
- parent rloc16: `n/a`
- child extaddr: `da3c14127ba26371`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **92.664 ms**
- Response -> Child ID Request: **661.428 ms**
- Child ID Request -> Response: **14.605 ms**
- Full Attach: **768.697 ms**
- pcap parent request: `01:31:12.995` (frame 196)
- pcap parent response: `01:31:13.087` (frame 197)
- pcap child id request: `01:31:13.749` (frame 205)
- pcap child id response: `01:31:13.763` (frame 207)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `0a1ef109785f3aaa`
- parent rloc16: `n/a`
- child extaddr: `da3c14127ba26371`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **435.839 ms**
- Response -> Child ID Request: **318.952 ms**
- Child ID Request -> Response: **16.071 ms**
- Full Attach: **770.862 ms**
- pcap parent request: `01:35:12.987` (frame 556)
- pcap parent response: `01:35:13.423` (frame 561)
- pcap child id request: `01:35:13.742` (frame 563)
- pcap child id response: `01:35:13.758` (frame 565)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-013534-run49.log`

- manifest status: `completed`
- child extaddr: `92144fe1973f2858`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `2f7071c89b0230d98eb36bdea1089514467b0ca5849d9a0bf1ff802e5253fa8b` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `a67bbdbac14b4ae1`
- parent rloc16: `n/a`
- child extaddr: `92144fe1973f2858`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **478.307 ms**
- Response -> Child ID Request: **273.685 ms**
- Child ID Request -> Response: **12.778 ms**
- Full Attach: **764.77 ms**
- pcap parent request: `01:38:55.999` (frame 447)
- pcap parent response: `01:38:56.478` (frame 452)
- pcap child id request: `01:38:56.751` (frame 456)
- pcap child id response: `01:38:56.764` (frame 458)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `0ebda8ffc8f96621`
- parent rloc16: `n/a`
- child extaddr: `92144fe1973f2858`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **190.838 ms**
- Response -> Child ID Request: **560.405 ms**
- Child ID Request -> Response: **14.63 ms**
- Full Attach: **765.873 ms**
- pcap parent request: `01:42:56.602` (frame 730)
- pcap parent response: `01:42:56.792` (frame 731)
- pcap child id request: `01:42:57.353` (frame 737)
- pcap child id response: `01:42:57.367` (frame 739)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-014317-run50.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `ee09f68ab3ed49c4`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock_low_power/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `2f7071c89b0230d98eb36bdea1089514467b0ca5849d9a0bf1ff802e5253fa8b` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `4a20ff51afaa5d07`
- parent rloc16: `n/a`
- child extaddr: `ee09f68ab3ed49c4`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **129.226 ms**
- Response -> Child ID Request: **624.745 ms**
- Child ID Request -> Response: **14.673 ms**
- Full Attach: **768.644 ms**
- pcap parent request: `01:46:38.002` (frame 165)
- pcap parent response: `01:46:38.131` (frame 166)
- pcap child id request: `01:46:38.756` (frame 174)
- pcap child id response: `01:46:38.771` (frame 176)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `de6daadf609bd1e3`
- parent rloc16: `n/a`
- child extaddr: `ee09f68ab3ed49c4`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **319.339 ms**
- Response -> Child ID Request: **435.371 ms**
- Child ID Request -> Response: **12.869 ms**
- Full Attach: **767.579 ms**
- pcap parent request: `01:50:37.975` (frame 530)
- pcap parent response: `01:50:38.295` (frame 533)
- pcap child id request: `01:50:38.730` (frame 537)
- pcap child id response: `01:50:38.743` (frame 539)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**
