# Child Log Analysis

## ucast_fastpr_child

Files analyzed: **24**

- batch folders: `ucast_fastpr-4router-24runs-20260714-153221`

### PCAP-complete child attach summary

| Attach | Metric | M (SD), ms | n |
| --- | --- | ---: | ---: |
| 1 | Request -> Response | 156.46 (128.42) | 24 |
| 1 | Response -> Child ID Request | 595.96 (128.37) | 24 |
| 1 | Child ID Request -> Response | 13.92 (1.82) | 24 |
| 1 | Full Attach | 766.33 (3.66) | 24 |
| 2 | Request -> Response | 10.00 (5.38) | 24 |
| 2 | Response -> Child ID Request | 27.92 (1.21) | 24 |
| 2 | Child ID Request -> Response | 13.58 (0.88) | 24 |
| 2 | Full Attach | 51.50 (5.23) | 24 |

| Metric | M (SD) | n |
| --- | ---: | ---: |
| Failed TX Attempts per Log | 0.00 (0.00) | 24 |
| Log-only or Partial Sequences per Log | 1.00 (0.00) | 24 |

### `ucast_fastpr_child_20260714-153451-run01.log`

- manifest status: `completed`
- child extaddr: `12bd271abb196487`
- switch target extaddr(s): `da8efd21a9b9de9d, da8efd21a9b9de9d, da8efd21a9b9de9d`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `abe7749db0a80d7aae137aa33655e374716f9b446f15c477f2efc545c83e9e3d` |
| fast unicast Parent Response marker | `True` |
| expected for variant | `True` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `be2ceefcbd82454f`
- parent rloc16: `n/a`
- child extaddr: `12bd271abb196487`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **357 ms**
- Response -> Child ID Request: **394 ms**
- Child ID Request -> Response: **14 ms**
- Full Attach: **765 ms**
- pcap parent request: `15:40:42.093` (frame 630)
- pcap parent response: `15:40:42.450` (frame 633)
- pcap child id request: `15:40:42.844` (frame 639)
- pcap child id response: `15:40:42.858` (frame 641)

#### PCAP-complete child attach 2

- log parent request: `15:40:46.570`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `da8efd21a9b9de9d`
- parent rloc16: `n/a`
- child extaddr: `12bd271abb196487`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **10 ms**
- Response -> Child ID Request: **28 ms**
- Child ID Request -> Response: **14 ms**
- Full Attach: **52 ms**
- pcap parent request: `15:40:46.617` (frame 664)
- pcap parent response: `15:40:46.627` (frame 666)
- pcap child id request: `15:40:46.655` (frame 668)
- pcap child id response: `15:40:46.669` (frame 670)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `15:40:46.588`
- log parent response: `15:40:46.603`
- log child id request: `15:40:46.618`
- log child id response: `15:40:46.648`
- parent ipv6: `n/a`
- parent extaddr: `da8efd21a9b9de9d`
- parent rloc16: `0xb800`
- child extaddr: `12bd271abb196487`
- timing source: **unavailable**
- complete log attach: **True**
- complete pcap attach: **False**
- Request -> Response: **None ms**
- Response -> Child ID Request: **None ms**
- Child ID Request -> Response: **None ms**
- Full Attach: **None ms**

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260714-154649-run02.log`

- manifest status: `completed`
- child extaddr: `42c0d6d3d8f3f917`
- switch target extaddr(s): `3e5b40b950dea98e, 3e5b40b950dea98e, 3e5b40b950dea98e`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `abe7749db0a80d7aae137aa33655e374716f9b446f15c477f2efc545c83e9e3d` |
| fast unicast Parent Response marker | `True` |
| expected for variant | `True` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `26e03648e4d10437`
- parent rloc16: `n/a`
- child extaddr: `42c0d6d3d8f3f917`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **12 ms**
- Response -> Child ID Request: **739 ms**
- Child ID Request -> Response: **13 ms**
- Full Attach: **764 ms**
- pcap parent request: `15:52:39.703` (frame 567)
- pcap parent response: `15:52:39.715` (frame 568)
- pcap child id request: `15:52:40.454` (frame 577)
- pcap child id response: `15:52:40.467` (frame 579)

#### PCAP-complete child attach 2

- log parent request: `15:52:44.279`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `3e5b40b950dea98e`
- parent rloc16: `n/a`
- child extaddr: `42c0d6d3d8f3f917`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **9 ms**
- Response -> Child ID Request: **28 ms**
- Child ID Request -> Response: **14 ms**
- Full Attach: **51 ms**
- pcap parent request: `15:52:44.326` (frame 593)
- pcap parent response: `15:52:44.335` (frame 595)
- pcap child id request: `15:52:44.363` (frame 597)
- pcap child id response: `15:52:44.377` (frame 599)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `15:52:44.297`
- log parent response: `15:52:44.311`
- log child id request: `15:52:44.326`
- log child id response: `15:52:44.356`
- parent ipv6: `n/a`
- parent extaddr: `3e5b40b950dea98e`
- parent rloc16: `0x8800`
- child extaddr: `42c0d6d3d8f3f917`
- timing source: **unavailable**
- complete log attach: **True**
- complete pcap attach: **False**
- Request -> Response: **None ms**
- Response -> Child ID Request: **None ms**
- Child ID Request -> Response: **None ms**
- Full Attach: **None ms**

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260714-155846-run03.log`

- manifest status: `completed`
- child extaddr: `1663fb5a813be6e1`
- switch target extaddr(s): `665a0537b2179792, 665a0537b2179792, 665a0537b2179792`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `abe7749db0a80d7aae137aa33655e374716f9b446f15c477f2efc545c83e9e3d` |
| fast unicast Parent Response marker | `True` |
| expected for variant | `True` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `3e1640bd9bb8d53a`
- parent rloc16: `n/a`
- child extaddr: `1663fb5a813be6e1`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **199 ms**
- Response -> Child ID Request: **555 ms**
- Child ID Request -> Response: **13 ms**
- Full Attach: **767 ms**
- pcap parent request: `16:04:37.550` (frame 600)
- pcap parent response: `16:04:37.749` (frame 601)
- pcap child id request: `16:04:38.304` (frame 610)
- pcap child id response: `16:04:38.317` (frame 612)

#### PCAP-complete child attach 2

- log parent request: `16:04:42.161`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `665a0537b2179792`
- parent rloc16: `n/a`
- child extaddr: `1663fb5a813be6e1`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **8 ms**
- Response -> Child ID Request: **29 ms**
- Child ID Request -> Response: **13 ms**
- Full Attach: **50 ms**
- pcap parent request: `16:04:42.210` (frame 616)
- pcap parent response: `16:04:42.218` (frame 618)
- pcap child id request: `16:04:42.247` (frame 620)
- pcap child id response: `16:04:42.260` (frame 622)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `16:04:42.180`
- log parent response: `16:04:42.194`
- log child id request: `16:04:42.210`
- log child id response: `16:04:42.239`
- parent ipv6: `n/a`
- parent extaddr: `665a0537b2179792`
- parent rloc16: `0x5c00`
- child extaddr: `1663fb5a813be6e1`
- timing source: **unavailable**
- complete log attach: **True**
- complete pcap attach: **False**
- Request -> Response: **None ms**
- Response -> Child ID Request: **None ms**
- Child ID Request -> Response: **None ms**
- Full Attach: **None ms**

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260714-161044-run04.log`

- manifest status: `completed`
- child extaddr: `b66120f32125fc1e`
- switch target extaddr(s): `fa654ad047b0e50f, fa654ad047b0e50f, fa654ad047b0e50f`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `abe7749db0a80d7aae137aa33655e374716f9b446f15c477f2efc545c83e9e3d` |
| fast unicast Parent Response marker | `True` |
| expected for variant | `True` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `6e59a65c49b0e2b1`
- parent rloc16: `n/a`
- child extaddr: `b66120f32125fc1e`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **19 ms**
- Response -> Child ID Request: **736 ms**
- Child ID Request -> Response: **13 ms**
- Full Attach: **768 ms**
- pcap parent request: `16:16:35.616` (frame 615)
- pcap parent response: `16:16:35.635` (frame 616)
- pcap child id request: `16:16:36.371` (frame 644)
- pcap child id response: `16:16:36.384` (frame 646)

#### PCAP-complete child attach 2

- log parent request: `16:16:39.877`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `fa654ad047b0e50f`
- parent rloc16: `n/a`
- child extaddr: `b66120f32125fc1e`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **9 ms**
- Response -> Child ID Request: **28 ms**
- Child ID Request -> Response: **13 ms**
- Full Attach: **50 ms**
- pcap parent request: `16:16:39.925` (frame 648)
- pcap parent response: `16:16:39.934` (frame 650)
- pcap child id request: `16:16:39.962` (frame 652)
- pcap child id response: `16:16:39.975` (frame 654)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `16:16:39.895`
- log parent response: `16:16:39.910`
- log child id request: `16:16:39.925`
- log child id response: `16:16:39.954`
- parent ipv6: `n/a`
- parent extaddr: `fa654ad047b0e50f`
- parent rloc16: `0x0400`
- child extaddr: `b66120f32125fc1e`
- timing source: **unavailable**
- complete log attach: **True**
- complete pcap attach: **False**
- Request -> Response: **None ms**
- Response -> Child ID Request: **None ms**
- Child ID Request -> Response: **None ms**
- Full Attach: **None ms**

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260714-162242-run05.log`

- manifest status: `completed`
- child extaddr: `d249c54c1d3a2fed`
- switch target extaddr(s): `c6696e19fcb4df9e, c6696e19fcb4df9e, c6696e19fcb4df9e`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `abe7749db0a80d7aae137aa33655e374716f9b446f15c477f2efc545c83e9e3d` |
| fast unicast Parent Response marker | `True` |
| expected for variant | `True` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `f6148310e66a1159`
- parent rloc16: `n/a`
- child extaddr: `d249c54c1d3a2fed`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **428 ms**
- Response -> Child ID Request: **321 ms**
- Child ID Request -> Response: **13 ms**
- Full Attach: **762 ms**
- pcap parent request: `16:28:33.552` (frame 602)
- pcap parent response: `16:28:33.980` (frame 605)
- pcap child id request: `16:28:34.301` (frame 611)
- pcap child id response: `16:28:34.314` (frame 613)

#### PCAP-complete child attach 2

- log parent request: `16:28:37.532`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `c6696e19fcb4df9e`
- parent rloc16: `n/a`
- child extaddr: `d249c54c1d3a2fed`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **9 ms**
- Response -> Child ID Request: **28 ms**
- Child ID Request -> Response: **14 ms**
- Full Attach: **51 ms**
- pcap parent request: `16:28:37.578` (frame 615)
- pcap parent response: `16:28:37.587` (frame 617)
- pcap child id request: `16:28:37.615` (frame 619)
- pcap child id response: `16:28:37.629` (frame 621)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `16:28:37.551`
- log parent response: `16:28:37.563`
- log child id request: `16:28:37.577`
- log child id response: `16:28:37.608`
- parent ipv6: `n/a`
- parent extaddr: `c6696e19fcb4df9e`
- parent rloc16: `0x6000`
- child extaddr: `d249c54c1d3a2fed`
- timing source: **unavailable**
- complete log attach: **True**
- complete pcap attach: **False**
- Request -> Response: **None ms**
- Response -> Child ID Request: **None ms**
- Child ID Request -> Response: **None ms**
- Full Attach: **None ms**

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260714-163440-run06.log`

- manifest status: `completed`
- child extaddr: `2608b6678e592210`
- switch target extaddr(s): `32e9e9c7f9ac40f6, 32e9e9c7f9ac40f6, 32e9e9c7f9ac40f6`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `abe7749db0a80d7aae137aa33655e374716f9b446f15c477f2efc545c83e9e3d` |
| fast unicast Parent Response marker | `True` |
| expected for variant | `True` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `4e0dbfe4111c1eeb`
- parent rloc16: `n/a`
- child extaddr: `2608b6678e592210`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **246 ms**
- Response -> Child ID Request: **513 ms**
- Child ID Request -> Response: **21 ms**
- Full Attach: **780 ms**
- pcap parent request: `16:40:30.491` (frame 589)
- pcap parent response: `16:40:30.737` (frame 592)
- pcap child id request: `16:40:31.250` (frame 610)
- pcap child id response: `16:40:31.271` (frame 614)

#### PCAP-complete child attach 2

- log parent request: `16:40:34.992`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `32e9e9c7f9ac40f6`
- parent rloc16: `n/a`
- child extaddr: `2608b6678e592210`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **11 ms**
- Response -> Child ID Request: **26 ms**
- Child ID Request -> Response: **13 ms**
- Full Attach: **50 ms**
- pcap parent request: `16:40:35.040` (frame 639)
- pcap parent response: `16:40:35.051` (frame 641)
- pcap child id request: `16:40:35.077` (frame 643)
- pcap child id response: `16:40:35.090` (frame 645)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `16:40:35.010`
- log parent response: `16:40:35.025`
- log child id request: `16:40:35.040`
- log child id response: `16:40:35.068`
- parent ipv6: `n/a`
- parent extaddr: `32e9e9c7f9ac40f6`
- parent rloc16: `0xf800`
- child extaddr: `2608b6678e592210`
- timing source: **unavailable**
- complete log attach: **True**
- complete pcap attach: **False**
- Request -> Response: **None ms**
- Response -> Child ID Request: **None ms**
- Child ID Request -> Response: **None ms**
- Full Attach: **None ms**

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260714-164637-run07.log`

- manifest status: `completed`
- child extaddr: `8e1cff8802bd3935`
- switch target extaddr(s): `aac698d502e03eb3, aac698d502e03eb3, aac698d502e03eb3`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `abe7749db0a80d7aae137aa33655e374716f9b446f15c477f2efc545c83e9e3d` |
| fast unicast Parent Response marker | `True` |
| expected for variant | `True` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `0a5f99ac65d0b49c`
- parent rloc16: `n/a`
- child extaddr: `8e1cff8802bd3935`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **50 ms**
- Response -> Child ID Request: **704 ms**
- Child ID Request -> Response: **15 ms**
- Full Attach: **769 ms**
- pcap parent request: `16:52:28.659` (frame 600)
- pcap parent response: `16:52:28.709` (frame 601)
- pcap child id request: `16:52:29.413` (frame 609)
- pcap child id response: `16:52:29.428` (frame 611)

#### PCAP-complete child attach 2

- log parent request: `16:52:32.684`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `aac698d502e03eb3`
- parent rloc16: `n/a`
- child extaddr: `8e1cff8802bd3935`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **9 ms**
- Response -> Child ID Request: **27 ms**
- Child ID Request -> Response: **13 ms**
- Full Attach: **49 ms**
- pcap parent request: `16:52:32.730` (frame 630)
- pcap parent response: `16:52:32.739` (frame 632)
- pcap child id request: `16:52:32.766` (frame 634)
- pcap child id response: `16:52:32.779` (frame 636)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `16:52:32.703`
- log parent response: `16:52:32.716`
- log child id request: `16:52:32.730`
- log child id response: `16:52:32.759`
- parent ipv6: `n/a`
- parent extaddr: `aac698d502e03eb3`
- parent rloc16: `0xd800`
- child extaddr: `8e1cff8802bd3935`
- timing source: **unavailable**
- complete log attach: **True**
- complete pcap attach: **False**
- Request -> Response: **None ms**
- Response -> Child ID Request: **None ms**
- Child ID Request -> Response: **None ms**
- Full Attach: **None ms**

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260714-165835-run08.log`

- manifest status: `completed`
- child extaddr: `7eb3c88c6c89a651`
- switch target extaddr(s): `ae75ef8dbac60635, ae75ef8dbac60635, ae75ef8dbac60635`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `abe7749db0a80d7aae137aa33655e374716f9b446f15c477f2efc545c83e9e3d` |
| fast unicast Parent Response marker | `True` |
| expected for variant | `True` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `723e44a74616632f`
- parent rloc16: `n/a`
- child extaddr: `7eb3c88c6c89a651`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **116 ms**
- Response -> Child ID Request: **635 ms**
- Child ID Request -> Response: **14 ms**
- Full Attach: **765 ms**
- pcap parent request: `17:04:26.087` (frame 590)
- pcap parent response: `17:04:26.203` (frame 591)
- pcap child id request: `17:04:26.838` (frame 599)
- pcap child id response: `17:04:26.852` (frame 601)

#### PCAP-complete child attach 2

- log parent request: `17:04:30.217`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `ae75ef8dbac60635`
- parent rloc16: `n/a`
- child extaddr: `7eb3c88c6c89a651`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **10 ms**
- Response -> Child ID Request: **27 ms**
- Child ID Request -> Response: **15 ms**
- Full Attach: **52 ms**
- pcap parent request: `17:04:30.262` (frame 619)
- pcap parent response: `17:04:30.272` (frame 621)
- pcap child id request: `17:04:30.299` (frame 623)
- pcap child id response: `17:04:30.314` (frame 625)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `17:04:30.235`
- log parent response: `17:04:30.249`
- log child id request: `17:04:30.264`
- log child id response: `17:04:30.294`
- parent ipv6: `n/a`
- parent extaddr: `ae75ef8dbac60635`
- parent rloc16: `0xa800`
- child extaddr: `7eb3c88c6c89a651`
- timing source: **unavailable**
- complete log attach: **True**
- complete pcap attach: **False**
- Request -> Response: **None ms**
- Response -> Child ID Request: **None ms**
- Child ID Request -> Response: **None ms**
- Full Attach: **None ms**

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260714-171032-run09.log`

- manifest status: `completed`
- child extaddr: `fe8b9cca16a14713`
- switch target extaddr(s): `0200327c723dcb59, 0200327c723dcb59, 0200327c723dcb59`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `abe7749db0a80d7aae137aa33655e374716f9b446f15c477f2efc545c83e9e3d` |
| fast unicast Parent Response marker | `True` |
| expected for variant | `True` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `ae3a4f70e714200f`
- parent rloc16: `n/a`
- child extaddr: `fe8b9cca16a14713`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **215 ms**
- Response -> Child ID Request: **536 ms**
- Child ID Request -> Response: **12 ms**
- Full Attach: **763 ms**
- pcap parent request: `17:16:23.301` (frame 596)
- pcap parent response: `17:16:23.516` (frame 599)
- pcap child id request: `17:16:24.052` (frame 614)
- pcap child id response: `17:16:24.064` (frame 616)

#### PCAP-complete child attach 2

- log parent request: `17:16:27.835`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `0200327c723dcb59`
- parent rloc16: `n/a`
- child extaddr: `fe8b9cca16a14713`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **9 ms**
- Response -> Child ID Request: **28 ms**
- Child ID Request -> Response: **15 ms**
- Full Attach: **52 ms**
- pcap parent request: `17:16:27.882` (frame 619)
- pcap parent response: `17:16:27.891` (frame 621)
- pcap child id request: `17:16:27.919` (frame 623)
- pcap child id response: `17:16:27.934` (frame 625)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `17:16:27.854`
- log parent response: `17:16:27.869`
- log child id request: `17:16:27.886`
- log child id response: `17:16:27.916`
- parent ipv6: `n/a`
- parent extaddr: `0200327c723dcb59`
- parent rloc16: `0x8800`
- child extaddr: `fe8b9cca16a14713`
- timing source: **unavailable**
- complete log attach: **True**
- complete pcap attach: **False**
- Request -> Response: **None ms**
- Response -> Child ID Request: **None ms**
- Child ID Request -> Response: **None ms**
- Full Attach: **None ms**

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260714-172230-run10.log`

- manifest status: `completed`
- child extaddr: `56042c2ff199b468`
- switch target extaddr(s): `6afc81d18ce4e4e1, 6afc81d18ce4e4e1, 6afc81d18ce4e4e1`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `abe7749db0a80d7aae137aa33655e374716f9b446f15c477f2efc545c83e9e3d` |
| fast unicast Parent Response marker | `True` |
| expected for variant | `True` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `0ed60311b9dc7445`
- parent rloc16: `n/a`
- child extaddr: `56042c2ff199b468`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **300 ms**
- Response -> Child ID Request: **452 ms**
- Child ID Request -> Response: **14 ms**
- Full Attach: **766 ms**
- pcap parent request: `17:28:21.008` (frame 619)
- pcap parent response: `17:28:21.308` (frame 620)
- pcap child id request: `17:28:21.760` (frame 628)
- pcap child id response: `17:28:21.774` (frame 630)

#### PCAP-complete child attach 2

- log parent request: `17:28:25.369`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `6afc81d18ce4e4e1`
- parent rloc16: `n/a`
- child extaddr: `56042c2ff199b468`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **9 ms**
- Response -> Child ID Request: **29 ms**
- Child ID Request -> Response: **15 ms**
- Full Attach: **53 ms**
- pcap parent request: `17:28:25.414` (frame 639)
- pcap parent response: `17:28:25.423` (frame 641)
- pcap child id request: `17:28:25.452` (frame 643)
- pcap child id response: `17:28:25.467` (frame 645)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `17:28:25.388`
- log parent response: `17:28:25.402`
- log child id request: `17:28:25.418`
- log child id response: `17:28:25.449`
- parent ipv6: `n/a`
- parent extaddr: `6afc81d18ce4e4e1`
- parent rloc16: `0x8800`
- child extaddr: `56042c2ff199b468`
- timing source: **unavailable**
- complete log attach: **True**
- complete pcap attach: **False**
- Request -> Response: **None ms**
- Response -> Child ID Request: **None ms**
- Child ID Request -> Response: **None ms**
- Full Attach: **None ms**

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260714-173427-run11.log`

- manifest status: `completed`
- child extaddr: `5e4568e6358b2896`
- switch target extaddr(s): `e68de794b1a25eab, e68de794b1a25eab, e68de794b1a25eab`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `abe7749db0a80d7aae137aa33655e374716f9b446f15c477f2efc545c83e9e3d` |
| fast unicast Parent Response marker | `True` |
| expected for variant | `True` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `ce737bf39c8a3dfc`
- parent rloc16: `n/a`
- child extaddr: `5e4568e6358b2896`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **337 ms**
- Response -> Child ID Request: **421 ms**
- Child ID Request -> Response: **15 ms**
- Full Attach: **773 ms**
- pcap parent request: `17:40:18.519` (frame 595)
- pcap parent response: `17:40:18.856` (frame 600)
- pcap child id request: `17:40:19.277` (frame 605)
- pcap child id response: `17:40:19.292` (frame 607)

#### PCAP-complete child attach 2

- log parent request: `17:40:23.052`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `e68de794b1a25eab`
- parent rloc16: `n/a`
- child extaddr: `5e4568e6358b2896`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **8 ms**
- Response -> Child ID Request: **28 ms**
- Child ID Request -> Response: **14 ms**
- Full Attach: **50 ms**
- pcap parent request: `17:40:23.098` (frame 629)
- pcap parent response: `17:40:23.106` (frame 631)
- pcap child id request: `17:40:23.134` (frame 633)
- pcap child id response: `17:40:23.148` (frame 635)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `17:40:23.070`
- log parent response: `17:40:23.084`
- log child id request: `17:40:23.098`
- log child id response: `17:40:23.129`
- parent ipv6: `n/a`
- parent extaddr: `e68de794b1a25eab`
- parent rloc16: `0x3800`
- child extaddr: `5e4568e6358b2896`
- timing source: **unavailable**
- complete log attach: **True**
- complete pcap attach: **False**
- Request -> Response: **None ms**
- Response -> Child ID Request: **None ms**
- Child ID Request -> Response: **None ms**
- Full Attach: **None ms**

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260714-174625-run12.log`

- manifest status: `completed`
- child extaddr: `4e9287adff3964fa`
- switch target extaddr(s): `5ae654d5f3382a87, 5ae654d5f3382a87, 5ae654d5f3382a87`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `abe7749db0a80d7aae137aa33655e374716f9b446f15c477f2efc545c83e9e3d` |
| fast unicast Parent Response marker | `True` |
| expected for variant | `True` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `c21c9f76cd674c4a`
- parent rloc16: `n/a`
- child extaddr: `4e9287adff3964fa`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **66 ms**
- Response -> Child ID Request: **686 ms**
- Child ID Request -> Response: **14 ms**
- Full Attach: **766 ms**
- pcap parent request: `17:52:16.253` (frame 566)
- pcap parent response: `17:52:16.319` (frame 567)
- pcap child id request: `17:52:17.005` (frame 575)
- pcap child id response: `17:52:17.019` (frame 577)

#### PCAP-complete child attach 2

- log parent request: `17:52:20.677`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `5ae654d5f3382a87`
- parent rloc16: `n/a`
- child extaddr: `4e9287adff3964fa`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **9 ms**
- Response -> Child ID Request: **26 ms**
- Child ID Request -> Response: **13 ms**
- Full Attach: **48 ms**
- pcap parent request: `17:52:20.722` (frame 579)
- pcap parent response: `17:52:20.731` (frame 581)
- pcap child id request: `17:52:20.757` (frame 583)
- pcap child id response: `17:52:20.770` (frame 585)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `17:52:20.695`
- log parent response: `17:52:20.709`
- log child id request: `17:52:20.724`
- log child id response: `17:52:20.752`
- parent ipv6: `n/a`
- parent extaddr: `5ae654d5f3382a87`
- parent rloc16: `0x9c00`
- child extaddr: `4e9287adff3964fa`
- timing source: **unavailable**
- complete log attach: **True**
- complete pcap attach: **False**
- Request -> Response: **None ms**
- Response -> Child ID Request: **None ms**
- Child ID Request -> Response: **None ms**
- Full Attach: **None ms**

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260714-175823-run13.log`

- manifest status: `completed`
- child extaddr: `9ae3c90226fa237a`
- switch target extaddr(s): `92e32c54d8a17f11, 92e32c54d8a17f11, 92e32c54d8a17f11`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `abe7749db0a80d7aae137aa33655e374716f9b446f15c477f2efc545c83e9e3d` |
| fast unicast Parent Response marker | `True` |
| expected for variant | `True` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `6e13a0e8cbba820c`
- parent rloc16: `n/a`
- child extaddr: `9ae3c90226fa237a`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **192 ms**
- Response -> Child ID Request: **560 ms**
- Child ID Request -> Response: **15 ms**
- Full Attach: **767 ms**
- pcap parent request: `18:04:14.381` (frame 640)
- pcap parent response: `18:04:14.573` (frame 643)
- pcap child id request: `18:04:15.133` (frame 649)
- pcap child id response: `18:04:15.148` (frame 651)

#### PCAP-complete child attach 2

- log parent request: `18:04:18.354`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `92e32c54d8a17f11`
- parent rloc16: `n/a`
- child extaddr: `9ae3c90226fa237a`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **8 ms**
- Response -> Child ID Request: **29 ms**
- Child ID Request -> Response: **13 ms**
- Full Attach: **50 ms**
- pcap parent request: `18:04:18.404` (frame 675)
- pcap parent response: `18:04:18.412` (frame 677)
- pcap child id request: `18:04:18.441` (frame 679)
- pcap child id response: `18:04:18.454` (frame 681)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `18:04:18.376`
- log parent response: `18:04:18.390`
- log child id request: `18:04:18.406`
- log child id response: `18:04:18.435`
- parent ipv6: `n/a`
- parent extaddr: `92e32c54d8a17f11`
- parent rloc16: `0xec00`
- child extaddr: `9ae3c90226fa237a`
- timing source: **unavailable**
- complete log attach: **True**
- complete pcap attach: **False**
- Request -> Response: **None ms**
- Response -> Child ID Request: **None ms**
- Child ID Request -> Response: **None ms**
- Full Attach: **None ms**

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260714-181020-run14.log`

- manifest status: `completed`
- child extaddr: `36f242b4795a12aa`
- switch target extaddr(s): `8e15953408bad061, 8e15953408bad061, 8e15953408bad061`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `abe7749db0a80d7aae137aa33655e374716f9b446f15c477f2efc545c83e9e3d` |
| fast unicast Parent Response marker | `True` |
| expected for variant | `True` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `72550064cad1aa4f`
- parent rloc16: `n/a`
- child extaddr: `36f242b4795a12aa`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **155 ms**
- Response -> Child ID Request: **596 ms**
- Child ID Request -> Response: **12 ms**
- Full Attach: **763 ms**
- pcap parent request: `18:16:11.698` (frame 584)
- pcap parent response: `18:16:11.853` (frame 589)
- pcap child id request: `18:16:12.449` (frame 593)
- pcap child id response: `18:16:12.461` (frame 595)

#### PCAP-complete child attach 2

- log parent request: `18:16:15.766`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `8e15953408bad061`
- parent rloc16: `n/a`
- child extaddr: `36f242b4795a12aa`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **10 ms**
- Response -> Child ID Request: **29 ms**
- Child ID Request -> Response: **12 ms**
- Full Attach: **51 ms**
- pcap parent request: `18:16:15.813` (frame 597)
- pcap parent response: `18:16:15.823` (frame 599)
- pcap child id request: `18:16:15.852` (frame 601)
- pcap child id response: `18:16:15.864` (frame 603)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `18:16:15.786`
- log parent response: `18:16:15.801`
- log child id request: `18:16:15.817`
- log child id response: `18:16:15.845`
- parent ipv6: `n/a`
- parent extaddr: `8e15953408bad061`
- parent rloc16: `0x6c00`
- child extaddr: `36f242b4795a12aa`
- timing source: **unavailable**
- complete log attach: **True**
- complete pcap attach: **False**
- Request -> Response: **None ms**
- Response -> Child ID Request: **None ms**
- Child ID Request -> Response: **None ms**
- Full Attach: **None ms**

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260714-182218-run15.log`

- manifest status: `completed`
- child extaddr: `2ee8d59e805a1aa2`
- switch target extaddr(s): `c2758094671c7826, c2758094671c7826, c2758094671c7826`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `abe7749db0a80d7aae137aa33655e374716f9b446f15c477f2efc545c83e9e3d` |
| fast unicast Parent Response marker | `True` |
| expected for variant | `True` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `e610329524f0865c`
- parent rloc16: `n/a`
- child extaddr: `2ee8d59e805a1aa2`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **27 ms**
- Response -> Child ID Request: **725 ms**
- Child ID Request -> Response: **14 ms**
- Full Attach: **766 ms**
- pcap parent request: `18:28:09.277` (frame 615)
- pcap parent response: `18:28:09.304` (frame 616)
- pcap child id request: `18:28:10.029` (frame 624)
- pcap child id response: `18:28:10.043` (frame 626)

#### PCAP-complete child attach 2

- log parent request: `18:28:13.324`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `c2758094671c7826`
- parent rloc16: `n/a`
- child extaddr: `2ee8d59e805a1aa2`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **9 ms**
- Response -> Child ID Request: **29 ms**
- Child ID Request -> Response: **13 ms**
- Full Attach: **51 ms**
- pcap parent request: `18:28:13.369` (frame 639)
- pcap parent response: `18:28:13.378` (frame 641)
- pcap child id request: `18:28:13.407` (frame 643)
- pcap child id response: `18:28:13.420` (frame 645)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `18:28:13.342`
- log parent response: `18:28:13.356`
- log child id request: `18:28:13.370`
- log child id response: `18:28:13.400`
- parent ipv6: `n/a`
- parent extaddr: `c2758094671c7826`
- parent rloc16: `0x5800`
- child extaddr: `2ee8d59e805a1aa2`
- timing source: **unavailable**
- complete log attach: **True**
- complete pcap attach: **False**
- Request -> Response: **None ms**
- Response -> Child ID Request: **None ms**
- Child ID Request -> Response: **None ms**
- Full Attach: **None ms**

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260714-183416-run16.log`

- manifest status: `completed`
- child extaddr: `caf4f31a4aabef0b`
- switch target extaddr(s): `ee4c91992d52d2c6, ee4c91992d52d2c6, ee4c91992d52d2c6`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `abe7749db0a80d7aae137aa33655e374716f9b446f15c477f2efc545c83e9e3d` |
| fast unicast Parent Response marker | `True` |
| expected for variant | `True` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `76ccb3be804db23e`
- parent rloc16: `n/a`
- child extaddr: `caf4f31a4aabef0b`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **58 ms**
- Response -> Child ID Request: **693 ms**
- Child ID Request -> Response: **13 ms**
- Full Attach: **764 ms**
- pcap parent request: `18:40:07.045` (frame 598)
- pcap parent response: `18:40:07.103` (frame 599)
- pcap child id request: `18:40:07.796` (frame 607)
- pcap child id response: `18:40:07.809` (frame 609)

#### PCAP-complete child attach 2

- log parent request: `18:40:10.995`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `ee4c91992d52d2c6`
- parent rloc16: `n/a`
- child extaddr: `caf4f31a4aabef0b`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **8 ms**
- Response -> Child ID Request: **29 ms**
- Child ID Request -> Response: **12 ms**
- Full Attach: **49 ms**
- pcap parent request: `18:40:11.036` (frame 612)
- pcap parent response: `18:40:11.044` (frame 614)
- pcap child id request: `18:40:11.073` (frame 616)
- pcap child id response: `18:40:11.085` (frame 618)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `18:40:11.014`
- log parent response: `18:40:11.027`
- log child id request: `18:40:11.043`
- log child id response: `18:40:11.071`
- parent ipv6: `n/a`
- parent extaddr: `ee4c91992d52d2c6`
- parent rloc16: `0xe000`
- child extaddr: `caf4f31a4aabef0b`
- timing source: **unavailable**
- complete log attach: **True**
- complete pcap attach: **False**
- Request -> Response: **None ms**
- Response -> Child ID Request: **None ms**
- Child ID Request -> Response: **None ms**
- Full Attach: **None ms**

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260714-184613-run17.log`

- manifest status: `completed`
- child extaddr: `1220854378184d75`
- switch target extaddr(s): `8af1062b0cf67393, 8af1062b0cf67393, 8af1062b0cf67393`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `abe7749db0a80d7aae137aa33655e374716f9b446f15c477f2efc545c83e9e3d` |
| fast unicast Parent Response marker | `True` |
| expected for variant | `True` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `86a90c296d14a0d1`
- parent rloc16: `n/a`
- child extaddr: `1220854378184d75`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **91 ms**
- Response -> Child ID Request: **661 ms**
- Child ID Request -> Response: **13 ms**
- Full Attach: **765 ms**
- pcap parent request: `18:52:04.080` (frame 587)
- pcap parent response: `18:52:04.171` (frame 588)
- pcap child id request: `18:52:04.832` (frame 596)
- pcap child id response: `18:52:04.845` (frame 598)

#### PCAP-complete child attach 2

- log parent request: `18:52:08.590`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `8af1062b0cf67393`
- parent rloc16: `n/a`
- child extaddr: `1220854378184d75`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **9 ms**
- Response -> Child ID Request: **29 ms**
- Child ID Request -> Response: **15 ms**
- Full Attach: **53 ms**
- pcap parent request: `18:52:08.636` (frame 600)
- pcap parent response: `18:52:08.645` (frame 602)
- pcap child id request: `18:52:08.674` (frame 604)
- pcap child id response: `18:52:08.689` (frame 606)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `18:52:08.610`
- log parent response: `18:52:08.623`
- log child id request: `18:52:08.640`
- log child id response: `18:52:08.670`
- parent ipv6: `n/a`
- parent extaddr: `8af1062b0cf67393`
- parent rloc16: `0xe400`
- child extaddr: `1220854378184d75`
- timing source: **unavailable**
- complete log attach: **True**
- complete pcap attach: **False**
- Request -> Response: **None ms**
- Response -> Child ID Request: **None ms**
- Child ID Request -> Response: **None ms**
- Full Attach: **None ms**

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260714-185811-run18.log`

- manifest status: `completed`
- child extaddr: `66aea295229a7f73`
- switch target extaddr(s): `12e395c1fbc3cdc9, 12e395c1fbc3cdc9, 12e395c1fbc3cdc9`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `abe7749db0a80d7aae137aa33655e374716f9b446f15c477f2efc545c83e9e3d` |
| fast unicast Parent Response marker | `True` |
| expected for variant | `True` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `0ab217bed24fa38f`
- parent rloc16: `n/a`
- child extaddr: `66aea295229a7f73`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **83 ms**
- Response -> Child ID Request: **668 ms**
- Child ID Request -> Response: **14 ms**
- Full Attach: **765 ms**
- pcap parent request: `19:04:01.720` (frame 630)
- pcap parent response: `19:04:01.803` (frame 631)
- pcap child id request: `19:04:02.471` (frame 639)
- pcap child id response: `19:04:02.485` (frame 641)

#### PCAP-complete child attach 2

- log parent request: `19:04:06.376`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `12e395c1fbc3cdc9`
- parent rloc16: `n/a`
- child extaddr: `66aea295229a7f73`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **9 ms**
- Response -> Child ID Request: **28 ms**
- Child ID Request -> Response: **14 ms**
- Full Attach: **51 ms**
- pcap parent request: `19:04:06.425` (frame 645)
- pcap parent response: `19:04:06.434` (frame 647)
- pcap child id request: `19:04:06.462` (frame 649)
- pcap child id response: `19:04:06.476` (frame 651)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `19:04:06.395`
- log parent response: `19:04:06.411`
- log child id request: `19:04:06.427`
- log child id response: `19:04:06.456`
- parent ipv6: `n/a`
- parent extaddr: `12e395c1fbc3cdc9`
- parent rloc16: `0xc800`
- child extaddr: `66aea295229a7f73`
- timing source: **unavailable**
- complete log attach: **True**
- complete pcap attach: **False**
- Request -> Response: **None ms**
- Response -> Child ID Request: **None ms**
- Child ID Request -> Response: **None ms**
- Full Attach: **None ms**

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260714-191009-run19.log`

- manifest status: `completed`
- child extaddr: `c28877a0b2eb0020`
- switch target extaddr(s): `e6defbd302299737, e6defbd302299737, e6defbd302299737`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `abe7749db0a80d7aae137aa33655e374716f9b446f15c477f2efc545c83e9e3d` |
| fast unicast Parent Response marker | `True` |
| expected for variant | `True` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `bee77f63d8dd58a6`
- parent rloc16: `n/a`
- child extaddr: `c28877a0b2eb0020`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **70 ms**
- Response -> Child ID Request: **681 ms**
- Child ID Request -> Response: **15 ms**
- Full Attach: **766 ms**
- pcap parent request: `19:15:59.555` (frame 638)
- pcap parent response: `19:15:59.625` (frame 645)
- pcap child id request: `19:16:00.306` (frame 655)
- pcap child id response: `19:16:00.321` (frame 657)

#### PCAP-complete child attach 2

- log parent request: `19:16:03.940`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `e6defbd302299737`
- parent rloc16: `n/a`
- child extaddr: `c28877a0b2eb0020`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **8 ms**
- Response -> Child ID Request: **30 ms**
- Child ID Request -> Response: **13 ms**
- Full Attach: **51 ms**
- pcap parent request: `19:16:03.988` (frame 672)
- pcap parent response: `19:16:03.996` (frame 674)
- pcap child id request: `19:16:04.026` (frame 676)
- pcap child id response: `19:16:04.039` (frame 678)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `19:16:03.959`
- log parent response: `19:16:03.974`
- log child id request: `19:16:03.990`
- log child id response: `19:16:04.020`
- parent ipv6: `n/a`
- parent extaddr: `e6defbd302299737`
- parent rloc16: `0xbc00`
- child extaddr: `c28877a0b2eb0020`
- timing source: **unavailable**
- complete log attach: **True**
- complete pcap attach: **False**
- Request -> Response: **None ms**
- Response -> Child ID Request: **None ms**
- Child ID Request -> Response: **None ms**
- Full Attach: **None ms**

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260714-192206-run20.log`

- manifest status: `completed`
- child extaddr: `02c9c87142d611b8`
- switch target extaddr(s): `6662f612aa47a245, 6662f612aa47a245, 6662f612aa47a245`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `abe7749db0a80d7aae137aa33655e374716f9b446f15c477f2efc545c83e9e3d` |
| fast unicast Parent Response marker | `True` |
| expected for variant | `True` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `4af8ce9a46f8b239`
- parent rloc16: `n/a`
- child extaddr: `02c9c87142d611b8`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **375 ms**
- Response -> Child ID Request: **377 ms**
- Child ID Request -> Response: **12 ms**
- Full Attach: **764 ms**
- pcap parent request: `19:27:57.098` (frame 628)
- pcap parent response: `19:27:57.473` (frame 631)
- pcap child id request: `19:27:57.850` (frame 637)
- pcap child id response: `19:27:57.862` (frame 639)

#### PCAP-complete child attach 2

- log parent request: `19:28:01.616`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `6662f612aa47a245`
- parent rloc16: `n/a`
- child extaddr: `02c9c87142d611b8`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **9 ms**
- Response -> Child ID Request: **29 ms**
- Child ID Request -> Response: **14 ms**
- Full Attach: **52 ms**
- pcap parent request: `19:28:01.665` (frame 641)
- pcap parent response: `19:28:01.674` (frame 643)
- pcap child id request: `19:28:01.703` (frame 645)
- pcap child id response: `19:28:01.717` (frame 647)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `19:28:01.635`
- log parent response: `19:28:01.651`
- log child id request: `19:28:01.667`
- log child id response: `19:28:01.698`
- parent ipv6: `n/a`
- parent extaddr: `6662f612aa47a245`
- parent rloc16: `0x3000`
- child extaddr: `02c9c87142d611b8`
- timing source: **unavailable**
- complete log attach: **True**
- complete pcap attach: **False**
- Request -> Response: **None ms**
- Response -> Child ID Request: **None ms**
- Child ID Request -> Response: **None ms**
- Full Attach: **None ms**

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260714-193404-run21.log`

- manifest status: `completed`
- child extaddr: `1ec66cff4dc6a77d`
- switch target extaddr(s): `6ea0cd64245141a5, 6ea0cd64245141a5, 6ea0cd64245141a5`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `abe7749db0a80d7aae137aa33655e374716f9b446f15c477f2efc545c83e9e3d` |
| fast unicast Parent Response marker | `True` |
| expected for variant | `True` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `1687dc02e65cb9a5`
- parent rloc16: `n/a`
- child extaddr: `1ec66cff4dc6a77d`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **27 ms**
- Response -> Child ID Request: **725 ms**
- Child ID Request -> Response: **14 ms**
- Full Attach: **766 ms**
- pcap parent request: `19:39:54.817` (frame 583)
- pcap parent response: `19:39:54.844` (frame 584)
- pcap child id request: `19:39:55.569` (frame 592)
- pcap child id response: `19:39:55.583` (frame 594)

#### PCAP-complete child attach 2

- log parent request: `19:39:59.094`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `6ea0cd64245141a5`
- parent rloc16: `n/a`
- child extaddr: `1ec66cff4dc6a77d`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **35 ms**
- Response -> Child ID Request: **26 ms**
- Child ID Request -> Response: **14 ms**
- Full Attach: **75 ms**
- pcap parent request: `19:39:59.143` (frame 616)
- pcap parent response: `19:39:59.178` (frame 622)
- pcap child id request: `19:39:59.204` (frame 626)
- pcap child id response: `19:39:59.218` (frame 630)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `19:39:59.113`
- log parent response: `19:39:59.156`
- log child id request: `19:39:59.171`
- log child id response: `19:39:59.199`
- parent ipv6: `n/a`
- parent extaddr: `6ea0cd64245141a5`
- parent rloc16: `0x6400`
- child extaddr: `1ec66cff4dc6a77d`
- timing source: **unavailable**
- complete log attach: **True**
- complete pcap attach: **False**
- Request -> Response: **None ms**
- Response -> Child ID Request: **None ms**
- Child ID Request -> Response: **None ms**
- Full Attach: **None ms**

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260714-194601-run22.log`

- manifest status: `completed`
- child extaddr: `3edc7ed0c883c509`
- switch target extaddr(s): `1a93b17afeaad72c, 1a93b17afeaad72c, 1a93b17afeaad72c`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `abe7749db0a80d7aae137aa33655e374716f9b446f15c477f2efc545c83e9e3d` |
| fast unicast Parent Response marker | `True` |
| expected for variant | `True` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `8e2535ba1b3ac7ec`
- parent rloc16: `n/a`
- child extaddr: `3edc7ed0c883c509`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **26 ms**
- Response -> Child ID Request: **728 ms**
- Child ID Request -> Response: **12 ms**
- Full Attach: **766 ms**
- pcap parent request: `19:51:52.764` (frame 599)
- pcap parent response: `19:51:52.790` (frame 600)
- pcap child id request: `19:51:53.518` (frame 608)
- pcap child id response: `19:51:53.530` (frame 610)

#### PCAP-complete child attach 2

- log parent request: `19:51:56.812`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `1a93b17afeaad72c`
- parent rloc16: `n/a`
- child extaddr: `3edc7ed0c883c509`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **8 ms**
- Response -> Child ID Request: **26 ms**
- Child ID Request -> Response: **13 ms**
- Full Attach: **47 ms**
- pcap parent request: `19:51:56.858` (frame 613)
- pcap parent response: `19:51:56.866` (frame 615)
- pcap child id request: `19:51:56.892` (frame 617)
- pcap child id response: `19:51:56.905` (frame 619)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `19:51:56.829`
- log parent response: `19:51:56.844`
- log child id request: `19:51:56.859`
- log child id response: `19:51:56.886`
- parent ipv6: `n/a`
- parent extaddr: `1a93b17afeaad72c`
- parent rloc16: `0x5c00`
- child extaddr: `3edc7ed0c883c509`
- timing source: **unavailable**
- complete log attach: **True**
- complete pcap attach: **False**
- Request -> Response: **None ms**
- Response -> Child ID Request: **None ms**
- Child ID Request -> Response: **None ms**
- Full Attach: **None ms**

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260714-195759-run23.log`

- manifest status: `completed`
- child extaddr: `027ba31481534fc7`
- switch target extaddr(s): `321d0f2bd4eb08d1, 321d0f2bd4eb08d1, 321d0f2bd4eb08d1`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `abe7749db0a80d7aae137aa33655e374716f9b446f15c477f2efc545c83e9e3d` |
| fast unicast Parent Response marker | `True` |
| expected for variant | `True` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `d61163bdbf59f1c1`
- parent rloc16: `n/a`
- child extaddr: `027ba31481534fc7`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **229 ms**
- Response -> Child ID Request: **522 ms**
- Child ID Request -> Response: **15 ms**
- Full Attach: **766 ms**
- pcap parent request: `20:03:50.339` (frame 632)
- pcap parent response: `20:03:50.568` (frame 651)
- pcap child id request: `20:03:51.090` (frame 658)
- pcap child id response: `20:03:51.105` (frame 660)

#### PCAP-complete child attach 2

- log parent request: `20:03:54.403`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `321d0f2bd4eb08d1`
- parent rloc16: `n/a`
- child extaddr: `027ba31481534fc7`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **9 ms**
- Response -> Child ID Request: **28 ms**
- Child ID Request -> Response: **13 ms**
- Full Attach: **50 ms**
- pcap parent request: `20:03:54.449` (frame 663)
- pcap parent response: `20:03:54.458` (frame 665)
- pcap child id request: `20:03:54.486` (frame 667)
- pcap child id response: `20:03:54.499` (frame 669)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `20:03:54.423`
- log parent response: `20:03:54.437`
- log child id request: `20:03:54.453`
- log child id response: `20:03:54.481`
- parent ipv6: `n/a`
- parent extaddr: `321d0f2bd4eb08d1`
- parent rloc16: `0xe000`
- child extaddr: `027ba31481534fc7`
- timing source: **unavailable**
- complete log attach: **True**
- complete pcap attach: **False**
- Request -> Response: **None ms**
- Response -> Child ID Request: **None ms**
- Child ID Request -> Response: **None ms**
- Full Attach: **None ms**

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260714-200957-run24.log`

- manifest status: `completed`
- child extaddr: `3e63b531f19ad908`
- switch target extaddr(s): `4645628615dd0f95, 4645628615dd0f95, 4645628615dd0f95`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/ucast_fastpr/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `abe7749db0a80d7aae137aa33655e374716f9b446f15c477f2efc545c83e9e3d` |
| fast unicast Parent Response marker | `True` |
| expected for variant | `True` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `daeb18163003dd39`
- parent rloc16: `n/a`
- child extaddr: `3e63b531f19ad908`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **77 ms**
- Response -> Child ID Request: **675 ms**
- Child ID Request -> Response: **14 ms**
- Full Attach: **766 ms**
- pcap parent request: `20:15:47.821` (frame 625)
- pcap parent response: `20:15:47.898` (frame 626)
- pcap child id request: `20:15:48.573` (frame 634)
- pcap child id response: `20:15:48.587` (frame 636)

#### PCAP-complete child attach 2

- log parent request: `20:15:51.989`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `4645628615dd0f95`
- parent rloc16: `n/a`
- child extaddr: `3e63b531f19ad908`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **8 ms**
- Response -> Child ID Request: **26 ms**
- Child ID Request -> Response: **14 ms**
- Full Attach: **48 ms**
- pcap parent request: `20:15:52.035` (frame 638)
- pcap parent response: `20:15:52.043` (frame 640)
- pcap child id request: `20:15:52.069` (frame 642)
- pcap child id response: `20:15:52.083` (frame 644)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `20:15:52.007`
- log parent response: `20:15:52.022`
- log child id request: `20:15:52.036`
- log child id response: `20:15:52.065`
- parent ipv6: `n/a`
- parent extaddr: `4645628615dd0f95`
- parent rloc16: `0xb400`
- child extaddr: `3e63b531f19ad908`
- timing source: **unavailable**
- complete log attach: **True**
- complete pcap attach: **False**
- Request -> Response: **None ms**
- Response -> Child ID Request: **None ms**
- Child ID Request -> Response: **None ms**
- Full Attach: **None ms**

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**
