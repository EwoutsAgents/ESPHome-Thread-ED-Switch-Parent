# Child Log Analysis

## stock_child

Files analyzed: **50**

### PCAP-complete child attach summary

| Attach | Metric | M (SD), ms | n |
| --- | --- | ---: | ---: |
| 1 | Request -> Response | 201.02 (108.00) | 50 |
| 1 | Response -> Child ID Request | 547.54 (107.13) | 50 |
| 1 | Child ID Request -> Response | 67.06 (5.06) | 50 |
| 1 | Full Attach | 815.62 (7.89) | 50 |
| 2 | Request -> Response | 239.68 (123.90) | 50 |
| 2 | Response -> Child ID Request | 510.94 (124.18) | 50 |
| 2 | Child ID Request -> Response | 67.86 (7.55) | 50 |
| 2 | Full Attach | 818.48 (7.91) | 50 |

| Metric | M (SD) | n |
| --- | ---: | ---: |
| Failed TX Attempts per Log | 64.00 (0.00) | 50 |
| Log-only or Partial Sequences per Log | 0.00 (0.00) | 50 |

### `stock_child_20260624-043057-run01.log`

- child extaddr: `e6deaf981b5dbb3e`

#### PCAP-complete child attach 1

- log parent request: `04:36:48.669`
- log parent response: `04:36:48.726`
- log child id request: `04:36:49.392`
- log child id response: `04:36:49.478`
- parent ipv6: `fe80:0:0:0:e0a4:d37e:e6c:63d`
- parent extaddr: `e2a4d37e0e6c063d`
- parent rloc16: `0xe000`
- child extaddr: `e6deaf981b5dbb3e`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **85 ms**
- Response -> Child ID Request: **665 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **813 ms**
- pcap parent request: `04:36:48.668` (frame 673)
- pcap parent response: `04:36:48.753` (frame 676)
- pcap child id request: `04:36:49.418` (frame 682)
- pcap child id response: `04:36:49.481` (frame 684)

#### PCAP-complete child attach 2

- log parent request: `04:40:49.150`
- log parent response: `04:40:49.274`
- log child id request: `04:40:49.872`
- log child id response: `04:40:49.966`
- parent ipv6: `fe80:0:0:0:c0a7:742e:2e04:1712`
- parent extaddr: `c2a7742e2e041712`
- parent rloc16: `0x2000`
- child extaddr: `e6deaf981b5dbb3e`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **534 ms**
- Response -> Child ID Request: **217 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **821 ms**
- pcap parent request: `04:40:49.156` (frame 1103)
- pcap parent response: `04:40:49.690` (frame 1108)
- pcap child id request: `04:40:49.907` (frame 1110)
- pcap child id response: `04:40:49.977` (frame 1112)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 193: 16, seq 194: 16, seq 195: 16, seq 196: 16
- failed tx by dst: `e2a4d37e0e6c063d`: 62

### `stock_child_20260624-044300-run02.log`

- child extaddr: `8ad07abb139c194b`

#### PCAP-complete child attach 1

- log parent request: `04:48:50.919`
- log parent response: `04:48:51.049`
- log child id request: `04:48:51.640`
- log child id response: `04:48:51.726`
- parent ipv6: `fe80:0:0:0:7830:d6b6:5732:7a76`
- parent extaddr: `7a30d6b657327a76`
- parent rloc16: `0x4800`
- child extaddr: `8ad07abb139c194b`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **128 ms**
- Response -> Child ID Request: **621 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **811 ms**
- pcap parent request: `04:48:50.917` (frame 552)
- pcap parent response: `04:48:51.045` (frame 554)
- pcap child id request: `04:48:51.666` (frame 562)
- pcap child id response: `04:48:51.728` (frame 564)

#### PCAP-complete child attach 2

- log parent request: `04:52:51.464`
- log parent response: `04:52:51.511`
- log child id request: `04:52:52.184`
- log child id response: `04:52:52.280`
- parent ipv6: `fe80:0:0:0:ac43:d358:6626:77d6`
- parent extaddr: `ae43d358662677d6`
- parent rloc16: `0xec00`
- child extaddr: `8ad07abb139c194b`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **46 ms**
- Response -> Child ID Request: **706 ms**
- Child ID Request -> Response: **72 ms**
- Full Attach: **824 ms**
- pcap parent request: `04:52:51.469` (frame 1732)
- pcap parent response: `04:52:51.515` (frame 1733)
- pcap child id request: `04:52:52.221` (frame 1739)
- pcap child id response: `04:52:52.293` (frame 1741)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 171: 16, seq 172: 16, seq 173: 16, seq 174: 16
- failed tx by dst: `7a30d6b657327a76`: 63

### `stock_child_20260624-045502-run03.log`

- child extaddr: `9ab23f2e55385190`

#### PCAP-complete child attach 1

- log parent request: `05:00:53.071`
- log parent response: `05:00:53.266`
- log child id request: `05:00:53.838`
- log child id response: `05:00:53.931`
- parent ipv6: `fe80:0:0:0:4012:8a54:8736:7b9`
- parent extaddr: `42128a54873607b9`
- parent rloc16: `0x0800`
- child extaddr: `9ab23f2e55385190`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **306 ms**
- Response -> Child ID Request: **446 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **822 ms**
- pcap parent request: `05:00:53.113` (frame 681)
- pcap parent response: `05:00:53.419` (frame 684)
- pcap child id request: `05:00:53.865` (frame 690)
- pcap child id response: `05:00:53.935` (frame 692)

#### PCAP-complete child attach 2

- log parent request: `05:04:54.098`
- log parent response: `05:04:54.260`
- log child id request: `05:04:54.816`
- log child id response: `05:04:54.905`
- parent ipv6: `fe80:0:0:0:94ac:1915:ccd4:5348`
- parent extaddr: `96ac1915ccd45348`
- parent rloc16: `0x0400`
- child extaddr: `9ab23f2e55385190`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **161 ms**
- Response -> Child ID Request: **591 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **815 ms**
- pcap parent request: `05:04:54.099` (frame 986)
- pcap parent response: `05:04:54.260` (frame 987)
- pcap child id request: `05:04:54.851` (frame 993)
- pcap child id response: `05:04:54.914` (frame 995)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 133: 16, seq 134: 16, seq 135: 16, seq 136: 16
- failed tx by dst: `42128a54873607b9`: 63

### `stock_child_20260624-050704-run04.log`

- child extaddr: `0a11f511fd3aeccd`

#### PCAP-complete child attach 1

- log parent request: `05:12:55.583`
- log parent response: `05:12:55.786`
- log child id request: `05:12:56.352`
- log child id response: `05:12:56.439`
- parent ipv6: `fe80:0:0:0:9850:52fe:3e1a:2453`
- parent extaddr: `9a5052fe3e1a2453`
- parent rloc16: `0xc400`
- child extaddr: `0a11f511fd3aeccd`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **153 ms**
- Response -> Child ID Request: **597 ms**
- Child ID Request -> Response: **66 ms**
- Full Attach: **816 ms**
- pcap parent request: `05:12:55.626` (frame 600)
- pcap parent response: `05:12:55.779` (frame 601)
- pcap child id request: `05:12:56.376` (frame 618)
- pcap child id response: `05:12:56.442` (frame 623)

#### PCAP-complete child attach 2

- log parent request: `05:16:56.196`
- log parent response: `05:16:56.347`
- log child id request: `05:16:56.918`
- log child id response: `05:16:57.012`
- parent ipv6: `fe80:0:0:0:7ccc:a174:c93f:417d`
- parent extaddr: `7ecca174c93f417d`
- parent rloc16: `0x2c00`
- child extaddr: `0a11f511fd3aeccd`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **151 ms**
- Response -> Child ID Request: **600 ms**
- Child ID Request -> Response: **72 ms**
- Full Attach: **823 ms**
- pcap parent request: `05:16:56.200` (frame 1209)
- pcap parent response: `05:16:56.351` (frame 1210)
- pcap child id request: `05:16:56.951` (frame 1216)
- pcap child id response: `05:16:57.023` (frame 1218)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 218: 16, seq 219: 16, seq 220: 16, seq 221: 16
- failed tx by dst: `9a5052fe3e1a2453`: 64

### `stock_child_20260624-051907-run05.log`

- child extaddr: `0eb848177e008c43`

#### PCAP-complete child attach 1

- log parent request: `05:24:57.736`
- log parent response: `05:24:57.998`
- log child id request: `05:24:58.506`
- log child id response: `05:24:58.590`
- parent ipv6: `fe80:0:0:0:3c34:f971:6da6:6a5e`
- parent extaddr: `3e34f9716da66a5e`
- parent rloc16: `0xac00`
- child extaddr: `0eb848177e008c43`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **384 ms**
- Response -> Child ID Request: **364 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **810 ms**
- pcap parent request: `05:24:57.782` (frame 619)
- pcap parent response: `05:24:58.166` (frame 624)
- pcap child id request: `05:24:58.530` (frame 629)
- pcap child id response: `05:24:58.592` (frame 631)

#### PCAP-complete child attach 2

- log parent request: `05:28:58.170`
- log parent response: `05:28:58.217`
- log child id request: `05:28:58.892`
- log child id response: `05:28:58.982`
- parent ipv6: `fe80:0:0:0:50e0:bedc:cd94:d9e7`
- parent extaddr: `52e0bedccd94d9e7`
- parent rloc16: `0xc400`
- child extaddr: `0eb848177e008c43`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **450 ms**
- Response -> Child ID Request: **300 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **820 ms**
- pcap parent request: `05:28:58.174` (frame 1228)
- pcap parent response: `05:28:58.624` (frame 1233)
- pcap child id request: `05:28:58.924` (frame 1235)
- pcap child id response: `05:28:58.994` (frame 1237)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 11: 16, seq 12: 16, seq 13: 16, seq 14: 16
- failed tx by dst: `3e34f9716da66a5e`: 64

### `stock_child_20260624-053109-run06.log`

- child extaddr: `425952199c7e9087`

#### PCAP-complete child attach 1

- log parent request: `05:37:00.403`
- log parent response: `05:37:00.622`
- log child id request: `05:37:01.124`
- log child id response: `05:37:01.217`
- parent ipv6: `fe80:0:0:0:3c0c:9bcd:b814:76b6`
- parent extaddr: `3e0c9bcdb81476b6`
- parent rloc16: `0x1400`
- child extaddr: `425952199c7e9087`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **220 ms**
- Response -> Child ID Request: **532 ms**
- Child ID Request -> Response: **71 ms**
- Full Attach: **823 ms**
- pcap parent request: `05:37:00.396` (frame 535)
- pcap parent response: `05:37:00.616` (frame 536)
- pcap child id request: `05:37:01.148` (frame 544)
- pcap child id response: `05:37:01.219` (frame 546)

#### PCAP-complete child attach 2

- log parent request: `05:41:01.174`
- log parent response: `05:41:01.313`
- log child id request: `05:41:01.892`
- log child id response: `05:41:01.980`
- parent ipv6: `fe80:0:0:0:cc27:50b8:45e1:a6e`
- parent extaddr: `ce2750b845e10a6e`
- parent rloc16: `0xf800`
- child extaddr: `425952199c7e9087`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **138 ms**
- Response -> Child ID Request: **614 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **815 ms**
- pcap parent request: `05:41:01.172` (frame 868)
- pcap parent response: `05:41:01.310` (frame 869)
- pcap child id request: `05:41:01.924` (frame 876)
- pcap child id response: `05:41:01.987` (frame 878)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 13: 16, seq 14: 16, seq 15: 16, seq 16: 16
- failed tx by dst: `3e0c9bcdb81476b6`: 61

### `stock_child_20260624-054312-run07.log`

- child extaddr: `86da52881a5dbb53`

#### PCAP-complete child attach 1

- log parent request: `05:49:02.474`
- log parent response: `05:49:02.617`
- log child id request: `05:49:03.242`
- log child id response: `05:49:03.341`
- parent ipv6: `fe80:0:0:0:8c65:b76a:a45a:ae53`
- parent extaddr: `8e65b76aa45aae53`
- parent rloc16: `0x8400`
- child extaddr: `86da52881a5dbb53`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **65 ms**
- Response -> Child ID Request: **657 ms**
- Child ID Request -> Response: **72 ms**
- Full Attach: **794 ms**
- pcap parent request: `05:49:02.545` (frame 682)
- pcap parent response: `05:49:02.610` (frame 683)
- pcap child id request: `05:49:03.267` (frame 691)
- pcap child id response: `05:49:03.339` (frame 693)

#### PCAP-complete child attach 2

- log parent request: `05:53:03.259`
- log parent response: `05:53:03.483`
- log child id request: `05:53:03.976`
- log child id response: `05:53:04.066`
- parent ipv6: `fe80:0:0:0:90ad:157b:9f14:54b5`
- parent extaddr: `92ad157b9f1454b5`
- parent rloc16: `0x2800`
- child extaddr: `86da52881a5dbb53`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **221 ms**
- Response -> Child ID Request: **529 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **814 ms**
- pcap parent request: `05:53:03.260` (frame 1007)
- pcap parent response: `05:53:03.481` (frame 1008)
- pcap child id request: `05:53:04.010` (frame 1014)
- pcap child id response: `05:53:04.074` (frame 1016)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 29: 16, seq 30: 16, seq 31: 16, seq 32: 16
- failed tx by dst: `8e65b76aa45aae53`: 62

### `stock_child_20260624-055514-run08.log`

- child extaddr: `121a4eb40344c017`

#### PCAP-complete child attach 1

- log parent request: `06:01:05.251`
- log parent response: `06:01:05.421`
- log child id request: `06:01:05.971`
- log child id response: `06:01:06.063`
- parent ipv6: `fe80:0:0:0:6ca4:5e4e:e3e7:ce9a`
- parent extaddr: `6ea45e4ee3e7ce9a`
- parent rloc16: `0xb400`
- child extaddr: `121a4eb40344c017`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **180 ms**
- Response -> Child ID Request: **570 ms**
- Child ID Request -> Response: **71 ms**
- Full Attach: **821 ms**
- pcap parent request: `06:01:05.246` (frame 633)
- pcap parent response: `06:01:05.426` (frame 636)
- pcap child id request: `06:01:05.996` (frame 642)
- pcap child id response: `06:01:06.067` (frame 644)

#### PCAP-complete child attach 2

- log parent request: `06:05:06.057`
- log parent response: `06:05:06.326`
- log child id request: `06:05:06.775`
- log child id response: `06:05:06.861`
- parent ipv6: `fe80:0:0:0:883f:dcab:c4c5:49aa`
- parent extaddr: `8a3fdcabc4c549aa`
- parent rloc16: `0xf000`
- child extaddr: `121a4eb40344c017`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **268 ms**
- Response -> Child ID Request: **481 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **811 ms**
- pcap parent request: `06:05:06.058` (frame 975)
- pcap parent response: `06:05:06.326` (frame 976)
- pcap child id request: `06:05:06.807` (frame 982)
- pcap child id response: `06:05:06.869` (frame 984)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 190: 16, seq 191: 16, seq 192: 16, seq 193: 16
- failed tx by dst: `6ea45e4ee3e7ce9a`: 62

### `stock_child_20260624-060716-run09.log`

- child extaddr: `eab01e9d25c8cf0e`

#### PCAP-complete child attach 1

- log parent request: `06:13:07.521`
- log parent response: `06:13:07.651`
- log child id request: `06:13:08.351`
- log child id response: `06:13:08.400`
- parent ipv6: `fe80:0:0:0:f8cf:f397:fea3:76ed`
- parent extaddr: `facff397fea376ed`
- parent rloc16: `0xd800`
- child extaddr: `eab01e9d25c8cf0e`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **81 ms**
- Response -> Child ID Request: **670 ms**
- Child ID Request -> Response: **87 ms**
- Full Attach: **838 ms**
- pcap parent request: `06:13:07.565` (frame 614)
- pcap parent response: `06:13:07.646` (frame 615)
- pcap child id request: `06:13:08.316` (frame 624)
- pcap child id response: `06:13:08.403` (frame 626)

#### PCAP-complete child attach 2

- log parent request: `06:17:08.455`
- log parent response: `06:17:08.594`
- log child id request: `06:17:09.176`
- log child id response: `06:17:09.268`
- parent ipv6: `fe80:0:0:0:9453:3945:86e8:e914`
- parent extaddr: `9653394586e8e914`
- parent rloc16: `0x8800`
- child extaddr: `eab01e9d25c8cf0e`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **146 ms**
- Response -> Child ID Request: **603 ms**
- Child ID Request -> Response: **71 ms**
- Full Attach: **820 ms**
- pcap parent request: `06:17:08.461` (frame 1335)
- pcap parent response: `06:17:08.607` (frame 1338)
- pcap child id request: `06:17:09.210` (frame 1342)
- pcap child id response: `06:17:09.281` (frame 1344)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 31: 16, seq 32: 16, seq 33: 16, seq 34: 16
- failed tx by dst: `facff397fea376ed`: 63

### `stock_child_20260624-061919-run10.log`

- child extaddr: `02b19179afc2595d`

#### PCAP-complete child attach 1

- log parent request: `06:25:09.587`
- log parent response: `06:25:09.706`
- log child id request: `06:25:10.355`
- log child id response: `06:25:10.447`
- parent ipv6: `fe80:0:0:0:34a9:5d72:e6eb:b38`
- parent extaddr: `36a95d72e6eb0b38`
- parent rloc16: `0xd400`
- child extaddr: `02b19179afc2595d`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **131 ms**
- Response -> Child ID Request: **618 ms**
- Child ID Request -> Response: **71 ms**
- Full Attach: **820 ms**
- pcap parent request: `06:25:09.632` (frame 545)
- pcap parent response: `06:25:09.763` (frame 548)
- pcap child id request: `06:25:10.381` (frame 554)
- pcap child id response: `06:25:10.452` (frame 556)

#### PCAP-complete child attach 2

- log parent request: `06:29:10.657`
- log parent response: `06:29:10.824`
- log child id request: `06:29:11.376`
- log child id response: `06:29:11.464`
- parent ipv6: `fe80:0:0:0:647d:7345:9695:6997`
- parent extaddr: `667d734596956997`
- parent rloc16: `0xb400`
- child extaddr: `02b19179afc2595d`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **324 ms**
- Response -> Child ID Request: **425 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **813 ms**
- pcap parent request: `06:29:10.660` (frame 875)
- pcap parent response: `06:29:10.984` (frame 878)
- pcap child id request: `06:29:11.409` (frame 882)
- pcap child id response: `06:29:11.473` (frame 884)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 176: 16, seq 177: 16, seq 178: 16, seq 179: 16
- failed tx by dst: `36a95d72e6eb0b38`: 64

### `stock_child_20260624-063121-run11.log`

- child extaddr: `6ab4c12502485a87`

#### PCAP-complete child attach 1

- log parent request: `06:37:12.062`
- log parent response: `06:37:12.313`
- log child id request: `06:37:12.829`
- log child id response: `06:37:12.914`
- parent ipv6: `fe80:0:0:0:824:4f2c:126:6474`
- parent extaddr: `0a244f2c01266474`
- parent rloc16: `0xb400`
- child extaddr: `6ab4c12502485a87`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **212 ms**
- Response -> Child ID Request: **540 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **814 ms**
- pcap parent request: `06:37:12.103` (frame 636)
- pcap parent response: `06:37:12.315` (frame 639)
- pcap child id request: `06:37:12.855` (frame 645)
- pcap child id response: `06:37:12.917` (frame 647)

#### PCAP-complete child attach 2

- log parent request: `06:41:12.814`
- log parent response: `06:41:13.045`
- log child id request: `06:41:13.535`
- log child id response: `06:41:13.645`
- parent ipv6: `fe80:0:0:0:404f:1d6a:6359:ee3e`
- parent extaddr: `424f1d6a6359ee3e`
- parent rloc16: `0xa400`
- child extaddr: `6ab4c12502485a87`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **231 ms**
- Response -> Child ID Request: **540 ms**
- Child ID Request -> Response: **67 ms**
- Full Attach: **838 ms**
- pcap parent request: `06:41:12.818` (frame 1260)
- pcap parent response: `06:41:13.049` (frame 1261)
- pcap child id request: `06:41:13.589` (frame 1268)
- pcap child id response: `06:41:13.656` (frame 1270)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 157: 16, seq 158: 16, seq 159: 16, seq 160: 16
- failed tx by dst: `0a244f2c01266474`: 64

### `stock_child_20260624-064323-run12.log`

- child extaddr: `f2ba628fcad0b409`

#### PCAP-complete child attach 1

- log parent request: `06:49:14.327`
- log parent response: `06:49:14.384`
- log child id request: `06:49:15.045`
- log child id response: `06:49:15.137`
- parent ipv6: `fe80:0:0:0:40c:823d:acf:962a`
- parent extaddr: `060c823d0acf962a`
- parent rloc16: `0x3000`
- child extaddr: `f2ba628fcad0b409`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **60 ms**
- Response -> Child ID Request: **690 ms**
- Child ID Request -> Response: **71 ms**
- Full Attach: **821 ms**
- pcap parent request: `06:49:14.319` (frame 673)
- pcap parent response: `06:49:14.379` (frame 674)
- pcap child id request: `06:49:15.069` (frame 682)
- pcap child id response: `06:49:15.140` (frame 684)

#### PCAP-complete child attach 2

- log parent request: `06:53:15.059`
- log parent response: `06:53:15.171`
- log child id request: `06:53:15.832`
- log child id response: `06:53:15.919`
- parent ipv6: `fe80:0:0:0:c82b:c9fd:68b2:33ff`
- parent extaddr: `ca2bc9fd68b233ff`
- parent rloc16: `0x2800`
- child extaddr: `f2ba628fcad0b409`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **239 ms**
- Response -> Child ID Request: **512 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **814 ms**
- pcap parent request: `06:53:15.112` (frame 982)
- pcap parent response: `06:53:15.351` (frame 985)
- pcap child id request: `06:53:15.863` (frame 989)
- pcap child id response: `06:53:15.926` (frame 991)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 208: 16, seq 209: 16, seq 210: 16, seq 211: 16
- failed tx by dst: `060c823d0acf962a`: 59

### `stock_child_20260624-065526-run13.log`

- child extaddr: `fe139801f77600ae`

#### PCAP-complete child attach 1

- log parent request: `07:01:17.062`
- log parent response: `07:01:17.194`
- log child id request: `07:01:17.781`
- log child id response: `07:01:17.875`
- parent ipv6: `fe80:0:0:0:4c5:4357:b813:83ec`
- parent extaddr: `06c54357b81383ec`
- parent rloc16: `0x5c00`
- child extaddr: `fe139801f77600ae`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **182 ms**
- Response -> Child ID Request: **568 ms**
- Child ID Request -> Response: **71 ms**
- Full Attach: **821 ms**
- pcap parent request: `07:01:17.058` (frame 553)
- pcap parent response: `07:01:17.240` (frame 556)
- pcap child id request: `07:01:17.808` (frame 562)
- pcap child id response: `07:01:17.879` (frame 564)

#### PCAP-complete child attach 2

- log parent request: `07:05:17.908`
- log parent response: `07:05:18.042`
- log child id request: `07:05:18.596`
- log child id response: `07:05:18.682`
- parent ipv6: `fe80:0:0:0:8c43:59c6:859c:8762`
- parent extaddr: `8e4359c6859c8762`
- parent rloc16: `0x9800`
- child extaddr: `fe139801f77600ae`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **163 ms**
- Response -> Child ID Request: **586 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **812 ms**
- pcap parent request: `07:05:17.880` (frame 864)
- pcap parent response: `07:05:18.043` (frame 865)
- pcap child id request: `07:05:18.629` (frame 872)
- pcap child id response: `07:05:18.692` (frame 874)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 26: 16, seq 27: 16, seq 28: 16, seq 29: 16
- failed tx by dst: `06c54357b81383ec`: 62

### `stock_child_20260624-070728-run14.log`

- child extaddr: `6e69f6f182f357ad`

#### PCAP-complete child attach 1

- log parent request: `07:13:19.443`
- log parent response: `07:13:19.537`
- log child id request: `07:13:20.162`
- log child id response: `07:13:20.247`
- parent ipv6: `fe80:0:0:0:c8ab:aa21:ac4c:2ff1`
- parent extaddr: `caabaa21ac4c2ff1`
- parent rloc16: `0xb400`
- child extaddr: `6e69f6f182f357ad`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **158 ms**
- Response -> Child ID Request: **591 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **811 ms**
- pcap parent request: `07:13:19.438` (frame 631)
- pcap parent response: `07:13:19.596` (frame 634)
- pcap child id request: `07:13:20.187` (frame 640)
- pcap child id response: `07:13:20.249` (frame 642)

#### PCAP-complete child attach 2

- log parent request: `07:17:19.987`
- log parent response: `07:17:20.158`
- log child id request: `07:17:20.708`
- log child id response: `07:17:20.803`
- parent ipv6: `fe80:0:0:0:1039:23c4:ee98:86fc`
- parent extaddr: `123923c4ee9886fc`
- parent rloc16: `0xf800`
- child extaddr: `6e69f6f182f357ad`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **181 ms**
- Response -> Child ID Request: **570 ms**
- Child ID Request -> Response: **71 ms**
- Full Attach: **822 ms**
- pcap parent request: `07:17:19.992` (frame 1256)
- pcap parent response: `07:17:20.173` (frame 1265)
- pcap child id request: `07:17:20.743` (frame 1279)
- pcap child id response: `07:17:20.814` (frame 1281)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 168: 16, seq 169: 16, seq 170: 16, seq 171: 16
- failed tx by dst: `caabaa21ac4c2ff1`: 63

### `stock_child_20260624-071930-run15.log`

- child extaddr: `0e44e705203b4c1e`

#### PCAP-complete child attach 1

- log parent request: `07:25:21.608`
- log parent response: `07:25:21.748`
- log child id request: `07:25:22.328`
- log child id response: `07:25:22.413`
- parent ipv6: `fe80:0:0:0:68bf:8dab:afbb:68c1`
- parent extaddr: `6abf8dabafbb68c1`
- parent rloc16: `0x1000`
- child extaddr: `0e44e705203b4c1e`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **241 ms**
- Response -> Child ID Request: **511 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **814 ms**
- pcap parent request: `07:25:21.602` (frame 620)
- pcap parent response: `07:25:21.843` (frame 626)
- pcap child id request: `07:25:22.354` (frame 630)
- pcap child id response: `07:25:22.416` (frame 632)

#### PCAP-complete child attach 2

- log parent request: `07:29:22.540`
- log parent response: `07:29:22.767`
- log child id request: `07:29:23.262`
- log child id response: `07:29:23.353`
- parent ipv6: `fe80:0:0:0:889e:16cf:edac:82a0`
- parent extaddr: `8a9e16cfedac82a0`
- parent rloc16: `0x9000`
- child extaddr: `0e44e705203b4c1e`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **286 ms**
- Response -> Child ID Request: **464 ms**
- Child ID Request -> Response: **71 ms**
- Full Attach: **821 ms**
- pcap parent request: `07:29:22.545` (frame 1067)
- pcap parent response: `07:29:22.831` (frame 1072)
- pcap child id request: `07:29:23.295` (frame 1074)
- pcap child id response: `07:29:23.366` (frame 1076)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 104: 16, seq 105: 16, seq 106: 16, seq 107: 16
- failed tx by dst: `6abf8dabafbb68c1`: 62

### `stock_child_20260624-073133-run16.log`

- child extaddr: `36b6e412b5afd90c`

#### PCAP-complete child attach 1

- log parent request: `07:37:23.721`
- log parent response: `07:37:23.924`
- log child id request: `07:37:24.489`
- log child id response: `07:37:24.574`
- parent ipv6: `fe80:0:0:0:d8a3:97b:7a3a:7f19`
- parent extaddr: `daa3097b7a3a7f19`
- parent rloc16: `0xec00`
- child extaddr: `36b6e412b5afd90c`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **155 ms**
- Response -> Child ID Request: **597 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **814 ms**
- pcap parent request: `07:37:23.763` (frame 564)
- pcap parent response: `07:37:23.918` (frame 565)
- pcap child id request: `07:37:24.515` (frame 573)
- pcap child id response: `07:37:24.577` (frame 575)

#### PCAP-complete child attach 2

- log parent request: `07:41:24.239`
- log parent response: `07:41:24.442`
- log child id request: `07:41:24.960`
- log child id response: `07:41:25.056`
- parent ipv6: `fe80:0:0:0:34c6:509f:5037:35d2`
- parent extaddr: `36c6509f503735d2`
- parent rloc16: `0xc800`
- child extaddr: `36b6e412b5afd90c`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **200 ms**
- Response -> Child ID Request: **548 ms**
- Child ID Request -> Response: **74 ms**
- Full Attach: **822 ms**
- pcap parent request: `07:41:24.245` (frame 1172)
- pcap parent response: `07:41:24.445` (frame 1174)
- pcap child id request: `07:41:24.993` (frame 1180)
- pcap child id response: `07:41:25.067` (frame 1182)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 72: 16, seq 73: 16, seq 74: 16, seq 75: 16
- failed tx by dst: `daa3097b7a3a7f19`: 64

### `stock_child_20260624-074335-run17.log`

- child extaddr: `bedf4ecfaac24399`

#### PCAP-complete child attach 1

- log parent request: `07:49:26.129`
- log parent response: `07:49:26.350`
- log child id request: `07:49:26.936`
- log child id response: `07:49:26.983`
- parent ipv6: `fe80:0:0:0:185b:8845:433b:b895`
- parent extaddr: `1a5b8845433bb895`
- parent rloc16: `0xa800`
- child extaddr: `bedf4ecfaac24399`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **225 ms**
- Response -> Child ID Request: **522 ms**
- Child ID Request -> Response: **61 ms**
- Full Attach: **808 ms**
- pcap parent request: `07:49:26.177` (frame 505)
- pcap parent response: `07:49:26.402` (frame 508)
- pcap child id request: `07:49:26.924` (frame 514)
- pcap child id response: `07:49:26.985` (frame 516)

#### PCAP-complete child attach 2

- log parent request: `07:53:26.556`
- log parent response: `07:53:26.666`
- log child id request: `07:53:27.325`
- log child id response: `07:53:27.420`
- parent ipv6: `fe80:0:0:0:f02e:2b8e:7dbc:22c9`
- parent extaddr: `f22e2b8e7dbc22c9`
- parent rloc16: `0x2400`
- child extaddr: `bedf4ecfaac24399`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **61 ms**
- Response -> Child ID Request: **691 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **822 ms**
- pcap parent request: `07:53:26.609` (frame 1116)
- pcap parent response: `07:53:26.670` (frame 1117)
- pcap child id request: `07:53:27.361` (frame 1123)
- pcap child id response: `07:53:27.431` (frame 1125)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 248: 16, seq 249: 16, seq 250: 16, seq 251: 16
- failed tx by dst: `1a5b8845433bb895`: 64

### `stock_child_20260624-075538-run18.log`

- child extaddr: `a2206c1a14123f40`

#### PCAP-complete child attach 1

- log parent request: `08:01:28.944`
- log parent response: `08:01:29.316`
- log child id request: `08:01:29.711`
- log child id response: `08:01:29.802`
- parent ipv6: `fe80:0:0:0:9040:468:380:193b`
- parent extaddr: `924004680380193b`
- parent rloc16: `0xe800`
- child extaddr: `a2206c1a14123f40`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **325 ms**
- Response -> Child ID Request: **425 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **820 ms**
- pcap parent request: `08:01:28.985` (frame 497)
- pcap parent response: `08:01:29.310` (frame 498)
- pcap child id request: `08:01:29.735` (frame 506)
- pcap child id response: `08:01:29.805` (frame 508)

#### PCAP-complete child attach 2

- log parent request: `08:05:29.891`
- log parent response: `08:05:30.002`
- log child id request: `08:05:30.663`
- log child id response: `08:05:30.751`
- parent ipv6: `fe80:0:0:0:f8bf:62e1:1733:dc86`
- parent extaddr: `fabf62e11733dc86`
- parent rloc16: `0xd800`
- child extaddr: `a2206c1a14123f40`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **239 ms**
- Response -> Child ID Request: **511 ms**
- Child ID Request -> Response: **65 ms**
- Full Attach: **815 ms**
- pcap parent request: `08:05:29.944` (frame 790)
- pcap parent response: `08:05:30.183` (frame 793)
- pcap child id request: `08:05:30.694` (frame 797)
- pcap child id response: `08:05:30.759` (frame 799)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 0: 16, seq 1: 16, seq 254: 16, seq 255: 16
- failed tx by dst: `924004680380193b`: 63

### `stock_child_20260624-080740-run19.log`

- child extaddr: `ca7d04c414e3857a`

#### PCAP-complete child attach 1

- log parent request: `08:13:31.873`
- log parent response: `08:13:31.924`
- log child id request: `08:13:32.633`
- log child id response: `08:13:32.683`
- parent ipv6: `fe80:0:0:0:145b:978c:924e:35bc`
- parent extaddr: `165b978c924e35bc`
- parent rloc16: `0x0400`
- child extaddr: `ca7d04c414e3857a`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **180 ms**
- Response -> Child ID Request: **575 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **817 ms**
- pcap parent request: `08:13:31.868` (frame 516)
- pcap parent response: `08:13:32.048` (frame 519)
- pcap child id request: `08:13:32.623` (frame 526)
- pcap child id response: `08:13:32.685` (frame 528)

#### PCAP-complete child attach 2

- log parent request: `08:17:32.781`
- log parent response: `08:17:32.946`
- log child id request: `08:17:33.504`
- log child id response: `08:17:33.596`
- parent ipv6: `fe80:0:0:0:4476:6f42:7693:416f`
- parent extaddr: `46766f427693416f`
- parent rloc16: `0xbc00`
- child extaddr: `ca7d04c414e3857a`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **191 ms**
- Response -> Child ID Request: **559 ms**
- Child ID Request -> Response: **71 ms**
- Full Attach: **821 ms**
- pcap parent request: `08:17:32.788` (frame 961)
- pcap parent response: `08:17:32.979` (frame 964)
- pcap child id request: `08:17:33.538` (frame 968)
- pcap child id response: `08:17:33.609` (frame 970)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 127: 16, seq 128: 16, seq 129: 16, seq 130: 16
- failed tx by dst: `165b978c924e35bc`: 64

### `stock_child_20260624-081943-run20.log`

- child extaddr: `4a8f583d8c038420`

#### PCAP-complete child attach 1

- log parent request: `08:25:33.997`
- log parent response: `08:25:34.095`
- log child id request: `08:25:34.766`
- log child id response: `08:25:34.858`
- parent ipv6: `fe80:0:0:0:7cb2:29f1:1c91:6813`
- parent extaddr: `7eb229f11c916813`
- parent rloc16: `0x1800`
- child extaddr: `4a8f583d8c038420`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **148 ms**
- Response -> Child ID Request: **603 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **821 ms**
- pcap parent request: `08:25:34.040` (frame 675)
- pcap parent response: `08:25:34.188` (frame 680)
- pcap child id request: `08:25:34.791` (frame 684)
- pcap child id response: `08:25:34.861` (frame 686)

#### PCAP-complete child attach 2

- log parent request: `08:29:34.721`
- log parent response: `08:29:34.809`
- log child id request: `08:29:35.440`
- log child id response: `08:29:35.527`
- parent ipv6: `fe80:0:0:0:34d6:a26f:9995:1744`
- parent extaddr: `36d6a26f99951744`
- parent rloc16: `0x4400`
- child extaddr: `4a8f583d8c038420`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **245 ms**
- Response -> Child ID Request: **506 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **813 ms**
- pcap parent request: `08:29:34.723` (frame 1013)
- pcap parent response: `08:29:34.968` (frame 1016)
- pcap child id request: `08:29:35.474` (frame 1020)
- pcap child id response: `08:29:35.536` (frame 1022)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 25: 16, seq 26: 16, seq 27: 16, seq 28: 16
- failed tx by dst: `7eb229f11c916813`: 61

### `stock_child_20260624-083145-run21.log`

- child extaddr: `beaa8f8273f01331`

#### PCAP-complete child attach 1

- log parent request: `08:37:36.338`
- log parent response: `08:37:36.387`
- log child id request: `08:37:37.058`
- log child id response: `08:37:37.150`
- parent ipv6: `fe80:0:0:0:b489:93f2:e481:56e2`
- parent extaddr: `b68993f2e48156e2`
- parent rloc16: `0x0c00`
- child extaddr: `beaa8f8273f01331`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **348 ms**
- Response -> Child ID Request: **402 ms**
- Child ID Request -> Response: **69 ms**
- Full Attach: **819 ms**
- pcap parent request: `08:37:36.334` (frame 583)
- pcap parent response: `08:37:36.682` (frame 589)
- pcap child id request: `08:37:37.084` (frame 609)
- pcap child id response: `08:37:37.153` (frame 611)

#### PCAP-complete child attach 2

- log parent request: `08:41:37.394`
- log parent response: `08:41:37.495`
- log child id request: `08:41:38.115`
- log child id response: `08:41:38.206`
- parent ipv6: `fe80:0:0:0:b4b0:1800:8a5f:1b0b`
- parent extaddr: `b6b018008a5f1b0b`
- parent rloc16: `0x9800`
- child extaddr: `beaa8f8273f01331`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **363 ms**
- Response -> Child ID Request: **387 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **820 ms**
- pcap parent request: `08:41:37.398` (frame 1190)
- pcap parent response: `08:41:37.761` (frame 1196)
- pcap child id request: `08:41:38.148` (frame 1198)
- pcap child id response: `08:41:38.218` (frame 1200)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 153: 16, seq 154: 16, seq 155: 16, seq 156: 16
- failed tx by dst: `b68993f2e48156e2`: 64

### `stock_child_20260624-084348-run22.log`

- child extaddr: `4afa7ae640c0c68a`

#### PCAP-complete child attach 1

- log parent request: `08:49:38.879`
- log parent response: `08:49:39.063`
- log child id request: `08:49:39.648`
- log child id response: `08:49:39.738`
- parent ipv6: `fe80:0:0:0:6c1e:2758:1ce1:57d2`
- parent extaddr: `6e1e27581ce157d2`
- parent rloc16: `0x7c00`
- child extaddr: `4afa7ae640c0c68a`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **137 ms**
- Response -> Child ID Request: **613 ms**
- Child ID Request -> Response: **71 ms**
- Full Attach: **821 ms**
- pcap parent request: `08:49:38.921` (frame 570)
- pcap parent response: `08:49:39.058` (frame 571)
- pcap child id request: `08:49:39.671` (frame 579)
- pcap child id response: `08:49:39.742` (frame 581)

#### PCAP-complete child attach 2

- log parent request: `08:53:39.900`
- log parent response: `08:53:39.990`
- log child id request: `08:53:40.618`
- log child id response: `08:53:40.707`
- parent ipv6: `fe80:0:0:0:70c2:244c:ef38:1286`
- parent extaddr: `72c2244cef381286`
- parent rloc16: `0x9000`
- child extaddr: `4afa7ae640c0c68a`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **88 ms**
- Response -> Child ID Request: **662 ms**
- Child ID Request -> Response: **65 ms**
- Full Attach: **815 ms**
- pcap parent request: `08:53:39.901` (frame 879)
- pcap parent response: `08:53:39.989` (frame 880)
- pcap child id request: `08:53:40.651` (frame 886)
- pcap child id response: `08:53:40.716` (frame 888)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 235: 16, seq 236: 16, seq 237: 16, seq 238: 16
- failed tx by dst: `6e1e27581ce157d2`: 62

### `stock_child_20260624-085550-run23.log`

- child extaddr: `2e97462751460132`

#### PCAP-complete child attach 1

- log parent request: `09:01:41.413`
- log parent response: `09:01:41.629`
- log child id request: `09:01:42.133`
- log child id response: `09:01:42.225`
- parent ipv6: `fe80:0:0:0:2840:7368:3f66:807f`
- parent extaddr: `2a4073683f66807f`
- parent rloc16: `0x3800`
- child extaddr: `2e97462751460132`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **362 ms**
- Response -> Child ID Request: **387 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **819 ms**
- pcap parent request: `09:01:41.409` (frame 643)
- pcap parent response: `09:01:41.771` (frame 649)
- pcap child id request: `09:01:42.158` (frame 653)
- pcap child id response: `09:01:42.228` (frame 655)

#### PCAP-complete child attach 2

- log parent request: `09:05:42.377`
- log parent response: `09:05:42.627`
- log child id request: `09:05:43.095`
- log child id response: `09:05:43.183`
- parent ipv6: `fe80:0:0:0:8087:fcc0:c8eb:363d`
- parent extaddr: `8287fcc0c8eb363d`
- parent rloc16: `0x8000`
- child extaddr: `2e97462751460132`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **351 ms**
- Response -> Child ID Request: **397 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **812 ms**
- pcap parent request: `09:05:42.379` (frame 950)
- pcap parent response: `09:05:42.730` (frame 953)
- pcap child id request: `09:05:43.127` (frame 957)
- pcap child id response: `09:05:43.191` (frame 959)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 75: 16, seq 76: 16, seq 77: 16, seq 78: 16
- failed tx by dst: `2a4073683f66807f`: 62

### `stock_child_20260624-090753-run24.log`

- child extaddr: `be4f714ffa24c3dc`

#### PCAP-complete child attach 1

- log parent request: `09:13:44.083`
- log parent response: `09:13:44.245`
- log child id request: `09:13:44.804`
- log child id response: `09:13:44.895`
- parent ipv6: `fe80:0:0:0:88a8:5ec8:64ef:ec80`
- parent extaddr: `8aa85ec864efec80`
- parent rloc16: `0xc400`
- child extaddr: `be4f714ffa24c3dc`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **162 ms**
- Response -> Child ID Request: **588 ms**
- Child ID Request -> Response: **71 ms**
- Full Attach: **821 ms**
- pcap parent request: `09:13:44.078` (frame 626)
- pcap parent response: `09:13:44.240` (frame 627)
- pcap child id request: `09:13:44.828` (frame 635)
- pcap child id response: `09:13:44.899` (frame 637)

#### PCAP-complete child attach 2

- log parent request: `09:17:45.039`
- log parent response: `09:17:45.321`
- log child id request: `09:17:45.757`
- log child id response: `09:17:45.847`
- parent ipv6: `fe80:0:0:0:c0f3:8a29:152f:428a`
- parent extaddr: `c2f38a29152f428a`
- parent rloc16: `0xa800`
- child extaddr: `be4f714ffa24c3dc`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **382 ms**
- Response -> Child ID Request: **367 ms**
- Child ID Request -> Response: **66 ms**
- Full Attach: **815 ms**
- pcap parent request: `09:17:45.040` (frame 915)
- pcap parent response: `09:17:45.422` (frame 918)
- pcap child id request: `09:17:45.789` (frame 922)
- pcap child id response: `09:17:45.855` (frame 924)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 157: 16, seq 158: 16, seq 159: 16, seq 160: 16
- failed tx by dst: `8aa85ec864efec80`: 63

### `stock_child_20260624-091955-run25.log`

- child extaddr: `eae9b10dc65be7fa`

#### PCAP-complete child attach 1

- log parent request: `09:25:46.504`
- log parent response: `09:25:46.662`
- log child id request: `09:25:47.226`
- log child id response: `09:25:47.311`
- parent ipv6: `fe80:0:0:0:832:ceb9:f5ec:bc03`
- parent extaddr: `0a32ceb9f5ecbc03`
- parent rloc16: `0x9000`
- child extaddr: `eae9b10dc65be7fa`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **155 ms**
- Response -> Child ID Request: **595 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **813 ms**
- pcap parent request: `09:25:46.501` (frame 582)
- pcap parent response: `09:25:46.656` (frame 583)
- pcap child id request: `09:25:47.251` (frame 591)
- pcap child id response: `09:25:47.314` (frame 593)

#### PCAP-complete child attach 2

- log parent request: `09:29:46.871`
- log parent response: `09:29:46.932`
- log child id request: `09:29:47.592`
- log child id response: `09:29:47.683`
- parent ipv6: `fe80:0:0:0:58f3:4237:20e0:b14e`
- parent extaddr: `5af3423720e0b14e`
- parent rloc16: `0x0800`
- child extaddr: `eae9b10dc65be7fa`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **59 ms**
- Response -> Child ID Request: **690 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **819 ms**
- pcap parent request: `09:29:46.876` (frame 1037)
- pcap parent response: `09:29:46.935` (frame 1038)
- pcap child id request: `09:29:47.625` (frame 1044)
- pcap child id response: `09:29:47.695` (frame 1046)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 115: 16, seq 116: 16, seq 117: 16, seq 118: 16
- failed tx by dst: `0a32ceb9f5ecbc03`: 63

### `stock_child_20260624-093158-run26.log`

- child extaddr: `2660fab476a44dac`

#### PCAP-complete child attach 1

- log parent request: `09:37:48.774`
- log parent response: `09:37:48.853`
- log child id request: `09:37:49.493`
- log child id response: `09:37:49.585`
- parent ipv6: `fe80:0:0:0:9057:64a5:9b21:86e9`
- parent extaddr: `925764a59b2186e9`
- parent rloc16: `0xe400`
- child extaddr: `2660fab476a44dac`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **159 ms**
- Response -> Child ID Request: **590 ms**
- Child ID Request -> Response: **71 ms**
- Full Attach: **820 ms**
- pcap parent request: `09:37:48.769` (frame 619)
- pcap parent response: `09:37:48.928` (frame 622)
- pcap child id request: `09:37:49.518` (frame 628)
- pcap child id response: `09:37:49.589` (frame 630)

#### PCAP-complete child attach 2

- log parent request: `09:41:49.280`
- log parent response: `09:41:49.450`
- log child id request: `09:41:49.996`
- log child id response: `09:41:50.086`
- parent ipv6: `fe80:0:0:0:eca1:d092:98f8:39a0`
- parent extaddr: `eea1d09298f839a0`
- parent rloc16: `0xb000`
- child extaddr: `2660fab476a44dac`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **440 ms**
- Response -> Child ID Request: **310 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **813 ms**
- pcap parent request: `09:41:49.281` (frame 926)
- pcap parent response: `09:41:49.721` (frame 929)
- pcap child id request: `09:41:50.031` (frame 933)
- pcap child id response: `09:41:50.094` (frame 935)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 118: 16, seq 119: 16, seq 120: 16, seq 121: 16
- failed tx by dst: `925764a59b2186e9`: 62

### `stock_child_20260624-094400-run27.log`

- child extaddr: `f21a939927690594`

#### PCAP-complete child attach 1

- log parent request: `09:49:51.126`
- log parent response: `09:49:51.352`
- log child id request: `09:49:51.849`
- log child id response: `09:49:51.935`
- parent ipv6: `fe80:0:0:0:1044:ab25:5f49:5e3b`
- parent extaddr: `1244ab255f495e3b`
- parent rloc16: `0x5800`
- child extaddr: `f21a939927690594`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **366 ms**
- Response -> Child ID Request: **385 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **814 ms**
- pcap parent request: `09:49:51.123` (frame 514)
- pcap parent response: `09:49:51.489` (frame 517)
- pcap child id request: `09:49:51.874` (frame 523)
- pcap child id response: `09:49:51.937` (frame 525)

#### PCAP-complete child attach 2

- log parent request: `09:53:51.981`
- log parent response: `09:53:52.124`
- log child id request: `09:53:52.702`
- log child id response: `09:53:52.794`
- parent ipv6: `fe80:0:0:0:8c1:6c30:be4e:6696`
- parent extaddr: `0ac16c30be4e6696`
- parent rloc16: `0x2c00`
- child extaddr: `f21a939927690594`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **472 ms**
- Response -> Child ID Request: **278 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **820 ms**
- pcap parent request: `09:53:51.983` (frame 1125)
- pcap parent response: `09:53:52.455` (frame 1130)
- pcap child id request: `09:53:52.733` (frame 1132)
- pcap child id response: `09:53:52.803` (frame 1134)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 242: 16, seq 243: 16, seq 244: 16, seq 245: 16
- failed tx by dst: `1244ab255f495e3b`: 62

### `stock_child_20260624-095603-run28.log`

- child extaddr: `8a11ae1c3094840f`

#### PCAP-complete child attach 1

- log parent request: `10:01:53.655`
- log parent response: `10:01:53.922`
- log child id request: `10:01:54.375`
- log child id response: `10:01:54.469`
- parent ipv6: `fe80:0:0:0:40c0:3efb:3975:ae3a`
- parent extaddr: `42c03efb3975ae3a`
- parent rloc16: `0x3800`
- child extaddr: `8a11ae1c3094840f`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **397 ms**
- Response -> Child ID Request: **353 ms**
- Child ID Request -> Response: **73 ms**
- Full Attach: **823 ms**
- pcap parent request: `10:01:53.647` (frame 574)
- pcap parent response: `10:01:54.044` (frame 577)
- pcap child id request: `10:01:54.397` (frame 588)
- pcap child id response: `10:01:54.470` (frame 593)

#### PCAP-complete child attach 2

- log parent request: `10:05:54.586`
- log parent response: `10:05:54.694`
- log child id request: `10:05:55.305`
- log child id response: `10:05:55.391`
- parent ipv6: `fe80:0:0:0:5822:5016:a71d:e19f`
- parent extaddr: `5a225016a71de19f`
- parent rloc16: `0x3c00`
- child extaddr: `8a11ae1c3094840f`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **211 ms**
- Response -> Child ID Request: **540 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **813 ms**
- pcap parent request: `10:05:54.583` (frame 898)
- pcap parent response: `10:05:54.794` (frame 901)
- pcap child id request: `10:05:55.334` (frame 905)
- pcap child id response: `10:05:55.396` (frame 907)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 83: 16, seq 84: 16, seq 85: 16, seq 86: 16
- failed tx by dst: `42c03efb3975ae3a`: 62

### `stock_child_20260624-100805-run29.log`

- child extaddr: `5a5a65b460fb928b`

#### PCAP-complete child attach 1

- log parent request: `10:13:56.480`
- log parent response: `10:13:56.526`
- log child id request: `10:13:57.200`
- log child id response: `10:13:57.285`
- parent ipv6: `fe80:0:0:0:48ad:b4de:372d:cfa3`
- parent extaddr: `4aadb4de372dcfa3`
- parent rloc16: `0x6000`
- child extaddr: `5a5a65b460fb928b`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **87 ms**
- Response -> Child ID Request: **663 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **813 ms**
- pcap parent request: `10:13:56.470` (frame 607)
- pcap parent response: `10:13:56.557` (frame 610)
- pcap child id request: `10:13:57.220` (frame 617)
- pcap child id response: `10:13:57.283` (frame 619)

#### PCAP-complete child attach 2

- log parent request: `10:17:57.263`
- log parent response: `10:17:57.416`
- log child id request: `10:17:57.983`
- log child id response: `10:17:58.072`
- parent ipv6: `fe80:0:0:0:2440:ccad:a90b:58bf`
- parent extaddr: `2640ccada90b58bf`
- parent rloc16: `0xe400`
- child extaddr: `5a5a65b460fb928b`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **179 ms**
- Response -> Child ID Request: **571 ms**
- Child ID Request -> Response: **68 ms**
- Full Attach: **818 ms**
- pcap parent request: `10:17:57.261` (frame 1233)
- pcap parent response: `10:17:57.440` (frame 1236)
- pcap child id request: `10:17:58.011` (frame 1247)
- pcap child id response: `10:17:58.079` (frame 1252)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 114: 16, seq 115: 16, seq 116: 16, seq 117: 16
- failed tx by dst: `4aadb4de372dcfa3`: 63

### `stock_child_20260624-102008-run30.log`

- child extaddr: `ba19cf1905df780e`

#### PCAP-complete child attach 1

- log parent request: `10:25:58.768`
- log parent response: `10:25:58.873`
- log child id request: `10:25:59.488`
- log child id response: `10:25:59.572`
- parent ipv6: `fe80:0:0:0:6c42:8a16:102f:d03`
- parent extaddr: `6e428a16102f0d03`
- parent rloc16: `0xc800`
- child extaddr: `ba19cf1905df780e`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **246 ms**
- Response -> Child ID Request: **504 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **812 ms**
- pcap parent request: `10:25:58.758` (frame 500)
- pcap parent response: `10:25:59.004` (frame 506)
- pcap child id request: `10:25:59.508` (frame 510)
- pcap child id response: `10:25:59.570` (frame 515)

#### PCAP-complete child attach 2

- log parent request: `10:29:59.430`
- log parent response: `10:29:59.537`
- log child id request: `10:30:00.200`
- log child id response: `10:30:00.289`
- parent ipv6: `fe80:0:0:0:c8dd:f74:59db:a96a`
- parent extaddr: `cadd0f7459dba96a`
- parent rloc16: `0xa800`
- child extaddr: `ba19cf1905df780e`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **180 ms**
- Response -> Child ID Request: **571 ms**
- Child ID Request -> Response: **68 ms**
- Full Attach: **819 ms**
- pcap parent request: `10:29:59.478` (frame 1166)
- pcap parent response: `10:29:59.658` (frame 1169)
- pcap child id request: `10:30:00.229` (frame 1179)
- pcap child id response: `10:30:00.297` (frame 1184)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 226: 16, seq 227: 16, seq 228: 16, seq 229: 16
- failed tx by dst: `6e428a16102f0d03`: 62

### `stock_child_20260624-103210-run31.log`

- child extaddr: `fe2610be1f4ca016`

#### PCAP-complete child attach 1

- log parent request: `10:38:00.785`
- log parent response: `10:38:00.866`
- log child id request: `10:38:01.502`
- log child id response: `10:38:01.586`
- parent ipv6: `fe80:0:0:0:54cd:c058:fbc8:8357`
- parent extaddr: `56cdc058fbc88357`
- parent rloc16: `0xe400`
- child extaddr: `fe2610be1f4ca016`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **258 ms**
- Response -> Child ID Request: **491 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **811 ms**
- pcap parent request: `10:38:00.774` (frame 663)
- pcap parent response: `10:38:01.032` (frame 666)
- pcap child id request: `10:38:01.523` (frame 672)
- pcap child id response: `10:38:01.585` (frame 674)

#### PCAP-complete child attach 2

- log parent request: `10:42:01.594`
- log parent response: `10:42:01.667`
- log child id request: `10:42:02.316`
- log child id response: `10:42:02.451`
- parent ipv6: `fe80:0:0:0:2cd8:fefa:8b58:5aeb`
- parent extaddr: `2ed8fefa8b585aeb`
- parent rloc16: `0x2000`
- child extaddr: `fe2610be1f4ca016`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **333 ms**
- Response -> Child ID Request: **416 ms**
- Child ID Request -> Response: **113 ms**
- Full Attach: **862 ms**
- pcap parent request: `10:42:01.596` (frame 1090)
- pcap parent response: `10:42:01.929` (frame 1093)
- pcap child id request: `10:42:02.345` (frame 1097)
- pcap child id response: `10:42:02.458` (frame 1100)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 3: 16, seq 4: 16, seq 5: 16, seq 6: 16
- failed tx by dst: `56cdc058fbc88357`: 63

### `stock_child_20260624-104412-run32.log`

- child extaddr: `f65ba2bbc9f501d8`

#### PCAP-complete child attach 1

- log parent request: `10:50:03.403`
- log parent response: `10:50:03.520`
- log child id request: `10:50:04.124`
- log child id response: `10:50:04.209`
- parent ipv6: `fe80:0:0:0:5092:f78e:731f:b0cf`
- parent extaddr: `5292f78e731fb0cf`
- parent rloc16: `0x0800`
- child extaddr: `f65ba2bbc9f501d8`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **115 ms**
- Response -> Child ID Request: **635 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **812 ms**
- pcap parent request: `10:50:03.395` (frame 651)
- pcap parent response: `10:50:03.510` (frame 652)
- pcap child id request: `10:50:04.145` (frame 660)
- pcap child id response: `10:50:04.207` (frame 662)

#### PCAP-complete child attach 2

- log parent request: `10:54:04.198`
- log parent response: `10:54:04.398`
- log child id request: `10:54:04.919`
- log child id response: `10:54:05.010`
- parent ipv6: `fe80:0:0:0:20cc:2a6a:22a6:c7ab`
- parent extaddr: `22cc2a6a22a6c7ab`
- parent rloc16: `0x7400`
- child extaddr: `f65ba2bbc9f501d8`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **199 ms**
- Response -> Child ID Request: **551 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **820 ms**
- pcap parent request: `10:54:04.198` (frame 1833)
- pcap parent response: `10:54:04.397` (frame 1834)
- pcap child id request: `10:54:04.948` (frame 1840)
- pcap child id response: `10:54:05.018` (frame 1842)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 234: 16, seq 235: 16, seq 236: 16, seq 237: 16
- failed tx by dst: `5292f78e731fb0cf`: 64

### `stock_child_20260624-105615-run33.log`

- child extaddr: `8e08c18a0b94fcd9`

#### PCAP-complete child attach 1

- log parent request: `11:02:05.908`
- log parent response: `11:02:06.256`
- log child id request: `11:02:06.676`
- log child id response: `11:02:06.760`
- parent ipv6: `fe80:0:0:0:c0fe:e722:2c4e:9c53`
- parent extaddr: `c2fee7222c4e9c53`
- parent rloc16: `0x5c00`
- child extaddr: `8e08c18a0b94fcd9`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **435 ms**
- Response -> Child ID Request: **317 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **814 ms**
- pcap parent request: `11:02:05.948` (frame 664)
- pcap parent response: `11:02:06.383` (frame 667)
- pcap child id request: `11:02:06.700` (frame 673)
- pcap child id response: `11:02:06.762` (frame 675)

#### PCAP-complete child attach 2

- log parent request: `11:06:06.550`
- log parent response: `11:06:06.599`
- log child id request: `11:06:07.270`
- log child id response: `11:06:07.364`
- parent ipv6: `fe80:0:0:0:404e:e78c:75a:820a`
- parent extaddr: `424ee78c075a820a`
- parent rloc16: `0xc800`
- child extaddr: `8e08c18a0b94fcd9`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **164 ms**
- Response -> Child ID Request: **588 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **822 ms**
- pcap parent request: `11:06:06.554` (frame 1527)
- pcap parent response: `11:06:06.718` (frame 1530)
- pcap child id request: `11:06:07.306` (frame 1534)
- pcap child id response: `11:06:07.376` (frame 1536)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 163: 16, seq 164: 16, seq 165: 16, seq 166: 16
- failed tx by dst: `c2fee7222c4e9c53`: 64

### `stock_child_20260624-110817-run34.log`

- child extaddr: `7ef649e2a6e9d781`

#### PCAP-complete child attach 1

- log parent request: `11:14:08.588`
- log parent response: `11:14:08.705`
- log child id request: `11:14:09.307`
- log child id response: `11:14:09.391`
- parent ipv6: `fe80:0:0:0:f40f:84b:1d02:e47f`
- parent extaddr: `f60f084b1d02e47f`
- parent rloc16: `0x2400`
- child extaddr: `7ef649e2a6e9d781`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **116 ms**
- Response -> Child ID Request: **633 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **811 ms**
- pcap parent request: `11:14:08.584` (frame 583)
- pcap parent response: `11:14:08.700` (frame 584)
- pcap child id request: `11:14:09.333` (frame 592)
- pcap child id response: `11:14:09.395` (frame 594)

#### PCAP-complete child attach 2

- log parent request: `11:18:09.011`
- log parent response: `11:18:09.133`
- log child id request: `11:18:09.734`
- log child id response: `11:18:09.826`
- parent ipv6: `fe80:0:0:0:4822:2e75:e711:ef50`
- parent extaddr: `4a222e75e711ef50`
- parent rloc16: `0x3400`
- child extaddr: `7ef649e2a6e9d781`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **120 ms**
- Response -> Child ID Request: **629 ms**
- Child ID Request -> Response: **71 ms**
- Full Attach: **820 ms**
- pcap parent request: `11:18:09.018` (frame 1207)
- pcap parent response: `11:18:09.138` (frame 1208)
- pcap child id request: `11:18:09.767` (frame 1214)
- pcap child id response: `11:18:09.838` (frame 1216)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 168: 16, seq 169: 16, seq 170: 16, seq 171: 16
- failed tx by dst: `f60f084b1d02e47f`: 63

### `stock_child_20260624-112020-run35.log`

- child extaddr: `e2be032d224462f5`

#### PCAP-complete child attach 1

- log parent request: `11:26:10.781`
- log parent response: `11:26:10.891`
- log child id request: `11:26:11.499`
- log child id response: `11:26:11.586`
- parent ipv6: `fe80:0:0:0:e4f4:fb4c:1949:4692`
- parent extaddr: `e6f4fb4c19494692`
- parent rloc16: `0xf000`
- child extaddr: `e2be032d224462f5`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **292 ms**
- Response -> Child ID Request: **460 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **815 ms**
- pcap parent request: `11:26:10.776` (frame 524)
- pcap parent response: `11:26:11.068` (frame 527)
- pcap child id request: `11:26:11.528` (frame 533)
- pcap child id response: `11:26:11.591` (frame 535)

#### PCAP-complete child attach 2

- log parent request: `11:30:11.695`
- log parent response: `11:30:11.897`
- log child id request: `11:30:12.417`
- log child id response: `11:30:12.507`
- parent ipv6: `fe80:0:0:0:1416:7e3f:27ab:81f9`
- parent extaddr: `16167e3f27ab81f9`
- parent rloc16: `0x4400`
- child extaddr: `e2be032d224462f5`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **265 ms**
- Response -> Child ID Request: **484 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **819 ms**
- pcap parent request: `11:30:11.703` (frame 1757)
- pcap parent response: `11:30:11.968` (frame 1762)
- pcap child id request: `11:30:12.452` (frame 1765)
- pcap child id response: `11:30:12.522` (frame 1767)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 102: 16, seq 103: 16, seq 104: 16, seq 105: 16
- failed tx by dst: `e6f4fb4c19494692`: 64

### `stock_child_20260624-113222-run36.log`

- child extaddr: `c2e1ef6cedbc23c8`

#### PCAP-complete child attach 1

- log parent request: `11:38:13.087`
- log parent response: `11:38:13.369`
- log child id request: `11:38:13.854`
- log child id response: `11:38:13.946`
- parent ipv6: `fe80:0:0:0:bcb9:4f42:5b85:3dd8`
- parent extaddr: `beb94f425b853dd8`
- parent rloc16: `0x8000`
- child extaddr: `c2e1ef6cedbc23c8`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **204 ms**
- Response -> Child ID Request: **516 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **790 ms**
- pcap parent request: `11:38:13.161` (frame 545)
- pcap parent response: `11:38:13.365` (frame 546)
- pcap child id request: `11:38:13.881` (frame 554)
- pcap child id response: `11:38:13.951` (frame 556)

#### PCAP-complete child attach 2

- log parent request: `11:42:13.827`
- log parent response: `11:42:13.903`
- log child id request: `11:42:14.544`
- log child id response: `11:42:14.634`
- parent ipv6: `fe80:0:0:0:426:388e:e7:e0fe`
- parent extaddr: `0626388e00e7e0fe`
- parent rloc16: `0xf800`
- child extaddr: `c2e1ef6cedbc23c8`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **399 ms**
- Response -> Child ID Request: **349 ms**
- Child ID Request -> Response: **67 ms**
- Full Attach: **815 ms**
- pcap parent request: `11:42:13.829` (frame 858)
- pcap parent response: `11:42:14.228` (frame 861)
- pcap child id request: `11:42:14.577` (frame 865)
- pcap child id response: `11:42:14.644` (frame 867)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 186: 16, seq 187: 16, seq 188: 16, seq 189: 16
- failed tx by dst: `beb94f425b853dd8`: 63

### `stock_child_20260624-114425-run37.log`

- child extaddr: `32cbf2932756f2e9`

#### PCAP-complete child attach 1

- log parent request: `11:50:15.880`
- log parent response: `11:50:15.978`
- log child id request: `11:50:16.601`
- log child id response: `11:50:16.693`
- parent ipv6: `fe80:0:0:0:3453:cd9d:63fd:efac`
- parent extaddr: `3653cd9d63fdefac`
- parent rloc16: `0x1000`
- child extaddr: `32cbf2932756f2e9`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **97 ms**
- Response -> Child ID Request: **654 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **821 ms**
- pcap parent request: `11:50:15.877` (frame 633)
- pcap parent response: `11:50:15.974` (frame 634)
- pcap child id request: `11:50:16.628` (frame 642)
- pcap child id response: `11:50:16.698` (frame 644)

#### PCAP-complete child attach 2

- log parent request: `11:54:16.758`
- log parent response: `11:54:17.040`
- log child id request: `11:54:17.477`
- log child id response: `11:54:17.565`
- parent ipv6: `fe80:0:0:0:5c37:1707:f837:e94d`
- parent extaddr: `5e371707f837e94d`
- parent rloc16: `0x0000`
- child extaddr: `32cbf2932756f2e9`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **281 ms**
- Response -> Child ID Request: **470 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **814 ms**
- pcap parent request: `11:54:16.761` (frame 942)
- pcap parent response: `11:54:17.042` (frame 943)
- pcap child id request: `11:54:17.512` (frame 949)
- pcap child id response: `11:54:17.575` (frame 951)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 51: 16, seq 52: 16, seq 53: 16, seq 54: 16
- failed tx by dst: `3653cd9d63fdefac`: 63

### `stock_child_20260624-115627-run38.log`

- child extaddr: `16535cbc769af424`

#### PCAP-complete child attach 1

- log parent request: `12:02:18.274`
- log parent response: `12:02:18.393`
- log child id request: `12:02:18.996`
- log child id response: `12:02:19.089`
- parent ipv6: `fe80:0:0:0:2489:ec5a:5976:5c52`
- parent extaddr: `2689ec5a59765c52`
- parent rloc16: `0x8400`
- child extaddr: `16535cbc769af424`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **119 ms**
- Response -> Child ID Request: **633 ms**
- Child ID Request -> Response: **71 ms**
- Full Attach: **823 ms**
- pcap parent request: `12:02:18.271` (frame 543)
- pcap parent response: `12:02:18.390` (frame 544)
- pcap child id request: `12:02:19.023` (frame 552)
- pcap child id response: `12:02:19.094` (frame 554)

#### PCAP-complete child attach 2

- log parent request: `12:06:18.814`
- log parent response: `12:06:18.871`
- log child id request: `12:06:19.532`
- log child id response: `12:06:19.620`
- parent ipv6: `fe80:0:0:0:9853:cb59:b0f8:64e0`
- parent extaddr: `9a53cb59b0f864e0`
- parent rloc16: `0x3800`
- child extaddr: `16535cbc769af424`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **68 ms**
- Response -> Child ID Request: **682 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **814 ms**
- pcap parent request: `12:06:18.815` (frame 862)
- pcap parent response: `12:06:18.883` (frame 865)
- pcap child id request: `12:06:19.565` (frame 869)
- pcap child id response: `12:06:19.629` (frame 871)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 1: 1, seq 185: 16, seq 186: 16, seq 187: 16, seq 188: 15
- failed tx by dst: `2689ec5a59765c52`: 61

### `stock_child_20260624-120830-run39.log`

- child extaddr: `32426b42bac50f55`

#### PCAP-complete child attach 1

- log parent request: `12:14:20.582`
- log parent response: `12:14:20.701`
- log child id request: `12:14:21.350`
- log child id response: `12:14:21.434`
- parent ipv6: `fe80:0:0:0:8c52:3e02:c6a4:a665`
- parent extaddr: `8e523e02c6a4a665`
- parent rloc16: `0x8c00`
- child extaddr: `32426b42bac50f55`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **71 ms**
- Response -> Child ID Request: **680 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **813 ms**
- pcap parent request: `12:14:20.624` (frame 501)
- pcap parent response: `12:14:20.695` (frame 502)
- pcap child id request: `12:14:21.375` (frame 510)
- pcap child id response: `12:14:21.437` (frame 512)

#### PCAP-complete child attach 2

- log parent request: `12:18:21.193`
- log parent response: `12:18:21.414`
- log child id request: `12:18:21.915`
- log child id response: `12:18:22.007`
- parent ipv6: `fe80:0:0:0:8028:168:57f6:53ff`
- parent extaddr: `8228016857f653ff`
- parent rloc16: `0x5800`
- child extaddr: `32426b42bac50f55`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **219 ms**
- Response -> Child ID Request: **531 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **820 ms**
- pcap parent request: `12:18:21.198` (frame 1097)
- pcap parent response: `12:18:21.417` (frame 1098)
- pcap child id request: `12:18:21.948` (frame 1104)
- pcap child id response: `12:18:22.018` (frame 1106)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 230: 16, seq 231: 16, seq 232: 16, seq 233: 16
- failed tx by dst: `8e523e02c6a4a665`: 64

### `stock_child_20260624-122032-run40.log`

- child extaddr: `82c8ca6097b1aa74`

#### PCAP-complete child attach 1

- log parent request: `12:26:23.255`
- log parent response: `12:26:23.376`
- log child id request: `12:26:23.979`
- log child id response: `12:26:24.064`
- parent ipv6: `fe80:0:0:0:786c:b748:4c56:9f93`
- parent extaddr: `7a6cb7484c569f93`
- parent rloc16: `0x4000`
- child extaddr: `82c8ca6097b1aa74`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **118 ms**
- Response -> Child ID Request: **633 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **814 ms**
- pcap parent request: `12:26:23.252` (frame 707)
- pcap parent response: `12:26:23.370` (frame 708)
- pcap child id request: `12:26:24.003` (frame 717)
- pcap child id response: `12:26:24.066` (frame 719)

#### PCAP-complete child attach 2

- log parent request: `12:30:23.592`
- log parent response: `12:30:23.659`
- log child id request: `12:30:24.313`
- log child id response: `12:30:24.405`
- parent ipv6: `fe80:0:0:0:7006:4015:7dd:480b`
- parent extaddr: `7206401507dd480b`
- parent rloc16: `0xc000`
- child extaddr: `82c8ca6097b1aa74`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **465 ms**
- Response -> Child ID Request: **286 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **821 ms**
- pcap parent request: `12:30:23.596` (frame 1317)
- pcap parent response: `12:30:24.061` (frame 1322)
- pcap child id request: `12:30:24.347` (frame 1324)
- pcap child id response: `12:30:24.417` (frame 1326)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 22: 16, seq 23: 16, seq 24: 16, seq 25: 16
- failed tx by dst: `7a6cb7484c569f93`: 62

### `stock_child_20260624-123235-run41.log`

- child extaddr: `4ed04a6fea568f88`

#### PCAP-complete child attach 1

- log parent request: `12:38:25.845`
- log parent response: `12:38:25.895`
- log child id request: `12:38:26.564`
- log child id response: `12:38:26.656`
- parent ipv6: `fe80:0:0:0:5452:9de0:63a6:d9b4`
- parent extaddr: `56529de063a6d9b4`
- parent rloc16: `0xf800`
- child extaddr: `4ed04a6fea568f88`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **217 ms**
- Response -> Child ID Request: **530 ms**
- Child ID Request -> Response: **71 ms**
- Full Attach: **818 ms**
- pcap parent request: `12:38:25.842` (frame 429)
- pcap parent response: `12:38:26.059` (frame 434)
- pcap child id request: `12:38:26.589` (frame 439)
- pcap child id response: `12:38:26.660` (frame 441)

#### PCAP-complete child attach 2

- log parent request: `12:42:26.521`
- log parent response: `12:42:26.687`
- log child id request: `12:42:27.239`
- log child id response: `12:42:27.327`
- parent ipv6: `fe80:0:0:0:60b4:d764:189c:183f`
- parent extaddr: `62b4d764189c183f`
- parent rloc16: `0x1400`
- child extaddr: `4ed04a6fea568f88`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **195 ms**
- Response -> Child ID Request: **556 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **813 ms**
- pcap parent request: `12:42:26.522` (frame 729)
- pcap parent response: `12:42:26.717` (frame 732)
- pcap child id request: `12:42:27.273` (frame 736)
- pcap child id response: `12:42:27.335` (frame 738)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 226: 16, seq 227: 16, seq 228: 16, seq 229: 16
- failed tx by dst: `56529de063a6d9b4`: 63

### `stock_child_20260624-124437-run42.log`

- child extaddr: `72dcf113c03d1711`

#### PCAP-complete child attach 1

- log parent request: `12:50:27.526`
- log parent response: `12:50:27.713`
- log child id request: `12:50:28.294`
- log child id response: `12:50:28.382`
- parent ipv6: `fe80:0:0:0:a41a:3693:d7a5:4f2f`
- parent extaddr: `a61a3693d7a54f2f`
- parent rloc16: `0x6c00`
- child extaddr: `72dcf113c03d1711`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **209 ms**
- Response -> Child ID Request: **543 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **815 ms**
- pcap parent request: `12:50:27.569` (frame 169)
- pcap parent response: `12:50:27.778` (frame 174)
- pcap child id request: `12:50:28.321` (frame 179)
- pcap child id response: `12:50:28.384` (frame 181)

#### PCAP-complete child attach 2

- log parent request: `12:54:28.335`
- log parent response: `12:54:28.622`
- log child id request: `12:54:29.057`
- log child id response: `12:54:29.148`
- parent ipv6: `fe80:0:0:0:e8d0:49cd:85ab:e289`
- parent extaddr: `ead049cd85abe289`
- parent rloc16: `0xc000`
- child extaddr: `72dcf113c03d1711`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **295 ms**
- Response -> Child ID Request: **454 ms**
- Child ID Request -> Response: **71 ms**
- Full Attach: **820 ms**
- pcap parent request: `12:54:28.340` (frame 810)
- pcap parent response: `12:54:28.635` (frame 813)
- pcap child id request: `12:54:29.089` (frame 817)
- pcap child id response: `12:54:29.160` (frame 819)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 227: 16, seq 228: 16, seq 229: 16, seq 230: 16
- failed tx by dst: `a61a3693d7a54f2f`: 63

### `stock_child_20260624-125639-run43.log`

- child extaddr: `bafa26de228d2a29`

#### PCAP-complete child attach 1

- log parent request: `13:02:30.253`
- log parent response: `13:02:30.297`
- log child id request: `13:02:30.974`
- log child id response: `13:02:31.058`
- parent ipv6: `fe80:0:0:0:8051:f05b:9e48:1a70`
- parent extaddr: `8251f05b9e481a70`
- parent rloc16: `0xbc00`
- child extaddr: `bafa26de228d2a29`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **44 ms**
- Response -> Child ID Request: **705 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **812 ms**
- pcap parent request: `13:02:30.250` (frame 633)
- pcap parent response: `13:02:30.294` (frame 634)
- pcap child id request: `13:02:30.999` (frame 643)
- pcap child id response: `13:02:31.062` (frame 645)

#### PCAP-complete child attach 2

- log parent request: `13:06:30.734`
- log parent response: `13:06:30.912`
- log child id request: `13:06:31.457`
- log child id response: `13:06:31.549`
- parent ipv6: `fe80:0:0:0:d49c:b333:e52c:5025`
- parent extaddr: `d69cb333e52c5025`
- parent rloc16: `0xec00`
- child extaddr: `bafa26de228d2a29`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **531 ms**
- Response -> Child ID Request: **220 ms**
- Child ID Request -> Response: **71 ms**
- Full Attach: **822 ms**
- pcap parent request: `13:06:30.740` (frame 1303)
- pcap parent response: `13:06:31.271` (frame 1306)
- pcap child id request: `13:06:31.491` (frame 1310)
- pcap child id response: `13:06:31.562` (frame 1312)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 96: 16, seq 97: 16, seq 98: 16, seq 99: 16
- failed tx by dst: `8251f05b9e481a70`: 63

### `stock_child_20260624-130842-run44.log`

- child extaddr: `5eaa806725514f23`

#### PCAP-complete child attach 1

- log parent request: `13:14:33.201`
- log parent response: `13:14:33.313`
- log child id request: `13:14:33.921`
- log child id response: `13:14:34.014`
- parent ipv6: `fe80:0:0:0:a844:d89a:2933:b0e`
- parent extaddr: `aa44d89a29330b0e`
- parent rloc16: `0x1400`
- child extaddr: `5eaa806725514f23`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **112 ms**
- Response -> Child ID Request: **639 ms**
- Child ID Request -> Response: **71 ms**
- Full Attach: **822 ms**
- pcap parent request: `13:14:33.196` (frame 550)
- pcap parent response: `13:14:33.308` (frame 551)
- pcap child id request: `13:14:33.947` (frame 559)
- pcap child id response: `13:14:34.018` (frame 561)

#### PCAP-complete child attach 2

- log parent request: `13:18:33.761`
- log parent response: `13:18:33.903`
- log child id request: `13:18:34.479`
- log child id response: `13:18:34.567`
- parent ipv6: `fe80:0:0:0:5cbf:4a05:ca4c:60f6`
- parent extaddr: `5ebf4a05ca4c60f6`
- parent rloc16: `0x0400`
- child extaddr: `5eaa806725514f23`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **195 ms**
- Response -> Child ID Request: **556 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **814 ms**
- pcap parent request: `13:18:33.763` (frame 842)
- pcap parent response: `13:18:33.958` (frame 845)
- pcap child id request: `13:18:34.514` (frame 849)
- pcap child id response: `13:18:34.577` (frame 851)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 247: 16, seq 248: 16, seq 249: 16, seq 250: 16
- failed tx by dst: `aa44d89a29330b0e`: 62

### `stock_child_20260624-132044-run45.log`

- child extaddr: `82e0af691d1dae2a`

#### PCAP-complete child attach 1

- log parent request: `13:26:35.116`
- log parent response: `13:26:35.420`
- log child id request: `13:26:35.835`
- log child id response: `13:26:35.921`
- parent ipv6: `fe80:0:0:0:94ab:594e:3719:939`
- parent extaddr: `96ab594e37190939`
- parent rloc16: `0x6800`
- child extaddr: `82e0af691d1dae2a`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **426 ms**
- Response -> Child ID Request: **326 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **815 ms**
- pcap parent request: `13:26:35.110` (frame 526)
- pcap parent response: `13:26:35.536` (frame 529)
- pcap child id request: `13:26:35.862` (frame 535)
- pcap child id response: `13:26:35.925` (frame 537)

#### PCAP-complete child attach 2

- log parent request: `13:30:35.798`
- log parent response: `13:30:35.978`
- log child id request: `13:30:36.520`
- log child id response: `13:30:36.612`
- parent ipv6: `fe80:0:0:0:bc9f:195c:656d:6ea3`
- parent extaddr: `be9f195c656d6ea3`
- parent rloc16: `0x4c00`
- child extaddr: `82e0af691d1dae2a`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **180 ms**
- Response -> Child ID Request: **570 ms**
- Child ID Request -> Response: **72 ms**
- Full Attach: **822 ms**
- pcap parent request: `13:30:35.803` (frame 1132)
- pcap parent response: `13:30:35.983` (frame 1133)
- pcap child id request: `13:30:36.553` (frame 1139)
- pcap child id response: `13:30:36.625` (frame 1141)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 18: 16, seq 19: 16, seq 20: 16, seq 21: 16
- failed tx by dst: `96ab594e37190939`: 64

### `stock_child_20260624-133247-run46.log`

- child extaddr: `6a4d8a5e56ced9e3`

#### PCAP-complete child attach 1

- log parent request: `13:38:37.686`
- log parent response: `13:38:37.782`
- log child id request: `13:38:38.454`
- log child id response: `13:38:38.547`
- parent ipv6: `fe80:0:0:0:d0ff:9e69:580:2cf`
- parent extaddr: `d2ff9e69058002cf`
- parent rloc16: `0x6400`
- child extaddr: `6a4d8a5e56ced9e3`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **244 ms**
- Response -> Child ID Request: **505 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **819 ms**
- pcap parent request: `13:38:37.733` (frame 580)
- pcap parent response: `13:38:37.977` (frame 585)
- pcap child id request: `13:38:38.482` (frame 589)
- pcap child id response: `13:38:38.552` (frame 591)

#### PCAP-complete child attach 2

- log parent request: `13:42:38.504`
- log parent response: `13:42:38.784`
- log child id request: `13:42:39.224`
- log child id response: `13:42:39.310`
- parent ipv6: `fe80:0:0:0:9827:a22d:e784:f913`
- parent extaddr: `9a27a22de784f913`
- parent rloc16: `0x5c00`
- child extaddr: `6a4d8a5e56ced9e3`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **279 ms**
- Response -> Child ID Request: **473 ms**
- Child ID Request -> Response: **61 ms**
- Full Attach: **813 ms**
- pcap parent request: `13:42:38.506` (frame 880)
- pcap parent response: `13:42:38.785` (frame 881)
- pcap child id request: `13:42:39.258` (frame 885)
- pcap child id response: `13:42:39.319` (frame 887)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 241: 16, seq 242: 16, seq 243: 16, seq 244: 16
- failed tx by dst: `d2ff9e69058002cf`: 63

### `stock_child_20260624-134449-run47.log`

- child extaddr: `42e5632bd1e1119a`

#### PCAP-complete child attach 1

- log parent request: `13:50:39.941`
- log parent response: `13:50:40.179`
- log child id request: `13:50:40.709`
- log child id response: `13:50:40.803`
- parent ipv6: `fe80:0:0:0:2051:478e:e509:ed74`
- parent extaddr: `2251478ee509ed74`
- parent rloc16: `0xc800`
- child extaddr: `42e5632bd1e1119a`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **161 ms**
- Response -> Child ID Request: **561 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **792 ms**
- pcap parent request: `13:50:40.013` (frame 681)
- pcap parent response: `13:50:40.174` (frame 682)
- pcap child id request: `13:50:40.735` (frame 690)
- pcap child id response: `13:50:40.805` (frame 692)

#### PCAP-complete child attach 2

- log parent request: `13:54:40.524`
- log parent response: `13:54:40.770`
- log child id request: `13:54:41.243`
- log child id response: `13:54:41.329`
- parent ipv6: `fe80:0:0:0:486:22c8:15db:f2a`
- parent extaddr: `068622c815db0f2a`
- parent rloc16: `0xcc00`
- child extaddr: `42e5632bd1e1119a`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **245 ms**
- Response -> Child ID Request: **506 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **814 ms**
- pcap parent request: `13:54:40.523` (frame 970)
- pcap parent response: `13:54:40.768` (frame 971)
- pcap child id request: `13:54:41.274` (frame 977)
- pcap child id response: `13:54:41.337` (frame 979)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 223: 16, seq 224: 16, seq 225: 16, seq 226: 16
- failed tx by dst: `2251478ee509ed74`: 62

### `stock_child_20260624-135652-run48.log`

- child extaddr: `56a50ac45d7b9aab`

#### PCAP-complete child attach 1

- log parent request: `14:02:42.561`
- log parent response: `14:02:42.850`
- log child id request: `14:02:43.331`
- log child id response: `14:02:43.422`
- parent ipv6: `fe80:0:0:0:14b2:2753:37fe:bb31`
- parent extaddr: `16b2275337febb31`
- parent rloc16: `0xb800`
- child extaddr: `56a50ac45d7b9aab`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **457 ms**
- Response -> Child ID Request: **295 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **822 ms**
- pcap parent request: `14:02:42.601` (frame 570)
- pcap parent response: `14:02:43.058` (frame 575)
- pcap child id request: `14:02:43.353` (frame 579)
- pcap child id response: `14:02:43.423` (frame 581)

#### PCAP-complete child attach 2

- log parent request: `14:06:43.675`
- log parent response: `14:06:43.818`
- log child id request: `14:06:44.394`
- log child id response: `14:06:44.480`
- parent ipv6: `fe80:0:0:0:58f2:b0ad:5c12:1d1f`
- parent extaddr: `5af2b0ad5c121d1f`
- parent rloc16: `0x4c00`
- child extaddr: `56a50ac45d7b9aab`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **143 ms**
- Response -> Child ID Request: **608 ms**
- Child ID Request -> Response: **61 ms**
- Full Attach: **812 ms**
- pcap parent request: `14:06:43.673` (frame 879)
- pcap parent response: `14:06:43.816` (frame 880)
- pcap child id request: `14:06:44.424` (frame 887)
- pcap child id response: `14:06:44.485` (frame 889)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 159: 16, seq 160: 16, seq 161: 16, seq 162: 16
- failed tx by dst: `16b2275337febb31`: 60

### `stock_child_20260624-140854-run49.log`

- child extaddr: `aac030e9b24878d7`

#### PCAP-complete child attach 1

- log parent request: `14:14:45.045`
- log parent response: `14:14:45.132`
- log child id request: `14:14:45.767`
- log child id response: `14:14:45.857`
- parent ipv6: `fe80:0:0:0:2c8b:e364:2919:f0bf`
- parent extaddr: `2e8be3642919f0bf`
- parent rloc16: `0xf800`
- child extaddr: `aac030e9b24878d7`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **215 ms**
- Response -> Child ID Request: **533 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **818 ms**
- pcap parent request: `14:14:45.040` (frame 188)
- pcap parent response: `14:14:45.255` (frame 191)
- pcap child id request: `14:14:45.788` (frame 197)
- pcap child id response: `14:14:45.858` (frame 199)

#### PCAP-complete child attach 2

- log parent request: `14:18:45.539`
- log parent response: `14:18:45.692`
- log child id request: `14:18:46.257`
- log child id response: `14:18:46.344`
- parent ipv6: `fe80:0:0:0:a85b:d1b2:c301:6568`
- parent extaddr: `aa5bd1b2c3016568`
- parent rloc16: `0x8000`
- child extaddr: `aac030e9b24878d7`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **164 ms**
- Response -> Child ID Request: **585 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **811 ms**
- pcap parent request: `14:18:45.537` (frame 483)
- pcap parent response: `14:18:45.701` (frame 486)
- pcap child id request: `14:18:46.286` (frame 490)
- pcap child id response: `14:18:46.348` (frame 492)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 123: 16, seq 124: 16, seq 125: 16, seq 126: 16
- failed tx by dst: `2e8be3642919f0bf`: 62

### `stock_child_20260624-142056-run50.log`

- child extaddr: `5ea0561608490ea8`

#### PCAP-complete child attach 1

- log parent request: `14:26:47.295`
- log parent response: `14:26:47.401`
- log child id request: `14:26:48.015`
- log child id response: `14:26:48.109`
- parent ipv6: `fe80:0:0:0:6cdb:8062:576a:8de5`
- parent extaddr: `6edb8062576a8de5`
- parent rloc16: `0xc400`
- child extaddr: `5ea0561608490ea8`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **103 ms**
- Response -> Child ID Request: **646 ms**
- Child ID Request -> Response: **71 ms**
- Full Attach: **820 ms**
- pcap parent request: `14:26:47.290` (frame 312)
- pcap parent response: `14:26:47.393` (frame 313)
- pcap child id request: `14:26:48.039` (frame 321)
- pcap child id response: `14:26:48.110` (frame 323)

#### PCAP-complete child attach 2

- log parent request: `14:30:48.205`
- log parent response: `14:30:48.251`
- log child id request: `14:30:48.923`
- log child id response: `14:30:49.013`
- parent ipv6: `fe80:0:0:0:38f2:14bc:6750:c788`
- parent extaddr: `3af214bc6750c788`
- parent rloc16: `0x8000`
- child extaddr: `5ea0561608490ea8`
- timing source: **pcap-csv-tlv-existing**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **44 ms**
- Response -> Child ID Request: **707 ms**
- Child ID Request -> Response: **65 ms**
- Full Attach: **816 ms**
- pcap parent request: `14:30:48.205` (frame 628)
- pcap parent response: `14:30:48.249` (frame 629)
- pcap child id request: `14:30:48.956` (frame 635)
- pcap child id response: `14:30:49.021` (frame 637)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 212: 16, seq 213: 16, seq 214: 16, seq 215: 16
- failed tx by dst: `6edb8062576a8de5`: 61
