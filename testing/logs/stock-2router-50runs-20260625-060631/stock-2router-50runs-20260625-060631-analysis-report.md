# Child Log Analysis

## stock_child

Files analyzed: **50**

### PCAP-complete child attach summary

| Attach | Metric | M (SD), ms | n |
| --- | --- | ---: | ---: |
| 1 | Request -> Response | 197.04 (124.73) | 50 |
| 1 | Response -> Child ID Request | 549.76 (124.82) | 50 |
| 1 | Child ID Request -> Response | 63.50 (1.34) | 50 |
| 1 | Full Attach | 810.30 (10.24) | 50 |
| 2 | Request -> Response | 289.60 (146.58) | 25 |
| 2 | Response -> Child ID Request | 460.56 (146.48) | 25 |
| 2 | Child ID Request -> Response | 65.52 (7.04) | 25 |
| 2 | Full Attach | 815.68 (7.03) | 25 |

| Metric | M (SD) | n |
| --- | ---: | ---: |
| Failed TX Attempts per Log | 31.98 (32.30) | 50 |
| Log-only or Partial Sequences per Log | 0.00 (0.00) | 50 |

### `stock_child_20260625-060653-run01.log`

- child extaddr: `2a5dd0ae05cde17e`

#### PCAP-complete child attach 1

- log parent request: `06:12:34.912`
- log parent response: `06:12:35.287`
- log child id request: `06:12:35.621`
- log child id response: `06:12:35.714`
- parent ipv6: `fe80:0:0:0:f00e:8218:5b86:4260`
- parent extaddr: `f20e82185b864260`
- parent rloc16: `0x7c00`
- child extaddr: `2a5dd0ae05cde17e`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **378 ms**
- Response -> Child ID Request: **374 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **815 ms**
- pcap parent request: `06:12:34.896` (frame 77)
- pcap parent response: `06:12:35.274` (frame 78)
- pcap child id request: `06:12:35.648` (frame 82)
- pcap child id response: `06:12:35.711` (frame 84)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260625-061244-run02.log`

- child extaddr: `6e28c48e754c70b4`

#### PCAP-complete child attach 1

- log parent request: `06:18:24.873`
- log parent response: `06:18:25.034`
- log child id request: `06:18:25.644`
- log child id response: `06:18:25.732`
- parent ipv6: `fe80:0:0:0:20a7:1b7e:7423:5874`
- parent extaddr: `22a71b7e74235874`
- parent rloc16: `0x6800`
- child extaddr: `6e28c48e754c70b4`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **103 ms**
- Response -> Child ID Request: **648 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **813 ms**
- pcap parent request: `06:18:24.917` (frame 80)
- pcap parent response: `06:18:25.020` (frame 81)
- pcap child id request: `06:18:25.668` (frame 85)
- pcap child id response: `06:18:25.730` (frame 87)

#### PCAP-complete child attach 2

- log parent request: `06:22:25.648`
- log parent response: `06:22:25.843`
- log child id request: `06:22:26.358`
- log child id response: `06:22:26.449`
- parent ipv6: `fe80:0:0:0:2ceb:6da5:5988:89e6`
- parent extaddr: `2eeb6da5598889e6`
- parent rloc16: `0x4c00`
- child extaddr: `6e28c48e754c70b4`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **198 ms**
- Response -> Child ID Request: **552 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **814 ms**
- pcap parent request: `06:22:25.640` (frame 227)
- pcap parent response: `06:22:25.838` (frame 228)
- pcap child id request: `06:22:26.390` (frame 230)
- pcap child id response: `06:22:26.454` (frame 232)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 9: 16, seq 10: 16, seq 11: 16, seq 12: 16
- failed tx by dst: `22a71b7e74235874`: 53

### `stock_child_20260625-062436-run03.log`

- child extaddr: `d6b687d8ebb6d4cf`

#### PCAP-complete child attach 1

- log parent request: `06:30:17.207`
- log parent response: `06:30:17.690`
- log child id request: `06:30:18.027`
- log child id response: `06:30:18.072`
- parent ipv6: `fe80:0:0:0:bc5b:8df1:e79f:d16e`
- parent extaddr: `be5b8df1e79fd16e`
- parent rloc16: `0xa000`
- child extaddr: `d6b687d8ebb6d4cf`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **383 ms**
- Response -> Child ID Request: **327 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **773 ms**
- pcap parent request: `06:30:17.295` (frame 72)
- pcap parent response: `06:30:17.678` (frame 73)
- pcap child id request: `06:30:18.005` (frame 77)
- pcap child id response: `06:30:18.068` (frame 79)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260625-063027-run04.log`

- child extaddr: `425f68a477a787fc`

#### PCAP-complete child attach 1

- log parent request: `06:36:07.663`
- log parent response: `06:36:07.844`
- log child id request: `06:36:08.485`
- log child id response: `06:36:08.528`
- parent ipv6: `fe80:0:0:0:e821:6b4d:c970:842f`
- parent extaddr: `ea216b4dc970842f`
- parent rloc16: `0xd800`
- child extaddr: `425f68a477a787fc`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **84 ms**
- Response -> Child ID Request: **632 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **779 ms**
- pcap parent request: `06:36:07.748` (frame 80)
- pcap parent response: `06:36:07.832` (frame 81)
- pcap child id request: `06:36:08.464` (frame 85)
- pcap child id response: `06:36:08.527` (frame 87)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260625-063617-run05.log`

- child extaddr: `86a9bdd77944c1c0`

#### PCAP-complete child attach 1

- log parent request: `06:41:58.296`
- log parent response: `06:41:58.599`
- log child id request: `06:41:59.008`
- log child id response: `06:41:59.097`
- parent ipv6: `fe80:0:0:0:d42d:a104:c956:369d`
- parent extaddr: `d62da104c956369d`
- parent rloc16: `0xac00`
- child extaddr: `86a9bdd77944c1c0`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **306 ms**
- Response -> Child ID Request: **445 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **815 ms**
- pcap parent request: `06:41:58.281` (frame 73)
- pcap parent response: `06:41:58.587` (frame 74)
- pcap child id request: `06:41:59.032` (frame 78)
- pcap child id response: `06:41:59.096` (frame 80)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260625-064207-run06.log`

- child extaddr: `422f1a99f12b6ad6`

#### PCAP-complete child attach 1

- log parent request: `06:47:48.297`
- log parent response: `06:47:48.555`
- log child id request: `06:47:49.068`
- log child id response: `06:47:49.159`
- parent ipv6: `fe80:0:0:0:5809:bd03:5e54:97a5`
- parent extaddr: `5a09bd035e5497a5`
- parent rloc16: `0xac00`
- child extaddr: `422f1a99f12b6ad6`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **200 ms**
- Response -> Child ID Request: **550 ms**
- Child ID Request -> Response: **65 ms**
- Full Attach: **815 ms**
- pcap parent request: `06:47:48.342` (frame 76)
- pcap parent response: `06:47:48.542` (frame 77)
- pcap child id request: `06:47:49.092` (frame 81)
- pcap child id response: `06:47:49.157` (frame 83)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260625-064758-run07.log`

- child extaddr: `92eee5da6c3c1614`

#### PCAP-complete child attach 1

- log parent request: `06:53:38.253`
- log parent response: `06:53:38.319`
- log child id request: `06:53:38.958`
- log child id response: `06:53:39.051`
- parent ipv6: `fe80:0:0:0:2096:706f:d245:1fc7`
- parent extaddr: `2296706fd2451fc7`
- parent rloc16: `0x0000`
- child extaddr: `92eee5da6c3c1614`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **70 ms**
- Response -> Child ID Request: **679 ms**
- Child ID Request -> Response: **65 ms**
- Full Attach: **814 ms**
- pcap parent request: `06:53:38.236` (frame 74)
- pcap parent response: `06:53:38.306` (frame 75)
- pcap child id request: `06:53:38.985` (frame 79)
- pcap child id response: `06:53:39.050` (frame 81)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260625-065348-run08.log`

- child extaddr: `a6935570498479e3`

#### PCAP-complete child attach 1

- log parent request: `06:59:28.279`
- log parent response: `06:59:28.790`
- log child id request: `06:59:29.051`
- log child id response: `06:59:29.140`
- parent ipv6: `fe80:0:0:0:38c2:e17c:8475:2602`
- parent extaddr: `3ac2e17c84752602`
- parent rloc16: `0x8c00`
- child extaddr: `a6935570498479e3`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **447 ms**
- Response -> Child ID Request: **298 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **809 ms**
- pcap parent request: `06:59:28.330` (frame 72)
- pcap parent response: `06:59:28.777` (frame 73)
- pcap child id request: `06:59:29.075` (frame 77)
- pcap child id response: `06:59:29.139` (frame 79)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260625-065938-run09.log`

- child extaddr: `e2711ea5988ee2e1`

#### PCAP-complete child attach 1

- log parent request: `07:05:18.944`
- log parent response: `07:05:19.058`
- log child id request: `07:05:19.652`
- log child id response: `07:05:19.740`
- parent ipv6: `fe80:0:0:0:40a:88d:6e8e:b1ce`
- parent extaddr: `060a088d6e8eb1ce`
- parent rloc16: `0x9800`
- child extaddr: `e2711ea5988ee2e1`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **119 ms**
- Response -> Child ID Request: **631 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **813 ms**
- pcap parent request: `07:05:18.926` (frame 78)
- pcap parent response: `07:05:19.045` (frame 79)
- pcap child id request: `07:05:19.676` (frame 83)
- pcap child id response: `07:05:19.739` (frame 85)

#### PCAP-complete child attach 2

- log parent request: `07:09:19.957`
- log parent response: `07:09:20.451`
- log child id request: `07:09:20.732`
- log child id response: `07:09:20.823`
- parent ipv6: `fe80:0:0:0:8c65:db59:6b40:c34a`
- parent extaddr: `8e65db596b40c34a`
- parent rloc16: `0xac00`
- child extaddr: `e2711ea5988ee2e1`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **433 ms**
- Response -> Child ID Request: **319 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **815 ms**
- pcap parent request: `07:09:20.013` (frame 225)
- pcap parent response: `07:09:20.446` (frame 226)
- pcap child id request: `07:09:20.765` (frame 228)
- pcap child id response: `07:09:20.828` (frame 230)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 147: 16, seq 148: 16, seq 149: 16, seq 150: 16
- failed tx by dst: `060a088d6e8eb1ce`: 54

### `stock_child_20260625-071130-run10.log`

- child extaddr: `b63673d4c79d2d69`

#### PCAP-complete child attach 1

- log parent request: `07:17:10.916`
- log parent response: `07:17:11.000`
- log child id request: `07:17:11.627`
- log child id response: `07:17:11.717`
- parent ipv6: `fe80:0:0:0:4c61:8c59:7014:9b9c`
- parent extaddr: `4e618c5970149b9c`
- parent rloc16: `0x8400`
- child extaddr: `b63673d4c79d2d69`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **88 ms**
- Response -> Child ID Request: **664 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **814 ms**
- pcap parent request: `07:17:10.900` (frame 76)
- pcap parent response: `07:17:10.988` (frame 77)
- pcap child id request: `07:17:11.652` (frame 81)
- pcap child id response: `07:17:11.714` (frame 83)

#### PCAP-complete child attach 2

- log parent request: `07:21:11.677`
- log parent response: `07:21:11.755`
- log child id request: `07:21:12.430`
- log child id response: `07:21:12.479`
- parent ipv6: `fe80:0:0:0:f075:3f4b:1ac8:78c3`
- parent extaddr: `f2753f4b1ac878c3`
- parent rloc16: `0xe000`
- child extaddr: `b63673d4c79d2d69`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **81 ms**
- Response -> Child ID Request: **669 ms**
- Child ID Request -> Response: **65 ms**
- Full Attach: **815 ms**
- pcap parent request: `07:21:11.670` (frame 222)
- pcap parent response: `07:21:11.751` (frame 223)
- pcap child id request: `07:21:12.420` (frame 225)
- pcap child id response: `07:21:12.485` (frame 227)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 53: 16, seq 54: 16, seq 55: 16, seq 56: 16
- failed tx by dst: `4e618c5970149b9c`: 54

### `stock_child_20260625-072322-run11.log`

- child extaddr: `fae9b9a8465fa061`

#### PCAP-complete child attach 1

- log parent request: `07:29:03.123`
- log parent response: `07:29:03.255`
- log child id request: `07:29:03.832`
- log child id response: `07:29:03.921`
- parent ipv6: `fe80:0:0:0:2c86:115f:154f:79ca`
- parent extaddr: `2e86115f154f79ca`
- parent rloc16: `0x6800`
- child extaddr: `fae9b9a8465fa061`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **134 ms**
- Response -> Child ID Request: **615 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **812 ms**
- pcap parent request: `07:29:03.107` (frame 79)
- pcap parent response: `07:29:03.241` (frame 80)
- pcap child id request: `07:29:03.856` (frame 84)
- pcap child id response: `07:29:03.919` (frame 86)

#### PCAP-complete child attach 2

- log parent request: `07:33:03.790`
- log parent response: `07:33:04.040`
- log child id request: `07:33:04.500`
- log child id response: `07:33:04.591`
- parent ipv6: `fe80:0:0:0:acaa:d7a5:c930:e8db`
- parent extaddr: `aeaad7a5c930e8db`
- parent rloc16: `0xac00`
- child extaddr: `fae9b9a8465fa061`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **254 ms**
- Response -> Child ID Request: **496 ms**
- Child ID Request -> Response: **65 ms**
- Full Attach: **815 ms**
- pcap parent request: `07:33:03.781` (frame 225)
- pcap parent response: `07:33:04.035` (frame 226)
- pcap child id request: `07:33:04.531` (frame 228)
- pcap child id response: `07:33:04.596` (frame 230)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 116: 16, seq 117: 16, seq 118: 16, seq 119: 16
- failed tx by dst: `2e86115f154f79ca`: 49

### `stock_child_20260625-073515-run12.log`

- child extaddr: `beba1d24a78cd80e`

#### PCAP-complete child attach 1

- log parent request: `07:40:55.580`
- log parent response: `07:40:55.940`
- log child id request: `07:40:56.350`
- log child id response: `07:40:56.439`
- parent ipv6: `fe80:0:0:0:54c5:7799:adb9:8c80`
- parent extaddr: `56c57799adb98c80`
- parent rloc16: `0xbc00`
- child extaddr: `beba1d24a78cd80e`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **303 ms**
- Response -> Child ID Request: **447 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **813 ms**
- pcap parent request: `07:40:55.623` (frame 79)
- pcap parent response: `07:40:55.926` (frame 80)
- pcap child id request: `07:40:56.373` (frame 84)
- pcap child id response: `07:40:56.436` (frame 86)

#### PCAP-complete child attach 2

- log parent request: `07:44:56.326`
- log parent response: `07:44:56.663`
- log child id request: `07:44:57.036`
- log child id response: `07:44:57.126`
- parent ipv6: `fe80:0:0:0:c001:d9d9:73f:423e`
- parent extaddr: `c201d9d9073f423e`
- parent rloc16: `0x3800`
- child extaddr: `beba1d24a78cd80e`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **340 ms**
- Response -> Child ID Request: **409 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **812 ms**
- pcap parent request: `07:44:56.317` (frame 227)
- pcap parent response: `07:44:56.657` (frame 228)
- pcap child id request: `07:44:57.066` (frame 230)
- pcap child id response: `07:44:57.129` (frame 232)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 141: 16, seq 142: 16, seq 143: 16, seq 144: 16
- failed tx by dst: `56c57799adb98c80`: 55

### `stock_child_20260625-074707-run13.log`

- child extaddr: `5e49865fdbdb2f82`

#### PCAP-complete child attach 1

- log parent request: `07:52:47.753`
- log parent response: `07:52:48.019`
- log child id request: `07:52:48.510`
- log child id response: `07:52:48.551`
- parent ipv6: `fe80:0:0:0:8c3c:86b1:8393:fcd7`
- parent extaddr: `8e3c86b18393fcd7`
- parent rloc16: `0x9400`
- child extaddr: `5e49865fdbdb2f82`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **270 ms**
- Response -> Child ID Request: **479 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **812 ms**
- pcap parent request: `07:52:47.735` (frame 71)
- pcap parent response: `07:52:48.005` (frame 72)
- pcap child id request: `07:52:48.484` (frame 76)
- pcap child id response: `07:52:48.547` (frame 78)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260625-075257-run14.log`

- child extaddr: `ae18c6d9bd3a4b74`

#### PCAP-complete child attach 1

- log parent request: `07:58:38.126`
- log parent response: `07:58:38.293`
- log child id request: `07:58:38.896`
- log child id response: `07:58:38.986`
- parent ipv6: `fe80:0:0:0:682a:251:c868:841f`
- parent extaddr: `6a2a0251c868841f`
- parent rloc16: `0xe000`
- child extaddr: `ae18c6d9bd3a4b74`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **108 ms**
- Response -> Child ID Request: **640 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **812 ms**
- pcap parent request: `07:58:38.170` (frame 77)
- pcap parent response: `07:58:38.278` (frame 78)
- pcap child id request: `07:58:38.918` (frame 82)
- pcap child id response: `07:58:38.982` (frame 84)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260625-075847-run15.log`

- child extaddr: `4a613227e3c4cd9a`

#### PCAP-complete child attach 1

- log parent request: `08:04:28.111`
- log parent response: `08:04:28.607`
- log child id request: `08:04:28.821`
- log child id response: `08:04:28.914`
- parent ipv6: `fe80:0:0:0:3447:cf6d:917a:96d7`
- parent extaddr: `3647cf6d917a96d7`
- parent rloc16: `0xe800`
- child extaddr: `4a613227e3c4cd9a`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **497 ms**
- Response -> Child ID Request: **253 ms**
- Child ID Request -> Response: **66 ms**
- Full Attach: **816 ms**
- pcap parent request: `08:04:28.094` (frame 71)
- pcap parent response: `08:04:28.591` (frame 73)
- pcap child id request: `08:04:28.844` (frame 77)
- pcap child id response: `08:04:28.910` (frame 79)

#### PCAP-complete child attach 2

- log parent request: `08:08:28.607`
- log parent response: `08:08:28.847`
- log child id request: `08:08:29.361`
- log child id response: `08:08:29.408`
- parent ipv6: `fe80:0:0:0:343f:4ff8:8003:9dff`
- parent extaddr: `363f4ff880039dff`
- parent rloc16: `0xdc00`
- child extaddr: `4a613227e3c4cd9a`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **243 ms**
- Response -> Child ID Request: **506 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **813 ms**
- pcap parent request: `08:08:28.599` (frame 219)
- pcap parent response: `08:08:28.842` (frame 220)
- pcap child id request: `08:08:29.348` (frame 222)
- pcap child id response: `08:08:29.412` (frame 224)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 102: 16, seq 103: 16, seq 104: 16, seq 105: 16
- failed tx by dst: `3647cf6d917a96d7`: 53

### `stock_child_20260625-081039-run16.log`

- child extaddr: `12f2595c278fe1fe`

#### PCAP-complete child attach 1

- log parent request: `08:16:20.233`
- log parent response: `08:16:20.384`
- log child id request: `08:16:21.006`
- log child id response: `08:16:21.093`
- parent ipv6: `fe80:0:0:0:e456:f101:886c:fb38`
- parent extaddr: `e656f101886cfb38`
- parent rloc16: `0x3800`
- child extaddr: `12f2595c278fe1fe`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **85 ms**
- Response -> Child ID Request: **659 ms**
- Child ID Request -> Response: **61 ms**
- Full Attach: **805 ms**
- pcap parent request: `08:16:20.285` (frame 76)
- pcap parent response: `08:16:20.370` (frame 77)
- pcap child id request: `08:16:21.029` (frame 83)
- pcap child id response: `08:16:21.090` (frame 85)

#### PCAP-complete child attach 2

- log parent request: `08:20:21.204`
- log parent response: `08:20:21.707`
- log child id request: `08:20:21.915`
- log child id response: `08:20:22.005`
- parent ipv6: `fe80:0:0:0:1429:9d79:b61e:fab5`
- parent extaddr: `16299d79b61efab5`
- parent rloc16: `0x6000`
- child extaddr: `12f2595c278fe1fe`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **505 ms**
- Response -> Child ID Request: **245 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **814 ms**
- pcap parent request: `08:20:21.196` (frame 225)
- pcap parent response: `08:20:21.701` (frame 226)
- pcap child id request: `08:20:21.946` (frame 228)
- pcap child id response: `08:20:22.010` (frame 230)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 18: 16, seq 19: 16, seq 20: 16, seq 21: 16
- failed tx by dst: `e656f101886cfb38`: 61

### `stock_child_20260625-082232-run17.log`

- child extaddr: `12f43e49dbcc026f`

#### PCAP-complete child attach 1

- log parent request: `08:28:13.198`
- log parent response: `08:28:13.377`
- log child id request: `08:28:13.908`
- log child id response: `08:28:13.995`
- parent ipv6: `fe80:0:0:0:f41d:2c0b:a7dc:78d4`
- parent extaddr: `f61d2c0ba7dc78d4`
- parent rloc16: `0x8000`
- child extaddr: `12f43e49dbcc026f`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **183 ms**
- Response -> Child ID Request: **566 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **811 ms**
- pcap parent request: `08:28:13.182` (frame 80)
- pcap parent response: `08:28:13.365` (frame 81)
- pcap child id request: `08:28:13.931` (frame 85)
- pcap child id response: `08:28:13.993` (frame 87)

#### PCAP-complete child attach 2

- log parent request: `08:32:14.070`
- log parent response: `08:32:14.160`
- log child id request: `08:32:14.823`
- log child id response: `08:32:14.868`
- parent ipv6: `fe80:0:0:0:b878:e79b:7bd7:8e29`
- parent extaddr: `ba78e79b7bd78e29`
- parent rloc16: `0xcc00`
- child extaddr: `12f43e49dbcc026f`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **91 ms**
- Response -> Child ID Request: **657 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **811 ms**
- pcap parent request: `08:32:14.064` (frame 228)
- pcap parent response: `08:32:14.155` (frame 229)
- pcap child id request: `08:32:14.812` (frame 231)
- pcap child id response: `08:32:14.875` (frame 233)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 18: 16, seq 19: 16, seq 20: 16, seq 21: 16
- failed tx by dst: `f61d2c0ba7dc78d4`: 52

### `stock_child_20260625-083424-run18.log`

- child extaddr: `2ed15c4aa1bb62c6`

#### PCAP-complete child attach 1

- log parent request: `08:40:05.461`
- log parent response: `08:40:05.712`
- log child id request: `08:40:06.171`
- log child id response: `08:40:06.262`
- parent ipv6: `fe80:0:0:0:38e3:513f:26d3:ded8`
- parent extaddr: `3ae3513f26d3ded8`
- parent rloc16: `0x4400`
- child extaddr: `2ed15c4aa1bb62c6`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **254 ms**
- Response -> Child ID Request: **496 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **814 ms**
- pcap parent request: `08:40:05.445` (frame 77)
- pcap parent response: `08:40:05.699` (frame 78)
- pcap child id request: `08:40:06.195` (frame 82)
- pcap child id response: `08:40:06.259` (frame 84)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260625-084015-run19.log`

- child extaddr: `32e6e0d16d9c60c9`

#### PCAP-complete child attach 1

- log parent request: `08:45:55.542`
- log parent response: `08:45:55.870`
- log child id request: `08:45:56.252`
- log child id response: `08:45:56.342`
- parent ipv6: `fe80:0:0:0:b84a:3374:c9e6:222c`
- parent extaddr: `ba4a3374c9e6222c`
- parent rloc16: `0xbc00`
- child extaddr: `32e6e0d16d9c60c9`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **330 ms**
- Response -> Child ID Request: **420 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **814 ms**
- pcap parent request: `08:45:55.526` (frame 76)
- pcap parent response: `08:45:55.856` (frame 77)
- pcap child id request: `08:45:56.276` (frame 81)
- pcap child id response: `08:45:56.340` (frame 83)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260625-084605-run20.log`

- child extaddr: `8212d95e12e54f49`

#### PCAP-complete child attach 1

- log parent request: `08:51:46.000`
- log parent response: `08:51:46.102`
- log child id request: `08:51:46.709`
- log child id response: `08:51:46.796`
- parent ipv6: `fe80:0:0:0:b80a:ab42:38b2:d40`
- parent extaddr: `ba0aab4238b20d40`
- parent rloc16: `0xa400`
- child extaddr: `8212d95e12e54f49`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **106 ms**
- Response -> Child ID Request: **643 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **811 ms**
- pcap parent request: `08:51:45.983` (frame 78)
- pcap parent response: `08:51:46.089` (frame 79)
- pcap child id request: `08:51:46.732` (frame 83)
- pcap child id response: `08:51:46.794` (frame 85)

#### PCAP-complete child attach 2

- log parent request: `08:55:46.756`
- log parent response: `08:55:47.198`
- log child id request: `08:55:47.511`
- log child id response: `08:55:47.557`
- parent ipv6: `fe80:0:0:0:b447:35b4:73b6:d2d1`
- parent extaddr: `b64735b473b6d2d1`
- parent rloc16: `0xec00`
- child extaddr: `8212d95e12e54f49`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **445 ms**
- Response -> Child ID Request: **306 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **815 ms**
- pcap parent request: `08:55:46.748` (frame 225)
- pcap parent response: `08:55:47.193` (frame 226)
- pcap child id request: `08:55:47.499` (frame 228)
- pcap child id response: `08:55:47.563` (frame 230)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 119: 16, seq 120: 16, seq 121: 16, seq 122: 16
- failed tx by dst: `ba0aab4238b20d40`: 55

### `stock_child_20260625-085757-run21.log`

- child extaddr: `52f432b57e8f2257`

#### PCAP-complete child attach 1

- log parent request: `09:03:38.586`
- log parent response: `09:03:38.900`
- log child id request: `09:03:39.296`
- log child id response: `09:03:39.386`
- parent ipv6: `fe80:0:0:0:b01c:e9f2:bd84:c75f`
- parent extaddr: `b21ce9f2bd84c75f`
- parent rloc16: `0x3400`
- child extaddr: `52f432b57e8f2257`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **316 ms**
- Response -> Child ID Request: **434 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **814 ms**
- pcap parent request: `09:03:38.570` (frame 80)
- pcap parent response: `09:03:38.886` (frame 81)
- pcap child id request: `09:03:39.320` (frame 85)
- pcap child id response: `09:03:39.384` (frame 87)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260625-090347-run22.log`

- child extaddr: `b6ff696798d3775d`

#### PCAP-complete child attach 1

- log parent request: `09:09:28.534`
- log parent response: `09:09:28.579`
- log child id request: `09:09:29.245`
- log child id response: `09:09:29.334`
- parent ipv6: `fe80:0:0:0:ac3e:9ced:fee0:b225`
- parent extaddr: `ae3e9cedfee0b225`
- parent rloc16: `0x2000`
- child extaddr: `b6ff696798d3775d`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **48 ms**
- Response -> Child ID Request: **702 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **813 ms**
- pcap parent request: `09:09:28.518` (frame 79)
- pcap parent response: `09:09:28.566` (frame 80)
- pcap child id request: `09:09:29.268` (frame 84)
- pcap child id response: `09:09:29.331` (frame 86)

#### PCAP-complete child attach 2

- log parent request: `09:13:29.102`
- log parent response: `09:13:29.606`
- log child id request: `09:13:29.856`
- log child id response: `09:13:29.904`
- parent ipv6: `fe80:0:0:0:cce1:d1d5:5109:abd0`
- parent extaddr: `cee1d1d55109abd0`
- parent rloc16: `0x0c00`
- child extaddr: `b6ff696798d3775d`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **508 ms**
- Response -> Child ID Request: **243 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **815 ms**
- pcap parent request: `09:13:29.093` (frame 227)
- pcap parent response: `09:13:29.601` (frame 228)
- pcap child id request: `09:13:29.844` (frame 230)
- pcap child id response: `09:13:29.908` (frame 232)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 126: 16, seq 127: 16, seq 128: 16, seq 129: 16
- failed tx by dst: `ae3e9cedfee0b225`: 54

### `stock_child_20260625-091540-run23.log`

- child extaddr: `5a372cc3bab791d4`

#### PCAP-complete child attach 1

- log parent request: `09:21:20.936`
- log parent response: `09:21:21.286`
- log child id request: `09:21:21.643`
- log child id response: `09:21:21.735`
- parent ipv6: `fe80:0:0:0:c460:6301:c5ee:63fa`
- parent extaddr: `c6606301c5ee63fa`
- parent rloc16: `0xcc00`
- child extaddr: `5a372cc3bab791d4`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **357 ms**
- Response -> Child ID Request: **393 ms**
- Child ID Request -> Response: **66 ms**
- Full Attach: **816 ms**
- pcap parent request: `09:21:20.914` (frame 78)
- pcap parent response: `09:21:21.271` (frame 79)
- pcap child id request: `09:21:21.664` (frame 83)
- pcap child id response: `09:21:21.730` (frame 85)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260625-092130-run24.log`

- child extaddr: `9261301aa2484471`

#### PCAP-complete child attach 1

- log parent request: `09:27:11.595`
- log parent response: `09:27:11.963`
- log child id request: `09:27:12.306`
- log child id response: `09:27:12.397`
- parent ipv6: `fe80:0:0:0:8004:70d2:9a8:d363`
- parent extaddr: `820470d209a8d363`
- parent rloc16: `0xf000`
- child extaddr: `9261301aa2484471`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **370 ms**
- Response -> Child ID Request: **380 ms**
- Child ID Request -> Response: **65 ms**
- Full Attach: **815 ms**
- pcap parent request: `09:27:11.576` (frame 74)
- pcap parent response: `09:27:11.946` (frame 75)
- pcap child id request: `09:27:12.326` (frame 79)
- pcap child id response: `09:27:12.391` (frame 81)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260625-092720-run25.log`

- child extaddr: `ba3808863c2e5350`

#### PCAP-complete child attach 1

- log parent request: `09:33:01.553`
- log parent response: `09:33:01.874`
- log child id request: `09:33:02.263`
- log child id response: `09:33:02.353`
- parent ipv6: `fe80:0:0:0:cc10:adc:1975:387a`
- parent extaddr: `ce100adc1975387a`
- parent rloc16: `0xd400`
- child extaddr: `ba3808863c2e5350`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **324 ms**
- Response -> Child ID Request: **426 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **814 ms**
- pcap parent request: `09:33:01.534` (frame 71)
- pcap parent response: `09:33:01.858` (frame 72)
- pcap child id request: `09:33:02.284` (frame 76)
- pcap child id response: `09:33:02.348` (frame 78)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260625-093310-run26.log`

- child extaddr: `badc8b686b6069f7`

#### PCAP-complete child attach 1

- log parent request: `09:38:51.565`
- log parent response: `09:38:51.654`
- log child id request: `09:38:52.277`
- log child id response: `09:38:52.367`
- parent ipv6: `fe80:0:0:0:80ff:5cf:64a5:43b0`
- parent extaddr: `82ff05cf64a543b0`
- parent rloc16: `0x6c00`
- child extaddr: `badc8b686b6069f7`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **93 ms**
- Response -> Child ID Request: **659 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **816 ms**
- pcap parent request: `09:38:51.546` (frame 77)
- pcap parent response: `09:38:51.639` (frame 78)
- pcap child id request: `09:38:52.298` (frame 82)
- pcap child id response: `09:38:52.362` (frame 84)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260625-093901-run27.log`

- child extaddr: `c2de111030eb958d`

#### PCAP-complete child attach 1

- log parent request: `09:44:42.038`
- log parent response: `09:44:42.152`
- log child id request: `09:44:42.748`
- log child id response: `09:44:42.836`
- parent ipv6: `fe80:0:0:0:85e:2216:b783:eb5a`
- parent extaddr: `0a5e2216b783eb5a`
- parent rloc16: `0xd400`
- child extaddr: `c2de111030eb958d`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **118 ms**
- Response -> Child ID Request: **631 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **811 ms**
- pcap parent request: `09:44:42.018` (frame 80)
- pcap parent response: `09:44:42.136` (frame 81)
- pcap child id request: `09:44:42.767` (frame 85)
- pcap child id response: `09:44:42.829` (frame 87)

#### PCAP-complete child attach 2

- log parent request: `09:48:42.632`
- log parent response: `09:48:42.885`
- log child id request: `09:48:43.386`
- log child id response: `09:48:43.434`
- parent ipv6: `fe80:0:0:0:ac4f:5243:eeb1:89d0`
- parent extaddr: `ae4f5243eeb189d0`
- parent rloc16: `0xc000`
- child extaddr: `c2de111030eb958d`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **256 ms**
- Response -> Child ID Request: **495 ms**
- Child ID Request -> Response: **65 ms**
- Full Attach: **816 ms**
- pcap parent request: `09:48:42.620` (frame 226)
- pcap parent response: `09:48:42.876` (frame 227)
- pcap child id request: `09:48:43.371` (frame 229)
- pcap child id response: `09:48:43.436` (frame 231)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 34: 16, seq 35: 16, seq 36: 16, seq 37: 16
- failed tx by dst: `0a5e2216b783eb5a`: 51

### `stock_child_20260625-095053-run28.log`

- child extaddr: `02455be0d3289b8c`

#### PCAP-complete child attach 1

- log parent request: `09:56:34.196`
- log parent response: `09:56:34.293`
- log child id request: `09:56:34.907`
- log child id response: `09:56:34.999`
- parent ipv6: `fe80:0:0:0:a05f:ec37:8075:bcfd`
- parent extaddr: `a25fec378075bcfd`
- parent rloc16: `0x9400`
- child extaddr: `02455be0d3289b8c`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **100 ms**
- Response -> Child ID Request: **650 ms**
- Child ID Request -> Response: **66 ms**
- Full Attach: **816 ms**
- pcap parent request: `09:56:34.177` (frame 74)
- pcap parent response: `09:56:34.277` (frame 75)
- pcap child id request: `09:56:34.927` (frame 79)
- pcap child id response: `09:56:34.993` (frame 81)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260625-095643-run29.log`

- child extaddr: `6e9591fdd8be047c`

#### PCAP-complete child attach 1

- log parent request: `10:02:24.075`
- log parent response: `10:02:24.338`
- log child id request: `10:02:24.784`
- log child id response: `10:02:24.873`
- parent ipv6: `fe80:0:0:0:a440:2706:8d90:423a`
- parent extaddr: `a64027068d90423a`
- parent rloc16: `0xa400`
- child extaddr: `6e9591fdd8be047c`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **266 ms**
- Response -> Child ID Request: **482 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **811 ms**
- pcap parent request: `10:02:24.056` (frame 78)
- pcap parent response: `10:02:24.322` (frame 79)
- pcap child id request: `10:02:24.804` (frame 83)
- pcap child id response: `10:02:24.867` (frame 85)

#### PCAP-complete child attach 2

- log parent request: `10:06:25.154`
- log parent response: `10:06:25.292`
- log child id request: `10:06:25.908`
- log child id response: `10:06:25.956`
- parent ipv6: `fe80:0:0:0:8c69:8bf3:b244:965f`
- parent extaddr: `8e698bf3b244965f`
- parent rloc16: `0xe000`
- child extaddr: `6e9591fdd8be047c`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **141 ms**
- Response -> Child ID Request: **609 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **814 ms**
- pcap parent request: `10:06:25.143` (frame 224)
- pcap parent response: `10:06:25.284` (frame 225)
- pcap child id request: `10:06:25.893` (frame 227)
- pcap child id response: `10:06:25.957` (frame 229)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 112: 16, seq 113: 16, seq 114: 16, seq 115: 16
- failed tx by dst: `a64027068d90423a`: 49

### `stock_child_20260625-100836-run30.log`

- child extaddr: `6a8391da0af147a7`

#### PCAP-complete child attach 1

- log parent request: `10:14:16.683`
- log parent response: `10:14:16.866`
- log child id request: `10:14:17.393`
- log child id response: `10:14:17.485`
- parent ipv6: `fe80:0:0:0:f0cd:71f3:38f:f32a`
- parent extaddr: `f2cd71f3038ff32a`
- parent rloc16: `0x0400`
- child extaddr: `6a8391da0af147a7`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **186 ms**
- Response -> Child ID Request: **564 ms**
- Child ID Request -> Response: **65 ms**
- Full Attach: **815 ms**
- pcap parent request: `10:14:16.663` (frame 78)
- pcap parent response: `10:14:16.849` (frame 79)
- pcap child id request: `10:14:17.413` (frame 83)
- pcap child id response: `10:14:17.478` (frame 85)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260625-101426-run31.log`

- child extaddr: `1624dc03e7c6c4e2`

#### PCAP-complete child attach 1

- log parent request: `10:20:07.031`
- log parent response: `10:20:07.154`
- log child id request: `10:20:07.801`
- log child id response: `10:20:07.890`
- parent ipv6: `fe80:0:0:0:3c65:f59d:f6d1:d21`
- parent extaddr: `3e65f59df6d10d21`
- parent rloc16: `0x5000`
- child extaddr: `1624dc03e7c6c4e2`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **66 ms**
- Response -> Child ID Request: **684 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **813 ms**
- pcap parent request: `10:20:07.072` (frame 77)
- pcap parent response: `10:20:07.138` (frame 78)
- pcap child id request: `10:20:07.822` (frame 82)
- pcap child id response: `10:20:07.885` (frame 84)

#### PCAP-complete child attach 2

- log parent request: `10:24:07.801`
- log parent response: `10:24:08.062`
- log child id request: `10:24:08.556`
- log child id response: `10:24:08.602`
- parent ipv6: `fe80:0:0:0:b08a:49b3:93f2:7fa9`
- parent extaddr: `b28a49b393f27fa9`
- parent rloc16: `0xc800`
- child extaddr: `1624dc03e7c6c4e2`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **264 ms**
- Response -> Child ID Request: **486 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **814 ms**
- pcap parent request: `10:24:07.790` (frame 226)
- pcap parent response: `10:24:08.054` (frame 227)
- pcap child id request: `10:24:08.540` (frame 229)
- pcap child id response: `10:24:08.604` (frame 231)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 247: 16, seq 248: 16, seq 249: 16, seq 250: 16
- failed tx by dst: `3e65f59df6d10d21`: 55

### `stock_child_20260625-102619-run32.log`

- child extaddr: `4ec247f3c0458ed3`

#### PCAP-complete child attach 1

- log parent request: `10:31:59.219`
- log parent response: `10:31:59.471`
- log child id request: `10:32:00.039`
- log child id response: `10:32:00.082`
- parent ipv6: `fe80:0:0:0:84af:cc5c:6538:915d`
- parent extaddr: `86afcc5c6538915d`
- parent rloc16: `0x8000`
- child extaddr: `4ec247f3c0458ed3`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **155 ms**
- Response -> Child ID Request: **559 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **777 ms**
- pcap parent request: `10:31:59.299` (frame 74)
- pcap parent response: `10:31:59.454` (frame 75)
- pcap child id request: `10:32:00.013` (frame 79)
- pcap child id response: `10:32:00.076` (frame 81)

#### PCAP-complete child attach 2

- log parent request: `10:36:00.365`
- log parent response: `10:36:00.664`
- log child id request: `10:36:01.076`
- log child id response: `10:36:01.166`
- parent ipv6: `fe80:0:0:0:ec3f:4d48:570e:a6f2`
- parent extaddr: `ee3f4d48570ea6f2`
- parent rloc16: `0x7000`
- child extaddr: `4ec247f3c0458ed3`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **304 ms**
- Response -> Child ID Request: **448 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **815 ms**
- pcap parent request: `10:36:00.353` (frame 224)
- pcap parent response: `10:36:00.657` (frame 225)
- pcap child id request: `10:36:01.105` (frame 227)
- pcap child id response: `10:36:01.168` (frame 229)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 223: 16, seq 224: 16, seq 225: 16, seq 226: 16
- failed tx by dst: `86afcc5c6538915d`: 50

### `stock_child_20260625-103811-run33.log`

- child extaddr: `3a8bb3304bbd4d1a`

#### PCAP-complete child attach 1

- log parent request: `10:43:51.842`
- log parent response: `10:43:51.946`
- log child id request: `10:43:52.551`
- log child id response: `10:43:52.639`
- parent ipv6: `fe80:0:0:0:7890:a2df:b66f:4ef6`
- parent extaddr: `7a90a2dfb66f4ef6`
- parent rloc16: `0x9000`
- child extaddr: `3a8bb3304bbd4d1a`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **106 ms**
- Response -> Child ID Request: **642 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **810 ms**
- pcap parent request: `10:43:51.823` (frame 74)
- pcap parent response: `10:43:51.929` (frame 75)
- pcap child id request: `10:43:52.571` (frame 79)
- pcap child id response: `10:43:52.633` (frame 81)

#### PCAP-complete child attach 2

- log parent request: `10:47:52.217`
- log parent response: `10:47:52.783`
- log child id request: `10:47:52.991`
- log child id response: `10:47:53.082`
- parent ipv6: `fe80:0:0:0:8054:ced1:48e8:3a82`
- parent extaddr: `8254ced148e83a82`
- parent rloc16: `0x8800`
- child extaddr: `3a8bb3304bbd4d1a`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **505 ms**
- Response -> Child ID Request: **245 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **814 ms**
- pcap parent request: `10:47:52.270` (frame 220)
- pcap parent response: `10:47:52.775` (frame 221)
- pcap child id request: `10:47:53.020` (frame 223)
- pcap child id response: `10:47:53.084` (frame 225)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 8: 16, seq 9: 16, seq 10: 16, seq 11: 16
- failed tx by dst: `7a90a2dfb66f4ef6`: 54

### `stock_child_20260625-105003-run34.log`

- child extaddr: `7ad746b0707069ef`

#### PCAP-complete child attach 1

- log parent request: `10:55:44.525`
- log parent response: `10:55:44.637`
- log child id request: `10:55:45.235`
- log child id response: `10:55:45.322`
- parent ipv6: `fe80:0:0:0:f813:eb2c:c3df:b21f`
- parent extaddr: `fa13eb2cc3dfb21f`
- parent rloc16: `0xd400`
- child extaddr: `7ad746b0707069ef`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **115 ms**
- Response -> Child ID Request: **634 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **811 ms**
- pcap parent request: `10:55:44.508` (frame 77)
- pcap parent response: `10:55:44.623` (frame 78)
- pcap child id request: `10:55:45.257` (frame 82)
- pcap child id response: `10:55:45.319` (frame 84)

#### PCAP-complete child attach 2

- log parent request: `10:59:45.197`
- log parent response: `10:59:45.493`
- log child id request: `10:59:45.908`
- log child id response: `10:59:45.998`
- parent ipv6: `fe80:0:0:0:cc84:a74d:6d3e:6c35`
- parent extaddr: `ce84a74d6d3e6c35`
- parent rloc16: `0x0800`
- child extaddr: `7ad746b0707069ef`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **299 ms**
- Response -> Child ID Request: **452 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **815 ms**
- pcap parent request: `10:59:45.188` (frame 224)
- pcap parent response: `10:59:45.487` (frame 225)
- pcap child id request: `10:59:45.939` (frame 227)
- pcap child id response: `10:59:46.003` (frame 229)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 85: 16, seq 86: 16, seq 87: 16, seq 88: 16
- failed tx by dst: `fa13eb2cc3dfb21f`: 49

### `stock_child_20260625-110156-run35.log`

- child extaddr: `fe309028e82d6a21`

#### PCAP-complete child attach 1

- log parent request: `11:07:36.463`
- log parent response: `11:07:36.837`
- log child id request: `11:07:37.235`
- log child id response: `11:07:37.324`
- parent ipv6: `fe80:0:0:0:e0d8:9e2:4310:182c`
- parent extaddr: `e2d809e24310182c`
- parent rloc16: `0xa800`
- child extaddr: `fe309028e82d6a21`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **310 ms**
- Response -> Child ID Request: **434 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **807 ms**
- pcap parent request: `11:07:36.514` (frame 76)
- pcap parent response: `11:07:36.824` (frame 77)
- pcap child id request: `11:07:37.258` (frame 81)
- pcap child id response: `11:07:37.321` (frame 83)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260625-110746-run36.log`

- child extaddr: `9e962a9f63c2f03d`

#### PCAP-complete child attach 1

- log parent request: `11:13:27.378`
- log parent response: `11:13:27.772`
- log child id request: `11:13:28.089`
- log child id response: `11:13:28.180`
- parent ipv6: `fe80:0:0:0:6854:3692:d477:46c9`
- parent extaddr: `6a543692d47746c9`
- parent rloc16: `0xac00`
- child extaddr: `9e962a9f63c2f03d`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **395 ms**
- Response -> Child ID Request: **355 ms**
- Child ID Request -> Response: **65 ms**
- Full Attach: **815 ms**
- pcap parent request: `11:13:27.362` (frame 74)
- pcap parent response: `11:13:27.757` (frame 75)
- pcap child id request: `11:13:28.112` (frame 79)
- pcap child id response: `11:13:28.177` (frame 81)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260625-111336-run37.log`

- child extaddr: `5a4842615521a8a2`

#### PCAP-complete child attach 1

- log parent request: `11:19:17.527`
- log parent response: `11:19:17.699`
- log child id request: `11:19:18.299`
- log child id response: `11:19:18.388`
- parent ipv6: `fe80:0:0:0:80c8:d661:390e:347e`
- parent extaddr: `82c8d661390e347e`
- parent rloc16: `0x1800`
- child extaddr: `5a4842615521a8a2`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **113 ms**
- Response -> Child ID Request: **637 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **814 ms**
- pcap parent request: `11:19:17.572` (frame 72)
- pcap parent response: `11:19:17.685` (frame 73)
- pcap child id request: `11:19:18.322` (frame 77)
- pcap child id response: `11:19:18.386` (frame 79)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260625-111926-run38.log`

- child extaddr: `c6f17ac8c1bb7f98`

#### PCAP-complete child attach 1

- log parent request: `11:25:07.763`
- log parent response: `11:25:08.091`
- log child id request: `11:25:08.535`
- log child id response: `11:25:08.624`
- parent ipv6: `fe80:0:0:0:acf5:5e09:dc84:cf21`
- parent extaddr: `aef55e09dc84cf21`
- parent rloc16: `0x3c00`
- child extaddr: `c6f17ac8c1bb7f98`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **270 ms**
- Response -> Child ID Request: **483 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **815 ms**
- pcap parent request: `11:25:07.808` (frame 75)
- pcap parent response: `11:25:08.078` (frame 76)
- pcap child id request: `11:25:08.561` (frame 80)
- pcap child id response: `11:25:08.623` (frame 82)

#### PCAP-complete child attach 2

- log parent request: `11:29:08.568`
- log parent response: `11:29:08.648`
- log child id request: `11:29:09.279`
- log child id response: `11:29:09.369`
- parent ipv6: `fe80:0:0:0:811:f848:c0bb:c651`
- parent extaddr: `0a11f848c0bbc651`
- parent rloc16: `0x4400`
- child extaddr: `c6f17ac8c1bb7f98`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **83 ms**
- Response -> Child ID Request: **667 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **814 ms**
- pcap parent request: `11:29:08.561` (frame 223)
- pcap parent response: `11:29:08.644` (frame 224)
- pcap child id request: `11:29:09.311` (frame 226)
- pcap child id response: `11:29:09.375` (frame 228)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 201: 16, seq 202: 16, seq 203: 16, seq 204: 16
- failed tx by dst: `aef55e09dc84cf21`: 53

### `stock_child_20260625-113119-run39.log`

- child extaddr: `6649846a72f94611`

#### PCAP-complete child attach 1

- log parent request: `11:36:59.958`
- log parent response: `11:37:00.065`
- log child id request: `11:37:00.663`
- log child id response: `11:37:00.750`
- parent ipv6: `fe80:0:0:0:8c19:a000:9ba8:6d55`
- parent extaddr: `8e19a0009ba86d55`
- parent rloc16: `0x6c00`
- child extaddr: `6649846a72f94611`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **114 ms**
- Response -> Child ID Request: **634 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **810 ms**
- pcap parent request: `11:36:59.938` (frame 75)
- pcap parent response: `11:37:00.052` (frame 76)
- pcap child id request: `11:37:00.686` (frame 80)
- pcap child id response: `11:37:00.748` (frame 82)

#### PCAP-complete child attach 2

- log parent request: `11:41:00.413`
- log parent response: `11:41:00.467`
- log child id request: `11:41:01.123`
- log child id response: `11:41:01.215`
- parent ipv6: `fe80:0:0:0:6cf5:9e84:187a:ab18`
- parent extaddr: `6ef59e84187aab18`
- parent rloc16: `0x9000`
- child extaddr: `6649846a72f94611`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **59 ms**
- Response -> Child ID Request: **692 ms**
- Child ID Request -> Response: **65 ms**
- Full Attach: **816 ms**
- pcap parent request: `11:41:00.404` (frame 221)
- pcap parent response: `11:41:00.463` (frame 222)
- pcap child id request: `11:41:01.155` (frame 225)
- pcap child id response: `11:41:01.220` (frame 227)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 183: 16, seq 184: 16, seq 185: 16, seq 186: 16
- failed tx by dst: `8e19a0009ba86d55`: 49

### `stock_child_20260625-114311-run40.log`

- child extaddr: `826891d156980074`

#### PCAP-complete child attach 1

- log parent request: `11:48:52.691`
- log parent response: `11:48:52.949`
- log child id request: `11:48:53.463`
- log child id response: `11:48:53.551`
- parent ipv6: `fe80:0:0:0:413:7f23:a190:4614`
- parent extaddr: `06137f23a1904614`
- parent rloc16: `0x5000`
- child extaddr: `826891d156980074`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **199 ms**
- Response -> Child ID Request: **552 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **813 ms**
- pcap parent request: `11:48:52.736` (frame 77)
- pcap parent response: `11:48:52.935` (frame 78)
- pcap child id request: `11:48:53.487` (frame 82)
- pcap child id response: `11:48:53.549` (frame 84)

#### PCAP-complete child attach 2

- log parent request: `11:52:53.720`
- log parent response: `11:52:53.849`
- log child id request: `11:52:54.430`
- log child id response: `11:52:54.555`
- parent ipv6: `fe80:0:0:0:10d1:a451:2025:1762`
- parent extaddr: `12d1a45120251762`
- parent rloc16: `0xd000`
- child extaddr: `826891d156980074`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **132 ms**
- Response -> Child ID Request: **618 ms**
- Child ID Request -> Response: **99 ms**
- Full Attach: **849 ms**
- pcap parent request: `11:52:53.712` (frame 224)
- pcap parent response: `11:52:53.844` (frame 225)
- pcap child id request: `11:52:54.462` (frame 227)
- pcap child id response: `11:52:54.561` (frame 230)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 176: 16, seq 177: 16, seq 178: 16, seq 179: 16
- failed tx by dst: `06137f23a1904614`: 49

### `stock_child_20260625-115504-run41.log`

- child extaddr: `beebac13c21b9ac6`

#### PCAP-complete child attach 1

- log parent request: `12:00:44.780`
- log parent response: `12:00:44.830`
- log child id request: `12:00:45.489`
- log child id response: `12:00:45.581`
- parent ipv6: `fe80:0:0:0:d8e7:726:f032:6b5c`
- parent extaddr: `dae70726f0326b5c`
- parent rloc16: `0xc400`
- child extaddr: `beebac13c21b9ac6`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **56 ms**
- Response -> Child ID Request: **696 ms**
- Child ID Request -> Response: **65 ms**
- Full Attach: **817 ms**
- pcap parent request: `12:00:44.761` (frame 81)
- pcap parent response: `12:00:44.817` (frame 82)
- pcap child id request: `12:00:45.513` (frame 86)
- pcap child id response: `12:00:45.578` (frame 88)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260625-120054-run42.log`

- child extaddr: `62a38116877bcba0`

#### PCAP-complete child attach 1

- log parent request: `12:06:34.861`
- log parent response: `12:06:35.002`
- log child id request: `12:06:35.573`
- log child id response: `12:06:35.663`
- parent ipv6: `fe80:0:0:0:8bb:77fb:3934:704`
- parent extaddr: `0abb77fb39340704`
- parent rloc16: `0x8000`
- child extaddr: `62a38116877bcba0`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **144 ms**
- Response -> Child ID Request: **608 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **814 ms**
- pcap parent request: `12:06:34.845` (frame 76)
- pcap parent response: `12:06:34.989` (frame 77)
- pcap child id request: `12:06:35.597` (frame 82)
- pcap child id response: `12:06:35.659` (frame 84)

#### PCAP-complete child attach 2

- log parent request: `12:10:35.312`
- log parent response: `12:10:35.766`
- log child id request: `12:10:36.066`
- log child id response: `12:10:36.113`
- parent ipv6: `fe80:0:0:0:c47d:185c:7609:8b66`
- parent extaddr: `c67d185c76098b66`
- parent rloc16: `0x6400`
- child extaddr: `62a38116877bcba0`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **456 ms**
- Response -> Child ID Request: **294 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **814 ms**
- pcap parent request: `12:10:35.304` (frame 225)
- pcap parent response: `12:10:35.760` (frame 226)
- pcap child id request: `12:10:36.054` (frame 228)
- pcap child id response: `12:10:36.118` (frame 230)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 202: 16, seq 203: 16, seq 204: 16, seq 205: 16
- failed tx by dst: `0abb77fb39340704`: 48

### `stock_child_20260625-121246-run43.log`

- child extaddr: `2a1f3257d7c3cdc8`

#### PCAP-complete child attach 1

- log parent request: `12:18:27.537`
- log parent response: `12:18:27.579`
- log child id request: `12:18:28.249`
- log child id response: `12:18:28.337`
- parent ipv6: `fe80:0:0:0:603f:c9c6:4dc3:3f5a`
- parent extaddr: `623fc9c64dc33f5a`
- parent rloc16: `0xe800`
- child extaddr: `2a1f3257d7c3cdc8`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **45 ms**
- Response -> Child ID Request: **706 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **813 ms**
- pcap parent request: `12:18:27.522` (frame 79)
- pcap parent response: `12:18:27.567` (frame 80)
- pcap child id request: `12:18:28.273` (frame 84)
- pcap child id response: `12:18:28.335` (frame 86)

#### PCAP-complete child attach 2

- log parent request: `12:22:28.019`
- log parent response: `12:22:28.415`
- log child id request: `12:22:28.730`
- log child id response: `12:22:28.823`
- parent ipv6: `fe80:0:0:0:3cf2:7545:4737:2396`
- parent extaddr: `3ef2754547372396`
- parent rloc16: `0x2000`
- child extaddr: `2a1f3257d7c3cdc8`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **398 ms**
- Response -> Child ID Request: **351 ms**
- Child ID Request -> Response: **67 ms**
- Full Attach: **816 ms**
- pcap parent request: `12:22:28.013` (frame 227)
- pcap parent response: `12:22:28.411` (frame 228)
- pcap child id request: `12:22:28.762` (frame 230)
- pcap child id response: `12:22:28.829` (frame 232)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 159: 16, seq 160: 16, seq 161: 16, seq 162: 16
- failed tx by dst: `623fc9c64dc33f5a`: 48

### `stock_child_20260625-122439-run44.log`

- child extaddr: `82d242d97da33a8c`

#### PCAP-complete child attach 1

- log parent request: `12:30:19.473`
- log parent response: `12:30:19.644`
- log child id request: `12:30:20.294`
- log child id response: `12:30:20.337`
- parent ipv6: `fe80:0:0:0:b076:596e:1350:dc96`
- parent extaddr: `b276596e1350dc96`
- parent rloc16: `0x5000`
- child extaddr: `82d242d97da33a8c`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **56 ms**
- Response -> Child ID Request: **660 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **779 ms**
- pcap parent request: `12:30:19.556` (frame 78)
- pcap parent response: `12:30:19.612` (frame 79)
- pcap child id request: `12:30:20.272` (frame 83)
- pcap child id response: `12:30:20.335` (frame 85)

#### PCAP-complete child attach 2

- log parent request: `12:34:20.009`
- log parent response: `12:34:20.372`
- log child id request: `12:34:20.763`
- log child id response: `12:34:20.810`
- parent ipv6: `fe80:0:0:0:44c5:a185:66dc:6059`
- parent extaddr: `46c5a18566dc6059`
- parent rloc16: `0x6800`
- child extaddr: `82d242d97da33a8c`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **366 ms**
- Response -> Child ID Request: **384 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **814 ms**
- pcap parent request: `12:34:20.001` (frame 226)
- pcap parent response: `12:34:20.367` (frame 227)
- pcap child id request: `12:34:20.751` (frame 229)
- pcap child id response: `12:34:20.815` (frame 231)

#### Failed TX summary

- failed tx attempts: **63**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 197: 15, seq 198: 16, seq 199: 16, seq 200: 16
- failed tx by dst: `b276596e1350dc96`: 53

### `stock_child_20260625-123631-run45.log`

- child extaddr: `da2d1aa8130261e8`

#### PCAP-complete child attach 1

- log parent request: `12:42:11.900`
- log parent response: `12:42:12.062`
- log child id request: `12:42:12.672`
- log child id response: `12:42:12.761`
- parent ipv6: `fe80:0:0:0:a8e5:fc6f:ac4a:db1b`
- parent extaddr: `aae5fc6fac4adb1b`
- parent rloc16: `0xac00`
- child extaddr: `da2d1aa8130261e8`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **99 ms**
- Response -> Child ID Request: **647 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **809 ms**
- pcap parent request: `12:42:11.949` (frame 79)
- pcap parent response: `12:42:12.048` (frame 80)
- pcap child id request: `12:42:12.695` (frame 84)
- pcap child id response: `12:42:12.758` (frame 86)

#### PCAP-complete child attach 2

- log parent request: `12:46:12.715`
- log parent response: `12:46:13.047`
- log child id request: `12:46:13.471`
- log child id response: `12:46:13.516`
- parent ipv6: `fe80:0:0:0:e474:8f1f:d999:9762`
- parent extaddr: `e6748f1fd9999762`
- parent rloc16: `0xf000`
- child extaddr: `da2d1aa8130261e8`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **335 ms**
- Response -> Child ID Request: **416 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **814 ms**
- pcap parent request: `12:46:12.707` (frame 226)
- pcap parent response: `12:46:13.042` (frame 227)
- pcap child id request: `12:46:13.458` (frame 229)
- pcap child id response: `12:46:13.521` (frame 231)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 73: 16, seq 74: 16, seq 75: 16, seq 76: 16
- failed tx by dst: `aae5fc6fac4adb1b`: 52

### `stock_child_20260625-124824-run46.log`

- child extaddr: `56fba528a429b520`

#### PCAP-complete child attach 1

- log parent request: `12:54:04.637`
- log parent response: `12:54:04.766`
- log child id request: `12:54:05.409`
- log child id response: `12:54:05.497`
- parent ipv6: `fe80:0:0:0:6814:c2bb:25a1:d825`
- parent extaddr: `6a14c2bb25a1d825`
- parent rloc16: `0xc400`
- child extaddr: `56fba528a429b520`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **72 ms**
- Response -> Child ID Request: **679 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **814 ms**
- pcap parent request: `12:54:04.681` (frame 72)
- pcap parent response: `12:54:04.753` (frame 73)
- pcap child id request: `12:54:05.432` (frame 77)
- pcap child id response: `12:54:05.495` (frame 79)

#### PCAP-complete child attach 2

- log parent request: `12:58:05.174`
- log parent response: `12:58:05.586`
- log child id request: `12:58:05.883`
- log child id response: `12:58:05.974`
- parent ipv6: `fe80:0:0:0:c053:f2b1:d3ca:494c`
- parent extaddr: `c253f2b1d3ca494c`
- parent rloc16: `0x3000`
- child extaddr: `56fba528a429b520`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **414 ms**
- Response -> Child ID Request: **334 ms**
- Child ID Request -> Response: **66 ms**
- Full Attach: **814 ms**
- pcap parent request: `12:58:05.166` (frame 221)
- pcap parent response: `12:58:05.580` (frame 222)
- pcap child id request: `12:58:05.914` (frame 224)
- pcap child id response: `12:58:05.980` (frame 226)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 240: 16, seq 241: 16, seq 242: 16, seq 243: 16
- failed tx by dst: `6a14c2bb25a1d825`: 53

### `stock_child_20260625-130016-run47.log`

- child extaddr: `92f0f6c90b61c9ee`

#### PCAP-complete child attach 1

- log parent request: `13:05:57.288`
- log parent response: `13:05:57.490`
- log child id request: `13:05:57.998`
- log child id response: `13:05:58.091`
- parent ipv6: `fe80:0:0:0:3810:57fb:c57c:9ff3`
- parent extaddr: `3a1057fbc57c9ff3`
- parent rloc16: `0x2c00`
- child extaddr: `92f0f6c90b61c9ee`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **204 ms**
- Response -> Child ID Request: **546 ms**
- Child ID Request -> Response: **67 ms**
- Full Attach: **817 ms**
- pcap parent request: `13:05:57.271` (frame 77)
- pcap parent response: `13:05:57.475` (frame 78)
- pcap child id request: `13:05:58.021` (frame 82)
- pcap child id response: `13:05:58.088` (frame 84)

#### PCAP-complete child attach 2

- log parent request: `13:09:57.802`
- log parent response: `13:09:57.929`
- log child id request: `13:09:58.556`
- log child id response: `13:09:58.603`
- parent ipv6: `fe80:0:0:0:8847:f108:69cb:965`
- parent extaddr: `8a47f10869cb0965`
- parent rloc16: `0xcc00`
- child extaddr: `92f0f6c90b61c9ee`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **130 ms**
- Response -> Child ID Request: **621 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **814 ms**
- pcap parent request: `13:09:57.794` (frame 224)
- pcap parent response: `13:09:57.924` (frame 225)
- pcap child id request: `13:09:58.545` (frame 227)
- pcap child id response: `13:09:58.608` (frame 229)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 190: 16, seq 191: 16, seq 192: 16, seq 193: 16
- failed tx by dst: `3a1057fbc57c9ff3`: 56

### `stock_child_20260625-131208-run48.log`

- child extaddr: `ca48427a681c2ff1`

#### PCAP-complete child attach 1

- log parent request: `13:17:49.551`
- log parent response: `13:17:49.744`
- log child id request: `13:17:50.262`
- log child id response: `13:17:50.353`
- parent ipv6: `fe80:0:0:0:c4a8:7385:5618:69c6`
- parent extaddr: `c6a87385561869c6`
- parent rloc16: `0xd000`
- child extaddr: `ca48427a681c2ff1`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **195 ms**
- Response -> Child ID Request: **555 ms**
- Child ID Request -> Response: **65 ms**
- Full Attach: **815 ms**
- pcap parent request: `13:17:49.536` (frame 80)
- pcap parent response: `13:17:49.731` (frame 81)
- pcap child id request: `13:17:50.286` (frame 85)
- pcap child id response: `13:17:50.351` (frame 87)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260625-131758-run49.log`

- child extaddr: `7ee6bf05dbff2111`

#### PCAP-complete child attach 1

- log parent request: `13:23:39.302`
- log parent response: `13:23:39.376`
- log child id request: `13:23:40.012`
- log child id response: `13:23:40.102`
- parent ipv6: `fe80:0:0:0:2c7d:10f5:af19:5150`
- parent extaddr: `2e7d10f5af195150`
- parent rloc16: `0x4800`
- child extaddr: `7ee6bf05dbff2111`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **80 ms**
- Response -> Child ID Request: **672 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **816 ms**
- pcap parent request: `13:23:39.283` (frame 75)
- pcap parent response: `13:23:39.363` (frame 76)
- pcap child id request: `13:23:40.035` (frame 80)
- pcap child id response: `13:23:40.099` (frame 82)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260625-132348-run50.log`

- child extaddr: `a63521803dd3eb83`

#### PCAP-complete child attach 1

- log parent request: `13:29:29.134`
- log parent response: `13:29:29.564`
- log child id request: `13:29:29.844`
- log child id response: `13:29:29.935`
- parent ipv6: `fe80:0:0:0:c82a:371f:f678:9607`
- parent extaddr: `ca2a371ff6789607`
- parent rloc16: `0x2000`
- child extaddr: `a63521803dd3eb83`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **432 ms**
- Response -> Child ID Request: **318 ms**
- Child ID Request -> Response: **65 ms**
- Full Attach: **815 ms**
- pcap parent request: `13:29:29.118` (frame 76)
- pcap parent response: `13:29:29.550` (frame 77)
- pcap child id request: `13:29:29.868` (frame 81)
- pcap child id response: `13:29:29.933` (frame 83)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**
