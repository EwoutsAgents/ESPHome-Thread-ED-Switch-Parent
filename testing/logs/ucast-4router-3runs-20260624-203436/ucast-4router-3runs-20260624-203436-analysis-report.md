# Child Log Analysis

## ucast_child

Files analyzed: **3**

### PCAP-complete child attach summary

| Attach | Metric | M (SD), ms | n |
| --- | --- | ---: | ---: |
| 1 | Request -> Response | 118.67 (60.58) | 3 |
| 1 | Response -> Child ID Request | 621.00 (62.86) | 3 |
| 1 | Child ID Request -> Response | 67.67 (4.04) | 3 |
| 1 | Full Attach | 807.33 (14.36) | 3 |
| 2 | Request -> Response | 378.00 (141.38) | 3 |
| 2 | Response -> Child ID Request | 321.33 (2.08) | 3 |
| 2 | Child ID Request -> Response | 62.33 (1.53) | 3 |
| 2 | Full Attach | 761.67 (143.62) | 3 |

| Metric | M (SD) | n |
| --- | ---: | ---: |
| Failed TX Attempts per Log | 0.00 (0.00) | 3 |
| Log-only or Partial Sequences per Log | 0.00 (0.00) | 3 |

### `ucast_child_20260624-203613-run01.log`

- child extaddr: `c2feae4e42597734`
- switch target extaddr(s): `da62be79673d42b2, da62be79673d42b2, da62be79673d42b2`

#### PCAP-complete child attach 1

- log parent request: `20:42:04.295`
- log parent response: `20:42:04.355`
- log child id request: `20:42:05.015`
- log child id response: `20:42:05.100`
- parent ipv6: `fe80:0:0:0:70fa:bfa:95d4:8ba5`
- parent extaddr: `72fa0bfa95d48ba5`
- parent rloc16: `0x2c00`
- child extaddr: `c2feae4e42597734`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **60 ms**
- Response -> Child ID Request: **690 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **813 ms**
- pcap parent request: `20:42:04.292` (frame 582)
- pcap parent response: `20:42:04.352` (frame 583)
- pcap child id request: `20:42:05.042` (frame 591)
- pcap child id response: `20:42:05.105` (frame 593)

#### PCAP-complete child attach 2

- log parent request: `20:42:34.987`
- log parent response: `20:42:35.456`
- log child id request: `20:42:35.746`
- log child id response: `20:42:35.834`
- parent ipv6: `fe80:0:0:0:d862:be79:673d:42b2`
- parent extaddr: `da62be79673d42b2`
- parent rloc16: `0x9000`
- child extaddr: `c2feae4e42597734`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **390 ms**
- Response -> Child ID Request: **323 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **777 ms**
- pcap parent request: `20:42:35.063` (frame 656)
- pcap parent response: `20:42:35.453` (frame 658)
- pcap child id request: `20:42:35.776` (frame 660)
- pcap child id response: `20:42:35.840` (frame 662)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_child_20260624-204836-run02.log`

- child extaddr: `b63ca4455c94e7a5`
- switch target extaddr(s): `a6f105ba968b73fe, a6f105ba968b73fe, a6f105ba968b73fe`

#### PCAP-complete child attach 1

- log parent request: `20:54:26.460`
- log parent response: `20:54:26.652`
- log child id request: `20:54:27.229`
- log child id response: `20:54:27.319`
- parent ipv6: `fe80:0:0:0:7cf7:8abe:9ee6:16b0`
- parent extaddr: `7ef78abe9ee616b0`
- parent rloc16: `0xe000`
- child extaddr: `b63ca4455c94e7a5`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **115 ms**
- Response -> Child ID Request: **606 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **791 ms**
- pcap parent request: `20:54:26.532` (frame 637)
- pcap parent response: `20:54:26.647` (frame 638)
- pcap child id request: `20:54:27.253` (frame 646)
- pcap child id response: `20:54:27.323` (frame 648)

#### PCAP-complete child attach 2

- log parent request: `20:54:57.480`
- log parent response: `20:54:58.073`
- log child id request: `20:54:58.362`
- log child id response: `20:54:58.452`
- parent ipv6: `fe80:0:0:0:a4f1:5ba:968b:73fe`
- parent extaddr: `a6f105ba968b73fe`
- parent rloc16: `0x6000`
- child extaddr: `b63ca4455c94e7a5`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **513 ms**
- Response -> Child ID Request: **322 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **897 ms**
- pcap parent request: `20:54:57.555` (frame 685)
- pcap parent response: `20:54:58.068` (frame 687)
- pcap child id request: `20:54:58.390` (frame 689)
- pcap child id response: `20:54:58.452` (frame 691)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_child_20260624-210058-run03.log`

- child extaddr: `fea497ecdf2e8125`
- switch target extaddr(s): `02307151eedf33ae, 02307151eedf33ae, 02307151eedf33ae`

#### PCAP-complete child attach 1

- log parent request: `21:06:49.148`
- log parent response: `21:06:49.250`
- log child id request: `21:06:49.868`
- log child id response: `21:06:49.959`
- parent ipv6: `fe80:0:0:0:240b:9aac:fc8c:fa37`
- parent extaddr: `260b9aacfc8cfa37`
- parent rloc16: `0x2400`
- child extaddr: `fea497ecdf2e8125`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **181 ms**
- Response -> Child ID Request: **567 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **818 ms**
- pcap parent request: `21:06:49.145` (frame 553)
- pcap parent response: `21:06:49.326` (frame 556)
- pcap child id request: `21:06:49.893` (frame 562)
- pcap child id response: `21:06:49.963` (frame 564)

#### PCAP-complete child attach 2

- log parent request: `21:07:20.157`
- log parent response: `21:07:20.469`
- log child id request: `21:07:20.754`
- log child id response: `21:07:20.843`
- parent ipv6: `fe80:0:0:0:30:7151:eedf:33ae`
- parent extaddr: `02307151eedf33ae`
- parent rloc16: `0x5800`
- child extaddr: `fea497ecdf2e8125`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **231 ms**
- Response -> Child ID Request: **319 ms**
- Child ID Request -> Response: **61 ms**
- Full Attach: **611 ms**
- pcap parent request: `21:07:20.233` (frame 583)
- pcap parent response: `21:07:20.464` (frame 585)
- pcap child id request: `21:07:20.783` (frame 587)
- pcap child id response: `21:07:20.844` (frame 589)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**
