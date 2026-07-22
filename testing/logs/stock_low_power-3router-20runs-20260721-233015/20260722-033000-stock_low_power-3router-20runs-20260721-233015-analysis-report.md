# Child Log Analysis

## stock_child

Files analyzed: **20**

- batch folders: `stock_low_power-3router-20runs-20260721-233015`

### PCAP-complete child attach summary

| Attach | Metric | M (SD), ms | n |
| --- | --- | ---: | ---: |
| 1 | Request -> Response | 179.27 (117.52) | 20 |
| 1 | Response -> Child ID Request | 572.60 (117.65) | 20 |
| 1 | Child ID Request -> Response | 13.61 (0.65) | 20 |
| 1 | Full Attach | 765.48 (1.65) | 20 |
| 2 | Request -> Response | 298.69 (120.92) | 20 |
| 2 | Response -> Child ID Request | 452.07 (120.37) | 20 |
| 2 | Child ID Request -> Response | 13.80 (0.95) | 20 |
| 2 | Full Attach | 764.56 (1.97) | 20 |

| Metric | M (SD) | n |
| --- | ---: | ---: |
| Failed TX Attempts per Log | 0.00 (0.00) | 20 |
| Log-only or Partial Sequences per Log | 0.00 (0.00) | 20 |

### `stock_child_20260721-233207-run01.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `269110d1a9ce2ac1`

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
- parent extaddr: `26233f4174ed99a9`
- parent rloc16: `n/a`
- child extaddr: `269110d1a9ce2ac1`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **130.322 ms**
- Response -> Child ID Request: **619.682 ms**
- Child ID Request -> Response: **12.972 ms**
- Full Attach: **762.976 ms**
- pcap parent request: `23:37:54.019` (frame 134)
- pcap parent response: `23:37:54.149` (frame 135)
- pcap child id request: `23:37:54.769` (frame 141)
- pcap child id response: `23:37:54.782` (frame 143)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `3e336f4288324f66`
- parent rloc16: `n/a`
- child extaddr: `269110d1a9ce2ac1`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **108.008 ms**
- Response -> Child ID Request: **641.999 ms**
- Child ID Request -> Response: **12.645 ms**
- Full Attach: **762.652 ms**
- pcap parent request: `23:41:54.686` (frame 388)
- pcap parent response: `23:41:54.794` (frame 389)
- pcap child id request: `23:41:55.436` (frame 393)
- pcap child id response: `23:41:55.449` (frame 395)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260721-234401-run02.log`

- manifest status: `completed`
- child extaddr: `d6b0c664fc744536`

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
- parent extaddr: `6eb22a04024627dd`
- parent rloc16: `n/a`
- child extaddr: `d6b0c664fc744536`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **367.096 ms**
- Response -> Child ID Request: **385.968 ms**
- Child ID Request -> Response: **14.057 ms**
- Full Attach: **767.121 ms**
- pcap parent request: `23:49:46.602` (frame 126)
- pcap parent response: `23:49:46.969` (frame 129)
- pcap child id request: `23:49:47.355` (frame 133)
- pcap child id response: `23:49:47.369` (frame 135)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `bed313aaeec4a46e`
- parent rloc16: `n/a`
- child extaddr: `d6b0c664fc744536`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **333.779 ms**
- Response -> Child ID Request: **417.221 ms**
- Child ID Request -> Response: **12.792 ms**
- Full Attach: **763.792 ms**
- pcap parent request: `23:53:47.302` (frame 344)
- pcap parent response: `23:53:47.636` (frame 347)
- pcap child id request: `23:53:48.053` (frame 349)
- pcap child id response: `23:53:48.066` (frame 351)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260721-235553-run03.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `aa86371a05b4ce8d`

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
- parent extaddr: `c63e1569cd51a9ef`
- parent rloc16: `n/a`
- child extaddr: `aa86371a05b4ce8d`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **80.485 ms**
- Response -> Child ID Request: **672.682 ms**
- Child ID Request -> Response: **13.346 ms**
- Full Attach: **766.513 ms**
- pcap parent request: `00:01:39.529` (frame 123)
- pcap parent response: `00:01:39.610` (frame 124)
- pcap child id request: `00:01:40.282` (frame 130)
- pcap child id response: `00:01:40.296` (frame 132)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `4237bfa69ec341f3`
- parent rloc16: `n/a`
- child extaddr: `aa86371a05b4ce8d`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **296.607 ms**
- Response -> Child ID Request: **455.128 ms**
- Child ID Request -> Response: **14.903 ms**
- Full Attach: **766.638 ms**
- pcap parent request: `00:05:39.608` (frame 380)
- pcap parent response: `00:05:39.904` (frame 383)
- pcap child id request: `00:05:40.359` (frame 385)
- pcap child id response: `00:05:40.374` (frame 387)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260722-000746-run04.log`

- manifest status: `completed`
- child extaddr: `c6e0b59aa8e8ab90`

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
- parent extaddr: `1effdd7129f3159e`
- parent rloc16: `n/a`
- child extaddr: `c6e0b59aa8e8ab90`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **81.456 ms**
- Response -> Child ID Request: **671.663 ms**
- Child ID Request -> Response: **14.643 ms**
- Full Attach: **767.762 ms**
- pcap parent request: `00:13:31.919` (frame 123)
- pcap parent response: `00:13:32.001` (frame 124)
- pcap child id request: `00:13:32.673` (frame 130)
- pcap child id response: `00:13:32.687` (frame 132)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `e6656a6014d22c41`
- parent rloc16: `n/a`
- child extaddr: `c6e0b59aa8e8ab90`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **458.494 ms**
- Response -> Child ID Request: **291.809 ms**
- Child ID Request -> Response: **13.217 ms**
- Full Attach: **763.52 ms**
- pcap parent request: `00:17:31.913` (frame 343)
- pcap parent response: `00:17:32.372` (frame 344)
- pcap child id request: `00:17:32.664` (frame 348)
- pcap child id response: `00:17:32.677` (frame 350)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260722-001938-run05.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `1a7b229a870f7df0`

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
- parent extaddr: `52a6cd5cb1009908`
- parent rloc16: `n/a`
- child extaddr: `1a7b229a870f7df0`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **128.338 ms**
- Response -> Child ID Request: **624.675 ms**
- Child ID Request -> Response: **13.69 ms**
- Full Attach: **766.703 ms**
- pcap parent request: `00:25:24.027` (frame 129)
- pcap parent response: `00:25:24.155` (frame 130)
- pcap child id request: `00:25:24.780` (frame 137)
- pcap child id response: `00:25:24.794` (frame 139)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `6a2a3fac7d2172db`
- parent rloc16: `n/a`
- child extaddr: `1a7b229a870f7df0`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **205.464 ms**
- Response -> Child ID Request: **542.768 ms**
- Child ID Request -> Response: **15.616 ms**
- Full Attach: **763.848 ms**
- pcap parent request: `00:29:24.151` (frame 372)
- pcap parent response: `00:29:24.356` (frame 373)
- pcap child id request: `00:29:24.899` (frame 375)
- pcap child id response: `00:29:24.915` (frame 377)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260722-003131-run06.log`

- manifest status: `completed`
- child extaddr: `222fbbb91dfd8999`

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
- parent extaddr: `76531a185b82f652`
- parent rloc16: `n/a`
- child extaddr: `222fbbb91dfd8999`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **319.826 ms**
- Response -> Child ID Request: **432.162 ms**
- Child ID Request -> Response: **13.236 ms**
- Full Attach: **765.224 ms**
- pcap parent request: `00:37:17.074` (frame 119)
- pcap parent response: `00:37:17.394` (frame 122)
- pcap child id request: `00:37:17.826` (frame 126)
- pcap child id response: `00:37:17.840` (frame 128)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `b67700f2d0634e07`
- parent rloc16: `n/a`
- child extaddr: `222fbbb91dfd8999`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **214.14 ms**
- Response -> Child ID Request: **537.866 ms**
- Child ID Request -> Response: **13.163 ms**
- Full Attach: **765.169 ms**
- pcap parent request: `00:41:17.321` (frame 338)
- pcap parent response: `00:41:17.535` (frame 341)
- pcap child id request: `00:41:18.073` (frame 343)
- pcap child id response: `00:41:18.086` (frame 345)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260722-004323-run07.log`

- manifest status: `completed`
- child extaddr: `fed0d1ecf4632516`

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
- parent extaddr: `7e2883fa7f6d2d49`
- parent rloc16: `n/a`
- child extaddr: `fed0d1ecf4632516`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **135.938 ms**
- Response -> Child ID Request: **614.099 ms**
- Child ID Request -> Response: **13.154 ms**
- Full Attach: **763.191 ms**
- pcap parent request: `00:49:09.128` (frame 122)
- pcap parent response: `00:49:09.264` (frame 123)
- pcap child id request: `00:49:09.878` (frame 129)
- pcap child id response: `00:49:09.892` (frame 131)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `c6b8d3d97634e320`
- parent rloc16: `n/a`
- child extaddr: `fed0d1ecf4632516`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **144.132 ms**
- Response -> Child ID Request: **604.892 ms**
- Child ID Request -> Response: **13.139 ms**
- Full Attach: **762.163 ms**
- pcap parent request: `00:53:09.620` (frame 342)
- pcap parent response: `00:53:09.764` (frame 345)
- pcap child id request: `00:53:10.369` (frame 348)
- pcap child id response: `00:53:10.382` (frame 350)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260722-005516-run08.log`

- manifest status: `completed`
- child extaddr: `ee01afbfc63dcef9`

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
- parent extaddr: `82cd11779945f321`
- parent rloc16: `n/a`
- child extaddr: `ee01afbfc63dcef9`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **163.275 ms**
- Response -> Child ID Request: **586.698 ms**
- Child ID Request -> Response: **13.334 ms**
- Full Attach: **763.307 ms**
- pcap parent request: `01:01:01.739` (frame 129)
- pcap parent response: `01:01:01.902` (frame 130)
- pcap child id request: `01:01:02.489` (frame 136)
- pcap child id response: `01:01:02.502` (frame 138)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `9e68297a87a15b8a`
- parent rloc16: `n/a`
- child extaddr: `ee01afbfc63dcef9`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **254.169 ms**
- Response -> Child ID Request: **495.835 ms**
- Child ID Request -> Response: **14.505 ms**
- Full Attach: **764.509 ms**
- pcap parent request: `01:05:02.403` (frame 346)
- pcap parent response: `01:05:02.657` (frame 347)
- pcap child id request: `01:05:03.153` (frame 351)
- pcap child id response: `01:05:03.167` (frame 353)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260722-010708-run09.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `5283a39a8ce55f56`

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
- parent extaddr: `2a58f794640a9bff`
- parent rloc16: `n/a`
- child extaddr: `5283a39a8ce55f56`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **98.669 ms**
- Response -> Child ID Request: **653.321 ms**
- Child ID Request -> Response: **13.719 ms**
- Full Attach: **765.709 ms**
- pcap parent request: `01:12:54.039` (frame 124)
- pcap parent response: `01:12:54.138` (frame 125)
- pcap child id request: `01:12:54.791` (frame 131)
- pcap child id response: `01:12:54.805` (frame 133)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `6ecf7e4e4ba5f64d`
- parent rloc16: `n/a`
- child extaddr: `5283a39a8ce55f56`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **407.215 ms**
- Response -> Child ID Request: **343.083 ms**
- Child ID Request -> Response: **14.933 ms**
- Full Attach: **765.231 ms**
- pcap parent request: `01:16:54.413` (frame 365)
- pcap parent response: `01:16:54.821` (frame 366)
- pcap child id request: `01:16:55.164` (frame 368)
- pcap child id response: `01:16:55.179` (frame 370)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260722-011901-run10.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `7a042e0edd36294b`

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
- parent extaddr: `8abac1baead68652`
- parent rloc16: `n/a`
- child extaddr: `7a042e0edd36294b`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **55.304 ms**
- Response -> Child ID Request: **698.793 ms**
- Child ID Request -> Response: **13.25 ms**
- Full Attach: **767.347 ms**
- pcap parent request: `01:24:46.429` (frame 117)
- pcap parent response: `01:24:46.484` (frame 118)
- pcap child id request: `01:24:47.183` (frame 124)
- pcap child id response: `01:24:47.196` (frame 126)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `7a81d32dac7db225`
- parent rloc16: `n/a`
- child extaddr: `7a042e0edd36294b`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **464.621 ms**
- Response -> Child ID Request: **288.37 ms**
- Child ID Request -> Response: **13.665 ms**
- Full Attach: **766.656 ms**
- pcap parent request: `01:28:46.868` (frame 377)
- pcap parent response: `01:28:47.333` (frame 380)
- pcap child id request: `01:28:47.621` (frame 382)
- pcap child id response: `01:28:47.635` (frame 384)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260722-013053-run11.log`

- manifest status: `completed`
- child extaddr: `16ce7b4818002c89`

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
- parent extaddr: `1e0bfa0e488645ae`
- parent rloc16: `n/a`
- child extaddr: `16ce7b4818002c89`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **125.183 ms**
- Response -> Child ID Request: **626.815 ms**
- Child ID Request -> Response: **14.567 ms**
- Full Attach: **766.565 ms**
- pcap parent request: `01:36:38.965` (frame 131)
- pcap parent response: `01:36:39.090` (frame 132)
- pcap child id request: `01:36:39.717` (frame 138)
- pcap child id response: `01:36:39.731` (frame 140)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `ee47bfc4053478f6`
- parent rloc16: `n/a`
- child extaddr: `16ce7b4818002c89`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **431.486 ms**
- Response -> Child ID Request: **321.504 ms**
- Child ID Request -> Response: **14.51 ms**
- Full Attach: **767.5 ms**
- pcap parent request: `01:40:39.615` (frame 349)
- pcap parent response: `01:40:40.046` (frame 352)
- pcap child id request: `01:40:40.368` (frame 355)
- pcap child id response: `01:40:40.382` (frame 357)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260722-014246-run12.log`

- manifest status: `completed`
- child extaddr: `ba7e84b932821486`

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
- parent extaddr: `ced428b8e542617f`
- parent rloc16: `n/a`
- child extaddr: `ba7e84b932821486`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **401.127 ms**
- Response -> Child ID Request: **351.864 ms**
- Child ID Request -> Response: **12.745 ms**
- Full Attach: **765.736 ms**
- pcap parent request: `01:48:31.939` (frame 127)
- pcap parent response: `01:48:32.341` (frame 128)
- pcap child id request: `01:48:32.692` (frame 134)
- pcap child id response: `01:48:32.705` (frame 136)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `6e2e24a17c89a9e2`
- parent rloc16: `n/a`
- child extaddr: `ba7e84b932821486`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **248.184 ms**
- Response -> Child ID Request: **500.026 ms**
- Child ID Request -> Response: **12.198 ms**
- Full Attach: **760.408 ms**
- pcap parent request: `01:52:31.925` (frame 346)
- pcap parent response: `01:52:32.174` (frame 347)
- pcap child id request: `01:52:32.674` (frame 351)
- pcap child id response: `01:52:32.686` (frame 353)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260722-015438-run13.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `2648530e7b587596`

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
- parent extaddr: `6a53961160ce9411`
- parent rloc16: `n/a`
- child extaddr: `2648530e7b587596`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **46.869 ms**
- Response -> Child ID Request: **704.122 ms**
- Child ID Request -> Response: **13.915 ms**
- Full Attach: **764.906 ms**
- pcap parent request: `02:00:24.192` (frame 119)
- pcap parent response: `02:00:24.239` (frame 120)
- pcap child id request: `02:00:24.943` (frame 126)
- pcap child id response: `02:00:24.957` (frame 128)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `da98f8c117ecffde`
- parent rloc16: `n/a`
- child extaddr: `2648530e7b587596`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **213.093 ms**
- Response -> Child ID Request: **539.919 ms**
- Child ID Request -> Response: **14.132 ms**
- Full Attach: **767.144 ms**
- pcap parent request: `02:04:24.789` (frame 378)
- pcap parent response: `02:04:25.002` (frame 379)
- pcap child id request: `02:04:25.542` (frame 383)
- pcap child id response: `02:04:25.556` (frame 385)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260722-020631-run14.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `ce18237507503ac7`

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
- parent extaddr: `5e793ef33c75ad9b`
- parent rloc16: `n/a`
- child extaddr: `ce18237507503ac7`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **234.198 ms**
- Response -> Child ID Request: **515.796 ms**
- Child ID Request -> Response: **12.808 ms**
- Full Attach: **762.802 ms**
- pcap parent request: `02:12:16.505` (frame 118)
- pcap parent response: `02:12:16.739` (frame 121)
- pcap child id request: `02:12:17.255` (frame 125)
- pcap child id response: `02:12:17.268` (frame 127)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `6aed643f06f6cb08`
- parent rloc16: `n/a`
- child extaddr: `ce18237507503ac7`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **328.018 ms**
- Response -> Child ID Request: **423.005 ms**
- Child ID Request -> Response: **13.026 ms**
- Full Attach: **764.049 ms**
- pcap parent request: `02:16:16.961` (frame 368)
- pcap parent response: `02:16:17.289` (frame 369)
- pcap child id request: `02:16:17.712` (frame 373)
- pcap child id response: `02:16:17.725` (frame 375)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260722-021823-run15.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `92196496b5a59661`

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
- parent extaddr: `525693929d48a5f8`
- parent rloc16: `n/a`
- child extaddr: `92196496b5a59661`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **332.958 ms**
- Response -> Child ID Request: **419.054 ms**
- Child ID Request -> Response: **12.985 ms**
- Full Attach: **764.997 ms**
- pcap parent request: `02:24:09.688` (frame 124)
- pcap parent response: `02:24:10.021` (frame 125)
- pcap child id request: `02:24:10.440` (frame 131)
- pcap child id response: `02:24:10.453` (frame 133)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `6e017eec471eacf2`
- parent rloc16: `n/a`
- child extaddr: `92196496b5a59661`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **481.887 ms**
- Response -> Child ID Request: **270.099 ms**
- Child ID Request -> Response: **13.913 ms**
- Full Attach: **765.899 ms**
- pcap parent request: `02:28:09.661` (frame 382)
- pcap parent response: `02:28:10.143` (frame 385)
- pcap child id request: `02:28:10.413` (frame 387)
- pcap child id response: `02:28:10.427` (frame 389)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260722-023016-run16.log`

- manifest status: `completed`
- child extaddr: `eaee4012baca6902`

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
- parent extaddr: `3604ce8c7403641b`
- parent rloc16: `n/a`
- child extaddr: `eaee4012baca6902`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **78.506 ms**
- Response -> Child ID Request: **673.44 ms**
- Child ID Request -> Response: **14.614 ms**
- Full Attach: **766.56 ms**
- pcap parent request: `02:36:01.642` (frame 126)
- pcap parent response: `02:36:01.721` (frame 127)
- pcap child id request: `02:36:02.394` (frame 133)
- pcap child id response: `02:36:02.409` (frame 135)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `864d5e7c7acec559`
- parent rloc16: `n/a`
- child extaddr: `eaee4012baca6902`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **374.815 ms**
- Response -> Child ID Request: **376.192 ms**
- Child ID Request -> Response: **13.049 ms**
- Full Attach: **764.056 ms**
- pcap parent request: `02:40:01.895` (frame 343)
- pcap parent response: `02:40:02.270` (frame 345)
- pcap child id request: `02:40:02.646` (frame 349)
- pcap child id response: `02:40:02.659` (frame 351)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260722-024208-run17.log`

- manifest status: `completed`
- child extaddr: `1e27256618b42e68`

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
- parent extaddr: `8275239053b55958`
- parent rloc16: `n/a`
- child extaddr: `1e27256618b42e68`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **83.051 ms**
- Response -> Child ID Request: **671.086 ms**
- Child ID Request -> Response: **13.965 ms**
- Full Attach: **768.102 ms**
- pcap parent request: `02:47:54.351` (frame 124)
- pcap parent response: `02:47:54.434` (frame 125)
- pcap child id request: `02:47:55.105` (frame 131)
- pcap child id response: `02:47:55.119` (frame 133)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `7226c5632fb356fa`
- parent rloc16: `n/a`
- child extaddr: `1e27256618b42e68`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **437.179 ms**
- Response -> Child ID Request: **312.158 ms**
- Child ID Request -> Response: **14.864 ms**
- Full Attach: **764.201 ms**
- pcap parent request: `02:51:54.564` (frame 344)
- pcap parent response: `02:51:55.001` (frame 347)
- pcap child id request: `02:51:55.313` (frame 349)
- pcap child id response: `02:51:55.328` (frame 351)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260722-025401-run18.log`

- manifest status: `completed`
- child extaddr: `665f15d30d5b1efa`

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
- parent extaddr: `46facc43e520f0a6`
- parent rloc16: `n/a`
- child extaddr: `665f15d30d5b1efa`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **249.409 ms**
- Response -> Child ID Request: **499.369 ms**
- Child ID Request -> Response: **14.661 ms**
- Full Attach: **763.439 ms**
- pcap parent request: `02:59:47.022` (frame 126)
- pcap parent response: `02:59:47.271` (frame 129)
- pcap child id request: `02:59:47.770` (frame 133)
- pcap child id response: `02:59:47.785` (frame 135)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `8a37993ded26a591`
- parent rloc16: `n/a`
- child extaddr: `665f15d30d5b1efa`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **210.804 ms**
- Response -> Child ID Request: **542.196 ms**
- Child ID Request -> Response: **14.843 ms**
- Full Attach: **767.843 ms**
- pcap parent request: `03:03:47.274` (frame 344)
- pcap parent response: `03:03:47.485` (frame 345)
- pcap child id request: `03:03:48.027` (frame 349)
- pcap child id response: `03:03:48.042` (frame 351)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260722-030554-run19.log`

- manifest status: `completed`
- child extaddr: `9a9b0786b8da0ef1`

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
- parent extaddr: `aa89fcbe4918a37e`
- parent rloc16: `n/a`
- child extaddr: `9a9b0786b8da0ef1`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **110.576 ms**
- Response -> Child ID Request: **641.418 ms**
- Child ID Request -> Response: **12.856 ms**
- Full Attach: **764.85 ms**
- pcap parent request: `03:11:39.589` (frame 130)
- pcap parent response: `03:11:39.700` (frame 131)
- pcap child id request: `03:11:40.341` (frame 137)
- pcap child id response: `03:11:40.354` (frame 139)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `060f674b30c0ffe8`
- parent rloc16: `n/a`
- child extaddr: `9a9b0786b8da0ef1`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **105.838 ms**
- Response -> Child ID Request: **643.188 ms**
- Child ID Request -> Response: **13.037 ms**
- Full Attach: **762.063 ms**
- pcap parent request: `03:15:39.581` (frame 349)
- pcap parent response: `03:15:39.687` (frame 352)
- pcap child id request: `03:15:40.330` (frame 354)
- pcap child id response: `03:15:40.343` (frame 356)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260722-031746-run20.log`

- manifest status: `completed`
- child extaddr: `8e2cfaa16d53f703`

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
- parent extaddr: `0e0eb899ed63b97d`
- parent rloc16: `n/a`
- child extaddr: `8e2cfaa16d53f703`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **362.814 ms**
- Response -> Child ID Request: **389.32 ms**
- Child ID Request -> Response: **13.72 ms**
- Full Attach: **765.854 ms**
- pcap parent request: `03:23:32.608` (frame 127)
- pcap parent response: `03:23:32.971` (frame 131)
- pcap child id request: `03:23:33.361` (frame 135)
- pcap child id response: `03:23:33.374` (frame 137)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `d605a0683a311235`
- parent rloc16: `n/a`
- child extaddr: `8e2cfaa16d53f703`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **255.905 ms**
- Response -> Child ID Request: **494.109 ms**
- Child ID Request -> Response: **13.908 ms**
- Full Attach: **763.922 ms**
- pcap parent request: `03:27:32.899` (frame 344)
- pcap parent response: `03:27:33.155` (frame 347)
- pcap child id request: `03:27:33.649` (frame 349)
- pcap child id response: `03:27:33.663` (frame 351)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**
