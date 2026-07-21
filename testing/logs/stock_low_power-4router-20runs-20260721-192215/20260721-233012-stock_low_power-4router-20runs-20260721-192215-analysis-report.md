# Child Log Analysis

## stock_child

Files analyzed: **20**

- batch folders: `stock_low_power-4router-20runs-20260721-192215`

### PCAP-complete child attach summary

| Attach | Metric | M (SD), ms | n |
| --- | --- | ---: | ---: |
| 1 | Request -> Response | 208.79 (132.64) | 20 |
| 1 | Response -> Child ID Request | 542.10 (132.58) | 20 |
| 1 | Child ID Request -> Response | 13.76 (0.82) | 20 |
| 1 | Full Attach | 764.64 (1.58) | 20 |
| 2 | Request -> Response | 256.33 (142.48) | 20 |
| 2 | Response -> Child ID Request | 495.40 (142.83) | 20 |
| 2 | Child ID Request -> Response | 13.80 (1.05) | 20 |
| 2 | Full Attach | 765.53 (1.67) | 20 |

| Metric | M (SD) | n |
| --- | ---: | ---: |
| Failed TX Attempts per Log | 0.00 (0.00) | 20 |
| Log-only or Partial Sequences per Log | 0.00 (0.00) | 20 |

### `stock_child_20260721-193023-run01.log`

- manifest status: `completed`
- child extaddr: `060c482b2df30358`

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
- parent extaddr: `b6a6a2dc0ddf4c87`
- parent rloc16: `n/a`
- child extaddr: `060c482b2df30358`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **138.44 ms**
- Response -> Child ID Request: **613.709 ms**
- Child ID Request -> Response: **14.341 ms**
- Full Attach: **766.49 ms**
- pcap parent request: `19:36:14.064` (frame 213)
- pcap parent response: `19:36:14.202` (frame 216)
- pcap child id request: `19:36:14.816` (frame 223)
- pcap child id response: `19:36:14.830` (frame 225)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `ce05933abfba543c`
- parent rloc16: `n/a`
- child extaddr: `060c482b2df30358`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **299.69 ms**
- Response -> Child ID Request: **451.306 ms**
- Child ID Request -> Response: **14.741 ms**
- Full Attach: **765.737 ms**
- pcap parent request: `19:40:14.430` (frame 499)
- pcap parent response: `19:40:14.729` (frame 500)
- pcap child id request: `19:40:15.181` (frame 506)
- pcap child id response: `19:40:15.195` (frame 508)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260721-194220-run02.log`

- manifest status: `completed`
- child extaddr: `b68c344b6865fdfa`

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
- parent extaddr: `aa0ca1e19f12aa33`
- parent rloc16: `n/a`
- child extaddr: `b68c344b6865fdfa`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **24.473 ms**
- Response -> Child ID Request: **725.33 ms**
- Child ID Request -> Response: **12.919 ms**
- Full Attach: **762.722 ms**
- pcap parent request: `19:48:11.353` (frame 301)
- pcap parent response: `19:48:11.377` (frame 302)
- pcap child id request: `19:48:12.103` (frame 312)
- pcap child id response: `19:48:12.115` (frame 314)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `76f79525bb4cf8de`
- parent rloc16: `n/a`
- child extaddr: `b68c344b6865fdfa`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **278.761 ms**
- Response -> Child ID Request: **474.23 ms**
- Child ID Request -> Response: **15.783 ms**
- Full Attach: **768.774 ms**
- pcap parent request: `19:52:11.677` (frame 585)
- pcap parent response: `19:52:11.955` (frame 589)
- pcap child id request: `19:52:12.430` (frame 593)
- pcap child id response: `19:52:12.445` (frame 595)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260721-195418-run03.log`

- manifest status: `completed`
- child extaddr: `9aa946c6fb90215a`

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
- parent extaddr: `aa318aff3c58ed2e`
- parent rloc16: `n/a`
- child extaddr: `9aa946c6fb90215a`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **173.19 ms**
- Response -> Child ID Request: **577.723 ms**
- Child ID Request -> Response: **14.315 ms**
- Full Attach: **765.228 ms**
- pcap parent request: `20:00:08.904` (frame 1074)
- pcap parent response: `20:00:09.077` (frame 1077)
- pcap child id request: `20:00:09.655` (frame 1083)
- pcap child id response: `20:00:09.669` (frame 1085)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `b676fd611d9a904b`
- parent rloc16: `n/a`
- child extaddr: `9aa946c6fb90215a`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **283.978 ms**
- Response -> Child ID Request: **467.029 ms**
- Child ID Request -> Response: **14.007 ms**
- Full Attach: **765.014 ms**
- pcap parent request: `20:04:09.053` (frame 1466)
- pcap parent response: `20:04:09.337` (frame 1469)
- pcap child id request: `20:04:09.804` (frame 1473)
- pcap child id response: `20:04:09.818` (frame 1475)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260721-200615-run04.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `527c64d0651efbe3`

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
- parent extaddr: `66314ede5fdb94e4`
- parent rloc16: `n/a`
- child extaddr: `527c64d0651efbe3`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **205.784 ms**
- Response -> Child ID Request: **545.214 ms**
- Child ID Request -> Response: **13.834 ms**
- Full Attach: **764.832 ms**
- pcap parent request: `20:12:05.949` (frame 198)
- pcap parent response: `20:12:06.155` (frame 199)
- pcap child id request: `20:12:06.700` (frame 208)
- pcap child id response: `20:12:06.714` (frame 210)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `5669348b0dc1ed58`
- parent rloc16: `n/a`
- child extaddr: `527c64d0651efbe3`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **203.385 ms**
- Response -> Child ID Request: **548.618 ms**
- Child ID Request -> Response: **15.826 ms**
- Full Attach: **767.829 ms**
- pcap parent request: `20:16:06.576` (frame 537)
- pcap parent response: `20:16:06.779` (frame 538)
- pcap child id request: `20:16:07.328` (frame 542)
- pcap child id response: `20:16:07.344` (frame 544)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260721-201813-run05.log`

- manifest status: `completed`
- child extaddr: `6670316c13cd0aea`

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
- parent extaddr: `aa2393075a79a847`
- parent rloc16: `n/a`
- child extaddr: `6670316c13cd0aea`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **321.407 ms**
- Response -> Child ID Request: **428.385 ms**
- Child ID Request -> Response: **15.976 ms**
- Full Attach: **765.768 ms**
- pcap parent request: `20:24:04.092` (frame 1168)
- pcap parent response: `20:24:04.413` (frame 1173)
- pcap child id request: `20:24:04.842` (frame 1177)
- pcap child id response: `20:24:04.858` (frame 1179)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `c6a254225fc575a2`
- parent rloc16: `n/a`
- child extaddr: `6670316c13cd0aea`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **100.371 ms**
- Response -> Child ID Request: **651.376 ms**
- Child ID Request -> Response: **12.237 ms**
- Full Attach: **763.984 ms**
- pcap parent request: `20:28:04.379` (frame 1494)
- pcap parent response: `20:28:04.479` (frame 1497)
- pcap child id request: `20:28:05.131` (frame 1501)
- pcap child id response: `20:28:05.143` (frame 1503)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260721-203010-run06.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `b6a3d18815169a16`

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
- parent extaddr: `523260037ebc3e8f`
- parent rloc16: `n/a`
- child extaddr: `b6a3d18815169a16`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **286.706 ms**
- Response -> Child ID Request: **463.309 ms**
- Child ID Request -> Response: **12.913 ms**
- Full Attach: **762.928 ms**
- pcap parent request: `20:36:01.192` (frame 197)
- pcap parent response: `20:36:01.478` (frame 202)
- pcap child id request: `20:36:01.942` (frame 206)
- pcap child id response: `20:36:01.954` (frame 208)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `66094a69712f892c`
- parent rloc16: `n/a`
- child extaddr: `b6a3d18815169a16`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **497.497 ms**
- Response -> Child ID Request: **252.731 ms**
- Child ID Request -> Response: **12.468 ms**
- Full Attach: **762.696 ms**
- pcap parent request: `20:40:01.725` (frame 552)
- pcap parent response: `20:40:02.223` (frame 557)
- pcap child id request: `20:40:02.476` (frame 559)
- pcap child id response: `20:40:02.488` (frame 561)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260721-204208-run07.log`

- manifest status: `completed`
- child extaddr: `02ea0c0d28bb3848`

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
- parent extaddr: `5a95ce9c8fd6533c`
- parent rloc16: `n/a`
- child extaddr: `02ea0c0d28bb3848`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **453.035 ms**
- Response -> Child ID Request: **298.969 ms**
- Child ID Request -> Response: **14.063 ms**
- Full Attach: **766.067 ms**
- pcap parent request: `20:47:58.727` (frame 1223)
- pcap parent response: `20:47:59.180` (frame 1230)
- pcap child id request: `20:47:59.479` (frame 1232)
- pcap child id response: `20:47:59.493` (frame 1234)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `128130128f1202c1`
- parent rloc16: `n/a`
- child extaddr: `02ea0c0d28bb3848`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **410.418 ms**
- Response -> Child ID Request: **342.588 ms**
- Child ID Request -> Response: **13.434 ms**
- Full Attach: **766.44 ms**
- pcap parent request: `20:51:58.955` (frame 1633)
- pcap parent response: `20:51:59.366` (frame 1638)
- pcap child id request: `20:51:59.708` (frame 1640)
- pcap child id response: `20:51:59.722` (frame 1642)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260721-205405-run08.log`

- manifest status: `completed`
- child extaddr: `56c68a9c858c9ddc`

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
- parent extaddr: `2ebd4b78e6e60e65`
- parent rloc16: `n/a`
- child extaddr: `56c68a9c858c9ddc`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **26.653 ms**
- Response -> Child ID Request: **725.456 ms**
- Child ID Request -> Response: **13.591 ms**
- Full Attach: **765.7 ms**
- pcap parent request: `20:59:56.710` (frame 195)
- pcap parent response: `20:59:56.737` (frame 196)
- pcap child id request: `20:59:57.462` (frame 204)
- pcap child id response: `20:59:57.476` (frame 206)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `dac862f1d2771bc2`
- parent rloc16: `n/a`
- child extaddr: `56c68a9c858c9ddc`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **32.863 ms**
- Response -> Child ID Request: **720.831 ms**
- Child ID Request -> Response: **13.561 ms**
- Full Attach: **767.255 ms**
- pcap parent request: `21:03:57.327` (frame 479)
- pcap parent response: `21:03:57.360` (frame 482)
- pcap child id request: `21:03:58.080` (frame 486)
- pcap child id response: `21:03:58.094` (frame 488)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260721-210603-run09.log`

- manifest status: `completed`
- child extaddr: `0a9cad82cb38a7ff`

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
- parent extaddr: `fa6122886b2cd9a0`
- parent rloc16: `n/a`
- child extaddr: `0a9cad82cb38a7ff`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **348.937 ms**
- Response -> Child ID Request: **402.065 ms**
- Child ID Request -> Response: **13.196 ms**
- Full Attach: **764.198 ms**
- pcap parent request: `21:11:54.469` (frame 1185)
- pcap parent response: `21:11:54.818` (frame 1190)
- pcap child id request: `21:11:55.220` (frame 1194)
- pcap child id response: `21:11:55.233` (frame 1196)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `268db44f400596a6`
- parent rloc16: `n/a`
- child extaddr: `0a9cad82cb38a7ff`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **321.307 ms**
- Response -> Child ID Request: **432.476 ms**
- Child ID Request -> Response: **14.553 ms**
- Full Attach: **768.336 ms**
- pcap parent request: `21:15:54.477` (frame 1479)
- pcap parent response: `21:15:54.798` (frame 1484)
- pcap child id request: `21:15:55.231` (frame 1486)
- pcap child id response: `21:15:55.245` (frame 1488)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260721-211801-run10.log`

- manifest status: `completed`
- child extaddr: `62980ec245753d22`

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
- parent extaddr: `d67aacbce48e7279`
- parent rloc16: `n/a`
- child extaddr: `62980ec245753d22`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **344.327 ms**
- Response -> Child ID Request: **408.674 ms**
- Child ID Request -> Response: **14.363 ms**
- Full Attach: **767.364 ms**
- pcap parent request: `21:23:52.105` (frame 825)
- pcap parent response: `21:23:52.450` (frame 832)
- pcap child id request: `21:23:52.858` (frame 835)
- pcap child id response: `21:23:52.873` (frame 837)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `d68aa19abe5ec410`
- parent rloc16: `n/a`
- child extaddr: `62980ec245753d22`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **230.807 ms**
- Response -> Child ID Request: **521.169 ms**
- Child ID Request -> Response: **13.26 ms**
- Full Attach: **765.236 ms**
- pcap parent request: `21:27:52.086` (frame 1117)
- pcap parent response: `21:27:52.317` (frame 1120)
- pcap child id request: `21:27:52.838` (frame 1124)
- pcap child id response: `21:27:52.852` (frame 1126)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260721-212958-run11.log`

- manifest status: `completed`
- child extaddr: `a65ba8953cef8a8a`

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
- parent extaddr: `4a23e67da3dfdd1b`
- parent rloc16: `n/a`
- child extaddr: `a65ba8953cef8a8a`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **138.554 ms**
- Response -> Child ID Request: **611.449 ms**
- Child ID Request -> Response: **14.581 ms**
- Full Attach: **764.584 ms**
- pcap parent request: `21:35:49.797` (frame 223)
- pcap parent response: `21:35:49.936` (frame 224)
- pcap child id request: `21:35:50.547` (frame 232)
- pcap child id response: `21:35:50.562` (frame 234)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `b2b1f70053bbc5e7`
- parent rloc16: `n/a`
- child extaddr: `a65ba8953cef8a8a`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **375.614 ms**
- Response -> Child ID Request: **374.599 ms**
- Child ID Request -> Response: **14.437 ms**
- Full Attach: **764.65 ms**
- pcap parent request: `21:39:49.986` (frame 508)
- pcap parent response: `21:39:50.362` (frame 513)
- pcap child id request: `21:39:50.736` (frame 515)
- pcap child id response: `21:39:50.751` (frame 517)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260721-214156-run12.log`

- manifest status: `completed`
- child extaddr: `9a10e22d9b404b78`

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
- parent extaddr: `c66d26571992ff23`
- parent rloc16: `n/a`
- child extaddr: `9a10e22d9b404b78`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **185.835 ms**
- Response -> Child ID Request: **564.119 ms**
- Child ID Request -> Response: **14.195 ms**
- Full Attach: **764.149 ms**
- pcap parent request: `21:47:47.238` (frame 281)
- pcap parent response: `21:47:47.424` (frame 282)
- pcap child id request: `21:47:47.988` (frame 290)
- pcap child id response: `21:47:48.002` (frame 292)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `f2e660bb42e86647`
- parent rloc16: `n/a`
- child extaddr: `9a10e22d9b404b78`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **476.673 ms**
- Response -> Child ID Request: **272.503 ms**
- Child ID Request -> Response: **14.517 ms**
- Full Attach: **763.693 ms**
- pcap parent request: `21:51:47.336` (frame 567)
- pcap parent response: `21:51:47.812` (frame 572)
- pcap child id request: `21:51:48.085` (frame 574)
- pcap child id response: `21:51:48.099` (frame 576)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260721-215354-run13.log`

- manifest status: `completed`
- child extaddr: `56789c22f7c1f249`

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
- parent extaddr: `0af8297614ec7c94`
- parent rloc16: `n/a`
- child extaddr: `56789c22f7c1f249`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **21.757 ms**
- Response -> Child ID Request: **728.238 ms**
- Child ID Request -> Response: **13.133 ms**
- Full Attach: **763.128 ms**
- pcap parent request: `21:59:44.778` (frame 532)
- pcap parent response: `21:59:44.800` (frame 533)
- pcap child id request: `21:59:45.528` (frame 541)
- pcap child id response: `21:59:45.541` (frame 543)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `0a6945c11dfce573`
- parent rloc16: `n/a`
- child extaddr: `56789c22f7c1f249`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **290.714 ms**
- Response -> Child ID Request: **463.269 ms**
- Child ID Request -> Response: **12.353 ms**
- Full Attach: **766.336 ms**
- pcap parent request: `22:03:45.107` (frame 817)
- pcap parent response: `22:03:45.398` (frame 822)
- pcap child id request: `22:03:45.861` (frame 824)
- pcap child id response: `22:03:45.873` (frame 826)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260721-220551-run14.log`

- manifest status: `completed`
- child extaddr: `aa3891c6a9da4266`

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
- parent extaddr: `5e60ef4682146520`
- parent rloc16: `n/a`
- child extaddr: `aa3891c6a9da4266`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **183.886 ms**
- Response -> Child ID Request: **568.126 ms**
- Child ID Request -> Response: **12.429 ms**
- Full Attach: **764.441 ms**
- pcap parent request: `22:11:42.838` (frame 188)
- pcap parent response: `22:11:43.022` (frame 191)
- pcap child id request: `22:11:43.590` (frame 197)
- pcap child id response: `22:11:43.602` (frame 199)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `7eb5a2ec0a16c9c3`
- parent rloc16: `n/a`
- child extaddr: `aa3891c6a9da4266`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **330.559 ms**
- Response -> Child ID Request: **420.456 ms**
- Child ID Request -> Response: **12.792 ms**
- Full Attach: **763.807 ms**
- pcap parent request: `22:15:42.849` (frame 473)
- pcap parent response: `22:15:43.179` (frame 476)
- pcap child id request: `22:15:43.600` (frame 480)
- pcap child id response: `22:15:43.612` (frame 482)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260721-221749-run15.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `da1be92750f88bba`

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
- parent extaddr: `2e34f1714037cd3d`
- parent rloc16: `n/a`
- child extaddr: `da1be92750f88bba`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **51.098 ms**
- Response -> Child ID Request: **700.888 ms**
- Child ID Request -> Response: **14.166 ms**
- Full Attach: **766.152 ms**
- pcap parent request: `22:23:40.358` (frame 419)
- pcap parent response: `22:23:40.409` (frame 420)
- pcap child id request: `22:23:41.110` (frame 428)
- pcap child id response: `22:23:41.124` (frame 430)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `fae674f5d1161d01`
- parent rloc16: `n/a`
- child extaddr: `da1be92750f88bba`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **194.341 ms**
- Response -> Child ID Request: **555.806 ms**
- Child ID Request -> Response: **14.23 ms**
- Full Attach: **764.377 ms**
- pcap parent request: `22:27:40.981` (frame 780)
- pcap parent response: `22:27:41.175` (frame 783)
- pcap child id request: `22:27:41.731` (frame 788)
- pcap child id response: `22:27:41.745` (frame 790)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260721-222947-run16.log`

- manifest status: `completed`
- child extaddr: `b2709e479480b345`

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
- parent extaddr: `4a2e53a8395326ac`
- parent rloc16: `n/a`
- child extaddr: `b2709e479480b345`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **437.77 ms**
- Response -> Child ID Request: **312.244 ms**
- Child ID Request -> Response: **13.78 ms**
- Full Attach: **763.794 ms**
- pcap parent request: `22:35:38.082` (frame 1230)
- pcap parent response: `22:35:38.520` (frame 1237)
- pcap child id request: `22:35:38.832` (frame 1240)
- pcap child id response: `22:35:38.846` (frame 1242)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `1e89d3e7df6f0eac`
- parent rloc16: `n/a`
- child extaddr: `b2709e479480b345`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **73.089 ms**
- Response -> Child ID Request: **680.609 ms**
- Child ID Request -> Response: **12.987 ms**
- Full Attach: **766.685 ms**
- pcap parent request: `22:39:38.741` (frame 1526)
- pcap parent response: `22:39:38.814` (frame 1527)
- pcap child id request: `22:39:39.495` (frame 1534)
- pcap child id response: `22:39:39.508` (frame 1536)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260721-224145-run17.log`

- manifest status: `completed`
- child extaddr: `a294b97321ed34bb`

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
- parent extaddr: `96ceaf9a6bf0b0a2`
- parent rloc16: `n/a`
- child extaddr: `a294b97321ed34bb`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **341.181 ms**
- Response -> Child ID Request: **408.825 ms**
- Child ID Request -> Response: **13.226 ms**
- Full Attach: **763.232 ms**
- pcap parent request: `22:47:35.962` (frame 281)
- pcap parent response: `22:47:36.303` (frame 285)
- pcap child id request: `22:47:36.712` (frame 291)
- pcap child id response: `22:47:36.725` (frame 293)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `32706efcef728dd6`
- parent rloc16: `n/a`
- child extaddr: `a294b97321ed34bb`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **126.799 ms**
- Response -> Child ID Request: **622.225 ms**
- Child ID Request -> Response: **14.799 ms**
- Full Attach: **763.823 ms**
- pcap parent request: `22:51:36.290` (frame 566)
- pcap parent response: `22:51:36.416` (frame 567)
- pcap child id request: `22:51:37.039` (frame 573)
- pcap child id response: `22:51:37.053` (frame 575)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260721-225342-run18.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `fa363aa348001226`

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
- parent extaddr: `4aedd746508481b1`
- parent rloc16: `n/a`
- child extaddr: `fa363aa348001226`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **140.58 ms**
- Response -> Child ID Request: **608.437 ms**
- Child ID Request -> Response: **12.817 ms**
- Full Attach: **761.834 ms**
- pcap parent request: `22:59:33.450` (frame 434)
- pcap parent response: `22:59:33.591` (frame 435)
- pcap child id request: `22:59:34.199` (frame 443)
- pcap child id response: `22:59:34.212` (frame 445)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `3a354e8870ceb3ba`
- parent rloc16: `n/a`
- child extaddr: `fa363aa348001226`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **10.149 ms**
- Response -> Child ID Request: **741.741 ms**
- Child ID Request -> Response: **13.725 ms**
- Full Attach: **765.615 ms**
- pcap parent request: `23:03:33.757` (frame 768)
- pcap parent response: `23:03:33.767` (frame 769)
- pcap child id request: `23:03:34.509` (frame 774)
- pcap child id response: `23:03:34.523` (frame 776)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260721-230540-run19.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `c2341c3121f0490e`

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
- parent extaddr: `762dd2577a0574f8`
- parent rloc16: `n/a`
- child extaddr: `c2341c3121f0490e`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **145.998 ms**
- Response -> Child ID Request: **604.007 ms**
- Child ID Request -> Response: **13.022 ms**
- Full Attach: **763.027 ms**
- pcap parent request: `23:11:30.940` (frame 223)
- pcap parent response: `23:11:31.086` (frame 226)
- pcap child id request: `23:11:31.690` (frame 232)
- pcap child id response: `23:11:31.703` (frame 234)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `96ca84dc5ee1cdf1`
- parent rloc16: `n/a`
- child extaddr: `c2341c3121f0490e`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **169.357 ms**
- Response -> Child ID Request: **581.656 ms**
- Child ID Request -> Response: **13.395 ms**
- Full Attach: **764.408 ms**
- pcap parent request: `23:15:31.166` (frame 582)
- pcap parent response: `23:15:31.335` (frame 585)
- pcap child id request: `23:15:31.917` (frame 590)
- pcap child id response: `23:15:31.930` (frame 592)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260721-231738-run20.log`

- manifest status: `completed`
- child extaddr: `e64dc1caf4c8f0a0`

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
- parent extaddr: `3a02f43e8ff34ce2`
- parent rloc16: `n/a`
- child extaddr: `e64dc1caf4c8f0a0`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **206.186 ms**
- Response -> Child ID Request: **546.806 ms**
- Child ID Request -> Response: **14.24 ms**
- Full Attach: **767.232 ms**
- pcap parent request: `23:23:28.464` (frame 614)
- pcap parent response: `23:23:28.671` (frame 617)
- pcap child id request: `23:23:29.217` (frame 623)
- pcap child id response: `23:23:29.232` (frame 625)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `c6014a21dbbce304`
- parent rloc16: `n/a`
- child extaddr: `e64dc1caf4c8f0a0`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **420.286 ms**
- Response -> Child ID Request: **332.705 ms**
- Child ID Request -> Response: **12.889 ms**
- Full Attach: **765.88 ms**
- pcap parent request: `23:27:28.688` (frame 899)
- pcap parent response: `23:27:29.109` (frame 902)
- pcap child id request: `23:27:29.441` (frame 906)
- pcap child id response: `23:27:29.454` (frame 908)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**
