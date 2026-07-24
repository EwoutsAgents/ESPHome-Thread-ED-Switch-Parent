# Child Log Analysis

## stock_child

Files analyzed: **20**

- batch folders: `stock_low_power-3router-20runs-20260724-200932`

### PCAP-complete child attach summary

| Attach | Metric | M (SD), ms | n |
| --- | --- | ---: | ---: |
| 1 | Request -> Response | 201.16 (101.11) | 20 |
| 1 | Request -> Response minus Random Delay | 9.66 (1.16) | 20 |
| 1 | Response -> Child ID Request | 550.60 (100.97) | 20 |
| 1 | Child ID Request -> Response | 13.74 (0.95) | 20 |
| 1 | Full Attach | 765.51 (1.29) | 20 |
| 2 | Request -> Response | 269.93 (137.84) | 20 |
| 2 | Request -> Response minus Random Delay | 9.48 (1.36) | 20 |
| 2 | Response -> Child ID Request | 481.62 (137.93) | 20 |
| 2 | Child ID Request -> Response | 13.49 (1.13) | 20 |
| 2 | Full Attach | 765.05 (1.72) | 20 |

| Metric | M (SD) | n |
| --- | ---: | ---: |
| Failed TX Attempts per Log | 0.00 (0.00) | 20 |
| Log-only or Partial Sequences per Log | 0.00 (0.00) | 20 |

### `stock_child_20260724-201204-run01.log`

- manifest status: `completed`
- child extaddr: `5226fe875d39e1e4`

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
- parent extaddr: `7e71923315fa8744`
- parent rloc16: `n/a`
- child extaddr: `5226fe875d39e1e4`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **136.973 ms**
- selected-parent logged random delay: **126 ms**
- random-delay source router: `router2`
- random-delay source log time: `20:15:21.546`
- Request -> Response minus Random Delay: **10.973 ms**
- Response -> Child ID Request: **615.031 ms**
- Child ID Request -> Response: **13.258 ms**
- Full Attach: **765.262 ms**
- pcap parent request: `20:15:21.565` (frame 89)
- pcap parent response: `20:15:21.702` (frame 92)
- pcap child id request: `20:15:22.317` (frame 96)
- pcap child id response: `20:15:22.330` (frame 98)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `d6acd1443dd59340`
- parent rloc16: `n/a`
- child extaddr: `5226fe875d39e1e4`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **59.049 ms**
- selected-parent logged random delay: **50 ms**
- random-delay source router: `router1`
- random-delay source log time: `20:19:21.716`
- Request -> Response minus Random Delay: **9.049 ms**
- Response -> Child ID Request: **691.957 ms**
- Child ID Request -> Response: **14.801 ms**
- Full Attach: **765.807 ms**
- pcap parent request: `20:19:21.744` (frame 306)
- pcap parent response: `20:19:21.803` (frame 307)
- pcap child id request: `20:19:22.495` (frame 311)
- pcap child id response: `20:19:22.509` (frame 313)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-201943-run02.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `6e688df445510034`

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
- parent extaddr: `ae3fc34fc8f24160`
- parent rloc16: `n/a`
- child extaddr: `6e688df445510034`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **84.562 ms**
- selected-parent logged random delay: **74 ms**
- random-delay source router: `router1`
- random-delay source log time: `20:22:58.913`
- Request -> Response minus Random Delay: **10.562 ms**
- Response -> Child ID Request: **665.441 ms**
- Child ID Request -> Response: **12.83 ms**
- Full Attach: **762.833 ms**
- pcap parent request: `20:22:58.932` (frame 88)
- pcap parent response: `20:22:59.017` (frame 89)
- pcap child id request: `20:22:59.682` (frame 95)
- pcap child id response: `20:22:59.695` (frame 97)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `f62b57881ee9e126`
- parent rloc16: `n/a`
- child extaddr: `6e688df445510034`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **253.563 ms**
- selected-parent logged random delay: **244 ms**
- random-delay source router: `router2`
- random-delay source log time: `20:26:58.951`
- Request -> Response minus Random Delay: **9.563 ms**
- Response -> Child ID Request: **498.429 ms**
- Child ID Request -> Response: **14.592 ms**
- Full Attach: **766.584 ms**
- pcap parent request: `20:26:58.979` (frame 346)
- pcap parent response: `20:26:59.233` (frame 347)
- pcap child id request: `20:26:59.731` (frame 351)
- pcap child id response: `20:26:59.746` (frame 353)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-202720-run03.log`

- manifest status: `completed`
- child extaddr: `62451e09f376650a`

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
- parent extaddr: `6e84fbb083254cf0`
- parent rloc16: `n/a`
- child extaddr: `62451e09f376650a`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **86.544 ms**
- selected-parent logged random delay: **76 ms**
- random-delay source router: `router2`
- random-delay source log time: `20:30:36.165`
- Request -> Response minus Random Delay: **10.544 ms**
- Response -> Child ID Request: **666.437 ms**
- Child ID Request -> Response: **13.607 ms**
- Full Attach: **766.588 ms**
- pcap parent request: `20:30:36.184` (frame 95)
- pcap parent response: `20:30:36.270` (frame 96)
- pcap child id request: `20:30:36.937` (frame 102)
- pcap child id response: `20:30:36.950` (frame 104)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `3aac044f78dadd8c`
- parent rloc16: `n/a`
- child extaddr: `62451e09f376650a`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **243.183 ms**
- selected-parent logged random delay: **232 ms**
- random-delay source router: `router1`
- random-delay source log time: `20:34:36.451`
- Request -> Response minus Random Delay: **11.183 ms**
- Response -> Child ID Request: **507.822 ms**
- Child ID Request -> Response: **13.201 ms**
- Full Attach: **764.206 ms**
- pcap parent request: `20:34:36.479` (frame 314)
- pcap parent response: `20:34:36.722` (frame 315)
- pcap child id request: `20:34:37.230` (frame 319)
- pcap child id response: `20:34:37.243` (frame 321)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-203458-run04.log`

- manifest status: `completed`
- child extaddr: `a2c3c11f71eeb906`

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
- parent extaddr: `ea9304569c92a7b3`
- parent rloc16: `n/a`
- child extaddr: `a2c3c11f71eeb906`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **298.964 ms**
- selected-parent logged random delay: **290 ms**
- random-delay source router: `router2`
- random-delay source log time: `20:38:14.017`
- Request -> Response minus Random Delay: **8.964 ms**
- Response -> Child ID Request: **453.147 ms**
- Child ID Request -> Response: **14.882 ms**
- Full Attach: **766.993 ms**
- pcap parent request: `20:38:14.036` (frame 94)
- pcap parent response: `20:38:14.335` (frame 97)
- pcap child id request: `20:38:14.789` (frame 101)
- pcap child id response: `20:38:14.803` (frame 103)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `a60d0eb7b671e765`
- parent rloc16: `n/a`
- child extaddr: `a2c3c11f71eeb906`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **225.394 ms**
- selected-parent logged random delay: **216 ms**
- random-delay source router: `router1`
- random-delay source log time: `20:42:14.145`
- Request -> Response minus Random Delay: **9.394 ms**
- Response -> Child ID Request: **526.698 ms**
- Child ID Request -> Response: **12.571 ms**
- Full Attach: **764.663 ms**
- pcap parent request: `20:42:14.174` (frame 310)
- pcap parent response: `20:42:14.399` (frame 311)
- pcap child id request: `20:42:14.926` (frame 315)
- pcap child id response: `20:42:14.938` (frame 317)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-204236-run05.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `3e2a853f144abcd4`

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
- parent extaddr: `7aa9e7b17729bb6a`
- parent rloc16: `n/a`
- child extaddr: `3e2a853f144abcd4`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **400.127 ms**
- selected-parent logged random delay: **391 ms**
- random-delay source router: `router1`
- random-delay source log time: `20:45:52.079`
- Request -> Response minus Random Delay: **9.127 ms**
- Response -> Child ID Request: **351.874 ms**
- Child ID Request -> Response: **12.394 ms**
- Full Attach: **764.395 ms**
- pcap parent request: `20:45:52.097` (frame 85)
- pcap parent response: `20:45:52.497` (frame 86)
- pcap child id request: `20:45:52.849` (frame 92)
- pcap child id response: `20:45:52.861` (frame 94)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `9aadc69e001eca17`
- parent rloc16: `n/a`
- child extaddr: `3e2a853f144abcd4`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **414.584 ms**
- selected-parent logged random delay: **405 ms**
- random-delay source router: `router2`
- random-delay source log time: `20:49:52.609`
- Request -> Response minus Random Delay: **9.584 ms**
- Response -> Child ID Request: **337.424 ms**
- Child ID Request -> Response: **12.847 ms**
- Full Attach: **764.855 ms**
- pcap parent request: `20:49:52.636` (frame 335)
- pcap parent response: `20:49:53.051` (frame 338)
- pcap child id request: `20:49:53.388` (frame 340)
- pcap child id response: `20:49:53.401` (frame 342)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-205013-run06.log`

- manifest status: `completed`
- child extaddr: `c219012ce16efdef`

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
- parent extaddr: `e6f3425ec85672c4`
- parent rloc16: `n/a`
- child extaddr: `c219012ce16efdef`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **97.449 ms**
- selected-parent logged random delay: **89 ms**
- random-delay source router: `router2`
- random-delay source log time: `20:53:29.307`
- Request -> Response minus Random Delay: **8.449 ms**
- Response -> Child ID Request: **654.55 ms**
- Child ID Request -> Response: **13.591 ms**
- Full Attach: **765.59 ms**
- pcap parent request: `20:53:29.325` (frame 92)
- pcap parent response: `20:53:29.423` (frame 93)
- pcap child id request: `20:53:30.077` (frame 99)
- pcap child id response: `20:53:30.091` (frame 101)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `caced74b392fe611`
- parent rloc16: `n/a`
- child extaddr: `c219012ce16efdef`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **436.75 ms**
- selected-parent logged random delay: **427 ms**
- random-delay source router: `router1`
- random-delay source log time: `20:57:29.373`
- Request -> Response minus Random Delay: **9.75 ms**
- Response -> Child ID Request: **315.056 ms**
- Child ID Request -> Response: **12.183 ms**
- Full Attach: **763.989 ms**
- pcap parent request: `20:57:29.399` (frame 309)
- pcap parent response: `20:57:29.836` (frame 312)
- pcap child id request: `20:57:30.151` (frame 314)
- pcap child id response: `20:57:30.163` (frame 316)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-205751-run07.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `e652f67d016045ee`

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
- parent extaddr: `3e198a64baad4903`
- parent rloc16: `n/a`
- child extaddr: `e652f67d016045ee`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **144.675 ms**
- selected-parent logged random delay: **137 ms**
- random-delay source router: `router1`
- random-delay source log time: `21:01:07.248`
- Request -> Response minus Random Delay: **7.675 ms**
- Response -> Child ID Request: **607.45 ms**
- Child ID Request -> Response: **13.7 ms**
- Full Attach: **765.825 ms**
- pcap parent request: `21:01:07.265` (frame 89)
- pcap parent response: `21:01:07.409` (frame 90)
- pcap child id request: `21:01:08.017` (frame 96)
- pcap child id response: `21:01:08.030` (frame 98)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `d264bb6f2b3216e5`
- parent rloc16: `n/a`
- child extaddr: `e652f67d016045ee`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **303.492 ms**
- selected-parent logged random delay: **293 ms**
- random-delay source router: `router2`
- random-delay source log time: `21:05:07.506`
- Request -> Response minus Random Delay: **10.492 ms**
- Response -> Child ID Request: **447.497 ms**
- Child ID Request -> Response: **13.532 ms**
- Full Attach: **764.521 ms**
- pcap parent request: `21:05:07.531` (frame 345)
- pcap parent response: `21:05:07.834` (frame 346)
- pcap child id request: `21:05:08.282` (frame 350)
- pcap child id response: `21:05:08.295` (frame 352)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-210529-run08.log`

- manifest status: `completed`
- child extaddr: `66ad1c32b57bc5df`

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
- parent extaddr: `bade28e1ff0699ff`
- parent rloc16: `n/a`
- child extaddr: `66ad1c32b57bc5df`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **305.959 ms**
- selected-parent logged random delay: **297 ms**
- random-delay source router: `router2`
- random-delay source log time: `21:08:45.170`
- Request -> Response minus Random Delay: **8.959 ms**
- Response -> Child ID Request: **446.042 ms**
- Child ID Request -> Response: **13.22 ms**
- Full Attach: **765.221 ms**
- pcap parent request: `21:08:45.182` (frame 78)
- pcap parent response: `21:08:45.488` (frame 81)
- pcap child id request: `21:08:45.934` (frame 85)
- pcap child id response: `21:08:45.947` (frame 87)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `e64117e49b2dc1ef`
- parent rloc16: `n/a`
- child extaddr: `66ad1c32b57bc5df`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **478.005 ms**
- selected-parent logged random delay: **467 ms**
- random-delay source router: `router1`
- random-delay source log time: `21:12:45.344`
- Request -> Response minus Random Delay: **11.005 ms**
- Response -> Child ID Request: **272.008 ms**
- Child ID Request -> Response: **12.245 ms**
- Full Attach: **762.258 ms**
- pcap parent request: `21:12:45.364` (frame 295)
- pcap parent response: `21:12:45.842` (frame 298)
- pcap child id request: `21:12:46.114` (frame 300)
- pcap child id response: `21:12:46.126` (frame 302)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-211307-run09.log`

- manifest status: `completed`
- child extaddr: `0a2ae64458a8ad05`

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
- parent extaddr: `3a2cc13025b4299e`
- parent rloc16: `n/a`
- child extaddr: `0a2ae64458a8ad05`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **90.458 ms**
- selected-parent logged random delay: **80 ms**
- random-delay source router: `router2`
- random-delay source log time: `21:16:23.181`
- Request -> Response minus Random Delay: **10.458 ms**
- Response -> Child ID Request: **661.539 ms**
- Child ID Request -> Response: **12.721 ms**
- Full Attach: **764.718 ms**
- pcap parent request: `21:16:23.197` (frame 97)
- pcap parent response: `21:16:23.287` (frame 98)
- pcap child id request: `21:16:23.949` (frame 104)
- pcap child id response: `21:16:23.961` (frame 106)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `9eddc9572081fae6`
- parent rloc16: `n/a`
- child extaddr: `0a2ae64458a8ad05`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **59.217 ms**
- selected-parent logged random delay: **48 ms**
- random-delay source router: `router1`
- random-delay source log time: `21:20:23.788`
- Request -> Response minus Random Delay: **11.217 ms**
- Response -> Child ID Request: **691.08 ms**
- Child ID Request -> Response: **12.149 ms**
- Full Attach: **762.446 ms**
- pcap parent request: `21:20:23.812` (frame 314)
- pcap parent response: `21:20:23.871` (frame 315)
- pcap child id request: `21:20:24.562` (frame 319)
- pcap child id response: `21:20:24.574` (frame 321)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-212044-run10.log`

- manifest status: `completed`
- child extaddr: `be09c06c62490432`

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
- parent extaddr: `ca8bcaeef3df6c9f`
- parent rloc16: `n/a`
- child extaddr: `be09c06c62490432`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **101.136 ms**
- selected-parent logged random delay: **90 ms**
- random-delay source router: `router2`
- random-delay source log time: `21:24:00.816`
- Request -> Response minus Random Delay: **11.136 ms**
- Response -> Child ID Request: **648.81 ms**
- Child ID Request -> Response: **13.235 ms**
- Full Attach: **763.181 ms**
- pcap parent request: `21:24:00.830` (frame 89)
- pcap parent response: `21:24:00.931` (frame 92)
- pcap child id request: `21:24:01.580` (frame 96)
- pcap child id response: `21:24:01.593` (frame 98)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `a6bbde38e7614703`
- parent rloc16: `n/a`
- child extaddr: `be09c06c62490432`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **174.88 ms**
- selected-parent logged random delay: **166 ms**
- random-delay source router: `router1`
- random-delay source log time: `21:28:01.210`
- Request -> Response minus Random Delay: **8.88 ms**
- Response -> Child ID Request: **577.109 ms**
- Child ID Request -> Response: **14.011 ms**
- Full Attach: **766.0 ms**
- pcap parent request: `21:28:01.232` (frame 304)
- pcap parent response: `21:28:01.407` (frame 307)
- pcap child id request: `21:28:01.984` (frame 309)
- pcap child id response: `21:28:01.998` (frame 311)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-212822-run11.log`

- manifest status: `completed`
- child extaddr: `12d4ff1ff3becf3b`

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
- parent extaddr: `5a3c11e43b8ba5c6`
- parent rloc16: `n/a`
- child extaddr: `12d4ff1ff3becf3b`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **124.59 ms**
- selected-parent logged random delay: **114 ms**
- random-delay source router: `router2`
- random-delay source log time: `21:31:38.663`
- Request -> Response minus Random Delay: **10.59 ms**
- Response -> Child ID Request: **627.418 ms**
- Child ID Request -> Response: **14.605 ms**
- Full Attach: **766.613 ms**
- pcap parent request: `21:31:38.677` (frame 90)
- pcap parent response: `21:31:38.802` (frame 91)
- pcap child id request: `21:31:39.429` (frame 98)
- pcap child id response: `21:31:39.444` (frame 100)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `aa547332d04a52e2`
- parent rloc16: `n/a`
- child extaddr: `12d4ff1ff3becf3b`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **349.846 ms**
- selected-parent logged random delay: **341 ms**
- random-delay source router: `router1`
- random-delay source log time: `21:35:38.985`
- Request -> Response minus Random Delay: **8.846 ms**
- Response -> Child ID Request: **401.165 ms**
- Child ID Request -> Response: **12.17 ms**
- Full Attach: **763.181 ms**
- pcap parent request: `21:35:39.008` (frame 308)
- pcap parent response: `21:35:39.358` (frame 311)
- pcap child id request: `21:35:39.759` (frame 313)
- pcap child id response: `21:35:39.771` (frame 315)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-213600-run12.log`

- manifest status: `completed`
- child extaddr: `36ff55be1b267cc4`

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
- parent extaddr: `42450a7edfff8a0b`
- parent rloc16: `n/a`
- child extaddr: `36ff55be1b267cc4`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **114.421 ms**
- selected-parent logged random delay: **104 ms**
- random-delay source router: `router2`
- random-delay source log time: `21:39:16.664`
- Request -> Response minus Random Delay: **10.421 ms**
- Response -> Child ID Request: **637.558 ms**
- Child ID Request -> Response: **13.476 ms**
- Full Attach: **765.455 ms**
- pcap parent request: `21:39:16.679` (frame 92)
- pcap parent response: `21:39:16.794` (frame 95)
- pcap child id request: `21:39:17.431` (frame 99)
- pcap child id response: `21:39:17.445` (frame 101)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `be1a97b7d352b859`
- parent rloc16: `n/a`
- child extaddr: `36ff55be1b267cc4`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **349.623 ms**
- selected-parent logged random delay: **342 ms**
- random-delay source router: `router1`
- random-delay source log time: `21:43:17.296`
- Request -> Response minus Random Delay: **7.623 ms**
- Response -> Child ID Request: **401.384 ms**
- Child ID Request -> Response: **12.245 ms**
- Full Attach: **763.252 ms**
- pcap parent request: `21:43:17.321` (frame 311)
- pcap parent response: `21:43:17.671` (frame 314)
- pcap child id request: `21:43:18.072` (frame 318)
- pcap child id response: `21:43:18.084` (frame 320)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-214338-run13.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `56adfdd016238a79`

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
- parent extaddr: `fe8fc681cb696f34`
- parent rloc16: `n/a`
- child extaddr: `56adfdd016238a79`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **299.668 ms**
- selected-parent logged random delay: **290 ms**
- random-delay source router: `router1`
- random-delay source log time: `21:46:54.478`
- Request -> Response minus Random Delay: **9.668 ms**
- Response -> Child ID Request: **454.397 ms**
- Child ID Request -> Response: **12.872 ms**
- Full Attach: **766.937 ms**
- pcap parent request: `21:46:54.494` (frame 93)
- pcap parent response: `21:46:54.793` (frame 94)
- pcap child id request: `21:46:55.248` (frame 100)
- pcap child id response: `21:46:55.261` (frame 102)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `3e648564220c5070`
- parent rloc16: `n/a`
- child extaddr: `56adfdd016238a79`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **281.059 ms**
- selected-parent logged random delay: **270 ms**
- random-delay source router: `router2`
- random-delay source log time: `21:50:54.638`
- Request -> Response minus Random Delay: **11.059 ms**
- Response -> Child ID Request: **469.943 ms**
- Child ID Request -> Response: **13.336 ms**
- Full Attach: **764.338 ms**
- pcap parent request: `21:50:54.663` (frame 348)
- pcap parent response: `21:50:54.944` (frame 351)
- pcap child id request: `21:50:55.414` (frame 353)
- pcap child id response: `21:50:55.427` (frame 355)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-215116-run14.log`

- manifest status: `completed`
- child extaddr: `76ce275d7327e57b`

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
- parent extaddr: `a6427496af807d4d`
- parent rloc16: `n/a`
- child extaddr: `76ce275d7327e57b`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **262.424 ms**
- selected-parent logged random delay: **252 ms**
- random-delay source router: `router2`
- random-delay source log time: `21:54:32.109`
- Request -> Response minus Random Delay: **10.424 ms**
- Response -> Child ID Request: **486.452 ms**
- Child ID Request -> Response: **15.565 ms**
- Full Attach: **764.441 ms**
- pcap parent request: `21:54:32.125` (frame 93)
- pcap parent response: `21:54:32.387` (frame 94)
- pcap child id request: `21:54:32.874` (frame 101)
- pcap child id response: `21:54:32.889` (frame 103)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `ca9d0997ab1c2537`
- parent rloc16: `n/a`
- child extaddr: `76ce275d7327e57b`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **253.838 ms**
- selected-parent logged random delay: **246 ms**
- random-delay source router: `router1`
- random-delay source log time: `21:58:32.114`
- Request -> Response minus Random Delay: **7.838 ms**
- Response -> Child ID Request: **497.972 ms**
- Child ID Request -> Response: **14.047 ms**
- Full Attach: **765.857 ms**
- pcap parent request: `21:58:32.138` (frame 310)
- pcap parent response: `21:58:32.392` (frame 311)
- pcap child id request: `21:58:32.890` (frame 315)
- pcap child id response: `21:58:32.904` (frame 317)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-215854-run15.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `6ac4dc96655207ae`

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
- parent extaddr: `123ee36b0b67b156`
- parent rloc16: `n/a`
- child extaddr: `6ac4dc96655207ae`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **167.52 ms**
- selected-parent logged random delay: **159 ms**
- random-delay source router: `router1`
- random-delay source log time: `22:02:10.042`
- Request -> Response minus Random Delay: **8.52 ms**
- Response -> Child ID Request: **583.486 ms**
- Child ID Request -> Response: **12.776 ms**
- Full Attach: **763.782 ms**
- pcap parent request: `22:02:10.058` (frame 90)
- pcap parent response: `22:02:10.225` (frame 93)
- pcap child id request: `22:02:10.809` (frame 97)
- pcap child id response: `22:02:10.822` (frame 99)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `a2d115f6239bfbc2`
- parent rloc16: `n/a`
- child extaddr: `6ac4dc96655207ae`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **454.986 ms**
- selected-parent logged random delay: **446 ms**
- random-delay source router: `router2`
- random-delay source log time: `22:06:10.081`
- Request -> Response minus Random Delay: **8.986 ms**
- Response -> Child ID Request: **297.024 ms**
- Child ID Request -> Response: **15.994 ms**
- Full Attach: **768.004 ms**
- pcap parent request: `22:06:10.107` (frame 329)
- pcap parent response: `22:06:10.562` (frame 330)
- pcap child id request: `22:06:10.859` (frame 332)
- pcap child id response: `22:06:10.875` (frame 334)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-220631-run16.log`

- manifest status: `completed`
- child extaddr: `6e2d76e281450d55`

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
- parent extaddr: `6213e3265eaebd69`
- parent rloc16: `n/a`
- child extaddr: `6e2d76e281450d55`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **230.325 ms**
- selected-parent logged random delay: **220 ms**
- random-delay source router: `router2`
- random-delay source log time: `22:09:47.658`
- Request -> Response minus Random Delay: **10.325 ms**
- Response -> Child ID Request: **521.669 ms**
- Child ID Request -> Response: **14.356 ms**
- Full Attach: **766.35 ms**
- pcap parent request: `22:09:47.676` (frame 82)
- pcap parent response: `22:09:47.906` (frame 83)
- pcap child id request: `22:09:48.428` (frame 89)
- pcap child id response: `22:09:48.442` (frame 91)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `1efb71686abf1c0d`
- parent rloc16: `n/a`
- child extaddr: `6e2d76e281450d55`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **188.724 ms**
- selected-parent logged random delay: **181 ms**
- random-delay source router: `router1`
- random-delay source log time: `22:13:48.280`
- Request -> Response minus Random Delay: **7.724 ms**
- Response -> Child ID Request: **562.497 ms**
- Child ID Request -> Response: **12.907 ms**
- Full Attach: **764.128 ms**
- pcap parent request: `22:13:48.307` (frame 299)
- pcap parent response: `22:13:48.496` (frame 302)
- pcap child id request: `22:13:49.058` (frame 304)
- pcap child id response: `22:13:49.071` (frame 306)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-221409-run17.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `8aaad4128e0524d1`

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
- parent extaddr: `2e3d60276cc85c37`
- parent rloc16: `n/a`
- child extaddr: `8aaad4128e0524d1`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **271.564 ms**
- selected-parent logged random delay: **264 ms**
- random-delay source router: `router1`
- random-delay source log time: `22:17:25.202`
- Request -> Response minus Random Delay: **7.564 ms**
- Response -> Child ID Request: **479.433 ms**
- Child ID Request -> Response: **15.724 ms**
- Full Attach: **766.721 ms**
- pcap parent request: `22:17:25.221` (frame 83)
- pcap parent response: `22:17:25.492` (frame 86)
- pcap child id request: `22:17:25.972` (frame 90)
- pcap child id response: `22:17:25.987` (frame 92)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `fa6b11122f8d8210`
- parent rloc16: `n/a`
- child extaddr: `8aaad4128e0524d1`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **243.262 ms**
- selected-parent logged random delay: **232 ms**
- random-delay source router: `router2`
- random-delay source log time: `22:21:25.620`
- Request -> Response minus Random Delay: **11.262 ms**
- Response -> Child ID Request: **508.741 ms**
- Child ID Request -> Response: **14.289 ms**
- Full Attach: **766.292 ms**
- pcap parent request: `22:21:25.647` (frame 340)
- pcap parent response: `22:21:25.890` (frame 341)
- pcap child id request: `22:21:26.399` (frame 346)
- pcap child id response: `22:21:26.413` (frame 348)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-222147-run18.log`

- manifest status: `completed`
- child extaddr: `da20b1d5533a3ce8`

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
- parent extaddr: `56c107dfe514f429`
- parent rloc16: `n/a`
- child extaddr: `da20b1d5533a3ce8`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **313.378 ms**
- selected-parent logged random delay: **305 ms**
- random-delay source router: `router2`
- random-delay source log time: `22:25:03.177`
- Request -> Response minus Random Delay: **8.378 ms**
- Response -> Child ID Request: **437.627 ms**
- Child ID Request -> Response: **14.514 ms**
- Full Attach: **765.519 ms**
- pcap parent request: `22:25:03.196` (frame 90)
- pcap parent response: `22:25:03.509` (frame 93)
- pcap child id request: `22:25:03.947` (frame 97)
- pcap child id response: `22:25:03.961` (frame 99)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `261a98fc98c402ec`
- parent rloc16: `n/a`
- child extaddr: `da20b1d5533a3ce8`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **143.551 ms**
- selected-parent logged random delay: **136 ms**
- random-delay source router: `router1`
- random-delay source log time: `22:29:03.347`
- Request -> Response minus Random Delay: **7.551 ms**
- Response -> Child ID Request: **610.25 ms**
- Child ID Request -> Response: **14.895 ms**
- Full Attach: **768.696 ms**
- pcap parent request: `22:29:03.375` (frame 308)
- pcap parent response: `22:29:03.519` (frame 311)
- pcap child id request: `22:29:04.129` (frame 313)
- pcap child id response: `22:29:04.144` (frame 315)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-222925-run19.log`

- manifest status: `completed`
- child extaddr: `ce3e577d4e47deff`

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
- parent extaddr: `96ca5845ef791dab`
- parent rloc16: `n/a`
- child extaddr: `ce3e577d4e47deff`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **155.215 ms**
- selected-parent logged random delay: **146 ms**
- random-delay source router: `router2`
- random-delay source log time: `22:32:40.622`
- Request -> Response minus Random Delay: **9.215 ms**
- Response -> Child ID Request: **597.913 ms**
- Child ID Request -> Response: **13.196 ms**
- Full Attach: **766.324 ms**
- pcap parent request: `22:32:40.641` (frame 84)
- pcap parent response: `22:32:40.796` (frame 85)
- pcap child id request: `22:32:41.394` (frame 91)
- pcap child id response: `22:32:41.407` (frame 93)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `121859b44c8c1885`
- parent rloc16: `n/a`
- child extaddr: `ce3e577d4e47deff`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **460.584 ms**
- selected-parent logged random delay: **453 ms**
- random-delay source router: `router1`
- random-delay source log time: `22:36:41.251`
- Request -> Response minus Random Delay: **7.584 ms**
- Response -> Child ID Request: **291.402 ms**
- Child ID Request -> Response: **14.789 ms**
- Full Attach: **766.775 ms**
- pcap parent request: `22:36:41.279` (frame 302)
- pcap parent response: `22:36:41.740` (frame 303)
- pcap child id request: `22:36:42.031` (frame 307)
- pcap child id response: `22:36:42.046` (frame 309)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260724-223702-run20.log`

- manifest status: `completed`
- child extaddr: `0ef1932fcd310365`

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
- parent extaddr: `1e6dde1f8ac2dfe2`
- parent rloc16: `n/a`
- child extaddr: `0ef1932fcd310365`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **337.339 ms**
- selected-parent logged random delay: **326 ms**
- random-delay source router: `router2`
- random-delay source log time: `22:40:18.384`
- Request -> Response minus Random Delay: **11.339 ms**
- Response -> Child ID Request: **415.651 ms**
- Child ID Request -> Response: **14.364 ms**
- Full Attach: **767.354 ms**
- pcap parent request: `22:40:18.404` (frame 87)
- pcap parent response: `22:40:18.741` (frame 90)
- pcap child id request: `22:40:19.157` (frame 94)
- pcap child id response: `22:40:19.171` (frame 96)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `72019a213fe53bfb`
- parent rloc16: `n/a`
- child extaddr: `0ef1932fcd310365`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **25.076 ms**
- selected-parent logged random delay: **14 ms**
- random-delay source router: `router1`
- random-delay source log time: `22:44:19.012`
- Request -> Response minus Random Delay: **11.076 ms**
- Response -> Child ID Request: **726.931 ms**
- Child ID Request -> Response: **13.096 ms**
- Full Attach: **765.103 ms**
- pcap parent request: `22:44:19.041` (frame 305)
- pcap parent response: `22:44:19.066` (frame 306)
- pcap child id request: `22:44:19.793` (frame 310)
- pcap child id response: `22:44:19.806` (frame 312)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**
