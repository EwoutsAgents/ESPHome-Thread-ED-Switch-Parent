# Child Log Analysis

## mcast_no_early_attach_child

Files analyzed: **6**

### Summary

| Attach | Metric | M (SD), ms | n |
| --- | --- | ---: | ---: |
| 1 | Request → Response | 308.80 (179.29) | 5 |
| 1 | Response → Child ID Request | 425.80 (172.65) | 5 |
| 1 | Child ID Request → Response | 53.80 (22.84) | 5 |
| 1 | Full Attach | 788.40 (38.06) | 5 |
| 2 | Request → Response | 89.00 (0.00) | 1 |
| 2 | Response → Child ID Request | 627.00 (0.00) | 1 |
| 2 | Child ID Request → Response | 13.00 (0.00) | 1 |
| 2 | Full Attach | 729.00 (0.00) | 1 |
| 3 | Request → Response | 221.00 (0.00) | 1 |
| 3 | Response → Child ID Request | 4011.00 (0.00) | 1 |
| 3 | Child ID Request → Response | 62.00 (0.00) | 1 |
| 3 | Full Attach | 4294.00 (0.00) | 1 |
| 4 | Request → Response | n/a | 0 |
| 4 | Response → Child ID Request | n/a | 0 |
| 4 | Child ID Request → Response | n/a | 0 |
| 4 | Full Attach | n/a | 0 |

| Metric | M (SD) | n |
| --- | ---: | ---: |
| Failed TX Attempts per Log | 0.00 (0.00) | 6 |

### `mcast_no_early_attach_child_20260601-231334.log`

#### Attach sequence 1

- log parent request: `23:15:34.733`
- log parent response: `23:15:34.875`
- log child id request: `None`
- log child id response: `23:15:35.588`
- parent ipv6: `fe80:0:0:0:9847:e225:f44c:1b21`
- parent extaddr: `9a47e225f44c1b21`
- parent rloc16: `0x7800`
- timing source: **pcap**
- Request → Response: **21 ms**
- Response → Child ID Request: **693 ms**
- Child ID Request → Response: **13 ms**
- Full Attach: **727 ms**
- pcap parent request: `23:15:34.804` (frame 10)
- pcap parent response: `23:15:34.825` (frame 11)
- pcap child id request: `23:15:35.518` (frame 13)
- pcap child id response: `23:15:35.531` (frame 15)

#### Attach sequence 2

- log parent request: `23:16:09.215`
- log parent response: `23:16:09.405`
- log child id request: `None`
- log child id response: `23:16:10.074`
- parent ipv6: `fe80:0:0:0:28f7:8df3:5d30:a137`
- parent extaddr: `2af78df35d30a137`
- parent rloc16: `0xc800`
- timing source: **pcap**
- Request → Response: **89 ms**
- Response → Child ID Request: **627 ms**
- Child ID Request → Response: **13 ms**
- Full Attach: **729 ms**
- pcap parent request: `23:16:09.292` (frame 44)
- pcap parent response: `23:16:09.381` (frame 46)
- pcap child id request: `23:16:10.008` (frame 48)
- pcap child id response: `23:16:10.021` (frame 50)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_no_early_attach_child_20260602-103849.log`

#### Attach sequence 1

- log parent request: `10:39:53.114`
- log parent response: `10:39:53.513`
- log child id request: `10:39:53.886`
- log child id response: `10:39:53.977`
- parent ipv6: `fe80:0:0:0:cc4b:add2:ad3f:98c0`
- parent extaddr: `ce4badd2ad3f98c0`
- parent rloc16: `0x0800`
- timing source: **unavailable**
- Request → Response: **None ms**
- Response → Child ID Request: **None ms**
- Child ID Request → Response: **None ms**
- Full Attach: **None ms**

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_no_early_attach_child_20260602-105332.log`

#### Attach sequence 1

- log parent request: `10:54:34.801`
- log parent response: `10:54:35.355`
- log child id request: `10:54:35.621`
- log child id response: `10:54:35.665`
- parent ipv6: `fe80:0:0:0:8c9c:e462:3c3e:d571`
- parent extaddr: `8e9ce4623c3ed571`
- parent rloc16: `0x8c00`
- timing source: **pcap**
- Request → Response: **457 ms**
- Response → Child ID Request: **256 ms**
- Child ID Request → Response: **63 ms**
- Full Attach: **776 ms**
- pcap parent request: `10:54:34.872` (frame 9)
- pcap parent response: `10:54:35.329` (frame 10)
- pcap child id request: `10:54:35.585` (frame 13)
- pcap child id response: `10:54:35.648` (frame 15)

#### Attach sequence 2

- log parent request: `10:55:10.786`
- log parent response: `10:55:11.271`
- log child id request: `None`
- log child id response: `None`
- parent ipv6: `fe80:0:0:0:8c9c:e462:3c3e:d571`
- parent extaddr: `None`
- parent rloc16: `0x8c00`
- timing source: **unavailable**
- Request → Response: **None ms**
- Response → Child ID Request: **None ms**
- Child ID Request → Response: **None ms**
- Full Attach: **None ms**

#### Attach sequence 3

- log parent request: `10:55:20.065`
- log parent response: `10:55:20.162`
- log child id request: `None`
- log child id response: `None`
- parent ipv6: `fe80:0:0:0:8c9c:e462:3c3e:d571`
- parent extaddr: `8e9ce4623c3ed571`
- parent rloc16: `0x8c00`
- timing source: **unavailable**
- Request → Response: **None ms**
- Response → Child ID Request: **None ms**
- Child ID Request → Response: **None ms**
- Full Attach: **None ms**

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_no_early_attach_child_20260602-111617.log`

#### Attach sequence 1

- log parent request: `11:17:20.104`
- log parent response: `11:17:20.552`
- log child id request: `11:17:20.876`
- log child id response: `11:17:20.966`
- parent ipv6: `fe80:0:0:0:d401:4987:4917:2421`
- parent extaddr: `d601498749172421`
- parent rloc16: `0xc800`
- timing source: **pcap**
- Request → Response: **390 ms**
- Response → Child ID Request: **361 ms**
- Child ID Request → Response: **64 ms**
- Full Attach: **815 ms**
- pcap parent request: `11:17:20.135` (frame 9)
- pcap parent response: `11:17:20.525` (frame 11)
- pcap child id request: `11:17:20.886` (frame 13)
- pcap child id response: `11:17:20.950` (frame 15)

#### Attach sequence 2

- log parent request: `11:18:07.576`
- log parent response: `11:18:07.651`
- log child id request: `None`
- log child id response: `None`
- parent ipv6: `fe80:0:0:0:d401:4987:4917:2421`
- parent extaddr: `None`
- parent rloc16: `0xc800`
- timing source: **unavailable**
- Request → Response: **None ms**
- Response → Child ID Request: **None ms**
- Child ID Request → Response: **None ms**
- Full Attach: **None ms**

#### Attach sequence 3

- log parent request: `11:18:16.257`
- log parent response: `11:18:16.620`
- log child id request: `None`
- log child id response: `None`
- parent ipv6: `fe80:0:0:0:d401:4987:4917:2421`
- parent extaddr: `None`
- parent rloc16: `0xc800`
- timing source: **unavailable**
- Request → Response: **None ms**
- Response → Child ID Request: **None ms**
- Child ID Request → Response: **None ms**
- Full Attach: **None ms**

#### Attach sequence 4

- log parent request: `11:18:30.852`
- log parent response: `11:18:31.121`
- log child id request: `None`
- log child id response: `None`
- parent ipv6: `fe80:0:0:0:d4e2:6d6:5057:d5a9`
- parent extaddr: `d6e206d65057d5a9`
- parent rloc16: `0xf000`
- timing source: **unavailable**
- Request → Response: **None ms**
- Response → Child ID Request: **None ms**
- Child ID Request → Response: **None ms**
- Full Attach: **None ms**

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_no_early_attach_child_20260602-112623.log`

#### Attach sequence 1

- log parent request: `11:27:26.088`
- log parent response: `11:27:26.402`
- log child id request: `11:27:26.860`
- log child id response: `11:27:26.949`
- parent ipv6: `fe80:0:0:0:68ad:5be:ac1e:7809`
- parent extaddr: `6aad05beac1e7809`
- parent rloc16: `0x0000`
- timing source: **pcap**
- Request → Response: **250 ms**
- Response → Child ID Request: **494 ms**
- Child ID Request → Response: **63 ms**
- Full Attach: **807 ms**
- pcap parent request: `11:27:26.127` (frame 9)
- pcap parent response: `11:27:26.377` (frame 10)
- pcap child id request: `11:27:26.871` (frame 13)
- pcap child id response: `11:27:26.934` (frame 15)

#### Attach sequence 2

- log parent request: `11:28:47.863`
- log parent response: `11:28:48.010`
- log child id request: `None`
- log child id response: `None`
- parent ipv6: `fe80:0:0:0:68ad:5be:ac1e:7809`
- parent extaddr: `None`
- parent rloc16: `0x0000`
- timing source: **unavailable**
- Request → Response: **None ms**
- Response → Child ID Request: **None ms**
- Child ID Request → Response: **None ms**
- Full Attach: **None ms**

#### Attach sequence 3

- log parent request: `11:28:58.146`
- log parent response: `11:28:58.187`
- log child id request: `None`
- log child id response: `None`
- parent ipv6: `fe80:0:0:0:68ad:5be:ac1e:7809`
- parent extaddr: `6aad05beac1e7809`
- parent rloc16: `0x0000`
- timing source: **unavailable**
- Request → Response: **None ms**
- Response → Child ID Request: **None ms**
- Child ID Request → Response: **None ms**
- Full Attach: **None ms**

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_no_early_attach_child_20260602-115659.log`

#### Attach sequence 1

- log parent request: `11:58:02.493`
- log parent response: `11:58:02.916`
- log child id request: `11:58:03.205`
- log child id response: `11:58:03.296`
- parent ipv6: `fe80:0:0:0:4c9d:ec7f:e693:4b8e`
- parent extaddr: `4e9dec7fe6934b8e`
- parent rloc16: `0xc400`
- timing source: **pcap**
- Request → Response: **426 ms**
- Response → Child ID Request: **325 ms**
- Child ID Request → Response: **66 ms**
- Full Attach: **817 ms**
- pcap parent request: `11:58:02.466` (frame 9)
- pcap parent response: `11:58:02.892` (frame 11)
- pcap child id request: `11:58:03.217` (frame 13)
- pcap child id response: `11:58:03.283` (frame 15)

#### Attach sequence 2

- log parent request: `11:59:52.375`
- log parent response: `11:59:52.592`
- log child id request: `None`
- log child id response: `None`
- parent ipv6: `fe80:0:0:0:d86d:795b:b705:f409`
- parent extaddr: `None`
- parent rloc16: `0x4000`
- timing source: **unavailable**
- Request → Response: **None ms**
- Response → Child ID Request: **None ms**
- Child ID Request → Response: **None ms**
- Full Attach: **None ms**

#### Attach sequence 3

- log parent request: `11:59:55.787`
- log parent response: `11:59:55.964`
- log child id request: `11:59:56.612`
- log child id response: `11:59:56.655`
- parent ipv6: `fe80:0:0:0:d86d:795b:b705:f409`
- parent extaddr: `da6d795bb705f409`
- parent rloc16: `0x4000`
- timing source: **pcap**
- Request → Response: **221 ms**
- Response → Child ID Request: **4011 ms**
- Child ID Request → Response: **62 ms**
- Full Attach: **4294 ms**
- pcap parent request: `11:59:52.352` (frame 47)
- pcap parent response: `11:59:52.573` (frame 50)
- pcap child id request: `11:59:56.584` (frame 57)
- pcap child id response: `11:59:56.646` (frame 59)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**
