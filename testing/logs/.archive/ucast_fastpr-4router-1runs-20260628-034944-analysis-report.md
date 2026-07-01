# Child Log Analysis

## ucast_fastpr_child

Files analyzed: **1**

- batch folders: `ucast_fastpr-4router-1runs-20260628-034944`

### PCAP-complete child attach summary

| Attach | Metric | M (SD), ms | n |
| --- | --- | ---: | ---: |
| 1 | Request -> Response | 193.00 (0.00) | 1 |
| 1 | Response -> Child ID Request | 552.00 (0.00) | 1 |
| 1 | Child ID Request -> Response | 66.00 (0.00) | 1 |
| 1 | Full Attach | 811.00 (0.00) | 1 |
| 2 | Request -> Response | 41.00 (0.00) | 1 |
| 2 | Response -> Child ID Request | 321.00 (0.00) | 1 |
| 2 | Child ID Request -> Response | 64.00 (0.00) | 1 |
| 2 | Full Attach | 426.00 (0.00) | 1 |

| Metric | M (SD) | n |
| --- | ---: | ---: |
| Failed TX Attempts per Log | 0.00 (0.00) | 1 |
| Log-only or Partial Sequences per Log | 0.00 (0.00) | 1 |

### `ucast_fastpr_child_20260628-035032-run01.log`

- manifest status: `completed`
- child extaddr: `16b33ecf933f1116`
- switch target extaddr(s): `a2e36447847874db, a2e36447847874db, a2e36447847874db`

#### PCAP-complete child attach 1

- log parent request: `03:56:21.931`
- log parent response: `03:56:22.177`
- log child id request: `03:56:22.736`
- log child id response: `03:56:22.788`
- parent ipv6: `fe80:0:0:0:68c4:7403:ddd9:ef78`
- parent extaddr: `6ac47403ddd9ef78`
- parent rloc16: `0x4c00`
- child extaddr: `16b33ecf933f1116`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **193 ms**
- Response -> Child ID Request: **552 ms**
- Child ID Request -> Response: **66 ms**
- Full Attach: **811 ms**
- pcap parent request: `03:56:21.980` (frame 530)
- pcap parent response: `03:56:22.173` (frame 532)
- pcap child id request: `03:56:22.725` (frame 540)
- pcap child id response: `03:56:22.791` (frame 542)

#### PCAP-complete child attach 2

- log parent request: `03:56:26.696`
- log parent response: `03:56:26.786`
- log child id request: `03:56:27.070`
- log child id response: `03:56:27.162`
- parent ipv6: `fe80:0:0:0:a0e3:6447:8478:74db`
- parent extaddr: `a2e36447847874db`
- parent rloc16: `0xa400`
- child extaddr: `16b33ecf933f1116`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **41 ms**
- Response -> Child ID Request: **321 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **426 ms**
- pcap parent request: `03:56:26.741` (frame 546)
- pcap parent response: `03:56:26.782` (frame 548)
- pcap child id request: `03:56:27.103` (frame 550)
- pcap child id response: `03:56:27.167` (frame 552)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**
