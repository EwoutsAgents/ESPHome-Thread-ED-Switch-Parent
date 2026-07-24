# Child Log Analysis

## stock_child

Files analyzed: **50**

- batch folders: `stock_low_power-2router-50runs-20260724-081653`

### PCAP-complete child attach summary

| Attach | Metric | M (SD), ms | n |
| --- | --- | ---: | ---: |
| 1 | Request -> Response | 168.46 (122.69) | 50 |
| 1 | Response -> Child ID Request | 582.96 (122.89) | 50 |
| 1 | Child ID Request -> Response | 14.06 (0.95) | 50 |
| 1 | Full Attach | 765.48 (1.65) | 50 |
| 2 | Request -> Response | 260.40 (143.12) | 50 |
| 2 | Response -> Child ID Request | 491.31 (143.42) | 50 |
| 2 | Child ID Request -> Response | 13.73 (0.79) | 50 |
| 2 | Full Attach | 765.45 (1.55) | 50 |

| Metric | M (SD) | n |
| --- | ---: | ---: |
| Failed TX Attempts per Log | 0.00 (0.00) | 50 |
| Log-only or Partial Sequences per Log | 0.00 (0.00) | 50 |

### `stock_child_20260724-081848-run01.log`

- manifest status: `completed`
- child extaddr: `629956afe53397d2`

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
- parent extaddr: `1688db637398e683`
- parent rloc16: `n/a`
- child extaddr: `629956afe53397d2`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **76.028 ms**
- Response -> Child ID Request: **673.981 ms**
- Child ID Request -> Response: **14.413 ms**
- Full Attach: **764.422 ms**
- pcap parent request: `08:22:00.114` (frame 53)
- pcap parent response: `08:22:00.190` (frame 54)
- pcap child id request: `08:22:00.864` (frame 59)
- pcap child id response: `08:22:00.878` (frame 61)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `f6e6171ec28af2f1`
- parent rloc16: `n/a`
- child extaddr: `629956afe53397d2`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **114.186 ms**
- Response -> Child ID Request: **637.82 ms**
- Child ID Request -> Response: **13.217 ms**
- Full Attach: **765.223 ms**
- pcap parent request: `08:26:00.178` (frame 200)
- pcap parent response: `08:26:00.292` (frame 201)
- pcap child id request: `08:26:00.930` (frame 203)
- pcap child id response: `08:26:00.943` (frame 205)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-082622-run02.log`

- manifest status: `completed`
- child extaddr: `626ac5d3b318b369`

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
- parent extaddr: `d6d0e8069e988fb0`
- parent rloc16: `n/a`
- child extaddr: `626ac5d3b318b369`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **68.333 ms**
- Response -> Child ID Request: **683.66 ms**
- Child ID Request -> Response: **15.351 ms**
- Full Attach: **767.344 ms**
- pcap parent request: `08:29:32.842` (frame 51)
- pcap parent response: `08:29:32.911` (frame 52)
- pcap child id request: `08:29:33.594` (frame 56)
- pcap child id response: `08:29:33.610` (frame 58)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `ee7348d07b87d3fe`
- parent rloc16: `n/a`
- child extaddr: `626ac5d3b318b369`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **490.291 ms**
- Response -> Child ID Request: **258.909 ms**
- Child ID Request -> Response: **13.13 ms**
- Full Attach: **762.33 ms**
- pcap parent request: `08:33:33.082` (frame 196)
- pcap parent response: `08:33:33.573` (frame 197)
- pcap child id request: `08:33:33.832` (frame 199)
- pcap child id response: `08:33:33.845` (frame 201)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-083354-run03.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `7aaccb6e9afb25e0`

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
- parent extaddr: `3ad3e8f3b1dd988e`
- parent rloc16: `n/a`
- child extaddr: `7aaccb6e9afb25e0`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **34.913 ms**
- Response -> Child ID Request: **714.98 ms**
- Child ID Request -> Response: **14.475 ms**
- Full Attach: **764.368 ms**
- pcap parent request: `08:37:05.258` (frame 51)
- pcap parent response: `08:37:05.293` (frame 52)
- pcap child id request: `08:37:06.008` (frame 56)
- pcap child id response: `08:37:06.023` (frame 58)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `9eb7dac50ed8e181`
- parent rloc16: `n/a`
- child extaddr: `7aaccb6e9afb25e0`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **116.48 ms**
- Response -> Child ID Request: **636.269 ms**
- Child ID Request -> Response: **12.965 ms**
- Full Attach: **765.714 ms**
- pcap parent request: `08:41:05.689` (frame 209)
- pcap parent response: `08:41:05.805` (frame 210)
- pcap child id request: `08:41:06.441` (frame 212)
- pcap child id response: `08:41:06.454` (frame 214)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-084127-run04.log`

- manifest status: `completed`
- child extaddr: `ee51a6e88ab31e9b`

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
- parent extaddr: `06f002cf77b0089b`
- parent rloc16: `n/a`
- child extaddr: `ee51a6e88ab31e9b`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **74.768 ms**
- Response -> Child ID Request: **676.237 ms**
- Child ID Request -> Response: **15.065 ms**
- Full Attach: **766.07 ms**
- pcap parent request: `08:44:38.797` (frame 48)
- pcap parent response: `08:44:38.872` (frame 49)
- pcap child id request: `08:44:39.548` (frame 53)
- pcap child id response: `08:44:39.563` (frame 55)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `4ef36b297f7df648`
- parent rloc16: `n/a`
- child extaddr: `ee51a6e88ab31e9b`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **308.051 ms**
- Response -> Child ID Request: **443.945 ms**
- Child ID Request -> Response: **12.693 ms**
- Full Attach: **764.689 ms**
- pcap parent request: `08:48:38.897` (frame 193)
- pcap parent response: `08:48:39.205` (frame 194)
- pcap child id request: `08:48:39.649` (frame 196)
- pcap child id response: `08:48:39.662` (frame 198)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-084900-run05.log`

- manifest status: `completed`
- child extaddr: `8ecc5d31627fe0b9`

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
- parent extaddr: `d22ed5b3efb15ac3`
- parent rloc16: `n/a`
- child extaddr: `8ecc5d31627fe0b9`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **215.723 ms**
- Response -> Child ID Request: **535.491 ms**
- Child ID Request -> Response: **15.538 ms**
- Full Attach: **766.752 ms**
- pcap parent request: `08:52:10.921` (frame 52)
- pcap parent response: `08:52:11.136` (frame 53)
- pcap child id request: `08:52:11.672` (frame 57)
- pcap child id response: `08:52:11.687` (frame 59)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `6e5702bf9efb2ad0`
- parent rloc16: `n/a`
- child extaddr: `8ecc5d31627fe0b9`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **159.379 ms**
- Response -> Child ID Request: **591.64 ms**
- Child ID Request -> Response: **13.403 ms**
- Full Attach: **764.422 ms**
- pcap parent request: `08:56:11.554` (frame 200)
- pcap parent response: `08:56:11.713` (frame 201)
- pcap child id request: `08:56:12.305` (frame 203)
- pcap child id response: `08:56:12.318` (frame 205)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-085633-run06.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `6a9a176cc1c17f33`

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
- parent extaddr: `b63202ecca95191a`
- parent rloc16: `n/a`
- child extaddr: `6a9a176cc1c17f33`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **25.723 ms**
- Response -> Child ID Request: **725.189 ms**
- Child ID Request -> Response: **13.853 ms**
- Full Attach: **764.765 ms**
- pcap parent request: `08:59:43.437` (frame 45)
- pcap parent response: `08:59:43.463` (frame 46)
- pcap child id request: `08:59:44.188` (frame 51)
- pcap child id response: `08:59:44.202` (frame 53)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `0e94d33a874e2863`
- parent rloc16: `n/a`
- child extaddr: `6a9a176cc1c17f33`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **465.549 ms**
- Response -> Child ID Request: **283.809 ms**
- Child ID Request -> Response: **12.436 ms**
- Full Attach: **761.794 ms**
- pcap parent request: `09:03:43.651` (frame 204)
- pcap parent response: `09:03:44.116` (frame 205)
- pcap child id request: `09:03:44.400` (frame 207)
- pcap child id response: `09:03:44.413` (frame 209)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-090405-run07.log`

- manifest status: `completed`
- child extaddr: `96f513e67359338d`

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
- parent extaddr: `265cfc9d43701f6a`
- parent rloc16: `n/a`
- child extaddr: `96f513e67359338d`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **145.608 ms**
- Response -> Child ID Request: **607.519 ms**
- Child ID Request -> Response: **15.508 ms**
- Full Attach: **768.635 ms**
- pcap parent request: `09:07:16.486` (frame 51)
- pcap parent response: `09:07:16.631` (frame 52)
- pcap child id request: `09:07:17.239` (frame 58)
- pcap child id response: `09:07:17.254` (frame 60)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `1e182da2e0e1968a`
- parent rloc16: `n/a`
- child extaddr: `96f513e67359338d`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **43.978 ms**
- Response -> Child ID Request: **709.743 ms**
- Child ID Request -> Response: **13.666 ms**
- Full Attach: **767.387 ms**
- pcap parent request: `09:11:17.088` (frame 198)
- pcap parent response: `09:11:17.132` (frame 199)
- pcap child id request: `09:11:17.842` (frame 201)
- pcap child id response: `09:11:17.856` (frame 203)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-091138-run08.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `8efc8641914302b0`

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
- parent extaddr: `3e5739b38604fdb6`
- parent rloc16: `n/a`
- child extaddr: `8efc8641914302b0`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **53.275 ms**
- Response -> Child ID Request: **697.625 ms**
- Child ID Request -> Response: **14.427 ms**
- Full Attach: **765.327 ms**
- pcap parent request: `09:14:49.422` (frame 55)
- pcap parent response: `09:14:49.475` (frame 56)
- pcap child id request: `09:14:50.173` (frame 60)
- pcap child id response: `09:14:50.187` (frame 62)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `56262aa8afa3c79f`
- parent rloc16: `n/a`
- child extaddr: `8efc8641914302b0`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **9.209 ms**
- Response -> Child ID Request: **743.789 ms**
- Child ID Request -> Response: **13.685 ms**
- Full Attach: **766.683 ms**
- pcap parent request: `09:18:49.613` (frame 214)
- pcap parent response: `09:18:49.622` (frame 215)
- pcap child id request: `09:18:50.366` (frame 217)
- pcap child id response: `09:18:50.380` (frame 219)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-091911-run09.log`

- manifest status: `completed`
- child extaddr: `5ede8acb8563d018`

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
- parent extaddr: `024a61d2a4f64bd8`
- parent rloc16: `n/a`
- child extaddr: `5ede8acb8563d018`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **24.372 ms**
- Response -> Child ID Request: **727.626 ms**
- Child ID Request -> Response: **13.419 ms**
- Full Attach: **765.417 ms**
- pcap parent request: `09:22:21.909` (frame 52)
- pcap parent response: `09:22:21.933` (frame 53)
- pcap child id request: `09:22:22.661` (frame 57)
- pcap child id response: `09:22:22.674` (frame 59)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `de6356e644e94a26`
- parent rloc16: `n/a`
- child extaddr: `5ede8acb8563d018`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **329.728 ms**
- Response -> Child ID Request: **421.305 ms**
- Child ID Request -> Response: **14.715 ms**
- Full Attach: **765.748 ms**
- pcap parent request: `09:26:22.576` (frame 199)
- pcap parent response: `09:26:22.905` (frame 200)
- pcap child id request: `09:26:23.327` (frame 202)
- pcap child id response: `09:26:23.341` (frame 204)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-092643-run10.log`

- manifest status: `completed`
- child extaddr: `627cec3dcbb3dcda`

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
- parent extaddr: `ee8d0a16d0e66e50`
- parent rloc16: `n/a`
- child extaddr: `627cec3dcbb3dcda`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **410.155 ms**
- Response -> Child ID Request: **341.859 ms**
- Child ID Request -> Response: **13.152 ms**
- Full Attach: **765.166 ms**
- pcap parent request: `09:29:54.693` (frame 51)
- pcap parent response: `09:29:55.103` (frame 52)
- pcap child id request: `09:29:55.445` (frame 56)
- pcap child id response: `09:29:55.458` (frame 58)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `d6bca98bfd0d3a0e`
- parent rloc16: `n/a`
- child extaddr: `627cec3dcbb3dcda`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **94.108 ms**
- Response -> Child ID Request: **658.577 ms**
- Child ID Request -> Response: **14.455 ms**
- Full Attach: **767.14 ms**
- pcap parent request: `09:33:55.347` (frame 198)
- pcap parent response: `09:33:55.441` (frame 199)
- pcap child id request: `09:33:56.100` (frame 201)
- pcap child id response: `09:33:56.114` (frame 203)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-093416-run11.log`

- manifest status: `completed`
- child extaddr: `42f8bff4996572c4`

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
- parent extaddr: `ca3982126335bf0f`
- parent rloc16: `n/a`
- child extaddr: `42f8bff4996572c4`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **87.059 ms**
- Response -> Child ID Request: **662.745 ms**
- Child ID Request -> Response: **13.306 ms**
- Full Attach: **763.11 ms**
- pcap parent request: `09:37:26.835` (frame 55)
- pcap parent response: `09:37:26.922` (frame 56)
- pcap child id request: `09:37:27.585` (frame 60)
- pcap child id response: `09:37:27.598` (frame 62)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `9e1093ba95f2375e`
- parent rloc16: `n/a`
- child extaddr: `42f8bff4996572c4`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **290.887 ms**
- Response -> Child ID Request: **461.121 ms**
- Child ID Request -> Response: **13.905 ms**
- Full Attach: **765.913 ms**
- pcap parent request: `09:41:26.893` (frame 202)
- pcap parent response: `09:41:27.184` (frame 203)
- pcap child id request: `09:41:27.645` (frame 205)
- pcap child id response: `09:41:27.659` (frame 207)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-094149-run12.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `3a20582a19780f28`

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
- parent extaddr: `4ad4673bfda72d73`
- parent rloc16: `n/a`
- child extaddr: `3a20582a19780f28`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **187.251 ms**
- Response -> Child ID Request: **563.715 ms**
- Child ID Request -> Response: **13.322 ms**
- Full Attach: **764.288 ms**
- pcap parent request: `09:44:59.577` (frame 51)
- pcap parent response: `09:44:59.764` (frame 52)
- pcap child id request: `09:45:00.328` (frame 56)
- pcap child id response: `09:45:00.341` (frame 58)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `bec81d55e50f6e1d`
- parent rloc16: `n/a`
- child extaddr: `3a20582a19780f28`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **348.425 ms**
- Response -> Child ID Request: **404.307 ms**
- Child ID Request -> Response: **14.725 ms**
- Full Attach: **767.457 ms**
- pcap parent request: `09:49:00.178` (frame 209)
- pcap parent response: `09:49:00.527` (frame 210)
- pcap child id request: `09:49:00.931` (frame 212)
- pcap child id response: `09:49:00.946` (frame 214)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-094921-run13.log`

- manifest status: `completed`
- child extaddr: `52e5d3041ca2d818`

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
- parent extaddr: `c21c07691110554d`
- parent rloc16: `n/a`
- child extaddr: `52e5d3041ca2d818`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **44.828 ms**
- Response -> Child ID Request: **705.121 ms**
- Child ID Request -> Response: **15.917 ms**
- Full Attach: **765.866 ms**
- pcap parent request: `09:52:32.321` (frame 51)
- pcap parent response: `09:52:32.366` (frame 52)
- pcap child id request: `09:52:33.071` (frame 56)
- pcap child id response: `09:52:33.087` (frame 58)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `ce665916ed6d9449`
- parent rloc16: `n/a`
- child extaddr: `52e5d3041ca2d818`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **379.352 ms**
- Response -> Child ID Request: **371.667 ms**
- Child ID Request -> Response: **14.352 ms**
- Full Attach: **765.371 ms**
- pcap parent request: `09:56:32.434` (frame 197)
- pcap parent response: `09:56:32.813` (frame 198)
- pcap child id request: `09:56:33.185` (frame 200)
- pcap child id response: `09:56:33.199` (frame 202)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-095654-run14.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `66c7b8323730e332`

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
- parent extaddr: `8efbaab692a79c8d`
- parent rloc16: `n/a`
- child extaddr: `66c7b8323730e332`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **262.298 ms**
- Response -> Child ID Request: **489.701 ms**
- Child ID Request -> Response: **15.321 ms**
- Full Attach: **767.32 ms**
- pcap parent request: `10:00:05.419` (frame 49)
- pcap parent response: `10:00:05.682` (frame 50)
- pcap child id request: `10:00:06.171` (frame 54)
- pcap child id response: `10:00:06.187` (frame 56)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `c288479962f69c59`
- parent rloc16: `n/a`
- child extaddr: `66c7b8323730e332`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **328.894 ms**
- Response -> Child ID Request: **423.111 ms**
- Child ID Request -> Response: **13.153 ms**
- Full Attach: **765.158 ms**
- pcap parent request: `10:04:05.977` (frame 208)
- pcap parent response: `10:04:06.306` (frame 209)
- pcap child id request: `10:04:06.729` (frame 211)
- pcap child id response: `10:04:06.743` (frame 213)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-100427-run15.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `2e4a68f954b88ea9`

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
- parent extaddr: `828c9dcb2a0d6ef7`
- parent rloc16: `n/a`
- child extaddr: `2e4a68f954b88ea9`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **43.284 ms**
- Response -> Child ID Request: **708.705 ms**
- Child ID Request -> Response: **12.538 ms**
- Full Attach: **764.527 ms**
- pcap parent request: `10:07:38.074` (frame 54)
- pcap parent response: `10:07:38.117` (frame 55)
- pcap child id request: `10:07:38.826` (frame 59)
- pcap child id response: `10:07:38.838` (frame 61)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `a294ed7f6a657f5f`
- parent rloc16: `n/a`
- child extaddr: `2e4a68f954b88ea9`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **112.028 ms**
- Response -> Child ID Request: **641.7 ms**
- Child ID Request -> Response: **12.942 ms**
- Full Attach: **766.67 ms**
- pcap parent request: `10:11:38.019` (frame 212)
- pcap parent response: `10:11:38.131` (frame 213)
- pcap child id request: `10:11:38.773` (frame 215)
- pcap child id response: `10:11:38.786` (frame 217)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-101159-run16.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `a2096d034740e507`

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
- parent extaddr: `f6bedfbf7d326811`
- parent rloc16: `n/a`
- child extaddr: `a2096d034740e507`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **52.282 ms**
- Response -> Child ID Request: **700.698 ms**
- Child ID Request -> Response: **12.535 ms**
- Full Attach: **765.515 ms**
- pcap parent request: `10:15:10.299` (frame 54)
- pcap parent response: `10:15:10.351` (frame 55)
- pcap child id request: `10:15:11.052` (frame 60)
- pcap child id response: `10:15:11.064` (frame 62)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `3e55f855dcc9c98a`
- parent rloc16: `n/a`
- child extaddr: `a2096d034740e507`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **499.922 ms**
- Response -> Child ID Request: **252.092 ms**
- Child ID Request -> Response: **14.162 ms**
- Full Attach: **766.176 ms**
- pcap parent request: `10:19:10.653` (frame 213)
- pcap parent response: `10:19:11.152` (frame 214)
- pcap child id request: `10:19:11.405` (frame 216)
- pcap child id response: `10:19:11.419` (frame 218)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-101932-run17.log`

- manifest status: `completed`
- child extaddr: `96619537c98ae6a9`

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
- parent extaddr: `b6eb1cd70633a850`
- parent rloc16: `n/a`
- child extaddr: `96619537c98ae6a9`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **214.905 ms**
- Response -> Child ID Request: **536.101 ms**
- Child ID Request -> Response: **14.929 ms**
- Full Attach: **765.935 ms**
- pcap parent request: `10:22:42.971` (frame 52)
- pcap parent response: `10:22:43.186` (frame 53)
- pcap child id request: `10:22:43.722` (frame 57)
- pcap child id response: `10:22:43.737` (frame 59)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `aa4753ea7c7901fe`
- parent rloc16: `n/a`
- child extaddr: `96619537c98ae6a9`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **332.263 ms**
- Response -> Child ID Request: **418.754 ms**
- Child ID Request -> Response: **14.269 ms**
- Full Attach: **765.286 ms**
- pcap parent request: `10:26:43.489` (frame 198)
- pcap parent response: `10:26:43.821` (frame 199)
- pcap child id request: `10:26:44.240` (frame 201)
- pcap child id response: `10:26:44.254` (frame 203)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-102705-run18.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `d2dc9803e699ec81`

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
- parent extaddr: `828bfc78568370de`
- parent rloc16: `n/a`
- child extaddr: `d2dc9803e699ec81`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **229.266 ms**
- Response -> Child ID Request: **522.737 ms**
- Child ID Request -> Response: **14.601 ms**
- Full Attach: **766.604 ms**
- pcap parent request: `10:30:15.824` (frame 53)
- pcap parent response: `10:30:16.053` (frame 54)
- pcap child id request: `10:30:16.576` (frame 58)
- pcap child id response: `10:30:16.591` (frame 60)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `229e0af3a2a399d0`
- parent rloc16: `n/a`
- child extaddr: `d2dc9803e699ec81`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **66.854 ms**
- Response -> Child ID Request: **685.276 ms**
- Child ID Request -> Response: **13.153 ms**
- Full Attach: **765.283 ms**
- pcap parent request: `10:34:16.103` (frame 212)
- pcap parent response: `10:34:16.170` (frame 213)
- pcap child id request: `10:34:16.855` (frame 215)
- pcap child id response: `10:34:16.869` (frame 217)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-103438-run19.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `6eafe020acc797e5`

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
- parent extaddr: `6e94be3167ef9bb3`
- parent rloc16: `n/a`
- child extaddr: `6eafe020acc797e5`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **95.541 ms**
- Response -> Child ID Request: **658.598 ms**
- Child ID Request -> Response: **13.449 ms**
- Full Attach: **767.588 ms**
- pcap parent request: `10:37:48.919` (frame 50)
- pcap parent response: `10:37:49.015` (frame 51)
- pcap child id request: `10:37:49.673` (frame 55)
- pcap child id response: `10:37:49.687` (frame 57)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `1e98ce5e88f26975`
- parent rloc16: `n/a`
- child extaddr: `6eafe020acc797e5`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **295.851 ms**
- Response -> Child ID Request: **455.167 ms**
- Child ID Request -> Response: **13.099 ms**
- Full Attach: **764.117 ms**
- pcap parent request: `10:41:49.481` (frame 209)
- pcap parent response: `10:41:49.777` (frame 210)
- pcap child id request: `10:41:50.232` (frame 212)
- pcap child id response: `10:41:50.246` (frame 214)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-104210-run20.log`

- manifest status: `completed`
- child extaddr: `3e9c6caf25615de2`

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
- parent extaddr: `e6464cfe2cd4cdc8`
- parent rloc16: `n/a`
- child extaddr: `3e9c6caf25615de2`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **280.226 ms**
- Response -> Child ID Request: **471.845 ms**
- Child ID Request -> Response: **14.186 ms**
- Full Attach: **766.257 ms**
- pcap parent request: `10:45:21.161` (frame 48)
- pcap parent response: `10:45:21.441` (frame 49)
- pcap child id request: `10:45:21.913` (frame 53)
- pcap child id response: `10:45:21.927` (frame 55)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `6a6133aa7e7cfcb3`
- parent rloc16: `n/a`
- child extaddr: `3e9c6caf25615de2`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **445.792 ms**
- Response -> Child ID Request: **307.967 ms**
- Child ID Request -> Response: **14.054 ms**
- Full Attach: **767.813 ms**
- pcap parent request: `10:49:21.771` (frame 195)
- pcap parent response: `10:49:22.217` (frame 196)
- pcap child id request: `10:49:22.525` (frame 198)
- pcap child id response: `10:49:22.539` (frame 200)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-104943-run21.log`

- manifest status: `completed`
- child extaddr: `0e7bcfe9d8211d1b`

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
- parent extaddr: `ea1ac5526926758e`
- parent rloc16: `n/a`
- child extaddr: `0e7bcfe9d8211d1b`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **313.431 ms**
- Response -> Child ID Request: **435.561 ms**
- Child ID Request -> Response: **13.009 ms**
- Full Attach: **762.001 ms**
- pcap parent request: `10:52:54.092` (frame 52)
- pcap parent response: `10:52:54.406` (frame 53)
- pcap child id request: `10:52:54.841` (frame 57)
- pcap child id response: `10:52:54.854` (frame 59)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `dade0fe37aee068f`
- parent rloc16: `n/a`
- child extaddr: `0e7bcfe9d8211d1b`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **404.526 ms**
- Response -> Child ID Request: **345.485 ms**
- Child ID Request -> Response: **14.55 ms**
- Full Attach: **764.561 ms**
- pcap parent request: `10:56:54.252` (frame 199)
- pcap parent response: `10:56:54.657` (frame 200)
- pcap child id request: `10:56:55.002` (frame 202)
- pcap child id response: `10:56:55.017` (frame 204)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-105716-run22.log`

- manifest status: `completed`
- child extaddr: `f67ce5163923d352`

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
- parent extaddr: `c6e53bdf34d39a71`
- parent rloc16: `n/a`
- child extaddr: `f67ce5163923d352`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **92.677 ms**
- Response -> Child ID Request: **661.31 ms**
- Child ID Request -> Response: **14.74 ms**
- Full Attach: **768.727 ms**
- pcap parent request: `11:00:26.581` (frame 55)
- pcap parent response: `11:00:26.673` (frame 56)
- pcap child id request: `11:00:27.335` (frame 60)
- pcap child id response: `11:00:27.349` (frame 62)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `c2c7f26aa3a05249`
- parent rloc16: `n/a`
- child extaddr: `f67ce5163923d352`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **31.869 ms**
- Response -> Child ID Request: **720.892 ms**
- Child ID Request -> Response: **13.137 ms**
- Full Attach: **765.898 ms**
- pcap parent request: `11:04:26.843` (frame 200)
- pcap parent response: `11:04:26.875` (frame 201)
- pcap child id request: `11:04:27.596` (frame 203)
- pcap child id response: `11:04:27.609` (frame 205)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-110448-run23.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `469265df9a1d7489`

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
- parent extaddr: `023b8d04a3234410`
- parent rloc16: `n/a`
- child extaddr: `469265df9a1d7489`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **117.961 ms**
- Response -> Child ID Request: **633.035 ms**
- Child ID Request -> Response: **12.634 ms**
- Full Attach: **763.63 ms**
- pcap parent request: `11:07:59.936` (frame 52)
- pcap parent response: `11:08:00.054` (frame 53)
- pcap child id request: `11:08:00.687` (frame 58)
- pcap child id response: `11:08:00.700` (frame 60)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `ee33d57d4e383d7a`
- parent rloc16: `n/a`
- child extaddr: `469265df9a1d7489`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **291.903 ms**
- Response -> Child ID Request: **461.102 ms**
- Child ID Request -> Response: **13.942 ms**
- Full Attach: **766.947 ms**
- pcap parent request: `11:12:00.491` (frame 213)
- pcap parent response: `11:12:00.783` (frame 214)
- pcap child id request: `11:12:01.244` (frame 216)
- pcap child id response: `11:12:01.258` (frame 218)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-111221-run24.log`

- manifest status: `completed`
- child extaddr: `d60827e2087160b4`

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
- parent extaddr: `067a38205f74fbfb`
- parent rloc16: `n/a`
- child extaddr: `d60827e2087160b4`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **260.05 ms**
- Response -> Child ID Request: **488.947 ms**
- Child ID Request -> Response: **14.365 ms**
- Full Attach: **763.362 ms**
- pcap parent request: `11:15:32.569` (frame 56)
- pcap parent response: `11:15:32.829` (frame 57)
- pcap child id request: `11:15:33.318` (frame 61)
- pcap child id response: `11:15:33.332` (frame 63)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `f6b8a49b6b274b96`
- parent rloc16: `n/a`
- child extaddr: `d60827e2087160b4`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **31.897 ms**
- Response -> Child ID Request: **717.472 ms**
- Child ID Request -> Response: **14.573 ms**
- Full Attach: **763.942 ms**
- pcap parent request: `11:19:32.559` (frame 201)
- pcap parent response: `11:19:32.591` (frame 202)
- pcap child id request: `11:19:33.308` (frame 204)
- pcap child id response: `11:19:33.323` (frame 206)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-111954-run25.log`

- manifest status: `completed`
- child extaddr: `92b25a23f63b692e`

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
- parent extaddr: `bea0663cf12015f2`
- parent rloc16: `n/a`
- child extaddr: `92b25a23f63b692e`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **41.377 ms**
- Response -> Child ID Request: **712.633 ms**
- Child ID Request -> Response: **14.415 ms**
- Full Attach: **768.425 ms**
- pcap parent request: `11:23:04.743` (frame 51)
- pcap parent response: `11:23:04.784` (frame 52)
- pcap child id request: `11:23:05.497` (frame 56)
- pcap child id response: `11:23:05.511` (frame 58)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `ba04e79fdfdedde6`
- parent rloc16: `n/a`
- child extaddr: `92b25a23f63b692e`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **88.025 ms**
- Response -> Child ID Request: **662.161 ms**
- Child ID Request -> Response: **12.883 ms**
- Full Attach: **763.069 ms**
- pcap parent request: `11:27:05.416` (frame 199)
- pcap parent response: `11:27:05.504` (frame 200)
- pcap child id request: `11:27:06.166` (frame 203)
- pcap child id response: `11:27:06.179` (frame 205)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-112727-run26.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `4ab31ebbf3abafc6`

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
- parent extaddr: `a2d748c1d049ca03`
- parent rloc16: `n/a`
- child extaddr: `4ab31ebbf3abafc6`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **91.82 ms**
- Response -> Child ID Request: **658.044 ms**
- Child ID Request -> Response: **14.0 ms**
- Full Attach: **763.864 ms**
- pcap parent request: `11:30:38.011` (frame 55)
- pcap parent response: `11:30:38.103` (frame 56)
- pcap child id request: `11:30:38.761` (frame 60)
- pcap child id response: `11:30:38.775` (frame 62)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `aa40b163da8a01e8`
- parent rloc16: `n/a`
- child extaddr: `4ab31ebbf3abafc6`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **182.015 ms**
- Response -> Child ID Request: **570.739 ms**
- Child ID Request -> Response: **12.511 ms**
- Full Attach: **765.265 ms**
- pcap parent request: `11:34:38.240` (frame 214)
- pcap parent response: `11:34:38.422` (frame 215)
- pcap child id request: `11:34:38.992` (frame 217)
- pcap child id response: `11:34:39.005` (frame 219)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-113459-run27.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `f62b0def64c0f593`

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
- parent extaddr: `9ec734befaa460f9`
- parent rloc16: `n/a`
- child extaddr: `f62b0def64c0f593`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **138.383 ms**
- Response -> Child ID Request: **611.63 ms**
- Child ID Request -> Response: **13.416 ms**
- Full Attach: **763.429 ms**
- pcap parent request: `11:38:10.446` (frame 55)
- pcap parent response: `11:38:10.584` (frame 56)
- pcap child id request: `11:38:11.196` (frame 60)
- pcap child id response: `11:38:11.209` (frame 62)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `6a783a5cbcca4445`
- parent rloc16: `n/a`
- child extaddr: `f62b0def64c0f593`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **172.891 ms**
- Response -> Child ID Request: **580.902 ms**
- Child ID Request -> Response: **14.144 ms**
- Full Attach: **767.937 ms**
- pcap parent request: `11:42:10.439` (frame 214)
- pcap parent response: `11:42:10.612` (frame 215)
- pcap child id request: `11:42:11.193` (frame 217)
- pcap child id response: `11:42:11.207` (frame 219)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-114232-run28.log`

- manifest status: `completed`
- child extaddr: `821b40adea8dea1c`

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
- parent extaddr: `960c26df399eab23`
- parent rloc16: `n/a`
- child extaddr: `821b40adea8dea1c`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **40.729 ms**
- Response -> Child ID Request: **711.261 ms**
- Child ID Request -> Response: **15.776 ms**
- Full Attach: **767.766 ms**
- pcap parent request: `11:45:42.833` (frame 47)
- pcap parent response: `11:45:42.874` (frame 48)
- pcap child id request: `11:45:43.585` (frame 52)
- pcap child id response: `11:45:43.601` (frame 54)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `5a5f20b11f165cc4`
- parent rloc16: `n/a`
- child extaddr: `821b40adea8dea1c`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **423.109 ms**
- Response -> Child ID Request: **329.002 ms**
- Child ID Request -> Response: **14.018 ms**
- Full Attach: **766.129 ms**
- pcap parent request: `11:49:42.787` (frame 194)
- pcap parent response: `11:49:43.210` (frame 195)
- pcap child id request: `11:49:43.539` (frame 197)
- pcap child id response: `11:49:43.553` (frame 199)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-115004-run29.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `6aba127ff7cc10ac`

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
- parent extaddr: `ba81cee282493629`
- parent rloc16: `n/a`
- child extaddr: `6aba127ff7cc10ac`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **345.905 ms**
- Response -> Child ID Request: **406.145 ms**
- Child ID Request -> Response: **13.885 ms**
- Full Attach: **765.935 ms**
- pcap parent request: `11:53:15.594` (frame 49)
- pcap parent response: `11:53:15.940` (frame 50)
- pcap child id request: `11:53:16.346` (frame 54)
- pcap child id response: `11:53:16.360` (frame 56)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `52b8751f37fd0185`
- parent rloc16: `n/a`
- child extaddr: `6aba127ff7cc10ac`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **210.495 ms**
- Response -> Child ID Request: **540.664 ms**
- Child ID Request -> Response: **12.583 ms**
- Full Attach: **763.742 ms**
- pcap parent request: `11:57:15.651` (frame 207)
- pcap parent response: `11:57:15.862` (frame 208)
- pcap child id request: `11:57:16.402` (frame 210)
- pcap child id response: `11:57:16.415` (frame 212)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-115737-run30.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `3e74d35ee8ad1c64`

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
- parent extaddr: `666880cd70f1a6c1`
- parent rloc16: `n/a`
- child extaddr: `3e74d35ee8ad1c64`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **225.299 ms**
- Response -> Child ID Request: **527.783 ms**
- Child ID Request -> Response: **13.569 ms**
- Full Attach: **766.651 ms**
- pcap parent request: `12:00:48.263` (frame 56)
- pcap parent response: `12:00:48.489` (frame 57)
- pcap child id request: `12:00:49.016` (frame 61)
- pcap child id response: `12:00:49.030` (frame 63)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `c2dd113bf7afb4e6`
- parent rloc16: `n/a`
- child extaddr: `3e74d35ee8ad1c64`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **204.159 ms**
- Response -> Child ID Request: **547.842 ms**
- Child ID Request -> Response: **12.44 ms**
- Full Attach: **764.441 ms**
- pcap parent request: `12:04:48.636` (frame 215)
- pcap parent response: `12:04:48.840` (frame 216)
- pcap child id request: `12:04:49.388` (frame 218)
- pcap child id response: `12:04:49.401` (frame 220)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-120510-run31.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `9ace34a9bd265503`

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
- parent extaddr: `4e9adc8142dda1b4`
- parent rloc16: `n/a`
- child extaddr: `9ace34a9bd265503`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **249.188 ms**
- Response -> Child ID Request: **502.957 ms**
- Child ID Request -> Response: **14.088 ms**
- Full Attach: **766.233 ms**
- pcap parent request: `12:08:21.220` (frame 49)
- pcap parent response: `12:08:21.470` (frame 50)
- pcap child id request: `12:08:21.973` (frame 54)
- pcap child id response: `12:08:21.987` (frame 56)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `7ae11bf6c829b58e`
- parent rloc16: `n/a`
- child extaddr: `9ace34a9bd265503`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **348.241 ms**
- Response -> Child ID Request: **404.751 ms**
- Child ID Request -> Response: **12.474 ms**
- Full Attach: **765.466 ms**
- pcap parent request: `12:12:21.604` (frame 207)
- pcap parent response: `12:12:21.952` (frame 208)
- pcap child id request: `12:12:22.357` (frame 210)
- pcap child id response: `12:12:22.369` (frame 212)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-121243-run32.log`

- manifest status: `completed`
- child extaddr: `0afdd859a248e99a`

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
- parent extaddr: `6a27466ece2f4c02`
- parent rloc16: `n/a`
- child extaddr: `0afdd859a248e99a`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **40.425 ms**
- Response -> Child ID Request: **711.738 ms**
- Child ID Request -> Response: **12.899 ms**
- Full Attach: **765.062 ms**
- pcap parent request: `12:15:53.853` (frame 52)
- pcap parent response: `12:15:53.894` (frame 53)
- pcap child id request: `12:15:54.605` (frame 57)
- pcap child id response: `12:15:54.618` (frame 59)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `e28707a65156d69a`
- parent rloc16: `n/a`
- child extaddr: `0afdd859a248e99a`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **178.438 ms**
- Response -> Child ID Request: **573.314 ms**
- Child ID Request -> Response: **13.1 ms**
- Full Attach: **764.852 ms**
- pcap parent request: `12:19:54.393` (frame 197)
- pcap parent response: `12:19:54.571` (frame 198)
- pcap child id request: `12:19:55.144` (frame 200)
- pcap child id response: `12:19:55.157` (frame 202)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-122016-run33.log`

- manifest status: `completed`
- child extaddr: `f638be7f369e9492`

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
- parent extaddr: `46cde9ad482a3c69`
- parent rloc16: `n/a`
- child extaddr: `f638be7f369e9492`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **115.919 ms**
- Response -> Child ID Request: **637.081 ms**
- Child ID Request -> Response: **12.444 ms**
- Full Attach: **765.444 ms**
- pcap parent request: `12:23:27.009` (frame 52)
- pcap parent response: `12:23:27.125` (frame 53)
- pcap child id request: `12:23:27.762` (frame 57)
- pcap child id response: `12:23:27.774` (frame 59)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `3ea94326c9546212`
- parent rloc16: `n/a`
- child extaddr: `f638be7f369e9492`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **98.332 ms**
- Response -> Child ID Request: **652.823 ms**
- Child ID Request -> Response: **15.21 ms**
- Full Attach: **766.365 ms**
- pcap parent request: `12:27:27.117` (frame 197)
- pcap parent response: `12:27:27.215` (frame 198)
- pcap child id request: `12:27:27.868` (frame 200)
- pcap child id response: `12:27:27.883` (frame 202)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-122748-run34.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `5a5745b3ce84f7f6`

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
- parent extaddr: `06fc346bb1b3fdd0`
- parent rloc16: `n/a`
- child extaddr: `5a5745b3ce84f7f6`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **160.257 ms**
- Response -> Child ID Request: **592.72 ms**
- Child ID Request -> Response: **15.32 ms**
- Full Attach: **768.297 ms**
- pcap parent request: `12:30:59.356` (frame 52)
- pcap parent response: `12:30:59.517` (frame 53)
- pcap child id request: `12:31:00.109` (frame 58)
- pcap child id response: `12:31:00.125` (frame 60)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `06fa09c3024576da`
- parent rloc16: `n/a`
- child extaddr: `5a5745b3ce84f7f6`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **253.566 ms**
- Response -> Child ID Request: **497.446 ms**
- Child ID Request -> Response: **13.179 ms**
- Full Attach: **764.191 ms**
- pcap parent request: `12:34:59.502` (frame 210)
- pcap parent response: `12:34:59.756` (frame 211)
- pcap child id request: `12:35:00.253` (frame 213)
- pcap child id response: `12:35:00.266` (frame 215)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-123521-run35.log`

- manifest status: `completed`
- child extaddr: `3a23f3d3b7dcd38d`

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
- parent extaddr: `066e854b4a9322c5`
- parent rloc16: `n/a`
- child extaddr: `3a23f3d3b7dcd38d`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **54.075 ms**
- Response -> Child ID Request: **697.915 ms**
- Child ID Request -> Response: **15.135 ms**
- Full Attach: **767.125 ms**
- pcap parent request: `12:38:31.969` (frame 54)
- pcap parent response: `12:38:32.023` (frame 55)
- pcap child id request: `12:38:32.721` (frame 59)
- pcap child id response: `12:38:32.736` (frame 61)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `1ec6fad79927f5a1`
- parent rloc16: `n/a`
- child extaddr: `3a23f3d3b7dcd38d`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **355.98 ms**
- Response -> Child ID Request: **397.822 ms**
- Child ID Request -> Response: **14.204 ms**
- Full Attach: **768.006 ms**
- pcap parent request: `12:42:32.207` (frame 200)
- pcap parent response: `12:42:32.563` (frame 201)
- pcap child id request: `12:42:32.961` (frame 203)
- pcap child id response: `12:42:32.975` (frame 205)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-124254-run36.log`

- manifest status: `completed`
- child extaddr: `3613e1de2872270b`

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
- parent extaddr: `0e97aded1f838f9c`
- parent rloc16: `n/a`
- child extaddr: `3613e1de2872270b`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **10.583 ms**
- Response -> Child ID Request: **739.269 ms**
- Child ID Request -> Response: **13.104 ms**
- Full Attach: **762.956 ms**
- pcap parent request: `12:46:04.915` (frame 51)
- pcap parent response: `12:46:04.925` (frame 52)
- pcap child id request: `12:46:05.665` (frame 56)
- pcap child id response: `12:46:05.678` (frame 58)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `d6c02ad4b232aa30`
- parent rloc16: `n/a`
- child extaddr: `3613e1de2872270b`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **312.728 ms**
- Response -> Child ID Request: **437.285 ms**
- Child ID Request -> Response: **14.749 ms**
- Full Attach: **764.762 ms**
- pcap parent request: `12:50:05.344` (frame 197)
- pcap parent response: `12:50:05.656` (frame 198)
- pcap child id request: `12:50:06.094` (frame 200)
- pcap child id response: `12:50:06.108` (frame 202)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-125026-run37.log`

- manifest status: `completed`
- child extaddr: `7ed8efca8d641146`

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
- parent extaddr: `868b65f551eadb91`
- parent rloc16: `n/a`
- child extaddr: `7ed8efca8d641146`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **118.835 ms**
- Response -> Child ID Request: **633.152 ms**
- Child ID Request -> Response: **13.256 ms**
- Full Attach: **765.243 ms**
- pcap parent request: `12:53:37.184` (frame 49)
- pcap parent response: `12:53:37.303` (frame 50)
- pcap child id request: `12:53:37.936` (frame 54)
- pcap child id response: `12:53:37.949` (frame 56)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `b25d636cf7903c67`
- parent rloc16: `n/a`
- child extaddr: `7ed8efca8d641146`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **450.114 ms**
- Response -> Child ID Request: **300.037 ms**
- Child ID Request -> Response: **12.971 ms**
- Full Attach: **763.122 ms**
- pcap parent request: `12:57:37.133` (frame 196)
- pcap parent response: `12:57:37.583` (frame 197)
- pcap child id request: `12:57:37.883` (frame 199)
- pcap child id response: `12:57:37.896` (frame 201)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-125759-run38.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `7abd93219541a27e`

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
- parent extaddr: `22d83a692cc2e79d`
- parent rloc16: `n/a`
- child extaddr: `7abd93219541a27e`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **36.413 ms**
- Response -> Child ID Request: **715.587 ms**
- Child ID Request -> Response: **12.671 ms**
- Full Attach: **764.671 ms**
- pcap parent request: `13:01:09.713` (frame 47)
- pcap parent response: `13:01:09.749` (frame 48)
- pcap child id request: `13:01:10.465` (frame 52)
- pcap child id response: `13:01:10.477` (frame 54)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `d65829a897472650`
- parent rloc16: `n/a`
- child extaddr: `7abd93219541a27e`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **416.077 ms**
- Response -> Child ID Request: **336.723 ms**
- Child ID Request -> Response: **14.301 ms**
- Full Attach: **767.101 ms**
- pcap parent request: `13:05:09.748` (frame 205)
- pcap parent response: `13:05:10.164` (frame 206)
- pcap child id request: `13:05:10.501` (frame 208)
- pcap child id response: `13:05:10.515` (frame 210)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-130531-run39.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `1612a1e91d729681`

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
- parent extaddr: `86dbe13d38e02919`
- parent rloc16: `n/a`
- child extaddr: `1612a1e91d729681`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **310.246 ms**
- Response -> Child ID Request: **439.673 ms**
- Child ID Request -> Response: **12.572 ms**
- Full Attach: **762.491 ms**
- pcap parent request: `13:08:42.408` (frame 51)
- pcap parent response: `13:08:42.718` (frame 52)
- pcap child id request: `13:08:43.158` (frame 56)
- pcap child id response: `13:08:43.170` (frame 58)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `82de08f88f074bbe`
- parent rloc16: `n/a`
- child extaddr: `1612a1e91d729681`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **406.738 ms**
- Response -> Child ID Request: **347.056 ms**
- Child ID Request -> Response: **13.963 ms**
- Full Attach: **767.757 ms**
- pcap parent request: `13:12:42.609` (frame 209)
- pcap parent response: `13:12:43.016` (frame 210)
- pcap child id request: `13:12:43.363` (frame 212)
- pcap child id response: `13:12:43.377` (frame 214)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-131304-run40.log`

- manifest status: `completed`
- child extaddr: `86e332efc6ca4cf1`

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
- parent extaddr: `1e6a30e9de0f9f88`
- parent rloc16: `n/a`
- child extaddr: `86e332efc6ca4cf1`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **180.392 ms**
- Response -> Child ID Request: **571.613 ms**
- Child ID Request -> Response: **13.424 ms**
- Full Attach: **765.429 ms**
- pcap parent request: `13:16:15.415` (frame 51)
- pcap parent response: `13:16:15.596` (frame 52)
- pcap child id request: `13:16:16.167` (frame 56)
- pcap child id response: `13:16:16.181` (frame 58)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `5ec0e21ec88af049`
- parent rloc16: `n/a`
- child extaddr: `86e332efc6ca4cf1`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **216.828 ms**
- Response -> Child ID Request: **532.421 ms**
- Child ID Request -> Response: **13.599 ms**
- Full Attach: **762.848 ms**
- pcap parent request: `13:20:16.004` (frame 197)
- pcap parent response: `13:20:16.221` (frame 198)
- pcap child id request: `13:20:16.754` (frame 200)
- pcap child id response: `13:20:16.767` (frame 202)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-132037-run41.log`

- manifest status: `completed`
- child extaddr: `ea52b5f93f53a802`

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
- parent extaddr: `e2b2f36381deae02`
- parent rloc16: `n/a`
- child extaddr: `ea52b5f93f53a802`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **395.021 ms**
- Response -> Child ID Request: **354.997 ms**
- Child ID Request -> Response: **14.032 ms**
- Full Attach: **764.05 ms**
- pcap parent request: `13:23:48.015` (frame 55)
- pcap parent response: `13:23:48.410` (frame 56)
- pcap child id request: `13:23:48.765` (frame 60)
- pcap child id response: `13:23:48.779` (frame 62)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `5a8c1889e149ea92`
- parent rloc16: `n/a`
- child extaddr: `ea52b5f93f53a802`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **427.079 ms**
- Response -> Child ID Request: **323.944 ms**
- Child ID Request -> Response: **15.42 ms**
- Full Attach: **766.443 ms**
- pcap parent request: `13:27:48.130` (frame 200)
- pcap parent response: `13:27:48.557` (frame 201)
- pcap child id request: `13:27:48.881` (frame 203)
- pcap child id response: `13:27:48.896` (frame 205)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-132809-run42.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `12701345e2582434`

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
- parent extaddr: `9a2ac71f0a1ffc03`
- parent rloc16: `n/a`
- child extaddr: `12701345e2582434`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **409.727 ms**
- Response -> Child ID Request: **340.276 ms**
- Child ID Request -> Response: **13.755 ms**
- Full Attach: **763.758 ms**
- pcap parent request: `13:31:20.644` (frame 54)
- pcap parent response: `13:31:21.053` (frame 55)
- pcap child id request: `13:31:21.394` (frame 59)
- pcap child id response: `13:31:21.408` (frame 61)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `ee3486abf0dc6901`
- parent rloc16: `n/a`
- child extaddr: `12701345e2582434`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **377.27 ms**
- Response -> Child ID Request: **374.088 ms**
- Child ID Request -> Response: **14.958 ms**
- Full Attach: **766.316 ms**
- pcap parent request: `13:35:20.636` (frame 213)
- pcap parent response: `13:35:21.013` (frame 214)
- pcap child id request: `13:35:21.387` (frame 216)
- pcap child id response: `13:35:21.402` (frame 218)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-133542-run43.log`

- manifest status: `completed`
- child extaddr: `c2bfa67872c0ee5f`

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
- parent extaddr: `e69108784f14a5b6`
- parent rloc16: `n/a`
- child extaddr: `c2bfa67872c0ee5f`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **353.442 ms**
- Response -> Child ID Request: **396.548 ms**
- Child ID Request -> Response: **14.801 ms**
- Full Attach: **764.791 ms**
- pcap parent request: `13:38:53.339` (frame 50)
- pcap parent response: `13:38:53.693` (frame 51)
- pcap child id request: `13:38:54.089` (frame 55)
- pcap child id response: `13:38:54.104` (frame 57)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `563b3d973f400465`
- parent rloc16: `n/a`
- child extaddr: `c2bfa67872c0ee5f`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **440.441 ms**
- Response -> Child ID Request: **309.579 ms**
- Child ID Request -> Response: **13.435 ms**
- Full Attach: **763.455 ms**
- pcap parent request: `13:42:53.387` (frame 197)
- pcap parent response: `13:42:53.828` (frame 198)
- pcap child id request: `13:42:54.137` (frame 200)
- pcap child id response: `13:42:54.151` (frame 202)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-134315-run44.log`

- manifest status: `completed`
- child extaddr: `764eae5502c3d1a9`

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
- parent extaddr: `de7470f13533a8b2`
- parent rloc16: `n/a`
- child extaddr: `764eae5502c3d1a9`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **174.28 ms**
- Response -> Child ID Request: **578.721 ms**
- Child ID Request -> Response: **14.322 ms**
- Full Attach: **767.323 ms**
- pcap parent request: `13:46:26.204` (frame 50)
- pcap parent response: `13:46:26.378` (frame 51)
- pcap child id request: `13:46:26.957` (frame 55)
- pcap child id response: `13:46:26.971` (frame 57)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `2a95181f9b95c959`
- parent rloc16: `n/a`
- child extaddr: `764eae5502c3d1a9`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **191.901 ms**
- Response -> Child ID Request: **559.118 ms**
- Child ID Request -> Response: **13.928 ms**
- Full Attach: **764.947 ms**
- pcap parent request: `13:50:26.546` (frame 198)
- pcap parent response: `13:50:26.738` (frame 199)
- pcap child id request: `13:50:27.297` (frame 201)
- pcap child id response: `13:50:27.311` (frame 203)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-135047-run45.log`

- manifest status: `completed`
- child extaddr: `ea7dd969b906f44b`

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
- parent extaddr: `cab53f9ba63c1b9a`
- parent rloc16: `n/a`
- child extaddr: `ea7dd969b906f44b`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **82.393 ms**
- Response -> Child ID Request: **667.622 ms**
- Child ID Request -> Response: **13.42 ms**
- Full Attach: **763.435 ms**
- pcap parent request: `13:53:58.626` (frame 53)
- pcap parent response: `13:53:58.708` (frame 54)
- pcap child id request: `13:53:59.376` (frame 58)
- pcap child id response: `13:53:59.389` (frame 60)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `6a061d8780d7dd64`
- parent rloc16: `n/a`
- child extaddr: `ea7dd969b906f44b`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **288.165 ms**
- Response -> Child ID Request: **462.854 ms**
- Child ID Request -> Response: **14.185 ms**
- Full Attach: **765.204 ms**
- pcap parent request: `13:57:58.670` (frame 198)
- pcap parent response: `13:57:58.958` (frame 199)
- pcap child id request: `13:57:59.421` (frame 202)
- pcap child id response: `13:57:59.435` (frame 204)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-135820-run46.log`

- manifest status: `completed`
- child extaddr: `3aa66cb2cd30e960`

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
- parent extaddr: `0e451cfc690468c8`
- parent rloc16: `n/a`
- child extaddr: `3aa66cb2cd30e960`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **399.599 ms**
- Response -> Child ID Request: **352.541 ms**
- Child ID Request -> Response: **14.49 ms**
- Full Attach: **766.63 ms**
- pcap parent request: `14:01:31.107` (frame 54)
- pcap parent response: `14:01:31.507` (frame 55)
- pcap child id request: `14:01:31.860` (frame 59)
- pcap child id response: `14:01:31.874` (frame 61)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `3a0fbb2e2b1967e9`
- parent rloc16: `n/a`
- child extaddr: `3aa66cb2cd30e960`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **121.862 ms**
- Response -> Child ID Request: **630.142 ms**
- Child ID Request -> Response: **14.284 ms**
- Full Attach: **766.288 ms**
- pcap parent request: `14:05:31.750` (frame 201)
- pcap parent response: `14:05:31.872` (frame 202)
- pcap child id request: `14:05:32.502` (frame 204)
- pcap child id response: `14:05:32.516` (frame 206)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-140553-run47.log`

- manifest status: `completed`
- child extaddr: `7e0f807597a36b08`

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
- parent extaddr: `1a55e7307d25dc11`
- parent rloc16: `n/a`
- child extaddr: `7e0f807597a36b08`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **138.764 ms**
- Response -> Child ID Request: **612.236 ms**
- Child ID Request -> Response: **14.805 ms**
- Full Attach: **765.805 ms**
- pcap parent request: `14:09:04.218` (frame 48)
- pcap parent response: `14:09:04.356` (frame 49)
- pcap child id request: `14:09:04.969` (frame 53)
- pcap child id response: `14:09:04.983` (frame 55)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `5e263c70c9561412`
- parent rloc16: `n/a`
- child extaddr: `7e0f807597a36b08`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **460.773 ms**
- Response -> Child ID Request: **290.405 ms**
- Child ID Request -> Response: **12.868 ms**
- Full Attach: **764.046 ms**
- pcap parent request: `14:13:04.213` (frame 195)
- pcap parent response: `14:13:04.674` (frame 196)
- pcap child id request: `14:13:04.965` (frame 198)
- pcap child id response: `14:13:04.978` (frame 200)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-141326-run48.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `e67e74b62143416b`

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
- parent extaddr: `42213f39bdaf45da`
- parent rloc16: `n/a`
- child extaddr: `e67e74b62143416b`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **184.942 ms**
- Response -> Child ID Request: **564.903 ms**
- Child ID Request -> Response: **15.128 ms**
- Full Attach: **764.973 ms**
- pcap parent request: `14:16:36.604` (frame 56)
- pcap parent response: `14:16:36.789` (frame 57)
- pcap child id request: `14:16:37.354` (frame 61)
- pcap child id response: `14:16:37.369` (frame 63)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `de4a96248a51760a`
- parent rloc16: `n/a`
- child extaddr: `e67e74b62143416b`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **174.324 ms**
- Response -> Child ID Request: **576.875 ms**
- Child ID Request -> Response: **13.534 ms**
- Full Attach: **764.733 ms**
- pcap parent request: `14:20:36.649` (frame 215)
- pcap parent response: `14:20:36.823` (frame 216)
- pcap child id request: `14:20:37.400` (frame 218)
- pcap child id response: `14:20:37.414` (frame 220)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-142058-run49.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `66724b6c7544134e`

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
- parent extaddr: `0a7cf49defddd8ca`
- parent rloc16: `n/a`
- child extaddr: `66724b6c7544134e`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **362.665 ms**
- Response -> Child ID Request: **390.325 ms**
- Child ID Request -> Response: **13.705 ms**
- Full Attach: **766.695 ms**
- pcap parent request: `14:24:09.215` (frame 54)
- pcap parent response: `14:24:09.577` (frame 55)
- pcap child id request: `14:24:09.967` (frame 59)
- pcap child id response: `14:24:09.981` (frame 61)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `be81ecd2419170b7`
- parent rloc16: `n/a`
- child extaddr: `66724b6c7544134e`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **114.632 ms**
- Response -> Child ID Request: **639.13 ms**
- Child ID Request -> Response: **14.914 ms**
- Full Attach: **768.676 ms**
- pcap parent request: `14:28:09.280` (frame 213)
- pcap parent response: `14:28:09.394` (frame 214)
- pcap child id request: `14:28:10.033` (frame 216)
- pcap child id response: `14:28:10.048` (frame 218)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-142831-run50.log`

- manifest status: `completed`
- child extaddr: `665e80a546073fa6`

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
- parent extaddr: `b2812c3a94f4a53d`
- parent rloc16: `n/a`
- child extaddr: `665e80a546073fa6`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **352.432 ms**
- Response -> Child ID Request: **397.589 ms**
- Child ID Request -> Response: **14.444 ms**
- Full Attach: **764.465 ms**
- pcap parent request: `14:31:42.414` (frame 54)
- pcap parent response: `14:31:42.767` (frame 55)
- pcap child id request: `14:31:43.164` (frame 59)
- pcap child id response: `14:31:43.179` (frame 61)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `b66809adfd5a31df`
- parent rloc16: `n/a`
- child extaddr: `665e80a546073fa6`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **114.482 ms**
- Response -> Child ID Request: **636.533 ms**
- Child ID Request -> Response: **14.493 ms**
- Full Attach: **765.508 ms**
- pcap parent request: `14:35:42.931` (frame 202)
- pcap parent response: `14:35:43.046` (frame 203)
- pcap child id request: `14:35:43.682` (frame 205)
- pcap child id response: `14:35:43.697` (frame 207)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**
