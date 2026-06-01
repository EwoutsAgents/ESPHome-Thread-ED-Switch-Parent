# Child Log Analysis

## stock_child

### Summary

| Attach | Request → Response (ms) | Response → Child ID Req (ms) | Child ID Req → Response (ms) | Full attach (ms) | n |
| --- | ---: | ---: | ---: | ---: | ---: |
| 1 | 255.60 ± 186.20 | 495.40 ± 187.06 | 14.00 ± 0.71 | 765.00 ± 2.55 | 5 |
| 2 | 238.00 ± 152.50 | 511.20 ± 152.37 | 13.40 ± 0.55 | 762.60 ± 0.89 | 5 |

| Failed TX attempts per log | n |
| ---: | ---: |
| 64.00 ± 0.00 | 5 |

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
- request -> response: **419 ms**
- response -> child id request: **332 ms**
- child id request -> response: **14 ms**
- full attach: **765 ms**
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
- request -> response: **66 ms**
- response -> child id request: **683 ms**
- child id request -> response: **13 ms**
- full attach: **762 ms**
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
- request -> response: **319 ms**
- response -> child id request: **433 ms**
- child id request -> response: **15 ms**
- full attach: **767 ms**
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
- request -> response: **92 ms**
- response -> child id request: **657 ms**
- child id request -> response: **13 ms**
- full attach: **762 ms**
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
- request -> response: **25 ms**
- response -> child id request: **729 ms**
- child id request -> response: **14 ms**
- full attach: **768 ms**
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
- request -> response: **297 ms**
- response -> child id request: **452 ms**
- child id request -> response: **14 ms**
- full attach: **763 ms**
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
- request -> response: **423 ms**
- response -> child id request: **326 ms**
- child id request -> response: **13 ms**
- full attach: **762 ms**
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
- request -> response: **317 ms**
- response -> child id request: **433 ms**
- child id request -> response: **14 ms**
- full attach: **764 ms**
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
- request -> response: **92 ms**
- response -> child id request: **657 ms**
- child id request -> response: **14 ms**
- full attach: **763 ms**
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
- request -> response: **418 ms**
- response -> child id request: **331 ms**
- child id request -> response: **13 ms**
- full attach: **762 ms**
- pcap parent request: `12:40:16.820` (frame 189)
- pcap parent response: `12:40:17.238` (frame 190)
- pcap child id request: `12:40:17.569` (frame 192)
- pcap child id response: `12:40:17.582` (frame 194)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 220: 16, seq 221: 16, seq 222: 16, seq 223: 16
- failed tx by dst: `a605ee962ad7a308`: 48
