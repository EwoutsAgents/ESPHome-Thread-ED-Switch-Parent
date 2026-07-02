# Child Log Analysis

## ucast_fastpr_child

Files analyzed: **5**

- batch folders: `ucast_fastpr-2router-5runs-20260702-012315`

### PCAP-complete child attach summary

| Attach | Metric | M (SD), ms | n |
| --- | --- | ---: | ---: |
| 1 | Request -> Response | 254.00 (176.11) | 5 |
| 1 | Response -> Child ID Request | 494.60 (176.06) | 5 |
| 1 | Child ID Request -> Response | 63.40 (1.34) | 5 |
| 1 | Full Attach | 812.00 (2.35) | 5 |
| 2 | Request -> Response | 41.20 (1.64) | 5 |
| 2 | Response -> Child ID Request | 221.20 (271.57) | 5 |
| 2 | Child ID Request -> Response | 63.80 (0.84) | 5 |
| 2 | Full Attach | 326.20 (273.25) | 5 |

| Metric | M (SD) | n |
| --- | ---: | ---: |
| Failed TX Attempts per Log | 12.80 (28.62) | 5 |
| Log-only or Partial Sequences per Log | 0.20 (0.45) | 5 |

### `ucast_fastpr_child_20260702-012430-run01.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `ea1c731de9ac7e75`
- switch target extaddr(s): `b6f3e0a9f38e1889, b6f3e0a9f38e1889, b6f3e0a9f38e1889`

#### PCAP-complete child attach 1

- log parent request: `01:30:13.108`
- log parent response: `01:30:13.517`
- log child id request: `01:30:13.881`
- log child id response: `01:30:13.970`
- parent ipv6: `fe80:0:0:0:34a0:f595:2c69:61de`
- parent extaddr: `36a0f5952c6961de`
- parent rloc16: `0x4400`
- child extaddr: `ea1c731de9ac7e75`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **350 ms**
- Response -> Child ID Request: **399 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **813 ms**
- pcap parent request: `01:30:13.156` (frame 74)
- pcap parent response: `01:30:13.506` (frame 75)
- pcap child id request: `01:30:13.905` (frame 79)
- pcap child id response: `01:30:13.969` (frame 81)

#### PCAP-complete child attach 2

- log parent request: `01:30:17.034`
- log parent response: `01:30:17.122`
- log child id request: `01:30:17.174`
- log child id response: `01:30:17.272`
- parent ipv6: `fe80:0:0:0:b4f3:e0a9:f38e:1889`
- parent extaddr: `b6f3e0a9f38e1889`
- parent rloc16: `0xcc00`
- child extaddr: `ea1c731de9ac7e75`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **41 ms**
- Response -> Child ID Request: **101 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **205 ms**
- pcap parent request: `01:30:17.061` (frame 84)
- pcap parent response: `01:30:17.102` (frame 86)
- pcap child id request: `01:30:17.203` (frame 88)
- pcap child id response: `01:30:17.266` (frame 90)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260702-013619-run02.log`

- manifest status: `completed`
- child extaddr: `e6e241941bd9b9bc`
- switch target extaddr(s): `7e72bdade8cfd6a5, 7e72bdade8cfd6a5, 7e72bdade8cfd6a5`

#### PCAP-complete child attach 1

- log parent request: `01:42:00.611`
- log parent response: `01:42:01.119`
- log child id request: `01:42:01.321`
- log child id response: `01:42:01.409`
- parent ipv6: `fe80:0:0:0:f011:a083:bd0d:dfe7`
- parent extaddr: `f211a083bd0ddfe7`
- parent rloc16: `0x1000`
- child extaddr: `e6e241941bd9b9bc`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **509 ms**
- Response -> Child ID Request: **239 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **810 ms**
- pcap parent request: `01:42:00.596` (frame 77)
- pcap parent response: `01:42:01.105` (frame 78)
- pcap child id request: `01:42:01.344` (frame 82)
- pcap child id response: `01:42:01.406` (frame 84)

#### PCAP-complete child attach 2

- log parent request: `01:42:04.680`
- log parent response: `01:42:04.769`
- log child id request: `01:42:04.820`
- log child id response: `01:42:04.918`
- parent ipv6: `fe80:0:0:0:7c72:bdad:e8cf:d6a5`
- parent extaddr: `7e72bdade8cfd6a5`
- parent rloc16: `0x8800`
- child extaddr: `e6e241941bd9b9bc`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **41 ms**
- Response -> Child ID Request: **98 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **203 ms**
- pcap parent request: `01:42:04.708` (frame 88)
- pcap parent response: `01:42:04.749` (frame 90)
- pcap child id request: `01:42:04.847` (frame 92)
- pcap child id response: `01:42:04.911` (frame 94)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260702-014807-run03.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `9652946acb0ad4cd`
- switch target extaddr(s): `6ee08a5439d17ab5, 6ee08a5439d17ab5, 6ee08a5439d17ab5`

#### PCAP-complete child attach 1

- log parent request: `01:53:48.208`
- log parent response: `01:53:48.367`
- log child id request: `01:53:48.919`
- log child id response: `01:53:49.007`
- parent ipv6: `fe80:0:0:0:b4c7:6ff2:29eb:9ad1`
- parent extaddr: `b6c76ff229eb9ad1`
- parent rloc16: `0xa400`
- child extaddr: `9652946acb0ad4cd`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **162 ms**
- Response -> Child ID Request: **588 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **814 ms**
- pcap parent request: `01:53:48.192` (frame 71)
- pcap parent response: `01:53:48.354` (frame 72)
- pcap child id request: `01:53:48.942` (frame 77)
- pcap child id response: `01:53:49.006` (frame 79)

#### PCAP-complete child attach 2

- log parent request: `01:57:48.872`
- log parent response: `01:57:48.915`
- log child id request: `01:57:49.584`
- log child id response: `01:57:49.674`
- parent ipv6: `fe80:0:0:0:6ce0:8a54:39d1:7ab5`
- parent extaddr: `6ee08a5439d17ab5`
- parent rloc16: `0x3800`
- child extaddr: `9652946acb0ad4cd`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **44 ms**
- Response -> Child ID Request: **707 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **815 ms**
- pcap parent request: `01:57:48.865` (frame 235)
- pcap parent response: `01:57:48.909` (frame 236)
- pcap child id request: `01:57:49.616` (frame 238)
- pcap child id response: `01:57:49.680` (frame 240)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `01:53:52.151`
- log parent response: `01:53:52.238`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `fe80:0:0:0:6ce0:8a54:39d1:7ab5`
- parent extaddr: `6ee08a5439d17ab5`
- parent rloc16: `0x3800`
- child extaddr: `9652946acb0ad4cd`
- timing source: **unavailable**
- complete log attach: **False**
- complete pcap attach: **False**
- Request -> Response: **None ms**
- Response -> Child ID Request: **None ms**
- Child ID Request -> Response: **None ms**
- Full Attach: **None ms**

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 103: 16, seq 104: 16, seq 105: 16, seq 106: 16
- failed tx by dst: `b6c76ff229eb9ad1`: 54

### `ucast_fastpr_child_20260702-015954-run04.log`

- manifest status: `completed`
- child extaddr: `821f3781744609e5`
- switch target extaddr(s): `2e988c55481306f9, 2e988c55481306f9, 2e988c55481306f9`

#### PCAP-complete child attach 1

- log parent request: `02:05:35.540`
- log parent response: `02:05:35.600`
- log child id request: `02:05:36.250`
- log child id response: `02:05:36.336`
- parent ipv6: `fe80:0:0:0:5ce7:a23a:df17:4242`
- parent extaddr: `5ee7a23adf174242`
- parent rloc16: `0x3c00`
- child extaddr: `821f3781744609e5`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **62 ms**
- Response -> Child ID Request: **685 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **809 ms**
- pcap parent request: `02:05:35.525` (frame 71)
- pcap parent response: `02:05:35.587` (frame 72)
- pcap child id request: `02:05:36.272` (frame 76)
- pcap child id response: `02:05:36.334` (frame 78)

#### PCAP-complete child attach 2

- log parent request: `02:05:39.552`
- log parent response: `02:05:39.640`
- log child id request: `02:05:39.691`
- log child id response: `02:05:39.789`
- parent ipv6: `fe80:0:0:0:2c98:8c55:4813:6f9`
- parent extaddr: `2e988c55481306f9`
- parent rloc16: `0x4800`
- child extaddr: `821f3781744609e5`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **40 ms**
- Response -> Child ID Request: **100 ms**
- Child ID Request -> Response: **65 ms**
- Full Attach: **205 ms**
- pcap parent request: `02:05:39.577` (frame 81)
- pcap parent response: `02:05:39.617` (frame 83)
- pcap child id request: `02:05:39.717` (frame 85)
- pcap child id response: `02:05:39.782` (frame 87)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260702-021142-run05.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `ae163f57682d628e`
- switch target extaddr(s): `82b31e59bf759eff, 82b31e59bf759eff, 82b31e59bf759eff`

#### PCAP-complete child attach 1

- log parent request: `02:17:23.041`
- log parent response: `02:17:23.226`
- log child id request: `02:17:23.752`
- log child id response: `02:17:23.842`
- parent ipv6: `fe80:0:0:0:3006:bc23:9ac2:4354`
- parent extaddr: `3206bc239ac24354`
- parent rloc16: `0x3800`
- child extaddr: `ae163f57682d628e`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **187 ms**
- Response -> Child ID Request: **562 ms**
- Child ID Request -> Response: **65 ms**
- Full Attach: **814 ms**
- pcap parent request: `02:17:23.027` (frame 79)
- pcap parent response: `02:17:23.214` (frame 80)
- pcap child id request: `02:17:23.776` (frame 84)
- pcap child id response: `02:17:23.841` (frame 86)

#### PCAP-complete child attach 2

- log parent request: `02:17:27.184`
- log parent response: `02:17:27.270`
- log child id request: `02:17:27.324`
- log child id response: `02:17:27.421`
- parent ipv6: `fe80:0:0:0:80b3:1e59:bf75:9eff`
- parent extaddr: `82b31e59bf759eff`
- parent rloc16: `0xe400`
- child extaddr: `ae163f57682d628e`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **40 ms**
- Response -> Child ID Request: **100 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **203 ms**
- pcap parent request: `02:17:27.211` (frame 90)
- pcap parent response: `02:17:27.251` (frame 92)
- pcap child id request: `02:17:27.351` (frame 94)
- pcap child id response: `02:17:27.414` (frame 96)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**
