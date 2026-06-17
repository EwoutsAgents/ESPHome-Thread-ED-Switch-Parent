# Child Log Analysis

## mcast_no_early_attach_child

Files analyzed: **5**

### Summary

| Attach | Metric | M (SD), ms | n |
| --- | --- | ---: | ---: |
| 1 | Request → Response | 356.80 (113.58) | 5 |
| 1 | Response → Child ID Request | 384.80 (114.12) | 5 |
| 1 | Child ID Request → Response | 63.40 (1.14) | 5 |
| 1 | Full Attach | 805.00 (14.71) | 5 |
| 2 | Request → Response | 157.20 (51.83) | 5 |
| 2 | Response → Child ID Request | 2197.80 (1850.59) | 5 |
| 2 | Child ID Request → Response | 61.80 (1.30) | 5 |
| 2 | Full Attach | 2416.80 (1815.31) | 5 |

| Metric | M (SD) | n |
| --- | ---: | ---: |
| Failed TX Attempts per Log | 0.00 (0.00) | 5 |

### `mcast_no_early_attach_child_20260617-172951.log`

#### Attach sequence 1

- log parent request: `17:30:59.611`
- log parent response: `17:30:59.988`
- log child id request: `17:31:00.383`
- log child id response: `17:31:00.472`
- parent ipv6: `fe80:0:0:0:f867:f8bb:6aa1:c587`
- parent extaddr: `fa67f8bb6aa1c587`
- parent rloc16: `0x8400`
- timing source: **pcap**
- Request → Response: **314 ms**
- Response → Child ID Request: **430 ms**
- Child ID Request → Response: **64 ms**
- Full Attach: **808 ms**
- pcap parent request: `17:30:59.651` (frame 9)
- pcap parent response: `17:30:59.965` (frame 10)
- pcap child id request: `17:31:00.395` (frame 13)
- pcap child id response: `17:31:00.459` (frame 15)

#### Attach sequence 2

- log parent request: `17:32:57.860`
- log parent response: `17:32:58.049`
- log child id request: `17:32:59.507`
- log child id response: `17:32:59.601`
- parent ipv6: `fe80:0:0:0:8c3c:e1a3:ea7c:fa15`
- parent extaddr: `8e3ce1a3ea7cfa15`
- parent rloc16: `0xbc00`
- timing source: **pcap**
- Request → Response: **191 ms**
- Response → Child ID Request: **1499 ms**
- Child ID Request → Response: **61 ms**
- Full Attach: **1751 ms**
- pcap parent request: `17:32:57.838` (frame 49)
- pcap parent response: `17:32:58.029` (frame 50)
- pcap child id request: `17:32:59.528` (frame 55)
- pcap child id response: `17:32:59.589` (frame 57)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_no_early_attach_child_20260617-173553.log`

#### Attach sequence 1

- log parent request: `17:37:02.510`
- log parent response: `17:37:02.934`
- log child id request: `17:37:03.219`
- log child id response: `17:37:03.307`
- parent ipv6: `fe80:0:0:0:68d1:9179:fbea:1118`
- parent extaddr: `6ad19179fbea1118`
- parent rloc16: `0xe400`
- timing source: **pcap**
- Request → Response: **430 ms**
- Response → Child ID Request: **321 ms**
- Child ID Request → Response: **62 ms**
- Full Attach: **813 ms**
- pcap parent request: `17:37:02.481` (frame 10)
- pcap parent response: `17:37:02.911` (frame 11)
- pcap child id request: `17:37:03.232` (frame 13)
- pcap child id response: `17:37:03.294` (frame 15)

#### Attach sequence 2

- log parent request: `17:39:00.198`
- log parent response: `17:39:00.301`
- log child id request: `17:39:01.782`
- log child id response: `17:39:01.882`
- parent ipv6: `fe80:0:0:0:2430:e4de:cd86:c5a6`
- parent extaddr: `2630e4decd86c5a6`
- parent rloc16: `0xd800`
- timing source: **pcap**
- Request → Response: **105 ms**
- Response → Child ID Request: **1526 ms**
- Child ID Request → Response: **64 ms**
- Full Attach: **1695 ms**
- pcap parent request: `17:39:00.177` (frame 49)
- pcap parent response: `17:39:00.282` (frame 50)
- pcap child id request: `17:39:01.808` (frame 55)
- pcap child id response: `17:39:01.872` (frame 57)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_no_early_attach_child_20260617-174156.log`

#### Attach sequence 1

- log parent request: `17:43:04.642`
- log parent response: `17:43:05.135`
- log child id request: `17:43:05.352`
- log child id response: `17:43:05.440`
- parent ipv6: `fe80:0:0:0:cc87:8cc8:ca6e:179d`
- parent extaddr: `ce878cc8ca6e179d`
- parent rloc16: `0x9c00`
- timing source: **pcap**
- Request → Response: **495 ms**
- Response → Child ID Request: **253 ms**
- Child ID Request → Response: **63 ms**
- Full Attach: **811 ms**
- pcap parent request: `17:43:04.617` (frame 10)
- pcap parent response: `17:43:05.112` (frame 11)
- pcap child id request: `17:43:05.365` (frame 13)
- pcap child id response: `17:43:05.428` (frame 15)

#### Attach sequence 2

- log parent request: `17:45:04.307`
- log parent response: `17:45:04.413`
- log child id request: `17:45:04.574`
- log child id response: `17:45:04.667`
- parent ipv6: `fe80:0:0:0:3818:2113:dbbc:4719`
- parent extaddr: `3a182113dbbc4719`
- parent rloc16: `0x1800`
- timing source: **pcap**
- Request → Response: **227 ms**
- Response → Child ID Request: **85 ms**
- Child ID Request → Response: **61 ms**
- Full Attach: **373 ms**
- pcap parent request: `17:45:04.284` (frame 54)
- pcap parent response: `17:45:04.511` (frame 57)
- pcap child id request: `17:45:04.596` (frame 59)
- pcap child id response: `17:45:04.657` (frame 61)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_no_early_attach_child_20260617-174758.log`

#### Attach sequence 1

- log parent request: `17:49:06.336`
- log parent response: `17:49:06.777`
- log child id request: `17:49:07.153`
- log child id response: `17:49:07.200`
- parent ipv6: `fe80:0:0:0:d8e1:ccc:cbd4:2747`
- parent extaddr: `dae10ccccbd42747`
- parent rloc16: `0x0800`
- timing source: **pcap**
- Request → Response: **347 ms**
- Response → Child ID Request: **367 ms**
- Child ID Request → Response: **65 ms**
- Full Attach: **779 ms**
- pcap parent request: `17:49:06.408` (frame 9)
- pcap parent response: `17:49:06.755` (frame 10)
- pcap child id request: `17:49:07.122` (frame 13)
- pcap child id response: `17:49:07.187` (frame 15)

#### Attach sequence 2

- log parent request: `17:51:01.179`
- log parent response: `17:51:01.289`
- log child id request: `17:51:06.244`
- log child id response: `17:51:06.338`
- parent ipv6: `fe80:0:0:0:7474:5980:c3fa:a2b0`
- parent extaddr: `76745980c3faa2b0`
- parent rloc16: `0xbc00`
- timing source: **pcap**
- Request → Response: **113 ms**
- Response → Child ID Request: **4995 ms**
- Child ID Request → Response: **62 ms**
- Full Attach: **5170 ms**
- pcap parent request: `17:51:01.158` (frame 51)
- pcap parent response: `17:51:01.271` (frame 52)
- pcap child id request: `17:51:06.266` (frame 57)
- pcap child id response: `17:51:06.328` (frame 59)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_no_early_attach_child_20260617-175400.log`

#### Attach sequence 1

- log parent request: `17:55:08.995`
- log parent response: `17:55:09.249`
- log child id request: `17:55:09.766`
- log child id response: `17:55:09.854`
- parent ipv6: `fe80:0:0:0:6876:bce9:7799:d3c3`
- parent extaddr: `6a76bce97799d3c3`
- parent rloc16: `0xe000`
- timing source: **pcap**
- Request → Response: **198 ms**
- Response → Child ID Request: **553 ms**
- Child ID Request → Response: **63 ms**
- Full Attach: **814 ms**
- pcap parent request: `17:55:09.029` (frame 10)
- pcap parent response: `17:55:09.227` (frame 11)
- pcap child id request: `17:55:09.780` (frame 13)
- pcap child id response: `17:55:09.843` (frame 15)

#### Attach sequence 2

- log parent request: `17:57:05.553`
- log parent response: `17:57:05.700`
- log child id request: `17:57:08.546`
- log child id response: `17:57:08.640`
- parent ipv6: `fe80:0:0:0:346e:36fa:80eb:ef05`
- parent extaddr: `366e36fa80ebef05`
- parent rloc16: `0x1c00`
- timing source: **pcap**
- Request → Response: **150 ms**
- Response → Child ID Request: **2884 ms**
- Child ID Request → Response: **61 ms**
- Full Attach: **3095 ms**
- pcap parent request: `17:57:05.533` (frame 50)
- pcap parent response: `17:57:05.683` (frame 51)
- pcap child id request: `17:57:08.567` (frame 56)
- pcap child id response: `17:57:08.628` (frame 58)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**
