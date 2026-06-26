# Child Log Analysis

## ucast_fastpr_child

Files analyzed: **2**

- batch folders: `ucast_fastpr-4router-1runs-20260626-212247, ucast_fastpr-4router-1runs-20260626-214654`

### PCAP-complete child attach summary

| Attach | Metric | M (SD), ms | n |
| --- | --- | ---: | ---: |
| 1 | Request -> Response | 150.50 (149.20) | 2 |
| 1 | Response -> Child ID Request | 600.00 (148.49) | 2 |
| 1 | Child ID Request -> Response | 62.00 (0.00) | 2 |
| 1 | Full Attach | 812.50 (0.71) | 2 |
| 2 | Request -> Response | 47.50 (4.95) | 2 |
| 2 | Response -> Child ID Request | 319.50 (2.12) | 2 |
| 2 | Child ID Request -> Response | 70.50 (0.71) | 2 |
| 2 | Full Attach | 437.50 (3.54) | 2 |

| Metric | M (SD) | n |
| --- | ---: | ---: |
| Failed TX Attempts per Log | 0.00 (0.00) | 2 |
| Log-only or Partial Sequences per Log | 0.00 (0.00) | 2 |

### `ucast_fastpr_child_20260626-212247-run01.log`

- manifest status: `completed`
- child extaddr: `6654808815406715`
- switch target extaddr(s): `5ad440c4bc9d1fe6, 5ad440c4bc9d1fe6, 5ad440c4bc9d1fe6`

#### PCAP-complete child attach 1

- log parent request: `21:28:37.982`
- log parent response: `21:28:38.025`
- log child id request: `21:28:38.700`
- log child id response: `21:28:38.784`
- parent ipv6: `fe80:0:0:0:5c81:ab66:aa49:3fc9`
- parent extaddr: `5e81ab66aa493fc9`
- parent rloc16: `0x6c00`
- child extaddr: `6654808815406715`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **45 ms**
- Response -> Child ID Request: **705 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **812 ms**
- pcap parent request: `21:28:37.975` (frame 534)
- pcap parent response: `21:28:38.020` (frame 535)
- pcap child id request: `21:28:38.725` (frame 543)
- pcap child id response: `21:28:38.787` (frame 545)

#### PCAP-complete child attach 2

- log parent request: `21:28:42.639`
- log parent response: `21:28:42.740`
- log child id request: `21:28:43.023`
- log child id response: `21:28:43.121`
- parent ipv6: `fe80:0:0:0:58d4:40c4:bc9d:1fe6`
- parent extaddr: `5ad440c4bc9d1fe6`
- parent rloc16: `0xe800`
- child extaddr: `6654808815406715`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **51 ms**
- Response -> Child ID Request: **318 ms**
- Child ID Request -> Response: **71 ms**
- Full Attach: **440 ms**
- pcap parent request: `21:28:42.686` (frame 564)
- pcap parent response: `21:28:42.737` (frame 566)
- pcap child id request: `21:28:43.055` (frame 568)
- pcap child id response: `21:28:43.126` (frame 570)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260626-214654-run01.log`

- manifest status: `completed`
- child extaddr: `26ba9d96752b115f`
- switch target extaddr(s): `3e7c298a366472c7, 3e7c298a366472c7, 3e7c298a366472c7`

#### PCAP-complete child attach 1

- log parent request: `21:52:45.575`
- log parent response: `21:52:45.739`
- log child id request: `21:52:46.296`
- log child id response: `21:52:46.381`
- parent ipv6: `fe80:0:0:0:e2:1aee:9901:12ac`
- parent extaddr: `02e21aee990112ac`
- parent rloc16: `0xa000`
- child extaddr: `26ba9d96752b115f`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **256 ms**
- Response -> Child ID Request: **495 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **813 ms**
- pcap parent request: `21:52:45.571` (frame 607)
- pcap parent response: `21:52:45.827` (frame 620)
- pcap child id request: `21:52:46.322` (frame 630)
- pcap child id response: `21:52:46.384` (frame 632)

#### PCAP-complete child attach 2

- log parent request: `21:52:49.935`
- log parent response: `21:52:50.027`
- log child id request: `21:52:50.311`
- log child id response: `21:52:50.409`
- parent ipv6: `fe80:0:0:0:3c7c:298a:3664:72c7`
- parent extaddr: `3e7c298a366472c7`
- parent rloc16: `0x7c00`
- child extaddr: `26ba9d96752b115f`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **44 ms**
- Response -> Child ID Request: **321 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **435 ms**
- pcap parent request: `21:52:49.979` (frame 634)
- pcap parent response: `21:52:50.023` (frame 636)
- pcap child id request: `21:52:50.344` (frame 638)
- pcap child id response: `21:52:50.414` (frame 640)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**
