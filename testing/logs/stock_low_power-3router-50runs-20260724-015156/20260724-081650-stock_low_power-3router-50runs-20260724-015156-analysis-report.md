# Child Log Analysis

## stock_child

Files analyzed: **50**

- batch folders: `stock_low_power-3router-50runs-20260724-015156`

### PCAP-complete child attach summary

| Attach | Metric | M (SD), ms | n |
| --- | --- | ---: | ---: |
| 1 | Request -> Response | 162.56 (108.69) | 50 |
| 1 | Response -> Child ID Request | 589.07 (108.61) | 50 |
| 1 | Child ID Request -> Response | 13.80 (0.86) | 50 |
| 1 | Full Attach | 765.42 (1.46) | 50 |
| 2 | Request -> Response | 260.63 (145.46) | 50 |
| 2 | Response -> Child ID Request | 490.83 (145.34) | 50 |
| 2 | Child ID Request -> Response | 13.74 (0.96) | 50 |
| 2 | Full Attach | 765.20 (1.58) | 50 |

| Metric | M (SD) | n |
| --- | ---: | ---: |
| Failed TX Attempts per Log | 0.00 (0.00) | 50 |
| Log-only or Partial Sequences per Log | 0.00 (0.00) | 50 |

### `stock_child_20260724-015430-run01.log`

- manifest status: `completed`
- child extaddr: `da51cd30a0b74a54`

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
- parent extaddr: `2e27ae10dc5c32cb`
- parent rloc16: `n/a`
- child extaddr: `da51cd30a0b74a54`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **79.185 ms**
- Response -> Child ID Request: **672.829 ms**
- Child ID Request -> Response: **13.207 ms**
- Full Attach: **765.221 ms**
- pcap parent request: `01:57:46.369` (frame 86)
- pcap parent response: `01:57:46.448` (frame 87)
- pcap child id request: `01:57:47.121` (frame 93)
- pcap child id response: `01:57:47.134` (frame 95)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `8e559f88d8192fd5`
- parent rloc16: `n/a`
- child extaddr: `da51cd30a0b74a54`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **158.227 ms**
- Response -> Child ID Request: **592.789 ms**
- Child ID Request -> Response: **14.234 ms**
- Full Attach: **765.25 ms**
- pcap parent request: `02:01:46.799` (frame 304)
- pcap parent response: `02:01:46.957` (frame 305)
- pcap child id request: `02:01:47.550` (frame 309)
- pcap child id response: `02:01:47.564` (frame 311)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-020208-run02.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `5e90a54aadff070c`

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
- parent extaddr: `8226fe0091591625`
- parent rloc16: `n/a`
- child extaddr: `5e90a54aadff070c`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **438.678 ms**
- Response -> Child ID Request: **311.262 ms**
- Child ID Request -> Response: **12.981 ms**
- Full Attach: **762.921 ms**
- pcap parent request: `02:05:24.249` (frame 85)
- pcap parent response: `02:05:24.688` (frame 88)
- pcap child id request: `02:05:24.999` (frame 92)
- pcap child id response: `02:05:25.012` (frame 94)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `fa3437e22fa0fd23`
- parent rloc16: `n/a`
- child extaddr: `5e90a54aadff070c`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **73.705 ms**
- Response -> Child ID Request: **676.307 ms**
- Child ID Request -> Response: **13.115 ms**
- Full Attach: **763.127 ms**
- pcap parent request: `02:09:24.908` (frame 342)
- pcap parent response: `02:09:24.982` (frame 345)
- pcap child id request: `02:09:25.658` (frame 348)
- pcap child id response: `02:09:25.671` (frame 350)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-020946-run03.log`

- manifest status: `completed`
- child extaddr: `36572f7462b3f79c`

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
- parent extaddr: `c63ef76782d431d7`
- parent rloc16: `n/a`
- child extaddr: `36572f7462b3f79c`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **242.71 ms**
- Response -> Child ID Request: **507.059 ms**
- Child ID Request -> Response: **12.198 ms**
- Full Attach: **761.967 ms**
- pcap parent request: `02:13:01.928` (frame 87)
- pcap parent response: `02:13:02.171` (frame 88)
- pcap child id request: `02:13:02.678` (frame 95)
- pcap child id response: `02:13:02.690` (frame 97)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `3edb8403efd73dcd`
- parent rloc16: `n/a`
- child extaddr: `36572f7462b3f79c`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **414.225 ms**
- Response -> Child ID Request: **338.774 ms**
- Child ID Request -> Response: **14.239 ms**
- Full Attach: **767.238 ms**
- pcap parent request: `02:17:02.094` (frame 303)
- pcap parent response: `02:17:02.508` (frame 306)
- pcap child id request: `02:17:02.847` (frame 309)
- pcap child id response: `02:17:02.861` (frame 311)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-021724-run04.log`

- manifest status: `completed`
- child extaddr: `2e6ba8c4b2fc7fb1`

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
- parent extaddr: `beeb219fe0ca12ed`
- parent rloc16: `n/a`
- child extaddr: `2e6ba8c4b2fc7fb1`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **121.486 ms**
- Response -> Child ID Request: **630.344 ms**
- Child ID Request -> Response: **14.701 ms**
- Full Attach: **766.531 ms**
- pcap parent request: `02:20:39.486` (frame 91)
- pcap parent response: `02:20:39.608` (frame 92)
- pcap child id request: `02:20:40.238` (frame 98)
- pcap child id response: `02:20:40.253` (frame 100)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `26a80b35a4a02db1`
- parent rloc16: `n/a`
- child extaddr: `2e6ba8c4b2fc7fb1`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **225.054 ms**
- Response -> Child ID Request: **526.826 ms**
- Child ID Request -> Response: **13.208 ms**
- Full Attach: **765.088 ms**
- pcap parent request: `02:24:39.617` (frame 306)
- pcap parent response: `02:24:39.842` (frame 307)
- pcap child id request: `02:24:40.369` (frame 312)
- pcap child id response: `02:24:40.382` (frame 314)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-022501-run05.log`

- manifest status: `completed`
- child extaddr: `da8e1987cb7f2295`

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
- parent extaddr: `82f8a1c20e377563`
- parent rloc16: `n/a`
- child extaddr: `da8e1987cb7f2295`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **60.725 ms**
- Response -> Child ID Request: **691.348 ms**
- Child ID Request -> Response: **14.706 ms**
- Full Attach: **766.779 ms**
- pcap parent request: `02:28:17.456` (frame 88)
- pcap parent response: `02:28:17.517` (frame 89)
- pcap child id request: `02:28:18.209` (frame 96)
- pcap child id response: `02:28:18.223` (frame 98)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `660a8f6eb6ee0582`
- parent rloc16: `n/a`
- child extaddr: `da8e1987cb7f2295`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **437.408 ms**
- Response -> Child ID Request: **314.604 ms**
- Child ID Request -> Response: **14.411 ms**
- Full Attach: **766.423 ms**
- pcap parent request: `02:32:17.428` (frame 307)
- pcap parent response: `02:32:17.866` (frame 310)
- pcap child id request: `02:32:18.180` (frame 312)
- pcap child id response: `02:32:18.195` (frame 314)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-023239-run06.log`

- manifest status: `completed`
- child extaddr: `66f786c0f08fe26f`

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
- parent extaddr: `bea5c5513b94416c`
- parent rloc16: `n/a`
- child extaddr: `66f786c0f08fe26f`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **239.64 ms**
- Response -> Child ID Request: **512.355 ms**
- Child ID Request -> Response: **12.861 ms**
- Full Attach: **764.856 ms**
- pcap parent request: `02:35:55.360` (frame 83)
- pcap parent response: `02:35:55.600` (frame 84)
- pcap child id request: `02:35:56.112` (frame 90)
- pcap child id response: `02:35:56.125` (frame 92)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `a2a55a7eec9383d7`
- parent rloc16: `n/a`
- child extaddr: `66f786c0f08fe26f`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **251.543 ms**
- Response -> Child ID Request: **498.465 ms**
- Child ID Request -> Response: **14.573 ms**
- Full Attach: **764.581 ms**
- pcap parent request: `02:39:56.015` (frame 298)
- pcap parent response: `02:39:56.267` (frame 299)
- pcap child id request: `02:39:56.765` (frame 303)
- pcap child id response: `02:39:56.780` (frame 305)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-024017-run07.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `624d3ea830331d33`

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
- parent extaddr: `82cf4a6d70c9169b`
- parent rloc16: `n/a`
- child extaddr: `624d3ea830331d33`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **280.081 ms**
- Response -> Child ID Request: **470.913 ms**
- Child ID Request -> Response: **13.533 ms**
- Full Attach: **764.527 ms**
- pcap parent request: `02:43:32.758` (frame 94)
- pcap parent response: `02:43:33.039` (frame 95)
- pcap child id request: `02:43:33.509` (frame 101)
- pcap child id response: `02:43:33.523` (frame 103)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `3a44cd4539e54135`
- parent rloc16: `n/a`
- child extaddr: `624d3ea830331d33`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **36.656 ms**
- Response -> Child ID Request: **715.485 ms**
- Child ID Request -> Response: **12.765 ms**
- Full Attach: **764.906 ms**
- pcap parent request: `02:47:33.144` (frame 341)
- pcap parent response: `02:47:33.180` (frame 342)
- pcap child id request: `02:47:33.896` (frame 346)
- pcap child id response: `02:47:33.909` (frame 348)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-024754-run08.log`

- manifest status: `completed`
- child extaddr: `4699c8233bb2b33b`

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
- parent extaddr: `7a46f0112062ed41`
- parent rloc16: `n/a`
- child extaddr: `4699c8233bb2b33b`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **140.347 ms**
- Response -> Child ID Request: **610.656 ms**
- Child ID Request -> Response: **14.366 ms**
- Full Attach: **765.369 ms**
- pcap parent request: `02:51:10.891` (frame 91)
- pcap parent response: `02:51:11.031` (frame 94)
- pcap child id request: `02:51:11.642` (frame 98)
- pcap child id response: `02:51:11.656` (frame 100)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `9e736bd73659cdfd`
- parent rloc16: `n/a`
- child extaddr: `4699c8233bb2b33b`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **470.882 ms**
- Response -> Child ID Request: **281.107 ms**
- Child ID Request -> Response: **12.133 ms**
- Full Attach: **764.122 ms**
- pcap parent request: `02:55:11.187` (frame 308)
- pcap parent response: `02:55:11.658` (frame 311)
- pcap child id request: `02:55:11.939` (frame 313)
- pcap child id response: `02:55:11.951` (frame 315)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-025532-run09.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `663a75f7c59935df`

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
- parent extaddr: `225566627a93f4ae`
- parent rloc16: `n/a`
- child extaddr: `663a75f7c59935df`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **26.769 ms**
- Response -> Child ID Request: **724.214 ms**
- Child ID Request -> Response: **12.472 ms**
- Full Attach: **763.455 ms**
- pcap parent request: `02:58:48.547` (frame 95)
- pcap parent response: `02:58:48.574` (frame 96)
- pcap child id request: `02:58:49.298` (frame 102)
- pcap child id response: `02:58:49.310` (frame 104)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `66c3ab023d6b3d32`
- parent rloc16: `n/a`
- child extaddr: `663a75f7c59935df`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **54.333 ms**
- Response -> Child ID Request: **695.685 ms**
- Child ID Request -> Response: **13.708 ms**
- Full Attach: **763.726 ms**
- pcap parent request: `03:02:48.870` (frame 349)
- pcap parent response: `03:02:48.924` (frame 350)
- pcap child id request: `03:02:49.620` (frame 354)
- pcap child id response: `03:02:49.634` (frame 356)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-030310-run10.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `6a91394b145d9e94`

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
- parent extaddr: `fa347980a2628020`
- parent rloc16: `n/a`
- child extaddr: `6a91394b145d9e94`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **60.444 ms**
- Response -> Child ID Request: **689.568 ms**
- Child ID Request -> Response: **13.472 ms**
- Full Attach: **763.484 ms**
- pcap parent request: `03:06:26.282` (frame 82)
- pcap parent response: `03:06:26.343` (frame 83)
- pcap child id request: `03:06:27.032` (frame 89)
- pcap child id response: `03:06:27.046` (frame 91)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `9eb1ad619fdf2861`
- parent rloc16: `n/a`
- child extaddr: `6a91394b145d9e94`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **292.167 ms**
- Response -> Child ID Request: **458.023 ms**
- Child ID Request -> Response: **15.998 ms**
- Full Attach: **766.188 ms**
- pcap parent request: `03:10:26.830` (frame 339)
- pcap parent response: `03:10:27.123` (frame 341)
- pcap child id request: `03:10:27.581` (frame 345)
- pcap child id response: `03:10:27.597` (frame 347)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-031048-run11.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `b2e6607b5cd117d9`

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
- parent extaddr: `1a8ce9dd76ec2e51`
- parent rloc16: `n/a`
- child extaddr: `b2e6607b5cd117d9`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **11.963 ms**
- Response -> Child ID Request: **737.994 ms**
- Child ID Request -> Response: **14.045 ms**
- Full Attach: **764.002 ms**
- pcap parent request: `03:14:04.273` (frame 93)
- pcap parent response: `03:14:04.285` (frame 94)
- pcap child id request: `03:14:05.023` (frame 100)
- pcap child id response: `03:14:05.037` (frame 102)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `8e1b84601a02c5fc`
- parent rloc16: `n/a`
- child extaddr: `b2e6607b5cd117d9`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **427.486 ms**
- Response -> Child ID Request: **323.526 ms**
- Child ID Request -> Response: **14.821 ms**
- Full Attach: **765.833 ms**
- pcap parent request: `03:18:04.645` (frame 345)
- pcap parent response: `03:18:05.073` (frame 348)
- pcap child id request: `03:18:05.396` (frame 350)
- pcap child id response: `03:18:05.411` (frame 352)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-031826-run12.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `ce06e26e0c30f97c`

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
- parent extaddr: `f6b29253d9916f6e`
- parent rloc16: `n/a`
- child extaddr: `ce06e26e0c30f97c`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **57.692 ms**
- Response -> Child ID Request: **693.31 ms**
- Child ID Request -> Response: **13.744 ms**
- Full Attach: **764.746 ms**
- pcap parent request: `03:21:41.474` (frame 77)
- pcap parent response: `03:21:41.532` (frame 78)
- pcap child id request: `03:21:42.225` (frame 84)
- pcap child id response: `03:21:42.239` (frame 86)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `fe5029dd791cb61f`
- parent rloc16: `n/a`
- child extaddr: `ce06e26e0c30f97c`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **139.32 ms**
- Response -> Child ID Request: **612.684 ms**
- Child ID Request -> Response: **12.596 ms**
- Full Attach: **764.6 ms**
- pcap parent request: `03:25:41.784` (frame 324)
- pcap parent response: `03:25:41.923` (frame 325)
- pcap child id request: `03:25:42.536` (frame 330)
- pcap child id response: `03:25:42.548` (frame 332)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-032603-run13.log`

- manifest status: `completed`
- child extaddr: `a248a543b4b878ad`

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
- parent extaddr: `020e3ed46ab856ac`
- parent rloc16: `n/a`
- child extaddr: `a248a543b4b878ad`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **117.647 ms**
- Response -> Child ID Request: **633.347 ms**
- Child ID Request -> Response: **14.694 ms**
- Full Attach: **765.688 ms**
- pcap parent request: `03:29:19.424` (frame 90)
- pcap parent response: `03:29:19.542` (frame 91)
- pcap child id request: `03:29:20.175` (frame 97)
- pcap child id response: `03:29:20.190` (frame 99)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `aa2e61d53536a65a`
- parent rloc16: `n/a`
- child extaddr: `a248a543b4b878ad`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **248.179 ms**
- Response -> Child ID Request: **502.838 ms**
- Child ID Request -> Response: **12.384 ms**
- Full Attach: **763.401 ms**
- pcap parent request: `03:33:19.670` (frame 307)
- pcap parent response: `03:33:19.919` (frame 310)
- pcap child id request: `03:33:20.421` (frame 312)
- pcap child id response: `03:33:20.434` (frame 314)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-033341-run14.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `faf222b7db31534f`

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
- parent extaddr: `f214a4299a59d4d8`
- parent rloc16: `n/a`
- child extaddr: `faf222b7db31534f`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **318.038 ms**
- Response -> Child ID Request: **436.078 ms**
- Child ID Request -> Response: **12.143 ms**
- Full Attach: **766.259 ms**
- pcap parent request: `03:36:57.576` (frame 93)
- pcap parent response: `03:36:57.894` (frame 96)
- pcap child id request: `03:36:58.330` (frame 100)
- pcap child id response: `03:36:58.343` (frame 102)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `8e5f5cd4f5c65fc4`
- parent rloc16: `n/a`
- child extaddr: `faf222b7db31534f`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **323.854 ms**
- Response -> Child ID Request: **428.149 ms**
- Child ID Request -> Response: **14.875 ms**
- Full Attach: **766.878 ms**
- pcap parent request: `03:40:58.085` (frame 350)
- pcap parent response: `03:40:58.409` (frame 353)
- pcap child id request: `03:40:58.837` (frame 355)
- pcap child id response: `03:40:58.852` (frame 357)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-034119-run15.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `163e0806d6589248`

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
- parent extaddr: `fa5d90e0dd351ee7`
- parent rloc16: `n/a`
- child extaddr: `163e0806d6589248`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **312.65 ms**
- Response -> Child ID Request: **438.338 ms**
- Child ID Request -> Response: **14.699 ms**
- Full Attach: **765.687 ms**
- pcap parent request: `03:44:35.022` (frame 93)
- pcap parent response: `03:44:35.335` (frame 94)
- pcap child id request: `03:44:35.773` (frame 100)
- pcap child id response: `03:44:35.788` (frame 102)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `f6a0976a32383a2b`
- parent rloc16: `n/a`
- child extaddr: `163e0806d6589248`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **303.671 ms**
- Response -> Child ID Request: **447.34 ms**
- Child ID Request -> Response: **12.281 ms**
- Full Attach: **763.292 ms**
- pcap parent request: `03:48:35.279` (frame 347)
- pcap parent response: `03:48:35.583` (frame 350)
- pcap child id request: `03:48:36.030` (frame 352)
- pcap child id response: `03:48:36.042` (frame 354)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-034857-run16.log`

- manifest status: `completed`
- child extaddr: `0e45b571e97007b9`

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
- parent extaddr: `de40258268685fef`
- parent rloc16: `n/a`
- child extaddr: `0e45b571e97007b9`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **19.01 ms**
- Response -> Child ID Request: **732.994 ms**
- Child ID Request -> Response: **15.045 ms**
- Full Attach: **767.049 ms**
- pcap parent request: `03:52:12.534` (frame 91)
- pcap parent response: `03:52:12.553` (frame 92)
- pcap child id request: `03:52:13.286` (frame 98)
- pcap child id response: `03:52:13.301` (frame 100)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `bebdf39aa85fec6d`
- parent rloc16: `n/a`
- child extaddr: `0e45b571e97007b9`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **389.292 ms**
- Response -> Child ID Request: **364.499 ms**
- Child ID Request -> Response: **14.525 ms**
- Full Attach: **768.316 ms**
- pcap parent request: `03:56:12.621` (frame 307)
- pcap parent response: `03:56:13.010` (frame 310)
- pcap child id request: `03:56:13.374` (frame 312)
- pcap child id response: `03:56:13.389` (frame 314)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-035634-run17.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `6eec8f81ac5f0cc7`

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
- parent extaddr: `76b0ee0a39916dbf`
- parent rloc16: `n/a`
- child extaddr: `6eec8f81ac5f0cc7`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **176.638 ms**
- Response -> Child ID Request: **574.36 ms**
- Child ID Request -> Response: **12.908 ms**
- Full Attach: **763.906 ms**
- pcap parent request: `03:59:50.751` (frame 87)
- pcap parent response: `03:59:50.928` (frame 88)
- pcap child id request: `03:59:51.502` (frame 94)
- pcap child id response: `03:59:51.515` (frame 96)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `42eccd28df4350f2`
- parent rloc16: `n/a`
- child extaddr: `6eec8f81ac5f0cc7`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **407.559 ms**
- Response -> Child ID Request: **342.611 ms**
- Child ID Request -> Response: **14.4 ms**
- Full Attach: **764.57 ms**
- pcap parent request: `04:03:51.126` (frame 342)
- pcap parent response: `04:03:51.534` (frame 343)
- pcap child id request: `04:03:51.876` (frame 347)
- pcap child id response: `04:03:51.891` (frame 349)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-040412-run18.log`

- manifest status: `completed`
- child extaddr: `826dfb6f6f1ba7ac`

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
- parent extaddr: `c2a9181f4fdab4e1`
- parent rloc16: `n/a`
- child extaddr: `826dfb6f6f1ba7ac`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **46.44 ms**
- Response -> Child ID Request: **706.547 ms**
- Child ID Request -> Response: **14.497 ms**
- Full Attach: **767.484 ms**
- pcap parent request: `04:07:28.348` (frame 85)
- pcap parent response: `04:07:28.395` (frame 86)
- pcap child id request: `04:07:29.101` (frame 92)
- pcap child id response: `04:07:29.116` (frame 94)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `3aa8c9ec49cf1e3f`
- parent rloc16: `n/a`
- child extaddr: `826dfb6f6f1ba7ac`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **365.035 ms**
- Response -> Child ID Request: **386.966 ms**
- Child ID Request -> Response: **14.07 ms**
- Full Attach: **766.071 ms**
- pcap parent request: `04:11:28.784` (frame 303)
- pcap parent response: `04:11:29.149` (frame 306)
- pcap child id request: `04:11:29.536` (frame 308)
- pcap child id response: `04:11:29.550` (frame 310)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-041150-run19.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `a2fdbe24c30a859f`

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
- parent extaddr: `c2f5ccad43fb76ea`
- parent rloc16: `n/a`
- child extaddr: `a2fdbe24c30a859f`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **138.328 ms**
- Response -> Child ID Request: **611.631 ms**
- Child ID Request -> Response: **13.412 ms**
- Full Attach: **763.371 ms**
- pcap parent request: `04:15:06.050` (frame 85)
- pcap parent response: `04:15:06.189` (frame 88)
- pcap child id request: `04:15:06.800` (frame 92)
- pcap child id response: `04:15:06.814` (frame 94)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `dabf3a26f1a113ab`
- parent rloc16: `n/a`
- child extaddr: `a2fdbe24c30a859f`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **24.225 ms**
- Response -> Child ID Request: **727.775 ms**
- Child ID Request -> Response: **12.458 ms**
- Full Attach: **764.458 ms**
- pcap parent request: `04:19:06.499` (frame 343)
- pcap parent response: `04:19:06.523` (frame 344)
- pcap child id request: `04:19:07.251` (frame 348)
- pcap child id response: `04:19:07.264` (frame 350)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-041928-run20.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `8abef90d32260ce8`

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
- parent extaddr: `6aea6b023e8684fa`
- parent rloc16: `n/a`
- child extaddr: `8abef90d32260ce8`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **14.338 ms**
- Response -> Child ID Request: **736.668 ms**
- Child ID Request -> Response: **14.378 ms**
- Full Attach: **765.384 ms**
- pcap parent request: `04:22:43.873` (frame 86)
- pcap parent response: `04:22:43.887` (frame 87)
- pcap child id request: `04:22:44.624` (frame 93)
- pcap child id response: `04:22:44.638` (frame 95)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `babb0f24dcd3ff2f`
- parent rloc16: `n/a`
- child extaddr: `8abef90d32260ce8`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **21.918 ms**
- Response -> Child ID Request: **729.878 ms**
- Child ID Request -> Response: **13.161 ms**
- Full Attach: **764.957 ms**
- pcap parent request: `04:26:43.927` (frame 339)
- pcap parent response: `04:26:43.949` (frame 340)
- pcap child id request: `04:26:44.679` (frame 345)
- pcap child id response: `04:26:44.692` (frame 347)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-042705-run21.log`

- manifest status: `completed`
- child extaddr: `6a4ecaefb39a9dbf`

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
- parent extaddr: `82c7c1e17291b7fb`
- parent rloc16: `n/a`
- child extaddr: `6a4ecaefb39a9dbf`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **73.683 ms**
- Response -> Child ID Request: **677.058 ms**
- Child ID Request -> Response: **14.993 ms**
- Full Attach: **765.734 ms**
- pcap parent request: `04:30:21.082` (frame 92)
- pcap parent response: `04:30:21.156` (frame 93)
- pcap child id request: `04:30:21.833` (frame 99)
- pcap child id response: `04:30:21.848` (frame 101)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `02f0fd6218e4653c`
- parent rloc16: `n/a`
- child extaddr: `6a4ecaefb39a9dbf`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **128.232 ms**
- Response -> Child ID Request: **619.909 ms**
- Child ID Request -> Response: **13.135 ms**
- Full Attach: **761.276 ms**
- pcap parent request: `04:34:21.095` (frame 308)
- pcap parent response: `04:34:21.223` (frame 309)
- pcap child id request: `04:34:21.843` (frame 314)
- pcap child id response: `04:34:21.856` (frame 316)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-043443-run22.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `faeab9d870e145dd`

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
- parent extaddr: `6efd4665413f996d`
- parent rloc16: `n/a`
- child extaddr: `faeab9d870e145dd`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **289.202 ms**
- Response -> Child ID Request: **461.612 ms**
- Child ID Request -> Response: **15.401 ms**
- Full Attach: **766.215 ms**
- pcap parent request: `04:37:59.085` (frame 88)
- pcap parent response: `04:37:59.374` (frame 91)
- pcap child id request: `04:37:59.835` (frame 95)
- pcap child id response: `04:37:59.851` (frame 97)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `264f484130c1b0f8`
- parent rloc16: `n/a`
- child extaddr: `faeab9d870e145dd`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **374.316 ms**
- Response -> Child ID Request: **375.84 ms**
- Child ID Request -> Response: **14.199 ms**
- Full Attach: **764.355 ms**
- pcap parent request: `04:41:59.604` (frame 349)
- pcap parent response: `04:41:59.978` (frame 352)
- pcap child id request: `04:42:00.354` (frame 354)
- pcap child id response: `04:42:00.368` (frame 356)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-044221-run23.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `ba1650321bc5c636`

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
- parent extaddr: `0aca5922ca31b349`
- parent rloc16: `n/a`
- child extaddr: `ba1650321bc5c636`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **31.593 ms**
- Response -> Child ID Request: **718.248 ms**
- Child ID Request -> Response: **13.802 ms**
- Full Attach: **763.643 ms**
- pcap parent request: `04:45:37.244` (frame 96)
- pcap parent response: `04:45:37.275` (frame 97)
- pcap child id request: `04:45:37.994` (frame 103)
- pcap child id response: `04:45:38.007` (frame 105)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `ae5b47eef680e6b2`
- parent rloc16: `n/a`
- child extaddr: `ba1650321bc5c636`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **283.03 ms**
- Response -> Child ID Request: **467.975 ms**
- Child ID Request -> Response: **12.613 ms**
- Full Attach: **763.618 ms**
- pcap parent request: `04:49:37.838` (frame 350)
- pcap parent response: `04:49:38.121` (frame 353)
- pcap child id request: `04:49:38.589` (frame 355)
- pcap child id response: `04:49:38.601` (frame 357)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-044959-run24.log`

- manifest status: `completed`
- child extaddr: `86638599c1bc0a47`

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
- parent extaddr: `e2f4cb3841966e2a`
- parent rloc16: `n/a`
- child extaddr: `86638599c1bc0a47`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **201.464 ms**
- Response -> Child ID Request: **550.824 ms**
- Child ID Request -> Response: **14.204 ms**
- Full Attach: **766.492 ms**
- pcap parent request: `04:53:14.809` (frame 97)
- pcap parent response: `04:53:15.010` (frame 98)
- pcap child id request: `04:53:15.561` (frame 104)
- pcap child id response: `04:53:15.575` (frame 106)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `72be9c5e18ef19a8`
- parent rloc16: `n/a`
- child extaddr: `86638599c1bc0a47`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **451.931 ms**
- Response -> Child ID Request: **301.824 ms**
- Child ID Request -> Response: **14.495 ms**
- Full Attach: **768.25 ms**
- pcap parent request: `04:57:15.150` (frame 316)
- pcap parent response: `04:57:15.602` (frame 317)
- pcap child id request: `04:57:15.904` (frame 321)
- pcap child id response: `04:57:15.919` (frame 323)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-045736-run25.log`

- manifest status: `completed`
- child extaddr: `9655025e26eea717`

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
- parent extaddr: `0a91446438482d1b`
- parent rloc16: `n/a`
- child extaddr: `9655025e26eea717`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **247.121 ms**
- Response -> Child ID Request: **503.872 ms**
- Child ID Request -> Response: **14.206 ms**
- Full Attach: **765.199 ms**
- pcap parent request: `05:00:52.605` (frame 91)
- pcap parent response: `05:00:52.852` (frame 94)
- pcap child id request: `05:00:53.356` (frame 99)
- pcap child id response: `05:00:53.370` (frame 101)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `922baddaaab15829`
- parent rloc16: `n/a`
- child extaddr: `9655025e26eea717`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **425.544 ms**
- Response -> Child ID Request: **328.334 ms**
- Child ID Request -> Response: **12.923 ms**
- Full Attach: **766.801 ms**
- pcap parent request: `05:04:52.924` (frame 309)
- pcap parent response: `05:04:53.350` (frame 310)
- pcap child id request: `05:04:53.678` (frame 314)
- pcap child id response: `05:04:53.691` (frame 316)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-050514-run26.log`

- manifest status: `completed`
- child extaddr: `da8e67d41c3fd779`

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
- parent extaddr: `c6d615a528e0af19`
- parent rloc16: `n/a`
- child extaddr: `da8e67d41c3fd779`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **227.761 ms**
- Response -> Child ID Request: **526.38 ms**
- Child ID Request -> Response: **14.62 ms**
- Full Attach: **768.761 ms**
- pcap parent request: `05:08:30.512` (frame 93)
- pcap parent response: `05:08:30.740` (frame 96)
- pcap child id request: `05:08:31.266` (frame 100)
- pcap child id response: `05:08:31.281` (frame 102)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `3295c7fc152703e0`
- parent rloc16: `n/a`
- child extaddr: `da8e67d41c3fd779`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **308.926 ms**
- Response -> Child ID Request: **441.245 ms**
- Child ID Request -> Response: **14.8 ms**
- Full Attach: **764.971 ms**
- pcap parent request: `05:12:30.677` (frame 312)
- pcap parent response: `05:12:30.986` (frame 313)
- pcap child id request: `05:12:31.427` (frame 317)
- pcap child id response: `05:12:31.442` (frame 319)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-051252-run27.log`

- manifest status: `completed`
- child extaddr: `6a775d9396fb0608`

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
- parent extaddr: `069e786fbf841b2d`
- parent rloc16: `n/a`
- child extaddr: `6a775d9396fb0608`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **145.91 ms**
- Response -> Child ID Request: **606.067 ms**
- Child ID Request -> Response: **13.971 ms**
- Full Attach: **765.948 ms**
- pcap parent request: `05:16:08.459` (frame 86)
- pcap parent response: `05:16:08.604` (frame 87)
- pcap child id request: `05:16:09.211` (frame 93)
- pcap child id response: `05:16:09.225` (frame 95)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `aab397db6424a4de`
- parent rloc16: `n/a`
- child extaddr: `6a775d9396fb0608`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **308.116 ms**
- Response -> Child ID Request: **442.885 ms**
- Child ID Request -> Response: **14.161 ms**
- Full Attach: **765.162 ms**
- pcap parent request: `05:20:08.744` (frame 301)
- pcap parent response: `05:20:09.052` (frame 305)
- pcap child id request: `05:20:09.495` (frame 307)
- pcap child id response: `05:20:09.509` (frame 309)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-052030-run28.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `6671d0d6e45eb0f3`

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
- parent extaddr: `c612fa2dc50a7ab6`
- parent rloc16: `n/a`
- child extaddr: `6671d0d6e45eb0f3`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **137.62 ms**
- Response -> Child ID Request: **615.388 ms**
- Child ID Request -> Response: **14.642 ms**
- Full Attach: **767.65 ms**
- pcap parent request: `05:23:45.965` (frame 80)
- pcap parent response: `05:23:46.102` (frame 81)
- pcap child id request: `05:23:46.718` (frame 87)
- pcap child id response: `05:23:46.732` (frame 89)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `f24075d34d73782c`
- parent rloc16: `n/a`
- child extaddr: `6671d0d6e45eb0f3`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **216.006 ms**
- Response -> Child ID Request: **533.173 ms**
- Child ID Request -> Response: **14.872 ms**
- Full Attach: **764.051 ms**
- pcap parent request: `05:27:46.272` (frame 333)
- pcap parent response: `05:27:46.489` (frame 334)
- pcap child id request: `05:27:47.022` (frame 338)
- pcap child id response: `05:27:47.037` (frame 340)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-052807-run29.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `c62416027be4f31f`

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
- parent extaddr: `c6ab1b50eced5f6e`
- parent rloc16: `n/a`
- child extaddr: `c62416027be4f31f`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **355.584 ms**
- Response -> Child ID Request: **396.413 ms**
- Child ID Request -> Response: **13.627 ms**
- Full Attach: **765.624 ms**
- pcap parent request: `05:31:23.314` (frame 91)
- pcap parent response: `05:31:23.670` (frame 92)
- pcap child id request: `05:31:24.066` (frame 98)
- pcap child id response: `05:31:24.080` (frame 100)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `8ad060c79fae14ce`
- parent rloc16: `n/a`
- child extaddr: `c62416027be4f31f`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **22.352 ms**
- Response -> Child ID Request: **729.642 ms**
- Child ID Request -> Response: **14.409 ms**
- Full Attach: **766.403 ms**
- pcap parent request: `05:35:23.458` (frame 347)
- pcap parent response: `05:35:23.480` (frame 348)
- pcap child id request: `05:35:24.210` (frame 352)
- pcap child id response: `05:35:24.225` (frame 354)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-053545-run30.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `1a6c666e6332dd60`

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
- parent extaddr: `6e8cdd0366af5f69`
- parent rloc16: `n/a`
- child extaddr: `1a6c666e6332dd60`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **59.033 ms**
- Response -> Child ID Request: **694.118 ms**
- Child ID Request -> Response: **12.928 ms**
- Full Attach: **766.079 ms**
- pcap parent request: `05:39:01.279` (frame 89)
- pcap parent response: `05:39:01.338` (frame 92)
- pcap child id request: `05:39:02.032` (frame 96)
- pcap child id response: `05:39:02.045` (frame 98)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `3255a27062d78d2d`
- parent rloc16: `n/a`
- child extaddr: `1a6c666e6332dd60`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **152.501 ms**
- Response -> Child ID Request: **600.207 ms**
- Child ID Request -> Response: **13.081 ms**
- Full Attach: **765.789 ms**
- pcap parent request: `05:43:01.865` (frame 345)
- pcap parent response: `05:43:02.018` (frame 348)
- pcap child id request: `05:43:02.618` (frame 350)
- pcap child id response: `05:43:02.631` (frame 352)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-054323-run31.log`

- manifest status: `completed`
- child extaddr: `2abd9caf7b0093d1`

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
- parent extaddr: `f6bd7880bd374d38`
- parent rloc16: `n/a`
- child extaddr: `2abd9caf7b0093d1`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **30.72 ms**
- Response -> Child ID Request: **720.285 ms**
- Child ID Request -> Response: **14.755 ms**
- Full Attach: **765.76 ms**
- pcap parent request: `05:46:38.605` (frame 88)
- pcap parent response: `05:46:38.636` (frame 89)
- pcap child id request: `05:46:39.356` (frame 95)
- pcap child id response: `05:46:39.371` (frame 97)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `02ae419abde04b8b`
- parent rloc16: `n/a`
- child extaddr: `2abd9caf7b0093d1`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **249.942 ms**
- Response -> Child ID Request: **502.771 ms**
- Child ID Request -> Response: **12.438 ms**
- Full Attach: **765.151 ms**
- pcap parent request: `05:50:38.764` (frame 307)
- pcap parent response: `05:50:39.014` (frame 310)
- pcap child id request: `05:50:39.516` (frame 312)
- pcap child id response: `05:50:39.529` (frame 314)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-055101-run32.log`

- manifest status: `completed`
- child extaddr: `4685747b3493ca8b`

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
- parent extaddr: `a2832fe124faf9de`
- parent rloc16: `n/a`
- child extaddr: `4685747b3493ca8b`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **133.686 ms**
- Response -> Child ID Request: **619.396 ms**
- Child ID Request -> Response: **14.654 ms**
- Full Attach: **767.736 ms**
- pcap parent request: `05:54:16.567` (frame 90)
- pcap parent response: `05:54:16.701` (frame 91)
- pcap child id request: `05:54:17.321` (frame 97)
- pcap child id response: `05:54:17.335` (frame 99)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `ee98764542b7c6cc`
- parent rloc16: `n/a`
- child extaddr: `4685747b3493ca8b`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **41.688 ms**
- Response -> Child ID Request: **711.053 ms**
- Child ID Request -> Response: **13.004 ms**
- Full Attach: **765.745 ms**
- pcap parent request: `05:58:17.087` (frame 307)
- pcap parent response: `05:58:17.128` (frame 308)
- pcap child id request: `05:58:17.840` (frame 312)
- pcap child id response: `05:58:17.853` (frame 314)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-055838-run33.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `0eb9852fd29b8b69`

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
- parent extaddr: `daea2f60f2d186e3`
- parent rloc16: `n/a`
- child extaddr: `0eb9852fd29b8b69`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **86.551 ms**
- Response -> Child ID Request: **665.601 ms**
- Child ID Request -> Response: **14.437 ms**
- Full Attach: **766.589 ms**
- pcap parent request: `06:01:54.460` (frame 89)
- pcap parent response: `06:01:54.546` (frame 92)
- pcap child id request: `06:01:55.212` (frame 96)
- pcap child id response: `06:01:55.226` (frame 98)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `02657453a42710b0`
- parent rloc16: `n/a`
- child extaddr: `0eb9852fd29b8b69`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **106.193 ms**
- Response -> Child ID Request: **647.6 ms**
- Child ID Request -> Response: **14.438 ms**
- Full Attach: **768.231 ms**
- pcap parent request: `06:05:54.457` (frame 340)
- pcap parent response: `06:05:54.563` (frame 341)
- pcap child id request: `06:05:55.211` (frame 345)
- pcap child id response: `06:05:55.225` (frame 347)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-060616-run34.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `22768edc5177512c`

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
- parent extaddr: `4e5d16d931c48bb7`
- parent rloc16: `n/a`
- child extaddr: `22768edc5177512c`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **228.403 ms**
- Response -> Child ID Request: **522.748 ms**
- Child ID Request -> Response: **14.283 ms**
- Full Attach: **765.434 ms**
- pcap parent request: `06:09:32.277` (frame 94)
- pcap parent response: `06:09:32.505` (frame 97)
- pcap child id request: `06:09:33.028` (frame 101)
- pcap child id response: `06:09:33.042` (frame 103)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `6e4c30388b5cdc21`
- parent rloc16: `n/a`
- child extaddr: `22768edc5177512c`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **400.62 ms**
- Response -> Child ID Request: **351.379 ms**
- Child ID Request -> Response: **12.865 ms**
- Full Attach: **764.864 ms**
- pcap parent request: `06:13:32.437` (frame 350)
- pcap parent response: `06:13:32.837` (frame 354)
- pcap child id request: `06:13:33.189` (frame 356)
- pcap child id response: `06:13:33.202` (frame 358)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-061354-run35.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `2ad25d3124df2f14`

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
- parent extaddr: `8e17c8c05d89c512`
- parent rloc16: `n/a`
- child extaddr: `2ad25d3124df2f14`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **181.28 ms**
- Response -> Child ID Request: **570.161 ms**
- Child ID Request -> Response: **13.07 ms**
- Full Attach: **764.511 ms**
- pcap parent request: `06:17:10.121` (frame 87)
- pcap parent response: `06:17:10.302` (frame 90)
- pcap child id request: `06:17:10.872` (frame 94)
- pcap child id response: `06:17:10.886` (frame 96)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `4e152a62046ab6ed`
- parent rloc16: `n/a`
- child extaddr: `2ad25d3124df2f14`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **298.787 ms**
- Response -> Child ID Request: **449.417 ms**
- Child ID Request -> Response: **13.606 ms**
- Full Attach: **761.81 ms**
- pcap parent request: `06:21:10.696` (frame 342)
- pcap parent response: `06:21:10.995` (frame 345)
- pcap child id request: `06:21:11.445` (frame 347)
- pcap child id response: `06:21:11.458` (frame 349)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-062132-run36.log`

- manifest status: `completed`
- child extaddr: `9e7e2387081c73a6`

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
- parent extaddr: `ea9757bc15fad61d`
- parent rloc16: `n/a`
- child extaddr: `9e7e2387081c73a6`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **335.512 ms**
- Response -> Child ID Request: **417.466 ms**
- Child ID Request -> Response: **13.168 ms**
- Full Attach: **766.146 ms**
- pcap parent request: `06:24:47.571` (frame 91)
- pcap parent response: `06:24:47.907` (frame 94)
- pcap child id request: `06:24:48.324` (frame 98)
- pcap child id response: `06:24:48.337` (frame 100)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `de5da63085ddeb16`
- parent rloc16: `n/a`
- child extaddr: `9e7e2387081c73a6`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **101.657 ms**
- Response -> Child ID Request: **649.357 ms**
- Child ID Request -> Response: **12.894 ms**
- Full Attach: **763.908 ms**
- pcap parent request: `06:28:47.593` (frame 308)
- pcap parent response: `06:28:47.695` (frame 309)
- pcap child id request: `06:28:48.344` (frame 313)
- pcap child id response: `06:28:48.357` (frame 315)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-062909-run37.log`

- manifest status: `completed`
- child extaddr: `8a0d7efbc11cf890`

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
- parent extaddr: `c2e423030539c04f`
- parent rloc16: `n/a`
- child extaddr: `8a0d7efbc11cf890`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **30.336 ms**
- Response -> Child ID Request: **722.643 ms**
- Child ID Request -> Response: **13.717 ms**
- Full Attach: **766.696 ms**
- pcap parent request: `06:32:25.464` (frame 89)
- pcap parent response: `06:32:25.494` (frame 90)
- pcap child id request: `06:32:26.217` (frame 96)
- pcap child id response: `06:32:26.230` (frame 98)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `3effebbd19f492d8`
- parent rloc16: `n/a`
- child extaddr: `8a0d7efbc11cf890`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **227.835 ms**
- Response -> Child ID Request: **524.182 ms**
- Child ID Request -> Response: **12.409 ms**
- Full Attach: **764.426 ms**
- pcap parent request: `06:36:25.642` (frame 306)
- pcap parent response: `06:36:25.870` (frame 307)
- pcap child id request: `06:36:26.394` (frame 311)
- pcap child id response: `06:36:26.406` (frame 313)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-063647-run38.log`

- manifest status: `completed`
- child extaddr: `1e40c4dde87ce77e`

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
- parent extaddr: `32f68bde4bd5f82b`
- parent rloc16: `n/a`
- child extaddr: `1e40c4dde87ce77e`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **187.388 ms**
- Response -> Child ID Request: **565.706 ms**
- Child ID Request -> Response: **12.562 ms**
- Full Attach: **765.656 ms**
- pcap parent request: `06:40:03.939` (frame 84)
- pcap parent response: `06:40:04.127` (frame 87)
- pcap child id request: `06:40:04.692` (frame 91)
- pcap child id response: `06:40:04.705` (frame 93)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `625df1b79dae38c1`
- parent rloc16: `n/a`
- child extaddr: `1e40c4dde87ce77e`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **364.014 ms**
- Response -> Child ID Request: **386.175 ms**
- Child ID Request -> Response: **14.825 ms**
- Full Attach: **765.014 ms**
- pcap parent request: `06:44:03.941` (frame 300)
- pcap parent response: `06:44:04.305` (frame 303)
- pcap child id request: `06:44:04.692` (frame 305)
- pcap child id response: `06:44:04.706` (frame 307)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-064425-run39.log`

- manifest status: `completed`
- child extaddr: `0e3af1dfa655ec1f`

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
- parent extaddr: `3ee4e3e8736ec57c`
- parent rloc16: `n/a`
- child extaddr: `0e3af1dfa655ec1f`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **134.911 ms**
- Response -> Child ID Request: **615.966 ms**
- Child ID Request -> Response: **13.288 ms**
- Full Attach: **764.165 ms**
- pcap parent request: `06:47:40.944` (frame 93)
- pcap parent response: `06:47:41.078` (frame 96)
- pcap child id request: `06:47:41.694` (frame 100)
- pcap child id response: `06:47:41.708` (frame 102)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `5e808477373fd522`
- parent rloc16: `n/a`
- child extaddr: `0e3af1dfa655ec1f`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **15.359 ms**
- Response -> Child ID Request: **735.718 ms**
- Child ID Request -> Response: **12.556 ms**
- Full Attach: **763.633 ms**
- pcap parent request: `06:51:41.496` (frame 311)
- pcap parent response: `06:51:41.511` (frame 312)
- pcap child id request: `06:51:42.247` (frame 316)
- pcap child id response: `06:51:42.259` (frame 318)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-065203-run40.log`

- manifest status: `completed`
- child extaddr: `8a602c8d4c26647f`

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
- parent extaddr: `a2b82e6fa48fd73b`
- parent rloc16: `n/a`
- child extaddr: `8a602c8d4c26647f`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **243.281 ms**
- Response -> Child ID Request: **507.732 ms**
- Child ID Request -> Response: **14.617 ms**
- Full Attach: **765.63 ms**
- pcap parent request: `06:55:19.548` (frame 91)
- pcap parent response: `06:55:19.791` (frame 94)
- pcap child id request: `06:55:20.299` (frame 98)
- pcap child id response: `06:55:20.313` (frame 100)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `563b4f41608389c7`
- parent rloc16: `n/a`
- child extaddr: `8a602c8d4c26647f`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **362.185 ms**
- Response -> Child ID Request: **392.57 ms**
- Child ID Request -> Response: **14.458 ms**
- Full Attach: **769.213 ms**
- pcap parent request: `06:59:19.669` (frame 307)
- pcap parent response: `06:59:20.031` (frame 310)
- pcap child id request: `06:59:20.424` (frame 312)
- pcap child id response: `06:59:20.438` (frame 314)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-065941-run41.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `96a7f112c52cb0c8`

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
- parent extaddr: `cacdd096c6434199`
- parent rloc16: `n/a`
- child extaddr: `96a7f112c52cb0c8`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **127.137 ms**
- Response -> Child ID Request: **626.98 ms**
- Child ID Request -> Response: **12.275 ms**
- Full Attach: **766.392 ms**
- pcap parent request: `07:02:57.004` (frame 86)
- pcap parent response: `07:02:57.131` (frame 87)
- pcap child id request: `07:02:57.758` (frame 93)
- pcap child id response: `07:02:57.770` (frame 95)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `ee3a6860610b524d`
- parent rloc16: `n/a`
- child extaddr: `96a7f112c52cb0c8`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **374.519 ms**
- Response -> Child ID Request: **375.662 ms**
- Child ID Request -> Response: **14.359 ms**
- Full Attach: **764.54 ms**
- pcap parent request: `07:06:57.599` (frame 344)
- pcap parent response: `07:06:57.974` (frame 345)
- pcap child id request: `07:06:58.349` (frame 349)
- pcap child id response: `07:06:58.364` (frame 351)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-070718-run42.log`

- manifest status: `completed`
- child extaddr: `e6a76099a5b54b9d`

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
- parent extaddr: `1ebb7925e2189f70`
- parent rloc16: `n/a`
- child extaddr: `e6a76099a5b54b9d`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **35.445 ms**
- Response -> Child ID Request: **714.3 ms**
- Child ID Request -> Response: **12.949 ms**
- Full Attach: **762.694 ms**
- pcap parent request: `07:10:34.979` (frame 83)
- pcap parent response: `07:10:35.015` (frame 84)
- pcap child id request: `07:10:35.729` (frame 90)
- pcap child id response: `07:10:35.742` (frame 92)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `eac78534718e8fcf`
- parent rloc16: `n/a`
- child extaddr: `e6a76099a5b54b9d`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **167.454 ms**
- Response -> Child ID Request: **583.539 ms**
- Child ID Request -> Response: **14.495 ms**
- Full Attach: **765.488 ms**
- pcap parent request: `07:14:35.433` (frame 302)
- pcap parent response: `07:14:35.601` (frame 303)
- pcap child id request: `07:14:36.184` (frame 307)
- pcap child id response: `07:14:36.199` (frame 309)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-071456-run43.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `0ab3a13976e6d1fa`

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
- parent extaddr: `12e4be32c14cbfc7`
- parent rloc16: `n/a`
- child extaddr: `0ab3a13976e6d1fa`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **97.63 ms**
- Response -> Child ID Request: **652.354 ms**
- Child ID Request -> Response: **13.693 ms**
- Full Attach: **763.677 ms**
- pcap parent request: `07:18:12.523` (frame 85)
- pcap parent response: `07:18:12.621` (frame 86)
- pcap child id request: `07:18:13.273` (frame 92)
- pcap child id response: `07:18:13.287` (frame 94)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `525ddbf1bbfb8d5a`
- parent rloc16: `n/a`
- child extaddr: `0ab3a13976e6d1fa`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **108.535 ms**
- Response -> Child ID Request: **642.736 ms**
- Child ID Request -> Response: **13.303 ms**
- Full Attach: **764.574 ms**
- pcap parent request: `07:22:12.732` (frame 336)
- pcap parent response: `07:22:12.841` (frame 337)
- pcap child id request: `07:22:13.484` (frame 341)
- pcap child id response: `07:22:13.497` (frame 343)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-072234-run44.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `429c97acbd09af3d`

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
- parent extaddr: `1aa6d27d4fbd67f7`
- parent rloc16: `n/a`
- child extaddr: `429c97acbd09af3d`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **93.978 ms**
- Response -> Child ID Request: **658.006 ms**
- Child ID Request -> Response: **15.049 ms**
- Full Attach: **767.033 ms**
- pcap parent request: `07:25:50.099` (frame 89)
- pcap parent response: `07:25:50.193` (frame 93)
- pcap child id request: `07:25:50.851` (frame 97)
- pcap child id response: `07:25:50.866` (frame 99)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `f69b98ebcb5c28d8`
- parent rloc16: `n/a`
- child extaddr: `429c97acbd09af3d`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **137.963 ms**
- Response -> Child ID Request: **614.015 ms**
- Child ID Request -> Response: **13.345 ms**
- Full Attach: **765.323 ms**
- pcap parent request: `07:29:50.616` (frame 343)
- pcap parent response: `07:29:50.754` (frame 346)
- pcap child id request: `07:29:51.368` (frame 348)
- pcap child id response: `07:29:51.381` (frame 350)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-073012-run45.log`

- manifest status: `completed`
- child extaddr: `6a5442589c03968b`

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
- parent extaddr: `d6c477cf945b93ac`
- parent rloc16: `n/a`
- child extaddr: `6a5442589c03968b`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **130.464 ms**
- Response -> Child ID Request: **622.517 ms**
- Child ID Request -> Response: **13.066 ms**
- Full Attach: **766.047 ms**
- pcap parent request: `07:33:27.732` (frame 94)
- pcap parent response: `07:33:27.862` (frame 95)
- pcap child id request: `07:33:28.485` (frame 101)
- pcap child id response: `07:33:28.498` (frame 103)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `f67e454e37fcbd75`
- parent rloc16: `n/a`
- child extaddr: `6a5442589c03968b`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **353.373 ms**
- Response -> Child ID Request: **398.648 ms**
- Child ID Request -> Response: **14.37 ms**
- Full Attach: **766.391 ms**
- pcap parent request: `07:37:28.233` (frame 313)
- pcap parent response: `07:37:28.586` (frame 316)
- pcap child id request: `07:37:28.985` (frame 318)
- pcap child id response: `07:37:28.999` (frame 320)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-073750-run46.log`

- manifest status: `completed`
- child extaddr: `d62bf7a0d287f37a`

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
- parent extaddr: `6ede02eef6530ca6`
- parent rloc16: `n/a`
- child extaddr: `d62bf7a0d287f37a`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **216.371 ms**
- Response -> Child ID Request: **536.766 ms**
- Child ID Request -> Response: **14.277 ms**
- Full Attach: **767.414 ms**
- pcap parent request: `07:41:05.601` (frame 93)
- pcap parent response: `07:41:05.817` (frame 94)
- pcap child id request: `07:41:06.354` (frame 100)
- pcap child id response: `07:41:06.368` (frame 102)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `9afe46e5736d1efb`
- parent rloc16: `n/a`
- child extaddr: `d62bf7a0d287f37a`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **489.065 ms**
- Response -> Child ID Request: **261.945 ms**
- Child ID Request -> Response: **13.08 ms**
- Full Attach: **764.09 ms**
- pcap parent request: `07:45:06.115` (frame 311)
- pcap parent response: `07:45:06.604` (frame 314)
- pcap child id request: `07:45:06.866` (frame 316)
- pcap child id response: `07:45:06.879` (frame 318)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-074527-run47.log`

- manifest status: `completed`
- child extaddr: `0e0eefa4fd6abc73`

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
- parent extaddr: `5a24c29dd2777216`
- parent rloc16: `n/a`
- child extaddr: `0e0eefa4fd6abc73`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **257.247 ms**
- Response -> Child ID Request: **495.755 ms**
- Child ID Request -> Response: **13.269 ms**
- Full Attach: **766.271 ms**
- pcap parent request: `07:48:43.849` (frame 85)
- pcap parent response: `07:48:44.106` (frame 88)
- pcap child id request: `07:48:44.602` (frame 92)
- pcap child id response: `07:48:44.615` (frame 94)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `2291f0d168431733`
- parent rloc16: `n/a`
- child extaddr: `0e0eefa4fd6abc73`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **431.204 ms**
- Response -> Child ID Request: **319.933 ms**
- Child ID Request -> Response: **13.097 ms**
- Full Attach: **764.234 ms**
- pcap parent request: `07:52:44.343` (frame 301)
- pcap parent response: `07:52:44.774` (frame 304)
- pcap child id request: `07:52:45.094` (frame 306)
- pcap child id response: `07:52:45.107` (frame 308)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-075305-run48.log`

- manifest status: `completed`
- child extaddr: `d2a1ddd37c49b699`

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
- parent extaddr: `42f48fc533c78d85`
- parent rloc16: `n/a`
- child extaddr: `d2a1ddd37c49b699`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **247.378 ms**
- Response -> Child ID Request: **503.662 ms**
- Child ID Request -> Response: **14.361 ms**
- Full Attach: **765.401 ms**
- pcap parent request: `07:56:21.294` (frame 91)
- pcap parent response: `07:56:21.541` (frame 92)
- pcap child id request: `07:56:22.045` (frame 98)
- pcap child id response: `07:56:22.059` (frame 100)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `9e29db91207da8b4`
- parent rloc16: `n/a`
- child extaddr: `d2a1ddd37c49b699`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **452.747 ms**
- Response -> Child ID Request: **298.376 ms**
- Child ID Request -> Response: **15.641 ms**
- Full Attach: **766.764 ms**
- pcap parent request: `08:00:21.264` (frame 309)
- pcap parent response: `08:00:21.717` (frame 312)
- pcap child id request: `08:00:22.015` (frame 314)
- pcap child id response: `08:00:22.031` (frame 316)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-080043-run49.log`

- manifest status: `completed`
- child extaddr: `c6be5c63c99ec4e5`

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
- parent extaddr: `8e5f42504be1f9cc`
- parent rloc16: `n/a`
- child extaddr: `c6be5c63c99ec4e5`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **328.543 ms**
- Response -> Child ID Request: **422.457 ms**
- Child ID Request -> Response: **12.75 ms**
- Full Attach: **763.75 ms**
- pcap parent request: `08:03:59.174` (frame 82)
- pcap parent response: `08:03:59.503` (frame 85)
- pcap child id request: `08:03:59.925` (frame 89)
- pcap child id response: `08:03:59.938` (frame 91)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `cea6f07695fc7d6f`
- parent rloc16: `n/a`
- child extaddr: `c6be5c63c99ec4e5`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **192.772 ms**
- Response -> Child ID Request: **559.226 ms**
- Child ID Request -> Response: **14.803 ms**
- Full Attach: **766.801 ms**
- pcap parent request: `08:07:59.227` (frame 300)
- pcap parent response: `08:07:59.420` (frame 301)
- pcap child id request: `08:07:59.979` (frame 305)
- pcap child id response: `08:07:59.994` (frame 307)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-080821-run50.log`

- manifest status: `completed`
- child extaddr: `4a361ba6b8597471`

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
- parent extaddr: `d2e2b4eb10b7c4aa`
- parent rloc16: `n/a`
- child extaddr: `4a361ba6b8597471`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **329.845 ms**
- Response -> Child ID Request: **421.147 ms**
- Child ID Request -> Response: **13.093 ms**
- Full Attach: **764.085 ms**
- pcap parent request: `08:11:36.510` (frame 84)
- pcap parent response: `08:11:36.840` (frame 85)
- pcap child id request: `08:11:37.261` (frame 91)
- pcap child id response: `08:11:37.274` (frame 93)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `7e0e2d62307b630f`
- parent rloc16: `n/a`
- child extaddr: `4a361ba6b8597471`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **419.71 ms**
- Response -> Child ID Request: **332.064 ms**
- Child ID Request -> Response: **14.303 ms**
- Full Attach: **766.077 ms**
- pcap parent request: `08:15:36.684` (frame 300)
- pcap parent response: `08:15:37.104` (frame 303)
- pcap child id request: `08:15:37.436` (frame 305)
- pcap child id response: `08:15:37.450` (frame 307)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**
