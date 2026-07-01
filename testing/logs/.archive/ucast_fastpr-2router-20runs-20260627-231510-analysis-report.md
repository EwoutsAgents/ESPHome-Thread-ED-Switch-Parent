# Child Log Analysis

## ucast_fastpr_child

Files analyzed: **20**

- batch folders: `ucast_fastpr-2router-20runs-20260627-231510`

### PCAP-complete child attach summary

| Attach | Metric | M (SD), ms | n |
| --- | --- | ---: | ---: |
| 1 | Request -> Response | 207.25 (127.08) | 20 |
| 1 | Response -> Child ID Request | 542.75 (128.26) | 20 |
| 1 | Child ID Request -> Response | 62.95 (1.28) | 20 |
| 1 | Full Attach | 812.95 (9.56) | 20 |
| 2 | Request -> Response | 40.35 (0.99) | 20 |
| 2 | Response -> Child ID Request | 346.65 (3.50) | 20 |
| 2 | Child ID Request -> Response | 63.20 (1.40) | 20 |
| 2 | Full Attach | 450.20 (3.29) | 20 |

| Metric | M (SD) | n |
| --- | ---: | ---: |
| Failed TX Attempts per Log | 0.00 (0.00) | 20 |
| Log-only or Partial Sequences per Log | 0.00 (0.00) | 20 |

### `ucast_fastpr_child_20260627-231538-run01.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `9e98dffadf2765cc`
- switch target extaddr(s): `7a7435e7cd8ad71d, 7a7435e7cd8ad71d, 7a7435e7cd8ad71d`

#### PCAP-complete child attach 1

- log parent request: `23:21:20.990`
- log parent response: `23:21:21.058`
- log child id request: `23:21:21.694`
- log child id response: `23:21:21.784`
- parent ipv6: `fe80:0:0:0:ec3f:c95c:7377:9e27`
- parent extaddr: `ee3fc95c73779e27`
- parent rloc16: `0x6c00`
- child extaddr: `9e98dffadf2765cc`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **79 ms**
- Response -> Child ID Request: **672 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **815 ms**
- pcap parent request: `23:21:20.962` (frame 79)
- pcap parent response: `23:21:21.041` (frame 80)
- pcap child id request: `23:21:21.713` (frame 84)
- pcap child id response: `23:21:21.777` (frame 86)

#### PCAP-complete child attach 2

- log parent request: `23:21:25.570`
- log parent response: `23:21:25.681`
- log child id request: `23:21:25.976`
- log child id response: `23:21:26.078`
- parent ipv6: `fe80:0:0:0:7874:35e7:cd8a:d71d`
- parent extaddr: `7a7435e7cd8ad71d`
- parent rloc16: `0xb000`
- child extaddr: `9e98dffadf2765cc`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **40 ms**
- Response -> Child ID Request: **350 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **452 ms**
- pcap parent request: `23:21:25.615` (frame 89)
- pcap parent response: `23:21:25.655` (frame 91)
- pcap child id request: `23:21:26.005` (frame 93)
- pcap child id response: `23:21:26.067` (frame 95)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260627-232727-run02.log`

- manifest status: `completed`
- child extaddr: `ca12c09426b22260`
- switch target extaddr(s): `960b9ac5a711c793, 960b9ac5a711c793, 960b9ac5a711c793`

#### PCAP-complete child attach 1

- log parent request: `23:33:08.296`
- log parent response: `23:33:08.533`
- log child id request: `23:33:09.126`
- log child id response: `23:33:09.168`
- parent ipv6: `fe80:0:0:0:cc34:4f72:fbe0:9c38`
- parent extaddr: `ce344f72fbe09c38`
- parent rloc16: `0xd000`
- child extaddr: `ca12c09426b22260`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **140 ms**
- Response -> Child ID Request: **582 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **785 ms**
- pcap parent request: `23:33:08.375` (frame 79)
- pcap parent response: `23:33:08.515` (frame 80)
- pcap child id request: `23:33:09.097` (frame 85)
- pcap child id response: `23:33:09.160` (frame 87)

#### PCAP-complete child attach 2

- log parent request: `23:33:13.053`
- log parent response: `23:33:13.160`
- log child id request: `23:33:13.459`
- log child id response: `23:33:13.558`
- parent ipv6: `fe80:0:0:0:940b:9ac5:a711:c793`
- parent extaddr: `960b9ac5a711c793`
- parent rloc16: `0x1c00`
- child extaddr: `ca12c09426b22260`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **41 ms**
- Response -> Child ID Request: **347 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **451 ms**
- pcap parent request: `23:33:13.095` (frame 90)
- pcap parent response: `23:33:13.136` (frame 92)
- pcap child id request: `23:33:13.483` (frame 94)
- pcap child id response: `23:33:13.546` (frame 96)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260627-233915-run03.log`

- manifest status: `completed`
- child extaddr: `12fbdeff64831bf5`
- switch target extaddr(s): `ba55504135b5a227, ba55504135b5a227, ba55504135b5a227`

#### PCAP-complete child attach 1

- log parent request: `23:44:56.210`
- log parent response: `23:44:56.313`
- log child id request: `23:44:56.912`
- log child id response: `23:44:57.001`
- parent ipv6: `fe80:0:0:0:f0cc:8347:1077:a3b5`
- parent extaddr: `f2cc83471077a3b5`
- parent rloc16: `0xf000`
- child extaddr: `12fbdeff64831bf5`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **112 ms**
- Response -> Child ID Request: **636 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **810 ms**
- pcap parent request: `23:44:56.183` (frame 72)
- pcap parent response: `23:44:56.295` (frame 73)
- pcap child id request: `23:44:56.931` (frame 77)
- pcap child id response: `23:44:56.993` (frame 79)

#### PCAP-complete child attach 2

- log parent request: `23:45:00.823`
- log parent response: `23:45:00.931`
- log child id request: `23:45:01.226`
- log child id response: `23:45:01.325`
- parent ipv6: `fe80:0:0:0:b855:5041:35b5:a227`
- parent extaddr: `ba55504135b5a227`
- parent rloc16: `0x1000`
- child extaddr: `12fbdeff64831bf5`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **40 ms**
- Response -> Child ID Request: **343 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **446 ms**
- pcap parent request: `23:45:00.866` (frame 82)
- pcap parent response: `23:45:00.906` (frame 84)
- pcap child id request: `23:45:01.249` (frame 86)
- pcap child id response: `23:45:01.312` (frame 88)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260627-235103-run04.log`

- manifest status: `completed`
- child extaddr: `22e49d53a118e0ee`
- switch target extaddr(s): `42c26f2f4f160b9c, 42c26f2f4f160b9c, 42c26f2f4f160b9c`

#### PCAP-complete child attach 1

- log parent request: `23:56:44.159`
- log parent response: `23:56:44.549`
- log child id request: `23:56:44.931`
- log child id response: `23:56:45.020`
- parent ipv6: `fe80:0:0:0:386d:b369:6c68:cde0`
- parent extaddr: `3a6db3696c68cde0`
- parent rloc16: `0xb800`
- child extaddr: `22e49d53a118e0ee`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **333 ms**
- Response -> Child ID Request: **419 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **814 ms**
- pcap parent request: `23:56:44.202` (frame 78)
- pcap parent response: `23:56:44.535` (frame 79)
- pcap child id request: `23:56:44.954` (frame 83)
- pcap child id response: `23:56:45.016` (frame 85)

#### PCAP-complete child attach 2

- log parent request: `23:56:48.480`
- log parent response: `23:56:48.589`
- log child id request: `23:56:48.880`
- log child id response: `23:56:48.979`
- parent ipv6: `fe80:0:0:0:40c2:6f2f:4f16:b9c`
- parent extaddr: `42c26f2f4f160b9c`
- parent rloc16: `0xc800`
- child extaddr: `22e49d53a118e0ee`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **41 ms**
- Response -> Child ID Request: **339 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **444 ms**
- pcap parent request: `23:56:48.527` (frame 88)
- pcap parent response: `23:56:48.568` (frame 90)
- pcap child id request: `23:56:48.907` (frame 92)
- pcap child id response: `23:56:48.971` (frame 94)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260628-000250-run05.log`

- manifest status: `completed`
- child extaddr: `c2f897fb569546a1`
- switch target extaddr(s): `121c3f8ddcd73a7c, 121c3f8ddcd73a7c, 121c3f8ddcd73a7c`

#### PCAP-complete child attach 1

- log parent request: `00:08:31.915`
- log parent response: `00:08:32.364`
- log child id request: `00:08:32.626`
- log child id response: `00:08:32.714`
- parent ipv6: `fe80:0:0:0:9cd7:780a:8b43:2b6`
- parent extaddr: `9ed7780a8b4302b6`
- parent rloc16: `0x1400`
- child extaddr: `c2f897fb569546a1`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **452 ms**
- Response -> Child ID Request: **300 ms**
- Child ID Request -> Response: **61 ms**
- Full Attach: **813 ms**
- pcap parent request: `00:08:31.897` (frame 76)
- pcap parent response: `00:08:32.349` (frame 77)
- pcap child id request: `00:08:32.649` (frame 81)
- pcap child id response: `00:08:32.710` (frame 83)

#### PCAP-complete child attach 2

- log parent request: `00:08:35.997`
- log parent response: `00:08:36.105`
- log child id request: `00:08:36.402`
- log child id response: `00:08:36.503`
- parent ipv6: `fe80:0:0:0:101c:3f8d:dcd7:3a7c`
- parent extaddr: `121c3f8ddcd73a7c`
- parent rloc16: `0xd400`
- child extaddr: `c2f897fb569546a1`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **43 ms**
- Response -> Child ID Request: **347 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **453 ms**
- pcap parent request: `00:08:36.043` (frame 85)
- pcap parent response: `00:08:36.086` (frame 87)
- pcap child id request: `00:08:36.433` (frame 89)
- pcap child id response: `00:08:36.496` (frame 91)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260628-001438-run06.log`

- manifest status: `completed`
- child extaddr: `a2953142924157a5`
- switch target extaddr(s): `2625b5beed404a21, 2625b5beed404a21, 2625b5beed404a21`

#### PCAP-complete child attach 1

- log parent request: `00:20:19.266`
- log parent response: `00:20:19.331`
- log child id request: `00:20:19.979`
- log child id response: `00:20:20.095`
- parent ipv6: `fe80:0:0:0:b8cd:972b:2e58:9b5`
- parent extaddr: `bacd972b2e5809b5`
- parent rloc16: `0x6c00`
- child extaddr: `a2953142924157a5`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **69 ms**
- Response -> Child ID Request: **713 ms**
- Child ID Request -> Response: **61 ms**
- Full Attach: **843 ms**
- pcap parent request: `00:20:19.248` (frame 75)
- pcap parent response: `00:20:19.317` (frame 76)
- pcap child id request: `00:20:20.030` (frame 82)
- pcap child id response: `00:20:20.091` (frame 84)

#### PCAP-complete child attach 2

- log parent request: `00:20:23.418`
- log parent response: `00:20:23.527`
- log child id request: `00:20:23.826`
- log child id response: `00:20:23.924`
- parent ipv6: `fe80:0:0:0:2425:b5be:ed40:4a21`
- parent extaddr: `2625b5beed404a21`
- parent rloc16: `0x1c00`
- child extaddr: `a2953142924157a5`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **41 ms**
- Response -> Child ID Request: **346 ms**
- Child ID Request -> Response: **66 ms**
- Full Attach: **453 ms**
- pcap parent request: `00:20:23.465` (frame 86)
- pcap parent response: `00:20:23.506` (frame 88)
- pcap child id request: `00:20:23.852` (frame 90)
- pcap child id response: `00:20:23.918` (frame 92)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260628-002625-run07.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `56a778c1f0bc2cf6`
- switch target extaddr(s): `964607a520c17a01, 964607a520c17a01, 964607a520c17a01`

#### PCAP-complete child attach 1

- log parent request: `00:32:06.539`
- log parent response: `00:32:06.691`
- log child id request: `00:32:07.249`
- log child id response: `00:32:07.339`
- parent ipv6: `fe80:0:0:0:a8a9:8aad:e467:f490`
- parent extaddr: `aaa98aade467f490`
- parent rloc16: `0xc400`
- child extaddr: `56a778c1f0bc2cf6`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **155 ms**
- Response -> Child ID Request: **594 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **813 ms**
- pcap parent request: `00:32:06.522` (frame 76)
- pcap parent response: `00:32:06.677` (frame 77)
- pcap child id request: `00:32:07.271` (frame 81)
- pcap child id response: `00:32:07.335` (frame 83)

#### PCAP-complete child attach 2

- log parent request: `00:32:10.794`
- log parent response: `00:32:10.902`
- log child id request: `00:32:11.194`
- log child id response: `00:32:11.292`
- parent ipv6: `fe80:0:0:0:9446:7a5:20c1:7a01`
- parent extaddr: `964607a520c17a01`
- parent rloc16: `0xa000`
- child extaddr: `56a778c1f0bc2cf6`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **40 ms**
- Response -> Child ID Request: **340 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **442 ms**
- pcap parent request: `00:32:10.840` (frame 85)
- pcap parent response: `00:32:10.880` (frame 87)
- pcap child id request: `00:32:11.220` (frame 89)
- pcap child id response: `00:32:11.282` (frame 91)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260628-003813-run08.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `7a17981879b302da`
- switch target extaddr(s): `8280e462dcbda1e3, 8280e462dcbda1e3, 8280e462dcbda1e3`

#### PCAP-complete child attach 1

- log parent request: `00:43:54.168`
- log parent response: `00:43:54.308`
- log child id request: `00:43:54.920`
- log child id response: `00:43:54.966`
- parent ipv6: `fe80:0:0:0:e4d8:b014:bc42:2b06`
- parent extaddr: `e6d8b014bc422b06`
- parent rloc16: `0x8000`
- child extaddr: `7a17981879b302da`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **144 ms**
- Response -> Child ID Request: **604 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **812 ms**
- pcap parent request: `00:43:54.150` (frame 75)
- pcap parent response: `00:43:54.294` (frame 76)
- pcap child id request: `00:43:54.898` (frame 80)
- pcap child id response: `00:43:54.962` (frame 82)

#### PCAP-complete child attach 2

- log parent request: `00:43:58.441`
- log parent response: `00:43:58.550`
- log child id request: `00:43:58.848`
- log child id response: `00:43:58.947`
- parent ipv6: `fe80:0:0:0:8080:e462:dcbd:a1e3`
- parent extaddr: `8280e462dcbda1e3`
- parent rloc16: `0x0000`
- child extaddr: `7a17981879b302da`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **40 ms**
- Response -> Child ID Request: **346 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **448 ms**
- pcap parent request: `00:43:58.488` (frame 84)
- pcap parent response: `00:43:58.528` (frame 86)
- pcap child id request: `00:43:58.874` (frame 89)
- pcap child id response: `00:43:58.936` (frame 91)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260628-005000-run09.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `22d1b7c0794c163d`
- switch target extaddr(s): `b22de6f44202e2c0, b22de6f44202e2c0, b22de6f44202e2c0`

#### PCAP-complete child attach 1

- log parent request: `00:55:41.632`
- log parent response: `00:55:41.924`
- log child id request: `00:55:42.341`
- log child id response: `00:55:42.431`
- parent ipv6: `fe80:0:0:0:494:4d6d:543a:3d5c`
- parent extaddr: `06944d6d543a3d5c`
- parent rloc16: `0x2000`
- child extaddr: `22d1b7c0794c163d`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **295 ms**
- Response -> Child ID Request: **454 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **813 ms**
- pcap parent request: `00:55:41.615` (frame 81)
- pcap parent response: `00:55:41.910` (frame 82)
- pcap child id request: `00:55:42.364` (frame 86)
- pcap child id response: `00:55:42.428` (frame 88)

#### PCAP-complete child attach 2

- log parent request: `00:55:45.681`
- log parent response: `00:55:45.788`
- log child id request: `00:55:46.082`
- log child id response: `00:55:46.181`
- parent ipv6: `fe80:0:0:0:b02d:e6f4:4202:e2c0`
- parent extaddr: `b22de6f44202e2c0`
- parent rloc16: `0xa800`
- child extaddr: `22d1b7c0794c163d`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **40 ms**
- Response -> Child ID Request: **341 ms**
- Child ID Request -> Response: **66 ms**
- Full Attach: **447 ms**
- pcap parent request: `00:55:45.729` (frame 90)
- pcap parent response: `00:55:45.769` (frame 92)
- pcap child id request: `00:55:46.110` (frame 94)
- pcap child id response: `00:55:46.176` (frame 96)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260628-010148-run10.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `a69849a6e3b7eb20`
- switch target extaddr(s): `266a10593f3351d7, 266a10593f3351d7, 266a10593f3351d7`

#### PCAP-complete child attach 1

- log parent request: `01:07:28.867`
- log parent response: `01:07:29.086`
- log child id request: `01:07:29.573`
- log child id response: `01:07:29.663`
- parent ipv6: `fe80:0:0:0:10f8:9aca:5170:82ca`
- parent extaddr: `12f89aca517082ca`
- parent rloc16: `0xc000`
- child extaddr: `a69849a6e3b7eb20`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **224 ms**
- Response -> Child ID Request: **525 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **813 ms**
- pcap parent request: `01:07:28.847` (frame 78)
- pcap parent response: `01:07:29.071` (frame 79)
- pcap child id request: `01:07:29.596` (frame 83)
- pcap child id response: `01:07:29.660` (frame 85)

#### PCAP-complete child attach 2

- log parent request: `01:07:33.286`
- log parent response: `01:07:33.435`
- log child id request: `01:07:33.735`
- log child id response: `01:07:33.833`
- parent ipv6: `fe80:0:0:0:246a:1059:3f33:51d7`
- parent extaddr: `266a10593f3351d7`
- parent rloc16: `0x3c00`
- child extaddr: `a69849a6e3b7eb20`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **41 ms**
- Response -> Child ID Request: **348 ms**
- Child ID Request -> Response: **61 ms**
- Full Attach: **450 ms**
- pcap parent request: `01:07:33.373` (frame 89)
- pcap parent response: `01:07:33.414` (frame 91)
- pcap child id request: `01:07:33.762` (frame 93)
- pcap child id response: `01:07:33.823` (frame 95)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260628-011335-run11.log`

- manifest status: `completed`
- child extaddr: `427248b657caed5b`
- switch target extaddr(s): `02449cc53251369d, 02449cc53251369d, 02449cc53251369d`

#### PCAP-complete child attach 1

- log parent request: `01:19:16.664`
- log parent response: `01:19:17.030`
- log child id request: `01:19:17.436`
- log child id response: `01:19:17.527`
- parent ipv6: `fe80:0:0:0:741e:85a7:aa09:4df0`
- parent extaddr: `761e85a7aa094df0`
- parent rloc16: `0x5c00`
- child extaddr: `427248b657caed5b`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **307 ms**
- Response -> Child ID Request: **444 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **815 ms**
- pcap parent request: `01:19:16.709` (frame 81)
- pcap parent response: `01:19:17.016` (frame 82)
- pcap child id request: `01:19:17.460` (frame 86)
- pcap child id response: `01:19:17.524` (frame 88)

#### PCAP-complete child attach 2

- log parent request: `01:19:20.918`
- log parent response: `01:19:21.030`
- log child id request: `01:19:21.325`
- log child id response: `01:19:21.428`
- parent ipv6: `fe80:0:0:0:44:9cc5:3251:369d`
- parent extaddr: `02449cc53251369d`
- parent rloc16: `0x9c00`
- child extaddr: `427248b657caed5b`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **40 ms**
- Response -> Child ID Request: **350 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **453 ms**
- pcap parent request: `01:19:20.969` (frame 90)
- pcap parent response: `01:19:21.009` (frame 92)
- pcap child id request: `01:19:21.359` (frame 94)
- pcap child id response: `01:19:21.422` (frame 96)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260628-012523-run12.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `8241cc41a593c86f`
- switch target extaddr(s): `1a1d90b39a88c099, 1a1d90b39a88c099, 1a1d90b39a88c099`

#### PCAP-complete child attach 1

- log parent request: `01:31:04.183`
- log parent response: `01:31:04.307`
- log child id request: `01:31:04.892`
- log child id response: `01:31:04.982`
- parent ipv6: `fe80:0:0:0:e855:3acd:ac6f:224`
- parent extaddr: `ea553acdac6f0224`
- parent rloc16: `0xb000`
- child extaddr: `8241cc41a593c86f`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **125 ms**
- Response -> Child ID Request: **624 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **812 ms**
- pcap parent request: `01:31:04.165` (frame 79)
- pcap parent response: `01:31:04.290` (frame 80)
- pcap child id request: `01:31:04.914` (frame 84)
- pcap child id response: `01:31:04.977` (frame 86)

#### PCAP-complete child attach 2

- log parent request: `01:31:08.572`
- log parent response: `01:31:08.681`
- log child id request: `01:31:08.977`
- log child id response: `01:31:09.081`
- parent ipv6: `fe80:0:0:0:181d:90b3:9a88:c099`
- parent extaddr: `1a1d90b39a88c099`
- parent rloc16: `0x8400`
- child extaddr: `8241cc41a593c86f`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **39 ms**
- Response -> Child ID Request: **349 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **452 ms**
- pcap parent request: `01:31:08.619` (frame 90)
- pcap parent response: `01:31:08.658` (frame 92)
- pcap child id request: `01:31:09.007` (frame 94)
- pcap child id response: `01:31:09.071` (frame 96)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260628-013710-run13.log`

- manifest status: `completed`
- child extaddr: `6e0d2d7902e4f730`
- switch target extaddr(s): `8201ebd3574c3bd3, 8201ebd3574c3bd3, 8201ebd3574c3bd3`

#### PCAP-complete child attach 1

- log parent request: `01:42:52.072`
- log parent response: `01:42:52.175`
- log child id request: `01:42:52.843`
- log child id response: `01:42:52.935`
- parent ipv6: `fe80:0:0:0:44d0:5c9c:a99d:4377`
- parent extaddr: `46d05c9ca99d4377`
- parent rloc16: `0x5c00`
- child extaddr: `6e0d2d7902e4f730`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **45 ms**
- Response -> Child ID Request: **705 ms**
- Child ID Request -> Response: **66 ms**
- Full Attach: **816 ms**
- pcap parent request: `01:42:52.113` (frame 77)
- pcap parent response: `01:42:52.158` (frame 78)
- pcap child id request: `01:42:52.863` (frame 82)
- pcap child id response: `01:42:52.929` (frame 84)

#### PCAP-complete child attach 2

- log parent request: `01:42:56.335`
- log parent response: `01:42:56.442`
- log child id request: `01:42:56.743`
- log child id response: `01:42:56.842`
- parent ipv6: `fe80:0:0:0:8001:ebd3:574c:3bd3`
- parent extaddr: `8201ebd3574c3bd3`
- parent rloc16: `0xd000`
- child extaddr: `6e0d2d7902e4f730`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **40 ms**
- Response -> Child ID Request: **349 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **453 ms**
- pcap parent request: `01:42:56.378` (frame 86)
- pcap parent response: `01:42:56.418` (frame 88)
- pcap child id request: `01:42:56.767` (frame 90)
- pcap child id response: `01:42:56.831` (frame 92)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260628-014858-run14.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `cec1b7313356f983`
- switch target extaddr(s): `ea800c444b442394, ea800c444b442394, ea800c444b442394`

#### PCAP-complete child attach 1

- log parent request: `01:54:39.297`
- log parent response: `01:54:39.767`
- log child id request: `01:54:40.069`
- log child id response: `01:54:40.157`
- parent ipv6: `fe80:0:0:0:7848:c489:ed8a:3b3f`
- parent extaddr: `7a48c489ed8a3b3f`
- parent rloc16: `0xb400`
- child extaddr: `cec1b7313356f983`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **408 ms**
- Response -> Child ID Request: **338 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **809 ms**
- pcap parent request: `01:54:39.342` (frame 73)
- pcap parent response: `01:54:39.750` (frame 74)
- pcap child id request: `01:54:40.088` (frame 78)
- pcap child id response: `01:54:40.151` (frame 80)

#### PCAP-complete child attach 2

- log parent request: `01:54:44.007`
- log parent response: `01:54:44.113`
- log child id request: `01:54:44.416`
- log child id response: `01:54:44.515`
- parent ipv6: `fe80:0:0:0:e880:c44:4b44:2394`
- parent extaddr: `ea800c444b442394`
- parent rloc16: `0xc800`
- child extaddr: `cec1b7313356f983`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **40 ms**
- Response -> Child ID Request: **351 ms**
- Child ID Request -> Response: **61 ms**
- Full Attach: **452 ms**
- pcap parent request: `01:54:44.049` (frame 83)
- pcap parent response: `01:54:44.089` (frame 85)
- pcap child id request: `01:54:44.440` (frame 87)
- pcap child id response: `01:54:44.501` (frame 89)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260628-020046-run15.log`

- manifest status: `completed`
- child extaddr: `b681200e4f1372f8`
- switch target extaddr(s): `1ed8f2bd94e186f0, 1ed8f2bd94e186f0, 1ed8f2bd94e186f0`

#### PCAP-complete child attach 1

- log parent request: `02:06:27.233`
- log parent response: `02:06:27.601`
- log child id request: `02:06:28.004`
- log child id response: `02:06:28.092`
- parent ipv6: `fe80:0:0:0:98da:ba37:3f05:15b7`
- parent extaddr: `9adaba373f0515b7`
- parent rloc16: `0x8800`
- child extaddr: `b681200e4f1372f8`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **309 ms**
- Response -> Child ID Request: **441 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **812 ms**
- pcap parent request: `02:06:27.275` (frame 72)
- pcap parent response: `02:06:27.584` (frame 73)
- pcap child id request: `02:06:28.025` (frame 77)
- pcap child id response: `02:06:28.087` (frame 79)

#### PCAP-complete child attach 2

- log parent request: `02:06:31.545`
- log parent response: `02:06:31.653`
- log child id request: `02:06:31.954`
- log child id response: `02:06:32.053`
- parent ipv6: `fe80:0:0:0:1cd8:f2bd:94e1:86f0`
- parent extaddr: `1ed8f2bd94e186f0`
- parent rloc16: `0x4400`
- child extaddr: `b681200e4f1372f8`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **40 ms**
- Response -> Child ID Request: **348 ms**
- Child ID Request -> Response: **65 ms**
- Full Attach: **453 ms**
- pcap parent request: `02:06:31.591` (frame 81)
- pcap parent response: `02:06:31.631` (frame 83)
- pcap child id request: `02:06:31.979` (frame 85)
- pcap child id response: `02:06:32.044` (frame 87)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260628-021233-run16.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `be5cf9970d422c90`
- switch target extaddr(s): `0ef839c124364e58, 0ef839c124364e58, 0ef839c124364e58`

#### PCAP-complete child attach 1

- log parent request: `02:18:14.623`
- log parent response: `02:18:14.664`
- log child id request: `02:18:15.331`
- log child id response: `02:18:15.421`
- parent ipv6: `fe80:0:0:0:d4fc:45af:4468:ba67`
- parent extaddr: `d6fc45af4468ba67`
- parent rloc16: `0x5800`
- child extaddr: `be5cf9970d422c90`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **46 ms**
- Response -> Child ID Request: **704 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **813 ms**
- pcap parent request: `02:18:14.604` (frame 76)
- pcap parent response: `02:18:14.650` (frame 77)
- pcap child id request: `02:18:15.354` (frame 81)
- pcap child id response: `02:18:15.417` (frame 83)

#### PCAP-complete child attach 2

- log parent request: `02:18:19.164`
- log parent response: `02:18:19.273`
- log child id request: `02:18:19.572`
- log child id response: `02:18:19.669`
- parent ipv6: `fe80:0:0:0:cf8:39c1:2436:4e58`
- parent extaddr: `0ef839c124364e58`
- parent rloc16: `0x2800`
- child extaddr: `be5cf9970d422c90`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **42 ms**
- Response -> Child ID Request: **344 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **449 ms**
- pcap parent request: `02:18:19.213` (frame 86)
- pcap parent response: `02:18:19.255` (frame 88)
- pcap child id request: `02:18:19.599` (frame 90)
- pcap child id response: `02:18:19.662` (frame 92)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260628-022421-run17.log`

- manifest status: `completed`
- child extaddr: `b262ee2a56eb20d4`
- switch target extaddr(s): `fe6b9f159f0099e5, fe6b9f159f0099e5, fe6b9f159f0099e5`

#### PCAP-complete child attach 1

- log parent request: `02:30:02.461`
- log parent response: `02:30:02.816`
- log child id request: `02:30:03.234`
- log child id response: `02:30:03.321`
- parent ipv6: `fe80:0:0:0:82d:e23c:1477:1528`
- parent extaddr: `0a2de23c14771528`
- parent rloc16: `0x9400`
- child extaddr: `b262ee2a56eb20d4`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **296 ms**
- Response -> Child ID Request: **455 ms**
- Child ID Request -> Response: **61 ms**
- Full Attach: **812 ms**
- pcap parent request: `02:30:02.506` (frame 79)
- pcap parent response: `02:30:02.802` (frame 80)
- pcap child id request: `02:30:03.257` (frame 84)
- pcap child id response: `02:30:03.318` (frame 86)

#### PCAP-complete child attach 2

- log parent request: `02:30:06.721`
- log parent response: `02:30:06.831`
- log child id request: `02:30:07.131`
- log child id response: `02:30:07.229`
- parent ipv6: `fe80:0:0:0:fc6b:9f15:9f00:99e5`
- parent extaddr: `fe6b9f159f0099e5`
- parent rloc16: `0x1000`
- child extaddr: `b262ee2a56eb20d4`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **40 ms**
- Response -> Child ID Request: **349 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **453 ms**
- pcap parent request: `02:30:06.769` (frame 90)
- pcap parent response: `02:30:06.809` (frame 92)
- pcap child id request: `02:30:07.158` (frame 94)
- pcap child id response: `02:30:07.222` (frame 96)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260628-023609-run18.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `c6728a4604d0bb7a`
- switch target extaddr(s): `9277051d9ada7d2a, 9277051d9ada7d2a, 9277051d9ada7d2a`

#### PCAP-complete child attach 1

- log parent request: `02:41:49.651`
- log parent response: `02:41:50.049`
- log child id request: `02:41:50.424`
- log child id response: `02:41:50.514`
- parent ipv6: `fe80:0:0:0:ece3:f300:abe5:4833`
- parent extaddr: `eee3f300abe54833`
- parent rloc16: `0x9000`
- child extaddr: `c6728a4604d0bb7a`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **338 ms**
- Response -> Child ID Request: **414 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **815 ms**
- pcap parent request: `02:41:49.696` (frame 81)
- pcap parent response: `02:41:50.034` (frame 82)
- pcap child id request: `02:41:50.448` (frame 86)
- pcap child id response: `02:41:50.511` (frame 88)

#### PCAP-complete child attach 2

- log parent request: `02:41:54.266`
- log parent response: `02:41:54.374`
- log child id request: `02:41:54.677`
- log child id response: `02:41:54.775`
- parent ipv6: `fe80:0:0:0:9077:51d:9ada:7d2a`
- parent extaddr: `9277051d9ada7d2a`
- parent rloc16: `0xc400`
- child extaddr: `c6728a4604d0bb7a`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **39 ms**
- Response -> Child ID Request: **350 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **452 ms**
- pcap parent request: `02:41:54.314` (frame 90)
- pcap parent response: `02:41:54.353` (frame 92)
- pcap child id request: `02:41:54.703` (frame 94)
- pcap child id response: `02:41:54.766` (frame 96)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260628-024756-run19.log`

- manifest status: `completed`
- child extaddr: `8af265a00a2c1832`
- switch target extaddr(s): `1aa32d35bcc09125, 1aa32d35bcc09125, 1aa32d35bcc09125`

#### PCAP-complete child attach 1

- log parent request: `02:53:37.805`
- log parent response: `02:53:37.861`
- log child id request: `02:53:38.515`
- log child id response: `02:53:38.603`
- parent ipv6: `fe80:0:0:0:7ceb:cf86:849b:d559`
- parent extaddr: `7eebcf86849bd559`
- parent rloc16: `0x7800`
- child extaddr: `8af265a00a2c1832`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **57 ms**
- Response -> Child ID Request: **693 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **812 ms**
- pcap parent request: `02:53:37.788` (frame 78)
- pcap parent response: `02:53:37.845` (frame 79)
- pcap child id request: `02:53:38.538` (frame 83)
- pcap child id response: `02:53:38.600` (frame 85)

#### PCAP-complete child attach 2

- log parent request: `02:53:41.862`
- log parent response: `02:53:41.972`
- log child id request: `02:53:42.267`
- log child id response: `02:53:42.370`
- parent ipv6: `fe80:0:0:0:18a3:2d35:bcc0:9125`
- parent extaddr: `1aa32d35bcc09125`
- parent rloc16: `0x5400`
- child extaddr: `8af265a00a2c1832`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **41 ms**
- Response -> Child ID Request: **348 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **452 ms**
- pcap parent request: `02:53:41.910` (frame 89)
- pcap parent response: `02:53:41.951` (frame 91)
- pcap child id request: `02:53:42.299` (frame 93)
- pcap child id response: `02:53:42.362` (frame 95)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260628-025944-run20.log`

- manifest status: `completed`
- child extaddr: `96e620320d4eabae`
- switch target extaddr(s): `e2002f6c90a768f1, e2002f6c90a768f1, e2002f6c90a768f1`

#### PCAP-complete child attach 1

- log parent request: `03:05:24.770`
- log parent response: `03:05:25.040`
- log child id request: `03:05:25.541`
- log child id response: `03:05:25.630`
- parent ipv6: `fe80:0:0:0:e4e7:b5a2:9c44:1fd2`
- parent extaddr: `e6e7b5a29c441fd2`
- parent rloc16: `0x0c00`
- child extaddr: `96e620320d4eabae`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **211 ms**
- Response -> Child ID Request: **538 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **812 ms**
- pcap parent request: `03:05:24.815` (frame 78)
- pcap parent response: `03:05:25.026` (frame 79)
- pcap child id request: `03:05:25.564` (frame 83)
- pcap child id response: `03:05:25.627` (frame 85)

#### PCAP-complete child attach 2

- log parent request: `03:05:29.387`
- log parent response: `03:05:29.494`
- log child id request: `03:05:29.789`
- log child id response: `03:05:29.892`
- parent ipv6: `fe80:0:0:0:e000:2f6c:90a7:68f1`
- parent extaddr: `e2002f6c90a768f1`
- parent rloc16: `0x2c00`
- child extaddr: `96e620320d4eabae`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **39 ms**
- Response -> Child ID Request: **348 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **449 ms**
- pcap parent request: `03:05:29.434` (frame 87)
- pcap parent response: `03:05:29.473` (frame 89)
- pcap child id request: `03:05:29.821` (frame 91)
- pcap child id response: `03:05:29.883` (frame 93)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**
