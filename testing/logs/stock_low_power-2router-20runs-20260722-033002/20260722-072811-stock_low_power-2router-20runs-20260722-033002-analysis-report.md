# Child Log Analysis

## stock_child

Files analyzed: **20**

- batch folders: `stock_low_power-2router-20runs-20260722-033002`

### PCAP-complete child attach summary

| Attach | Metric | M (SD), ms | n |
| --- | --- | ---: | ---: |
| 1 | Request -> Response | 125.76 (109.98) | 20 |
| 1 | Response -> Child ID Request | 625.21 (109.88) | 20 |
| 1 | Child ID Request -> Response | 13.88 (0.73) | 20 |
| 1 | Full Attach | 764.84 (1.58) | 20 |
| 2 | Request -> Response | 254.96 (136.17) | 20 |
| 2 | Response -> Child ID Request | 496.60 (136.29) | 20 |
| 2 | Child ID Request -> Response | 13.34 (0.88) | 20 |
| 2 | Full Attach | 764.90 (1.61) | 20 |

| Metric | M (SD) | n |
| --- | ---: | ---: |
| Failed TX Attempts per Log | 0.00 (0.00) | 20 |
| Log-only or Partial Sequences per Log | 0.00 (0.00) | 20 |

### `stock_child_20260722-033158-run01.log`

- manifest status: `completed`
- child extaddr: `6a9e4b0290e8a756`

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
- parent extaddr: `8ae662780cde590b`
- parent rloc16: `n/a`
- child extaddr: `6a9e4b0290e8a756`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **122.703 ms**
- Response -> Child ID Request: **627.347 ms**
- Child ID Request -> Response: **12.883 ms**
- Full Attach: **762.933 ms**
- pcap parent request: `03:37:39.626` (frame 80)
- pcap parent response: `03:37:39.748` (frame 82)
- pcap child id request: `03:37:40.376` (frame 86)
- pcap child id response: `03:37:40.389` (frame 88)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `e2c3a17dd26b309b`
- parent rloc16: `n/a`
- child extaddr: `6a9e4b0290e8a756`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **106.892 ms**
- Response -> Child ID Request: **646.112 ms**
- Child ID Request -> Response: **12.934 ms**
- Full Attach: **765.938 ms**
- pcap parent request: `03:41:40.248` (frame 227)
- pcap parent response: `03:41:40.355` (frame 228)
- pcap child id request: `03:41:41.001` (frame 230)
- pcap child id response: `03:41:41.014` (frame 232)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260722-034346-run02.log`

- manifest status: `completed`
- child extaddr: `4e9339bc09ed67ef`

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
- parent extaddr: `961482367165a781`
- parent rloc16: `n/a`
- child extaddr: `4e9339bc09ed67ef`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **80.108 ms**
- Response -> Child ID Request: **669.888 ms**
- Child ID Request -> Response: **14.486 ms**
- Full Attach: **764.482 ms**
- pcap parent request: `03:49:27.517` (frame 81)
- pcap parent response: `03:49:27.597` (frame 82)
- pcap child id request: `03:49:28.267` (frame 86)
- pcap child id response: `03:49:28.281` (frame 88)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `2233c0b6aa846581`
- parent rloc16: `n/a`
- child extaddr: `4e9339bc09ed67ef`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **255.34 ms**
- Response -> Child ID Request: **493.904 ms**
- Child ID Request -> Response: **13.134 ms**
- Full Attach: **762.378 ms**
- pcap parent request: `03:53:27.952` (frame 229)
- pcap parent response: `03:53:28.208` (frame 230)
- pcap child id request: `03:53:28.702` (frame 232)
- pcap child id response: `03:53:28.715` (frame 234)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260722-035534-run03.log`

- manifest status: `completed`
- child extaddr: `2a5329a79ca186a4`

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
- parent extaddr: `a665e859c99580c0`
- parent rloc16: `n/a`
- child extaddr: `2a5329a79ca186a4`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **335.24 ms**
- Response -> Child ID Request: **415.745 ms**
- Child ID Request -> Response: **13.281 ms**
- Full Attach: **764.266 ms**
- pcap parent request: `04:01:15.245` (frame 73)
- pcap parent response: `04:01:15.580` (frame 74)
- pcap child id request: `04:01:15.996` (frame 79)
- pcap child id response: `04:01:16.009` (frame 81)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `fa9b4e4be2006c7c`
- parent rloc16: `n/a`
- child extaddr: `2a5329a79ca186a4`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **336.684 ms**
- Response -> Child ID Request: **413.672 ms**
- Child ID Request -> Response: **14.361 ms**
- Full Attach: **764.717 ms**
- pcap parent request: `04:05:15.376` (frame 221)
- pcap parent response: `04:05:15.712` (frame 222)
- pcap child id request: `04:05:16.126` (frame 224)
- pcap child id response: `04:05:16.140` (frame 226)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260722-040722-run04.log`

- manifest status: `completed`
- child extaddr: `969b7531212f5128`

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
- parent extaddr: `2664a327974b2c99`
- parent rloc16: `n/a`
- child extaddr: `969b7531212f5128`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **202.404 ms**
- Response -> Child ID Request: **546.577 ms**
- Child ID Request -> Response: **14.455 ms**
- Full Attach: **763.436 ms**
- pcap parent request: `04:13:02.812` (frame 79)
- pcap parent response: `04:13:03.015` (frame 80)
- pcap child id request: `04:13:03.561` (frame 85)
- pcap child id response: `04:13:03.576` (frame 87)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `22bc5f229427b0bb`
- parent rloc16: `n/a`
- child extaddr: `969b7531212f5128`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **60.243 ms**
- Response -> Child ID Request: **690.023 ms**
- Child ID Request -> Response: **12.225 ms**
- Full Attach: **762.491 ms**
- pcap parent request: `04:17:03.287` (frame 227)
- pcap parent response: `04:17:03.348` (frame 228)
- pcap child id request: `04:17:04.038` (frame 230)
- pcap child id response: `04:17:04.050` (frame 232)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260722-041909-run05.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `f6bdc42727c6f13d`

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
- parent extaddr: `3a7d5c2f300aebc1`
- parent rloc16: `n/a`
- child extaddr: `f6bdc42727c6f13d`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **278.704 ms**
- Response -> Child ID Request: **473.296 ms**
- Child ID Request -> Response: **13.969 ms**
- Full Attach: **765.969 ms**
- pcap parent request: `04:24:50.216` (frame 77)
- pcap parent response: `04:24:50.495` (frame 78)
- pcap child id request: `04:24:50.968` (frame 82)
- pcap child id response: `04:24:50.982` (frame 84)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `fe4abb12e900aea6`
- parent rloc16: `n/a`
- child extaddr: `f6bdc42727c6f13d`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **255.781 ms**
- Response -> Child ID Request: **496.368 ms**
- Child ID Request -> Response: **15.016 ms**
- Full Attach: **767.165 ms**
- pcap parent request: `04:28:50.155` (frame 235)
- pcap parent response: `04:28:50.411` (frame 236)
- pcap child id request: `04:28:50.908` (frame 238)
- pcap child id response: `04:28:50.923` (frame 240)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260722-043057-run06.log`

- manifest status: `completed`
- child extaddr: `26a41c8e0b812351`

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
- parent extaddr: `f698cadac3a00c35`
- parent rloc16: `n/a`
- child extaddr: `26a41c8e0b812351`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **10.222 ms**
- Response -> Child ID Request: **740.744 ms**
- Child ID Request -> Response: **14.291 ms**
- Full Attach: **765.257 ms**
- pcap parent request: `04:36:37.866` (frame 73)
- pcap parent response: `04:36:37.877` (frame 74)
- pcap child id request: `04:36:38.617` (frame 79)
- pcap child id response: `04:36:38.632` (frame 81)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `fe30a7f18095aa3e`
- parent rloc16: `n/a`
- child extaddr: `26a41c8e0b812351`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **234.814 ms**
- Response -> Child ID Request: **517.196 ms**
- Child ID Request -> Response: **12.848 ms**
- Full Attach: **764.858 ms**
- pcap parent request: `04:40:37.925` (frame 221)
- pcap parent response: `04:40:38.160` (frame 222)
- pcap child id request: `04:40:38.677` (frame 224)
- pcap child id response: `04:40:38.690` (frame 226)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260722-044244-run07.log`

- manifest status: `completed`
- child extaddr: `da859d150437b760`

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
- parent extaddr: `d2879cf77272d601`
- parent rloc16: `n/a`
- child extaddr: `da859d150437b760`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **74.978 ms**
- Response -> Child ID Request: **677.029 ms**
- Child ID Request -> Response: **15.014 ms**
- Full Attach: **767.021 ms**
- pcap parent request: `04:48:25.111` (frame 80)
- pcap parent response: `04:48:25.186` (frame 81)
- pcap child id request: `04:48:25.863` (frame 85)
- pcap child id response: `04:48:25.878` (frame 87)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `9e779871f4675568`
- parent rloc16: `n/a`
- child extaddr: `da859d150437b760`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **314.799 ms**
- Response -> Child ID Request: **437.945 ms**
- Child ID Request -> Response: **12.592 ms**
- Full Attach: **765.336 ms**
- pcap parent request: `04:52:25.078` (frame 225)
- pcap parent response: `04:52:25.393` (frame 226)
- pcap child id request: `04:52:25.831` (frame 228)
- pcap child id response: `04:52:25.844` (frame 230)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260722-045432-run08.log`

- manifest status: `completed`
- child extaddr: `5e9c91506b5a1d27`

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
- parent extaddr: `fe10a9466be16821`
- parent rloc16: `n/a`
- child extaddr: `5e9c91506b5a1d27`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **293.05 ms**
- Response -> Child ID Request: **459.068 ms**
- Child ID Request -> Response: **13.961 ms**
- Full Attach: **766.079 ms**
- pcap parent request: `05:00:13.032` (frame 78)
- pcap parent response: `05:00:13.325` (frame 79)
- pcap child id request: `05:00:13.784` (frame 83)
- pcap child id response: `05:00:13.798` (frame 85)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `6e5cece067b18fce`
- parent rloc16: `n/a`
- child extaddr: `5e9c91506b5a1d27`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **494.804 ms**
- Response -> Child ID Request: **256.203 ms**
- Child ID Request -> Response: **13.066 ms**
- Full Attach: **764.073 ms**
- pcap parent request: `05:04:13.119` (frame 228)
- pcap parent response: `05:04:13.614` (frame 229)
- pcap child id request: `05:04:13.870` (frame 231)
- pcap child id response: `05:04:13.883` (frame 233)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260722-050619-run09.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `42f24f05e377471b`

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
- parent extaddr: `3efd5dde3a0c2486`
- parent rloc16: `n/a`
- child extaddr: `42f24f05e377471b`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **109.638 ms**
- Response -> Child ID Request: **640.646 ms**
- Child ID Request -> Response: **13.389 ms**
- Full Attach: **763.673 ms**
- pcap parent request: `05:12:00.394` (frame 76)
- pcap parent response: `05:12:00.504` (frame 77)
- pcap child id request: `05:12:01.144` (frame 81)
- pcap child id response: `05:12:01.158` (frame 83)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `527dda466efe9b61`
- parent rloc16: `n/a`
- child extaddr: `42f24f05e377471b`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **14.917 ms**
- Response -> Child ID Request: **735.441 ms**
- Child ID Request -> Response: **12.803 ms**
- Full Attach: **763.161 ms**
- pcap parent request: `05:16:00.808` (frame 234)
- pcap parent response: `05:16:00.823` (frame 235)
- pcap child id request: `05:16:01.558` (frame 237)
- pcap child id response: `05:16:01.571` (frame 239)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260722-051807-run10.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `96270f73a1521de5`

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
- parent extaddr: `2e1fe48668746acf`
- parent rloc16: `n/a`
- child extaddr: `96270f73a1521de5`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **28.479 ms**
- Response -> Child ID Request: **724.51 ms**
- Child ID Request -> Response: **13.946 ms**
- Full Attach: **766.935 ms**
- pcap parent request: `05:23:48.532` (frame 72)
- pcap parent response: `05:23:48.560` (frame 73)
- pcap child id request: `05:23:49.285` (frame 77)
- pcap child id response: `05:23:49.299` (frame 79)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `f67cab5849989b13`
- parent rloc16: `n/a`
- child extaddr: `96270f73a1521de5`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **344.121 ms**
- Response -> Child ID Request: **408.652 ms**
- Child ID Request -> Response: **14.377 ms**
- Full Attach: **767.15 ms**
- pcap parent request: `05:27:48.560` (frame 232)
- pcap parent response: `05:27:48.904` (frame 233)
- pcap child id request: `05:27:49.313` (frame 235)
- pcap child id response: `05:27:49.327` (frame 237)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260722-052955-run11.log`

- manifest status: `completed`
- child extaddr: `9e44aa7d25a57a4a`

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
- parent extaddr: `e2c2e72e96e874d5`
- parent rloc16: `n/a`
- child extaddr: `9e44aa7d25a57a4a`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **40.814 ms**
- Response -> Child ID Request: **711.17 ms**
- Child ID Request -> Response: **13.12 ms**
- Full Attach: **765.104 ms**
- pcap parent request: `05:35:35.853` (frame 79)
- pcap parent response: `05:35:35.894` (frame 80)
- pcap child id request: `05:35:36.605` (frame 84)
- pcap child id response: `05:35:36.619` (frame 86)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `de8abf3478f1f96b`
- parent rloc16: `n/a`
- child extaddr: `9e44aa7d25a57a4a`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **229.099 ms**
- Response -> Child ID Request: **522.918 ms**
- Child ID Request -> Response: **13.122 ms**
- Full Attach: **765.139 ms**
- pcap parent request: `05:39:35.809` (frame 227)
- pcap parent response: `05:39:36.038` (frame 228)
- pcap child id request: `05:39:36.561` (frame 230)
- pcap child id response: `05:39:36.574` (frame 232)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260722-054142-run12.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `f654caf1f0baf49d`

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
- parent extaddr: `de5f3c78b6c2dee8`
- parent rloc16: `n/a`
- child extaddr: `f654caf1f0baf49d`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **96.036 ms**
- Response -> Child ID Request: **654.98 ms**
- Child ID Request -> Response: **14.063 ms**
- Full Attach: **765.079 ms**
- pcap parent request: `05:47:23.520` (frame 72)
- pcap parent response: `05:47:23.616` (frame 73)
- pcap child id request: `05:47:24.271` (frame 77)
- pcap child id response: `05:47:24.285` (frame 79)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `ee1eb6f7359f5bc1`
- parent rloc16: `n/a`
- child extaddr: `f654caf1f0baf49d`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **145.033 ms**
- Response -> Child ID Request: **606.988 ms**
- Child ID Request -> Response: **12.255 ms**
- Full Attach: **764.276 ms**
- pcap parent request: `05:51:24.125` (frame 230)
- pcap parent response: `05:51:24.270` (frame 231)
- pcap child id request: `05:51:24.877` (frame 233)
- pcap child id response: `05:51:24.889` (frame 235)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260722-055330-run13.log`

- manifest status: `completed`
- child extaddr: `0ab1d0ae3e785935`

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
- parent extaddr: `b2eeb8fcf721dea6`
- parent rloc16: `n/a`
- child extaddr: `0ab1d0ae3e785935`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **14.085 ms**
- Response -> Child ID Request: **735.796 ms**
- Child ID Request -> Response: **14.245 ms**
- Full Attach: **764.126 ms**
- pcap parent request: `05:59:10.585` (frame 72)
- pcap parent response: `05:59:10.599` (frame 73)
- pcap child id request: `05:59:11.335` (frame 77)
- pcap child id response: `05:59:11.349` (frame 79)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `3a6446dc649be114`
- parent rloc16: `n/a`
- child extaddr: `0ab1d0ae3e785935`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **430.288 ms**
- Response -> Child ID Request: **321.037 ms**
- Child ID Request -> Response: **14.335 ms**
- Full Attach: **765.66 ms**
- pcap parent request: `06:03:10.993` (frame 219)
- pcap parent response: `06:03:11.423` (frame 220)
- pcap child id request: `06:03:11.745` (frame 222)
- pcap child id response: `06:03:11.759` (frame 224)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260722-060517-run14.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `8231edad30402a72`

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
- parent extaddr: `de780fba4db24cdf`
- parent rloc16: `n/a`
- child extaddr: `8231edad30402a72`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **177.117 ms**
- Response -> Child ID Request: **576.049 ms**
- Child ID Request -> Response: **14.351 ms**
- Full Attach: **767.517 ms**
- pcap parent request: `06:10:58.667` (frame 73)
- pcap parent response: `06:10:58.844` (frame 74)
- pcap child id request: `06:10:59.420` (frame 78)
- pcap child id response: `06:10:59.435` (frame 80)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `c61cde8af6a3fd79`
- parent rloc16: `n/a`
- child extaddr: `8231edad30402a72`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **182.112 ms**
- Response -> Child ID Request: **571.857 ms**
- Child ID Request -> Response: **14.521 ms**
- Full Attach: **768.49 ms**
- pcap parent request: `06:14:59.286` (frame 231)
- pcap parent response: `06:14:59.468` (frame 232)
- pcap child id request: `06:15:00.040` (frame 234)
- pcap child id response: `06:15:00.055` (frame 236)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260722-061705-run15.log`

- manifest status: `completed`
- child extaddr: `aeec09ec27c26e9e`

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
- parent extaddr: `921393085c1d2ccb`
- parent rloc16: `n/a`
- child extaddr: `aeec09ec27c26e9e`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **26.713 ms**
- Response -> Child ID Request: **725.284 ms**
- Child ID Request -> Response: **13.762 ms**
- Full Attach: **765.759 ms**
- pcap parent request: `06:22:46.168` (frame 78)
- pcap parent response: `06:22:46.195` (frame 79)
- pcap child id request: `06:22:46.920` (frame 83)
- pcap child id response: `06:22:46.934` (frame 85)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `9a5254ce531098c9`
- parent rloc16: `n/a`
- child extaddr: `aeec09ec27c26e9e`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **367.971 ms**
- Response -> Child ID Request: **383.05 ms**
- Child ID Request -> Response: **12.242 ms**
- Full Attach: **763.263 ms**
- pcap parent request: `06:26:46.421` (frame 226)
- pcap parent response: `06:26:46.789` (frame 227)
- pcap child id request: `06:26:47.172` (frame 229)
- pcap child id response: `06:26:47.184` (frame 231)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260722-062852-run16.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `be186534faf457ec`

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
- parent extaddr: `2a8f7e72d9b53a77`
- parent rloc16: `n/a`
- child extaddr: `be186534faf457ec`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **10.176 ms**
- Response -> Child ID Request: **738.826 ms**
- Child ID Request -> Response: **14.575 ms**
- Full Attach: **763.577 ms**
- pcap parent request: `06:34:33.374` (frame 74)
- pcap parent response: `06:34:33.384` (frame 75)
- pcap child id request: `06:34:34.123` (frame 79)
- pcap child id response: `06:34:34.137` (frame 81)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `1e85cfba71f5d3b7`
- parent rloc16: `n/a`
- child extaddr: `be186534faf457ec`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **398.974 ms**
- Response -> Child ID Request: **353.029 ms**
- Child ID Request -> Response: **12.187 ms**
- Full Attach: **764.19 ms**
- pcap parent request: `06:38:33.848` (frame 233)
- pcap parent response: `06:38:34.247` (frame 234)
- pcap child id request: `06:38:34.600` (frame 236)
- pcap child id response: `06:38:34.612` (frame 238)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260722-064040-run17.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `36297e9262223ef8`

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
- parent extaddr: `421b809ee68f444b`
- parent rloc16: `n/a`
- child extaddr: `36297e9262223ef8`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **258.633 ms**
- Response -> Child ID Request: **493.37 ms**
- Child ID Request -> Response: **14.663 ms**
- Full Attach: **766.666 ms**
- pcap parent request: `06:46:20.589` (frame 75)
- pcap parent response: `06:46:20.847` (frame 76)
- pcap child id request: `06:46:21.341` (frame 80)
- pcap child id response: `06:46:21.355` (frame 82)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `06d6e15831b6642e`
- parent rloc16: `n/a`
- child extaddr: `36297e9262223ef8`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **247.646 ms**
- Response -> Child ID Request: **502.369 ms**
- Child ID Request -> Response: **13.673 ms**
- Full Attach: **763.688 ms**
- pcap parent request: `06:50:21.049` (frame 236)
- pcap parent response: `06:50:21.296` (frame 237)
- pcap child id request: `06:50:21.799` (frame 239)
- pcap child id response: `06:50:21.812` (frame 241)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260722-065227-run18.log`

- manifest status: `completed`
- child extaddr: `4294a05d35fbff0c`

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
- parent extaddr: `729092fe8d5d0c62`
- parent rloc16: `n/a`
- child extaddr: `4294a05d35fbff0c`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **38.051 ms**
- Response -> Child ID Request: **712.858 ms**
- Child ID Request -> Response: **12.403 ms**
- Full Attach: **763.312 ms**
- pcap parent request: `06:58:08.767` (frame 79)
- pcap parent response: `06:58:08.805` (frame 80)
- pcap child id request: `06:58:09.518` (frame 84)
- pcap child id response: `06:58:09.530` (frame 86)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `d6e40c97397ab615`
- parent rloc16: `n/a`
- child extaddr: `4294a05d35fbff0c`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **432.221 ms**
- Response -> Child ID Request: **318.808 ms**
- Child ID Request -> Response: **14.207 ms**
- Full Attach: **765.236 ms**
- pcap parent request: `07:02:09.350` (frame 227)
- pcap parent response: `07:02:09.782` (frame 228)
- pcap child id request: `07:02:10.101` (frame 230)
- pcap child id response: `07:02:10.115` (frame 232)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260722-070415-run19.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `1a852d94d55e5520`

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
- parent extaddr: `b240865479534de0`
- parent rloc16: `n/a`
- child extaddr: `1a852d94d55e5520`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **42.875 ms**
- Response -> Child ID Request: **707.107 ms**
- Child ID Request -> Response: **14.237 ms**
- Full Attach: **764.219 ms**
- pcap parent request: `07:09:55.944` (frame 73)
- pcap parent response: `07:09:55.987` (frame 74)
- pcap child id request: `07:09:56.694` (frame 78)
- pcap child id response: `07:09:56.709` (frame 80)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `6a176c58b37659ec`
- parent rloc16: `n/a`
- child extaddr: `1a852d94d55e5520`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **195.939 ms**
- Response -> Child ID Request: **555.076 ms**
- Child ID Request -> Response: **13.213 ms**
- Full Attach: **764.228 ms**
- pcap parent request: `07:13:55.961` (frame 233)
- pcap parent response: `07:13:56.157` (frame 234)
- pcap child id request: `07:13:56.712` (frame 236)
- pcap child id response: `07:13:56.726` (frame 238)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260722-071603-run20.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `5aee43c597347224`

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
- parent extaddr: `b228ea1ea3de0eb7`
- parent rloc16: `n/a`
- child extaddr: `5aee43c597347224`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **275.199 ms**
- Response -> Child ID Request: **473.819 ms**
- Child ID Request -> Response: **12.431 ms**
- Full Attach: **761.449 ms**
- pcap parent request: `07:21:43.671` (frame 77)
- pcap parent response: `07:21:43.947` (frame 78)
- pcap child id request: `07:21:44.420` (frame 82)
- pcap child id response: `07:21:44.433` (frame 84)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `5ea0a788a905905b`
- parent rloc16: `n/a`
- child extaddr: `5aee43c597347224`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **51.466 ms**
- Response -> Child ID Request: **701.265 ms**
- Child ID Request -> Response: **13.787 ms**
- Full Attach: **766.518 ms**
- pcap parent request: `07:25:43.960` (frame 236)
- pcap parent response: `07:25:44.011` (frame 237)
- pcap child id request: `07:25:44.712` (frame 239)
- pcap child id response: `07:25:44.726` (frame 241)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**
