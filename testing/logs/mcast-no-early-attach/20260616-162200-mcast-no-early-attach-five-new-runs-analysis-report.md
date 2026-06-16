# Child Log Analysis

## mcast_no_early_attach_child

Files analyzed: **5**

### Summary

| Attach | Metric | M (SD), ms | n |
| --- | --- | ---: | ---: |
| 1 | Request → Response | 392.20 (124.75) | 5 |
| 1 | Response → Child ID Request | 355.40 (124.17) | 5 |
| 1 | Child ID Request → Response | 63.60 (1.14) | 5 |
| 1 | Full Attach | 811.20 (2.17) | 5 |
| 2 | Request → Response | 139.00 (0.00) | 1 |
| 2 | Response → Child ID Request | 575.00 (0.00) | 1 |
| 2 | Child ID Request → Response | 64.00 (0.00) | 1 |
| 2 | Full Attach | 778.00 (0.00) | 1 |
| 3 | Request → Response | 465.00 (0.00) | 1 |
| 3 | Response → Child ID Request | 250.00 (0.00) | 1 |
| 3 | Child ID Request → Response | 62.00 (0.00) | 1 |
| 3 | Full Attach | 777.00 (0.00) | 1 |

| Metric | M (SD) | n |
| --- | ---: | ---: |
| Failed TX Attempts per Log | 0.00 (0.00) | 5 |

### `mcast_no_early_attach_child_20260616-155048.log`

#### Attach sequence 1

- log parent request: `15:51:27.965`
- log parent response: `15:51:28.369`
- log child id request: `15:51:28.738`
- log child id response: `15:51:28.828`
- parent ipv6: `fe80:0:0:0:50e6:88fa:7cd:23fa`
- parent extaddr: `52e688fa07cd23fa`
- parent rloc16: `0xb000`
- timing source: **pcap**
- Request → Response: **338 ms**
- Response → Child ID Request: **406 ms**
- Child ID Request → Response: **65 ms**
- Full Attach: **809 ms**
- pcap parent request: `15:51:28.007` (frame 9)
- pcap parent response: `15:51:28.345` (frame 10)
- pcap child id request: `15:51:28.751` (frame 13)
- pcap child id response: `15:51:28.816` (frame 15)

#### Attach sequence 2

- log parent request: `15:53:19.491`
- log parent response: `15:53:19.792`
- log child id request: `15:53:19.866`
- log child id response: `15:53:19.964`
- parent ipv6: `fe80:0:0:0:50e6:88fa:7cd:23fa`
- parent extaddr: `52e688fa07cd23fa`
- parent rloc16: `0xb000`
- timing source: **unavailable**
- Request → Response: **None ms**
- Response → Child ID Request: **None ms**
- Child ID Request → Response: **None ms**
- Full Attach: **None ms**

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_no_early_attach_child_20260616-155614.log`

#### Attach sequence 1

- log parent request: `15:56:54.440`
- log parent response: `15:56:55.016`
- log child id request: `15:56:55.211`
- log child id response: `15:56:55.299`
- parent ipv6: `fe80:0:0:0:a496:e4ee:10c3:91a9`
- parent extaddr: `a696e4ee10c391a9`
- parent rloc16: `0x2400`
- timing source: **pcap**
- Request → Response: **518 ms**
- Response → Child ID Request: **232 ms**
- Child ID Request → Response: **62 ms**
- Full Attach: **812 ms**
- pcap parent request: `15:56:54.474` (frame 10)
- pcap parent response: `15:56:54.992` (frame 11)
- pcap child id request: `15:56:55.224` (frame 13)
- pcap child id response: `15:56:55.286` (frame 15)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_no_early_attach_child_20260616-160140.log`

#### Attach sequence 1

- log parent request: `16:02:20.175`
- log parent response: `16:02:20.681`
- log child id request: `16:02:20.882`
- log child id response: `16:02:20.970`
- parent ipv6: `fe80:0:0:0:58c4:e21a:943d:a0e1`
- parent extaddr: `5ac4e21a943da0e1`
- parent rloc16: `0x3000`
- timing source: **pcap**
- Request → Response: **511 ms**
- Response → Child ID Request: **238 ms**
- Child ID Request → Response: **63 ms**
- Full Attach: **812 ms**
- pcap parent request: `16:02:20.146` (frame 10)
- pcap parent response: `16:02:20.657` (frame 11)
- pcap child id request: `16:02:20.895` (frame 13)
- pcap child id response: `16:02:20.958` (frame 15)

#### Attach sequence 2

- log parent request: `16:04:08.326`
- log parent response: `16:04:08.816`
- log child id request: `None`
- log child id response: `None`
- parent ipv6: `fe80:0:0:0:d443:998:4d0c:727b`
- parent extaddr: `None`
- parent rloc16: `0xc400`
- timing source: **unavailable**
- Request → Response: **None ms**
- Response → Child ID Request: **None ms**
- Child ID Request → Response: **None ms**
- Full Attach: **None ms**

#### Attach sequence 3

- log parent request: `16:04:19.480`
- log parent response: `16:04:20.048`
- log child id request: `16:04:20.307`
- log child id response: `16:04:20.349`
- parent ipv6: `fe80:0:0:0:d443:998:4d0c:727b`
- parent extaddr: `d64309984d0c727b`
- parent rloc16: `0xc400`
- timing source: **pcap**
- Request → Response: **465 ms**
- Response → Child ID Request: **250 ms**
- Child ID Request → Response: **62 ms**
- Full Attach: **777 ms**
- pcap parent request: `16:04:19.563` (frame 51)
- pcap parent response: `16:04:20.028` (frame 54)
- pcap child id request: `16:04:20.278` (frame 56)
- pcap child id response: `16:04:20.340` (frame 58)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_no_early_attach_child_20260616-160706.log`

#### Attach sequence 1

- log parent request: `16:07:46.362`
- log parent response: `16:07:46.582`
- log child id request: `16:07:47.117`
- log child id response: `16:07:47.163`
- parent ipv6: `fe80:0:0:0:3c27:2245:1dbe:f10a`
- parent extaddr: `3e2722451dbef10a`
- parent rloc16: `0xbc00`
- timing source: **pcap**
- Request → Response: **222 ms**
- Response → Child ID Request: **528 ms**
- Child ID Request → Response: **64 ms**
- Full Attach: **814 ms**
- pcap parent request: `16:07:46.336` (frame 9)
- pcap parent response: `16:07:46.558` (frame 11)
- pcap child id request: `16:07:47.086` (frame 13)
- pcap child id response: `16:07:47.150` (frame 15)

#### Attach sequence 2

- log parent request: `16:09:43.480`
- log parent response: `16:09:43.722`
- log child id request: `16:09:44.307`
- log child id response: `16:09:44.350`
- parent ipv6: `fe80:0:0:0:2850:d9c6:7104:49f1`
- parent extaddr: `2a50d9c6710449f1`
- parent rloc16: `0x1800`
- timing source: **pcap**
- Request → Response: **139 ms**
- Response → Child ID Request: **575 ms**
- Child ID Request → Response: **64 ms**
- Full Attach: **778 ms**
- pcap parent request: `16:09:43.564` (frame 53)
- pcap parent response: `16:09:43.703` (frame 55)
- pcap child id request: `16:09:44.278` (frame 57)
- pcap child id response: `16:09:44.342` (frame 59)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_no_early_attach_child_20260616-161232.log`

#### Attach sequence 1

- log parent request: `16:13:11.743`
- log parent response: `16:13:12.179`
- log child id request: `16:13:12.515`
- log child id response: `16:13:12.606`
- parent ipv6: `fe80:0:0:0:c9c:a679:6a77:19af`
- parent extaddr: `0e9ca6796a7719af`
- parent rloc16: `0xf800`
- timing source: **pcap**
- Request → Response: **372 ms**
- Response → Child ID Request: **373 ms**
- Child ID Request → Response: **64 ms**
- Full Attach: **809 ms**
- pcap parent request: `16:13:11.784` (frame 10)
- pcap parent response: `16:13:12.156` (frame 11)
- pcap child id request: `16:13:12.529` (frame 13)
- pcap child id response: `16:13:12.593` (frame 15)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**
