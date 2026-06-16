# Child Log Analysis

## ucast_no_early_attach_child

Files analyzed: **1**

### Summary

| Attach | Metric | M (SD), ms | n |
| --- | --- | ---: | ---: |
| 1 | Request → Response | 305.00 (0.00) | 1 |
| 1 | Response → Child ID Request | 417.00 (0.00) | 1 |
| 1 | Child ID Request → Response | 65.00 (0.00) | 1 |
| 1 | Full Attach | 787.00 (0.00) | 1 |
| 2 | Request → Response | 481.00 (0.00) | 1 |
| 2 | Response → Child ID Request | 234.00 (0.00) | 1 |
| 2 | Child ID Request → Response | 63.00 (0.00) | 1 |
| 2 | Full Attach | 778.00 (0.00) | 1 |

| Metric | M (SD) | n |
| --- | ---: | ---: |
| Failed TX Attempts per Log | 0.00 (0.00) | 1 |

### `ucast_no_early_attach_child_20260610-135758.log`

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
