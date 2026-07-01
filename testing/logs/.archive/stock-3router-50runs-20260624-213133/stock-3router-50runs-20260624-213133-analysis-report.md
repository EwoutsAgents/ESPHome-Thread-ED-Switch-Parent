# Child Log Analysis

## stock_child

Files analyzed: **50**

### PCAP-complete child attach summary

| Attach | Metric | M (SD), ms | n |
| --- | --- | ---: | ---: |
| 1 | Request -> Response | 172.38 (110.79) | 50 |
| 1 | Response -> Child ID Request | 575.94 (111.98) | 50 |
| 1 | Child ID Request -> Response | 68.56 (6.89) | 50 |
| 1 | Full Attach | 816.88 (10.66) | 50 |
| 2 | Request -> Response | 197.61 (138.76) | 36 |
| 2 | Response -> Child ID Request | 552.53 (138.72) | 36 |
| 2 | Child ID Request -> Response | 67.17 (5.04) | 36 |
| 2 | Full Attach | 817.31 (5.28) | 36 |

| Metric | M (SD) | n |
| --- | ---: | ---: |
| Failed TX Attempts per Log | 46.08 (29.03) | 50 |
| Log-only or Partial Sequences per Log | 0.00 (0.00) | 50 |

### `stock_child_20260624-213302-run01.log`

- child extaddr: `eed8ea0f04774c4b`

#### PCAP-complete child attach 1

- log parent request: `21:38:49.291`
- log parent response: `21:38:49.417`
- log child id request: `21:38:50.007`
- log child id response: `21:38:50.095`
- parent ipv6: `fe80:0:0:0:ec96:67f2:1386:ef27`
- parent extaddr: `ee9667f21386ef27`
- parent rloc16: `0xf400`
- child extaddr: `eed8ea0f04774c4b`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **125 ms**
- Response -> Child ID Request: **624 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **811 ms**
- pcap parent request: `21:38:49.280` (frame 124)
- pcap parent response: `21:38:49.405` (frame 126)
- pcap child id request: `21:38:50.029` (frame 132)
- pcap child id response: `21:38:50.091` (frame 134)

#### PCAP-complete child attach 2

- log parent request: `21:42:49.869`
- log parent response: `21:42:50.071`
- log child id request: `21:42:50.587`
- log child id response: `21:42:50.675`
- parent ipv6: `fe80:0:0:0:1c84:4c2:b6a6:9665`
- parent extaddr: `1e8404c2b6a69665`
- parent rloc16: `0x2400`
- child extaddr: `eed8ea0f04774c4b`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **202 ms**
- Response -> Child ID Request: **547 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **813 ms**
- pcap parent request: `21:42:49.865` (frame 342)
- pcap parent response: `21:42:50.067` (frame 343)
- pcap child id request: `21:42:50.614` (frame 348)
- pcap child id response: `21:42:50.678` (frame 350)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 107: 16, seq 108: 16, seq 109: 16, seq 110: 16
- failed tx by dst: `ee9667f21386ef27`: 61

### `stock_child_20260624-214501-run02.log`

- child extaddr: `7e11089540fc72cd`

#### PCAP-complete child attach 1

- log parent request: `21:50:46.985`
- log parent response: `21:50:47.053`
- log child id request: `21:50:47.705`
- log child id response: `21:50:47.790`
- parent ipv6: `fe80:0:0:0:2c63:3085:b51a:867e`
- parent extaddr: `2e633085b51a867e`
- parent rloc16: `0x4400`
- child extaddr: `7e11089540fc72cd`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **65 ms**
- Response -> Child ID Request: **685 ms**
- Child ID Request -> Response: **61 ms**
- Full Attach: **811 ms**
- pcap parent request: `21:50:46.980` (frame 122)
- pcap parent response: `21:50:47.045` (frame 123)
- pcap child id request: `21:50:47.730` (frame 129)
- pcap child id response: `21:50:47.791` (frame 131)

#### PCAP-complete child attach 2

- log parent request: `21:54:48.001`
- log parent response: `21:54:48.398`
- log child id request: `21:54:48.717`
- log child id response: `21:54:48.816`
- parent ipv6: `fe80:0:0:0:947d:139:e6e2:28b0`
- parent extaddr: `967d0139e6e228b0`
- parent rloc16: `0xcc00`
- child extaddr: `7e11089540fc72cd`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **398 ms**
- Response -> Child ID Request: **352 ms**
- Child ID Request -> Response: **75 ms**
- Full Attach: **825 ms**
- pcap parent request: `21:54:48.001` (frame 342)
- pcap parent response: `21:54:48.399` (frame 343)
- pcap child id request: `21:54:48.751` (frame 347)
- pcap child id response: `21:54:48.826` (frame 349)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 45: 16, seq 46: 16, seq 47: 16, seq 48: 16
- failed tx by dst: `2e633085b51a867e`: 61

### `stock_child_20260624-215658-run03.log`

- child extaddr: `2263869f6640a373`

#### PCAP-complete child attach 1

- log parent request: `22:02:44.617`
- log parent response: `22:02:44.942`
- log child id request: `22:02:45.336`
- log child id response: `22:02:45.432`
- parent ipv6: `fe80:0:0:0:fc07:680f:5318:6e2d`
- parent extaddr: `fe07680f53186e2d`
- parent rloc16: `0x0c00`
- child extaddr: `2263869f6640a373`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **327 ms**
- Response -> Child ID Request: **424 ms**
- Child ID Request -> Response: **75 ms**
- Full Attach: **826 ms**
- pcap parent request: `22:02:44.607` (frame 130)
- pcap parent response: `22:02:44.934` (frame 131)
- pcap child id request: `22:02:45.358` (frame 137)
- pcap child id response: `22:02:45.433` (frame 139)

#### PCAP-complete child attach 2

- log parent request: `22:06:45.398`
- log parent response: `22:06:45.757`
- log child id request: `22:06:46.108`
- log child id response: `22:06:46.199`
- parent ipv6: `fe80:0:0:0:1471:ac57:bb18:5d06`
- parent extaddr: `1671ac57bb185d06`
- parent rloc16: `0x5000`
- child extaddr: `2263869f6640a373`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **362 ms**
- Response -> Child ID Request: **387 ms**
- Child ID Request -> Response: **65 ms**
- Full Attach: **814 ms**
- pcap parent request: `22:06:45.388` (frame 349)
- pcap parent response: `22:06:45.750` (frame 350)
- pcap child id request: `22:06:46.137` (frame 354)
- pcap child id response: `22:06:46.202` (frame 356)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 208: 16, seq 209: 16, seq 210: 16, seq 211: 16
- failed tx by dst: `fe07680f53186e2d`: 56

### `stock_child_20260624-220856-run04.log`

- child extaddr: `b6e03cfba9ce55f1`

#### PCAP-complete child attach 1

- log parent request: `22:14:42.206`
- log parent response: `22:14:42.309`
- log child id request: `22:14:42.924`
- log child id response: `22:14:43.011`
- parent ipv6: `fe80:0:0:0:9c57:5002:c593:eaac`
- parent extaddr: `9e575002c593eaac`
- parent rloc16: `0x0400`
- child extaddr: `b6e03cfba9ce55f1`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **102 ms**
- Response -> Child ID Request: **650 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **814 ms**
- pcap parent request: `22:14:42.196` (frame 126)
- pcap parent response: `22:14:42.298` (frame 127)
- pcap child id request: `22:14:42.948` (frame 133)
- pcap child id response: `22:14:43.010` (frame 135)

#### PCAP-complete child attach 2

- log parent request: `22:18:42.920`
- log parent response: `22:18:42.967`
- log child id request: `22:18:43.639`
- log child id response: `22:18:43.728`
- parent ipv6: `fe80:0:0:0:5c84:729d:ee06:9b5f`
- parent extaddr: `5e84729dee069b5f`
- parent rloc16: `0xc800`
- child extaddr: `b6e03cfba9ce55f1`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **45 ms**
- Response -> Child ID Request: **706 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **815 ms**
- pcap parent request: `22:18:42.918` (frame 346)
- pcap parent response: `22:18:42.963` (frame 347)
- pcap child id request: `22:18:43.669` (frame 351)
- pcap child id response: `22:18:43.733` (frame 353)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 243: 16, seq 244: 16, seq 245: 16, seq 246: 16
- failed tx by dst: `9e575002c593eaac`: 61

### `stock_child_20260624-222054-run05.log`

- child extaddr: `aae93e2f676b2235`

#### PCAP-complete child attach 1

- log parent request: `22:26:39.577`
- log parent response: `22:26:39.985`
- log child id request: `22:26:40.346`
- log child id response: `22:26:40.433`
- parent ipv6: `fe80:0:0:0:20b6:715e:a84b:e33a`
- parent extaddr: `22b6715ea84be33a`
- parent rloc16: `0x9800`
- child extaddr: `aae93e2f676b2235`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **353 ms**
- Response -> Child ID Request: **395 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **811 ms**
- pcap parent request: `22:26:39.622` (frame 134)
- pcap parent response: `22:26:39.975` (frame 135)
- pcap child id request: `22:26:40.370` (frame 141)
- pcap child id response: `22:26:40.433` (frame 143)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260624-222649-run06.log`

- child extaddr: `d22fc3f4d4afc346`

#### PCAP-complete child attach 1

- log parent request: `22:32:35.152`
- log parent response: `22:32:35.248`
- log child id request: `22:32:35.923`
- log child id response: `22:32:36.010`
- parent ipv6: `fe80:0:0:0:94a7:f3b1:56ed:1d1d`
- parent extaddr: `96a7f3b156ed1d1d`
- parent rloc16: `0x0000`
- child extaddr: `d22fc3f4d4afc346`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **45 ms**
- Response -> Child ID Request: **707 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **816 ms**
- pcap parent request: `22:32:35.194` (frame 127)
- pcap parent response: `22:32:35.239` (frame 128)
- pcap child id request: `22:32:35.946` (frame 134)
- pcap child id response: `22:32:36.010` (frame 136)

#### PCAP-complete child attach 2

- log parent request: `22:36:36.021`
- log parent response: `22:36:36.369`
- log child id request: `22:36:36.738`
- log child id response: `22:36:36.835`
- parent ipv6: `fe80:0:0:0:a43e:1260:f89f:d6fb`
- parent extaddr: `a63e1260f89fd6fb`
- parent rloc16: `0xb800`
- child extaddr: `d22fc3f4d4afc346`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **350 ms**
- Response -> Child ID Request: **399 ms**
- Child ID Request -> Response: **76 ms**
- Full Attach: **825 ms**
- pcap parent request: `22:36:36.020` (frame 346)
- pcap parent response: `22:36:36.370` (frame 347)
- pcap child id request: `22:36:36.769` (frame 351)
- pcap child id response: `22:36:36.845` (frame 353)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 73: 16, seq 74: 16, seq 75: 16, seq 76: 16
- failed tx by dst: `96a7f3b156ed1d1d`: 61

### `stock_child_20260624-223847-run07.log`

- child extaddr: `66b100167912d0a6`

#### PCAP-complete child attach 1

- log parent request: `22:44:33.214`
- log parent response: `22:44:33.271`
- log child id request: `22:44:33.931`
- log child id response: `22:44:34.030`
- parent ipv6: `fe80:0:0:0:4c06:81d7:df6b:577e`
- parent extaddr: `4e0681d7df6b577e`
- parent rloc16: `0x3800`
- child extaddr: `66b100167912d0a6`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **58 ms**
- Response -> Child ID Request: **693 ms**
- Child ID Request -> Response: **74 ms**
- Full Attach: **825 ms**
- pcap parent request: `22:44:33.206` (frame 131)
- pcap parent response: `22:44:33.264` (frame 132)
- pcap child id request: `22:44:33.957` (frame 139)
- pcap child id response: `22:44:34.031` (frame 141)

#### PCAP-complete child attach 2

- log parent request: `22:48:34.274`
- log parent response: `22:48:34.409`
- log child id request: `22:48:35.092`
- log child id response: `22:48:35.142`
- parent ipv6: `fe80:0:0:0:e0ee:1a53:2902:b31b`
- parent extaddr: `e2ee1a532902b31b`
- parent rloc16: `0x2000`
- child extaddr: `66b100167912d0a6`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **72 ms**
- Response -> Child ID Request: **678 ms**
- Child ID Request -> Response: **66 ms**
- Full Attach: **816 ms**
- pcap parent request: `22:48:34.331` (frame 336)
- pcap parent response: `22:48:34.403` (frame 337)
- pcap child id request: `22:48:35.081` (frame 341)
- pcap child id response: `22:48:35.147` (frame 343)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 87: 16, seq 88: 16, seq 89: 16, seq 90: 16
- failed tx by dst: `4e0681d7df6b577e`: 54

### `stock_child_20260624-225044-run08.log`

- child extaddr: `9632ffb392e74266`

#### PCAP-complete child attach 1

- log parent request: `22:56:30.842`
- log parent response: `22:56:30.977`
- log child id request: `22:56:31.612`
- log child id response: `22:56:31.698`
- parent ipv6: `fe80:0:0:0:e0f6:5a9:5b03:84aa`
- parent extaddr: `e2f605a95b0384aa`
- parent rloc16: `0x0800`
- child extaddr: `9632ffb392e74266`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **84 ms**
- Response -> Child ID Request: **668 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **814 ms**
- pcap parent request: `22:56:30.884` (frame 127)
- pcap parent response: `22:56:30.968` (frame 128)
- pcap child id request: `22:56:31.636` (frame 134)
- pcap child id response: `22:56:31.698` (frame 136)

#### PCAP-complete child attach 2

- log parent request: `23:00:31.326`
- log parent response: `23:00:31.606`
- log child id request: `23:00:32.045`
- log child id response: `23:00:32.141`
- parent ipv6: `fe80:0:0:0:88de:b5c4:e751:df59`
- parent extaddr: `8adeb5c4e751df59`
- parent rloc16: `0x5800`
- child extaddr: `9632ffb392e74266`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **280 ms**
- Response -> Child ID Request: **469 ms**
- Child ID Request -> Response: **75 ms**
- Full Attach: **824 ms**
- pcap parent request: `23:00:31.328` (frame 346)
- pcap parent response: `23:00:31.608` (frame 347)
- pcap child id request: `23:00:32.077` (frame 351)
- pcap child id response: `23:00:32.152` (frame 353)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 115: 16, seq 116: 16, seq 117: 16, seq 118: 16
- failed tx by dst: `e2f605a95b0384aa`: 62

### `stock_child_20260624-230242-run09.log`

- child extaddr: `82e6e607367b723a`

#### PCAP-complete child attach 1

- log parent request: `23:08:28.448`
- log parent response: `23:08:28.493`
- log child id request: `23:08:29.166`
- log child id response: `23:08:29.255`
- parent ipv6: `fe80:0:0:0:c0f9:955b:4311:44a5`
- parent extaddr: `c2f9955b431144a5`
- parent rloc16: `0xe000`
- child extaddr: `82e6e607367b723a`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **44 ms**
- Response -> Child ID Request: **709 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **816 ms**
- pcap parent request: `23:08:28.440` (frame 120)
- pcap parent response: `23:08:28.484` (frame 121)
- pcap child id request: `23:08:29.193` (frame 128)
- pcap child id response: `23:08:29.256` (frame 130)

#### PCAP-complete child attach 2

- log parent request: `23:12:29.416`
- log parent response: `23:12:29.484`
- log child id request: `23:12:30.135`
- log child id response: `23:12:30.232`
- parent ipv6: `fe80:0:0:0:8401:b0e6:fa16:6a81`
- parent extaddr: `8601b0e6fa166a81`
- parent rloc16: `0x0800`
- child extaddr: `82e6e607367b723a`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **69 ms**
- Response -> Child ID Request: **682 ms**
- Child ID Request -> Response: **75 ms**
- Full Attach: **826 ms**
- pcap parent request: `23:12:29.417` (frame 341)
- pcap parent response: `23:12:29.486` (frame 342)
- pcap child id request: `23:12:30.168` (frame 346)
- pcap child id response: `23:12:30.243` (frame 348)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 184: 16, seq 185: 16, seq 186: 16, seq 187: 16
- failed tx by dst: `c2f9955b431144a5`: 58

### `stock_child_20260624-231440-run10.log`

- child extaddr: `7a68d5ad5ccd3408`

#### PCAP-complete child attach 1

- log parent request: `23:20:25.661`
- log parent response: `23:20:25.719`
- log child id request: `23:20:26.380`
- log child id response: `23:20:26.464`
- parent ipv6: `fe80:0:0:0:5822:4d80:64bd:dff2`
- parent extaddr: `5a224d8064bddff2`
- parent rloc16: `0x4c00`
- child extaddr: `7a68d5ad5ccd3408`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **58 ms**
- Response -> Child ID Request: **692 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **812 ms**
- pcap parent request: `23:20:25.654` (frame 129)
- pcap parent response: `23:20:25.712` (frame 130)
- pcap child id request: `23:20:26.404` (frame 136)
- pcap child id response: `23:20:26.466` (frame 138)

#### PCAP-complete child attach 2

- log parent request: `23:24:26.045`
- log parent response: `23:24:26.366`
- log child id request: `23:24:26.763`
- log child id response: `23:24:26.860`
- parent ipv6: `fe80:0:0:0:64a2:4ba2:5ba1:8ded`
- parent extaddr: `66a24ba25ba18ded`
- parent rloc16: `0x5400`
- child extaddr: `7a68d5ad5ccd3408`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **322 ms**
- Response -> Child ID Request: **429 ms**
- Child ID Request -> Response: **75 ms**
- Full Attach: **826 ms**
- pcap parent request: `23:24:26.046` (frame 346)
- pcap parent response: `23:24:26.368` (frame 347)
- pcap child id request: `23:24:26.797` (frame 351)
- pcap child id response: `23:24:26.872` (frame 353)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 194: 16, seq 195: 16, seq 196: 16, seq 197: 16
- failed tx by dst: `5a224d8064bddff2`: 63

### `stock_child_20260624-232637-run11.log`

- child extaddr: `3e17d3ebe26ee8e4`

#### PCAP-complete child attach 1

- log parent request: `23:32:23.106`
- log parent response: `23:32:23.457`
- log child id request: `23:32:23.874`
- log child id response: `23:32:23.965`
- parent ipv6: `fe80:0:0:0:1cdf:3580:3614:873c`
- parent extaddr: `1edf35803614873c`
- parent rloc16: `0x8400`
- child extaddr: `3e17d3ebe26ee8e4`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **292 ms**
- Response -> Child ID Request: **453 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **809 ms**
- pcap parent request: `23:32:23.155` (frame 125)
- pcap parent response: `23:32:23.447` (frame 126)
- pcap child id request: `23:32:23.900` (frame 132)
- pcap child id response: `23:32:23.964` (frame 134)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260624-233233-run12.log`

- child extaddr: `7a006a7a78abd53c`

#### PCAP-complete child attach 1

- log parent request: `23:38:18.996`
- log parent response: `23:38:19.143`
- log child id request: `23:38:19.716`
- log child id response: `23:38:19.815`
- parent ipv6: `fe80:0:0:0:2f:d2b7:4c43:d33f`
- parent extaddr: `022fd2b74c43d33f`
- parent rloc16: `0xf400`
- child extaddr: `7a006a7a78abd53c`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **146 ms**
- Response -> Child ID Request: **605 ms**
- Child ID Request -> Response: **75 ms**
- Full Attach: **826 ms**
- pcap parent request: `23:38:18.989` (frame 132)
- pcap parent response: `23:38:19.135` (frame 133)
- pcap child id request: `23:38:19.740` (frame 139)
- pcap child id response: `23:38:19.815` (frame 141)

#### PCAP-complete child attach 2

- log parent request: `23:42:20.155`
- log parent response: `23:42:20.516`
- log child id request: `23:42:20.908`
- log child id response: `23:42:20.952`
- parent ipv6: `fe80:0:0:0:4c8f:a151:b589:2178`
- parent extaddr: `4e8fa151b5892178`
- parent rloc16: `0x9800`
- child extaddr: `7a006a7a78abd53c`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **365 ms**
- Response -> Child ID Request: **384 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **812 ms**
- pcap parent request: `23:42:20.144` (frame 352)
- pcap parent response: `23:42:20.509` (frame 353)
- pcap child id request: `23:42:20.893` (frame 357)
- pcap child id response: `23:42:20.956` (frame 359)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 45: 16, seq 46: 16, seq 47: 16, seq 48: 16
- failed tx by dst: `022fd2b74c43d33f`: 44

### `stock_child_20260624-234430-run13.log`

- child extaddr: `f2968c326c49de57`

#### PCAP-complete child attach 1

- log parent request: `23:50:16.035`
- log parent response: `23:50:16.207`
- log child id request: `23:50:16.803`
- log child id response: `23:50:16.903`
- parent ipv6: `fe80:0:0:0:486d:e315:2fe6:221d`
- parent extaddr: `4a6de3152fe6221d`
- parent rloc16: `0xec00`
- child extaddr: `f2968c326c49de57`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **117 ms**
- Response -> Child ID Request: **628 ms**
- Child ID Request -> Response: **76 ms**
- Full Attach: **821 ms**
- pcap parent request: `23:50:16.081` (frame 128)
- pcap parent response: `23:50:16.198` (frame 129)
- pcap child id request: `23:50:16.826` (frame 135)
- pcap child id response: `23:50:16.902` (frame 137)

#### PCAP-complete child attach 2

- log parent request: `23:54:16.897`
- log parent response: `23:54:16.940`
- log child id request: `23:54:17.608`
- log child id response: `23:54:17.700`
- parent ipv6: `fe80:0:0:0:1423:4d8f:39a2:5187`
- parent extaddr: `16234d8f39a25187`
- parent rloc16: `0x1000`
- child extaddr: `f2968c326c49de57`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **45 ms**
- Response -> Child ID Request: **706 ms**
- Child ID Request -> Response: **66 ms**
- Full Attach: **817 ms**
- pcap parent request: `23:54:16.886` (frame 344)
- pcap parent response: `23:54:16.931` (frame 345)
- pcap child id request: `23:54:17.637` (frame 349)
- pcap child id response: `23:54:17.703` (frame 351)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 142: 16, seq 143: 16, seq 144: 16, seq 145: 16
- failed tx by dst: `4a6de3152fe6221d`: 49

### `stock_child_20260624-235628-run14.log`

- child extaddr: `52f0cb291a71e435`

#### PCAP-complete child attach 1

- log parent request: `00:02:14.029`
- log parent response: `00:02:14.317`
- log child id request: `00:02:14.800`
- log child id response: `00:02:14.905`
- parent ipv6: `fe80:0:0:0:ecd4:ad96:d29c:3491`
- parent extaddr: `eed4ad96d29c3491`
- parent rloc16: `0x3000`
- child extaddr: `52f0cb291a71e435`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **238 ms**
- Response -> Child ID Request: **513 ms**
- Child ID Request -> Response: **84 ms**
- Full Attach: **835 ms**
- pcap parent request: `00:02:14.070` (frame 131)
- pcap parent response: `00:02:14.308` (frame 133)
- pcap child id request: `00:02:14.821` (frame 139)
- pcap child id response: `00:02:14.905` (frame 141)

#### PCAP-complete child attach 2

- log parent request: `00:06:14.813`
- log parent response: `00:06:15.301`
- log child id request: `00:06:15.524`
- log child id response: `00:06:15.615`
- parent ipv6: `fe80:0:0:0:3478:c124:3a0f:3e0c`
- parent extaddr: `3678c1243a0f3e0c`
- parent rloc16: `0x6c00`
- child extaddr: `52f0cb291a71e435`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **490 ms**
- Response -> Child ID Request: **260 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **814 ms**
- pcap parent request: `00:06:14.803` (frame 352)
- pcap parent response: `00:06:15.293` (frame 353)
- pcap child id request: `00:06:15.553` (frame 357)
- pcap child id response: `00:06:15.617` (frame 359)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 108: 16, seq 109: 16, seq 110: 16, seq 111: 16
- failed tx by dst: `eed4ad96d29c3491`: 50

### `stock_child_20260625-000825-run15.log`

- child extaddr: `a26dc2be21e9df9c`

#### PCAP-complete child attach 1

- log parent request: `00:14:11.576`
- log parent response: `00:14:11.838`
- log child id request: `00:14:12.293`
- log child id response: `00:14:12.393`
- parent ipv6: `fe80:0:0:0:e0a1:34b6:7ffb:c029`
- parent extaddr: `e2a134b67ffbc029`
- parent rloc16: `0x5000`
- child extaddr: `a26dc2be21e9df9c`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **263 ms**
- Response -> Child ID Request: **488 ms**
- Child ID Request -> Response: **76 ms**
- Full Attach: **827 ms**
- pcap parent request: `00:14:11.567` (frame 133)
- pcap parent response: `00:14:11.830` (frame 134)
- pcap child id request: `00:14:12.318` (frame 140)
- pcap child id response: `00:14:12.394` (frame 142)

#### PCAP-complete child attach 2

- log parent request: `00:18:12.447`
- log parent response: `00:18:12.539`
- log child id request: `00:18:13.201`
- log child id response: `00:18:13.249`
- parent ipv6: `fe80:0:0:0:a402:3e62:2039:914`
- parent extaddr: `a6023e6220390914`
- parent rloc16: `0xbc00`
- child extaddr: `a26dc2be21e9df9c`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **95 ms**
- Response -> Child ID Request: **654 ms**
- Child ID Request -> Response: **67 ms**
- Full Attach: **816 ms**
- pcap parent request: `00:18:12.437` (frame 352)
- pcap parent response: `00:18:12.532` (frame 353)
- pcap child id request: `00:18:13.186` (frame 357)
- pcap child id response: `00:18:13.253` (frame 359)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 51: 16, seq 52: 16, seq 53: 16, seq 54: 16
- failed tx by dst: `e2a134b67ffbc029`: 55

### `stock_child_20260625-002023-run16.log`

- child extaddr: `262655b36a04d8b4`

#### PCAP-complete child attach 1

- log parent request: `00:26:08.933`
- log parent response: `00:26:09.050`
- log child id request: `00:26:09.701`
- log child id response: `00:26:09.790`
- parent ipv6: `fe80:0:0:0:71:e1ef:2509:e864`
- parent extaddr: `0271e1ef2509e864`
- parent rloc16: `0xe000`
- child extaddr: `262655b36a04d8b4`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **56 ms**
- Response -> Child ID Request: **689 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **809 ms**
- pcap parent request: `00:26:08.980` (frame 124)
- pcap parent response: `00:26:09.036` (frame 125)
- pcap child id request: `00:26:09.725` (frame 131)
- pcap child id response: `00:26:09.789` (frame 133)

#### PCAP-complete child attach 2

- log parent request: `00:30:09.426`
- log parent response: `00:30:09.528`
- log child id request: `00:30:10.144`
- log child id response: `00:30:10.231`
- parent ipv6: `fe80:0:0:0:8ce1:4ee7:ee82:5d1d`
- parent extaddr: `8ee14ee7ee825d1d`
- parent rloc16: `0x6c00`
- child extaddr: `262655b36a04d8b4`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **100 ms**
- Response -> Child ID Request: **650 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **814 ms**
- pcap parent request: `00:30:09.424` (frame 346)
- pcap parent response: `00:30:09.524` (frame 347)
- pcap child id request: `00:30:10.174` (frame 351)
- pcap child id response: `00:30:10.238` (frame 353)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 211: 16, seq 212: 16, seq 213: 16, seq 214: 16
- failed tx by dst: `0271e1ef2509e864`: 62

### `stock_child_20260625-003221-run17.log`

- child extaddr: `aec5dac150fbb6d0`

#### PCAP-complete child attach 1

- log parent request: `00:38:07.155`
- log parent response: `00:38:07.616`
- log child id request: `00:38:07.925`
- log child id response: `00:38:08.014`
- parent ipv6: `fe80:0:0:0:78e8:901:73b8:351c`
- parent extaddr: `7ae8090173b8351c`
- parent rloc16: `0x3800`
- child extaddr: `aec5dac150fbb6d0`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **410 ms**
- Response -> Child ID Request: **341 ms**
- Child ID Request -> Response: **65 ms**
- Full Attach: **816 ms**
- pcap parent request: `00:38:07.196` (frame 133)
- pcap parent response: `00:38:07.606` (frame 135)
- pcap child id request: `00:38:07.947` (frame 141)
- pcap child id response: `00:38:08.012` (frame 143)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260625-003816-run18.log`

- child extaddr: `dec08761ece9a7a7`

#### PCAP-complete child attach 1

- log parent request: `00:44:02.088`
- log parent response: `00:44:02.369`
- log child id request: `00:44:02.857`
- log child id response: `00:44:02.947`
- parent ipv6: `fe80:0:0:0:e8cc:4626:536b:88dc`
- parent extaddr: `eacc4626536b88dc`
- parent rloc16: `0xbc00`
- child extaddr: `dec08761ece9a7a7`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **197 ms**
- Response -> Child ID Request: **521 ms**
- Child ID Request -> Response: **65 ms**
- Full Attach: **783 ms**
- pcap parent request: `00:44:02.164` (frame 127)
- pcap parent response: `00:44:02.361` (frame 128)
- pcap child id request: `00:44:02.882` (frame 134)
- pcap child id response: `00:44:02.947` (frame 136)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260625-004412-run19.log`

- child extaddr: `cea7a1025ed5d59b`

#### PCAP-complete child attach 1

- log parent request: `00:49:58.174`
- log parent response: `00:49:58.219`
- log child id request: `00:49:58.891`
- log child id response: `00:49:58.984`
- parent ipv6: `fe80:0:0:0:cb0:1354:cae8:4135`
- parent extaddr: `0eb01354cae84135`
- parent rloc16: `0xe800`
- child extaddr: `cea7a1025ed5d59b`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **45 ms**
- Response -> Child ID Request: **707 ms**
- Child ID Request -> Response: **67 ms**
- Full Attach: **819 ms**
- pcap parent request: `00:49:58.165` (frame 128)
- pcap parent response: `00:49:58.210` (frame 129)
- pcap child id request: `00:49:58.917` (frame 135)
- pcap child id response: `00:49:58.984` (frame 137)

#### PCAP-complete child attach 2

- log parent request: `00:53:58.561`
- log parent response: `00:53:58.827`
- log child id request: `00:53:59.280`
- log child id response: `00:53:59.377`
- parent ipv6: `fe80:0:0:0:b0af:d528:4274:28d6`
- parent extaddr: `b2afd528427428d6`
- parent rloc16: `0x5000`
- child extaddr: `cea7a1025ed5d59b`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **267 ms**
- Response -> Child ID Request: **484 ms**
- Child ID Request -> Response: **75 ms**
- Full Attach: **826 ms**
- pcap parent request: `00:53:58.561` (frame 346)
- pcap parent response: `00:53:58.828` (frame 347)
- pcap child id request: `00:53:59.312` (frame 351)
- pcap child id response: `00:53:59.387` (frame 353)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 194: 16, seq 195: 16, seq 196: 16, seq 197: 16
- failed tx by dst: `0eb01354cae84135`: 61

### `stock_child_20260625-005609-run20.log`

- child extaddr: `b22e95cc51e4a5bd`

#### PCAP-complete child attach 1

- log parent request: `01:01:55.491`
- log parent response: `01:01:55.714`
- log child id request: `01:01:56.260`
- log child id response: `01:01:56.347`
- parent ipv6: `fe80:0:0:0:f43d:b6c0:6b29:f27b`
- parent extaddr: `f63db6c06b29f27b`
- parent rloc16: `0x1c00`
- child extaddr: `b22e95cc51e4a5bd`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **171 ms**
- Response -> Child ID Request: **580 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **814 ms**
- pcap parent request: `01:01:55.533` (frame 127)
- pcap parent response: `01:01:55.704` (frame 128)
- pcap child id request: `01:01:56.284` (frame 134)
- pcap child id response: `01:01:56.347` (frame 136)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260625-010205-run21.log`

- child extaddr: `d690e6208052dc59`

#### PCAP-complete child attach 1

- log parent request: `01:07:50.592`
- log parent response: `01:07:50.803`
- log child id request: `01:07:51.312`
- log child id response: `01:07:51.408`
- parent ipv6: `fe80:0:0:0:58fb:6a81:f50b:e4d2`
- parent extaddr: `5afb6a81f50be4d2`
- parent rloc16: `0xe000`
- child extaddr: `d690e6208052dc59`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **209 ms**
- Response -> Child ID Request: **540 ms**
- Child ID Request -> Response: **74 ms**
- Full Attach: **823 ms**
- pcap parent request: `01:07:50.588` (frame 126)
- pcap parent response: `01:07:50.797` (frame 127)
- pcap child id request: `01:07:51.337` (frame 133)
- pcap child id response: `01:07:51.411` (frame 135)

#### PCAP-complete child attach 2

- log parent request: `01:11:51.566`
- log parent response: `01:11:51.679`
- log child id request: `01:11:52.277`
- log child id response: `01:11:52.367`
- parent ipv6: `fe80:0:0:0:248d:5f51:6446:b41b`
- parent extaddr: `268d5f516446b41b`
- parent rloc16: `0xe400`
- child extaddr: `d690e6208052dc59`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **112 ms**
- Response -> Child ID Request: **637 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **812 ms**
- pcap parent request: `01:11:51.561` (frame 343)
- pcap parent response: `01:11:51.673` (frame 344)
- pcap child id request: `01:11:52.310` (frame 348)
- pcap child id response: `01:11:52.373` (frame 350)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 10: 16, seq 11: 16, seq 12: 16, seq 13: 16
- failed tx by dst: `5afb6a81f50be4d2`: 50

### `stock_child_20260625-011402-run22.log`

- child extaddr: `ce3e3ca3098867ef`

#### PCAP-complete child attach 1

- log parent request: `01:19:48.198`
- log parent response: `01:19:48.353`
- log child id request: `01:19:48.916`
- log child id response: `01:19:49.003`
- parent ipv6: `fe80:0:0:0:6c86:3001:a50d:234`
- parent extaddr: `6e863001a50d0234`
- parent rloc16: `0xe400`
- child extaddr: `ce3e3ca3098867ef`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **154 ms**
- Response -> Child ID Request: **596 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **813 ms**
- pcap parent request: `01:19:48.190` (frame 111)
- pcap parent response: `01:19:48.344` (frame 112)
- pcap child id request: `01:19:48.940` (frame 118)
- pcap child id response: `01:19:49.003` (frame 120)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260625-011957-run23.log`

- child extaddr: `32a3ca9a2a89df8e`

#### PCAP-complete child attach 1

- log parent request: `01:25:43.245`
- log parent response: `01:25:43.382`
- log child id request: `01:25:44.015`
- log child id response: `01:25:44.106`
- parent ipv6: `fe80:0:0:0:c05c:9fe6:a84c:69dc`
- parent extaddr: `c25c9fe6a84c69dc`
- parent rloc16: `0xf000`
- child extaddr: `32a3ca9a2a89df8e`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **85 ms**
- Response -> Child ID Request: **665 ms**
- Child ID Request -> Response: **68 ms**
- Full Attach: **818 ms**
- pcap parent request: `01:25:43.290` (frame 134)
- pcap parent response: `01:25:43.375` (frame 135)
- pcap child id request: `01:25:44.040` (frame 141)
- pcap child id response: `01:25:44.108` (frame 143)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260625-012552-run24.log`

- child extaddr: `667feb91a2646154`

#### PCAP-complete child attach 1

- log parent request: `01:31:39.076`
- log parent response: `01:31:39.247`
- log child id request: `01:31:39.796`
- log child id response: `01:31:39.892`
- parent ipv6: `fe80:0:0:0:a07e:da71:df35:5929`
- parent extaddr: `a27eda71df355929`
- parent rloc16: `0x9c00`
- child extaddr: `667feb91a2646154`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **172 ms**
- Response -> Child ID Request: **579 ms**
- Child ID Request -> Response: **74 ms**
- Full Attach: **825 ms**
- pcap parent request: `01:31:39.070` (frame 130)
- pcap parent response: `01:31:39.242` (frame 131)
- pcap child id request: `01:31:39.821` (frame 137)
- pcap child id response: `01:31:39.895` (frame 139)

#### PCAP-complete child attach 2

- log parent request: `01:35:40.131`
- log parent response: `01:35:40.196`
- log child id request: `01:35:40.842`
- log child id response: `01:35:40.932`
- parent ipv6: `fe80:0:0:0:a06b:3896:e8fa:2304`
- parent extaddr: `a26b3896e8fa2304`
- parent rloc16: `0x0800`
- child extaddr: `667feb91a2646154`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **67 ms**
- Response -> Child ID Request: **683 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **814 ms**
- pcap parent request: `01:35:40.125` (frame 345)
- pcap parent response: `01:35:40.192` (frame 346)
- pcap child id request: `01:35:40.875` (frame 350)
- pcap child id response: `01:35:40.939` (frame 352)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 160: 16, seq 161: 16, seq 162: 16, seq 163: 16
- failed tx by dst: `a27eda71df355929`: 53

### `stock_child_20260625-013750-run25.log`

- child extaddr: `1a6d09e689cdad0e`

#### PCAP-complete child attach 1

- log parent request: `01:43:36.166`
- log parent response: `01:43:36.290`
- log child id request: `01:43:36.885`
- log child id response: `01:43:36.980`
- parent ipv6: `fe80:0:0:0:d83c:9d05:e24e:a104`
- parent extaddr: `da3c9d05e24ea104`
- parent rloc16: `0xf000`
- child extaddr: `1a6d09e689cdad0e`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **125 ms**
- Response -> Child ID Request: **625 ms**
- Child ID Request -> Response: **74 ms**
- Full Attach: **824 ms**
- pcap parent request: `01:43:36.159` (frame 128)
- pcap parent response: `01:43:36.284` (frame 129)
- pcap child id request: `01:43:36.909` (frame 135)
- pcap child id response: `01:43:36.983` (frame 137)

#### PCAP-complete child attach 2

- log parent request: `01:47:37.128`
- log parent response: `01:47:37.179`
- log child id request: `01:47:37.838`
- log child id response: `01:47:37.928`
- parent ipv6: `fe80:0:0:0:c8c8:1612:eab5:2d64`
- parent extaddr: `cac81612eab52d64`
- parent rloc16: `0x7800`
- child extaddr: `1a6d09e689cdad0e`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **53 ms**
- Response -> Child ID Request: **696 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **813 ms**
- pcap parent request: `01:47:37.120` (frame 347)
- pcap parent response: `01:47:37.173` (frame 348)
- pcap child id request: `01:47:37.869` (frame 352)
- pcap child id response: `01:47:37.933` (frame 354)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 51: 16, seq 52: 16, seq 53: 16, seq 54: 16
- failed tx by dst: `da3c9d05e24ea104`: 51

### `stock_child_20260625-014948-run26.log`

- child extaddr: `b69845f6bf63dc35`

#### PCAP-complete child attach 1

- log parent request: `01:55:33.599`
- log parent response: `01:55:33.644`
- log child id request: `01:55:34.319`
- log child id response: `01:55:34.407`
- parent ipv6: `fe80:0:0:0:c8cc:e4c6:6986:aadd`
- parent extaddr: `cacce4c66986aadd`
- parent rloc16: `0x5400`
- child extaddr: `b69845f6bf63dc35`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **45 ms**
- Response -> Child ID Request: **707 ms**
- Child ID Request -> Response: **65 ms**
- Full Attach: **817 ms**
- pcap parent request: `01:55:33.589` (frame 131)
- pcap parent response: `01:55:33.634` (frame 132)
- pcap child id request: `01:55:34.341` (frame 138)
- pcap child id response: `01:55:34.406` (frame 140)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260625-015543-run27.log`

- child extaddr: `ee238eeec80e483b`

#### PCAP-complete child attach 1

- log parent request: `02:01:28.976`
- log parent response: `02:01:29.210`
- log child id request: `02:01:29.694`
- log child id response: `02:01:29.781`
- parent ipv6: `fe80:0:0:0:ec26:21c8:9af6:1754`
- parent extaddr: `ee2621c89af61754`
- parent rloc16: `0x5800`
- child extaddr: `ee238eeec80e483b`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **233 ms**
- Response -> Child ID Request: **517 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **814 ms**
- pcap parent request: `02:01:28.966` (frame 129)
- pcap parent response: `02:01:29.199` (frame 130)
- pcap child id request: `02:01:29.716` (frame 137)
- pcap child id response: `02:01:29.780` (frame 139)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260625-020138-run28.log`

- child extaddr: `8ebf97b5aa482c2c`

#### PCAP-complete child attach 1

- log parent request: `02:07:24.654`
- log parent response: `02:07:24.756`
- log child id request: `02:07:25.371`
- log child id response: `02:07:25.461`
- parent ipv6: `fe80:0:0:0:7c30:13c6:71b5:224f`
- parent extaddr: `7e3013c671b5224f`
- parent rloc16: `0xbc00`
- child extaddr: `8ebf97b5aa482c2c`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **101 ms**
- Response -> Child ID Request: **651 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **815 ms**
- pcap parent request: `02:07:24.644` (frame 133)
- pcap parent response: `02:07:24.745` (frame 134)
- pcap child id request: `02:07:25.396` (frame 140)
- pcap child id response: `02:07:25.459` (frame 142)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260625-020733-run29.log`

- child extaddr: `8eb61a9ad50b3914`

#### PCAP-complete child attach 1

- log parent request: `02:13:19.470`
- log parent response: `02:13:19.571`
- log child id request: `02:13:20.189`
- log child id response: `02:13:20.286`
- parent ipv6: `fe80:0:0:0:9841:4b90:de3c:fa21`
- parent extaddr: `9a414b90de3cfa21`
- parent rloc16: `0x2800`
- child extaddr: `8eb61a9ad50b3914`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **103 ms**
- Response -> Child ID Request: **648 ms**
- Child ID Request -> Response: **75 ms**
- Full Attach: **826 ms**
- pcap parent request: `02:13:19.460` (frame 128)
- pcap parent response: `02:13:19.563` (frame 129)
- pcap child id request: `02:13:20.211` (frame 135)
- pcap child id response: `02:13:20.286` (frame 137)

#### PCAP-complete child attach 2

- log parent request: `02:17:20.457`
- log parent response: `02:17:20.646`
- log child id request: `02:17:21.212`
- log child id response: `02:17:21.260`
- parent ipv6: `fe80:0:0:0:5888:ce16:16d1:1829`
- parent extaddr: `5a88ce1616d11829`
- parent rloc16: `0x6c00`
- child extaddr: `8eb61a9ad50b3914`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **192 ms**
- Response -> Child ID Request: **559 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **815 ms**
- pcap parent request: `02:17:20.447` (frame 344)
- pcap parent response: `02:17:20.639` (frame 345)
- pcap child id request: `02:17:21.198` (frame 349)
- pcap child id response: `02:17:21.262` (frame 351)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 250: 16, seq 251: 16, seq 252: 16, seq 253: 16
- failed tx by dst: `9a414b90de3cfa21`: 49

### `stock_child_20260625-021931-run30.log`

- child extaddr: `9a000472aff49cba`

#### PCAP-complete child attach 1

- log parent request: `02:25:16.784`
- log parent response: `02:25:17.025`
- log child id request: `02:25:17.553`
- log child id response: `02:25:17.649`
- parent ipv6: `fe80:0:0:0:dc31:723a:8d2:2569`
- parent extaddr: `de31723a08d22569`
- parent rloc16: `0x7000`
- child extaddr: `9a000472aff49cba`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **192 ms**
- Response -> Child ID Request: **558 ms**
- Child ID Request -> Response: **75 ms**
- Full Attach: **825 ms**
- pcap parent request: `02:25:16.826` (frame 121)
- pcap parent response: `02:25:17.018` (frame 123)
- pcap child id request: `02:25:17.576` (frame 129)
- pcap child id response: `02:25:17.651` (frame 131)

#### PCAP-complete child attach 2

- log parent request: `02:29:17.604`
- log parent response: `02:29:17.913`
- log child id request: `02:29:18.315`
- log child id response: `02:29:18.405`
- parent ipv6: `fe80:0:0:0:a81d:c6b7:213d:f07`
- parent extaddr: `aa1dc6b7213d0f07`
- parent rloc16: `0xd800`
- child extaddr: `9a000472aff49cba`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **312 ms**
- Response -> Child ID Request: **439 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **813 ms**
- pcap parent request: `02:29:17.596` (frame 342)
- pcap parent response: `02:29:17.908` (frame 343)
- pcap child id request: `02:29:18.347` (frame 347)
- pcap child id response: `02:29:18.409` (frame 349)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 51: 16, seq 52: 16, seq 53: 16, seq 54: 16
- failed tx by dst: `de31723a08d22569`: 49

### `stock_child_20260625-023128-run31.log`

- child extaddr: `4e1315fb28eaa5f7`

#### PCAP-complete child attach 1

- log parent request: `02:37:14.441`
- log parent response: `02:37:14.486`
- log child id request: `02:37:15.158`
- log child id response: `02:37:15.247`
- parent ipv6: `fe80:0:0:0:fc84:399b:f01f:4bd3`
- parent extaddr: `fe84399bf01f4bd3`
- parent rloc16: `0xc400`
- child extaddr: `4e1315fb28eaa5f7`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **45 ms**
- Response -> Child ID Request: **704 ms**
- Child ID Request -> Response: **66 ms**
- Full Attach: **815 ms**
- pcap parent request: `02:37:14.433` (frame 133)
- pcap parent response: `02:37:14.478` (frame 134)
- pcap child id request: `02:37:15.182` (frame 140)
- pcap child id response: `02:37:15.248` (frame 142)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260625-023724-run32.log`

- child extaddr: `ce350b0a138abb8e`

#### PCAP-complete child attach 1

- log parent request: `02:43:10.029`
- log parent response: `02:43:10.220`
- log child id request: `02:43:10.746`
- log child id response: `02:43:10.838`
- parent ipv6: `fe80:0:0:0:a0cb:7ef0:28d9:75bb`
- parent extaddr: `a2cb7ef028d975bb`
- parent rloc16: `0x0c00`
- child extaddr: `ce350b0a138abb8e`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **190 ms**
- Response -> Child ID Request: **559 ms**
- Child ID Request -> Response: **69 ms**
- Full Attach: **818 ms**
- pcap parent request: `02:43:10.021` (frame 119)
- pcap parent response: `02:43:10.211` (frame 120)
- pcap child id request: `02:43:10.770` (frame 126)
- pcap child id response: `02:43:10.839` (frame 128)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260625-024319-run33.log`

- child extaddr: `06a8240755c93177`

#### PCAP-complete child attach 1

- log parent request: `02:49:05.190`
- log parent response: `02:49:05.284`
- log child id request: `02:49:05.908`
- log child id response: `02:49:05.998`
- parent ipv6: `fe80:0:0:0:283f:e0b9:eda0:7336`
- parent extaddr: `2a3fe0b9eda07336`
- parent rloc16: `0xd800`
- child extaddr: `06a8240755c93177`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **95 ms**
- Response -> Child ID Request: **655 ms**
- Child ID Request -> Response: **67 ms**
- Full Attach: **817 ms**
- pcap parent request: `02:49:05.183` (frame 124)
- pcap parent response: `02:49:05.278` (frame 125)
- pcap child id request: `02:49:05.933` (frame 132)
- pcap child id response: `02:49:06.000` (frame 134)

#### PCAP-complete child attach 2

- log parent request: `02:53:06.106`
- log parent response: `02:53:06.187`
- log child id request: `02:53:06.824`
- log child id response: `02:53:06.922`
- parent ipv6: `fe80:0:0:0:48bc:3ab4:e1e1:c226`
- parent extaddr: `4abc3ab4e1e1c226`
- parent rloc16: `0xbc00`
- child extaddr: `06a8240755c93177`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **81 ms**
- Response -> Child ID Request: **669 ms**
- Child ID Request -> Response: **75 ms**
- Full Attach: **825 ms**
- pcap parent request: `02:53:06.109` (frame 341)
- pcap parent response: `02:53:06.190` (frame 342)
- pcap child id request: `02:53:06.859` (frame 346)
- pcap child id response: `02:53:06.934` (frame 348)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 89: 16, seq 90: 16, seq 91: 16, seq 92: 16
- failed tx by dst: `2a3fe0b9eda07336`: 61

### `stock_child_20260625-025517-run34.log`

- child extaddr: `fe370911337afb58`

#### PCAP-complete child attach 1

- log parent request: `03:01:02.313`
- log parent response: `03:01:02.522`
- log child id request: `03:01:03.082`
- log child id response: `03:01:03.180`
- parent ipv6: `fe80:0:0:0:a0fd:827c:c18b:d2fd`
- parent extaddr: `a2fd827cc18bd2fd`
- parent rloc16: `0xf400`
- child extaddr: `fe370911337afb58`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **156 ms**
- Response -> Child ID Request: **592 ms**
- Child ID Request -> Response: **75 ms**
- Full Attach: **823 ms**
- pcap parent request: `03:01:02.360` (frame 126)
- pcap parent response: `03:01:02.516` (frame 127)
- pcap child id request: `03:01:03.108` (frame 133)
- pcap child id response: `03:01:03.183` (frame 135)

#### PCAP-complete child attach 2

- log parent request: `03:05:03.156`
- log parent response: `03:05:03.611`
- log child id request: `03:05:03.867`
- log child id response: `03:05:03.958`
- parent ipv6: `fe80:0:0:0:94e2:3c24:d3e6:757a`
- parent extaddr: `96e23c24d3e6757a`
- parent rloc16: `0x1400`
- child extaddr: `fe370911337afb58`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **457 ms**
- Response -> Child ID Request: **293 ms**
- Child ID Request -> Response: **65 ms**
- Full Attach: **815 ms**
- pcap parent request: `03:05:03.148` (frame 343)
- pcap parent response: `03:05:03.605` (frame 344)
- pcap child id request: `03:05:03.898` (frame 349)
- pcap child id response: `03:05:03.963` (frame 351)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 51: 16, seq 52: 16, seq 53: 16, seq 54: 16
- failed tx by dst: `a2fd827cc18bd2fd`: 50

### `stock_child_20260625-030714-run35.log`

- child extaddr: `aa273309a6fe6132`

#### PCAP-complete child attach 1

- log parent request: `03:13:00.332`
- log parent response: `03:13:00.378`
- log child id request: `03:13:01.046`
- log child id response: `03:13:01.142`
- parent ipv6: `fe80:0:0:0:2860:4097:14e:bfc9`
- parent extaddr: `2a604097014ebfc9`
- parent rloc16: `0xdc00`
- child extaddr: `aa273309a6fe6132`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **52 ms**
- Response -> Child ID Request: **698 ms**
- Child ID Request -> Response: **75 ms**
- Full Attach: **825 ms**
- pcap parent request: `03:13:00.320` (frame 123)
- pcap parent response: `03:13:00.372` (frame 124)
- pcap child id request: `03:13:01.070` (frame 130)
- pcap child id response: `03:13:01.145` (frame 132)

#### PCAP-complete child attach 2

- log parent request: `03:17:01.318`
- log parent response: `03:17:01.604`
- log child id request: `03:17:02.030`
- log child id response: `03:17:02.120`
- parent ipv6: `fe80:0:0:0:6427:5aa:4e96:6fc9`
- parent extaddr: `662705aa4e966fc9`
- parent rloc16: `0x4c00`
- child extaddr: `aa273309a6fe6132`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **290 ms**
- Response -> Child ID Request: **462 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **816 ms**
- pcap parent request: `03:17:01.310` (frame 342)
- pcap parent response: `03:17:01.600` (frame 343)
- pcap child id request: `03:17:02.062` (frame 347)
- pcap child id response: `03:17:02.126` (frame 349)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 125: 16, seq 126: 16, seq 127: 16, seq 128: 16
- failed tx by dst: `2a604097014ebfc9`: 55

### `stock_child_20260625-031912-run36.log`

- child extaddr: `fe96de738462a237`

#### PCAP-complete child attach 1

- log parent request: `03:24:58.064`
- log parent response: `03:24:58.151`
- log child id request: `03:24:58.783`
- log child id response: `03:24:58.869`
- parent ipv6: `fe80:0:0:0:984b:4ffe:969f:dc45`
- parent extaddr: `9a4b4ffe969fdc45`
- parent rloc16: `0xd800`
- child extaddr: `fe96de738462a237`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **87 ms**
- Response -> Child ID Request: **664 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **814 ms**
- pcap parent request: `03:24:58.056` (frame 125)
- pcap parent response: `03:24:58.143` (frame 126)
- pcap child id request: `03:24:58.807` (frame 132)
- pcap child id response: `03:24:58.870` (frame 134)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260625-032507-run37.log`

- child extaddr: `6699b122bd000244`

#### PCAP-complete child attach 1

- log parent request: `03:30:52.910`
- log parent response: `03:30:53.218`
- log child id request: `03:30:53.681`
- log child id response: `03:30:53.767`
- parent ipv6: `fe80:0:0:0:e88a:38c4:e92d:d165`
- parent extaddr: `ea8a38c4e92dd165`
- parent rloc16: `0x8800`
- child extaddr: `6699b122bd000244`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **221 ms**
- Response -> Child ID Request: **496 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **779 ms**
- pcap parent request: `03:30:52.989` (frame 130)
- pcap parent response: `03:30:53.210` (frame 131)
- pcap child id request: `03:30:53.706` (frame 137)
- pcap child id response: `03:30:53.768` (frame 139)

#### PCAP-complete child attach 2

- log parent request: `03:34:53.391`
- log parent response: `03:34:53.499`
- log child id request: `03:34:54.108`
- log child id response: `03:34:54.197`
- parent ipv6: `fe80:0:0:0:f0db:9fce:f8c5:a301`
- parent extaddr: `f2db9fcef8c5a301`
- parent rloc16: `0xa800`
- child extaddr: `6699b122bd000244`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **107 ms**
- Response -> Child ID Request: **644 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **814 ms**
- pcap parent request: `03:34:53.392` (frame 348)
- pcap parent response: `03:34:53.499` (frame 349)
- pcap child id request: `03:34:54.143` (frame 353)
- pcap child id response: `03:34:54.206` (frame 355)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 151: 16, seq 152: 16, seq 153: 16, seq 154: 16
- failed tx by dst: `ea8a38c4e92dd165`: 61

### `stock_child_20260625-033705-run38.log`

- child extaddr: `6638a1de6e2f3b70`

#### PCAP-complete child attach 1

- log parent request: `03:42:50.924`
- log parent response: `03:42:51.205`
- log child id request: `03:42:51.643`
- log child id response: `03:42:51.740`
- parent ipv6: `fe80:0:0:0:f01b:67b6:fa0d:5c43`
- parent extaddr: `f21b67b6fa0d5c43`
- parent rloc16: `0x4400`
- child extaddr: `6638a1de6e2f3b70`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **282 ms**
- Response -> Child ID Request: **468 ms**
- Child ID Request -> Response: **75 ms**
- Full Attach: **825 ms**
- pcap parent request: `03:42:50.917` (frame 127)
- pcap parent response: `03:42:51.199` (frame 128)
- pcap child id request: `03:42:51.667` (frame 134)
- pcap child id response: `03:42:51.742` (frame 136)

#### PCAP-complete child attach 2

- log parent request: `03:46:51.901`
- log parent response: `03:46:51.965`
- log child id request: `03:46:52.655`
- log child id response: `03:46:52.702`
- parent ipv6: `fe80:0:0:0:341d:3fda:1eb5:791`
- parent extaddr: `361d3fda1eb50791`
- parent rloc16: `0x9000`
- child extaddr: `6638a1de6e2f3b70`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **65 ms**
- Response -> Child ID Request: **685 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **814 ms**
- pcap parent request: `03:46:51.894` (frame 344)
- pcap parent response: `03:46:51.959` (frame 345)
- pcap child id request: `03:46:52.644` (frame 349)
- pcap child id response: `03:46:52.708` (frame 351)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 24: 16, seq 25: 16, seq 26: 16, seq 27: 16
- failed tx by dst: `f21b67b6fa0d5c43`: 53

### `stock_child_20260625-034902-run39.log`

- child extaddr: `4e5f893b72227682`

#### PCAP-complete child attach 1

- log parent request: `03:54:48.474`
- log parent response: `03:54:48.748`
- log child id request: `03:54:49.244`
- log child id response: `03:54:49.330`
- parent ipv6: `fe80:0:0:0:818:3aac:e5a:bf3a`
- parent extaddr: `0a183aac0e5abf3a`
- parent rloc16: `0x2000`
- child extaddr: `4e5f893b72227682`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **223 ms**
- Response -> Child ID Request: **528 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **814 ms**
- pcap parent request: `03:54:48.518` (frame 127)
- pcap parent response: `03:54:48.741` (frame 128)
- pcap child id request: `03:54:49.269` (frame 134)
- pcap child id response: `03:54:49.332` (frame 136)

#### PCAP-complete child attach 2

- log parent request: `03:58:49.565`
- log parent response: `03:58:49.667`
- log child id request: `03:58:50.284`
- log child id response: `03:58:50.370`
- parent ipv6: `fe80:0:0:0:d879:92aa:122d:c200`
- parent extaddr: `da7992aa122dc200`
- parent rloc16: `0x2400`
- child extaddr: `4e5f893b72227682`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **100 ms**
- Response -> Child ID Request: **649 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **813 ms**
- pcap parent request: `03:58:49.568` (frame 346)
- pcap parent response: `03:58:49.668` (frame 347)
- pcap child id request: `03:58:50.317` (frame 351)
- pcap child id response: `03:58:50.381` (frame 353)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 194: 16, seq 195: 16, seq 196: 16, seq 197: 16
- failed tx by dst: `0a183aac0e5abf3a`: 62

### `stock_child_20260625-040100-run40.log`

- child extaddr: `8acea0d8bd7193e5`

#### PCAP-complete child attach 1

- log parent request: `04:06:45.705`
- log parent response: `04:06:45.881`
- log child id request: `04:06:46.423`
- log child id response: `04:06:46.513`
- parent ipv6: `fe80:0:0:0:cc03:a789:7b92:ec55`
- parent extaddr: `ce03a7897b92ec55`
- parent rloc16: `0x4400`
- child extaddr: `8acea0d8bd7193e5`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **172 ms**
- Response -> Child ID Request: **578 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **814 ms**
- pcap parent request: `04:06:45.700` (frame 128)
- pcap parent response: `04:06:45.872` (frame 129)
- pcap child id request: `04:06:46.450` (frame 135)
- pcap child id response: `04:06:46.514` (frame 137)

#### PCAP-complete child attach 2

- log parent request: `04:10:46.106`
- log parent response: `04:10:46.502`
- log child id request: `04:10:46.826`
- log child id response: `04:10:46.921`
- parent ipv6: `fe80:0:0:0:d4bd:7157:9239:f79d`
- parent extaddr: `d6bd71579239f79d`
- parent rloc16: `0xd000`
- child extaddr: `8acea0d8bd7193e5`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **397 ms**
- Response -> Child ID Request: **354 ms**
- Child ID Request -> Response: **74 ms**
- Full Attach: **825 ms**
- pcap parent request: `04:10:46.107` (frame 347)
- pcap parent response: `04:10:46.504` (frame 348)
- pcap child id request: `04:10:46.858` (frame 352)
- pcap child id response: `04:10:46.932` (frame 354)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 232: 16, seq 233: 16, seq 234: 16, seq 235: 16
- failed tx by dst: `ce03a7897b92ec55`: 64

### `stock_child_20260625-041257-run41.log`

- child extaddr: `1a4604f0113c3641`

#### PCAP-complete child attach 1

- log parent request: `04:18:43.335`
- log parent response: `04:18:43.787`
- log child id request: `04:18:44.052`
- log child id response: `04:18:44.150`
- parent ipv6: `fe80:0:0:0:d447:3517:39a0:7f30`
- parent extaddr: `d647351739a07f30`
- parent rloc16: `0x4400`
- child extaddr: `1a4604f0113c3641`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **453 ms**
- Response -> Child ID Request: **298 ms**
- Child ID Request -> Response: **74 ms**
- Full Attach: **825 ms**
- pcap parent request: `04:18:43.327` (frame 125)
- pcap parent response: `04:18:43.780` (frame 126)
- pcap child id request: `04:18:44.078` (frame 132)
- pcap child id response: `04:18:44.152` (frame 134)

#### PCAP-complete child attach 2

- log parent request: `04:22:44.490`
- log parent response: `04:22:44.663`
- log child id request: `04:22:45.199`
- log child id response: `04:22:45.288`
- parent ipv6: `fe80:0:0:0:430:4d92:8deb:a1f6`
- parent extaddr: `06304d928deba1f6`
- parent rloc16: `0xc800`
- child extaddr: `1a4604f0113c3641`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **175 ms**
- Response -> Child ID Request: **573 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **811 ms**
- pcap parent request: `04:22:44.482` (frame 343)
- pcap parent response: `04:22:44.657` (frame 344)
- pcap child id request: `04:22:45.230` (frame 348)
- pcap child id response: `04:22:45.293` (frame 350)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 2: 16, seq 3: 16, seq 4: 16, seq 5: 16
- failed tx by dst: `d647351739a07f30`: 52

### `stock_child_20260625-042455-run42.log`

- child extaddr: `b2dda9c183e5da70`

#### PCAP-complete child attach 1

- log parent request: `04:30:41.358`
- log parent response: `04:30:41.455`
- log child id request: `04:30:42.128`
- log child id response: `04:30:42.215`
- parent ipv6: `fe80:0:0:0:9cc1:1150:8059:5de5`
- parent extaddr: `9ec1115080595de5`
- parent rloc16: `0x9000`
- child extaddr: `b2dda9c183e5da70`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **46 ms**
- Response -> Child ID Request: **706 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **815 ms**
- pcap parent request: `04:30:41.400` (frame 128)
- pcap parent response: `04:30:41.446` (frame 129)
- pcap child id request: `04:30:42.152` (frame 135)
- pcap child id response: `04:30:42.215` (frame 137)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260625-043050-run43.log`

- child extaddr: `e62ea5033757ef08`

#### PCAP-complete child attach 1

- log parent request: `04:36:36.029`
- log parent response: `04:36:36.356`
- log child id request: `04:36:36.804`
- log child id response: `04:36:36.900`
- parent ipv6: `fe80:0:0:0:4052:6114:4313:2504`
- parent extaddr: `4252611443132504`
- parent rloc16: `0xa800`
- child extaddr: `e62ea5033757ef08`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **245 ms**
- Response -> Child ID Request: **477 ms**
- Child ID Request -> Response: **75 ms**
- Full Attach: **797 ms**
- pcap parent request: `04:36:36.105` (frame 131)
- pcap parent response: `04:36:36.350` (frame 133)
- pcap child id request: `04:36:36.827` (frame 139)
- pcap child id response: `04:36:36.902` (frame 141)

#### PCAP-complete child attach 2

- log parent request: `04:40:36.669`
- log parent response: `04:40:36.844`
- log child id request: `04:40:37.423`
- log child id response: `04:40:37.469`
- parent ipv6: `fe80:0:0:0:4427:b121:f21a:f9e1`
- parent extaddr: `4627b121f21af9e1`
- parent rloc16: `0x7400`
- child extaddr: `e62ea5033757ef08`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **177 ms**
- Response -> Child ID Request: **573 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **813 ms**
- pcap parent request: `04:40:36.660` (frame 350)
- pcap parent response: `04:40:36.837` (frame 351)
- pcap child id request: `04:40:37.410` (frame 355)
- pcap child id response: `04:40:37.473` (frame 357)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 184: 16, seq 185: 16, seq 186: 16, seq 187: 16
- failed tx by dst: `4252611443132504`: 52

### `stock_child_20260625-044248-run44.log`

- child extaddr: `f2c650b1e0ac7e73`

#### PCAP-complete child attach 1

- log parent request: `04:48:33.804`
- log parent response: `04:48:34.174`
- log child id request: `04:48:34.524`
- log child id response: `04:48:34.623`
- parent ipv6: `fe80:0:0:0:f8b8:56f9:fab5:bd19`
- parent extaddr: `fab856f9fab5bd19`
- parent rloc16: `0xcc00`
- child extaddr: `f2c650b1e0ac7e73`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **369 ms**
- Response -> Child ID Request: **381 ms**
- Child ID Request -> Response: **76 ms**
- Full Attach: **826 ms**
- pcap parent request: `04:48:33.797` (frame 127)
- pcap parent response: `04:48:34.166` (frame 129)
- pcap child id request: `04:48:34.547` (frame 135)
- pcap child id response: `04:48:34.623` (frame 137)

#### PCAP-complete child attach 2

- log parent request: `04:52:34.417`
- log parent response: `04:52:34.475`
- log child id request: `04:52:35.172`
- log child id response: `04:52:35.219`
- parent ipv6: `fe80:0:0:0:8c66:8075:560c:616f`
- parent extaddr: `8e668075560c616f`
- parent rloc16: `0xe800`
- child extaddr: `f2c650b1e0ac7e73`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **60 ms**
- Response -> Child ID Request: **691 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **815 ms**
- pcap parent request: `04:52:34.407` (frame 345)
- pcap parent response: `04:52:34.467` (frame 346)
- pcap child id request: `04:52:35.158` (frame 350)
- pcap child id response: `04:52:35.222` (frame 352)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 154: 16, seq 155: 16, seq 156: 16, seq 157: 16
- failed tx by dst: `fab856f9fab5bd19`: 56

### `stock_child_20260625-045445-run45.log`

- child extaddr: `f23b9edfffd45913`

#### PCAP-complete child attach 1

- log parent request: `05:00:31.196`
- log parent response: `05:00:31.441`
- log child id request: `05:00:31.966`
- log child id response: `05:00:32.052`
- parent ipv6: `fe80:0:0:0:822:cf9:9dfd:8ce`
- parent extaddr: `0a220cf99dfd08ce`
- parent rloc16: `0x7800`
- child extaddr: `f23b9edfffd45913`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **193 ms**
- Response -> Child ID Request: **558 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **814 ms**
- pcap parent request: `05:00:31.236` (frame 121)
- pcap parent response: `05:00:31.429` (frame 122)
- pcap child id request: `05:00:31.987` (frame 128)
- pcap child id response: `05:00:32.050` (frame 130)

#### PCAP-complete child attach 2

- log parent request: `05:04:32.235`
- log parent response: `05:04:32.372`
- log child id request: `05:04:32.954`
- log child id response: `05:04:33.045`
- parent ipv6: `fe80:0:0:0:345e:13c8:8bb7:75d0`
- parent extaddr: `365e13c88bb775d0`
- parent rloc16: `0x1400`
- child extaddr: `f23b9edfffd45913`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **136 ms**
- Response -> Child ID Request: **615 ms**
- Child ID Request -> Response: **67 ms**
- Full Attach: **818 ms**
- pcap parent request: `05:04:32.233` (frame 338)
- pcap parent response: `05:04:32.369` (frame 339)
- pcap child id request: `05:04:32.984` (frame 343)
- pcap child id response: `05:04:33.051` (frame 345)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 35: 16, seq 36: 16, seq 37: 16, seq 38: 16
- failed tx by dst: `0a220cf99dfd08ce`: 64

### `stock_child_20260625-050643-run46.log`

- child extaddr: `b65e2bc947a5b790`

#### PCAP-complete child attach 1

- log parent request: `05:12:29.150`
- log parent response: `05:12:29.425`
- log child id request: `05:12:29.869`
- log child id response: `05:12:29.954`
- parent ipv6: `fe80:0:0:0:f8e5:cd44:2ec3:5ba2`
- parent extaddr: `fae5cd442ec35ba2`
- parent rloc16: `0x5800`
- child extaddr: `b65e2bc947a5b790`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **275 ms**
- Response -> Child ID Request: **475 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **812 ms**
- pcap parent request: `05:12:29.141` (frame 132)
- pcap parent response: `05:12:29.416` (frame 133)
- pcap child id request: `05:12:29.891` (frame 139)
- pcap child id response: `05:12:29.953` (frame 141)

#### PCAP-complete child attach 2

- log parent request: `05:16:30.044`
- log parent response: `05:16:30.128`
- log child id request: `05:16:30.761`
- log child id response: `05:16:30.849`
- parent ipv6: `fe80:0:0:0:30f4:adcb:282b:8f61`
- parent extaddr: `32f4adcb282b8f61`
- parent rloc16: `0xf400`
- child extaddr: `b65e2bc947a5b790`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **83 ms**
- Response -> Child ID Request: **668 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **814 ms**
- pcap parent request: `05:16:30.044` (frame 349)
- pcap parent response: `05:16:30.127` (frame 350)
- pcap child id request: `05:16:30.795` (frame 354)
- pcap child id response: `05:16:30.858` (frame 356)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 187: 16, seq 188: 16, seq 189: 16, seq 190: 16
- failed tx by dst: `fae5cd442ec35ba2`: 62

### `stock_child_20260625-051840-run47.log`

- child extaddr: `72a8827c2ca4dbaf`

#### PCAP-complete child attach 1

- log parent request: `05:24:26.365`
- log parent response: `05:24:26.452`
- log child id request: `05:24:27.083`
- log child id response: `05:24:27.169`
- parent ipv6: `fe80:0:0:0:2824:7ffb:49f6:9ff4`
- parent extaddr: `2a247ffb49f69ff4`
- parent rloc16: `0xb000`
- child extaddr: `72a8827c2ca4dbaf`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **87 ms**
- Response -> Child ID Request: **663 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **813 ms**
- pcap parent request: `05:24:26.356` (frame 133)
- pcap parent response: `05:24:26.443` (frame 134)
- pcap child id request: `05:24:27.106` (frame 141)
- pcap child id response: `05:24:27.169` (frame 143)

#### PCAP-complete child attach 2

- log parent request: `05:28:26.851`
- log parent response: `05:28:26.901`
- log child id request: `05:28:27.569`
- log child id response: `05:28:27.667`
- parent ipv6: `fe80:0:0:0:8076:ccd8:a4f1:bee5`
- parent extaddr: `8276ccd8a4f1bee5`
- parent rloc16: `0xf000`
- child extaddr: `72a8827c2ca4dbaf`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **51 ms**
- Response -> Child ID Request: **699 ms**
- Child ID Request -> Response: **75 ms**
- Full Attach: **825 ms**
- pcap parent request: `05:28:26.851` (frame 353)
- pcap parent response: `05:28:26.902` (frame 354)
- pcap child id request: `05:28:27.601` (frame 358)
- pcap child id response: `05:28:27.676` (frame 360)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 127: 16, seq 128: 16, seq 129: 16, seq 130: 16
- failed tx by dst: `2a247ffb49f69ff4`: 63

### `stock_child_20260625-053038-run48.log`

- child extaddr: `a2ab70b9e803a529`

#### PCAP-complete child attach 1

- log parent request: `05:36:23.959`
- log parent response: `05:36:24.318`
- log child id request: `05:36:24.729`
- log child id response: `05:36:24.844`
- parent ipv6: `fe80:0:0:0:9073:1f72:179a:8aa7`
- parent extaddr: `92731f72179a8aa7`
- parent rloc16: `0x2800`
- child extaddr: `a2ab70b9e803a529`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **309 ms**
- Response -> Child ID Request: **443 ms**
- Child ID Request -> Response: **92 ms**
- Full Attach: **844 ms**
- pcap parent request: `05:36:24.002` (frame 136)
- pcap parent response: `05:36:24.311` (frame 138)
- pcap child id request: `05:36:24.754` (frame 144)
- pcap child id response: `05:36:24.846` (frame 147)

#### PCAP-complete child attach 2

- log parent request: `05:40:25.038`
- log parent response: `05:40:25.471`
- log child id request: `05:40:25.755`
- log child id response: `05:40:25.854`
- parent ipv6: `fe80:0:0:0:30bb:a870:c195:8a77`
- parent extaddr: `32bba870c1958a77`
- parent rloc16: `0x5400`
- child extaddr: `a2ab70b9e803a529`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **435 ms**
- Response -> Child ID Request: **317 ms**
- Child ID Request -> Response: **75 ms**
- Full Attach: **827 ms**
- pcap parent request: `05:40:25.039` (frame 358)
- pcap parent response: `05:40:25.474` (frame 359)
- pcap child id request: `05:40:25.791` (frame 363)
- pcap child id response: `05:40:25.866` (frame 365)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 109: 16, seq 110: 16, seq 111: 16, seq 112: 16
- failed tx by dst: `92731f72179a8aa7`: 62

### `stock_child_20260625-054236-run49.log`

- child extaddr: `aa9d049587220856`

#### PCAP-complete child attach 1

- log parent request: `05:48:22.019`
- log parent response: `05:48:22.112`
- log child id request: `05:48:22.736`
- log child id response: `05:48:22.821`
- parent ipv6: `fe80:0:0:0:4810:a975:3aca:8d32`
- parent extaddr: `4a10a9753aca8d32`
- parent rloc16: `0xb800`
- child extaddr: `aa9d049587220856`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **93 ms**
- Response -> Child ID Request: **656 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **811 ms**
- pcap parent request: `05:48:22.011` (frame 131)
- pcap parent response: `05:48:22.104` (frame 132)
- pcap child id request: `05:48:22.760` (frame 138)
- pcap child id response: `05:48:22.822` (frame 140)

#### PCAP-complete child attach 2

- log parent request: `05:52:22.485`
- log parent response: `05:52:22.605`
- log child id request: `05:52:23.202`
- log child id response: `05:52:23.290`
- parent ipv6: `fe80:0:0:0:6cbf:6dba:5069:32e`
- parent extaddr: `6ebf6dba5069032e`
- parent rloc16: `0x0400`
- child extaddr: `aa9d049587220856`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **119 ms**
- Response -> Child ID Request: **631 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **814 ms**
- pcap parent request: `05:52:22.486` (frame 352)
- pcap parent response: `05:52:22.605` (frame 354)
- pcap child id request: `05:52:23.236` (frame 358)
- pcap child id response: `05:52:23.300` (frame 360)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 152: 16, seq 153: 16, seq 154: 16, seq 155: 16
- failed tx by dst: `4a10a9753aca8d32`: 62

### `stock_child_20260625-055433-run50.log`

- child extaddr: `560e4839f4cc018a`

#### PCAP-complete child attach 1

- log parent request: `06:00:19.020`
- log parent response: `06:00:19.429`
- log child id request: `06:00:19.738`
- log child id response: `06:00:19.837`
- parent ipv6: `fe80:0:0:0:842d:7057:af21:441`
- parent extaddr: `862d7057af210441`
- parent rloc16: `0xa800`
- child extaddr: `560e4839f4cc018a`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **411 ms**
- Response -> Child ID Request: **340 ms**
- Child ID Request -> Response: **77 ms**
- Full Attach: **828 ms**
- pcap parent request: `06:00:19.012` (frame 125)
- pcap parent response: `06:00:19.423` (frame 127)
- pcap child id request: `06:00:19.763` (frame 133)
- pcap child id response: `06:00:19.840` (frame 135)

#### PCAP-complete child attach 2

- log parent request: `06:04:20.116`
- log parent response: `06:04:20.297`
- log child id request: `06:04:20.827`
- log child id response: `06:04:20.918`
- parent ipv6: `fe80:0:0:0:8018:283c:6a44:5425`
- parent extaddr: `8218283c6a445425`
- parent rloc16: `0x5c00`
- child extaddr: `560e4839f4cc018a`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **183 ms**
- Response -> Child ID Request: **567 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **814 ms**
- pcap parent request: `06:04:20.109` (frame 342)
- pcap parent response: `06:04:20.292` (frame 343)
- pcap child id request: `06:04:20.859` (frame 348)
- pcap child id response: `06:04:20.923` (frame 350)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 33: 16, seq 34: 16, seq 35: 16, seq 36: 16
- failed tx by dst: `862d7057af210441`: 55
