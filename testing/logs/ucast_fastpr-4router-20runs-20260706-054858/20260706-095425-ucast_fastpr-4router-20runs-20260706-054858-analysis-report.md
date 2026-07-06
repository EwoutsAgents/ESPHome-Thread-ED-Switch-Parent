# Child Log Analysis

## ucast_fastpr_child

Files analyzed: **20**

- batch folders: `ucast_fastpr-4router-20runs-20260706-054858`

### PCAP-complete child attach summary

| Attach | Metric | M (SD), ms | n |
| --- | --- | ---: | ---: |
| 1 | Request -> Response | 106.55 (99.08) | 20 |
| 1 | Response -> Child ID Request | 645.85 (99.10) | 20 |
| 1 | Child ID Request -> Response | 14.20 (1.28) | 20 |
| 1 | Full Attach | 766.60 (1.64) | 20 |
| 2 | Request -> Response | 8.70 (0.86) | 20 |
| 2 | Response -> Child ID Request | 29.55 (1.00) | 20 |
| 2 | Child ID Request -> Response | 14.30 (1.13) | 20 |
| 2 | Full Attach | 52.55 (1.88) | 20 |

| Metric | M (SD) | n |
| --- | ---: | ---: |
| Failed TX Attempts per Log | 0.00 (0.00) | 20 |
| Log-only or Partial Sequences per Log | 1.00 (0.00) | 20 |

### `ucast_fastpr_child_20260706-055507-run01.log`

- manifest status: `completed`
- child extaddr: `9e26c13986962d45`
- switch target extaddr(s): `ea6598b0af79c8b9, ea6598b0af79c8b9, ea6598b0af79c8b9`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `8631a7444b60c749`
- parent rloc16: `n/a`
- child extaddr: `9e26c13986962d45`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **45 ms**
- Response -> Child ID Request: **705 ms**
- Child ID Request -> Response: **14 ms**
- Full Attach: **764 ms**
- pcap parent request: `06:00:57.373` (frame 1013)
- pcap parent response: `06:00:57.418` (frame 1014)
- pcap child id request: `06:00:58.123` (frame 1022)
- pcap child id response: `06:00:58.137` (frame 1024)

#### PCAP-complete child attach 2

- log parent request: `06:01:01.362`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `ea6598b0af79c8b9`
- parent rloc16: `n/a`
- child extaddr: `9e26c13986962d45`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **8 ms**
- Response -> Child ID Request: **27 ms**
- Child ID Request -> Response: **15 ms**
- Full Attach: **50 ms**
- pcap parent request: `06:01:01.407` (frame 1026)
- pcap parent response: `06:01:01.415` (frame 1028)
- pcap child id request: `06:01:01.442` (frame 1030)
- pcap child id response: `06:01:01.457` (frame 1032)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `06:01:01.380`
- log parent response: `06:01:01.395`
- log child id request: `06:01:01.410`
- log child id response: `06:01:01.439`
- parent ipv6: `n/a`
- parent extaddr: `ea6598b0af79c8b9`
- parent rloc16: `0xf400`
- child extaddr: `9e26c13986962d45`
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

### `ucast_fastpr_child_20260706-060704-run02.log`

- manifest status: `completed`
- child extaddr: `1213b10887549a83`
- switch target extaddr(s): `c61b5598a0b26b45, c61b5598a0b26b45, c61b5598a0b26b45`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `86672d46e4973e19`
- parent rloc16: `n/a`
- child extaddr: `1213b10887549a83`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **52 ms**
- Response -> Child ID Request: **702 ms**
- Child ID Request -> Response: **13 ms**
- Full Attach: **767 ms**
- pcap parent request: `06:12:54.271` (frame 1095)
- pcap parent response: `06:12:54.323` (frame 1096)
- pcap child id request: `06:12:55.025` (frame 1104)
- pcap child id response: `06:12:55.038` (frame 1106)

#### PCAP-complete child attach 2

- log parent request: `06:12:58.239`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `c61b5598a0b26b45`
- parent rloc16: `n/a`
- child extaddr: `1213b10887549a83`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **8 ms**
- Response -> Child ID Request: **30 ms**
- Child ID Request -> Response: **13 ms**
- Full Attach: **51 ms**
- pcap parent request: `06:12:58.282` (frame 1129)
- pcap parent response: `06:12:58.290` (frame 1131)
- pcap child id request: `06:12:58.320` (frame 1133)
- pcap child id response: `06:12:58.333` (frame 1135)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `06:12:58.257`
- log parent response: `06:12:58.272`
- log child id request: `06:12:58.287`
- log child id response: `06:12:58.316`
- parent ipv6: `n/a`
- parent extaddr: `c61b5598a0b26b45`
- parent rloc16: `0x8000`
- child extaddr: `1213b10887549a83`
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

### `ucast_fastpr_child_20260706-061900-run03.log`

- manifest status: `completed`
- child extaddr: `d23d3691e49bdfa3`
- switch target extaddr(s): `2a258f640c7b3eb7, 2a258f640c7b3eb7, 2a258f640c7b3eb7`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `1efd69ca73cc44b1`
- parent rloc16: `n/a`
- child extaddr: `d23d3691e49bdfa3`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **22 ms**
- Response -> Child ID Request: **730 ms**
- Child ID Request -> Response: **14 ms**
- Full Attach: **766 ms**
- pcap parent request: `06:24:51.148` (frame 845)
- pcap parent response: `06:24:51.170` (frame 846)
- pcap child id request: `06:24:51.900` (frame 854)
- pcap child id response: `06:24:51.914` (frame 856)

#### PCAP-complete child attach 2

- log parent request: `06:24:55.081`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `2a258f640c7b3eb7`
- parent rloc16: `n/a`
- child extaddr: `d23d3691e49bdfa3`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **8 ms**
- Response -> Child ID Request: **30 ms**
- Child ID Request -> Response: **14 ms**
- Full Attach: **52 ms**
- pcap parent request: `06:24:55.127` (frame 859)
- pcap parent response: `06:24:55.135` (frame 861)
- pcap child id request: `06:24:55.165` (frame 863)
- pcap child id response: `06:24:55.179` (frame 865)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `06:24:55.100`
- log parent response: `06:24:55.115`
- log child id request: `06:24:55.131`
- log child id response: `06:24:55.161`
- parent ipv6: `n/a`
- parent extaddr: `2a258f640c7b3eb7`
- parent rloc16: `0xbc00`
- child extaddr: `d23d3691e49bdfa3`
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

### `ucast_fastpr_child_20260706-063057-run04.log`

- manifest status: `completed`
- child extaddr: `8eb69ce6839699aa`
- switch target extaddr(s): `f68b57611f7e40af, f68b57611f7e40af, f68b57611f7e40af`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `ae90db1d9ef3e2fc`
- parent rloc16: `n/a`
- child extaddr: `8eb69ce6839699aa`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **58 ms**
- Response -> Child ID Request: **696 ms**
- Child ID Request -> Response: **12 ms**
- Full Attach: **766 ms**
- pcap parent request: `06:36:47.897` (frame 465)
- pcap parent response: `06:36:47.955` (frame 466)
- pcap child id request: `06:36:48.651` (frame 474)
- pcap child id response: `06:36:48.663` (frame 476)

#### PCAP-complete child attach 2

- log parent request: `06:36:51.840`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `f68b57611f7e40af`
- parent rloc16: `n/a`
- child extaddr: `8eb69ce6839699aa`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **7 ms**
- Response -> Child ID Request: **28 ms**
- Child ID Request -> Response: **13 ms**
- Full Attach: **48 ms**
- pcap parent request: `06:36:51.884` (frame 479)
- pcap parent response: `06:36:51.891` (frame 481)
- pcap child id request: `06:36:51.919` (frame 483)
- pcap child id response: `06:36:51.932` (frame 485)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `06:36:51.858`
- log parent response: `06:36:51.873`
- log child id request: `06:36:51.887`
- log child id response: `06:36:51.915`
- parent ipv6: `n/a`
- parent extaddr: `f68b57611f7e40af`
- parent rloc16: `0x5c00`
- child extaddr: `8eb69ce6839699aa`
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

### `ucast_fastpr_child_20260706-064254-run05.log`

- manifest status: `completed`
- child extaddr: `66148b0d7d6e6313`
- switch target extaddr(s): `16991a483542b028, 16991a483542b028, 16991a483542b028`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `dab973374656676e`
- parent rloc16: `n/a`
- child extaddr: `66148b0d7d6e6313`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **25 ms**
- Response -> Child ID Request: **728 ms**
- Child ID Request -> Response: **15 ms**
- Full Attach: **768 ms**
- pcap parent request: `06:48:44.239` (frame 512)
- pcap parent response: `06:48:44.264` (frame 513)
- pcap child id request: `06:48:44.992` (frame 521)
- pcap child id response: `06:48:45.007` (frame 523)

#### PCAP-complete child attach 2

- log parent request: `06:48:48.593`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `16991a483542b028`
- parent rloc16: `n/a`
- child extaddr: `66148b0d7d6e6313`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **9 ms**
- Response -> Child ID Request: **29 ms**
- Child ID Request -> Response: **13 ms**
- Full Attach: **51 ms**
- pcap parent request: `06:48:48.637` (frame 525)
- pcap parent response: `06:48:48.646` (frame 527)
- pcap child id request: `06:48:48.675` (frame 529)
- pcap child id response: `06:48:48.688` (frame 531)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `06:48:48.611`
- log parent response: `06:48:48.627`
- log child id request: `06:48:48.642`
- log child id response: `06:48:48.671`
- parent ipv6: `n/a`
- parent extaddr: `16991a483542b028`
- parent rloc16: `0x4400`
- child extaddr: `66148b0d7d6e6313`
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

### `ucast_fastpr_child_20260706-065451-run06.log`

- manifest status: `completed`
- child extaddr: `72080f451d3e37ea`
- switch target extaddr(s): `b242812b85ac3a77, b242812b85ac3a77, b242812b85ac3a77`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `4e719c9301551822`
- parent rloc16: `n/a`
- child extaddr: `72080f451d3e37ea`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **28 ms**
- Response -> Child ID Request: **725 ms**
- Child ID Request -> Response: **15 ms**
- Full Attach: **768 ms**
- pcap parent request: `07:00:40.954` (frame 233)
- pcap parent response: `07:00:40.982` (frame 234)
- pcap child id request: `07:00:41.707` (frame 242)
- pcap child id response: `07:00:41.722` (frame 244)

#### PCAP-complete child attach 2

- log parent request: `07:00:45.521`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `b242812b85ac3a77`
- parent rloc16: `n/a`
- child extaddr: `72080f451d3e37ea`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **8 ms**
- Response -> Child ID Request: **31 ms**
- Child ID Request -> Response: **16 ms**
- Full Attach: **55 ms**
- pcap parent request: `07:00:45.570` (frame 246)
- pcap parent response: `07:00:45.578` (frame 248)
- pcap child id request: `07:00:45.609` (frame 250)
- pcap child id response: `07:00:45.625` (frame 252)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `07:00:45.540`
- log parent response: `07:00:45.557`
- log child id request: `07:00:45.573`
- log child id response: `07:00:45.606`
- parent ipv6: `n/a`
- parent extaddr: `b242812b85ac3a77`
- parent rloc16: `0x1800`
- child extaddr: `72080f451d3e37ea`
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

### `ucast_fastpr_child_20260706-070648-run07.log`

- manifest status: `completed`
- child extaddr: `e6245d66b4563c1f`
- switch target extaddr(s): `ee697b50425319ec, ee697b50425319ec, ee697b50425319ec`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `62b6ab32898750e4`
- parent rloc16: `n/a`
- child extaddr: `e6245d66b4563c1f`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **243 ms**
- Response -> Child ID Request: **508 ms**
- Child ID Request -> Response: **13 ms**
- Full Attach: **764 ms**
- pcap parent request: `07:12:38.301` (frame 460)
- pcap parent response: `07:12:38.544` (frame 461)
- pcap child id request: `07:12:39.052` (frame 469)
- pcap child id response: `07:12:39.065` (frame 471)

#### PCAP-complete child attach 2

- log parent request: `07:12:42.286`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `ee697b50425319ec`
- parent rloc16: `n/a`
- child extaddr: `e6245d66b4563c1f`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **7 ms**
- Response -> Child ID Request: **30 ms**
- Child ID Request -> Response: **14 ms**
- Full Attach: **51 ms**
- pcap parent request: `07:12:42.334` (frame 473)
- pcap parent response: `07:12:42.341` (frame 475)
- pcap child id request: `07:12:42.371` (frame 477)
- pcap child id response: `07:12:42.385` (frame 479)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `07:12:42.304`
- log parent response: `07:12:42.320`
- log child id request: `07:12:42.335`
- log child id response: `07:12:42.365`
- parent ipv6: `n/a`
- parent extaddr: `ee697b50425319ec`
- parent rloc16: `0x1400`
- child extaddr: `e6245d66b4563c1f`
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

### `ucast_fastpr_child_20260706-071844-run08.log`

- manifest status: `completed`
- child extaddr: `1ea04a680136e873`
- switch target extaddr(s): `a6584058a5c8deba, a6584058a5c8deba, a6584058a5c8deba`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `26cbe5fa2a6db3e4`
- parent rloc16: `n/a`
- child extaddr: `1ea04a680136e873`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **105 ms**
- Response -> Child ID Request: **647 ms**
- Child ID Request -> Response: **14 ms**
- Full Attach: **766 ms**
- pcap parent request: `07:24:34.845` (frame 188)
- pcap parent response: `07:24:34.950` (frame 189)
- pcap child id request: `07:24:35.597` (frame 197)
- pcap child id response: `07:24:35.611` (frame 199)

#### PCAP-complete child attach 2

- log parent request: `07:24:39.022`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `a6584058a5c8deba`
- parent rloc16: `n/a`
- child extaddr: `1ea04a680136e873`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **9 ms**
- Response -> Child ID Request: **29 ms**
- Child ID Request -> Response: **15 ms**
- Full Attach: **53 ms**
- pcap parent request: `07:24:39.069` (frame 201)
- pcap parent response: `07:24:39.078` (frame 203)
- pcap child id request: `07:24:39.107` (frame 205)
- pcap child id response: `07:24:39.122` (frame 207)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `07:24:39.041`
- log parent response: `07:24:39.056`
- log child id request: `07:24:39.073`
- log child id response: `07:24:39.102`
- parent ipv6: `n/a`
- parent extaddr: `a6584058a5c8deba`
- parent rloc16: `0x1c00`
- child extaddr: `1ea04a680136e873`
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

### `ucast_fastpr_child_20260706-073041-run09.log`

- manifest status: `completed`
- child extaddr: `7e8f38ab578218e6`
- switch target extaddr(s): `06ccf1fd9e51d4b9, 06ccf1fd9e51d4b9, 06ccf1fd9e51d4b9`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `5a97bc3d675bb1d9`
- parent rloc16: `n/a`
- child extaddr: `7e8f38ab578218e6`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **91 ms**
- Response -> Child ID Request: **661 ms**
- Child ID Request -> Response: **17 ms**
- Full Attach: **769 ms**
- pcap parent request: `07:36:31.889` (frame 799)
- pcap parent response: `07:36:31.980` (frame 800)
- pcap child id request: `07:36:32.641` (frame 808)
- pcap child id response: `07:36:32.658` (frame 811)

#### PCAP-complete child attach 2

- log parent request: `07:36:36.057`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `06ccf1fd9e51d4b9`
- parent rloc16: `n/a`
- child extaddr: `7e8f38ab578218e6`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **9 ms**
- Response -> Child ID Request: **30 ms**
- Child ID Request -> Response: **16 ms**
- Full Attach: **55 ms**
- pcap parent request: `07:36:36.102` (frame 814)
- pcap parent response: `07:36:36.111` (frame 816)
- pcap child id request: `07:36:36.141` (frame 818)
- pcap child id response: `07:36:36.157` (frame 820)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `07:36:36.077`
- log parent response: `07:36:36.090`
- log child id request: `07:36:36.107`
- log child id response: `07:36:36.138`
- parent ipv6: `n/a`
- parent extaddr: `06ccf1fd9e51d4b9`
- parent rloc16: `0x1000`
- child extaddr: `7e8f38ab578218e6`
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

### `ucast_fastpr_child_20260706-074238-run10.log`

- manifest status: `completed`
- child extaddr: `9ef7d9aa44307ed2`
- switch target extaddr(s): `5a772946a45ec1d1, 5a772946a45ec1d1, 5a772946a45ec1d1`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `aeb5f37a207b273c`
- parent rloc16: `n/a`
- child extaddr: `9ef7d9aa44307ed2`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **58 ms**
- Response -> Child ID Request: **694 ms**
- Child ID Request -> Response: **16 ms**
- Full Attach: **768 ms**
- pcap parent request: `07:48:28.202` (frame 937)
- pcap parent response: `07:48:28.260` (frame 938)
- pcap child id request: `07:48:28.954` (frame 947)
- pcap child id response: `07:48:28.970` (frame 949)

#### PCAP-complete child attach 2

- log parent request: `07:48:32.801`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `5a772946a45ec1d1`
- parent rloc16: `n/a`
- child extaddr: `9ef7d9aa44307ed2`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **9 ms**
- Response -> Child ID Request: **29 ms**
- Child ID Request -> Response: **15 ms**
- Full Attach: **53 ms**
- pcap parent request: `07:48:32.845` (frame 952)
- pcap parent response: `07:48:32.854` (frame 954)
- pcap child id request: `07:48:32.883` (frame 956)
- pcap child id response: `07:48:32.898` (frame 958)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `07:48:32.821`
- log parent response: `07:48:32.834`
- log child id request: `07:48:32.851`
- log child id response: `07:48:32.880`
- parent ipv6: `n/a`
- parent extaddr: `5a772946a45ec1d1`
- parent rloc16: `0x7800`
- child extaddr: `9ef7d9aa44307ed2`
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

### `ucast_fastpr_child_20260706-075435-run11.log`

- manifest status: `completed`
- child extaddr: `d2f7a7e063165819`
- switch target extaddr(s): `96d7deb75464a36d, 96d7deb75464a36d, 96d7deb75464a36d`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `ce6851f8474751d4`
- parent rloc16: `n/a`
- child extaddr: `d2f7a7e063165819`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **221 ms**
- Response -> Child ID Request: **532 ms**
- Child ID Request -> Response: **15 ms**
- Full Attach: **768 ms**
- pcap parent request: `08:00:25.457` (frame 207)
- pcap parent response: `08:00:25.678` (frame 208)
- pcap child id request: `08:00:26.210` (frame 216)
- pcap child id response: `08:00:26.225` (frame 218)

#### PCAP-complete child attach 2

- log parent request: `08:00:29.456`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `96d7deb75464a36d`
- parent rloc16: `n/a`
- child extaddr: `d2f7a7e063165819`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **9 ms**
- Response -> Child ID Request: **29 ms**
- Child ID Request -> Response: **14 ms**
- Full Attach: **52 ms**
- pcap parent request: `08:00:29.500` (frame 221)
- pcap parent response: `08:00:29.509` (frame 223)
- pcap child id request: `08:00:29.538` (frame 225)
- pcap child id response: `08:00:29.552` (frame 227)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `08:00:29.473`
- log parent response: `08:00:29.490`
- log child id request: `08:00:29.504`
- log child id response: `08:00:29.534`
- parent ipv6: `n/a`
- parent extaddr: `96d7deb75464a36d`
- parent rloc16: `0xb800`
- child extaddr: `d2f7a7e063165819`
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

### `ucast_fastpr_child_20260706-080632-run12.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `3e1368d7767fb5b4`
- switch target extaddr(s): `b252a370a3d6c7ac, b252a370a3d6c7ac, b252a370a3d6c7ac`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `46801e2b517b87fc`
- parent rloc16: `n/a`
- child extaddr: `3e1368d7767fb5b4`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **126 ms**
- Response -> Child ID Request: **626 ms**
- Child ID Request -> Response: **14 ms**
- Full Attach: **766 ms**
- pcap parent request: `08:12:21.748` (frame 457)
- pcap parent response: `08:12:21.874` (frame 458)
- pcap child id request: `08:12:22.500` (frame 467)
- pcap child id response: `08:12:22.514` (frame 469)

#### PCAP-complete child attach 2

- log parent request: `08:12:26.372`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `b252a370a3d6c7ac`
- parent rloc16: `n/a`
- child extaddr: `3e1368d7767fb5b4`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **10 ms**
- Response -> Child ID Request: **29 ms**
- Child ID Request -> Response: **16 ms**
- Full Attach: **55 ms**
- pcap parent request: `08:12:26.417` (frame 472)
- pcap parent response: `08:12:26.427` (frame 474)
- pcap child id request: `08:12:26.456` (frame 476)
- pcap child id response: `08:12:26.472` (frame 478)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `08:12:26.390`
- log parent response: `08:12:26.407`
- log child id request: `08:12:26.422`
- log child id response: `08:12:26.454`
- parent ipv6: `n/a`
- parent extaddr: `b252a370a3d6c7ac`
- parent rloc16: `0xb000`
- child extaddr: `3e1368d7767fb5b4`
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

### `ucast_fastpr_child_20260706-081828-run13.log`

- manifest status: `completed`
- child extaddr: `3a48faff6894ad7d`
- switch target extaddr(s): `eeac073cd03fc2c8, eeac073cd03fc2c8, eeac073cd03fc2c8`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `c6654450fa7a6e2c`
- parent rloc16: `n/a`
- child extaddr: `3a48faff6894ad7d`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **120 ms**
- Response -> Child ID Request: **632 ms**
- Child ID Request -> Response: **13 ms**
- Full Attach: **765 ms**
- pcap parent request: `08:24:18.921` (frame 171)
- pcap parent response: `08:24:19.041` (frame 172)
- pcap child id request: `08:24:19.673` (frame 181)
- pcap child id response: `08:24:19.686` (frame 183)

#### PCAP-complete child attach 2

- log parent request: `08:24:23.200`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `eeac073cd03fc2c8`
- parent rloc16: `n/a`
- child extaddr: `3a48faff6894ad7d`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **8 ms**
- Response -> Child ID Request: **31 ms**
- Child ID Request -> Response: **14 ms**
- Full Attach: **53 ms**
- pcap parent request: `08:24:23.245` (frame 185)
- pcap parent response: `08:24:23.253` (frame 187)
- pcap child id request: `08:24:23.284` (frame 189)
- pcap child id response: `08:24:23.298` (frame 191)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `08:24:23.220`
- log parent response: `08:24:23.233`
- log child id request: `08:24:23.249`
- log child id response: `08:24:23.279`
- parent ipv6: `n/a`
- parent extaddr: `eeac073cd03fc2c8`
- parent rloc16: `0xe000`
- child extaddr: `3a48faff6894ad7d`
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

### `ucast_fastpr_child_20260706-083025-run14.log`

- manifest status: `completed`
- child extaddr: `8e1fbb18f13ff688`
- switch target extaddr(s): `82fb74dcdb8213d9, 82fb74dcdb8213d9, 82fb74dcdb8213d9`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `5a3845a1268f516c`
- parent rloc16: `n/a`
- child extaddr: `8e1fbb18f13ff688`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **20 ms**
- Response -> Child ID Request: **731 ms**
- Child ID Request -> Response: **15 ms**
- Full Attach: **766 ms**
- pcap parent request: `08:36:15.451` (frame 230)
- pcap parent response: `08:36:15.471` (frame 231)
- pcap child id request: `08:36:16.202` (frame 239)
- pcap child id response: `08:36:16.217` (frame 241)

#### PCAP-complete child attach 2

- log parent request: `08:36:19.986`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `82fb74dcdb8213d9`
- parent rloc16: `n/a`
- child extaddr: `8e1fbb18f13ff688`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **9 ms**
- Response -> Child ID Request: **30 ms**
- Child ID Request -> Response: **12 ms**
- Full Attach: **51 ms**
- pcap parent request: `08:36:20.033` (frame 245)
- pcap parent response: `08:36:20.042` (frame 247)
- pcap child id request: `08:36:20.072` (frame 249)
- pcap child id response: `08:36:20.084` (frame 251)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `08:36:20.006`
- log parent response: `08:36:20.021`
- log child id request: `08:36:20.037`
- log child id response: `08:36:20.065`
- parent ipv6: `n/a`
- parent extaddr: `82fb74dcdb8213d9`
- parent rloc16: `0xe800`
- child extaddr: `8e1fbb18f13ff688`
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

### `ucast_fastpr_child_20260706-084222-run15.log`

- manifest status: `completed`
- child extaddr: `1e8d46ee9e6b825e`
- switch target extaddr(s): `d65ecc339dba56c3, d65ecc339dba56c3, d65ecc339dba56c3`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `4a3fbcbd0922e982`
- parent rloc16: `n/a`
- child extaddr: `1e8d46ee9e6b825e`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **42 ms**
- Response -> Child ID Request: **711 ms**
- Child ID Request -> Response: **13 ms**
- Full Attach: **766 ms**
- pcap parent request: `08:48:12.587` (frame 811)
- pcap parent response: `08:48:12.629` (frame 812)
- pcap child id request: `08:48:13.340` (frame 820)
- pcap child id response: `08:48:13.353` (frame 822)

#### PCAP-complete child attach 2

- log parent request: `08:48:16.698`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `d65ecc339dba56c3`
- parent rloc16: `n/a`
- child extaddr: `1e8d46ee9e6b825e`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **9 ms**
- Response -> Child ID Request: **29 ms**
- Child ID Request -> Response: **15 ms**
- Full Attach: **53 ms**
- pcap parent request: `08:48:16.745` (frame 824)
- pcap parent response: `08:48:16.754` (frame 826)
- pcap child id request: `08:48:16.783` (frame 828)
- pcap child id response: `08:48:16.798` (frame 830)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `08:48:16.718`
- log parent response: `08:48:16.733`
- log child id request: `08:48:16.749`
- log child id response: `08:48:16.779`
- parent ipv6: `n/a`
- parent extaddr: `d65ecc339dba56c3`
- parent rloc16: `0xac00`
- child extaddr: `1e8d46ee9e6b825e`
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

### `ucast_fastpr_child_20260706-085419-run16.log`

- manifest status: `completed`
- child extaddr: `f6af8a7e498bea30`
- switch target extaddr(s): `d60529f83bcda75f, d60529f83bcda75f, d60529f83bcda75f`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `d6e6e6c503e7e7ea`
- parent rloc16: `n/a`
- child extaddr: `f6af8a7e498bea30`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **380 ms**
- Response -> Child ID Request: **371 ms**
- Child ID Request -> Response: **16 ms**
- Full Attach: **767 ms**
- pcap parent request: `09:00:09.551` (frame 228)
- pcap parent response: `09:00:09.931` (frame 230)
- pcap child id request: `09:00:10.302` (frame 238)
- pcap child id response: `09:00:10.318` (frame 240)

#### PCAP-complete child attach 2

- log parent request: `09:00:13.503`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `d60529f83bcda75f`
- parent rloc16: `n/a`
- child extaddr: `f6af8a7e498bea30`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **9 ms**
- Response -> Child ID Request: **29 ms**
- Child ID Request -> Response: **14 ms**
- Full Attach: **52 ms**
- pcap parent request: `09:00:13.549` (frame 242)
- pcap parent response: `09:00:13.558` (frame 244)
- pcap child id request: `09:00:13.587` (frame 246)
- pcap child id response: `09:00:13.601` (frame 248)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `09:00:13.521`
- log parent response: `09:00:13.537`
- log child id request: `09:00:13.552`
- log child id response: `09:00:13.582`
- parent ipv6: `n/a`
- parent extaddr: `d60529f83bcda75f`
- parent rloc16: `0xb400`
- child extaddr: `f6af8a7e498bea30`
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

### `ucast_fastpr_child_20260706-090616-run17.log`

- manifest status: `completed`
- child extaddr: `5e082f486342f3c8`
- switch target extaddr(s): `b6b3014098d91ea4, b6b3014098d91ea4, b6b3014098d91ea4`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `120e30b2235c5da5`
- parent rloc16: `n/a`
- child extaddr: `5e082f486342f3c8`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **16 ms**
- Response -> Child ID Request: **735 ms**
- Child ID Request -> Response: **13 ms**
- Full Attach: **764 ms**
- pcap parent request: `09:12:05.973` (frame 1026)
- pcap parent response: `09:12:05.989` (frame 1027)
- pcap child id request: `09:12:06.724` (frame 1035)
- pcap child id response: `09:12:06.737` (frame 1037)

#### PCAP-complete child attach 2

- log parent request: `09:12:10.245`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `b6b3014098d91ea4`
- parent rloc16: `n/a`
- child extaddr: `5e082f486342f3c8`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **9 ms**
- Response -> Child ID Request: **31 ms**
- Child ID Request -> Response: **14 ms**
- Full Attach: **54 ms**
- pcap parent request: `09:12:10.289` (frame 1039)
- pcap parent response: `09:12:10.298` (frame 1041)
- pcap child id request: `09:12:10.329` (frame 1043)
- pcap child id response: `09:12:10.343` (frame 1045)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `09:12:10.264`
- log parent response: `09:12:10.278`
- log child id request: `09:12:10.294`
- log child id response: `09:12:10.325`
- parent ipv6: `n/a`
- parent extaddr: `b6b3014098d91ea4`
- parent rloc16: `0x9000`
- child extaddr: `5e082f486342f3c8`
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

### `ucast_fastpr_child_20260706-091812-run18.log`

- manifest status: `completed`
- child extaddr: `0e6fb97450eb5237`
- switch target extaddr(s): `e26ef5a61b0356f0, e26ef5a61b0356f0, e26ef5a61b0356f0`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `4619c0e9ce4f4261`
- parent rloc16: `n/a`
- child extaddr: `0e6fb97450eb5237`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **64 ms**
- Response -> Child ID Request: **689 ms**
- Child ID Request -> Response: **14 ms**
- Full Attach: **767 ms**
- pcap parent request: `09:24:02.493` (frame 250)
- pcap parent response: `09:24:02.557` (frame 251)
- pcap child id request: `09:24:03.246` (frame 259)
- pcap child id response: `09:24:03.260` (frame 261)

#### PCAP-complete child attach 2

- log parent request: `09:24:06.950`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `e26ef5a61b0356f0`
- parent rloc16: `n/a`
- child extaddr: `0e6fb97450eb5237`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **10 ms**
- Response -> Child ID Request: **30 ms**
- Child ID Request -> Response: **15 ms**
- Full Attach: **55 ms**
- pcap parent request: `09:24:06.994` (frame 264)
- pcap parent response: `09:24:07.004` (frame 266)
- pcap child id request: `09:24:07.034` (frame 268)
- pcap child id response: `09:24:07.049` (frame 270)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `09:24:06.969`
- log parent response: `09:24:06.984`
- log child id request: `09:24:07.001`
- log child id response: `09:24:07.031`
- parent ipv6: `n/a`
- parent extaddr: `e26ef5a61b0356f0`
- parent rloc16: `0x1800`
- child extaddr: `0e6fb97450eb5237`
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

### `ucast_fastpr_child_20260706-093009-run19.log`

- manifest status: `completed`
- child extaddr: `4e6bb49d8d49f7a7`
- switch target extaddr(s): `3e395173f18e0a88, 3e395173f18e0a88, 3e395173f18e0a88`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `bada0fb4f4d12400`
- parent rloc16: `n/a`
- child extaddr: `4e6bb49d8d49f7a7`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **261 ms**
- Response -> Child ID Request: **493 ms**
- Child ID Request -> Response: **13 ms**
- Full Attach: **767 ms**
- pcap parent request: `09:35:59.210` (frame 200)
- pcap parent response: `09:35:59.471` (frame 203)
- pcap child id request: `09:35:59.964` (frame 209)
- pcap child id response: `09:35:59.977` (frame 211)

#### PCAP-complete child attach 2

- log parent request: `09:36:03.780`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `3e395173f18e0a88`
- parent rloc16: `n/a`
- child extaddr: `4e6bb49d8d49f7a7`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **9 ms**
- Response -> Child ID Request: **30 ms**
- Child ID Request -> Response: **15 ms**
- Full Attach: **54 ms**
- pcap parent request: `09:36:03.824` (frame 213)
- pcap parent response: `09:36:03.833` (frame 215)
- pcap child id request: `09:36:03.863` (frame 217)
- pcap child id response: `09:36:03.878` (frame 219)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `09:36:03.798`
- log parent response: `09:36:03.813`
- log child id request: `09:36:03.827`
- log child id response: `09:36:03.860`
- parent ipv6: `n/a`
- parent extaddr: `3e395173f18e0a88`
- parent rloc16: `0x0000`
- child extaddr: `4e6bb49d8d49f7a7`
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

### `ucast_fastpr_child_20260706-094206-run20.log`

- manifest status: `completed`
- child extaddr: `f204834572d29b03`
- switch target extaddr(s): `921d8b6caa6448ea, 921d8b6caa6448ea, 921d8b6caa6448ea`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `6ad97604b7673ab7`
- parent rloc16: `n/a`
- child extaddr: `f204834572d29b03`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **154 ms**
- Response -> Child ID Request: **601 ms**
- Child ID Request -> Response: **15 ms**
- Full Attach: **770 ms**
- pcap parent request: `09:47:56.231` (frame 825)
- pcap parent response: `09:47:56.385` (frame 826)
- pcap child id request: `09:47:56.986` (frame 834)
- pcap child id response: `09:47:57.001` (frame 836)

#### PCAP-complete child attach 2

- log parent request: `09:48:00.701`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `921d8b6caa6448ea`
- parent rloc16: `n/a`
- child extaddr: `f204834572d29b03`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **10 ms**
- Response -> Child ID Request: **30 ms**
- Child ID Request -> Response: **13 ms**
- Full Attach: **53 ms**
- pcap parent request: `09:48:00.747` (frame 839)
- pcap parent response: `09:48:00.757` (frame 841)
- pcap child id request: `09:48:00.787` (frame 843)
- pcap child id response: `09:48:00.800` (frame 845)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `09:48:00.719`
- log parent response: `09:48:00.736`
- log child id request: `09:48:00.750`
- log child id response: `09:48:00.780`
- parent ipv6: `n/a`
- parent extaddr: `921d8b6caa6448ea`
- parent rloc16: `0x3c00`
- child extaddr: `f204834572d29b03`
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
