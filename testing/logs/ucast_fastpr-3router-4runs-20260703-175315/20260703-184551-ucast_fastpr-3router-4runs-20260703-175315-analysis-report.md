# Child Log Analysis

## ucast_fastpr_child

Files analyzed: **4**

- batch folders: `ucast_fastpr-3router-4runs-20260703-175315`

### PCAP-complete child attach summary

| Attach | Metric | M (SD), ms | n |
| --- | --- | ---: | ---: |
| 1 | Request -> Response | 156.25 (91.73) | 4 |
| 1 | Response -> Child ID Request | 597.50 (91.88) | 4 |
| 1 | Child ID Request -> Response | 13.75 (1.26) | 4 |
| 1 | Full Attach | 767.50 (2.08) | 4 |
| 2 | Request -> Response | 9.75 (1.26) | 4 |
| 2 | Response -> Child ID Request | 30.50 (1.29) | 4 |
| 2 | Child ID Request -> Response | 14.75 (0.96) | 4 |
| 2 | Full Attach | 55.00 (0.82) | 4 |

| Metric | M (SD) | n |
| --- | ---: | ---: |
| Failed TX Attempts per Log | 0.00 (0.00) | 4 |
| Log-only or Partial Sequences per Log | 1.00 (0.00) | 4 |

### `ucast_fastpr_child_20260703-175818-run01.log`

- manifest status: `completed`
- child extaddr: `c6c1796bc312ee73`
- switch target extaddr(s): `ea8916eae4f35adb, ea8916eae4f35adb, ea8916eae4f35adb`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `ca7dddcfe945f6ab`
- parent rloc16: `n/a`
- child extaddr: `c6c1796bc312ee73`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **80 ms**
- Response -> Child ID Request: **675 ms**
- Child ID Request -> Response: **15 ms**
- Full Attach: **770 ms**
- pcap parent request: `18:04:03.781` (frame 129)
- pcap parent response: `18:04:03.861` (frame 130)
- pcap child id request: `18:04:04.536` (frame 136)
- pcap child id response: `18:04:04.551` (frame 138)

#### PCAP-complete child attach 2

- log parent request: `18:04:08.298`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `ea8916eae4f35adb`
- parent rloc16: `n/a`
- child extaddr: `c6c1796bc312ee73`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **8 ms**
- Response -> Child ID Request: **32 ms**
- Child ID Request -> Response: **14 ms**
- Full Attach: **54 ms**
- pcap parent request: `18:04:08.345` (frame 141)
- pcap parent response: `18:04:08.353` (frame 143)
- pcap child id request: `18:04:08.385` (frame 145)
- pcap child id response: `18:04:08.399` (frame 147)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `18:04:08.317`
- log parent response: `18:04:08.333`
- log child id request: `18:04:08.350`
- log child id response: `18:04:08.382`
- parent ipv6: `n/a`
- parent extaddr: `ea8916eae4f35adb`
- parent rloc16: `0xe800`
- child extaddr: `c6c1796bc312ee73`
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

### `ucast_fastpr_child_20260703-181010-run02.log`

- manifest status: `completed`
- child extaddr: `f29106e598c10337`
- switch target extaddr(s): `fecd0d647c15f2e4, fecd0d647c15f2e4, fecd0d647c15f2e4`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `8246ceea1c66cd7f`
- parent rloc16: `n/a`
- child extaddr: `f29106e598c10337`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **269 ms**
- Response -> Child ID Request: **485 ms**
- Child ID Request -> Response: **14 ms**
- Full Attach: **768 ms**
- pcap parent request: `18:15:56.064` (frame 124)
- pcap parent response: `18:15:56.333` (frame 125)
- pcap child id request: `18:15:56.818` (frame 131)
- pcap child id response: `18:15:56.832` (frame 133)

#### PCAP-complete child attach 2

- log parent request: `18:16:00.232`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `fecd0d647c15f2e4`
- parent rloc16: `n/a`
- child extaddr: `f29106e598c10337`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **10 ms**
- Response -> Child ID Request: **31 ms**
- Child ID Request -> Response: **14 ms**
- Full Attach: **55 ms**
- pcap parent request: `18:16:00.276` (frame 135)
- pcap parent response: `18:16:00.286` (frame 137)
- pcap child id request: `18:16:00.317` (frame 139)
- pcap child id response: `18:16:00.331` (frame 141)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `18:16:00.251`
- log parent response: `18:16:00.266`
- log child id request: `18:16:00.283`
- log child id response: `18:16:00.313`
- parent ipv6: `n/a`
- parent extaddr: `fecd0d647c15f2e4`
- parent rloc16: `0x3c00`
- child extaddr: `f29106e598c10337`
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

### `ucast_fastpr_child_20260703-182202-run03.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `5622358fe79889bb`
- switch target extaddr(s): `029111ad5260f8ac, 029111ad5260f8ac, 029111ad5260f8ac`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `1612a9abe59d3b80`
- parent rloc16: `n/a`
- child extaddr: `5622358fe79889bb`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **83 ms**
- Response -> Child ID Request: **670 ms**
- Child ID Request -> Response: **12 ms**
- Full Attach: **765 ms**
- pcap parent request: `18:27:48.410` (frame 130)
- pcap parent response: `18:27:48.493` (frame 131)
- pcap child id request: `18:27:49.163` (frame 137)
- pcap child id response: `18:27:49.175` (frame 139)

#### PCAP-complete child attach 2

- log parent request: `18:27:52.372`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `029111ad5260f8ac`
- parent rloc16: `n/a`
- child extaddr: `5622358fe79889bb`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **10 ms**
- Response -> Child ID Request: **29 ms**
- Child ID Request -> Response: **16 ms**
- Full Attach: **55 ms**
- pcap parent request: `18:27:52.417` (frame 143)
- pcap parent response: `18:27:52.427` (frame 145)
- pcap child id request: `18:27:52.456` (frame 147)
- pcap child id response: `18:27:52.472` (frame 149)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `18:27:52.390`
- log parent response: `18:27:52.408`
- log child id request: `18:27:52.424`
- log child id response: `18:27:52.455`
- parent ipv6: `n/a`
- parent extaddr: `029111ad5260f8ac`
- parent rloc16: `0xcc00`
- child extaddr: `5622358fe79889bb`
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

### `ucast_fastpr_child_20260703-183354-run04.log`

- manifest status: `completed`
- child extaddr: `b21fdd631825951f`
- switch target extaddr(s): `a6d13f5de8823cb0, a6d13f5de8823cb0, a6d13f5de8823cb0`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `5e0cb586002195ba`
- parent rloc16: `n/a`
- child extaddr: `b21fdd631825951f`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **193 ms**
- Response -> Child ID Request: **560 ms**
- Child ID Request -> Response: **14 ms**
- Full Attach: **767 ms**
- pcap parent request: `18:39:40.338` (frame 127)
- pcap parent response: `18:39:40.531` (frame 128)
- pcap child id request: `18:39:41.091` (frame 135)
- pcap child id response: `18:39:41.105` (frame 137)

#### PCAP-complete child attach 2

- log parent request: `18:39:44.228`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `a6d13f5de8823cb0`
- parent rloc16: `n/a`
- child extaddr: `b21fdd631825951f`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **11 ms**
- Response -> Child ID Request: **30 ms**
- Child ID Request -> Response: **15 ms**
- Full Attach: **56 ms**
- pcap parent request: `18:39:44.272` (frame 140)
- pcap parent response: `18:39:44.283` (frame 142)
- pcap child id request: `18:39:44.313` (frame 144)
- pcap child id response: `18:39:44.328` (frame 146)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `18:39:44.247`
- log parent response: `18:39:44.262`
- log child id request: `18:39:44.279`
- log child id response: `18:39:44.309`
- parent ipv6: `n/a`
- parent extaddr: `a6d13f5de8823cb0`
- parent rloc16: `0xb800`
- child extaddr: `b21fdd631825951f`
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
