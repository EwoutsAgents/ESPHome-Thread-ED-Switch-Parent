# Child Log Analysis

## ucast_child

Files analyzed: **20**

- batch folders: `ucast-4router-20runs-20260628-154723`

### PCAP-complete child attach summary

| Attach | Metric | M (SD), ms | n |
| --- | --- | ---: | ---: |
| 1 | Request -> Response | 212.85 (141.22) | 20 |
| 1 | Response -> Child ID Request | 537.45 (141.14) | 20 |
| 1 | Child ID Request -> Response | 66.25 (3.96) | 20 |
| 1 | Full Attach | 816.55 (4.20) | 20 |
| 2 | Request -> Response | 42.60 (3.02) | 20 |
| 2 | Response -> Child ID Request | 78.75 (1.86) | 20 |
| 2 | Child ID Request -> Response | 66.60 (3.78) | 20 |
| 2 | Full Attach | 187.95 (5.16) | 20 |

| Metric | M (SD) | n |
| --- | ---: | ---: |
| Failed TX Attempts per Log | 0.00 (0.00) | 20 |
| Log-only or Partial Sequences per Log | 0.00 (0.00) | 20 |

### `ucast_child_20260628-154842-run01.log`

- manifest status: `completed`
- child extaddr: `36b743bf7e67ef0d`
- switch target extaddr(s): `f680e8ccd89d69b7, f680e8ccd89d69b7, f680e8ccd89d69b7`

#### PCAP-complete child attach 1

- log parent request: `15:54:33.174`
- log parent response: `15:54:33.353`
- log child id request: `15:54:33.894`
- log child id response: `15:54:33.978`
- parent ipv6: `fe80:0:0:0:d8f3:efdd:7d4c:4295`
- parent extaddr: `daf3efdd7d4c4295`
- parent rloc16: `0xf000`
- child extaddr: `36b743bf7e67ef0d`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **421 ms**
- Response -> Child ID Request: **329 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **812 ms**
- pcap parent request: `15:54:33.170` (frame 188)
- pcap parent response: `15:54:33.591` (frame 191)
- pcap child id request: `15:54:33.920` (frame 197)
- pcap child id response: `15:54:33.982` (frame 199)

#### PCAP-complete child attach 2

- log parent request: `15:54:37.801`
- log parent response: `15:54:37.896`
- log child id request: `15:54:37.941`
- log child id response: `15:54:38.033`
- parent ipv6: `fe80:0:0:0:f480:e8cc:d89d:69b7`
- parent extaddr: `f680e8ccd89d69b7`
- parent rloc16: `0x9000`
- child extaddr: `36b743bf7e67ef0d`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **45 ms**
- Response -> Child ID Request: **77 ms**
- Child ID Request -> Response: **69 ms**
- Full Attach: **191 ms**
- pcap parent request: `15:54:37.847` (frame 202)
- pcap parent response: `15:54:37.892` (frame 204)
- pcap child id request: `15:54:37.969` (frame 206)
- pcap child id response: `15:54:38.038` (frame 208)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_child_20260628-160040-run02.log`

- manifest status: `completed`
- child extaddr: `1e24e3d50c358aaa`
- switch target extaddr(s): `62c08da2ddaa46f0, 62c08da2ddaa46f0, 62c08da2ddaa46f0`

#### PCAP-complete child attach 1

- log parent request: `16:06:31.527`
- log parent response: `16:06:31.899`
- log child id request: `16:06:32.295`
- log child id response: `16:06:32.388`
- parent ipv6: `fe80:0:0:0:d8e1:199f:926e:b4b1`
- parent extaddr: `dae1199f926eb4b1`
- parent rloc16: `0x4400`
- child extaddr: `1e24e3d50c358aaa`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **326 ms**
- Response -> Child ID Request: **426 ms**
- Child ID Request -> Response: **71 ms**
- Full Attach: **823 ms**
- pcap parent request: `16:06:31.569` (frame 210)
- pcap parent response: `16:06:31.895` (frame 211)
- pcap child id request: `16:06:32.321` (frame 219)
- pcap child id response: `16:06:32.392` (frame 221)

#### PCAP-complete child attach 2

- log parent request: `16:06:35.607`
- log parent response: `16:06:35.697`
- log child id request: `16:06:35.746`
- log child id response: `16:06:35.837`
- parent ipv6: `fe80:0:0:0:60c0:8da2:ddaa:46f0`
- parent extaddr: `62c08da2ddaa46f0`
- parent rloc16: `0xac00`
- child extaddr: `1e24e3d50c358aaa`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **39 ms**
- Response -> Child ID Request: **82 ms**
- Child ID Request -> Response: **67 ms**
- Full Attach: **188 ms**
- pcap parent request: `16:06:35.652` (frame 225)
- pcap parent response: `16:06:35.691` (frame 227)
- pcap child id request: `16:06:35.773` (frame 229)
- pcap child id response: `16:06:35.840` (frame 231)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_child_20260628-161238-run03.log`

- manifest status: `completed`
- child extaddr: `4e2912c9551e58fc`
- switch target extaddr(s): `6227fdf52454b721, 6227fdf52454b721, 6227fdf52454b721`

#### PCAP-complete child attach 1

- log parent request: `16:18:28.988`
- log parent response: `16:18:29.105`
- log child id request: `16:18:29.755`
- log child id response: `16:18:29.847`
- parent ipv6: `fe80:0:0:0:586f:8560:359a:3cdd`
- parent extaddr: `5a6f8560359a3cdd`
- parent rloc16: `0xb000`
- child extaddr: `4e2912c9551e58fc`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **71 ms**
- Response -> Child ID Request: **680 ms**
- Child ID Request -> Response: **71 ms**
- Full Attach: **822 ms**
- pcap parent request: `16:18:29.030` (frame 212)
- pcap parent response: `16:18:29.101` (frame 213)
- pcap child id request: `16:18:29.781` (frame 221)
- pcap child id response: `16:18:29.852` (frame 223)

#### PCAP-complete child attach 2

- log parent request: `16:18:33.548`
- log parent response: `16:18:33.669`
- log child id request: `16:18:33.715`
- log child id response: `16:18:33.801`
- parent ipv6: `fe80:0:0:0:6027:fdf5:2454:b721`
- parent extaddr: `6227fdf52454b721`
- parent rloc16: `0x6000`
- child extaddr: `4e2912c9551e58fc`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **40 ms**
- Response -> Child ID Request: **80 ms**
- Child ID Request -> Response: **61 ms**
- Full Attach: **181 ms**
- pcap parent request: `16:18:33.624` (frame 226)
- pcap parent response: `16:18:33.664` (frame 228)
- pcap child id request: `16:18:33.744` (frame 230)
- pcap child id response: `16:18:33.805` (frame 232)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_child_20260628-162436-run04.log`

- manifest status: `completed`
- child extaddr: `2accd2505214f9a3`
- switch target extaddr(s): `6292e1b07368f764, 6292e1b07368f764, 6292e1b07368f764`

#### PCAP-complete child attach 1

- log parent request: `16:30:27.250`
- log parent response: `16:30:27.597`
- log child id request: `16:30:28.020`
- log child id response: `16:30:28.105`
- parent ipv6: `fe80:0:0:0:2cae:936e:2bfd:3bd0`
- parent extaddr: `2eae936e2bfd3bd0`
- parent rloc16: `0x4c00`
- child extaddr: `2accd2505214f9a3`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **378 ms**
- Response -> Child ID Request: **375 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **815 ms**
- pcap parent request: `16:30:27.292` (frame 884)
- pcap parent response: `16:30:27.670` (frame 887)
- pcap child id request: `16:30:28.045` (frame 893)
- pcap child id response: `16:30:28.107` (frame 895)

#### PCAP-complete child attach 2

- log parent request: `16:30:31.394`
- log parent response: `16:30:31.491`
- log child id request: `16:30:31.536`
- log child id response: `16:30:31.632`
- parent ipv6: `fe80:0:0:0:6092:e1b0:7368:f764`
- parent extaddr: `6292e1b07368f764`
- parent rloc16: `0xd000`
- child extaddr: `2accd2505214f9a3`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **49 ms**
- Response -> Child ID Request: **78 ms**
- Child ID Request -> Response: **71 ms**
- Full Attach: **198 ms**
- pcap parent request: `16:30:31.437` (frame 897)
- pcap parent response: `16:30:31.486` (frame 899)
- pcap child id request: `16:30:31.564` (frame 901)
- pcap child id response: `16:30:31.635` (frame 903)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_child_20260628-163633-run05.log`

- manifest status: `completed`
- child extaddr: `2ac4337160a877db`
- switch target extaddr(s): `ca1eb81b3ca898ce, ca1eb81b3ca898ce, ca1eb81b3ca898ce`

#### PCAP-complete child attach 1

- log parent request: `16:42:24.927`
- log parent response: `16:42:25.162`
- log child id request: `16:42:25.731`
- log child id response: `16:42:25.786`
- parent ipv6: `fe80:0:0:0:b0fd:ca47:abdd:487c`
- parent extaddr: `b2fdca47abdd487c`
- parent rloc16: `0x9c00`
- child extaddr: `2ac4337160a877db`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **183 ms**
- Response -> Child ID Request: **564 ms**
- Child ID Request -> Response: **69 ms**
- Full Attach: **816 ms**
- pcap parent request: `16:42:24.973` (frame 182)
- pcap parent response: `16:42:25.156` (frame 183)
- pcap child id request: `16:42:25.720` (frame 191)
- pcap child id response: `16:42:25.789` (frame 193)

#### PCAP-complete child attach 2

- log parent request: `16:42:29.690`
- log parent response: `16:42:29.782`
- log child id request: `16:42:29.828`
- log child id response: `16:42:29.917`
- parent ipv6: `fe80:0:0:0:c81e:b81b:3ca8:98ce`
- parent extaddr: `ca1eb81b3ca898ce`
- parent rloc16: `0x1800`
- child extaddr: `2ac4337160a877db`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **41 ms**
- Response -> Child ID Request: **81 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **186 ms**
- pcap parent request: `16:42:29.733` (frame 196)
- pcap parent response: `16:42:29.774` (frame 198)
- pcap child id request: `16:42:29.855` (frame 200)
- pcap child id response: `16:42:29.919` (frame 202)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_child_20260628-164832-run06.log`

- manifest status: `completed`
- child extaddr: `eac973d2674d4688`
- switch target extaddr(s): `a6863afcecc75514, a6863afcecc75514, a6863afcecc75514`

#### PCAP-complete child attach 1

- log parent request: `16:54:23.571`
- log parent response: `16:54:23.626`
- log child id request: `16:54:24.293`
- log child id response: `16:54:24.377`
- parent ipv6: `fe80:0:0:0:14d3:2b87:560e:d685`
- parent extaddr: `16d32b87560ed685`
- parent rloc16: `0xb400`
- child extaddr: `eac973d2674d4688`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **54 ms**
- Response -> Child ID Request: **698 ms**
- Child ID Request -> Response: **61 ms**
- Full Attach: **813 ms**
- pcap parent request: `16:54:23.566` (frame 1040)
- pcap parent response: `16:54:23.620` (frame 1041)
- pcap child id request: `16:54:24.318` (frame 1049)
- pcap child id response: `16:54:24.379` (frame 1051)

#### PCAP-complete child attach 2

- log parent request: `16:54:27.633`
- log parent response: `16:54:27.722`
- log child id request: `16:54:27.768`
- log child id response: `16:54:27.858`
- parent ipv6: `fe80:0:0:0:a486:3afc:ecc7:5514`
- parent extaddr: `a6863afcecc75514`
- parent rloc16: `0x1400`
- child extaddr: `eac973d2674d4688`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **39 ms**
- Response -> Child ID Request: **81 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **184 ms**
- pcap parent request: `16:54:27.676` (frame 1056)
- pcap parent response: `16:54:27.715` (frame 1058)
- pcap child id request: `16:54:27.796` (frame 1060)
- pcap child id response: `16:54:27.860` (frame 1062)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_child_20260628-170030-run07.log`

- manifest status: `completed`
- child extaddr: `8e44acae658d6c90`
- switch target extaddr(s): `5a97ff8a36ba38b5, 5a97ff8a36ba38b5, 5a97ff8a36ba38b5`

#### PCAP-complete child attach 1

- log parent request: `17:06:20.885`
- log parent response: `17:06:21.125`
- log child id request: `17:06:21.653`
- log child id response: `17:06:21.740`
- parent ipv6: `fe80:0:0:0:6c6d:b740:bd0e:b99a`
- parent extaddr: `6e6db740bd0eb99a`
- parent rloc16: `0xe000`
- child extaddr: `8e44acae658d6c90`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **192 ms**
- Response -> Child ID Request: **559 ms**
- Child ID Request -> Response: **65 ms**
- Full Attach: **816 ms**
- pcap parent request: `17:06:20.929` (frame 264)
- pcap parent response: `17:06:21.121` (frame 265)
- pcap child id request: `17:06:21.680` (frame 273)
- pcap child id response: `17:06:21.745` (frame 275)

#### PCAP-complete child attach 2

- log parent request: `17:06:25.623`
- log parent response: `17:06:25.720`
- log child id request: `17:06:25.764`
- log child id response: `17:06:25.859`
- parent ipv6: `fe80:0:0:0:5897:ff8a:36ba:38b5`
- parent extaddr: `5a97ff8a36ba38b5`
- parent rloc16: `0x6c00`
- child extaddr: `8e44acae658d6c90`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **46 ms**
- Response -> Child ID Request: **77 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **193 ms**
- pcap parent request: `17:06:25.670` (frame 279)
- pcap parent response: `17:06:25.716` (frame 281)
- pcap child id request: `17:06:25.793` (frame 283)
- pcap child id response: `17:06:25.863` (frame 285)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_child_20260628-171228-run08.log`

- manifest status: `completed`
- child extaddr: `5217e4952f3ab1a8`
- switch target extaddr(s): `268c65d0d3c58347, 268c65d0d3c58347, 268c65d0d3c58347`

#### PCAP-complete child attach 1

- log parent request: `17:18:18.978`
- log parent response: `17:18:19.056`
- log child id request: `17:18:19.701`
- log child id response: `17:18:19.791`
- parent ipv6: `fe80:0:0:0:c413:4bb1:f2b7:9e53`
- parent extaddr: `c6134bb1f2b79e53`
- parent rloc16: `0x4c00`
- child extaddr: `5217e4952f3ab1a8`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **78 ms**
- Response -> Child ID Request: **674 ms**
- Child ID Request -> Response: **69 ms**
- Full Attach: **821 ms**
- pcap parent request: `17:18:18.974` (frame 172)
- pcap parent response: `17:18:19.052` (frame 173)
- pcap child id request: `17:18:19.726` (frame 181)
- pcap child id response: `17:18:19.795` (frame 183)

#### PCAP-complete child attach 2

- log parent request: `17:18:23.375`
- log parent response: `17:18:23.495`
- log child id request: `17:18:23.537`
- log child id response: `17:18:23.628`
- parent ipv6: `fe80:0:0:0:248c:65d0:d3c5:8347`
- parent extaddr: `268c65d0d3c58347`
- parent rloc16: `0x3000`
- child extaddr: `5217e4952f3ab1a8`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **39 ms**
- Response -> Child ID Request: **81 ms**
- Child ID Request -> Response: **61 ms**
- Full Attach: **181 ms**
- pcap parent request: `17:18:23.450` (frame 187)
- pcap parent response: `17:18:23.489` (frame 189)
- pcap child id request: `17:18:23.570` (frame 191)
- pcap child id response: `17:18:23.631` (frame 193)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_child_20260628-172425-run09.log`

- manifest status: `completed`
- child extaddr: `2abd735723497b22`
- switch target extaddr(s): `3ec7b9748f447e71, 3ec7b9748f447e71, 3ec7b9748f447e71`

#### PCAP-complete child attach 1

- log parent request: `17:30:17.154`
- log parent response: `17:30:17.221`
- log child id request: `17:30:17.877`
- log child id response: `17:30:17.962`
- parent ipv6: `fe80:0:0:0:a087:580a:e96c:12a6`
- parent extaddr: `a287580ae96c12a6`
- parent rloc16: `0x2800`
- child extaddr: `2abd735723497b22`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **105 ms**
- Response -> Child ID Request: **644 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **812 ms**
- pcap parent request: `17:30:17.153` (frame 174)
- pcap parent response: `17:30:17.258` (frame 177)
- pcap child id request: `17:30:17.902` (frame 183)
- pcap child id response: `17:30:17.965` (frame 185)

#### PCAP-complete child attach 2

- log parent request: `17:30:21.502`
- log parent response: `17:30:21.597`
- log child id request: `17:30:21.639`
- log child id response: `17:30:21.736`
- parent ipv6: `fe80:0:0:0:3cc7:b974:8f44:7e71`
- parent extaddr: `3ec7b9748f447e71`
- parent rloc16: `0xf000`
- child extaddr: `2abd735723497b22`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **46 ms**
- Response -> Child ID Request: **78 ms**
- Child ID Request -> Response: **69 ms**
- Full Attach: **193 ms**
- pcap parent request: `17:30:21.547` (frame 187)
- pcap parent response: `17:30:21.593` (frame 189)
- pcap child id request: `17:30:21.671` (frame 191)
- pcap child id response: `17:30:21.740` (frame 193)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_child_20260628-173623-run10.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `4a742b3c063b5d71`
- switch target extaddr(s): `529244b97c7f34c9, 529244b97c7f34c9, 529244b97c7f34c9`

#### PCAP-complete child attach 1

- log parent request: `17:42:14.990`
- log parent response: `17:42:15.054`
- log child id request: `17:42:15.711`
- log child id response: `17:42:15.797`
- parent ipv6: `fe80:0:0:0:45b:b926:82:62cb`
- parent extaddr: `065bb926008262cb`
- parent rloc16: `0xf800`
- child extaddr: `4a742b3c063b5d71`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **106 ms**
- Response -> Child ID Request: **644 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **814 ms**
- pcap parent request: `17:42:14.986` (frame 198)
- pcap parent response: `17:42:15.092` (frame 201)
- pcap child id request: `17:42:15.736` (frame 207)
- pcap child id response: `17:42:15.800` (frame 209)

#### PCAP-complete child attach 2

- log parent request: `17:42:19.530`
- log parent response: `17:42:19.623`
- log child id request: `17:42:19.668`
- log child id response: `17:42:19.762`
- parent ipv6: `fe80:0:0:0:5092:44b9:7c7f:34c9`
- parent extaddr: `529244b97c7f34c9`
- parent rloc16: `0xa800`
- child extaddr: `4a742b3c063b5d71`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **44 ms**
- Response -> Child ID Request: **76 ms**
- Child ID Request -> Response: **71 ms**
- Full Attach: **191 ms**
- pcap parent request: `17:42:19.575` (frame 212)
- pcap parent response: `17:42:19.619` (frame 214)
- pcap child id request: `17:42:19.695` (frame 216)
- pcap child id response: `17:42:19.766` (frame 218)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_child_20260628-174821-run11.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `3a11781c761b5826`
- switch target extaddr(s): `262f9eeb07cc37f6, 262f9eeb07cc37f6, 262f9eeb07cc37f6`

#### PCAP-complete child attach 1

- log parent request: `17:54:12.836`
- log parent response: `17:54:12.996`
- log child id request: `17:54:13.547`
- log child id response: `17:54:13.635`
- parent ipv6: `fe80:0:0:0:d0f5:2145:9c0f:cce5`
- parent extaddr: `d2f521459c0fcce5`
- parent rloc16: `0xe400`
- child extaddr: `3a11781c761b5826`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **207 ms**
- Response -> Child ID Request: **542 ms**
- Child ID Request -> Response: **65 ms**
- Full Attach: **814 ms**
- pcap parent request: `17:54:12.823` (frame 285)
- pcap parent response: `17:54:13.030` (frame 288)
- pcap child id request: `17:54:13.572` (frame 294)
- pcap child id response: `17:54:13.637` (frame 296)

#### PCAP-complete child attach 2

- log parent request: `17:54:17.493`
- log parent response: `17:54:17.583`
- log child id request: `17:54:17.629`
- log child id response: `17:54:17.719`
- parent ipv6: `fe80:0:0:0:242f:9eeb:7cc:37f6`
- parent extaddr: `262f9eeb07cc37f6`
- parent rloc16: `0x6800`
- child extaddr: `3a11781c761b5826`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **40 ms**
- Response -> Child ID Request: **79 ms**
- Child ID Request -> Response: **65 ms**
- Full Attach: **184 ms**
- pcap parent request: `17:54:17.538` (frame 298)
- pcap parent response: `17:54:17.578` (frame 300)
- pcap child id request: `17:54:17.657` (frame 302)
- pcap child id response: `17:54:17.722` (frame 304)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_child_20260628-180019-run12.log`

- manifest status: `completed`
- child extaddr: `ea2a27c6273483ff`
- switch target extaddr(s): `028e11a3fc1eec21, 028e11a3fc1eec21, 028e11a3fc1eec21`

#### PCAP-complete child attach 1

- log parent request: `18:06:11.050`
- log parent response: `18:06:11.252`
- log child id request: `18:06:11.818`
- log child id response: `18:06:11.903`
- parent ipv6: `fe80:0:0:0:e4fb:7bc5:a7a7:8c85`
- parent extaddr: `e6fb7bc5a7a78c85`
- parent rloc16: `0x4400`
- child extaddr: `ea2a27c6273483ff`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **154 ms**
- Response -> Child ID Request: **599 ms**
- Child ID Request -> Response: **61 ms**
- Full Attach: **814 ms**
- pcap parent request: `18:06:11.091` (frame 199)
- pcap parent response: `18:06:11.245` (frame 200)
- pcap child id request: `18:06:11.844` (frame 208)
- pcap child id response: `18:06:11.905` (frame 210)

#### PCAP-complete child attach 2

- log parent request: `18:06:15.647`
- log parent response: `18:06:15.739`
- log child id request: `18:06:15.781`
- log child id response: `18:06:15.880`
- parent ipv6: `fe80:0:0:0:8e:11a3:fc1e:ec21`
- parent extaddr: `028e11a3fc1eec21`
- parent rloc16: `0xf800`
- child extaddr: `ea2a27c6273483ff`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **44 ms**
- Response -> Child ID Request: **79 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **193 ms**
- pcap parent request: `18:06:15.689` (frame 215)
- pcap parent response: `18:06:15.733` (frame 217)
- pcap child id request: `18:06:15.812` (frame 219)
- pcap child id response: `18:06:15.882` (frame 221)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_child_20260628-181218-run13.log`

- manifest status: `completed`
- child extaddr: `a63d3b4301168d72`
- switch target extaddr(s): `36d3912c3493dd95, 36d3912c3493dd95, 36d3912c3493dd95`

#### PCAP-complete child attach 1

- log parent request: `18:18:09.309`
- log parent response: `18:18:09.441`
- log child id request: `18:18:10.030`
- log child id response: `18:18:10.124`
- parent ipv6: `fe80:0:0:0:982e:37bf:2850:ebf3`
- parent extaddr: `9a2e37bf2850ebf3`
- parent rloc16: `0xdc00`
- child extaddr: `a63d3b4301168d72`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **315 ms**
- Response -> Child ID Request: **436 ms**
- Child ID Request -> Response: **71 ms**
- Full Attach: **822 ms**
- pcap parent request: `18:18:09.302` (frame 197)
- pcap parent response: `18:18:09.617` (frame 200)
- pcap child id request: `18:18:10.053` (frame 206)
- pcap child id response: `18:18:10.124` (frame 208)

#### PCAP-complete child attach 2

- log parent request: `18:18:13.649`
- log parent response: `18:18:13.741`
- log child id request: `18:18:13.786`
- log child id response: `18:18:13.879`
- parent ipv6: `fe80:0:0:0:34d3:912c:3493:dd95`
- parent extaddr: `36d3912c3493dd95`
- parent rloc16: `0xc000`
- child extaddr: `a63d3b4301168d72`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **45 ms**
- Response -> Child ID Request: **77 ms**
- Child ID Request -> Response: **69 ms**
- Full Attach: **191 ms**
- pcap parent request: `18:18:13.689` (frame 210)
- pcap parent response: `18:18:13.734` (frame 212)
- pcap child id request: `18:18:13.811` (frame 214)
- pcap child id response: `18:18:13.880` (frame 216)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_child_20260628-182415-run14.log`

- manifest status: `completed`
- child extaddr: `6ed5be5685b2d5ea`
- switch target extaddr(s): `9238bf5b9f73eed6, 9238bf5b9f73eed6, 9238bf5b9f73eed6`

#### PCAP-complete child attach 1

- log parent request: `18:30:07.338`
- log parent response: `18:30:07.478`
- log child id request: `18:30:08.061`
- log child id response: `18:30:08.152`
- parent ipv6: `fe80:0:0:0:f8d6:a8b1:7717:70bb`
- parent extaddr: `fad6a8b1771770bb`
- parent rloc16: `0x4800`
- child extaddr: `6ed5be5685b2d5ea`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **200 ms**
- Response -> Child ID Request: **550 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **820 ms**
- pcap parent request: `18:30:07.333` (frame 1005)
- pcap parent response: `18:30:07.533` (frame 1010)
- pcap child id request: `18:30:08.083` (frame 1014)
- pcap child id response: `18:30:08.153` (frame 1016)

#### PCAP-complete child attach 2

- log parent request: `18:30:11.473`
- log parent response: `18:30:11.566`
- log child id request: `18:30:11.611`
- log child id response: `18:30:11.706`
- parent ipv6: `fe80:0:0:0:9038:bf5b:9f73:eed6`
- parent extaddr: `9238bf5b9f73eed6`
- parent rloc16: `0xcc00`
- child extaddr: `6ed5be5685b2d5ea`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **45 ms**
- Response -> Child ID Request: **77 ms**
- Child ID Request -> Response: **71 ms**
- Full Attach: **193 ms**
- pcap parent request: `18:30:11.513` (frame 1019)
- pcap parent response: `18:30:11.558` (frame 1021)
- pcap child id request: `18:30:11.635` (frame 1023)
- pcap child id response: `18:30:11.706` (frame 1025)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_child_20260628-183613-run15.log`

- manifest status: `completed`
- child extaddr: `12924018dc94e76c`
- switch target extaddr(s): `da6b23ca73ee1247, da6b23ca73ee1247, da6b23ca73ee1247`

#### PCAP-complete child attach 1

- log parent request: `18:42:04.719`
- log parent response: `18:42:04.800`
- log child id request: `18:42:05.439`
- log child id response: `18:42:05.532`
- parent ipv6: `fe80:0:0:0:9839:618a:16b7:6356`
- parent extaddr: `9a39618a16b76356`
- parent rloc16: `0x1c00`
- child extaddr: `12924018dc94e76c`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **80 ms**
- Response -> Child ID Request: **668 ms**
- Child ID Request -> Response: **71 ms**
- Full Attach: **819 ms**
- pcap parent request: `18:42:04.716` (frame 205)
- pcap parent response: `18:42:04.796` (frame 206)
- pcap child id request: `18:42:05.464` (frame 215)
- pcap child id response: `18:42:05.535` (frame 217)

#### PCAP-complete child attach 2

- log parent request: `18:42:09.397`
- log parent response: `18:42:09.486`
- log child id request: `18:42:09.532`
- log child id response: `18:42:09.619`
- parent ipv6: `fe80:0:0:0:d86b:23ca:73ee:1247`
- parent extaddr: `da6b23ca73ee1247`
- parent rloc16: `0xa800`
- child extaddr: `12924018dc94e76c`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **40 ms**
- Response -> Child ID Request: **79 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **182 ms**
- pcap parent request: `18:42:09.440` (frame 220)
- pcap parent response: `18:42:09.480` (frame 222)
- pcap child id request: `18:42:09.559` (frame 224)
- pcap child id response: `18:42:09.622` (frame 226)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_child_20260628-184811-run16.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `faaa44bd2f219453`
- switch target extaddr(s): `965bef987f890922, 965bef987f890922, 965bef987f890922`

#### PCAP-complete child attach 1

- log parent request: `18:54:02.768`
- log parent response: `18:54:02.982`
- log child id request: `18:54:03.537`
- log child id response: `18:54:03.623`
- parent ipv6: `fe80:0:0:0:9cf2:58a0:5f4a:3f1`
- parent extaddr: `9ef258a05f4a03f1`
- parent rloc16: `0x5000`
- child extaddr: `faaa44bd2f219453`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **166 ms**
- Response -> Child ID Request: **586 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **815 ms**
- pcap parent request: `18:54:02.812` (frame 203)
- pcap parent response: `18:54:02.978` (frame 204)
- pcap child id request: `18:54:03.564` (frame 212)
- pcap child id response: `18:54:03.627` (frame 214)

#### PCAP-complete child attach 2

- log parent request: `18:54:07.255`
- log parent response: `18:54:07.343`
- log child id request: `18:54:07.389`
- log child id response: `18:54:07.476`
- parent ipv6: `fe80:0:0:0:945b:ef98:7f89:922`
- parent extaddr: `965bef987f890922`
- parent rloc16: `0x0000`
- child extaddr: `faaa44bd2f219453`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **39 ms**
- Response -> Child ID Request: **80 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **181 ms**
- pcap parent request: `18:54:07.300` (frame 216)
- pcap parent response: `18:54:07.339` (frame 218)
- pcap child id request: `18:54:07.419` (frame 220)
- pcap child id response: `18:54:07.481` (frame 222)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_child_20260628-190009-run17.log`

- manifest status: `completed`
- child extaddr: `def4949e44ebd2f6`
- switch target extaddr(s): `c2af2b37ddbfc7da, c2af2b37ddbfc7da, c2af2b37ddbfc7da`

#### PCAP-complete child attach 1

- log parent request: `19:06:00.675`
- log parent response: `19:06:01.098`
- log child id request: `19:06:01.445`
- log child id response: `19:06:01.535`
- parent ipv6: `fe80:0:0:0:a853:bac7:4ed2:f5d`
- parent extaddr: `aa53bac74ed20f5d`
- parent rloc16: `0x4000`
- child extaddr: `def4949e44ebd2f6`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **489 ms**
- Response -> Child ID Request: **258 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **817 ms**
- pcap parent request: `19:06:00.723` (frame 873)
- pcap parent response: `19:06:01.212` (frame 876)
- pcap child id request: `19:06:01.470` (frame 882)
- pcap child id response: `19:06:01.540` (frame 884)

#### PCAP-complete child attach 2

- log parent request: `19:06:05.418`
- log parent response: `19:06:05.509`
- log child id request: `19:06:05.552`
- log child id response: `19:06:05.643`
- parent ipv6: `fe80:0:0:0:c0af:2b37:ddbf:c7da`
- parent extaddr: `c2af2b37ddbfc7da`
- parent rloc16: `0x2400`
- child extaddr: `def4949e44ebd2f6`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **41 ms**
- Response -> Child ID Request: **81 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **184 ms**
- pcap parent request: `19:06:05.463` (frame 886)
- pcap parent response: `19:06:05.504` (frame 888)
- pcap child id request: `19:06:05.585` (frame 890)
- pcap child id response: `19:06:05.647` (frame 892)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_child_20260628-191207-run18.log`

- manifest status: `completed`
- child extaddr: `5ed5f9fe70862f07`
- switch target extaddr(s): `ba49822f0d87134d, ba49822f0d87134d, ba49822f0d87134d`

#### PCAP-complete child attach 1

- log parent request: `19:17:59.051`
- log parent response: `19:17:59.214`
- log child id request: `19:17:59.820`
- log child id response: `19:17:59.904`
- parent ipv6: `fe80:0:0:0:ec78:b7a5:6532:3e2c`
- parent extaddr: `ee78b7a565323e2c`
- parent rloc16: `0x4800`
- child extaddr: `5ed5f9fe70862f07`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **116 ms**
- Response -> Child ID Request: **636 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **815 ms**
- pcap parent request: `19:17:59.090` (frame 1314)
- pcap parent response: `19:17:59.206` (frame 1315)
- pcap child id request: `19:17:59.842` (frame 1324)
- pcap child id response: `19:17:59.905` (frame 1326)

#### PCAP-complete child attach 2

- log parent request: `19:18:03.348`
- log parent response: `19:18:03.441`
- log child id request: `19:18:03.486`
- log child id response: `19:18:03.580`
- parent ipv6: `fe80:0:0:0:b849:822f:d87:134d`
- parent extaddr: `ba49822f0d87134d`
- parent rloc16: `0xb400`
- child extaddr: `5ed5f9fe70862f07`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **44 ms**
- Response -> Child ID Request: **76 ms**
- Child ID Request -> Response: **71 ms**
- Full Attach: **191 ms**
- pcap parent request: `19:18:03.391` (frame 1355)
- pcap parent response: `19:18:03.435` (frame 1357)
- pcap child id request: `19:18:03.511` (frame 1359)
- pcap child id response: `19:18:03.582` (frame 1361)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_child_20260628-192405-run19.log`

- manifest status: `completed`
- child extaddr: `5a4499735192875f`
- switch target extaddr(s): `322cb6f9d7345c87, 322cb6f9d7345c87, 322cb6f9d7345c87`

#### PCAP-complete child attach 1

- log parent request: `19:29:56.878`
- log parent response: `19:29:57.282`
- log child id request: `19:29:57.647`
- log child id response: `19:29:57.740`
- parent ipv6: `fe80:0:0:0:14e5:108d:6d0:feef`
- parent extaddr: `16e5108d06d0feef`
- parent rloc16: `0x0000`
- child extaddr: `5a4499735192875f`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **495 ms**
- Response -> Child ID Request: **257 ms**
- Child ID Request -> Response: **71 ms**
- Full Attach: **823 ms**
- pcap parent request: `19:29:56.918` (frame 180)
- pcap parent response: `19:29:57.413` (frame 183)
- pcap child id request: `19:29:57.670` (frame 189)
- pcap child id response: `19:29:57.741` (frame 191)

#### PCAP-complete child attach 2

- log parent request: `19:30:01.178`
- log parent response: `19:30:01.269`
- log child id request: `19:30:01.314`
- log child id response: `19:30:01.402`
- parent ipv6: `fe80:0:0:0:302c:b6f9:d734:5c87`
- parent extaddr: `322cb6f9d7345c87`
- parent rloc16: `0x5c00`
- child extaddr: `5a4499735192875f`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **41 ms**
- Response -> Child ID Request: **79 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **183 ms**
- pcap parent request: `19:30:01.219` (frame 194)
- pcap parent response: `19:30:01.260` (frame 196)
- pcap child id request: `19:30:01.339` (frame 198)
- pcap child id response: `19:30:01.402` (frame 200)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_child_20260628-193603-run20.log`

- manifest status: `completed`
- child extaddr: `72c51c7fe65e1502`
- switch target extaddr(s): `862ddab6897cb2be, 862ddab6897cb2be, 862ddab6897cb2be`

#### PCAP-complete child attach 1

- log parent request: `19:41:54.271`
- log parent response: `19:41:54.444`
- log child id request: `19:41:55.039`
- log child id response: `19:41:55.125`
- parent ipv6: `fe80:0:0:0:2400:7641:f76e:ebaf`
- parent extaddr: `26007641f76eebaf`
- parent rloc16: `0x6800`
- child extaddr: `72c51c7fe65e1502`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **121 ms**
- Response -> Child ID Request: **624 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **808 ms**
- pcap parent request: `19:41:54.317` (frame 231)
- pcap parent response: `19:41:54.438` (frame 232)
- pcap child id request: `19:41:55.062` (frame 240)
- pcap child id response: `19:41:55.125` (frame 242)

#### PCAP-complete child attach 2

- log parent request: `19:41:59.014`
- log parent response: `19:41:59.107`
- log child id request: `19:41:59.152`
- log child id response: `19:41:59.246`
- parent ipv6: `fe80:0:0:0:842d:dab6:897c:b2be`
- parent extaddr: `862ddab6897cb2be`
- parent rloc16: `0x7400`
- child extaddr: `72c51c7fe65e1502`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **45 ms**
- Response -> Child ID Request: **77 ms**
- Child ID Request -> Response: **69 ms**
- Full Attach: **191 ms**
- pcap parent request: `19:41:59.056` (frame 244)
- pcap parent response: `19:41:59.101` (frame 246)
- pcap child id request: `19:41:59.178` (frame 248)
- pcap child id response: `19:41:59.247` (frame 250)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**
