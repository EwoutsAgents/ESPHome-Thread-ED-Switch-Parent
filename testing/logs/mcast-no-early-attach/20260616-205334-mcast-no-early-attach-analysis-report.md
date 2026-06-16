# Child Log Analysis

## mcast_no_early_attach_child

Files analyzed: **5**

### Summary

| Attach | Metric | M (SD), ms | n |
| --- | --- | ---: | ---: |
| 1 | Request → Response | 344.80 (117.80) | 5 |
| 1 | Response → Child ID Request | 397.40 (128.38) | 5 |
| 1 | Child ID Request → Response | 63.80 (0.84) | 5 |
| 1 | Full Attach | 806.00 (15.68) | 5 |
| 2 | Request → Response | 102.00 (11.31) | 2 |
| 2 | Response → Child ID Request | 3228.50 (443.36) | 2 |
| 2 | Child ID Request → Response | 62.00 (1.41) | 2 |
| 2 | Full Attach | 3392.50 (456.08) | 2 |

| Metric | M (SD) | n |
| --- | ---: | ---: |
| Failed TX Attempts per Log | 0.00 (0.00) | 5 |

### `mcast_no_early_attach_child_20260616-201136.log`

#### Attach sequence 1

- log parent request: `20:13:02.141`
- log parent response: `20:13:02.590`
- log child id request: `20:13:02.852`
- log child id response: `20:13:02.941`
- parent ipv6: `fe80:0:0:0:44bf:3f53:b132:6ef7`
- parent extaddr: `46bf3f53b1326ef7`
- parent rloc16: `0xdc00`
- timing source: **pcap**
- Request → Response: **450 ms**
- Response → Child ID Request: **298 ms**
- Child ID Request → Response: **64 ms**
- Full Attach: **812 ms**
- pcap parent request: `20:13:02.119` (frame 9)
- pcap parent response: `20:13:02.569` (frame 10)
- pcap child id request: `20:13:02.867` (frame 13)
- pcap child id response: `20:13:02.931` (frame 15)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_no_early_attach_child_20260616-201747.log`

#### Attach sequence 1

- log parent request: `20:19:08.511`
- log parent response: `20:19:09.084`
- log child id request: `20:19:09.329`
- log child id response: `20:19:09.373`
- parent ipv6: `fe80:0:0:0:88c9:465a:6b6b:a9da`
- parent extaddr: `8ac9465a6b6ba9da`
- parent rloc16: `0xc800`
- timing source: **pcap**
- Request → Response: **479 ms**
- Response → Child ID Request: **236 ms**
- Child ID Request → Response: **63 ms**
- Full Attach: **778 ms**
- pcap parent request: `20:19:08.584` (frame 9)
- pcap parent response: `20:19:09.063` (frame 11)
- pcap child id request: `20:19:09.299` (frame 13)
- pcap child id response: `20:19:09.362` (frame 15)

#### Attach sequence 2

- log parent request: `20:20:57.458`
- log parent response: `20:20:57.551`
- log child id request: `20:21:00.426`
- log child id response: `20:21:00.521`
- parent ipv6: `fe80:0:0:0:308f:a8df:3c9c:278b`
- parent extaddr: `328fa8df3c9c278b`
- parent rloc16: `0x0000`
- timing source: **pcap**
- Request → Response: **94 ms**
- Response → Child ID Request: **2915 ms**
- Child ID Request → Response: **61 ms**
- Full Attach: **3070 ms**
- pcap parent request: `20:20:57.439` (frame 46)
- pcap parent response: `20:20:57.533` (frame 47)
- pcap child id request: `20:21:00.448` (frame 51)
- pcap child id response: `20:21:00.509` (frame 53)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_no_early_attach_child_20260616-202354.log`

#### Attach sequence 1

- log parent request: `20:25:03.219`
- log parent response: `20:25:03.480`
- log child id request: `20:25:03.989`
- log child id response: `20:25:04.078`
- parent ipv6: `fe80:0:0:0:2c5b:9e48:dd5f:9d9f`
- parent extaddr: `2e5b9e48dd5f9d9f`
- parent rloc16: `0x4c00`
- timing source: **pcap**
- Request → Response: **205 ms**
- Response → Child ID Request: **544 ms**
- Child ID Request → Response: **65 ms**
- Full Attach: **814 ms**
- pcap parent request: `20:25:03.253` (frame 10)
- pcap parent response: `20:25:03.458` (frame 11)
- pcap child id request: `20:25:04.002` (frame 13)
- pcap child id response: `20:25:04.067` (frame 15)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_no_early_attach_child_20260616-202949.log`

#### Attach sequence 1

- log parent request: `20:30:57.605`
- log parent response: `20:30:57.867`
- log child id request: `20:30:58.316`
- log child id response: `20:30:58.406`
- parent ipv6: `fe80:0:0:0:9cba:6e35:baf:8b77`
- parent extaddr: `9eba6e350baf8b77`
- parent rloc16: `0x8c00`
- timing source: **pcap**
- Request → Response: **264 ms**
- Response → Child ID Request: **486 ms**
- Child ID Request → Response: **64 ms**
- Full Attach: **814 ms**
- pcap parent request: `20:30:57.579` (frame 10)
- pcap parent response: `20:30:57.843` (frame 11)
- pcap child id request: `20:30:58.329` (frame 13)
- pcap child id response: `20:30:58.393` (frame 15)

#### Attach sequence 2

- log parent request: `20:32:48.271`
- log parent response: `20:32:48.592`
- log child id request: `None`
- log child id response: `None`
- parent ipv6: `fe80:0:0:0:9cba:6e35:baf:8b77`
- parent extaddr: `9eba6e350baf8b77`
- parent rloc16: `0x8c00`
- timing source: **unavailable**
- Request → Response: **None ms**
- Response → Child ID Request: **None ms**
- Child ID Request → Response: **None ms**
- Full Attach: **None ms**

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_no_early_attach_child_20260616-203543.log`

#### Attach sequence 1

- log parent request: `20:36:51.107`
- log parent response: `20:36:51.431`
- log child id request: `20:36:51.817`
- log child id response: `20:36:51.904`
- parent ipv6: `fe80:0:0:0:60d5:a9d2:177:c930`
- parent extaddr: `62d5a9d20177c930`
- parent rloc16: `0xdc00`
- timing source: **pcap**
- Request → Response: **326 ms**
- Response → Child ID Request: **423 ms**
- Child ID Request → Response: **63 ms**
- Full Attach: **812 ms**
- pcap parent request: `20:36:51.079` (frame 10)
- pcap parent response: `20:36:51.405` (frame 11)
- pcap child id request: `20:36:51.828` (frame 13)
- pcap child id response: `20:36:51.891` (frame 15)

#### Attach sequence 2

- log parent request: `20:38:39.059`
- log parent response: `20:38:39.167`
- log child id request: `20:38:42.664`
- log child id response: `20:38:42.763`
- parent ipv6: `fe80:0:0:0:f4af:1995:5423:f0d7`
- parent extaddr: `f6af19955423f0d7`
- parent rloc16: `0x0400`
- timing source: **pcap**
- Request → Response: **110 ms**
- Response → Child ID Request: **3542 ms**
- Child ID Request → Response: **63 ms**
- Full Attach: **3715 ms**
- pcap parent request: `20:38:39.036` (frame 50)
- pcap parent response: `20:38:39.146` (frame 51)
- pcap child id request: `20:38:42.688` (frame 56)
- pcap child id response: `20:38:42.751` (frame 58)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**
