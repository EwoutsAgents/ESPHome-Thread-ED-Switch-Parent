# Child Log Analysis

## ucast_fastpr_child

Files analyzed: **1**

- batch folders: `ucast_fastpr-4router-1runs-20260628-040307`

### PCAP-complete child attach summary

| Attach | Metric | M (SD), ms | n |
| --- | --- | ---: | ---: |
| 1 | Request -> Response | 123.00 (0.00) | 1 |
| 1 | Response -> Child ID Request | 628.00 (0.00) | 1 |
| 1 | Child ID Request -> Response | 64.00 (0.00) | 1 |
| 1 | Full Attach | 815.00 (0.00) | 1 |
| 2 | Request -> Response | 44.00 (0.00) | 1 |
| 2 | Response -> Child ID Request | 125.00 (0.00) | 1 |
| 2 | Child ID Request -> Response | 70.00 (0.00) | 1 |
| 2 | Full Attach | 239.00 (0.00) | 1 |

| Metric | M (SD) | n |
| --- | ---: | ---: |
| Failed TX Attempts per Log | 0.00 (0.00) | 1 |
| Log-only or Partial Sequences per Log | 0.00 (0.00) | 1 |

### `ucast_fastpr_child_20260628-040354-run01.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `028538913d156257`
- switch target extaddr(s): `b6ba2c1db2d18ce2, b6ba2c1db2d18ce2, b6ba2c1db2d18ce2`

#### PCAP-complete child attach 1

- log parent request: `04:09:45.201`
- log parent response: `04:09:45.371`
- log child id request: `04:09:45.968`
- log child id response: `04:09:46.055`
- parent ipv6: `fe80:0:0:0:a09a:df5e:e53d:b90b`
- parent extaddr: `a29adf5ee53db90b`
- parent rloc16: `0xf800`
- child extaddr: `028538913d156257`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **123 ms**
- Response -> Child ID Request: **628 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **815 ms**
- pcap parent request: `04:09:45.246` (frame 186)
- pcap parent response: `04:09:45.369` (frame 187)
- pcap child id request: `04:09:45.997` (frame 195)
- pcap child id response: `04:09:46.061` (frame 197)

#### PCAP-complete child attach 2

- log parent request: `04:09:49.765`
- log parent response: `04:09:49.859`
- log child id request: `04:09:49.952`
- log child id response: `04:09:50.046`
- parent ipv6: `fe80:0:0:0:b4ba:2c1d:b2d1:8ce2`
- parent extaddr: `b6ba2c1db2d18ce2`
- parent rloc16: `0xd000`
- child extaddr: `028538913d156257`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **44 ms**
- Response -> Child ID Request: **125 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **239 ms**
- pcap parent request: `04:09:49.813` (frame 199)
- pcap parent response: `04:09:49.857` (frame 201)
- pcap child id request: `04:09:49.982` (frame 203)
- pcap child id response: `04:09:50.052` (frame 205)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**
