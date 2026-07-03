# Child Log Analysis

## ucast_fastpr_child

Files analyzed: **4**

- batch folders: `ucast_fastpr-4router-4runs-20260703-165902`

### PCAP-complete child attach summary

| Attach | Metric | M (SD), ms | n |
| --- | --- | ---: | ---: |
| 1 | Request -> Response | 84.50 (47.53) | 4 |
| 1 | Response -> Child ID Request | 668.75 (47.70) | 4 |
| 1 | Child ID Request -> Response | 13.25 (1.26) | 4 |
| 1 | Full Attach | 766.50 (2.65) | 4 |
| 2 | Request -> Response | 8.50 (0.58) | 4 |
| 2 | Response -> Child ID Request | 29.00 (0.82) | 4 |
| 2 | Child ID Request -> Response | 14.50 (1.00) | 4 |
| 2 | Full Attach | 52.00 (2.16) | 4 |

| Metric | M (SD) | n |
| --- | ---: | ---: |
| Failed TX Attempts per Log | 0.00 (0.00) | 4 |
| Log-only or Partial Sequences per Log | 1.00 (0.00) | 4 |

### `ucast_fastpr_child_20260703-170521-run01.log`

- manifest status: `completed`
- child extaddr: `1a35cf72b07ac07d`
- switch target extaddr(s): `2eec0582532c9fc1, 2eec0582532c9fc1, 2eec0582532c9fc1`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `ca108cb69b372249`
- parent rloc16: `n/a`
- child extaddr: `1a35cf72b07ac07d`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **147 ms**
- Response -> Child ID Request: **607 ms**
- Child ID Request -> Response: **13 ms**
- Full Attach: **767 ms**
- pcap parent request: `17:11:11.270` (frame 1207)
- pcap parent response: `17:11:11.417` (frame 1210)
- pcap child id request: `17:11:12.024` (frame 1216)
- pcap child id response: `17:11:12.037` (frame 1218)

#### PCAP-complete child attach 2

- log parent request: `17:11:15.493`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `2eec0582532c9fc1`
- parent rloc16: `n/a`
- child extaddr: `1a35cf72b07ac07d`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **9 ms**
- Response -> Child ID Request: **30 ms**
- Child ID Request -> Response: **16 ms**
- Full Attach: **55 ms**
- pcap parent request: `17:11:15.540` (frame 1220)
- pcap parent response: `17:11:15.549` (frame 1222)
- pcap child id request: `17:11:15.579` (frame 1224)
- pcap child id response: `17:11:15.595` (frame 1226)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `17:11:15.511`
- log parent response: `17:11:15.528`
- log child id request: `17:11:15.543`
- log child id response: `17:11:15.576`
- parent ipv6: `n/a`
- parent extaddr: `2eec0582532c9fc1`
- parent rloc16: `0xec00`
- child extaddr: `1a35cf72b07ac07d`
- timing source: **unavailable**
- complete log attach: **True**
- complete pcap attach: **False**
- Request -> Response: **None ms**
- Response -> Child ID Request: **None ms**
- Child ID Request -> Response: **None ms**
- Full Attach: **None ms**

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260703-171718-run02.log`

- manifest status: `completed`
- child extaddr: `0223d488e3a67653`
- switch target extaddr(s): `4ac0bf22bde03732, 4ac0bf22bde03732, 4ac0bf22bde03732`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `463267880b57cb71`
- parent rloc16: `n/a`
- child extaddr: `0223d488e3a67653`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **36 ms**
- Response -> Child ID Request: **719 ms**
- Child ID Request -> Response: **15 ms**
- Full Attach: **770 ms**
- pcap parent request: `17:23:08.179` (frame 197)
- pcap parent response: `17:23:08.215` (frame 198)
- pcap child id request: `17:23:08.934` (frame 206)
- pcap child id response: `17:23:08.949` (frame 208)

#### PCAP-complete child attach 2

- log parent request: `17:23:12.431`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `4ac0bf22bde03732`
- parent rloc16: `n/a`
- child extaddr: `0223d488e3a67653`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **9 ms**
- Response -> Child ID Request: **29 ms**
- Child ID Request -> Response: **14 ms**
- Full Attach: **52 ms**
- pcap parent request: `17:23:12.478` (frame 210)
- pcap parent response: `17:23:12.487` (frame 212)
- pcap child id request: `17:23:12.516` (frame 214)
- pcap child id response: `17:23:12.530` (frame 216)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `17:23:12.449`
- log parent response: `17:23:12.466`
- log child id request: `17:23:12.481`
- log child id response: `17:23:12.511`
- parent ipv6: `n/a`
- parent extaddr: `4ac0bf22bde03732`
- parent rloc16: `0x4800`
- child extaddr: `0223d488e3a67653`
- timing source: **unavailable**
- complete log attach: **True**
- complete pcap attach: **False**
- Request -> Response: **None ms**
- Response -> Child ID Request: **None ms**
- Child ID Request -> Response: **None ms**
- Full Attach: **None ms**

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260703-172915-run03.log`

- manifest status: `completed`
- child extaddr: `96faa2c6bd747b4d`
- switch target extaddr(s): `a2d9a4753893d74e, a2d9a4753893d74e, a2d9a4753893d74e`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `ba46738a07cf5631`
- parent rloc16: `n/a`
- child extaddr: `96faa2c6bd747b4d`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **63 ms**
- Response -> Child ID Request: **689 ms**
- Child ID Request -> Response: **13 ms**
- Full Attach: **765 ms**
- pcap parent request: `17:35:05.142` (frame 216)
- pcap parent response: `17:35:05.205` (frame 217)
- pcap child id request: `17:35:05.894` (frame 225)
- pcap child id response: `17:35:05.907` (frame 227)

#### PCAP-complete child attach 2

- log parent request: `17:35:09.420`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `a2d9a4753893d74e`
- parent rloc16: `n/a`
- child extaddr: `96faa2c6bd747b4d`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **8 ms**
- Response -> Child ID Request: **28 ms**
- Child ID Request -> Response: **14 ms**
- Full Attach: **50 ms**
- pcap parent request: `17:35:09.465` (frame 230)
- pcap parent response: `17:35:09.473` (frame 232)
- pcap child id request: `17:35:09.501` (frame 234)
- pcap child id response: `17:35:09.515` (frame 236)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `17:35:09.438`
- log parent response: `17:35:09.452`
- log child id request: `17:35:09.467`
- log child id response: `17:35:09.496`
- parent ipv6: `n/a`
- parent extaddr: `a2d9a4753893d74e`
- parent rloc16: `0x3c00`
- child extaddr: `96faa2c6bd747b4d`
- timing source: **unavailable**
- complete log attach: **True**
- complete pcap attach: **False**
- Request -> Response: **None ms**
- Response -> Child ID Request: **None ms**
- Child ID Request -> Response: **None ms**
- Full Attach: **None ms**

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260703-174112-run04.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `360220733ead8d7b`
- switch target extaddr(s): `1659783c46fd24f6, 1659783c46fd24f6, 1659783c46fd24f6`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `5adf543fe42ea1a3`
- parent rloc16: `n/a`
- child extaddr: `360220733ead8d7b`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **92 ms**
- Response -> Child ID Request: **660 ms**
- Child ID Request -> Response: **12 ms**
- Full Attach: **764 ms**
- pcap parent request: `17:47:02.341` (frame 439)
- pcap parent response: `17:47:02.433` (frame 442)
- pcap child id request: `17:47:03.093` (frame 448)
- pcap child id response: `17:47:03.105` (frame 450)

#### PCAP-complete child attach 2

- log parent request: `17:47:06.465`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `1659783c46fd24f6`
- parent rloc16: `n/a`
- child extaddr: `360220733ead8d7b`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **8 ms**
- Response -> Child ID Request: **29 ms**
- Child ID Request -> Response: **14 ms**
- Full Attach: **51 ms**
- pcap parent request: `17:47:06.510` (frame 454)
- pcap parent response: `17:47:06.518` (frame 456)
- pcap child id request: `17:47:06.547` (frame 458)
- pcap child id response: `17:47:06.561` (frame 460)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `17:47:06.483`
- log parent response: `17:47:06.498`
- log child id request: `17:47:06.513`
- log child id response: `17:47:06.543`
- parent ipv6: `n/a`
- parent extaddr: `1659783c46fd24f6`
- parent rloc16: `0xac00`
- child extaddr: `360220733ead8d7b`
- timing source: **unavailable**
- complete log attach: **True**
- complete pcap attach: **False**
- Request -> Response: **None ms**
- Response -> Child ID Request: **None ms**
- Child ID Request -> Response: **None ms**
- Full Attach: **None ms**

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**
