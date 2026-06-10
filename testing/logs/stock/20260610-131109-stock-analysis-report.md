# Child Log Analysis

## stock_child

Files analyzed: **56**

### Summary

| Attach | Metric | M (SD), ms | n |
| --- | --- | ---: | ---: |
| 1 | Request → Response | 289.46 (142.45) | 56 |
| 1 | Response → Child ID Request | 457.25 (141.44) | 56 |
| 1 | Child ID Request → Response | 58.32 (15.49) | 56 |
| 1 | Full Attach | 805.04 (18.61) | 56 |
| 2 | Request → Response | 261.95 (152.32) | 55 |
| 2 | Response → Child ID Request | 487.98 (152.45) | 55 |
| 2 | Child ID Request → Response | 59.05 (14.59) | 55 |
| 2 | Full Attach | 808.98 (14.84) | 55 |

| Metric | M (SD) | n |
| --- | ---: | ---: |
| Failed TX Attempts per Log | 62.73 (8.56) | 56 |

### `stock_child_20260601-115057.log`

#### Attach sequence 1

- parent request: `11:52:00.305`
- parent response: `11:52:00.719`
- child id request: `11:52:01.014`
- child id response: `11:52:01.093`
- parent ipv6: `fe80:0:0:0:747d:521b:8f1b:a668`
- parent extaddr: `767d521b8f1ba668`
- parent rloc16: `0x5400`
- timing source: **pcap**
- Request → Response: **419 ms**
- Response → Child ID Request: **332 ms**
- Child ID Request → Response: **14 ms**
- Full Attach: **765 ms**
- pcap parent request: `11:52:00.277` (frame 11)
- pcap parent response: `11:52:00.696` (frame 12)
- pcap child id request: `11:52:01.028` (frame 14)
- pcap child id response: `11:52:01.042` (frame 16)

#### Attach sequence 2

- parent request: `11:56:01.449`
- parent response: `11:56:01.515`
- child id request: `None`
- child id response: `11:56:02.241`
- parent ipv6: `fe80:0:0:0:1084:af33:ed0:3bb3`
- parent extaddr: `1284af330ed03bb3`
- parent rloc16: `0xac00`
- timing source: **pcap**
- Request → Response: **66 ms**
- Response → Child ID Request: **683 ms**
- Child ID Request → Response: **13 ms**
- Full Attach: **762 ms**
- pcap parent request: `11:56:01.435` (frame 179)
- pcap parent response: `11:56:01.501` (frame 180)
- pcap child id request: `11:56:02.184` (frame 182)
- pcap child id response: `11:56:02.197` (frame 184)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 10: 16, seq 11: 16, seq 12: 16, seq 13: 16
- failed tx by dst: `767d521b8f1ba668`: 53

### `stock_child_20260601-121212.log`

#### Attach sequence 1

- parent request: `12:13:15.402`
- parent response: `12:13:15.780`
- child id request: `12:13:16.177`
- child id response: `12:13:16.256`
- parent ipv6: `fe80:0:0:0:d890:3c04:ae6:8c9c`
- parent extaddr: `da903c040ae68c9c`
- parent rloc16: `0xe000`
- timing source: **pcap**
- Request → Response: **319 ms**
- Response → Child ID Request: **433 ms**
- Child ID Request → Response: **15 ms**
- Full Attach: **767 ms**
- pcap parent request: `12:13:15.439` (frame 11)
- pcap parent response: `12:13:15.758` (frame 12)
- pcap child id request: `12:13:16.191` (frame 14)
- pcap child id response: `12:13:16.206` (frame 16)

#### Attach sequence 2

- parent request: `12:17:16.501`
- parent response: `12:17:16.590`
- child id request: `None`
- child id response: `12:17:17.290`
- parent ipv6: `fe80:0:0:0:940c:7957:1efb:5f08`
- parent extaddr: `960c79571efb5f08`
- parent rloc16: `0x3c00`
- timing source: **pcap**
- Request → Response: **92 ms**
- Response → Child ID Request: **657 ms**
- Child ID Request → Response: **13 ms**
- Full Attach: **762 ms**
- pcap parent request: `12:17:16.484` (frame 179)
- pcap parent response: `12:17:16.576` (frame 180)
- pcap child id request: `12:17:17.233` (frame 182)
- pcap child id response: `12:17:17.246` (frame 184)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 152: 16, seq 153: 16, seq 154: 16, seq 155: 16
- failed tx by dst: `da903c040ae68c9c`: 52

### `stock_child_20260601-121953.log`

#### Attach sequence 1

- parent request: `12:20:56.078`
- parent response: `None`
- child id request: `None`
- child id response: `12:20:56.818`
- parent ipv6: `fe80:0:0:0:18b1:863b:65df:33ed`
- parent extaddr: `1ab1863b65df33ed`
- parent rloc16: `0x7c00`
- timing source: **pcap**
- Request → Response: **25 ms**
- Response → Child ID Request: **729 ms**
- Child ID Request → Response: **14 ms**
- Full Attach: **768 ms**
- pcap parent request: `12:20:56.001` (frame 11)
- pcap parent response: `12:20:56.026` (frame 12)
- pcap child id request: `12:20:56.755` (frame 14)
- pcap child id response: `12:20:56.769` (frame 16)

#### Attach sequence 2

- parent request: `12:24:56.698`
- parent response: `12:24:56.993`
- child id request: `None`
- child id response: `12:24:57.488`
- parent ipv6: `fe80:0:0:0:c482:d39f:131:b69`
- parent extaddr: `c682d39f01310b69`
- parent rloc16: `0x4c00`
- timing source: **pcap**
- Request → Response: **297 ms**
- Response → Child ID Request: **452 ms**
- Child ID Request → Response: **14 ms**
- Full Attach: **763 ms**
- pcap parent request: `12:24:56.682` (frame 178)
- pcap parent response: `12:24:56.979` (frame 179)
- pcap child id request: `12:24:57.431` (frame 181)
- pcap child id response: `12:24:57.445` (frame 183)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 153: 16, seq 154: 16, seq 155: 16, seq 156: 16
- failed tx by dst: `1ab1863b65df33ed`: 53

### `stock_child_20260601-122733.log`

#### Attach sequence 1

- parent request: `12:28:35.458`
- parent response: `12:28:35.876`
- child id request: `12:28:36.165`
- child id response: `12:28:36.244`
- parent ipv6: `fe80:0:0:0:e41c:ac85:7cc8:2d78`
- parent extaddr: `e61cac857cc82d78`
- parent rloc16: `0x4800`
- timing source: **pcap**
- Request → Response: **423 ms**
- Response → Child ID Request: **326 ms**
- Child ID Request → Response: **13 ms**
- Full Attach: **762 ms**
- pcap parent request: `12:28:35.431` (frame 11)
- pcap parent response: `12:28:35.854` (frame 12)
- pcap child id request: `12:28:36.180` (frame 14)
- pcap child id response: `12:28:36.193` (frame 16)

#### Attach sequence 2

- parent request: `12:32:35.978`
- parent response: `12:32:36.292`
- child id request: `None`
- child id response: `12:32:36.768`
- parent ipv6: `fe80:0:0:0:3808:e1d3:5997:2937`
- parent extaddr: `3a08e1d359972937`
- parent rloc16: `0xf800`
- timing source: **pcap**
- Request → Response: **317 ms**
- Response → Child ID Request: **433 ms**
- Child ID Request → Response: **14 ms**
- Full Attach: **764 ms**
- pcap parent request: `12:32:35.962` (frame 184)
- pcap parent response: `12:32:36.279` (frame 185)
- pcap child id request: `12:32:36.712` (frame 187)
- pcap child id response: `12:32:36.726` (frame 189)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 121: 16, seq 122: 16, seq 123: 16, seq 124: 16
- failed tx by dst: `e61cac857cc82d78`: 52

### `stock_child_20260601-123513.log`

#### Attach sequence 1

- parent request: `12:36:16.211`
- parent response: `12:36:16.298`
- child id request: `None`
- child id response: `12:36:17.002`
- parent ipv6: `fe80:0:0:0:a405:ee96:2ad7:a308`
- parent extaddr: `a605ee962ad7a308`
- parent rloc16: `0x7800`
- timing source: **pcap**
- Request → Response: **92 ms**
- Response → Child ID Request: **657 ms**
- Child ID Request → Response: **14 ms**
- Full Attach: **763 ms**
- pcap parent request: `12:36:16.185` (frame 11)
- pcap parent response: `12:36:16.277` (frame 12)
- pcap child id request: `12:36:16.934` (frame 14)
- pcap child id response: `12:36:16.948` (frame 16)

#### Attach sequence 2

- parent request: `12:40:16.837`
- parent response: `12:40:17.252`
- child id request: `None`
- child id response: `12:40:17.627`
- parent ipv6: `fe80:0:0:0:b08a:c9bd:69f8:6000`
- parent extaddr: `b28ac9bd69f86000`
- parent rloc16: `0xc800`
- timing source: **pcap**
- Request → Response: **418 ms**
- Response → Child ID Request: **331 ms**
- Child ID Request → Response: **13 ms**
- Full Attach: **762 ms**
- pcap parent request: `12:40:16.820` (frame 189)
- pcap parent response: `12:40:17.238` (frame 190)
- pcap child id request: `12:40:17.569` (frame 192)
- pcap child id response: `12:40:17.582` (frame 194)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 220: 16, seq 221: 16, seq 222: 16, seq 223: 16
- failed tx by dst: `a605ee962ad7a308`: 48

### `stock_child_20260601-224253.log`

#### Attach sequence 1

- parent request: `22:43:54.868`
- parent response: `22:43:55.028`
- child id request: `22:43:55.577`
- child id response: `22:43:55.656`
- parent ipv6: `fe80:0:0:0:873:fdd6:33c7:705a`
- parent extaddr: `0a73fdd633c7705a`
- parent rloc16: `0x8000`
- timing source: **pcap**
- Request → Response: **163 ms**
- Response → Child ID Request: **586 ms**
- Child ID Request → Response: **15 ms**
- Full Attach: **764 ms**
- pcap parent request: `22:43:54.838` (frame 10)
- pcap parent response: `22:43:55.001` (frame 11)
- pcap child id request: `22:43:55.587` (frame 13)
- pcap child id response: `22:43:55.602` (frame 15)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `stock_child_20260609-030545-run01.log`

#### Attach sequence 1

- parent request: `03:06:26.340`
- parent response: `03:06:26.414`
- child id request: `03:06:27.049`
- child id response: `03:06:27.137`
- parent ipv6: `fe80:0:0:0:8cb9:67a1:3ba7:20f1`
- parent extaddr: `8eb967a13ba720f1`
- parent rloc16: `0x2c00`
- timing source: **pcap**
- Request → Response: **77 ms**
- Response → Child ID Request: **671 ms**
- Child ID Request → Response: **62 ms**
- Full Attach: **810 ms**
- pcap parent request: `03:06:26.314` (frame 9)
- pcap parent response: `03:06:26.391` (frame 10)
- pcap child id request: `03:06:27.062` (frame 13)
- pcap child id response: `03:06:27.124` (frame 15)

#### Attach sequence 2

- parent request: `03:10:27.394`
- parent response: `03:10:27.910`
- child id request: `03:10:28.147`
- child id response: `03:10:28.194`
- parent ipv6: `fe80:0:0:0:834:495d:9654:8b07`
- parent extaddr: `0a34495d96548b07`
- parent rloc16: `0x1800`
- timing source: **pcap**
- Request → Response: **519 ms**
- Response → Child ID Request: **231 ms**
- Child ID Request → Response: **65 ms**
- Full Attach: **815 ms**
- pcap parent request: `03:10:27.375` (frame 184)
- pcap parent response: `03:10:27.894` (frame 185)
- pcap child id request: `03:10:28.125` (frame 187)
- pcap child id response: `03:10:28.190` (frame 189)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 144: 16, seq 145: 16, seq 146: 16, seq 147: 16
- failed tx by dst: `8eb967a13ba720f1`: 50

### `stock_child_20260609-031112-run02.log`

#### Attach sequence 1

- parent request: `03:11:51.928`
- parent response: `03:11:52.199`
- child id request: `03:11:52.747`
- child id response: `03:11:52.792`
- parent ipv6: `fe80:0:0:0:2882:4e65:b0eb:d0f5`
- parent extaddr: `2a824e65b0ebd0f5`
- parent rloc16: `0x3000`
- timing source: **pcap**
- Request → Response: **175 ms**
- Response → Child ID Request: **539 ms**
- Child ID Request → Response: **65 ms**
- Full Attach: **779 ms**
- pcap parent request: `03:11:52.000` (frame 10)
- pcap parent response: `03:11:52.175` (frame 11)
- pcap child id request: `03:11:52.714` (frame 13)
- pcap child id response: `03:11:52.779` (frame 15)

#### Attach sequence 2

- parent request: `03:15:52.639`
- parent response: `03:15:53.090`
- child id request: `03:15:53.394`
- child id response: `03:15:53.440`
- parent ipv6: `fe80:0:0:0:f07e:1861:e2c6:b2af`
- parent extaddr: `f27e1861e2c6b2af`
- parent rloc16: `0x0400`
- timing source: **pcap**
- Request → Response: **454 ms**
- Response → Child ID Request: **296 ms**
- Child ID Request → Response: **64 ms**
- Full Attach: **814 ms**
- pcap parent request: `03:15:52.621` (frame 180)
- pcap parent response: `03:15:53.075` (frame 181)
- pcap child id request: `03:15:53.371` (frame 183)
- pcap child id response: `03:15:53.435` (frame 185)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 102: 16, seq 103: 16, seq 104: 16, seq 105: 16
- failed tx by dst: `2a824e65b0ebd0f5`: 56

### `stock_child_20260609-031638-run03.log`

#### Attach sequence 1

- parent request: `03:17:18.454`
- parent response: `03:17:18.517`
- child id request: `03:17:19.163`
- child id response: `03:17:19.256`
- parent ipv6: `fe80:0:0:0:9c58:db36:93d2:5004`
- parent extaddr: `9e58db3693d25004`
- parent rloc16: `0xbc00`
- timing source: **pcap**
- Request → Response: **67 ms**
- Response → Child ID Request: **682 ms**
- Child ID Request → Response: **67 ms**
- Full Attach: **816 ms**
- pcap parent request: `03:17:18.427` (frame 10)
- pcap parent response: `03:17:18.494` (frame 11)
- pcap child id request: `03:17:19.176` (frame 13)
- pcap child id response: `03:17:19.243` (frame 15)

#### Attach sequence 2

- parent request: `03:21:19.361`
- parent response: `03:21:19.601`
- child id request: `03:21:20.114`
- child id response: `03:21:20.160`
- parent ipv6: `fe80:0:0:0:bc7a:28ea:7f98:e0bf`
- parent extaddr: `be7a28ea7f98e0bf`
- parent rloc16: `0x5400`
- timing source: **pcap**
- Request → Response: **244 ms**
- Response → Child ID Request: **507 ms**
- Child ID Request → Response: **63 ms**
- Full Attach: **814 ms**
- pcap parent request: `03:21:19.342` (frame 183)
- pcap parent response: `03:21:19.586` (frame 185)
- pcap child id request: `03:21:20.093` (frame 187)
- pcap child id response: `03:21:20.156` (frame 189)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 107: 16, seq 108: 16, seq 109: 16, seq 110: 16
- failed tx by dst: `9e58db3693d25004`: 58

### `stock_child_20260609-115631-run01.log`

#### Attach sequence 1

- parent request: `11:57:11.480`
- parent response: `11:57:11.565`
- child id request: `11:57:12.191`
- child id response: `11:57:12.281`
- parent ipv6: `fe80:0:0:0:505b:8c9e:b185:b733`
- parent extaddr: `525b8c9eb185b733`
- parent rloc16: `0x7c00`
- timing source: **pcap**
- Request → Response: **88 ms**
- Response → Child ID Request: **662 ms**
- Child ID Request → Response: **64 ms**
- Full Attach: **814 ms**
- pcap parent request: `11:57:11.454` (frame 10)
- pcap parent response: `11:57:11.542` (frame 11)
- pcap child id request: `11:57:12.204` (frame 13)
- pcap child id response: `11:57:12.268` (frame 15)

#### Attach sequence 2

- parent request: `12:01:12.210`
- parent response: `12:01:12.344`
- child id request: `12:01:12.967`
- child id response: `12:01:13.012`
- parent ipv6: `fe80:0:0:0:f8c6:ad78:b6c8:49df`
- parent extaddr: `fac6ad78b6c849df`
- parent rloc16: `0xe400`
- timing source: **pcap**
- Request → Response: **136 ms**
- Response → Child ID Request: **616 ms**
- Child ID Request → Response: **63 ms**
- Full Attach: **815 ms**
- pcap parent request: `12:01:12.191` (frame 187)
- pcap parent response: `12:01:12.327` (frame 188)
- pcap child id request: `12:01:12.943` (frame 190)
- pcap child id response: `12:01:13.006` (frame 192)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 43: 16, seq 44: 16, seq 45: 16, seq 46: 16
- failed tx by dst: `525b8c9eb185b733`: 54

### `stock_child_20260609-120157-run02.log`

#### Attach sequence 1

- parent request: `12:02:37.327`
- parent response: `12:02:37.712`
- child id request: `12:02:38.033`
- child id response: `12:02:38.121`
- parent ipv6: `fe80:0:0:0:5456:a3af:182b:1c79`
- parent extaddr: `5656a3af182b1c79`
- parent rloc16: `0x6000`
- timing source: **pcap**
- Request → Response: **392 ms**
- Response → Child ID Request: **357 ms**
- Child ID Request → Response: **63 ms**
- Full Attach: **812 ms**
- pcap parent request: `12:02:37.295` (frame 10)
- pcap parent response: `12:02:37.687` (frame 11)
- pcap child id request: `12:02:38.044` (frame 13)
- pcap child id response: `12:02:38.107` (frame 15)

#### Attach sequence 2

- parent request: `12:06:37.801`
- parent response: `12:06:38.162`
- child id request: `12:06:38.554`
- child id response: `12:06:38.601`
- parent ipv6: `fe80:0:0:0:a0dc:3bd2:a94e:c426`
- parent extaddr: `a2dc3bd2a94ec426`
- parent rloc16: `0xc000`
- timing source: **pcap**
- Request → Response: **365 ms**
- Response → Child ID Request: **385 ms**
- Child ID Request → Response: **65 ms**
- Full Attach: **815 ms**
- pcap parent request: `12:06:37.780` (frame 186)
- pcap parent response: `12:06:38.145` (frame 187)
- pcap child id request: `12:06:38.530` (frame 189)
- pcap child id response: `12:06:38.595` (frame 191)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 148: 16, seq 149: 16, seq 150: 16, seq 151: 16
- failed tx by dst: `5656a3af182b1c79`: 50

### `stock_child_20260609-120723-run03.log`

#### Attach sequence 1

- parent request: `12:08:02.917`
- parent response: `12:08:03.311`
- child id request: `12:08:03.628`
- child id response: `12:08:03.716`
- parent ipv6: `fe80:0:0:0:d4ab:f49f:dabc:f36e`
- parent extaddr: `d6abf49fdabcf36e`
- parent rloc16: `0x5800`
- timing source: **pcap**
- Request → Response: **398 ms**
- Response → Child ID Request: **352 ms**
- Child ID Request → Response: **63 ms**
- Full Attach: **813 ms**
- pcap parent request: `12:08:02.888` (frame 9)
- pcap parent response: `12:08:03.286` (frame 11)
- pcap child id request: `12:08:03.638` (frame 13)
- pcap child id response: `12:08:03.701` (frame 15)

#### Attach sequence 2

- parent request: `12:12:03.867`
- parent response: `12:12:04.041`
- child id request: `12:12:04.577`
- child id response: `12:12:04.668`
- parent ipv6: `fe80:0:0:0:64d8:15e4:5951:b241`
- parent extaddr: `66d815e45951b241`
- parent rloc16: `0x1000`
- timing source: **pcap**
- Request → Response: **177 ms**
- Response → Child ID Request: **573 ms**
- Child ID Request → Response: **64 ms**
- Full Attach: **814 ms**
- pcap parent request: `12:12:03.846` (frame 179)
- pcap parent response: `12:12:04.023` (frame 180)
- pcap child id request: `12:12:04.596` (frame 182)
- pcap child id response: `12:12:04.660` (frame 184)

#### Failed TX summary

- failed tx attempts: **61**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 38: 16, seq 39: 16, seq 40: 16, seq 41: 13
- failed tx by dst: `d6abf49fdabcf36e`: 52

### `stock_child_20260609-121249-run04.log`

#### Attach sequence 1

- parent request: `12:13:28.961`
- parent response: `12:13:29.454`
- child id request: `12:13:29.672`
- child id response: `12:13:29.761`
- parent ipv6: `fe80:0:0:0:c0c1:7f38:7b03:17ea`
- parent extaddr: `c2c17f387b0317ea`
- parent rloc16: `0xec00`
- timing source: **pcap**
- Request → Response: **496 ms**
- Response → Child ID Request: **255 ms**
- Child ID Request → Response: **63 ms**
- Full Attach: **814 ms**
- pcap parent request: `12:13:28.931` (frame 9)
- pcap parent response: `12:13:29.427` (frame 11)
- pcap child id request: `12:13:29.682` (frame 13)
- pcap child id response: `12:13:29.745` (frame 15)

#### Attach sequence 2

- parent request: `12:17:29.842`
- parent response: `12:17:30.052`
- child id request: `12:17:30.594`
- child id response: `12:17:30.644`
- parent ipv6: `fe80:0:0:0:9419:cb9d:5d34:bef1`
- parent extaddr: `9619cb9d5d34bef1`
- parent rloc16: `0xd800`
- timing source: **pcap**
- Request → Response: **212 ms**
- Response → Child ID Request: **538 ms**
- Child ID Request → Response: **65 ms**
- Full Attach: **815 ms**
- pcap parent request: `12:17:29.820` (frame 179)
- pcap parent response: `12:17:30.032` (frame 180)
- pcap child id request: `12:17:30.570` (frame 183)
- pcap child id response: `12:17:30.635` (frame 185)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 73: 16, seq 74: 16, seq 75: 16, seq 76: 16
- failed tx by dst: `c2c17f387b0317ea`: 49

### `stock_child_20260609-121815-run05.log`

#### Attach sequence 1

- parent request: `12:18:54.893`
- parent response: `12:18:54.997`
- child id request: `12:18:55.664`
- child id response: `12:18:55.752`
- parent ipv6: `fe80:0:0:0:8814:f888:a93e:90f7`
- parent extaddr: `8a14f888a93e90f7`
- parent rloc16: `0x8400`
- timing source: **pcap**
- Request → Response: **46 ms**
- Response → Child ID Request: **704 ms**
- Child ID Request → Response: **62 ms**
- Full Attach: **812 ms**
- pcap parent request: `12:18:54.924` (frame 10)
- pcap parent response: `12:18:54.970` (frame 11)
- pcap child id request: `12:18:55.674` (frame 13)
- pcap child id response: `12:18:55.736` (frame 15)

#### Attach sequence 2

- parent request: `12:22:55.464`
- parent response: `12:22:55.947`
- child id request: `12:22:56.173`
- child id response: `12:22:56.263`
- parent ipv6: `fe80:0:0:0:c098:1c64:5e5b:50e4`
- parent extaddr: `c2981c645e5b50e4`
- parent rloc16: `0xcc00`
- timing source: **pcap**
- Request → Response: **485 ms**
- Response → Child ID Request: **263 ms**
- Child ID Request → Response: **63 ms**
- Full Attach: **811 ms**
- pcap parent request: `12:22:55.443` (frame 189)
- pcap parent response: `12:22:55.928` (frame 190)
- pcap child id request: `12:22:56.191` (frame 192)
- pcap child id response: `12:22:56.254` (frame 194)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 76: 16, seq 77: 16, seq 78: 16, seq 79: 16
- failed tx by dst: `8a14f888a93e90f7`: 52

### `stock_child_20260609-125338-run01.log`

#### Attach sequence 1

- parent request: `12:54:18.794`
- parent response: `12:54:18.942`
- child id request: `12:54:19.563`
- child id response: `12:54:19.655`
- parent ipv6: `fe80:0:0:0:3cab:e1e0:d502:f486`
- parent extaddr: `3eabe1e0d502f486`
- parent rloc16: `0x2c00`
- timing source: **pcap**
- Request → Response: **91 ms**
- Response → Child ID Request: **661 ms**
- Child ID Request → Response: **63 ms**
- Full Attach: **815 ms**
- pcap parent request: `12:54:18.828` (frame 10)
- pcap parent response: `12:54:18.919` (frame 11)
- pcap child id request: `12:54:19.580` (frame 13)
- pcap child id response: `12:54:19.643` (frame 15)

#### Attach sequence 2

- parent request: `12:58:19.796`
- parent response: `12:58:19.893`
- child id request: `12:58:20.507`
- child id response: `12:58:20.596`
- parent ipv6: `fe80:0:0:0:461:315c:6f4f:9359`
- parent extaddr: `0661315c6f4f9359`
- parent rloc16: `0xa000`
- timing source: **pcap**
- Request → Response: **99 ms**
- Response → Child ID Request: **651 ms**
- Child ID Request → Response: **63 ms**
- Full Attach: **813 ms**
- pcap parent request: `12:58:19.780` (frame 189)
- pcap parent response: `12:58:19.879` (frame 190)
- pcap child id request: `12:58:20.530` (frame 192)
- pcap child id response: `12:58:20.593` (frame 194)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 128: 16, seq 129: 16, seq 130: 16, seq 131: 16
- failed tx by dst: `3eabe1e0d502f486`: 55

### `stock_child_20260609-125904-run02.log`

#### Attach sequence 1

- parent request: `12:59:44.450`
- parent response: `12:59:44.828`
- child id request: `12:59:45.270`
- child id response: `12:59:45.315`
- parent ipv6: `fe80:0:0:0:1cf5:e640:4a2d:c4c8`
- parent extaddr: `1ef5e6404a2dc4c8`
- parent rloc16: `0x5400`
- timing source: **pcap**
- Request → Response: **283 ms**
- Response → Child ID Request: **432 ms**
- Child ID Request → Response: **66 ms**
- Full Attach: **781 ms**
- pcap parent request: `12:59:44.522` (frame 10)
- pcap parent response: `12:59:44.805` (frame 11)
- pcap child id request: `12:59:45.237` (frame 13)
- pcap child id response: `12:59:45.303` (frame 15)

#### Attach sequence 2

- parent request: `13:03:45.439`
- parent response: `13:03:45.755`
- child id request: `13:03:46.191`
- child id response: `13:03:46.238`
- parent ipv6: `fe80:0:0:0:9054:859d:a06b:d501`
- parent extaddr: `9254859da06bd501`
- parent rloc16: `0x2c00`
- timing source: **pcap**
- Request → Response: **318 ms**
- Response → Child ID Request: **432 ms**
- Child ID Request → Response: **63 ms**
- Full Attach: **813 ms**
- pcap parent request: `13:03:45.422` (frame 184)
- pcap parent response: `13:03:45.740` (frame 185)
- pcap child id request: `13:03:46.172` (frame 187)
- pcap child id response: `13:03:46.235` (frame 189)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 145: 16, seq 146: 16, seq 147: 16, seq 148: 16
- failed tx by dst: `1ef5e6404a2dc4c8`: 50

### `stock_child_20260609-130430-run03.log`

#### Attach sequence 1

- parent request: `13:05:10.506`
- parent response: `13:05:10.765`
- child id request: `13:05:11.217`
- child id response: `13:05:11.308`
- parent ipv6: `fe80:0:0:0:40a4:3dda:454b:87a8`
- parent extaddr: `42a43dda454b87a8`
- parent rloc16: `0xb000`
- timing source: **pcap**
- Request → Response: **262 ms**
- Response → Child ID Request: **489 ms**
- Child ID Request → Response: **65 ms**
- Full Attach: **816 ms**
- pcap parent request: `13:05:10.480` (frame 9)
- pcap parent response: `13:05:10.742` (frame 10)
- pcap child id request: `13:05:11.231` (frame 13)
- pcap child id response: `13:05:11.296` (frame 15)

#### Attach sequence 2

- parent request: `13:09:11.478`
- parent response: `13:09:11.519`
- child id request: `13:09:12.232`
- child id response: `13:09:12.278`
- parent ipv6: `fe80:0:0:0:b4d5:e443:74a9:e55b`
- parent extaddr: `b6d5e44374a9e55b`
- parent rloc16: `0x8c00`
- timing source: **pcap**
- Request → Response: **44 ms**
- Response → Child ID Request: **706 ms**
- Child ID Request → Response: **64 ms**
- Full Attach: **814 ms**
- pcap parent request: `13:09:11.461` (frame 179)
- pcap parent response: `13:09:11.505` (frame 180)
- pcap child id request: `13:09:12.211` (frame 182)
- pcap child id response: `13:09:12.275` (frame 184)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 158: 16, seq 159: 16, seq 160: 16, seq 161: 16
- failed tx by dst: `42a43dda454b87a8`: 49

### `stock_child_20260609-130956-run04.log`

#### Attach sequence 1

- parent request: `13:10:36.255`
- parent response: `13:10:36.531`
- child id request: `13:10:36.960`
- child id response: `13:10:37.048`
- parent ipv6: `fe80:0:0:0:f46f:2b2c:2792:803d`
- parent extaddr: `f66f2b2c2792803d`
- parent rloc16: `0x0800`
- timing source: **pcap**
- Request → Response: **285 ms**
- Response → Child ID Request: **465 ms**
- Child ID Request → Response: **63 ms**
- Full Attach: **813 ms**
- pcap parent request: `13:10:36.223` (frame 9)
- pcap parent response: `13:10:36.508` (frame 11)
- pcap child id request: `13:10:36.973` (frame 13)
- pcap child id response: `13:10:37.036` (frame 15)

#### Attach sequence 2

- parent request: `13:14:36.708`
- parent response: `13:14:36.962`
- child id request: `13:14:37.461`
- child id response: `13:14:37.509`
- parent ipv6: `fe80:0:0:0:7422:de89:fde1:c284`
- parent extaddr: `7622de89fde1c284`
- parent rloc16: `0xc400`
- timing source: **pcap**
- Request → Response: **256 ms**
- Response → Child ID Request: **494 ms**
- Child ID Request → Response: **64 ms**
- Full Attach: **814 ms**
- pcap parent request: `13:14:36.691` (frame 190)
- pcap parent response: `13:14:36.947` (frame 191)
- pcap child id request: `13:14:37.441` (frame 193)
- pcap child id response: `13:14:37.505` (frame 195)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 157: 16, seq 158: 16, seq 159: 16, seq 160: 16
- failed tx by dst: `f66f2b2c2792803d`: 51

### `stock_child_20260609-131522-run05.log`

#### Attach sequence 1

- parent request: `13:16:02.516`
- parent response: `13:16:02.966`
- child id request: `13:16:03.227`
- child id response: `13:16:03.315`
- parent ipv6: `fe80:0:0:0:bcdb:8fc6:c5b0:f089`
- parent extaddr: `bedb8fc6c5b0f089`
- parent rloc16: `0xb400`
- timing source: **pcap**
- Request → Response: **455 ms**
- Response → Child ID Request: **296 ms**
- Child ID Request → Response: **63 ms**
- Full Attach: **814 ms**
- pcap parent request: `13:16:02.489` (frame 10)
- pcap parent response: `13:16:02.944` (frame 11)
- pcap child id request: `13:16:03.240` (frame 13)
- pcap child id response: `13:16:03.303` (frame 15)

#### Attach sequence 2

- parent request: `13:20:03.692`
- parent response: `13:20:03.975`
- child id request: `13:20:04.403`
- child id response: `13:20:04.493`
- parent ipv6: `fe80:0:0:0:285f:b093:ea71:6159`
- parent extaddr: `2a5fb093ea716159`
- parent rloc16: `0x7800`
- timing source: **pcap**
- Request → Response: **286 ms**
- Response → Child ID Request: **464 ms**
- Child ID Request → Response: **64 ms**
- Full Attach: **814 ms**
- pcap parent request: `13:20:03.675` (frame 190)
- pcap parent response: `13:20:03.961` (frame 191)
- pcap child id request: `13:20:04.425` (frame 193)
- pcap child id response: `13:20:04.489` (frame 195)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 117: 16, seq 118: 16, seq 119: 16, seq 120: 16
- failed tx by dst: `bedb8fc6c5b0f089`: 55

### `stock_child_20260609-132048-run06.log`

#### Attach sequence 1

- parent request: `13:21:27.808`
- parent response: `13:21:28.271`
- child id request: `13:21:28.518`
- child id response: `13:21:28.610`
- parent ipv6: `fe80:0:0:0:815:b558:c755:e35f`
- parent extaddr: `0a15b558c755e35f`
- parent rloc16: `0xa800`
- timing source: **pcap**
- Request → Response: **467 ms**
- Response → Child ID Request: **283 ms**
- Child ID Request → Response: **63 ms**
- Full Attach: **813 ms**
- pcap parent request: `13:21:27.782` (frame 9)
- pcap parent response: `13:21:28.249` (frame 11)
- pcap child id request: `13:21:28.532` (frame 13)
- pcap child id response: `13:21:28.595` (frame 15)

#### Attach sequence 2

- parent request: `13:25:28.442`
- parent response: `13:25:28.728`
- child id request: `13:25:29.150`
- child id response: `13:25:29.241`
- parent ipv6: `fe80:0:0:0:d44e:d714:51be:fc49`
- parent extaddr: `d64ed71451befc49`
- parent rloc16: `0xec00`
- timing source: **pcap**
- Request → Response: **290 ms**
- Response → Child ID Request: **458 ms**
- Child ID Request → Response: **65 ms**
- Full Attach: **813 ms**
- pcap parent request: `13:25:28.424` (frame 178)
- pcap parent response: `13:25:28.714` (frame 179)
- pcap child id request: `13:25:29.172` (frame 181)
- pcap child id response: `13:25:29.237` (frame 183)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 165: 16, seq 166: 16, seq 167: 16, seq 168: 16
- failed tx by dst: `0a15b558c755e35f`: 52

### `stock_child_20260609-132613-run07.log`

#### Attach sequence 1

- parent request: `13:26:53.459`
- parent response: `13:26:53.810`
- child id request: `13:26:54.230`
- child id response: `13:26:54.318`
- parent ipv6: `fe80:0:0:0:2438:3cd0:33c8:44a6`
- parent extaddr: `26383cd033c844a6`
- parent rloc16: `0x7400`
- timing source: **pcap**
- Request → Response: **292 ms**
- Response → Child ID Request: **456 ms**
- Child ID Request → Response: **63 ms**
- Full Attach: **811 ms**
- pcap parent request: `13:26:53.495` (frame 10)
- pcap parent response: `13:26:53.787` (frame 11)
- pcap child id request: `13:26:54.243` (frame 13)
- pcap child id response: `13:26:54.306` (frame 15)

#### Attach sequence 2

- parent request: `13:30:54.630`
- parent response: `13:30:54.724`
- child id request: `13:30:55.384`
- child id response: `13:30:55.430`
- parent ipv6: `fe80:0:0:0:4d8:65ff:5f38:14a3`
- parent extaddr: `06d865ff5f3814a3`
- parent rloc16: `0x7800`
- timing source: **pcap**
- Request → Response: **96 ms**
- Response → Child ID Request: **654 ms**
- Child ID Request → Response: **64 ms**
- Full Attach: **814 ms**
- pcap parent request: `13:30:54.613` (frame 186)
- pcap parent response: `13:30:54.709` (frame 187)
- pcap child id request: `13:30:55.363` (frame 189)
- pcap child id response: `13:30:55.427` (frame 191)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 176: 16, seq 177: 16, seq 178: 16, seq 179: 16
- failed tx by dst: `26383cd033c844a6`: 53

### `stock_child_20260609-133139-run08.log`

#### Attach sequence 1

- parent request: `13:32:19.585`
- parent response: `13:32:19.895`
- child id request: `13:32:20.291`
- child id response: `13:32:20.380`
- parent ipv6: `fe80:0:0:0:7c4b:f0a6:b643:f032`
- parent extaddr: `7e4bf0a6b643f032`
- parent rloc16: `0xf800`
- timing source: **pcap**
- Request → Response: **320 ms**
- Response → Child ID Request: **432 ms**
- Child ID Request → Response: **63 ms**
- Full Attach: **815 ms**
- pcap parent request: `13:32:19.553` (frame 9)
- pcap parent response: `13:32:19.873` (frame 11)
- pcap child id request: `13:32:20.305` (frame 13)
- pcap child id response: `13:32:20.368` (frame 15)

#### Attach sequence 2

- parent request: `13:36:20.390`
- parent response: `13:36:20.466`
- child id request: `13:36:21.144`
- child id response: `13:36:21.190`
- parent ipv6: `fe80:0:0:0:9073:1531:9460:8f88`
- parent extaddr: `9273153194608f88`
- parent rloc16: `0xe800`
- timing source: **pcap**
- Request → Response: **79 ms**
- Response → Child ID Request: **670 ms**
- Child ID Request → Response: **63 ms**
- Full Attach: **812 ms**
- pcap parent request: `13:36:20.373` (frame 189)
- pcap parent response: `13:36:20.452` (frame 190)
- pcap child id request: `13:36:21.122` (frame 192)
- pcap child id response: `13:36:21.185` (frame 194)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 0: 16, seq 1: 16, seq 2: 16, seq 3: 16
- failed tx by dst: `7e4bf0a6b643f032`: 54

### `stock_child_20260609-133705-run09.log`

#### Attach sequence 1

- parent request: `13:37:45.850`
- parent response: `13:37:46.036`
- child id request: `13:37:46.561`
- child id response: `13:37:46.648`
- parent ipv6: `fe80:0:0:0:b849:20f8:364c:4ef6`
- parent extaddr: `ba4920f8364c4ef6`
- parent rloc16: `0x7c00`
- timing source: **pcap**
- Request → Response: **189 ms**
- Response → Child ID Request: **560 ms**
- Child ID Request → Response: **62 ms**
- Full Attach: **811 ms**
- pcap parent request: `13:37:45.825` (frame 10)
- pcap parent response: `13:37:46.014` (frame 11)
- pcap child id request: `13:37:46.574` (frame 13)
- pcap child id response: `13:37:46.636` (frame 15)

#### Attach sequence 2

- parent request: `13:41:46.724`
- parent response: `13:41:47.118`
- child id request: `13:41:47.434`
- child id response: `13:41:47.523`
- parent ipv6: `fe80:0:0:0:f887:c11f:9e:40a5`
- parent extaddr: `fa87c11f009e40a5`
- parent rloc16: `0x8c00`
- timing source: **pcap**
- Request → Response: **397 ms**
- Response → Child ID Request: **353 ms**
- Child ID Request → Response: **63 ms**
- Full Attach: **813 ms**
- pcap parent request: `13:41:46.707` (frame 179)
- pcap parent response: `13:41:47.104` (frame 180)
- pcap child id request: `13:41:47.457` (frame 182)
- pcap child id response: `13:41:47.520` (frame 184)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 89: 16, seq 90: 16, seq 91: 16, seq 92: 16
- failed tx by dst: `ba4920f8364c4ef6`: 49

### `stock_child_20260609-134231-run10.log`

#### Attach sequence 1

- parent request: `13:43:11.244`
- parent response: `13:43:11.507`
- child id request: `13:43:11.953`
- child id response: `13:43:12.044`
- parent ipv6: `fe80:0:0:0:6c17:7a32:c57:a3e9`
- parent extaddr: `6e177a320c57a3e9`
- parent rloc16: `0x0000`
- timing source: **pcap**
- Request → Response: **268 ms**
- Response → Child ID Request: **483 ms**
- Child ID Request → Response: **64 ms**
- Full Attach: **815 ms**
- pcap parent request: `13:43:11.216` (frame 9)
- pcap parent response: `13:43:11.484` (frame 10)
- pcap child id request: `13:43:11.967` (frame 13)
- pcap child id response: `13:43:12.031` (frame 15)

#### Attach sequence 2

- parent request: `13:47:12.033`
- parent response: `13:47:12.292`
- child id request: `13:47:12.740`
- child id response: `13:47:12.831`
- parent ipv6: `fe80:0:0:0:68b6:841b:226:999f`
- parent extaddr: `6ab6841b0226999f`
- parent rloc16: `0xa800`
- timing source: **pcap**
- Request → Response: **261 ms**
- Response → Child ID Request: **488 ms**
- Child ID Request → Response: **63 ms**
- Full Attach: **812 ms**
- pcap parent request: `13:47:12.016` (frame 189)
- pcap parent response: `13:47:12.277` (frame 190)
- pcap child id request: `13:47:12.765` (frame 192)
- pcap child id response: `13:47:12.828` (frame 194)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 48: 16, seq 49: 16, seq 50: 16, seq 51: 16
- failed tx by dst: `6e177a320c57a3e9`: 55

### `stock_child_20260609-134757-run11.log`

#### Attach sequence 1

- parent request: `13:48:37.326`
- parent response: `13:48:37.779`
- child id request: `13:48:38.036`
- child id response: `13:48:38.124`
- parent ipv6: `fe80:0:0:0:e483:65a2:e6e9:661d`
- parent extaddr: `e68365a2e6e9661d`
- parent rloc16: `0xc800`
- timing source: **pcap**
- Request → Response: **458 ms**
- Response → Child ID Request: **293 ms**
- Child ID Request → Response: **63 ms**
- Full Attach: **814 ms**
- pcap parent request: `13:48:37.299` (frame 9)
- pcap parent response: `13:48:37.757` (frame 11)
- pcap child id request: `13:48:38.050` (frame 13)
- pcap child id response: `13:48:38.113` (frame 15)

#### Attach sequence 2

- parent request: `13:52:38.145`
- parent response: `13:52:38.608`
- child id request: `13:52:38.900`
- child id response: `13:52:38.946`
- parent ipv6: `fe80:0:0:0:8c7f:6489:ef9e:70b5`
- parent extaddr: `8e7f6489ef9e70b5`
- parent rloc16: `0x7c00`
- timing source: **pcap**
- Request → Response: **465 ms**
- Response → Child ID Request: **285 ms**
- Child ID Request → Response: **63 ms**
- Full Attach: **813 ms**
- pcap parent request: `13:52:38.130` (frame 190)
- pcap parent response: `13:52:38.595` (frame 191)
- pcap child id request: `13:52:38.880` (frame 193)
- pcap child id response: `13:52:38.943` (frame 195)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 117: 16, seq 118: 16, seq 119: 16, seq 120: 16
- failed tx by dst: `e68365a2e6e9661d`: 49

### `stock_child_20260609-154439-run01.log`

#### Attach sequence 1

- parent request: `15:45:19.352`
- parent response: `15:45:19.848`
- child id request: `15:45:20.168`
- child id response: `15:45:20.256`
- parent ipv6: `fe80:0:0:0:cc9a:fdd0:fbb:a438`
- parent extaddr: `ce9afdd00fbba438`
- parent rloc16: `0x3800`
- timing source: **pcap**
- Request → Response: **437 ms**
- Response → Child ID Request: **357 ms**
- Child ID Request → Response: **62 ms**
- Full Attach: **856 ms**
- pcap parent request: `15:45:19.389` (frame 9)
- pcap parent response: `15:45:19.826` (frame 10)
- pcap child id request: `15:45:20.183` (frame 13)
- pcap child id response: `15:45:20.245` (frame 15)

#### Attach sequence 2

- parent request: `15:49:20.216`
- parent response: `15:49:20.259`
- child id request: `15:49:20.927`
- child id response: `15:49:21.017`
- parent ipv6: `fe80:0:0:0:f4b9:3c9e:6565:b643`
- parent extaddr: `f6b93c9e6565b643`
- parent rloc16: `0x3400`
- timing source: **pcap**
- Request → Response: **43 ms**
- Response → Child ID Request: **707 ms**
- Child ID Request → Response: **63 ms**
- Full Attach: **813 ms**
- pcap parent request: `15:49:20.201` (frame 185)
- pcap parent response: `15:49:20.244` (frame 186)
- pcap child id request: `15:49:20.951` (frame 188)
- pcap child id response: `15:49:21.014` (frame 190)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 201: 16, seq 202: 16, seq 203: 16, seq 204: 16
- failed tx by dst: `ce9afdd00fbba438`: 52

### `stock_child_20260609-155005-run02.log`

#### Attach sequence 1

- parent request: `15:50:45.759`
- parent response: `15:50:46.086`
- child id request: `15:50:46.518`
- child id response: `15:50:46.558`
- parent ipv6: `fe80:0:0:0:40bb:d61e:2b91:26ab`
- parent extaddr: `42bbd61e2b9126ab`
- parent rloc16: `0x6800`
- timing source: **pcap**
- Request → Response: **329 ms**
- Response → Child ID Request: **419 ms**
- Child ID Request → Response: **62 ms**
- Full Attach: **810 ms**
- pcap parent request: `15:50:45.734` (frame 10)
- pcap parent response: `15:50:46.063` (frame 11)
- pcap child id request: `15:50:46.482` (frame 13)
- pcap child id response: `15:50:46.544` (frame 15)

#### Attach sequence 2

- parent request: `15:54:46.854`
- parent response: `15:54:46.939`
- child id request: `15:54:47.608`
- child id response: `15:54:47.655`
- parent ipv6: `fe80:0:0:0:1cec:2697:c070:3356`
- parent extaddr: `1eec2697c0703356`
- parent rloc16: `0xc400`
- timing source: **pcap**
- Request → Response: **87 ms**
- Response → Child ID Request: **662 ms**
- Child ID Request → Response: **64 ms**
- Full Attach: **813 ms**
- pcap parent request: `15:54:46.838` (frame 184)
- pcap parent response: `15:54:46.925` (frame 185)
- pcap child id request: `15:54:47.587` (frame 187)
- pcap child id response: `15:54:47.651` (frame 189)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 115: 16, seq 116: 16, seq 117: 16, seq 118: 16
- failed tx by dst: `42bbd61e2b9126ab`: 57

### `stock_child_20260609-164122-run01.log`

#### Attach sequence 1

- parent request: `16:42:02.554`
- parent response: `16:42:02.947`
- child id request: `16:42:03.264`
- child id response: `16:42:03.354`
- parent ipv6: `fe80:0:0:0:9889:b4ec:703c:ac1a`
- parent extaddr: `9a89b4ec703cac1a`
- parent rloc16: `0x8400`
- timing source: **pcap**
- Request → Response: **395 ms**
- Response → Child ID Request: **354 ms**
- Child ID Request → Response: **65 ms**
- Full Attach: **814 ms**
- pcap parent request: `16:42:02.529` (frame 10)
- pcap parent response: `16:42:02.924` (frame 11)
- pcap child id request: `16:42:03.278` (frame 13)
- pcap child id response: `16:42:03.343` (frame 15)

#### Attach sequence 2

- parent request: `16:46:03.264`
- parent response: `16:46:03.448`
- child id request: `16:46:03.975`
- child id response: `16:46:04.063`
- parent ipv6: `fe80:0:0:0:208f:10db:6773:1a6b`
- parent extaddr: `228f10db67731a6b`
- parent rloc16: `0x1800`
- timing source: **pcap**
- Request → Response: **187 ms**
- Response → Child ID Request: **563 ms**
- Child ID Request → Response: **63 ms**
- Full Attach: **813 ms**
- pcap parent request: `16:46:03.248` (frame 185)
- pcap parent response: `16:46:03.435` (frame 186)
- pcap child id request: `16:46:03.998` (frame 188)
- pcap child id response: `16:46:04.061` (frame 190)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 116: 16, seq 117: 16, seq 118: 16, seq 119: 16
- failed tx by dst: `9a89b4ec703cac1a`: 51

### `stock_child_20260609-164648-run02.log`

#### Attach sequence 1

- parent request: `16:47:28.343`
- parent response: `16:47:28.582`
- child id request: `16:47:29.020`
- child id response: `16:47:29.109`
- parent ipv6: `fe80:0:0:0:64ee:d14:2673:e3f3`
- parent extaddr: `66ee0d142673e3f3`
- parent rloc16: `0xe400`
- timing source: **pcap**
- Request → Response: **279 ms**
- Response → Child ID Request: **473 ms**
- Child ID Request → Response: **64 ms**
- Full Attach: **816 ms**
- pcap parent request: `16:47:28.282` (frame 10)
- pcap parent response: `16:47:28.561` (frame 11)
- pcap child id request: `16:47:29.034` (frame 13)
- pcap child id response: `16:47:29.098` (frame 15)

#### Attach sequence 2

- parent request: `16:51:29.430`
- parent response: `16:51:29.471`
- child id request: `16:51:30.141`
- child id response: `16:51:30.231`
- parent ipv6: `fe80:0:0:0:a82c:25f5:18ba:18c6`
- parent extaddr: `aa2c25f518ba18c6`
- parent rloc16: `0x3c00`
- timing source: **pcap**
- Request → Response: **44 ms**
- Response → Child ID Request: **706 ms**
- Child ID Request → Response: **64 ms**
- Full Attach: **814 ms**
- pcap parent request: `16:51:29.414` (frame 186)
- pcap parent response: `16:51:29.458` (frame 187)
- pcap child id request: `16:51:30.164` (frame 189)
- pcap child id response: `16:51:30.228` (frame 191)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 210: 16, seq 211: 16, seq 212: 16, seq 213: 16
- failed tx by dst: `66ee0d142673e3f3`: 53

### `stock_child_20260609-165214-run03.log`

#### Attach sequence 1

- parent request: `16:52:54.746`
- parent response: `16:52:54.787`
- child id request: `16:52:55.454`
- child id response: `16:52:55.544`
- parent ipv6: `fe80:0:0:0:509c:cfb:5f5e:1c99`
- parent extaddr: `529c0cfb5f5e1c99`
- parent rloc16: `0xc400`
- timing source: **pcap**
- Request → Response: **45 ms**
- Response → Child ID Request: **703 ms**
- Child ID Request → Response: **64 ms**
- Full Attach: **812 ms**
- pcap parent request: `16:52:54.721` (frame 10)
- pcap parent response: `16:52:54.766` (frame 11)
- pcap child id request: `16:52:55.469` (frame 13)
- pcap child id response: `16:52:55.533` (frame 15)

#### Attach sequence 2

- parent request: `16:56:55.617`
- parent response: `16:56:56.064`
- child id request: `16:56:56.329`
- child id response: `16:56:56.419`
- parent ipv6: `fe80:0:0:0:a054:6762:9a24:7334`
- parent extaddr: `a25467629a247334`
- parent rloc16: `0xf800`
- timing source: **pcap**
- Request → Response: **450 ms**
- Response → Child ID Request: **300 ms**
- Child ID Request → Response: **64 ms**
- Full Attach: **814 ms**
- pcap parent request: `16:56:55.602` (frame 191)
- pcap parent response: `16:56:56.052` (frame 192)
- pcap child id request: `16:56:56.352` (frame 194)
- pcap child id response: `16:56:56.416` (frame 196)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 152: 16, seq 153: 16, seq 154: 16, seq 155: 16
- failed tx by dst: `529c0cfb5f5e1c99`: 50

### `stock_child_20260609-165740-run04.log`

#### Attach sequence 1

- parent request: `16:58:20.753`
- parent response: `16:58:20.823`
- child id request: `16:58:21.463`
- child id response: `16:58:21.552`
- parent ipv6: `fe80:0:0:0:b81e:c390:ad5a:f2a2`
- parent extaddr: `ba1ec390ad5af2a2`
- parent rloc16: `0x6800`
- timing source: **pcap**
- Request → Response: **74 ms**
- Response → Child ID Request: **676 ms**
- Child ID Request → Response: **63 ms**
- Full Attach: **813 ms**
- pcap parent request: `16:58:20.728` (frame 10)
- pcap parent response: `16:58:20.802` (frame 11)
- pcap child id request: `16:58:21.478` (frame 13)
- pcap child id response: `16:58:21.541` (frame 15)

#### Attach sequence 2

- parent request: `17:02:21.549`
- parent response: `17:02:21.975`
- child id request: `17:02:22.260`
- child id response: `17:02:22.352`
- parent ipv6: `fe80:0:0:0:b001:e899:d121:97`
- parent extaddr: `b201e899d1210097`
- parent rloc16: `0x5000`
- timing source: **pcap**
- Request → Response: **427 ms**
- Response → Child ID Request: **323 ms**
- Child ID Request → Response: **64 ms**
- Full Attach: **814 ms**
- pcap parent request: `17:02:21.535` (frame 179)
- pcap parent response: `17:02:21.962` (frame 180)
- pcap child id request: `17:02:22.285` (frame 182)
- pcap child id response: `17:02:22.349` (frame 184)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 25: 16, seq 26: 16, seq 27: 16, seq 28: 16
- failed tx by dst: `ba1ec390ad5af2a2`: 53

### `stock_child_20260609-170306-run05.log`

#### Attach sequence 1

- parent request: `17:03:46.223`
- parent response: `17:03:46.629`
- child id request: `17:03:47.044`
- child id response: `17:03:47.091`
- parent ipv6: `fe80:0:0:0:9059:1cd5:5c98:efdb`
- parent extaddr: `92591cd55c98efdb`
- parent rloc16: `0x2400`
- timing source: **pcap**
- Request → Response: **310 ms**
- Response → Child ID Request: **404 ms**
- Child ID Request → Response: **68 ms**
- Full Attach: **782 ms**
- pcap parent request: `17:03:46.297` (frame 9)
- pcap parent response: `17:03:46.607` (frame 10)
- pcap child id request: `17:03:47.011` (frame 12)
- pcap child id response: `17:03:47.079` (frame 14)

#### Attach sequence 2

- parent request: `17:07:46.802`
- parent response: `17:07:46.896`
- child id request: `17:07:47.556`
- child id response: `17:07:47.602`
- parent ipv6: `fe80:0:0:0:6cdb:b871:419d:75a0`
- parent extaddr: `6edbb871419d75a0`
- parent rloc16: `0xc800`
- timing source: **pcap**
- Request → Response: **97 ms**
- Response → Child ID Request: **653 ms**
- Child ID Request → Response: **63 ms**
- Full Attach: **813 ms**
- pcap parent request: `17:07:46.785` (frame 190)
- pcap parent response: `17:07:46.882` (frame 191)
- pcap child id request: `17:07:47.535` (frame 193)
- pcap child id response: `17:07:47.598` (frame 195)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 16: 16, seq 17: 16, seq 18: 16, seq 19: 16
- failed tx by dst: `92591cd55c98efdb`: 54

### `stock_child_20260609-170832-run06.log`

#### Attach sequence 1

- parent request: `17:09:12.664`
- parent response: `17:09:13.012`
- child id request: `17:09:13.376`
- child id response: `17:09:13.465`
- parent ipv6: `fe80:0:0:0:7844:f219:b1f:6588`
- parent extaddr: `7a44f2190b1f6588`
- parent rloc16: `0x2000`
- timing source: **pcap**
- Request → Response: **351 ms**
- Response → Child ID Request: **400 ms**
- Child ID Request → Response: **63 ms**
- Full Attach: **814 ms**
- pcap parent request: `17:09:12.638` (frame 10)
- pcap parent response: `17:09:12.989` (frame 11)
- pcap child id request: `17:09:13.389` (frame 13)
- pcap child id response: `17:09:13.452` (frame 15)

#### Attach sequence 2

- parent request: `17:13:13.870`
- parent response: `17:13:14.317`
- child id request: `17:13:14.580`
- child id response: `17:13:14.671`
- parent ipv6: `fe80:0:0:0:8838:1fca:b61b:7f5a`
- parent extaddr: `8a381fcab61b7f5a`
- parent rloc16: `0x2400`
- timing source: **pcap**
- Request → Response: **449 ms**
- Response → Child ID Request: **300 ms**
- Child ID Request → Response: **64 ms**
- Full Attach: **813 ms**
- pcap parent request: `17:13:13.852` (frame 189)
- pcap parent response: `17:13:14.301` (frame 190)
- pcap child id request: `17:13:14.601` (frame 192)
- pcap child id response: `17:13:14.665` (frame 194)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 84: 16, seq 85: 16, seq 86: 16, seq 87: 16
- failed tx by dst: `7a44f2190b1f6588`: 53

### `stock_child_20260609-171358-run07.log`

#### Attach sequence 1

- parent request: `17:14:38.416`
- parent response: `17:14:38.945`
- child id request: `17:14:39.187`
- child id response: `17:14:39.276`
- parent ipv6: `fe80:0:0:0:f89c:7238:4e0e:11f4`
- parent extaddr: `fa9c72384e0e11f4`
- parent rloc16: `0x5400`
- timing source: **pcap**
- Request → Response: **466 ms**
- Response → Child ID Request: **277 ms**
- Child ID Request → Response: **64 ms**
- Full Attach: **807 ms**
- pcap parent request: `17:14:38.457` (frame 9)
- pcap parent response: `17:14:38.923` (frame 11)
- pcap child id request: `17:14:39.200` (frame 13)
- pcap child id response: `17:14:39.264` (frame 15)

#### Attach sequence 2

- parent request: `17:18:39.174`
- parent response: `17:18:39.440`
- child id request: `17:18:39.927`
- child id response: `17:18:39.976`
- parent ipv6: `fe80:0:0:0:a814:a148:361e:2560`
- parent extaddr: `aa14a148361e2560`
- parent rloc16: `0xf800`
- timing source: **pcap**
- Request → Response: **268 ms**
- Response → Child ID Request: **482 ms**
- Child ID Request → Response: **65 ms**
- Full Attach: **815 ms**
- pcap parent request: `17:18:39.156` (frame 180)
- pcap parent response: `17:18:39.424` (frame 181)
- pcap child id request: `17:18:39.906` (frame 183)
- pcap child id response: `17:18:39.971` (frame 185)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 54: 16, seq 55: 16, seq 56: 16, seq 57: 16
- failed tx by dst: `fa9c72384e0e11f4`: 48

### `stock_child_20260609-171924-run08.log`

#### Attach sequence 1

- parent request: `17:20:04.831`
- parent response: `17:20:05.352`
- child id request: `17:20:05.602`
- child id response: `17:20:05.691`
- parent ipv6: `fe80:0:0:0:f08e:84c5:fba3:1dca`
- parent extaddr: `f28e84c5fba31dca`
- parent rloc16: `0xd800`
- timing source: **pcap**
- Request → Response: **464 ms**
- Response → Child ID Request: **286 ms**
- Child ID Request → Response: **63 ms**
- Full Attach: **813 ms**
- pcap parent request: `17:20:04.864` (frame 9)
- pcap parent response: `17:20:05.328` (frame 11)
- pcap child id request: `17:20:05.614` (frame 13)
- pcap child id response: `17:20:05.677` (frame 15)

#### Attach sequence 2

- parent request: `17:24:05.271`
- parent response: `17:24:05.524`
- child id request: `17:24:06.090`
- child id response: `17:24:06.136`
- parent ipv6: `fe80:0:0:0:8c81:8b4f:4e40:e66d`
- parent extaddr: `8e818b4f4e40e66d`
- parent rloc16: `0x7000`
- timing source: **pcap**
- Request → Response: **191 ms**
- Response → Child ID Request: **560 ms**
- Child ID Request → Response: **63 ms**
- Full Attach: **814 ms**
- pcap parent request: `17:24:05.316` (frame 187)
- pcap parent response: `17:24:05.507` (frame 188)
- pcap child id request: `17:24:06.067` (frame 190)
- pcap child id response: `17:24:06.130` (frame 192)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 1: 1, seq 174: 15, seq 175: 16, seq 176: 16, seq 177: 16
- failed tx by dst: `f28e84c5fba31dca`: 55

### `stock_child_20260609-172450-run09.log`

#### Attach sequence 1

- parent request: `17:25:31.231`
- parent response: `17:25:31.613`
- child id request: `17:25:31.939`
- child id response: `17:25:32.027`
- parent ipv6: `fe80:0:0:0:98de:4ee0:e9bc:68f`
- parent extaddr: `9ade4ee0e9bc068f`
- parent rloc16: `0xa000`
- timing source: **pcap**
- Request → Response: **384 ms**
- Response → Child ID Request: **364 ms**
- Child ID Request → Response: **62 ms**
- Full Attach: **810 ms**
- pcap parent request: `17:25:31.204` (frame 10)
- pcap parent response: `17:25:31.588` (frame 11)
- pcap child id request: `17:25:31.952` (frame 13)
- pcap child id response: `17:25:32.014` (frame 15)

#### Attach sequence 2

- parent request: `17:29:31.886`
- parent response: `17:29:32.266`
- child id request: `17:29:32.597`
- child id response: `17:29:32.688`
- parent ipv6: `fe80:0:0:0:9c5a:f9d2:1a36:b849`
- parent extaddr: `9e5af9d21a36b849`
- parent rloc16: `0x7000`
- timing source: **pcap**
- Request → Response: **383 ms**
- Response → Child ID Request: **368 ms**
- Child ID Request → Response: **64 ms**
- Full Attach: **815 ms**
- pcap parent request: `17:29:31.868` (frame 192)
- pcap parent response: `17:29:32.251` (frame 193)
- pcap child id request: `17:29:32.619` (frame 195)
- pcap child id response: `17:29:32.683` (frame 197)

#### Failed TX summary

- failed tx attempts: **60**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 239: 16, seq 240: 16, seq 241: 15, seq 242: 13
- failed tx by dst: `9ade4ee0e9bc068f`: 51

### `stock_child_20260609-173016-run10.log`

#### Attach sequence 1

- parent request: `17:30:56.691`
- parent response: `17:30:57.048`
- child id request: `17:30:57.464`
- child id response: `17:30:57.552`
- parent ipv6: `fe80:0:0:0:dca2:6af3:80b:7617`
- parent extaddr: `dea26af3080b7617`
- parent rloc16: `0xac00`
- timing source: **pcap**
- Request → Response: **299 ms**
- Response → Child ID Request: **451 ms**
- Child ID Request → Response: **63 ms**
- Full Attach: **813 ms**
- pcap parent request: `17:30:56.725` (frame 9)
- pcap parent response: `17:30:57.024` (frame 10)
- pcap child id request: `17:30:57.475` (frame 13)
- pcap child id response: `17:30:57.538` (frame 15)

#### Attach sequence 2

- parent request: `17:34:57.892`
- parent response: `17:34:58.015`
- child id request: `17:34:58.603`
- child id response: `17:34:58.693`
- parent ipv6: `fe80:0:0:0:604a:f4c3:3f0a:2e54`
- parent extaddr: `624af4c33f0a2e54`
- parent rloc16: `0x0800`
- timing source: **pcap**
- Request → Response: **126 ms**
- Response → Child ID Request: **624 ms**
- Child ID Request → Response: **64 ms**
- Full Attach: **814 ms**
- pcap parent request: `17:34:57.874` (frame 180)
- pcap parent response: `17:34:58.000` (frame 181)
- pcap child id request: `17:34:58.624` (frame 183)
- pcap child id response: `17:34:58.688` (frame 185)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 38: 16, seq 39: 16, seq 40: 16, seq 41: 16
- failed tx by dst: `dea26af3080b7617`: 54

### `stock_child_20260609-173543-run11.log`

#### Attach sequence 1

- parent request: `17:36:22.834`
- parent response: `17:36:23.187`
- child id request: `17:36:23.653`
- child id response: `17:36:23.699`
- parent ipv6: `fe80:0:0:0:c79:d4ce:9ea7:8fad`
- parent extaddr: `0e79d4ce9ea78fad`
- parent rloc16: `0x5c00`
- timing source: **pcap**
- Request → Response: **257 ms**
- Response → Child ID Request: **457 ms**
- Child ID Request → Response: **65 ms**
- Full Attach: **779 ms**
- pcap parent request: `17:36:22.905` (frame 9)
- pcap parent response: `17:36:23.162` (frame 10)
- pcap child id request: `17:36:23.619` (frame 13)
- pcap child id response: `17:36:23.684` (frame 15)

#### Attach sequence 2

- parent request: `17:40:23.902`
- parent response: `17:40:24.391`
- child id request: `17:40:24.657`
- child id response: `17:40:24.704`
- parent ipv6: `fe80:0:0:0:e8cf:2cfc:6384:9ba3`
- parent extaddr: `eacf2cfc63849ba3`
- parent rloc16: `0x3c00`
- timing source: **pcap**
- Request → Response: **492 ms**
- Response → Child ID Request: **259 ms**
- Child ID Request → Response: **64 ms**
- Full Attach: **815 ms**
- pcap parent request: `17:40:23.883` (frame 188)
- pcap parent response: `17:40:24.375` (frame 189)
- pcap child id request: `17:40:24.634` (frame 191)
- pcap child id response: `17:40:24.698` (frame 193)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 51: 16, seq 52: 16, seq 53: 16, seq 54: 16
- failed tx by dst: `0e79d4ce9ea78fad`: 55

### `stock_child_20260609-174109-run12.log`

#### Attach sequence 1

- parent request: `17:41:49.678`
- parent response: `17:41:49.942`
- child id request: `17:41:50.387`
- child id response: `17:41:50.476`
- parent ipv6: `fe80:0:0:0:487:62a9:ca92:7a4b`
- parent extaddr: `068762a9ca927a4b`
- parent rloc16: `0xec00`
- timing source: **pcap**
- Request → Response: **270 ms**
- Response → Child ID Request: **481 ms**
- Child ID Request → Response: **63 ms**
- Full Attach: **814 ms**
- pcap parent request: `17:41:49.648` (frame 10)
- pcap parent response: `17:41:49.918` (frame 11)
- pcap child id request: `17:41:50.399` (frame 13)
- pcap child id response: `17:41:50.462` (frame 15)

#### Attach sequence 2

- parent request: `17:45:50.321`
- parent response: `17:45:50.518`
- child id request: `17:45:51.075`
- child id response: `17:45:51.122`
- parent ipv6: `fe80:0:0:0:804:b1c7:eb14:3eff`
- parent extaddr: `0a04b1c7eb143eff`
- parent rloc16: `0x6400`
- timing source: **pcap**
- Request → Response: **200 ms**
- Response → Child ID Request: **550 ms**
- Child ID Request → Response: **64 ms**
- Full Attach: **814 ms**
- pcap parent request: `17:45:50.303` (frame 179)
- pcap parent response: `17:45:50.503` (frame 180)
- pcap child id request: `17:45:51.053` (frame 182)
- pcap child id response: `17:45:51.117` (frame 184)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 78: 16, seq 79: 16, seq 80: 16, seq 81: 16
- failed tx by dst: `068762a9ca927a4b`: 48

### `stock_child_20260609-174635-run13.log`

#### Attach sequence 1

- parent request: `17:47:15.060`
- parent response: `17:47:15.540`
- child id request: `17:47:15.765`
- child id response: `17:47:15.856`
- parent ipv6: `fe80:0:0:0:7c1c:5eb:c482:4932`
- parent extaddr: `7e1c05ebc4824932`
- parent rloc16: `0x3400`
- timing source: **pcap**
- Request → Response: **485 ms**
- Response → Child ID Request: **263 ms**
- Child ID Request → Response: **62 ms**
- Full Attach: **810 ms**
- pcap parent request: `17:47:15.030` (frame 10)
- pcap parent response: `17:47:15.515` (frame 11)
- pcap child id request: `17:47:15.778` (frame 13)
- pcap child id response: `17:47:15.840` (frame 15)

#### Attach sequence 2

- parent request: `17:51:15.858`
- parent response: `17:51:16.353`
- child id request: `17:51:16.568`
- child id response: `17:51:16.658`
- parent ipv6: `fe80:0:0:0:18a2:6fa6:59ff:809`
- parent extaddr: `1aa26fa659ff0809`
- parent rloc16: `0xcc00`
- timing source: **pcap**
- Request → Response: **497 ms**
- Response → Child ID Request: **252 ms**
- Child ID Request → Response: **63 ms**
- Full Attach: **812 ms**
- pcap parent request: `17:51:15.839` (frame 178)
- pcap parent response: `17:51:16.336` (frame 179)
- pcap child id request: `17:51:16.588` (frame 181)
- pcap child id response: `17:51:16.651` (frame 183)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 20: 16, seq 21: 16, seq 22: 16, seq 23: 16
- failed tx by dst: `7e1c05ebc4824932`: 61

### `stock_child_20260609-175201-run14.log`

#### Attach sequence 1

- parent request: `17:52:41.115`
- parent response: `17:52:41.364`
- child id request: `17:52:41.828`
- child id response: `17:52:41.917`
- parent ipv6: `fe80:0:0:0:1017:4462:e650:2ea4`
- parent extaddr: `12174462e6502ea4`
- parent rloc16: `0xf800`
- timing source: **pcap**
- Request → Response: **250 ms**
- Response → Child ID Request: **499 ms**
- Child ID Request → Response: **64 ms**
- Full Attach: **813 ms**
- pcap parent request: `17:52:41.091` (frame 10)
- pcap parent response: `17:52:41.341` (frame 11)
- pcap child id request: `17:52:41.840` (frame 13)
- pcap child id response: `17:52:41.904` (frame 15)

#### Attach sequence 2

- parent request: `17:56:41.867`
- parent response: `17:56:42.109`
- child id request: `17:56:42.621`
- child id response: `17:56:42.667`
- parent ipv6: `fe80:0:0:0:acf9:b312:7d2f:dc13`
- parent extaddr: `aef9b3127d2fdc13`
- parent rloc16: `0x8800`
- timing source: **pcap**
- Request → Response: **243 ms**
- Response → Child ID Request: **506 ms**
- Child ID Request → Response: **63 ms**
- Full Attach: **812 ms**
- pcap parent request: `17:56:41.850` (frame 187)
- pcap parent response: `17:56:42.093` (frame 188)
- pcap child id request: `17:56:42.599` (frame 190)
- pcap child id response: `17:56:42.662` (frame 192)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 89: 16, seq 90: 16, seq 91: 16, seq 92: 16
- failed tx by dst: `12174462e6502ea4`: 50

### `stock_child_20260609-175727-run15.log`

#### Attach sequence 1

- parent request: `17:58:06.888`
- parent response: `17:58:07.361`
- child id request: `17:58:07.659`
- child id response: `17:58:07.749`
- parent ipv6: `fe80:0:0:0:5819:6f3e:a369:401b`
- parent extaddr: `5a196f3ea369401b`
- parent rloc16: `0x5400`
- timing source: **pcap**
- Request → Response: **416 ms**
- Response → Child ID Request: **334 ms**
- Child ID Request → Response: **65 ms**
- Full Attach: **815 ms**
- pcap parent request: `17:58:06.920` (frame 9)
- pcap parent response: `17:58:07.336` (frame 11)
- pcap child id request: `17:58:07.670` (frame 13)
- pcap child id response: `17:58:07.735` (frame 15)

#### Attach sequence 2

- parent request: `18:02:07.428`
- parent response: `18:02:07.886`
- child id request: `18:02:08.181`
- child id response: `18:02:08.226`
- parent ipv6: `fe80:0:0:0:dcae:ba8b:970:591a`
- parent extaddr: `deaeba8b0970591a`
- parent rloc16: `0x8400`
- timing source: **pcap**
- Request → Response: **461 ms**
- Response → Child ID Request: **288 ms**
- Child ID Request → Response: **63 ms**
- Full Attach: **812 ms**
- pcap parent request: `18:02:07.409` (frame 178)
- pcap parent response: `18:02:07.870` (frame 179)
- pcap child id request: `18:02:08.158` (frame 181)
- pcap child id response: `18:02:08.221` (frame 183)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 61: 16, seq 62: 16, seq 63: 16, seq 64: 16
- failed tx by dst: `5a196f3ea369401b`: 50

### `stock_child_20260609-181617-run01.log`

#### Attach sequence 1

- parent request: `18:16:57.398`
- parent response: `18:16:57.883`
- child id request: `18:16:58.072`
- child id response: `18:16:58.161`
- parent ipv6: `fe80:0:0:0:d4b8:e6f9:7793:28df`
- parent extaddr: `d6b8e6f9779328df`
- parent rloc16: `0x5000`
- timing source: **pcap**
- Request → Response: **523 ms**
- Response → Child ID Request: **225 ms**
- Child ID Request → Response: **64 ms**
- Full Attach: **812 ms**
- pcap parent request: `18:16:57.336` (frame 10)
- pcap parent response: `18:16:57.859` (frame 11)
- pcap child id request: `18:16:58.084` (frame 13)
- pcap child id response: `18:16:58.148` (frame 15)

#### Attach sequence 2

- parent request: `18:20:58.530`
- parent response: `18:20:59.034`
- child id request: `18:20:59.241`
- child id response: `18:20:59.331`
- parent ipv6: `fe80:0:0:0:648c:4188:fc6a:817f`
- parent extaddr: `668c4188fc6a817f`
- parent rloc16: `0xc000`
- timing source: **pcap**
- Request → Response: **507 ms**
- Response → Child ID Request: **245 ms**
- Child ID Request → Response: **62 ms**
- Full Attach: **814 ms**
- pcap parent request: `18:20:58.513` (frame 188)
- pcap parent response: `18:20:59.020` (frame 189)
- pcap child id request: `18:20:59.265` (frame 191)
- pcap child id response: `18:20:59.327` (frame 193)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 71: 16, seq 72: 16, seq 73: 16, seq 74: 16
- failed tx by dst: `d6b8e6f9779328df`: 53

### `stock_child_20260609-182143-run02.log`

#### Attach sequence 1

- parent request: `18:22:22.901`
- parent response: `18:22:23.008`
- child id request: `18:22:23.612`
- child id response: `18:22:23.701`
- parent ipv6: `fe80:0:0:0:bc82:eb49:764c:260`
- parent extaddr: `be82eb49764c0260`
- parent rloc16: `0x0800`
- timing source: **pcap**
- Request → Response: **111 ms**
- Response → Child ID Request: **640 ms**
- Child ID Request → Response: **63 ms**
- Full Attach: **814 ms**
- pcap parent request: `18:22:22.876` (frame 10)
- pcap parent response: `18:22:22.987` (frame 11)
- pcap child id request: `18:22:23.627` (frame 13)
- pcap child id response: `18:22:23.690` (frame 15)

#### Attach sequence 2

- parent request: `18:26:23.535`
- parent response: `18:26:23.956`
- child id request: `18:26:24.288`
- child id response: `18:26:24.335`
- parent ipv6: `fe80:0:0:0:c47d:e7e:77ee:e771`
- parent extaddr: `c67d0e7e77eee771`
- parent rloc16: `0x2000`
- timing source: **pcap**
- Request → Response: **424 ms**
- Response → Child ID Request: **325 ms**
- Child ID Request → Response: **64 ms**
- Full Attach: **813 ms**
- pcap parent request: `18:26:23.520` (frame 189)
- pcap parent response: `18:26:23.944` (frame 190)
- pcap child id request: `18:26:24.269` (frame 192)
- pcap child id response: `18:26:24.333` (frame 194)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 120: 16, seq 121: 16, seq 122: 16, seq 123: 16
- failed tx by dst: `be82eb49764c0260`: 54

### `stock_child_20260609-182709-run03.log`

#### Attach sequence 1

- parent request: `18:27:48.707`
- parent response: `18:27:49.099`
- child id request: `18:27:49.527`
- child id response: `18:27:49.571`
- parent ipv6: `fe80:0:0:0:4874:a6f4:bdc8:2a9d`
- parent extaddr: `4a74a6f4bdc82a9d`
- parent rloc16: `0x9000`
- timing source: **pcap**
- Request → Response: **297 ms**
- Response → Child ID Request: **418 ms**
- Child ID Request → Response: **65 ms**
- Full Attach: **780 ms**
- pcap parent request: `18:27:48.781` (frame 9)
- pcap parent response: `18:27:49.078` (frame 10)
- pcap child id request: `18:27:49.496` (frame 12)
- pcap child id response: `18:27:49.561` (frame 14)

#### Attach sequence 2

- parent request: `18:31:49.771`
- parent response: `18:31:49.884`
- child id request: `18:31:50.526`
- child id response: `18:31:50.571`
- parent ipv6: `fe80:0:0:0:3cc3:4405:7420:7600`
- parent extaddr: `3ec3440574207600`
- parent rloc16: `0x4000`
- timing source: **pcap**
- Request → Response: **114 ms**
- Response → Child ID Request: **636 ms**
- Child ID Request → Response: **63 ms**
- Full Attach: **813 ms**
- pcap parent request: `18:31:49.757` (frame 183)
- pcap parent response: `18:31:49.871` (frame 184)
- pcap child id request: `18:31:50.507` (frame 186)
- pcap child id response: `18:31:50.570` (frame 188)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 207: 16, seq 208: 16, seq 209: 16, seq 210: 16
- failed tx by dst: `4a74a6f4bdc82a9d`: 57

### `stock_child_20260609-183235-run04.log`

#### Attach sequence 1

- parent request: `18:33:14.858`
- parent response: `18:33:15.216`
- child id request: `18:33:15.568`
- child id response: `18:33:15.659`
- parent ipv6: `fe80:0:0:0:54c4:4f60:f9b4:f2e2`
- parent extaddr: `56c44f60f9b4f2e2`
- parent rloc16: `0x9400`
- timing source: **pcap**
- Request → Response: **361 ms**
- Response → Child ID Request: **389 ms**
- Child ID Request → Response: **64 ms**
- Full Attach: **814 ms**
- pcap parent request: `18:33:14.833` (frame 10)
- pcap parent response: `18:33:15.194` (frame 11)
- pcap child id request: `18:33:15.583` (frame 13)
- pcap child id response: `18:33:15.647` (frame 15)

#### Attach sequence 2

- parent request: `18:37:15.302`
- parent response: `18:37:15.799`
- child id request: `18:37:16.011`
- child id response: `18:37:16.101`
- parent ipv6: `fe80:0:0:0:9cbf:2e15:40d2:7836`
- parent extaddr: `9ebf2e1540d27836`
- parent rloc16: `0xe400`
- timing source: **pcap**
- Request → Response: **498 ms**
- Response → Child ID Request: **250 ms**
- Child ID Request → Response: **64 ms**
- Full Attach: **812 ms**
- pcap parent request: `18:37:15.287` (frame 189)
- pcap parent response: `18:37:15.785` (frame 190)
- pcap child id request: `18:37:16.035` (frame 192)
- pcap child id response: `18:37:16.099` (frame 194)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 77: 16, seq 78: 16, seq 79: 16, seq 80: 16
- failed tx by dst: `56c44f60f9b4f2e2`: 48

### `stock_child_20260609-183801-run05.log`

#### Attach sequence 1

- parent request: `18:38:41.242`
- parent response: `18:38:41.419`
- child id request: `18:38:42.015`
- child id response: `18:38:42.105`
- parent ipv6: `fe80:0:0:0:a4b1:9ed8:c699:74b9`
- parent extaddr: `a6b19ed8c69974b9`
- parent rloc16: `0x6c00`
- timing source: **pcap**
- Request → Response: **120 ms**
- Response → Child ID Request: **632 ms**
- Child ID Request → Response: **64 ms**
- Full Attach: **816 ms**
- pcap parent request: `18:38:41.278` (frame 10)
- pcap parent response: `18:38:41.398` (frame 11)
- pcap child id request: `18:38:42.030` (frame 13)
- pcap child id response: `18:38:42.094` (frame 15)

#### Attach sequence 2

- parent request: `18:42:42.299`
- parent response: `18:42:42.536`
- child id request: `18:42:43.055`
- child id response: `18:42:43.102`
- parent ipv6: `fe80:0:0:0:34f8:f6f1:ffb7:a69e`
- parent extaddr: `36f8f6f1ffb7a69e`
- parent rloc16: `0xc800`
- timing source: **pcap**
- Request → Response: **237 ms**
- Response → Child ID Request: **512 ms**
- Child ID Request → Response: **64 ms**
- Full Attach: **813 ms**
- pcap parent request: `18:42:42.287` (frame 174)
- pcap parent response: `18:42:42.524` (frame 175)
- pcap child id request: `18:42:43.036` (frame 177)
- pcap child id response: `18:42:43.100` (frame 179)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 78: 16, seq 79: 16, seq 80: 16, seq 81: 16
- failed tx by dst: `a6b19ed8c69974b9`: 52

### `stock_child_20260609-184327-run06.log`

#### Attach sequence 1

- parent request: `18:44:07.377`
- parent response: `18:44:07.630`
- child id request: `18:44:08.086`
- child id response: `18:44:08.173`
- parent ipv6: `fe80:0:0:0:c8ef:3dc5:7b99:5dc7`
- parent extaddr: `caef3dc57b995dc7`
- parent rloc16: `0xb400`
- timing source: **pcap**
- Request → Response: **256 ms**
- Response → Child ID Request: **492 ms**
- Child ID Request → Response: **62 ms**
- Full Attach: **810 ms**
- pcap parent request: `18:44:07.353` (frame 10)
- pcap parent response: `18:44:07.609` (frame 11)
- pcap child id request: `18:44:08.101` (frame 13)
- pcap child id response: `18:44:08.163` (frame 15)

#### Attach sequence 2

- parent request: `18:48:08.026`
- parent response: `18:48:08.241`
- child id request: `18:48:08.780`
- child id response: `18:48:08.827`
- parent ipv6: `fe80:0:0:0:307a:988e:d11d:1736`
- parent extaddr: `327a988ed11d1736`
- parent rloc16: `0x8c00`
- timing source: **pcap**
- Request → Response: **218 ms**
- Response → Child ID Request: **533 ms**
- Child ID Request → Response: **63 ms**
- Full Attach: **814 ms**
- pcap parent request: `18:48:08.010` (frame 178)
- pcap parent response: `18:48:08.228` (frame 179)
- pcap child id request: `18:48:08.761` (frame 181)
- pcap child id response: `18:48:08.824` (frame 183)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 25: 16, seq 26: 16, seq 27: 16, seq 28: 16
- failed tx by dst: `caef3dc57b995dc7`: 57

### `stock_child_20260609-184853-run07.log`

#### Attach sequence 1

- parent request: `18:49:33.427`
- parent response: `18:49:33.571`
- child id request: `18:49:34.138`
- child id response: `18:49:34.229`
- parent ipv6: `fe80:0:0:0:6038:a085:9c7c:dc15`
- parent extaddr: `6238a0859c7cdc15`
- parent rloc16: `0x8000`
- timing source: **pcap**
- Request → Response: **147 ms**
- Response → Child ID Request: **604 ms**
- Child ID Request → Response: **64 ms**
- Full Attach: **815 ms**
- pcap parent request: `18:49:33.402` (frame 10)
- pcap parent response: `18:49:33.549` (frame 11)
- pcap child id request: `18:49:34.153` (frame 13)
- pcap child id response: `18:49:34.217` (frame 15)

#### Attach sequence 2

- parent request: `18:53:34.539`
- parent response: `18:53:34.684`
- child id request: `18:53:35.252`
- child id response: `18:53:35.342`
- parent ipv6: `fe80:0:0:0:705b:e06:6b7f:1c58`
- parent extaddr: `725b0e066b7f1c58`
- parent rloc16: `0x5400`
- timing source: **pcap**
- Request → Response: **147 ms**
- Response → Child ID Request: **606 ms**
- Child ID Request → Response: **63 ms**
- Full Attach: **816 ms**
- pcap parent request: `18:53:34.523` (frame 189)
- pcap parent response: `18:53:34.670` (frame 190)
- pcap child id request: `18:53:35.276` (frame 192)
- pcap child id response: `18:53:35.339` (frame 194)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 145: 16, seq 146: 16, seq 147: 16, seq 148: 16
- failed tx by dst: `6238a0859c7cdc15`: 54

### `stock_child_20260609-185419-run08.log`

#### Attach sequence 1

- parent request: `18:54:58.860`
- parent response: `18:54:59.114`
- child id request: `18:54:59.679`
- child id response: `18:54:59.724`
- parent ipv6: `fe80:0:0:0:340a:2aff:5fa5:66c3`
- parent extaddr: `360a2aff5fa566c3`
- parent rloc16: `0xe400`
- timing source: **pcap**
- Request → Response: **158 ms**
- Response → Child ID Request: **556 ms**
- Child ID Request → Response: **64 ms**
- Full Attach: **778 ms**
- pcap parent request: `18:54:58.935` (frame 9)
- pcap parent response: `18:54:59.093` (frame 10)
- pcap child id request: `18:54:59.649` (frame 13)
- pcap child id response: `18:54:59.713` (frame 15)

#### Attach sequence 2

- parent request: `18:58:59.782`
- parent response: `18:59:00.183`
- child id request: `18:59:00.536`
- child id response: `18:59:00.584`
- parent ipv6: `fe80:0:0:0:8cca:a291:6e28:34f1`
- parent extaddr: `8ecaa2916e2834f1`
- parent rloc16: `0xec00`
- timing source: **pcap**
- Request → Response: **403 ms**
- Response → Child ID Request: **348 ms**
- Child ID Request → Response: **63 ms**
- Full Attach: **814 ms**
- pcap parent request: `18:58:59.767` (frame 190)
- pcap parent response: `18:59:00.170` (frame 191)
- pcap child id request: `18:59:00.518` (frame 193)
- pcap child id response: `18:59:00.581` (frame 195)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 48: 16, seq 49: 16, seq 50: 16, seq 51: 16
- failed tx by dst: `360a2aff5fa566c3`: 55

### `stock_child_20260609-185945-run09.log`

#### Attach sequence 1

- parent request: `19:00:24.830`
- parent response: `19:00:25.349`
- child id request: `19:00:25.601`
- child id response: `19:00:25.691`
- parent ipv6: `fe80:0:0:0:544e:dfb5:edfb:b91c`
- parent extaddr: `564edfb5edfbb91c`
- parent rloc16: `0x3400`
- timing source: **pcap**
- Request → Response: **457 ms**
- Response → Child ID Request: **288 ms**
- Child ID Request → Response: **63 ms**
- Full Attach: **808 ms**
- pcap parent request: `19:00:24.871` (frame 9)
- pcap parent response: `19:00:25.328` (frame 11)
- pcap child id request: `19:00:25.616` (frame 13)
- pcap child id response: `19:00:25.679` (frame 15)

#### Attach sequence 2

- parent request: `19:04:26.002`
- parent response: `19:04:26.069`
- child id request: `19:04:26.713`
- child id response: `19:04:26.804`
- parent ipv6: `fe80:0:0:0:988b:d866:5c55:a047`
- parent extaddr: `9a8bd8665c55a047`
- parent rloc16: `0x3c00`
- timing source: **pcap**
- Request → Response: **69 ms**
- Response → Child ID Request: **681 ms**
- Child ID Request → Response: **63 ms**
- Full Attach: **813 ms**
- pcap parent request: `19:04:25.987` (frame 190)
- pcap parent response: `19:04:26.056` (frame 191)
- pcap child id request: `19:04:26.737` (frame 193)
- pcap child id response: `19:04:26.800` (frame 195)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 79: 16, seq 80: 16, seq 81: 16, seq 82: 16
- failed tx by dst: `564edfb5edfbb91c`: 52

### `stock_child_20260609-190511-run10.log`

#### Attach sequence 1

- parent request: `19:05:51.233`
- parent response: `19:05:51.611`
- child id request: `19:05:52.006`
- child id response: `19:05:52.094`
- parent ipv6: `fe80:0:0:0:b826:cef0:9f2d:31ea`
- parent extaddr: `ba26cef09f2d31ea`
- parent rloc16: `0xd000`
- timing source: **pcap**
- Request → Response: **319 ms**
- Response → Child ID Request: **432 ms**
- Child ID Request → Response: **63 ms**
- Full Attach: **814 ms**
- pcap parent request: `19:05:51.269` (frame 9)
- pcap parent response: `19:05:51.588` (frame 11)
- pcap child id request: `19:05:52.020` (frame 13)
- pcap child id response: `19:05:52.083` (frame 15)

#### Attach sequence 2

- parent request: `19:09:52.392`
- parent response: `19:09:52.634`
- child id request: `19:09:53.146`
- child id response: `19:09:53.194`
- parent ipv6: `fe80:0:0:0:20ef:d258:792a:15c6`
- parent extaddr: `22efd258792a15c6`
- parent rloc16: `0x6c00`
- timing source: **pcap**
- Request → Response: **246 ms**
- Response → Child ID Request: **505 ms**
- Child ID Request → Response: **64 ms**
- Full Attach: **815 ms**
- pcap parent request: `19:09:52.375` (frame 186)
- pcap parent response: `19:09:52.621` (frame 187)
- pcap child id request: `19:09:53.126` (frame 189)
- pcap child id response: `19:09:53.190` (frame 191)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 0: 16, seq 253: 16, seq 254: 16, seq 255: 16
- failed tx by dst: `ba26cef09f2d31ea`: 52

### `stock_child_20260609-191037-run11.log`

#### Attach sequence 1

- parent request: `19:11:17.434`
- parent response: `19:11:17.966`
- child id request: `19:11:18.145`
- child id response: `19:11:18.236`
- parent ipv6: `fe80:0:0:0:9c56:efd:3d1d:5843`
- parent extaddr: `9e560efd3d1d5843`
- parent rloc16: `0x2c00`
- timing source: **pcap**
- Request → Response: **534 ms**
- Response → Child ID Request: **216 ms**
- Child ID Request → Response: **65 ms**
- Full Attach: **815 ms**
- pcap parent request: `19:11:17.409` (frame 9)
- pcap parent response: `19:11:17.943` (frame 11)
- pcap child id request: `19:11:18.159` (frame 13)
- pcap child id response: `19:11:18.224` (frame 15)

#### Attach sequence 2

- parent request: `19:15:18.336`
- parent response: `19:15:18.425`
- child id request: `19:15:19.089`
- child id response: `19:15:19.135`
- parent ipv6: `fe80:0:0:0:d4a5:d0da:25a3:8b06`
- parent extaddr: `d6a5d0da25a38b06`
- parent rloc16: `0xb400`
- timing source: **pcap**
- Request → Response: **92 ms**
- Response → Child ID Request: **657 ms**
- Child ID Request → Response: **63 ms**
- Full Attach: **812 ms**
- pcap parent request: `19:15:18.320` (frame 191)
- pcap parent response: `19:15:18.412` (frame 192)
- pcap child id request: `19:15:19.069` (frame 194)
- pcap child id response: `19:15:19.132` (frame 196)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 224: 16, seq 225: 16, seq 226: 16, seq 227: 16
- failed tx by dst: `9e560efd3d1d5843`: 51

### `stock_child_20260609-191603-run12.log`

#### Attach sequence 1

- parent request: `19:16:43.404`
- parent response: `19:16:43.811`
- child id request: `19:16:44.114`
- child id response: `19:16:44.203`
- parent ipv6: `fe80:0:0:0:501e:57ae:1dc7:a59b`
- parent extaddr: `521e57ae1dc7a59b`
- parent rloc16: `0x6c00`
- timing source: **pcap**
- Request → Response: **408 ms**
- Response → Child ID Request: **341 ms**
- Child ID Request → Response: **63 ms**
- Full Attach: **812 ms**
- pcap parent request: `19:16:43.380` (frame 10)
- pcap parent response: `19:16:43.788` (frame 11)
- pcap child id request: `19:16:44.129` (frame 13)
- pcap child id response: `19:16:44.192` (frame 15)

#### Attach sequence 2

- parent request: `19:20:43.863`
- parent response: `19:20:43.943`
- child id request: `19:20:44.574`
- child id response: `19:20:44.668`
- parent ipv6: `fe80:0:0:0:2424:57ad:92a7:78e3`
- parent extaddr: `262457ad92a778e3`
- parent rloc16: `0x5400`
- timing source: **pcap**
- Request → Response: **82 ms**
- Response → Child ID Request: **669 ms**
- Child ID Request → Response: **65 ms**
- Full Attach: **816 ms**
- pcap parent request: `19:20:43.848` (frame 185)
- pcap parent response: `19:20:43.930` (frame 186)
- pcap child id request: `19:20:44.599` (frame 188)
- pcap child id response: `19:20:44.664` (frame 190)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 199: 16, seq 200: 16, seq 201: 16, seq 202: 16
- failed tx by dst: `521e57ae1dc7a59b`: 58

### `stock_child_20260609-192129-run13.log`

#### Attach sequence 1

- parent request: `19:22:09.452`
- parent response: `19:22:09.642`
- child id request: `19:22:10.160`
- child id response: `19:22:10.250`
- parent ipv6: `fe80:0:0:0:ca4:8bd4:772:3233`
- parent extaddr: `0ea48bd407723233`
- parent rloc16: `0x4000`
- timing source: **pcap**
- Request → Response: **196 ms**
- Response → Child ID Request: **554 ms**
- Child ID Request → Response: **62 ms**
- Full Attach: **812 ms**
- pcap parent request: `19:22:09.424` (frame 9)
- pcap parent response: `19:22:09.620` (frame 11)
- pcap child id request: `19:22:10.174` (frame 13)
- pcap child id response: `19:22:10.236` (frame 15)

#### Attach sequence 2

- parent request: `19:26:10.246`
- parent response: `19:26:10.485`
- child id request: `19:26:11.000`
- child id response: `19:26:11.046`
- parent ipv6: `fe80:0:0:0:401e:a1ed:7b76:fe0f`
- parent extaddr: `421ea1ed7b76fe0f`
- parent rloc16: `0xd000`
- timing source: **pcap**
- Request → Response: **243 ms**
- Response → Child ID Request: **508 ms**
- Child ID Request → Response: **64 ms**
- Full Attach: **815 ms**
- pcap parent request: `19:26:10.227` (frame 187)
- pcap parent response: `19:26:10.470` (frame 188)
- pcap child id request: `19:26:10.978` (frame 190)
- pcap child id response: `19:26:11.042` (frame 192)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 247: 16, seq 248: 16, seq 249: 16, seq 250: 16
- failed tx by dst: `0ea48bd407723233`: 51

### `stock_child_20260609-192655-run14.log`

#### Attach sequence 1

- parent request: `19:27:34.999`
- parent response: `19:27:35.322`
- child id request: `19:27:35.772`
- child id response: `19:27:35.864`
- parent ipv6: `fe80:0:0:0:d826:2d78:7714:6ba1`
- parent extaddr: `da262d7877146ba1`
- parent rloc16: `0x3800`
- timing source: **pcap**
- Request → Response: **262 ms**
- Response → Child ID Request: **486 ms**
- Child ID Request → Response: **66 ms**
- Full Attach: **814 ms**
- pcap parent request: `19:27:35.035` (frame 10)
- pcap parent response: `19:27:35.297` (frame 11)
- pcap child id request: `19:27:35.783` (frame 13)
- pcap child id response: `19:27:35.849` (frame 15)

#### Attach sequence 2

- parent request: `19:31:35.728`
- parent response: `19:31:35.834`
- child id request: `19:31:36.439`
- child id response: `19:31:36.528`
- parent ipv6: `fe80:0:0:0:1819:7094:2fc8:8d1`
- parent extaddr: `1a1970942fc808d1`
- parent rloc16: `0x4c00`
- timing source: **pcap**
- Request → Response: **109 ms**
- Response → Child ID Request: **641 ms**
- Child ID Request → Response: **63 ms**
- Full Attach: **813 ms**
- pcap parent request: `19:31:35.709` (frame 185)
- pcap parent response: `19:31:35.818` (frame 186)
- pcap child id request: `19:31:36.459` (frame 189)
- pcap child id response: `19:31:36.522` (frame 191)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 249: 16, seq 250: 16, seq 251: 16, seq 252: 16
- failed tx by dst: `da262d7877146ba1`: 49
