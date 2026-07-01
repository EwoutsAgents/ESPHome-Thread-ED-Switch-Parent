# Child Log Analysis

## mcast_child

Files analyzed: **3**

### PCAP-complete child attach summary

| Attach | Metric | M (SD), ms | n |
| --- | --- | ---: | ---: |
| 1 | Request -> Response | 303.33 (46.82) | 3 |
| 1 | Response -> Child ID Request | 445.33 (48.95) | 3 |
| 1 | Child ID Request -> Response | 71.33 (3.21) | 3 |
| 1 | Full Attach | 820.00 (4.58) | 3 |
| 2 | Request -> Response | 405.00 (169.73) | 3 |
| 2 | Response -> Child ID Request | 334.67 (16.77) | 3 |
| 2 | Child ID Request -> Response | 67.33 (5.77) | 3 |
| 2 | Full Attach | 807.00 (155.08) | 3 |

| Metric | M (SD) | n |
| --- | ---: | ---: |
| Failed TX Attempts per Log | 0.00 (0.00) | 3 |
| Log-only or Partial Sequences per Log | 0.00 (0.00) | 3 |

### `mcast_child_20260624-194940-run01.log`

- child extaddr: `02ae31a950198402`
- switch target extaddr(s): `e663c9c431b6e53e, e663c9c431b6e53e, e663c9c431b6e53e`

#### PCAP-complete child attach 1

- log parent request: `19:55:31.343`
- log parent response: `19:55:31.747`
- log child id request: `19:55:32.110`
- log child id response: `19:55:32.202`
- parent ipv6: `fe80:0:0:0:c8f7:f6e5:b338:bdd5`
- parent extaddr: `caf7f6e5b338bdd5`
- parent rloc16: `0xa000`
- child extaddr: `02ae31a950198402`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **353 ms**
- Response -> Child ID Request: **393 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **816 ms**
- pcap parent request: `19:55:31.388` (frame 629)
- pcap parent response: `19:55:31.741` (frame 630)
- pcap child id request: `19:55:32.134` (frame 655)
- pcap child id response: `19:55:32.204` (frame 660)

#### PCAP-complete child attach 2

- log parent request: `19:56:01.591`
- log parent response: `19:56:01.720`
- log child id request: `19:56:02.493`
- log child id response: `19:56:02.582`
- parent ipv6: `fe80:0:0:0:e463:c9c4:31b6:e53e`
- parent extaddr: `e663c9c431b6e53e`
- parent rloc16: `0xd000`
- child extaddr: `02ae31a950198402`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **531 ms**
- Response -> Child ID Request: **324 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **919 ms**
- pcap parent request: `19:56:01.665` (frame 690)
- pcap parent response: `19:56:02.196` (frame 695)
- pcap child id request: `19:56:02.520` (frame 698)
- pcap child id response: `19:56:02.584` (frame 700)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_child_20260624-200203-run02.log`

- child extaddr: `7e522edb77c23fe6`
- switch target extaddr(s): `c660ef613b5b5454, c660ef613b5b5454, c660ef613b5b5454`

#### PCAP-complete child attach 1

- log parent request: `20:07:54.507`
- log parent response: `20:07:54.622`
- log child id request: `20:07:55.229`
- log child id response: `20:07:55.325`
- parent ipv6: `fe80:0:0:0:7064:7530:a5a2:a65d`
- parent extaddr: `72647530a5a2a65d`
- parent rloc16: `0x1000`
- child extaddr: `7e522edb77c23fe6`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **297 ms**
- Response -> Child ID Request: **453 ms**
- Child ID Request -> Response: **75 ms**
- Full Attach: **825 ms**
- pcap parent request: `20:07:54.503` (frame 568)
- pcap parent response: `20:07:54.800` (frame 573)
- pcap child id request: `20:07:55.253` (frame 577)
- pcap child id response: `20:07:55.328` (frame 579)

#### PCAP-complete child attach 2

- log parent request: `20:08:29.484`
- log parent response: `20:08:29.782`
- log child id request: `20:08:30.101`
- log child id response: `20:08:30.191`
- parent ipv6: `fe80:0:0:0:c460:ef61:3b5b:5454`
- parent extaddr: `c660ef613b5b5454`
- parent rloc16: `0x1800`
- child extaddr: `7e522edb77c23fe6`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **212 ms**
- Response -> Child ID Request: **354 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **630 ms**
- pcap parent request: `20:08:29.562` (frame 632)
- pcap parent response: `20:08:29.774` (frame 633)
- pcap child id request: `20:08:30.128` (frame 639)
- pcap child id response: `20:08:30.192` (frame 641)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_child_20260624-201425-run03.log`

- child extaddr: `e68ceec04259d7ef`
- switch target extaddr(s): `b2a1081687ed555e, b2a1081687ed555e, b2a1081687ed555e`

#### PCAP-complete child attach 1

- log parent request: `20:20:16.676`
- log parent response: `20:20:16.871`
- log child id request: `20:20:17.398`
- log child id response: `20:20:17.489`
- parent ipv6: `fe80:0:0:0:60c8:8586:6bc8:95c3`
- parent extaddr: `62c885866bc895c3`
- parent rloc16: `0x3800`
- child extaddr: `e68ceec04259d7ef`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **260 ms**
- Response -> Child ID Request: **490 ms**
- Child ID Request -> Response: **69 ms**
- Full Attach: **819 ms**
- pcap parent request: `20:20:16.674` (frame 683)
- pcap parent response: `20:20:16.934` (frame 688)
- pcap child id request: `20:20:17.424` (frame 692)
- pcap child id response: `20:20:17.493` (frame 694)

#### PCAP-complete child attach 2

- log parent request: `20:20:49.441`
- log parent response: `20:20:49.631`
- log child id request: `20:20:50.289`
- log child id response: `20:20:50.387`
- parent ipv6: `fe80:0:0:0:b0a1:816:87ed:555e`
- parent extaddr: `b2a1081687ed555e`
- parent rloc16: `0xa800`
- child extaddr: `e68ceec04259d7ef`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **472 ms**
- Response -> Child ID Request: **326 ms**
- Child ID Request -> Response: **74 ms**
- Full Attach: **872 ms**
- pcap parent request: `20:20:49.519` (frame 775)
- pcap parent response: `20:20:49.991` (frame 786)
- pcap child id request: `20:20:50.317` (frame 788)
- pcap child id response: `20:20:50.391` (frame 790)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**
