# Child Log Analysis

## ucast_fastpr_child

Files analyzed: **4**

- batch folders: `ucast_fastpr-2router-4runs-20260703-122349`

### PCAP-complete child attach summary

| Attach | Metric | M (SD), ms | n |
| --- | --- | ---: | ---: |
| 1 | Request -> Response | 166.50 (110.50) | 4 |
| 1 | Response -> Child ID Request | 585.25 (109.58) | 4 |
| 1 | Child ID Request -> Response | 14.50 (1.00) | 4 |
| 1 | Full Attach | 766.25 (2.22) | 4 |
| 2 | Request -> Response | 8.25 (0.50) | 4 |
| 2 | Response -> Child ID Request | 34.25 (0.96) | 4 |
| 2 | Child ID Request -> Response | 13.25 (0.50) | 4 |
| 2 | Full Attach | 55.75 (0.50) | 4 |

| Metric | M (SD) | n |
| --- | ---: | ---: |
| Failed TX Attempts per Log | 0.00 (0.00) | 4 |
| Log-only or Partial Sequences per Log | 1.00 (0.00) | 4 |

### `ucast_fastpr_child_20260703-122744-run01.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `deefd8d383d1c952`
- switch target extaddr(s): `02d6cc3c8a74376d, 02d6cc3c8a74376d, 02d6cc3c8a74376d`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `86094d5753815b73`
- parent rloc16: `n/a`
- child extaddr: `deefd8d383d1c952`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **57 ms**
- Response -> Child ID Request: **693 ms**
- Child ID Request -> Response: **13 ms**
- Full Attach: **763 ms**
- pcap parent request: `12:33:26.378` (frame 80)
- pcap parent response: `12:33:26.435` (frame 81)
- pcap child id request: `12:33:27.128` (frame 85)
- pcap child id response: `12:33:27.141` (frame 87)

#### PCAP-complete child attach 2

- log parent request: `12:33:30.980`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `02d6cc3c8a74376d`
- parent rloc16: `n/a`
- child extaddr: `deefd8d383d1c952`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **8 ms**
- Response -> Child ID Request: **35 ms**
- Child ID Request -> Response: **13 ms**
- Full Attach: **56 ms**
- pcap parent request: `12:33:31.026` (frame 89)
- pcap parent response: `12:33:31.034` (frame 91)
- pcap child id request: `12:33:31.069` (frame 93)
- pcap child id response: `12:33:31.082` (frame 95)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `12:33:31.000`
- log parent response: `12:33:31.013`
- log child id request: `12:33:31.032`
- log child id response: `12:33:31.063`
- parent ipv6: `n/a`
- parent extaddr: `02d6cc3c8a74376d`
- parent rloc16: `0xd400`
- child extaddr: `deefd8d383d1c952`
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

### `ucast_fastpr_child_20260703-123933-run02.log`

- manifest status: `completed`
- child extaddr: `766ea949da789084`
- switch target extaddr(s): `32eedc819f55e03f, 32eedc819f55e03f, 32eedc819f55e03f`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `3a9c23dc461cfbdb`
- parent rloc16: `n/a`
- child extaddr: `766ea949da789084`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **254 ms**
- Response -> Child ID Request: **499 ms**
- Child ID Request -> Response: **15 ms**
- Full Attach: **768 ms**
- pcap parent request: `12:45:13.640` (frame 73)
- pcap parent response: `12:45:13.894` (frame 74)
- pcap child id request: `12:45:14.393` (frame 78)
- pcap child id response: `12:45:14.408` (frame 80)

#### PCAP-complete child attach 2

- log parent request: `12:45:18.126`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `32eedc819f55e03f`
- parent rloc16: `n/a`
- child extaddr: `766ea949da789084`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **8 ms**
- Response -> Child ID Request: **34 ms**
- Child ID Request -> Response: **14 ms**
- Full Attach: **56 ms**
- pcap parent request: `12:45:18.174` (frame 83)
- pcap parent response: `12:45:18.182` (frame 85)
- pcap child id request: `12:45:18.216` (frame 87)
- pcap child id response: `12:45:18.230` (frame 89)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `12:45:18.145`
- log parent response: `12:45:18.160`
- log child id request: `12:45:18.179`
- log child id response: `12:45:18.212`
- parent ipv6: `n/a`
- parent extaddr: `32eedc819f55e03f`
- parent rloc16: `0x0c00`
- child extaddr: `766ea949da789084`
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

### `ucast_fastpr_child_20260703-125120-run03.log`

- manifest status: `completed`
- child extaddr: `6af7b64fa9d7cbc2`
- switch target extaddr(s): `a60412f10e424332, a60412f10e424332, a60412f10e424332`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `e6e167747459a209`
- parent rloc16: `n/a`
- child extaddr: `6af7b64fa9d7cbc2`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **86 ms**
- Response -> Child ID Request: **666 ms**
- Child ID Request -> Response: **15 ms**
- Full Attach: **767 ms**
- pcap parent request: `12:57:01.036` (frame 81)
- pcap parent response: `12:57:01.122` (frame 82)
- pcap child id request: `12:57:01.788` (frame 86)
- pcap child id response: `12:57:01.803` (frame 88)

#### PCAP-complete child attach 2

- log parent request: `12:57:05.130`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `a60412f10e424332`
- parent rloc16: `n/a`
- child extaddr: `6af7b64fa9d7cbc2`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **9 ms**
- Response -> Child ID Request: **33 ms**
- Child ID Request -> Response: **13 ms**
- Full Attach: **55 ms**
- pcap parent request: `12:57:05.175` (frame 90)
- pcap parent response: `12:57:05.184` (frame 92)
- pcap child id request: `12:57:05.217` (frame 94)
- pcap child id response: `12:57:05.230` (frame 96)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `12:57:05.150`
- log parent response: `12:57:05.164`
- log child id request: `12:57:05.183`
- log child id response: `12:57:05.212`
- parent ipv6: `n/a`
- parent extaddr: `a60412f10e424332`
- parent rloc16: `0x5c00`
- child extaddr: `6af7b64fa9d7cbc2`
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

### `ucast_fastpr_child_20260703-130307-run04.log`

- manifest status: `completed`
- child extaddr: `eaa5e463993111cf`
- switch target extaddr(s): `2abdaeab6b9e3397, 2abdaeab6b9e3397, 2abdaeab6b9e3397`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `621eb5a2343c6c22`
- parent rloc16: `n/a`
- child extaddr: `eaa5e463993111cf`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **269 ms**
- Response -> Child ID Request: **483 ms**
- Child ID Request -> Response: **15 ms**
- Full Attach: **767 ms**
- pcap parent request: `13:08:47.499` (frame 75)
- pcap parent response: `13:08:47.768` (frame 76)
- pcap child id request: `13:08:48.251` (frame 80)
- pcap child id response: `13:08:48.266` (frame 82)

#### PCAP-complete child attach 2

- log parent request: `13:08:51.952`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `2abdaeab6b9e3397`
- parent rloc16: `n/a`
- child extaddr: `eaa5e463993111cf`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **8 ms**
- Response -> Child ID Request: **35 ms**
- Child ID Request -> Response: **13 ms**
- Full Attach: **56 ms**
- pcap parent request: `13:08:51.999` (frame 85)
- pcap parent response: `13:08:52.007` (frame 87)
- pcap child id request: `13:08:52.042` (frame 89)
- pcap child id response: `13:08:52.055` (frame 91)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `13:08:51.971`
- log parent response: `13:08:51.987`
- log child id request: `13:08:52.006`
- log child id response: `13:08:52.037`
- parent ipv6: `n/a`
- parent extaddr: `2abdaeab6b9e3397`
- parent rloc16: `0xe000`
- child extaddr: `eaa5e463993111cf`
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
