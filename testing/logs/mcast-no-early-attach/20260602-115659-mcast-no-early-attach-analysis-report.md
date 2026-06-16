# Child Log Analysis

## mcast_no_early_attach_child

Files analyzed: **1**

### Summary

| Attach | Metric | M (SD), ms | n |
| --- | --- | ---: | ---: |
| 1 | Request → Response | 426.00 (0.00) | 1 |
| 1 | Response → Child ID Request | 325.00 (0.00) | 1 |
| 1 | Child ID Request → Response | 66.00 (0.00) | 1 |
| 1 | Full Attach | 817.00 (0.00) | 1 |
| 2 | Request → Response | n/a | 0 |
| 2 | Response → Child ID Request | n/a | 0 |
| 2 | Child ID Request → Response | n/a | 0 |
| 2 | Full Attach | n/a | 0 |
| 3 | Request → Response | 221.00 (0.00) | 1 |
| 3 | Response → Child ID Request | 4011.00 (0.00) | 1 |
| 3 | Child ID Request → Response | 62.00 (0.00) | 1 |
| 3 | Full Attach | 4294.00 (0.00) | 1 |

| Metric | M (SD) | n |
| --- | ---: | ---: |
| Failed TX Attempts per Log | 0.00 (0.00) | 1 |

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
