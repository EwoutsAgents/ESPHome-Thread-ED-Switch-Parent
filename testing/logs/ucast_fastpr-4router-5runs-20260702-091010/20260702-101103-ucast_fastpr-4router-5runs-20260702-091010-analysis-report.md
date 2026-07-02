# Child Log Analysis

## ucast_fastpr_child

Files analyzed: **5**

- batch folders: `ucast_fastpr-4router-5runs-20260702-091010`

### PCAP-complete child attach summary

| Attach | Metric | M (SD), ms | n |
| --- | --- | ---: | ---: |
| 1 | Request -> Response | 88.60 (59.64) | 5 |
| 1 | Response -> Child ID Request | 649.40 (51.54) | 5 |
| 1 | Child ID Request -> Response | 67.20 (4.09) | 5 |
| 1 | Full Attach | 805.20 (15.93) | 5 |
| 2 | Request -> Response | 45.40 (3.71) | 5 |
| 2 | Response -> Child ID Request | 81.40 (7.23) | 5 |
| 2 | Child ID Request -> Response | 69.00 (4.80) | 5 |
| 2 | Full Attach | 195.80 (5.26) | 5 |

| Metric | M (SD) | n |
| --- | ---: | ---: |
| Failed TX Attempts per Log | 0.00 (0.00) | 5 |
| Log-only or Partial Sequences per Log | 0.00 (0.00) | 5 |

### `ucast_fastpr_child_20260702-091110-run01.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `467b397c5d015a59`
- switch target extaddr(s): `4a7e0107b49f496f, 4a7e0107b49f496f, 4a7e0107b49f496f`

#### PCAP-complete child attach 1

- log parent request: `09:17:00.647`
- log parent response: `09:17:00.874`
- log child id request: `09:17:01.416`
- log child id response: `09:17:01.505`
- parent ipv6: `fe80:0:0:0:38a1:686a:1156:2151`
- parent extaddr: `3aa1686a11562151`
- parent rloc16: `0x5800`
- child extaddr: `467b397c5d015a59`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **176 ms**
- Response -> Child ID Request: **574 ms**
- Child ID Request -> Response: **66 ms**
- Full Attach: **816 ms**
- pcap parent request: `09:17:00.692` (frame 179)
- pcap parent response: `09:17:00.868` (frame 180)
- pcap child id request: `09:17:01.442` (frame 188)
- pcap child id response: `09:17:01.508` (frame 190)

#### PCAP-complete child attach 2

- log parent request: `09:17:04.698`
- log parent response: `09:17:04.774`
- log child id request: `09:17:04.820`
- log child id response: `09:17:04.914`
- parent ipv6: `fe80:0:0:0:487e:107:b49f:496f`
- parent extaddr: `4a7e0107b49f496f`
- parent rloc16: `0x6000`
- child extaddr: `467b397c5d015a59`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **44 ms**
- Response -> Child ID Request: **78 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **192 ms**
- pcap parent request: `09:17:04.726` (frame 192)
- pcap parent response: `09:17:04.770` (frame 194)
- pcap child id request: `09:17:04.848` (frame 196)
- pcap child id response: `09:17:04.918` (frame 198)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260702-092307-run02.log`

- manifest status: `completed`
- child extaddr: `82ec9b565e575401`
- switch target extaddr(s): `4ef9b0411a46b66b, 4ef9b0411a46b66b, 4ef9b0411a46b66b`

#### PCAP-complete child attach 1

- log parent request: `09:28:57.760`
- log parent response: `09:28:57.892`
- log child id request: `09:28:58.529`
- log child id response: `09:28:58.622`
- parent ipv6: `fe80:0:0:0:d0b3:8887:57ed:58d4`
- parent extaddr: `d2b3888757ed58d4`
- parent rloc16: `0xec00`
- child extaddr: `82ec9b565e575401`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **47 ms**
- Response -> Child ID Request: **674 ms**
- Child ID Request -> Response: **71 ms**
- Full Attach: **792 ms**
- pcap parent request: `09:28:57.829` (frame 236)
- pcap parent response: `09:28:57.876` (frame 237)
- pcap child id request: `09:28:58.550` (frame 245)
- pcap child id response: `09:28:58.621` (frame 247)

#### PCAP-complete child attach 2

- log parent request: `09:29:02.402`
- log parent response: `09:29:02.488`
- log child id request: `09:29:02.535`
- log child id response: `09:29:02.629`
- parent ipv6: `fe80:0:0:0:4cf9:b041:1a46:b66b`
- parent extaddr: `4ef9b0411a46b66b`
- parent rloc16: `0xc800`
- child extaddr: `82ec9b565e575401`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **52 ms**
- Response -> Child ID Request: **81 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **203 ms**
- pcap parent request: `09:29:02.425` (frame 249)
- pcap parent response: `09:29:02.477` (frame 251)
- pcap child id request: `09:29:02.558` (frame 253)
- pcap child id response: `09:29:02.628` (frame 255)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260702-093504-run03.log`

- manifest status: `completed`
- child extaddr: `e2dd36e0224127f3`
- switch target extaddr(s): `c2ec2c7354593e81, c2ec2c7354593e81, c2ec2c7354593e81`

#### PCAP-complete child attach 1

- log parent request: `09:40:55.391`
- log parent response: `09:40:55.524`
- log child id request: `09:40:56.160`
- log child id response: `09:40:56.246`
- parent ipv6: `fe80:0:0:0:5490:5166:6ab6:a239`
- parent extaddr: `569051666ab6a239`
- parent rloc16: `0x1000`
- child extaddr: `e2dd36e0224127f3`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **47 ms**
- Response -> Child ID Request: **675 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **785 ms**
- pcap parent request: `09:40:55.464` (frame 176)
- pcap parent response: `09:40:55.511` (frame 177)
- pcap child id request: `09:40:56.186` (frame 185)
- pcap child id response: `09:40:56.249` (frame 187)

#### PCAP-complete child attach 2

- log parent request: `09:41:00.016`
- log parent response: `09:41:00.095`
- log child id request: `09:41:00.141`
- log child id response: `09:41:00.239`
- parent ipv6: `fe80:0:0:0:c0ec:2c73:5459:3e81`
- parent extaddr: `c2ec2c7354593e81`
- parent rloc16: `0x9400`
- child extaddr: `e2dd36e0224127f3`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **44 ms**
- Response -> Child ID Request: **77 ms**
- Child ID Request -> Response: **74 ms**
- Full Attach: **195 ms**
- pcap parent request: `09:41:00.048` (frame 193)
- pcap parent response: `09:41:00.092` (frame 195)
- pcap child id request: `09:41:00.169` (frame 197)
- pcap child id response: `09:41:00.243` (frame 199)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260702-094702-run04.log`

- manifest status: `completed`
- child extaddr: `e6554b6ff6e25e4b`
- switch target extaddr(s): `3a9243430376c543, 3a9243430376c543, 3a9243430376c543`

#### PCAP-complete child attach 1

- log parent request: `09:52:53.204`
- log parent response: `09:52:53.302`
- log child id request: `09:52:53.969`
- log child id response: `09:52:54.058`
- parent ipv6: `fe80:0:0:0:2815:c1ae:3f8a:6618`
- parent extaddr: `2a15c1ae3f8a6618`
- parent rloc16: `0x6400`
- child extaddr: `e6554b6ff6e25e4b`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **126 ms**
- Response -> Child ID Request: **621 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **811 ms**
- pcap parent request: `09:52:53.250` (frame 472)
- pcap parent response: `09:52:53.376` (frame 475)
- pcap child id request: `09:52:53.997` (frame 481)
- pcap child id response: `09:52:54.061` (frame 483)

#### PCAP-complete child attach 2

- log parent request: `09:52:57.741`
- log parent response: `09:52:57.817`
- log child id request: `09:52:57.862`
- log child id response: `09:52:57.955`
- parent ipv6: `fe80:0:0:0:3892:4343:376:c543`
- parent extaddr: `3a9243430376c543`
- parent rloc16: `0x3800`
- child extaddr: `e6554b6ff6e25e4b`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **43 ms**
- Response -> Child ID Request: **77 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **190 ms**
- pcap parent request: `09:52:57.770` (frame 485)
- pcap parent response: `09:52:57.813` (frame 487)
- pcap child id request: `09:52:57.890` (frame 489)
- pcap child id response: `09:52:57.960` (frame 491)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260702-095900-run05.log`

- manifest status: `completed`
- child extaddr: `5acf3c02e170c2b6`
- switch target extaddr(s): `eebe46dd74df72aa, eebe46dd74df72aa, eebe46dd74df72aa`

#### PCAP-complete child attach 1

- log parent request: `10:04:51.292`
- log parent response: `10:04:51.389`
- log child id request: `10:04:52.060`
- log child id response: `10:04:52.154`
- parent ipv6: `fe80:0:0:0:34b6:b583:baec:fe`
- parent extaddr: `36b6b583baec00fe`
- parent rloc16: `0x7000`
- child extaddr: `5acf3c02e170c2b6`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **47 ms**
- Response -> Child ID Request: **703 ms**
- Child ID Request -> Response: **72 ms**
- Full Attach: **822 ms**
- pcap parent request: `10:04:51.337` (frame 283)
- pcap parent response: `10:04:51.384` (frame 284)
- pcap child id request: `10:04:52.087` (frame 292)
- pcap child id response: `10:04:52.159` (frame 294)

#### PCAP-complete child attach 2

- log parent request: `10:04:55.535`
- log parent response: `10:04:55.620`
- log child id request: `10:04:55.667`
- log child id response: `10:04:55.759`
- parent ipv6: `fe80:0:0:0:ecbe:46dd:74df:72aa`
- parent extaddr: `eebe46dd74df72aa`
- parent rloc16: `0xcc00`
- child extaddr: `5acf3c02e170c2b6`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **44 ms**
- Response -> Child ID Request: **94 ms**
- Child ID Request -> Response: **61 ms**
- Full Attach: **199 ms**
- pcap parent request: `10:04:55.563` (frame 298)
- pcap parent response: `10:04:55.607` (frame 300)
- pcap child id request: `10:04:55.701` (frame 302)
- pcap child id response: `10:04:55.762` (frame 304)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**
