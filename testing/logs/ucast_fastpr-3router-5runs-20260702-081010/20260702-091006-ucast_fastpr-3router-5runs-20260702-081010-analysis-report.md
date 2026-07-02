# Child Log Analysis

## ucast_fastpr_child

Files analyzed: **5**

- batch folders: `ucast_fastpr-3router-5runs-20260702-081010`

### PCAP-complete child attach summary

| Attach | Metric | M (SD), ms | n |
| --- | --- | ---: | ---: |
| 1 | Request -> Response | 144.00 (103.11) | 5 |
| 1 | Response -> Child ID Request | 593.60 (111.18) | 5 |
| 1 | Child ID Request -> Response | 67.60 (8.08) | 5 |
| 1 | Full Attach | 805.20 (22.10) | 5 |
| 2 | Request -> Response | 43.80 (3.56) | 5 |
| 2 | Response -> Child ID Request | 91.80 (12.93) | 5 |
| 2 | Child ID Request -> Response | 70.40 (7.70) | 5 |
| 2 | Full Attach | 206.00 (7.91) | 5 |

| Metric | M (SD) | n |
| --- | ---: | ---: |
| Failed TX Attempts per Log | 0.00 (0.00) | 5 |
| Log-only or Partial Sequences per Log | 0.00 (0.00) | 5 |

### `ucast_fastpr_child_20260702-081038-run01.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `1aca368a2ebc1a01`
- switch target extaddr(s): `723eeccfcefb8963, 723eeccfcefb8963, 723eeccfcefb8963`

#### PCAP-complete child attach 1

- log parent request: `08:16:23.514`
- log parent response: `08:16:23.670`
- log child id request: `08:16:24.287`
- log child id response: `08:16:24.375`
- parent ipv6: `fe80:0:0:0:817:e9f0:d796:4963`
- parent extaddr: `0a17e9f0d7964963`
- parent rloc16: `0xdc00`
- child extaddr: `1aca368a2ebc1a01`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **73 ms**
- Response -> Child ID Request: **648 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **785 ms**
- pcap parent request: `08:16:23.587` (frame 138)
- pcap parent response: `08:16:23.660` (frame 139)
- pcap child id request: `08:16:24.308` (frame 145)
- pcap child id response: `08:16:24.372` (frame 147)

#### PCAP-complete child attach 2

- log parent request: `08:16:28.130`
- log parent response: `08:16:28.210`
- log child id request: `08:16:28.263`
- log child id response: `08:16:28.354`
- parent ipv6: `fe80:0:0:0:703e:eccf:cefb:8963`
- parent extaddr: `723eeccfcefb8963`
- parent rloc16: `0xec00`
- child extaddr: `1aca368a2ebc1a01`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **41 ms**
- Response -> Child ID Request: **92 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **196 ms**
- pcap parent request: `08:16:28.155` (frame 151)
- pcap parent response: `08:16:28.196` (frame 153)
- pcap child id request: `08:16:28.288` (frame 155)
- pcap child id response: `08:16:28.351` (frame 157)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260702-082230-run02.log`

- manifest status: `completed`
- child extaddr: `f289fda6c47f1c81`
- switch target extaddr(s): `f2b883c631dcb3a6, f2b883c631dcb3a6, f2b883c631dcb3a6`

#### PCAP-complete child attach 1

- log parent request: `08:28:16.685`
- log parent response: `08:28:16.915`
- log child id request: `08:28:17.457`
- log child id response: `08:28:17.560`
- parent ipv6: `fe80:0:0:0:2c96:380b:5664:a157`
- parent extaddr: `2e96380b5664a157`
- parent rloc16: `0xf400`
- child extaddr: `f289fda6c47f1c81`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **180 ms**
- Response -> Child ID Request: **572 ms**
- Child ID Request -> Response: **82 ms**
- Full Attach: **834 ms**
- pcap parent request: `08:28:16.727` (frame 131)
- pcap parent response: `08:28:16.907` (frame 132)
- pcap child id request: `08:28:17.479` (frame 138)
- pcap child id response: `08:28:17.561` (frame 140)

#### PCAP-complete child attach 2

- log parent request: `08:28:20.715`
- log parent response: `08:28:20.803`
- log child id request: `08:28:20.867`
- log child id response: `08:28:20.956`
- parent ipv6: `fe80:0:0:0:f0b8:83c6:31dc:b3a6`
- parent extaddr: `f2b883c631dcb3a6`
- parent rloc16: `0x0800`
- child extaddr: `f289fda6c47f1c81`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **39 ms**
- Response -> Child ID Request: **114 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **215 ms**
- pcap parent request: `08:28:20.739` (frame 142)
- pcap parent response: `08:28:20.778` (frame 144)
- pcap child id request: `08:28:20.892` (frame 146)
- pcap child id response: `08:28:20.954` (frame 148)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260702-083423-run03.log`

- manifest status: `completed`
- child extaddr: `421c36f2bcd1dbde`
- switch target extaddr(s): `deea14f27a386cfd, deea14f27a386cfd, deea14f27a386cfd`

#### PCAP-complete child attach 1

- log parent request: `08:40:08.610`
- log parent response: `08:40:08.731`
- log child id request: `08:40:09.380`
- log child id response: `08:40:09.469`
- parent ipv6: `fe80:0:0:0:7c56:5f09:8ddb:2f41`
- parent extaddr: `7e565f098ddb2f41`
- parent rloc16: `0x6000`
- child extaddr: `421c36f2bcd1dbde`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **63 ms**
- Response -> Child ID Request: **684 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **811 ms**
- pcap parent request: `08:40:08.660` (frame 129)
- pcap parent response: `08:40:08.723` (frame 130)
- pcap child id request: `08:40:09.407` (frame 136)
- pcap child id response: `08:40:09.471` (frame 138)

#### PCAP-complete child attach 2

- log parent request: `08:40:13.189`
- log parent response: `08:40:13.267`
- log child id request: `08:40:13.317`
- log child id response: `08:40:13.415`
- parent ipv6: `fe80:0:0:0:dcea:14f2:7a38:6cfd`
- parent extaddr: `deea14f27a386cfd`
- parent rloc16: `0xc800`
- child extaddr: `421c36f2bcd1dbde`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **46 ms**
- Response -> Child ID Request: **82 ms**
- Child ID Request -> Response: **74 ms**
- Full Attach: **202 ms**
- pcap parent request: `08:40:13.216` (frame 140)
- pcap parent response: `08:40:13.262` (frame 142)
- pcap child id request: `08:40:13.344` (frame 144)
- pcap child id response: `08:40:13.418` (frame 146)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260702-084615-run04.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `aa04d54e7dc43292`
- switch target extaddr(s): `be849ea7c75f3f94, be849ea7c75f3f94, be849ea7c75f3f94`

#### PCAP-complete child attach 1

- log parent request: `08:52:01.594`
- log parent response: `08:52:01.744`
- log child id request: `08:52:02.365`
- log child id response: `08:52:02.454`
- parent ipv6: `fe80:0:0:0:88d4:42c4:936c:353b`
- parent extaddr: `8ad442c4936c353b`
- parent rloc16: `0x1800`
- child extaddr: `aa04d54e7dc43292`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **95 ms**
- Response -> Child ID Request: **655 ms**
- Child ID Request -> Response: **65 ms**
- Full Attach: **815 ms**
- pcap parent request: `08:52:01.640` (frame 129)
- pcap parent response: `08:52:01.735` (frame 130)
- pcap child id request: `08:52:02.390` (frame 136)
- pcap child id response: `08:52:02.455` (frame 138)

#### PCAP-complete child attach 2

- log parent request: `08:52:05.744`
- log parent response: `08:52:05.823`
- log child id request: `08:52:05.875`
- log child id response: `08:52:05.973`
- parent ipv6: `fe80:0:0:0:bc84:9ea7:c75f:3f94`
- parent extaddr: `be849ea7c75f3f94`
- parent rloc16: `0x8c00`
- child extaddr: `aa04d54e7dc43292`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **46 ms**
- Response -> Child ID Request: **85 ms**
- Child ID Request -> Response: **73 ms**
- Full Attach: **204 ms**
- pcap parent request: `08:52:05.772` (frame 141)
- pcap parent response: `08:52:05.818` (frame 143)
- pcap child id request: `08:52:05.903` (frame 145)
- pcap child id response: `08:52:05.976` (frame 147)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260702-085808-run05.log`

- manifest status: `completed`
- child extaddr: `ea83f8b416ab052e`
- switch target extaddr(s): `be676617a15f189c, be676617a15f189c, be676617a15f189c`

#### PCAP-complete child attach 1

- log parent request: `09:03:53.677`
- log parent response: `09:03:54.069`
- log child id request: `09:03:54.449`
- log child id response: `09:03:54.536`
- parent ipv6: `fe80:0:0:0:e8a0:cc77:9e87:233f`
- parent extaddr: `eaa0cc779e87233f`
- parent rloc16: `0xe000`
- child extaddr: `ea83f8b416ab052e`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **309 ms**
- Response -> Child ID Request: **409 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **781 ms**
- pcap parent request: `09:03:53.755` (frame 133)
- pcap parent response: `09:03:54.064` (frame 134)
- pcap child id request: `09:03:54.473` (frame 140)
- pcap child id response: `09:03:54.536` (frame 142)

#### PCAP-complete child attach 2

- log parent request: `09:03:58.289`
- log parent response: `09:03:58.370`
- log child id request: `09:03:58.417`
- log child id response: `09:03:58.528`
- parent ipv6: `fe80:0:0:0:bc67:6617:a15f:189c`
- parent extaddr: `be676617a15f189c`
- parent rloc16: `0x2800`
- child extaddr: `ea83f8b416ab052e`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **47 ms**
- Response -> Child ID Request: **86 ms**
- Child ID Request -> Response: **80 ms**
- Full Attach: **213 ms**
- pcap parent request: `09:03:58.317` (frame 145)
- pcap parent response: `09:03:58.364` (frame 147)
- pcap child id request: `09:03:58.450` (frame 149)
- pcap child id response: `09:03:58.530` (frame 151)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**
