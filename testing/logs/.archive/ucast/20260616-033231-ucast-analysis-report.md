# Child Log Analysis

## ucast_child

Files analyzed: **3**

### Summary

| Attach | Metric | M (SD), ms | n |
| --- | --- | ---: | ---: |
| 1 | Request → Response | 271.67 (93.56) | 3 |
| 1 | Response → Child ID Request | 468.00 (98.91) | 3 |
| 1 | Child ID Request → Response | 63.33 (1.53) | 3 |
| 1 | Full Attach | 803.00 (13.86) | 3 |
| 2 | Request → Response | 481.00 (0.00) | 1 |
| 2 | Response → Child ID Request | 234.00 (0.00) | 1 |
| 2 | Child ID Request → Response | 63.00 (0.00) | 1 |
| 2 | Full Attach | 778.00 (0.00) | 1 |
| 3 | Request → Response | 393.50 (40.31) | 2 |
| 3 | Response → Child ID Request | 323.00 (41.01) | 2 |
| 3 | Child ID Request → Response | 63.00 (2.83) | 2 |
| 3 | Full Attach | 779.50 (2.12) | 2 |

| Metric | M (SD) | n |
| --- | ---: | ---: |
| Failed TX Attempts per Log | 0.00 (0.00) | 3 |

### `ucast_child_20260610-134525.log`

#### Attach sequence 1

- log parent request: `13:47:24.634`
- log parent response: `13:47:24.859`
- log child id request: `13:47:25.405`
- log child id response: `13:47:25.494`
- parent ipv6: `fe80:0:0:0:d8bc:c2dc:fc25:6173`
- parent extaddr: `dabcc2dcfc256173`
- parent rloc16: `0x2c00`
- timing source: **pcap**
- Request → Response: **166 ms**
- Response → Child ID Request: **582 ms**
- Child ID Request → Response: **63 ms**
- Full Attach: **811 ms**
- pcap parent request: `13:47:24.670` (frame 9)
- pcap parent response: `13:47:24.836` (frame 10)
- pcap child id request: `13:47:25.418` (frame 13)
- pcap child id response: `13:47:25.481` (frame 15)

#### Attach sequence 2

- log parent request: `13:49:11.048`
- log parent response: `13:49:11.671`
- log child id request: `None`
- log child id response: `None`
- parent ipv6: `fe80:0:0:0:7027:e14e:90a6:f9ec`
- parent extaddr: `None`
- parent rloc16: `0x2000`
- timing source: **unavailable**
- Request → Response: **None ms**
- Response → Child ID Request: **None ms**
- Child ID Request → Response: **None ms**
- Full Attach: **None ms**

#### Attach sequence 3

- log parent request: `13:49:20.498`
- log parent response: `13:49:20.964`
- log child id request: `13:49:21.324`
- log child id response: `13:49:21.367`
- parent ipv6: `fe80:0:0:0:7027:e14e:90a6:f9ec`
- parent extaddr: `7227e14e90a6f9ec`
- parent rloc16: `0x2000`
- timing source: **pcap**
- Request → Response: **365 ms**
- Response → Child ID Request: **352 ms**
- Child ID Request → Response: **61 ms**
- Full Attach: **778 ms**
- pcap parent request: `13:49:20.580` (frame 56)
- pcap parent response: `13:49:20.945` (frame 58)
- pcap child id request: `13:49:21.297` (frame 60)
- pcap child id response: `13:49:21.358` (frame 62)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_child_20260610-135210.log`

#### Attach sequence 1

- log parent request: `13:53:12.101`
- log parent response: `13:53:12.504`
- log child id request: `13:53:12.873`
- log child id response: `13:53:12.962`
- parent ipv6: `fe80:0:0:0:300b:d7ed:19f1:1ce`
- parent extaddr: `320bd7ed19f101ce`
- parent rloc16: `0x6800`
- timing source: **pcap**
- Request → Response: **344 ms**
- Response → Child ID Request: **405 ms**
- Child ID Request → Response: **62 ms**
- Full Attach: **811 ms**
- pcap parent request: `13:53:12.138` (frame 10)
- pcap parent response: `13:53:12.482` (frame 11)
- pcap child id request: `13:53:12.887` (frame 13)
- pcap child id response: `13:53:12.949` (frame 15)

#### Attach sequence 2

- log parent request: `13:55:04.060`
- log parent response: `13:55:04.642`
- log child id request: `None`
- log child id response: `None`
- parent ipv6: `fe80:0:0:0:282d:e593:b6ec:885b`
- parent extaddr: `None`
- parent rloc16: `0xbc00`
- timing source: **unavailable**
- Request → Response: **None ms**
- Response → Child ID Request: **None ms**
- Child ID Request → Response: **None ms**
- Full Attach: **None ms**

#### Attach sequence 3

- log parent request: `13:55:13.540`
- log parent response: `13:55:14.063`
- log child id request: `13:55:14.366`
- log child id response: `13:55:14.412`
- parent ipv6: `fe80:0:0:0:282d:e593:b6ec:885b`
- parent extaddr: `2a2de593b6ec885b`
- parent rloc16: `0xbc00`
- timing source: **pcap**
- Request → Response: **422 ms**
- Response → Child ID Request: **294 ms**
- Child ID Request → Response: **65 ms**
- Full Attach: **781 ms**
- pcap parent request: `13:55:13.623` (frame 56)
- pcap parent response: `13:55:14.045` (frame 58)
- pcap child id request: `13:55:14.339` (frame 60)
- pcap child id response: `13:55:14.404` (frame 62)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_child_20260610-135758.log`

#### Attach sequence 1

- log parent request: `13:59:00.113`
- log parent response: `13:59:00.506`
- log child id request: `13:59:00.887`
- log child id response: `13:59:00.978`
- parent ipv6: `fe80:0:0:0:f443:75cc:b1ab:bdbc`
- parent extaddr: `f64375ccb1abbdbc`
- parent rloc16: `0x2800`
- timing source: **pcap**
- Request → Response: **305 ms**
- Response → Child ID Request: **417 ms**
- Child ID Request → Response: **65 ms**
- Full Attach: **787 ms**
- pcap parent request: `13:59:00.177` (frame 9)
- pcap parent response: `13:59:00.482` (frame 10)
- pcap child id request: `13:59:00.899` (frame 13)
- pcap child id response: `13:59:00.964` (frame 15)

#### Attach sequence 2

- log parent request: `14:00:52.199`
- log parent response: `14:00:52.782`
- log child id request: `14:00:53.025`
- log child id response: `14:00:53.068`
- parent ipv6: `fe80:0:0:0:c46a:6780:ed1d:4a8b`
- parent extaddr: `c66a6780ed1d4a8b`
- parent rloc16: `0xa400`
- timing source: **pcap**
- Request → Response: **481 ms**
- Response → Child ID Request: **234 ms**
- Child ID Request → Response: **63 ms**
- Full Attach: **778 ms**
- pcap parent request: `14:00:52.281` (frame 55)
- pcap parent response: `14:00:52.762` (frame 57)
- pcap child id request: `14:00:52.996` (frame 59)
- pcap child id response: `14:00:53.059` (frame 61)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**
