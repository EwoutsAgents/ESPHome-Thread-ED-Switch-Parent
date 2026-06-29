# Child Log Analysis

## mcast_child

Files analyzed: **50**

- batch folders: `mcast-4router-50runs-20260629-014757`

### PCAP-complete child attach summary

| Attach | Metric | M (SD), ms | n |
| --- | --- | ---: | ---: |
| 1 | Request -> Response | 190.06 (95.99) | 50 |
| 1 | Response -> Child ID Request | 557.68 (96.16) | 50 |
| 1 | Child ID Request -> Response | 66.40 (3.73) | 50 |
| 1 | Full Attach | 814.14 (8.91) | 50 |
| 2 | Request -> Response | 300.60 (127.64) | 50 |
| 2 | Response -> Child ID Request | 98.86 (28.80) | 50 |
| 2 | Child ID Request -> Response | 74.70 (52.65) | 50 |
| 2 | Full Attach | 474.16 (139.89) | 50 |
| 3 | Request -> Response | 344.33 (152.61) | 6 |
| 3 | Response -> Child ID Request | 408.50 (153.96) | 6 |
| 3 | Child ID Request -> Response | 69.00 (5.93) | 6 |
| 3 | Full Attach | 821.83 (4.67) | 6 |

| Metric | M (SD) | n |
| --- | ---: | ---: |
| Failed TX Attempts per Log | 7.68 (21.01) | 50 |
| Log-only or Partial Sequences per Log | 0.02 (0.14) | 50 |

### `mcast_child_20260629-014841-run01.log`

- manifest status: `completed`
- child extaddr: `56acb49a172f419d`
- switch target extaddr(s): `463e72daf96a5d10, 463e72daf96a5d10, 463e72daf96a5d10`

#### PCAP-complete child attach 1

- log parent request: `01:54:32.551`
- log parent response: `01:54:32.874`
- log child id request: `01:54:33.320`
- log child id response: `01:54:33.412`
- parent ipv6: `fe80:0:0:0:3c68:af93:ceb9:82f3`
- parent extaddr: `3e68af93ceb982f3`
- parent rloc16: `0x0800`
- child extaddr: `56acb49a172f419d`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **275 ms**
- Response -> Child ID Request: **478 ms**
- Child ID Request -> Response: **69 ms**
- Full Attach: **822 ms**
- pcap parent request: `01:54:32.596` (frame 236)
- pcap parent response: `01:54:32.871` (frame 237)
- pcap child id request: `01:54:33.349` (frame 246)
- pcap child id response: `01:54:33.418` (frame 248)

#### PCAP-complete child attach 2

- log parent request: `01:54:36.656`
- log parent response: `01:54:36.917`
- log child id request: `01:54:37.044`
- log child id response: `01:54:37.138`
- parent ipv6: `fe80:0:0:0:443e:72da:f96a:5d10`
- parent extaddr: `463e72daf96a5d10`
- parent rloc16: `0xd400`
- child extaddr: `56acb49a172f419d`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **340 ms**
- Response -> Child ID Request: **81 ms**
- Child ID Request -> Response: **69 ms**
- Full Attach: **490 ms**
- pcap parent request: `01:54:36.654` (frame 250)
- pcap parent response: `01:54:36.994` (frame 253)
- pcap child id request: `01:54:37.075` (frame 255)
- pcap child id response: `01:54:37.144` (frame 257)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_child_20260629-020039-run02.log`

- manifest status: `completed`
- child extaddr: `c2db3214445e4a40`
- switch target extaddr(s): `ca8eb8f8f5361b82, ca8eb8f8f5361b82, ca8eb8f8f5361b82`

#### PCAP-complete child attach 1

- log parent request: `02:06:30.073`
- log parent response: `02:06:30.301`
- log child id request: `02:06:30.794`
- log child id response: `02:06:30.886`
- parent ipv6: `fe80:0:0:0:9066:616:b656:97fb`
- parent extaddr: `92660616b65697fb`
- parent rloc16: `0x3000`
- child extaddr: `c2db3214445e4a40`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **228 ms**
- Response -> Child ID Request: **523 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **821 ms**
- pcap parent request: `02:06:30.067` (frame 331)
- pcap parent response: `02:06:30.295` (frame 332)
- pcap child id request: `02:06:30.818` (frame 340)
- pcap child id response: `02:06:30.888` (frame 342)

#### PCAP-complete child attach 2

- log parent request: `02:06:34.592`
- log parent response: `02:06:34.940`
- log child id request: `02:06:34.980`
- log child id response: `02:06:35.095`
- parent ipv6: `fe80:0:0:0:c88e:b8f8:f536:1b82`
- parent extaddr: `ca8eb8f8f5361b82`
- parent rloc16: `0xc800`
- child extaddr: `c2db3214445e4a40`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **299 ms**
- Response -> Child ID Request: **73 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **435 ms**
- pcap parent request: `02:06:34.634` (frame 345)
- pcap parent response: `02:06:34.933` (frame 346)
- pcap child id request: `02:06:35.006` (frame 348)
- pcap child id response: `02:06:35.069` (frame 352)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_child_20260629-021236-run03.log`

- manifest status: `completed`
- child extaddr: `2e28913c77d3ad8b`
- switch target extaddr(s): `929857e18bacd66d, 929857e18bacd66d, 929857e18bacd66d`

#### PCAP-complete child attach 1

- log parent request: `02:18:27.776`
- log parent response: `02:18:27.851`
- log child id request: `02:18:28.497`
- log child id response: `02:18:28.589`
- parent ipv6: `fe80:0:0:0:7811:fab6:2721:28c9`
- parent extaddr: `7a11fab6272128c9`
- parent rloc16: `0x8800`
- child extaddr: `2e28913c77d3ad8b`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **232 ms**
- Response -> Child ID Request: **519 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **821 ms**
- pcap parent request: `02:18:27.770` (frame 198)
- pcap parent response: `02:18:28.002` (frame 201)
- pcap child id request: `02:18:28.521` (frame 207)
- pcap child id response: `02:18:28.591` (frame 209)

#### PCAP-complete child attach 2

- log parent request: `02:18:32.398`
- log parent response: `02:18:32.554`
- log child id request: `02:18:32.687`
- log child id response: `02:18:32.781`
- parent ipv6: `fe80:0:0:0:9098:57e1:8bac:d66d`
- parent extaddr: `929857e18bacd66d`
- parent rloc16: `0x1000`
- child extaddr: `2e28913c77d3ad8b`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **145 ms**
- Response -> Child ID Request: **131 ms**
- Child ID Request -> Response: **67 ms**
- Full Attach: **343 ms**
- pcap parent request: `02:18:32.441` (frame 211)
- pcap parent response: `02:18:32.586` (frame 214)
- pcap child id request: `02:18:32.717` (frame 218)
- pcap child id response: `02:18:32.784` (frame 220)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_child_20260629-022434-run04.log`

- manifest status: `completed`
- child extaddr: `926e921c7371f846`
- switch target extaddr(s): `3a2e946ceb827666, 3a2e946ceb827666, 3a2e946ceb827666`

#### PCAP-complete child attach 1

- log parent request: `02:30:25.738`
- log parent response: `02:30:25.927`
- log child id request: `02:30:26.458`
- log child id response: `02:30:26.544`
- parent ipv6: `fe80:0:0:0:d8e6:c03a:af9:d3f1`
- parent extaddr: `dae6c03a0af9d3f1`
- parent rloc16: `0x4c00`
- child extaddr: `926e921c7371f846`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **231 ms**
- Response -> Child ID Request: **520 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **813 ms**
- pcap parent request: `02:30:25.731` (frame 1154)
- pcap parent response: `02:30:25.962` (frame 1157)
- pcap child id request: `02:30:26.482` (frame 1163)
- pcap child id response: `02:30:26.544` (frame 1165)

#### PCAP-complete child attach 2

- log parent request: `02:30:30.260`
- log parent response: `02:30:30.363`
- log child id request: `02:30:30.893`
- log child id response: `02:30:30.986`
- parent ipv6: `fe80:0:0:0:382e:946c:eb82:7666`
- parent extaddr: `3a2e946ceb827666`
- parent rloc16: `0x0800`
- child extaddr: `926e921c7371f846`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **493 ms**
- Response -> Child ID Request: **124 ms**
- Child ID Request -> Response: **69 ms**
- Full Attach: **686 ms**
- pcap parent request: `02:30:30.302` (frame 1169)
- pcap parent response: `02:30:30.795` (frame 1172)
- pcap child id request: `02:30:30.919` (frame 1176)
- pcap child id response: `02:30:30.988` (frame 1178)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_child_20260629-023632-run05.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `c660382f2e2f0534`
- switch target extaddr(s): `56f6073fe7cb2c6f, 56f6073fe7cb2c6f, 56f6073fe7cb2c6f`

#### PCAP-complete child attach 1

- log parent request: `02:42:23.393`
- log parent response: `02:42:23.578`
- log child id request: `02:42:24.200`
- log child id response: `02:42:24.248`
- parent ipv6: `fe80:0:0:0:e003:eb61:82fc:bfd8`
- parent extaddr: `e203eb6182fcbfd8`
- parent rloc16: `0xdc00`
- child extaddr: `c660382f2e2f0534`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **133 ms**
- Response -> Child ID Request: **614 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **811 ms**
- pcap parent request: `02:42:23.440` (frame 197)
- pcap parent response: `02:42:23.573` (frame 198)
- pcap child id request: `02:42:24.187` (frame 206)
- pcap child id response: `02:42:24.251` (frame 208)

#### PCAP-complete child attach 2

- log parent request: `02:42:28.157`
- log parent response: `02:42:28.341`
- log child id request: `02:42:28.471`
- log child id response: `02:42:28.569`
- parent ipv6: `fe80:0:0:0:54f6:73f:e7cb:2c6f`
- parent extaddr: `56f6073fe7cb2c6f`
- parent rloc16: `0x5c00`
- child extaddr: `c660382f2e2f0534`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **134 ms**
- Response -> Child ID Request: **167 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **371 ms**
- pcap parent request: `02:42:28.202` (frame 210)
- pcap parent response: `02:42:28.336` (frame 211)
- pcap child id request: `02:42:28.503` (frame 217)
- pcap child id response: `02:42:28.573` (frame 219)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_child_20260629-024830-run06.log`

- manifest status: `completed`
- child extaddr: `0234d1f975bb353d`
- switch target extaddr(s): `9a6f5f71a7250c84, 9a6f5f71a7250c84, 9a6f5f71a7250c84`

#### PCAP-complete child attach 1

- log parent request: `02:54:22.037`
- log parent response: `02:54:22.198`
- log child id request: `02:54:22.756`
- log child id response: `02:54:22.843`
- parent ipv6: `fe80:0:0:0:3061:81e0:451:ce3c`
- parent extaddr: `326181e00451ce3c`
- parent rloc16: `0x1c00`
- child extaddr: `0234d1f975bb353d`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **390 ms**
- Response -> Child ID Request: **359 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **812 ms**
- pcap parent request: `02:54:22.034` (frame 247)
- pcap parent response: `02:54:22.424` (frame 250)
- pcap child id request: `02:54:22.783` (frame 256)
- pcap child id response: `02:54:22.846` (frame 258)

#### PCAP-complete child attach 2

- log parent request: `02:54:26.131`
- log parent response: `02:54:26.227`
- log child id request: `02:54:26.511`
- log child id response: `02:54:26.635`
- parent ipv6: `fe80:0:0:0:986f:5f71:a725:c84`
- parent extaddr: `9a6f5f71a7250c84`
- parent rloc16: `0x9c00`
- child extaddr: `0234d1f975bb353d`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **282 ms**
- Response -> Child ID Request: **82 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **427 ms**
- pcap parent request: `02:54:26.177` (frame 262)
- pcap parent response: `02:54:26.459` (frame 265)
- pcap child id request: `02:54:26.541` (frame 267)
- pcap child id response: `02:54:26.604` (frame 271)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_child_20260629-030028-run07.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `76cf7ff1620697e8`
- switch target extaddr(s): `06d1596a3cbec87d, 06d1596a3cbec87d, 06d1596a3cbec87d`

#### PCAP-complete child attach 1

- log parent request: `03:06:20.041`
- log parent response: `03:06:20.374`
- log child id request: `03:06:20.808`
- log child id response: `03:06:20.895`
- parent ipv6: `fe80:0:0:0:604c:67c2:d258:87b2`
- parent extaddr: `624c67c2d25887b2`
- parent rloc16: `0xc800`
- child extaddr: `76cf7ff1620697e8`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **313 ms**
- Response -> Child ID Request: **437 ms**
- Child ID Request -> Response: **65 ms**
- Full Attach: **815 ms**
- pcap parent request: `03:06:20.083` (frame 793)
- pcap parent response: `03:06:20.396` (frame 796)
- pcap child id request: `03:06:20.833` (frame 802)
- pcap child id response: `03:06:20.898` (frame 804)

#### PCAP-complete child attach 2

- log parent request: `03:06:24.145`
- log parent response: `03:06:24.273`
- log child id request: `03:06:24.543`
- log child id response: `03:06:24.630`
- parent ipv6: `fe80:0:0:0:4d1:596a:3cbe:c87d`
- parent extaddr: `06d1596a3cbec87d`
- parent rloc16: `0xf000`
- child extaddr: `76cf7ff1620697e8`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **299 ms**
- Response -> Child ID Request: **83 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **444 ms**
- pcap parent request: `03:06:24.189` (frame 808)
- pcap parent response: `03:06:24.488` (frame 815)
- pcap child id request: `03:06:24.571` (frame 817)
- pcap child id response: `03:06:24.633` (frame 819)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_child_20260629-031226-run08.log`

- manifest status: `completed`
- child extaddr: `aa78048140348959`
- switch target extaddr(s): `e68336c6cd00abff, e68336c6cd00abff, e68336c6cd00abff`

#### PCAP-complete child attach 1

- log parent request: `03:18:17.537`
- log parent response: `03:18:17.626`
- log child id request: `03:18:18.260`
- log child id response: `03:18:18.352`
- parent ipv6: `fe80:0:0:0:808d:ea6d:344c:4b2`
- parent extaddr: `828dea6d344c04b2`
- parent rloc16: `0x3c00`
- child extaddr: `aa78048140348959`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **190 ms**
- Response -> Child ID Request: **560 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **820 ms**
- pcap parent request: `03:18:17.536` (frame 1248)
- pcap parent response: `03:18:17.726` (frame 1251)
- pcap child id request: `03:18:18.286` (frame 1257)
- pcap child id response: `03:18:18.356` (frame 1259)

#### PCAP-complete child attach 2

- log parent request: `03:18:22.124`
- log parent response: `03:18:22.322`
- log child id request: `03:18:22.453`
- log child id response: `03:18:22.545`
- parent ipv6: `fe80:0:0:0:e483:36c6:cd00:abff`
- parent extaddr: `e68336c6cd00abff`
- parent rloc16: `0x6000`
- child extaddr: `aa78048140348959`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **262 ms**
- Response -> Child ID Request: **100 ms**
- Child ID Request -> Response: **68 ms**
- Full Attach: **430 ms**
- pcap parent request: `03:18:22.120` (frame 1262)
- pcap parent response: `03:18:22.382` (frame 1267)
- pcap child id request: `03:18:22.482` (frame 1269)
- pcap child id response: `03:18:22.550` (frame 1271)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_child_20260629-032424-run09.log`

- manifest status: `completed`
- child extaddr: `12d6440a7faee431`
- switch target extaddr(s): `a266ca1cf7f94c4c, a266ca1cf7f94c4c, a266ca1cf7f94c4c`

#### PCAP-complete child attach 1

- log parent request: `03:30:15.049`
- log parent response: `03:30:15.354`
- log child id request: `03:30:15.817`
- log child id response: `03:30:15.901`
- parent ipv6: `fe80:0:0:0:8f3:7f62:275:e990`
- parent extaddr: `0af37f620275e990`
- parent rloc16: `0x4000`
- child extaddr: `12d6440a7faee431`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **244 ms**
- Response -> Child ID Request: **476 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **782 ms**
- pcap parent request: `03:30:15.122` (frame 1214)
- pcap parent response: `03:30:15.366` (frame 1217)
- pcap child id request: `03:30:15.842` (frame 1224)
- pcap child id response: `03:30:15.904` (frame 1226)

#### PCAP-complete child attach 2

- log parent request: `03:30:19.841`
- log parent response: `03:30:19.933`
- log child id request: `03:30:20.311`
- log child id response: `03:30:20.410`
- parent ipv6: `fe80:0:0:0:a066:ca1c:f7f9:4c4c`
- parent extaddr: `a266ca1cf7f94c4c`
- parent rloc16: `0x6c00`
- child extaddr: `12d6440a7faee431`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **374 ms**
- Response -> Child ID Request: **80 ms**
- Child ID Request -> Response: **75 ms**
- Full Attach: **529 ms**
- pcap parent request: `03:30:19.885` (frame 1268)
- pcap parent response: `03:30:20.259` (frame 1275)
- pcap child id request: `03:30:20.339` (frame 1277)
- pcap child id response: `03:30:20.414` (frame 1279)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_child_20260629-033622-run10.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `1aafd118c4d1938c`
- switch target extaddr(s): `7ed2cf69dcb9a99b, 7ed2cf69dcb9a99b, 7ed2cf69dcb9a99b`

#### PCAP-complete child attach 1

- log parent request: `03:42:12.968`
- log parent response: `03:42:13.081`
- log child id request: `03:42:13.736`
- log child id response: `03:42:13.823`
- parent ipv6: `fe80:0:0:0:64ec:cb46:4ba1:812b`
- parent extaddr: `66eccb464ba1812b`
- parent rloc16: `0xac00`
- child extaddr: `1aafd118c4d1938c`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **352 ms**
- Response -> Child ID Request: **399 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **814 ms**
- pcap parent request: `03:42:13.011` (frame 191)
- pcap parent response: `03:42:13.363` (frame 195)
- pcap child id request: `03:42:13.762` (frame 201)
- pcap child id response: `03:42:13.825` (frame 203)

#### PCAP-complete child attach 2

- log parent request: `03:42:17.713`
- log parent response: `03:42:17.828`
- log child id request: `03:42:17.873`
- log child id response: `03:42:17.967`
- parent ipv6: `fe80:0:0:0:7cd2:cf69:dcb9:a99b`
- parent extaddr: `7ed2cf69dcb9a99b`
- parent rloc16: `0xa800`
- child extaddr: `1aafd118c4d1938c`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **66 ms**
- Response -> Child ID Request: **77 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **213 ms**
- pcap parent request: `03:42:17.757` (frame 206)
- pcap parent response: `03:42:17.823` (frame 207)
- pcap child id request: `03:42:17.900` (frame 209)
- pcap child id response: `03:42:17.970` (frame 211)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_child_20260629-034820-run11.log`

- manifest status: `completed`
- child extaddr: `7e8a2bfed7f97b3d`
- switch target extaddr(s): `d29b03b8b44c13e4, d29b03b8b44c13e4, d29b03b8b44c13e4`

#### PCAP-complete child attach 1

- log parent request: `03:54:11.098`
- log parent response: `03:54:11.143`
- log child id request: `03:54:11.819`
- log child id response: `03:54:11.903`
- parent ipv6: `fe80:0:0:0:e8e0:c7c4:f92e:aca0`
- parent extaddr: `eae0c7c4f92eaca0`
- parent rloc16: `0x6000`
- child extaddr: `7e8a2bfed7f97b3d`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **44 ms**
- Response -> Child ID Request: **706 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **812 ms**
- pcap parent request: `03:54:11.093` (frame 182)
- pcap parent response: `03:54:11.137` (frame 183)
- pcap child id request: `03:54:11.843` (frame 193)
- pcap child id response: `03:54:11.905` (frame 195)

#### PCAP-complete child attach 2

- log parent request: `03:54:15.706`
- log parent response: `03:54:15.902`
- log child id request: `03:54:16.071`
- log child id response: `03:54:16.164`
- parent ipv6: `fe80:0:0:0:d09b:3b8:b44c:13e4`
- parent extaddr: `d29b03b8b44c13e4`
- parent rloc16: `0xbc00`
- child extaddr: `7e8a2bfed7f97b3d`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **268 ms**
- Response -> Child ID Request: **79 ms**
- Child ID Request -> Response: **69 ms**
- Full Attach: **416 ms**
- pcap parent request: `03:54:15.751` (frame 197)
- pcap parent response: `03:54:16.019` (frame 202)
- pcap child id request: `03:54:16.098` (frame 204)
- pcap child id response: `03:54:16.167` (frame 206)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_child_20260629-040018-run12.log`

- manifest status: `completed`
- child extaddr: `8e49bfe9bbdd8055`
- switch target extaddr(s): `4acd07e4d5b71bf7, 4acd07e4d5b71bf7, 4acd07e4d5b71bf7`

#### PCAP-complete child attach 1

- log parent request: `04:06:09.340`
- log parent response: `04:06:09.563`
- log child id request: `04:06:10.061`
- log child id response: `04:06:10.153`
- parent ipv6: `fe80:0:0:0:c8c2:ee69:c94b:89ee`
- parent extaddr: `cac2ee69c94b89ee`
- parent rloc16: `0x3400`
- child extaddr: `8e49bfe9bbdd8055`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **223 ms**
- Response -> Child ID Request: **527 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **820 ms**
- pcap parent request: `04:06:09.336` (frame 236)
- pcap parent response: `04:06:09.559` (frame 237)
- pcap child id request: `04:06:10.086` (frame 245)
- pcap child id response: `04:06:10.156` (frame 247)

#### PCAP-complete child attach 2

- log parent request: `04:06:13.702`
- log parent response: `04:06:13.812`
- log child id request: `04:06:14.183`
- log child id response: `04:06:14.282`
- parent ipv6: `fe80:0:0:0:48cd:7e4:d5b7:1bf7`
- parent extaddr: `4acd07e4d5b71bf7`
- parent rloc16: `0x6c00`
- child extaddr: `8e49bfe9bbdd8055`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **387 ms**
- Response -> Child ID Request: **77 ms**
- Child ID Request -> Response: **75 ms**
- Full Attach: **539 ms**
- pcap parent request: `04:06:13.747` (frame 251)
- pcap parent response: `04:06:14.134` (frame 256)
- pcap child id request: `04:06:14.211` (frame 258)
- pcap child id response: `04:06:14.286` (frame 260)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_child_20260629-041216-run13.log`

- manifest status: `completed`
- child extaddr: `ae1ad3dd37e6753d`
- switch target extaddr(s): `f2886c0c70ae3292, f2886c0c70ae3292, f2886c0c70ae3292`

#### PCAP-complete child attach 1

- log parent request: `04:18:07.403`
- log parent response: `04:18:07.462`
- log child id request: `04:18:08.126`
- log child id response: `04:18:08.218`
- parent ipv6: `fe80:0:0:0:e48c:f6af:e98c:19b9`
- parent extaddr: `e68cf6afe98c19b9`
- parent rloc16: `0x8800`
- child extaddr: `ae1ad3dd37e6753d`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **81 ms**
- Response -> Child ID Request: **669 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **820 ms**
- pcap parent request: `04:18:07.401` (frame 1279)
- pcap parent response: `04:18:07.482` (frame 1282)
- pcap child id request: `04:18:08.151` (frame 1288)
- pcap child id response: `04:18:08.221` (frame 1290)

#### PCAP-complete child attach 2

- log parent request: `04:18:11.520`
- log parent response: `04:18:11.690`
- log child id request: `04:18:12.109`
- log child id response: `04:18:12.205`
- parent ipv6: `fe80:0:0:0:f088:6c0c:70ae:3292`
- parent extaddr: `f2886c0c70ae3292`
- parent rloc16: `0xbc00`
- child extaddr: `ae1ad3dd37e6753d`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **420 ms**
- Response -> Child ID Request: **153 ms**
- Child ID Request -> Response: **71 ms**
- Full Attach: **644 ms**
- pcap parent request: `04:18:11.564` (frame 1309)
- pcap parent response: `04:18:11.984` (frame 1314)
- pcap child id request: `04:18:12.137` (frame 1319)
- pcap child id response: `04:18:12.208` (frame 1321)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_child_20260629-042413-run14.log`

- manifest status: `completed`
- child extaddr: `a2f8ff292afcbb4b`
- switch target extaddr(s): `ca535fa99057c748, ca535fa99057c748, ca535fa99057c748`

#### PCAP-complete child attach 1

- log parent request: `04:30:04.808`
- log parent response: `04:30:04.911`
- log child id request: `04:30:05.530`
- log child id response: `04:30:05.614`
- parent ipv6: `fe80:0:0:0:1c0c:257e:aa13:62c4`
- parent extaddr: `1e0c257eaa1362c4`
- parent rloc16: `0xe400`
- child extaddr: `a2f8ff292afcbb4b`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **102 ms**
- Response -> Child ID Request: **648 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **812 ms**
- pcap parent request: `04:30:04.804` (frame 302)
- pcap parent response: `04:30:04.906` (frame 303)
- pcap child id request: `04:30:05.554` (frame 311)
- pcap child id response: `04:30:05.616` (frame 313)

#### PCAP-complete child attach 2

- log parent request: `04:30:09.376`
- log parent response: `04:30:09.479`
- log child id request: `04:30:09.999`
- log child id response: `04:30:10.096`
- parent ipv6: `fe80:0:0:0:c853:5fa9:9057:c748`
- parent extaddr: `ca535fa99057c748`
- parent rloc16: `0xb000`
- child extaddr: `a2f8ff292afcbb4b`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **493 ms**
- Response -> Child ID Request: **117 ms**
- Child ID Request -> Response: **69 ms**
- Full Attach: **679 ms**
- pcap parent request: `04:30:09.421` (frame 315)
- pcap parent response: `04:30:09.914` (frame 320)
- pcap child id request: `04:30:10.031` (frame 322)
- pcap child id response: `04:30:10.100` (frame 324)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_child_20260629-043611-run15.log`

- manifest status: `completed`
- child extaddr: `520c70af1d96170a`
- switch target extaddr(s): `f6703ec00b69e63a, f6703ec00b69e63a, f6703ec00b69e63a`

#### PCAP-complete child attach 1

- log parent request: `04:42:02.786`
- log parent response: `04:42:02.874`
- log child id request: `04:42:03.506`
- log child id response: `04:42:03.592`
- parent ipv6: `fe80:0:0:0:ac64:51cc:9265:b633`
- parent extaddr: `ae6451cc9265b633`
- parent rloc16: `0xbc00`
- child extaddr: `520c70af1d96170a`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **87 ms**
- Response -> Child ID Request: **663 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **813 ms**
- pcap parent request: `04:42:02.781` (frame 194)
- pcap parent response: `04:42:02.868` (frame 195)
- pcap child id request: `04:42:03.531` (frame 203)
- pcap child id response: `04:42:03.594` (frame 205)

#### PCAP-complete child attach 2

- log parent request: `04:42:07.474`
- log parent response: `04:42:07.521`
- log child id request: `04:42:07.791`
- log child id response: `04:42:07.883`
- parent ipv6: `fe80:0:0:0:f470:3ec0:b69:e63a`
- parent extaddr: `f6703ec00b69e63a`
- parent rloc16: `0x2400`
- child extaddr: `520c70af1d96170a`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **270 ms**
- Response -> Child ID Request: **79 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **419 ms**
- pcap parent request: `04:42:07.469` (frame 207)
- pcap parent response: `04:42:07.739` (frame 212)
- pcap child id request: `04:42:07.818` (frame 214)
- pcap child id response: `04:42:07.888` (frame 216)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_child_20260629-044809-run16.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `1e335401ef70549e`
- switch target extaddr(s): `ae4cab91c3189b99, ae4cab91c3189b99, ae4cab91c3189b99`

#### PCAP-complete child attach 1

- log parent request: `04:54:00.958`
- log parent response: `04:54:01.013`
- log child id request: `04:54:01.679`
- log child id response: `04:54:01.765`
- parent ipv6: `fe80:0:0:0:6c01:980f:7b5b:7efd`
- parent extaddr: `6e01980f7b5b7efd`
- parent rloc16: `0x1800`
- child extaddr: `1e335401ef70549e`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **53 ms**
- Response -> Child ID Request: **697 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **814 ms**
- pcap parent request: `04:54:00.955` (frame 260)
- pcap parent response: `04:54:01.008` (frame 261)
- pcap child id request: `04:54:01.705` (frame 269)
- pcap child id response: `04:54:01.769` (frame 271)

#### PCAP-complete child attach 2

- log parent request: `04:54:05.263`
- log parent response: `04:54:05.678`
- log child id request: `04:54:05.813`
- log child id response: `04:54:05.900`
- parent ipv6: `fe80:0:0:0:ac4c:ab91:c318:9b99`
- parent extaddr: `ae4cab91c3189b99`
- parent rloc16: `0xe800`
- child extaddr: `1e335401ef70549e`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **385 ms**
- Response -> Child ID Request: **148 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **595 ms**
- pcap parent request: `04:54:05.308` (frame 275)
- pcap parent response: `04:54:05.693` (frame 278)
- pcap child id request: `04:54:05.841` (frame 282)
- pcap child id response: `04:54:05.903` (frame 284)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_child_20260629-050007-run17.log`

- manifest status: `completed`
- child extaddr: `eeef15ed07006e4f`
- switch target extaddr(s): `5258a657070f2025, 5258a657070f2025, 5258a657070f2025`

#### PCAP-complete child attach 1

- log parent request: `05:05:58.835`
- log parent response: `05:05:58.973`
- log child id request: `05:05:59.602`
- log child id response: `05:05:59.685`
- parent ipv6: `fe80:0:0:0:44fe:2c05:d379:e316`
- parent extaddr: `46fe2c05d379e316`
- parent rloc16: `0x2000`
- child extaddr: `eeef15ed07006e4f`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **92 ms**
- Response -> Child ID Request: **659 ms**
- Child ID Request -> Response: **61 ms**
- Full Attach: **812 ms**
- pcap parent request: `05:05:58.877` (frame 201)
- pcap parent response: `05:05:58.969` (frame 202)
- pcap child id request: `05:05:59.628` (frame 210)
- pcap child id response: `05:05:59.689` (frame 212)

#### PCAP-complete child attach 2

- log parent request: `05:06:03.247`
- log parent response: `05:06:03.393`
- log child id request: `05:06:03.571`
- log child id response: `05:06:03.660`
- parent ipv6: `fe80:0:0:0:5058:a657:70f:2025`
- parent extaddr: `5258a657070f2025`
- parent rloc16: `0x6800`
- child extaddr: `eeef15ed07006e4f`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **224 ms**
- Response -> Child ID Request: **83 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **371 ms**
- pcap parent request: `05:06:03.293` (frame 214)
- pcap parent response: `05:06:03.517` (frame 219)
- pcap child id request: `05:06:03.600` (frame 221)
- pcap child id response: `05:06:03.664` (frame 223)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_child_20260629-051205-run18.log`

- manifest status: `completed`
- child extaddr: `960d684069630093`
- switch target extaddr(s): `0a9c8e7cec4d0899, 0a9c8e7cec4d0899, 0a9c8e7cec4d0899`

#### PCAP-complete child attach 1

- log parent request: `05:17:56.592`
- log parent response: `05:17:56.727`
- log child id request: `05:17:57.360`
- log child id response: `05:17:57.445`
- parent ipv6: `fe80:0:0:0:fc93:fe24:80d8:3454`
- parent extaddr: `fe93fe2480d83454`
- parent rloc16: `0x2c00`
- child extaddr: `960d684069630093`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **297 ms**
- Response -> Child ID Request: **454 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **813 ms**
- pcap parent request: `05:17:56.634` (frame 217)
- pcap parent response: `05:17:56.931` (frame 220)
- pcap child id request: `05:17:57.385` (frame 226)
- pcap child id response: `05:17:57.447` (frame 228)

#### PCAP-complete child attach 2

- log parent request: `05:18:01.091`
- log parent response: `05:18:01.161`
- log child id request: `05:18:01.337`
- log child id response: `05:18:01.453`
- parent ipv6: `fe80:0:0:0:89c:8e7c:ec4d:899`
- parent extaddr: `0a9c8e7cec4d0899`
- parent rloc16: `0x1000`
- child extaddr: `960d684069630093`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **199 ms**
- Response -> Child ID Request: **79 ms**
- Child ID Request -> Response: **69 ms**
- Full Attach: **347 ms**
- pcap parent request: `05:18:01.086` (frame 231)
- pcap parent response: `05:18:01.285` (frame 235)
- pcap child id request: `05:18:01.364` (frame 237)
- pcap child id response: `05:18:01.433` (frame 241)

#### PCAP-complete child attach 3

- log parent request: `05:21:57.371`
- log parent response: `05:21:57.417`
- log child id request: `05:21:58.091`
- log child id response: `05:21:58.194`
- parent ipv6: `fe80:0:0:0:89c:8e7c:ec4d:899`
- parent extaddr: `0a9c8e7cec4d0899`
- parent rloc16: `0x1000`
- child extaddr: `960d684069630093`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **400 ms**
- Response -> Child ID Request: **349 ms**
- Child ID Request -> Response: **79 ms**
- Full Attach: **828 ms**
- pcap parent request: `05:21:57.377` (frame 658)
- pcap parent response: `05:21:57.777` (frame 663)
- pcap child id request: `05:21:58.126` (frame 665)
- pcap child id response: `05:21:58.205` (frame 667)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 52: 16, seq 53: 16, seq 54: 16, seq 55: 16
- failed tx by dst: `fe93fe2480d83454`: 63

### `mcast_child_20260629-052403-run19.log`

- manifest status: `completed`
- child extaddr: `0a0fae6221df191d`
- switch target extaddr(s): `12e57451ccbd81f3, 12e57451ccbd81f3, 12e57451ccbd81f3`

#### PCAP-complete child attach 1

- log parent request: `05:29:54.439`
- log parent response: `05:29:54.650`
- log child id request: `05:29:55.247`
- log child id response: `05:29:55.298`
- parent ipv6: `fe80:0:0:0:60f3:bf20:ab5f:9d7e`
- parent extaddr: `62f3bf20ab5f9d7e`
- parent rloc16: `0x7000`
- child extaddr: `0a0fae6221df191d`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **159 ms**
- Response -> Child ID Request: **590 ms**
- Child ID Request -> Response: **67 ms**
- Full Attach: **816 ms**
- pcap parent request: `05:29:54.486` (frame 209)
- pcap parent response: `05:29:54.645` (frame 210)
- pcap child id request: `05:29:55.235` (frame 218)
- pcap child id response: `05:29:55.302` (frame 220)

#### PCAP-complete child attach 2

- log parent request: `05:29:59.203`
- log parent response: `05:29:59.298`
- log child id request: `05:29:59.431`
- log child id response: `05:29:59.530`
- parent ipv6: `fe80:0:0:0:10e5:7451:ccbd:81f3`
- parent extaddr: `12e57451ccbd81f3`
- parent rloc16: `0x0c00`
- child extaddr: `0a0fae6221df191d`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **129 ms**
- Response -> Child ID Request: **84 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **277 ms**
- pcap parent request: `05:29:59.247` (frame 222)
- pcap parent response: `05:29:59.376` (frame 225)
- pcap child id request: `05:29:59.460` (frame 227)
- pcap child id response: `05:29:59.524` (frame 230)

#### PCAP-complete child attach 3

- log parent request: `05:33:55.200`
- log parent response: `05:33:55.420`
- log child id request: `05:33:55.970`
- log child id response: `05:33:56.064`
- parent ipv6: `fe80:0:0:0:bc70:f2c2:2165:1587`
- parent extaddr: `be70f2c221651587`
- parent rloc16: `0xe400`
- child extaddr: `0a0fae6221df191d`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **374 ms**
- Response -> Child ID Request: **379 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **823 ms**
- pcap parent request: `05:33:55.253` (frame 648)
- pcap parent response: `05:33:55.627` (frame 651)
- pcap child id request: `05:33:56.006` (frame 655)
- pcap child id response: `05:33:56.076` (frame 657)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 37: 16, seq 38: 16, seq 39: 16, seq 40: 16
- failed tx by dst: `62f3bf20ab5f9d7e`: 64

### `mcast_child_20260629-053601-run20.log`

- manifest status: `completed`
- child extaddr: `12a8c289e1b49614`
- switch target extaddr(s): `a61cb65a015501e7, a61cb65a015501e7, a61cb65a015501e7`

#### PCAP-complete child attach 1

- log parent request: `05:41:52.551`
- log parent response: `05:41:52.647`
- log child id request: `05:41:53.269`
- log child id response: `05:41:53.360`
- parent ipv6: `fe80:0:0:0:3499:bc3e:468b:3058`
- parent extaddr: `3699bc3e468b3058`
- parent rloc16: `0x6800`
- child extaddr: `12a8c289e1b49614`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **98 ms**
- Response -> Child ID Request: **652 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **820 ms**
- pcap parent request: `05:41:52.546` (frame 318)
- pcap parent response: `05:41:52.644` (frame 319)
- pcap child id request: `05:41:53.296` (frame 327)
- pcap child id response: `05:41:53.366` (frame 329)

#### PCAP-complete child attach 2

- log parent request: `05:41:57.174`
- log parent response: `05:41:57.480`
- log child id request: `05:41:57.750`
- log child id response: `05:41:57.836`
- parent ipv6: `fe80:0:0:0:a41c:b65a:155:1e7`
- parent extaddr: `a61cb65a015501e7`
- parent rloc16: `0x9c00`
- child extaddr: `12a8c289e1b49614`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **430 ms**
- Response -> Child ID Request: **126 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **618 ms**
- pcap parent request: `05:41:57.222` (frame 331)
- pcap parent response: `05:41:57.652` (frame 334)
- pcap child id request: `05:41:57.778` (frame 338)
- pcap child id response: `05:41:57.840` (frame 340)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_child_20260629-054759-run21.log`

- manifest status: `completed`
- child extaddr: `3a2da3415d6dd2be`
- switch target extaddr(s): `9ac44ed1ffbf4eb9, 9ac44ed1ffbf4eb9, 9ac44ed1ffbf4eb9`

#### PCAP-complete child attach 1

- log parent request: `05:53:50.516`
- log parent response: `05:53:50.606`
- log child id request: `05:53:51.237`
- log child id response: `05:53:51.328`
- parent ipv6: `fe80:0:0:0:4cd8:3b0:6f42:83c7`
- parent extaddr: `4ed803b06f4283c7`
- parent rloc16: `0x3c00`
- child extaddr: `3a2da3415d6dd2be`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **280 ms**
- Response -> Child ID Request: **469 ms**
- Child ID Request -> Response: **71 ms**
- Full Attach: **820 ms**
- pcap parent request: `05:53:50.513` (frame 849)
- pcap parent response: `05:53:50.793` (frame 852)
- pcap child id request: `05:53:51.262` (frame 858)
- pcap child id response: `05:53:51.333` (frame 860)

#### PCAP-complete child attach 2

- log parent request: `05:53:55.122`
- log parent response: `05:53:55.414`
- log child id request: `05:53:55.502`
- log child id response: `05:53:55.627`
- parent ipv6: `fe80:0:0:0:98c4:4ed1:ffbf:4eb9`
- parent extaddr: `9ac44ed1ffbf4eb9`
- parent rloc16: `0xd400`
- child extaddr: `3a2da3415d6dd2be`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **243 ms**
- Response -> Child ID Request: **120 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **427 ms**
- pcap parent request: `05:53:55.168` (frame 863)
- pcap parent response: `05:53:55.411` (frame 864)
- pcap child id request: `05:53:55.531` (frame 868)
- pcap child id response: `05:53:55.595` (frame 872)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_child_20260629-055957-run22.log`

- manifest status: `completed`
- child extaddr: `6a4caaa46faf0e01`
- switch target extaddr(s): `f6db0cd5dc38c728, f6db0cd5dc38c728, f6db0cd5dc38c728`

#### PCAP-complete child attach 1

- log parent request: `06:05:48.551`
- log parent response: `06:05:48.882`
- log child id request: `06:05:49.271`
- log child id response: `06:05:49.364`
- parent ipv6: `fe80:0:0:0:88a2:6e67:cd17:8b3e`
- parent extaddr: `8aa26e67cd178b3e`
- parent rloc16: `0x1000`
- child extaddr: `6a4caaa46faf0e01`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **331 ms**
- Response -> Child ID Request: **420 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **821 ms**
- pcap parent request: `06:05:48.547` (frame 197)
- pcap parent response: `06:05:48.878` (frame 198)
- pcap child id request: `06:05:49.298` (frame 206)
- pcap child id response: `06:05:49.368` (frame 208)

#### PCAP-complete child attach 2

- log parent request: `06:05:52.857`
- log parent response: `06:05:53.077`
- log child id request: `06:05:53.305`
- log child id response: `06:05:53.420`
- parent ipv6: `fe80:0:0:0:f4db:cd5:dc38:c728`
- parent extaddr: `f6db0cd5dc38c728`
- parent rloc16: `0x6000`
- child extaddr: `6a4caaa46faf0e01`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **356 ms**
- Response -> Child ID Request: **74 ms**
- Child ID Request -> Response: **71 ms**
- Full Attach: **501 ms**
- pcap parent request: `06:05:52.903` (frame 210)
- pcap parent response: `06:05:53.259` (frame 213)
- pcap child id request: `06:05:53.333` (frame 215)
- pcap child id response: `06:05:53.404` (frame 219)

#### PCAP-complete child attach 3

- log parent request: `06:09:49.032`
- log parent response: `06:09:49.098`
- log child id request: `06:09:49.743`
- log child id response: `06:09:49.850`
- parent ipv6: `fe80:0:0:0:74b1:cdf8:c6df:e35e`
- parent extaddr: `76b1cdf8c6dfe35e`
- parent rloc16: `0xdc00`
- child extaddr: `6a4caaa46faf0e01`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **327 ms**
- Response -> Child ID Request: **437 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **826 ms**
- pcap parent request: `06:09:49.035` (frame 493)
- pcap parent response: `06:09:49.362` (frame 496)
- pcap child id request: `06:09:49.799` (frame 501)
- pcap child id response: `06:09:49.861` (frame 503)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 229: 16, seq 230: 16, seq 231: 16, seq 232: 16
- failed tx by dst: `8aa26e67cd178b3e`: 63

### `mcast_child_20260629-061155-run23.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `7e7289c3fe10042a`
- switch target extaddr(s): `56bcfef8a7dec018, 56bcfef8a7dec018, 56bcfef8a7dec018`

#### PCAP-complete child attach 1

- log parent request: `06:17:46.338`
- log parent response: `06:17:46.508`
- log child id request: `06:17:47.060`
- log child id response: `06:17:47.145`
- parent ipv6: `fe80:0:0:0:94bd:466b:d78b:b057`
- parent extaddr: `96bd466bd78bb057`
- parent rloc16: `0x9000`
- child extaddr: `7e7289c3fe10042a`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **167 ms**
- Response -> Child ID Request: **582 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **812 ms**
- pcap parent request: `06:17:46.336` (frame 184)
- pcap parent response: `06:17:46.503` (frame 185)
- pcap child id request: `06:17:47.085` (frame 193)
- pcap child id response: `06:17:47.148` (frame 195)

#### PCAP-complete child attach 2

- log parent request: `06:17:50.905`
- log parent response: `06:17:51.191`
- log child id request: `06:17:51.322`
- log child id response: `06:17:51.409`
- parent ipv6: `fe80:0:0:0:54bc:fef8:a7de:c018`
- parent extaddr: `56bcfef8a7dec018`
- parent rloc16: `0xa000`
- child extaddr: `7e7289c3fe10042a`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **235 ms**
- Response -> Child ID Request: **164 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **462 ms**
- pcap parent request: `06:17:50.951` (frame 198)
- pcap parent response: `06:17:51.186` (frame 199)
- pcap child id request: `06:17:51.350` (frame 205)
- pcap child id response: `06:17:51.413` (frame 207)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_child_20260629-062353-run24.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `5e007aa4ed7b596c`
- switch target extaddr(s): `12edb475546b6bce, 12edb475546b6bce, 12edb475546b6bce`

#### PCAP-complete child attach 1

- log parent request: `06:29:44.687`
- log parent response: `06:29:44.875`
- log child id request: `06:29:45.405`
- log child id response: `06:29:45.492`
- parent ipv6: `fe80:0:0:0:d8a3:a023:d36a:1370`
- parent extaddr: `daa3a023d36a1370`
- parent rloc16: `0xf400`
- child extaddr: `5e007aa4ed7b596c`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **187 ms**
- Response -> Child ID Request: **563 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **814 ms**
- pcap parent request: `06:29:44.682` (frame 267)
- pcap parent response: `06:29:44.869` (frame 268)
- pcap child id request: `06:29:45.432` (frame 276)
- pcap child id response: `06:29:45.496` (frame 278)

#### PCAP-complete child attach 2

- log parent request: `06:29:48.684`
- log parent response: `06:29:48.787`
- log child id request: `06:29:49.235`
- log child id response: `06:29:49.334`
- parent ipv6: `fe80:0:0:0:10ed:b475:546b:6bce`
- parent extaddr: `12edb475546b6bce`
- parent rloc16: `0xc000`
- child extaddr: `5e007aa4ed7b596c`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **413 ms**
- Response -> Child ID Request: **122 ms**
- Child ID Request -> Response: **76 ms**
- Full Attach: **611 ms**
- pcap parent request: `06:29:48.729` (frame 280)
- pcap parent response: `06:29:49.142` (frame 285)
- pcap child id request: `06:29:49.264` (frame 289)
- pcap child id response: `06:29:49.340` (frame 291)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_child_20260629-063551-run25.log`

- manifest status: `completed`
- child extaddr: `62d558a9193ba56b`
- switch target extaddr(s): `a229a36ed4d2254a, a229a36ed4d2254a, a229a36ed4d2254a`

#### PCAP-complete child attach 1

- log parent request: `06:41:42.539`
- log parent response: `06:41:42.683`
- log child id request: `06:41:43.259`
- log child id response: `06:41:43.343`
- parent ipv6: `fe80:0:0:0:c40b:e0d7:8f27:296`
- parent extaddr: `c60be0d78f270296`
- parent rloc16: `0x4800`
- child extaddr: `62d558a9193ba56b`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **141 ms**
- Response -> Child ID Request: **608 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **812 ms**
- pcap parent request: `06:41:42.536` (frame 230)
- pcap parent response: `06:41:42.677` (frame 231)
- pcap child id request: `06:41:43.285` (frame 239)
- pcap child id response: `06:41:43.348` (frame 241)

#### PCAP-complete child attach 2

- log parent request: `06:41:46.857`
- log parent response: `06:41:46.995`
- log child id request: `06:41:47.201`
- log child id response: `06:41:47.300`
- parent ipv6: `fe80:0:0:0:a029:a36e:d4d2:254a`
- parent extaddr: `a229a36ed4d2254a`
- parent rloc16: `0xb400`
- child extaddr: `62d558a9193ba56b`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **252 ms**
- Response -> Child ID Request: **81 ms**
- Child ID Request -> Response: **71 ms**
- Full Attach: **404 ms**
- pcap parent request: `06:41:46.901` (frame 246)
- pcap parent response: `06:41:47.153` (frame 251)
- pcap child id request: `06:41:47.234` (frame 253)
- pcap child id response: `06:41:47.305` (frame 255)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_child_20260629-064749-run26.log`

- manifest status: `completed`
- child extaddr: `025f960e1404fd25`
- switch target extaddr(s): `9e2ef80c77a646ac, 9e2ef80c77a646ac, 9e2ef80c77a646ac`

#### PCAP-complete child attach 1

- log parent request: `06:53:40.287`
- log parent response: `06:53:40.376`
- log child id request: `06:53:41.007`
- log child id response: `06:53:41.100`
- parent ipv6: `fe80:0:0:0:88ed:36df:1b8:6761`
- parent extaddr: `8aed36df01b86761`
- parent rloc16: `0x4800`
- child extaddr: `025f960e1404fd25`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **359 ms**
- Response -> Child ID Request: **392 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **821 ms**
- pcap parent request: `06:53:40.285` (frame 1099)
- pcap parent response: `06:53:40.644` (frame 1104)
- pcap child id request: `06:53:41.036` (frame 1108)
- pcap child id response: `06:53:41.106` (frame 1110)

#### PCAP-complete child attach 2

- log parent request: `06:53:44.775`
- log parent response: `06:53:44.896`
- log child id request: `06:53:44.945`
- log child id response: `06:53:45.035`
- parent ipv6: `fe80:0:0:0:9c2e:f80c:77a6:46ac`
- parent extaddr: `9e2ef80c77a646ac`
- parent rloc16: `0x0400`
- child extaddr: `025f960e1404fd25`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **72 ms**
- Response -> Child ID Request: **81 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **217 ms**
- pcap parent request: `06:53:44.821` (frame 1113)
- pcap parent response: `06:53:44.893` (frame 1114)
- pcap child id request: `06:53:44.974` (frame 1116)
- pcap child id response: `06:53:45.038` (frame 1118)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_child_20260629-065947-run27.log`

- manifest status: `completed`
- child extaddr: `4e978d865c520e89`
- switch target extaddr(s): `de6f8c23b4e482a2, de6f8c23b4e482a2, de6f8c23b4e482a2`

#### PCAP-complete child attach 1

- log parent request: `07:05:38.417`
- log parent response: `07:05:38.469`
- log child id request: `07:05:39.137`
- log child id response: `07:05:39.228`
- parent ipv6: `fe80:0:0:0:4408:2e1f:2a5c:9da2`
- parent extaddr: `46082e1f2a5c9da2`
- parent rloc16: `0xcc00`
- child extaddr: `4e978d865c520e89`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **51 ms**
- Response -> Child ID Request: **698 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **819 ms**
- pcap parent request: `07:05:38.414` (frame 202)
- pcap parent response: `07:05:38.465` (frame 203)
- pcap child id request: `07:05:39.163` (frame 211)
- pcap child id response: `07:05:39.233` (frame 213)

#### PCAP-complete child attach 2

- log parent request: `07:05:42.360`
- log parent response: `07:05:42.551`
- log child id request: `07:05:42.854`
- log child id response: `07:05:42.938`
- parent ipv6: `fe80:0:0:0:dc6f:8c23:b4e4:82a2`
- parent extaddr: `de6f8c23b4e482a2`
- parent rloc16: `0x6c00`
- child extaddr: `4e978d865c520e89`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **394 ms**
- Response -> Child ID Request: **81 ms**
- Child ID Request -> Response: **61 ms**
- Full Attach: **536 ms**
- pcap parent request: `07:05:42.407` (frame 216)
- pcap parent response: `07:05:42.801` (frame 223)
- pcap child id request: `07:05:42.882` (frame 225)
- pcap child id response: `07:05:42.943` (frame 227)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_child_20260629-071144-run28.log`

- manifest status: `completed`
- child extaddr: `a6146fc596d40d1c`
- switch target extaddr(s): `b2edc4e88c2c742c, b2edc4e88c2c742c, b2edc4e88c2c742c`

#### PCAP-complete child attach 1

- log parent request: `07:17:35.892`
- log parent response: `07:17:36.099`
- log child id request: `07:17:36.662`
- log child id response: `07:17:36.754`
- parent ipv6: `fe80:0:0:0:94d2:b7d6:f9c:af62`
- parent extaddr: `96d2b7d60f9caf62`
- parent rloc16: `0x0400`
- child extaddr: `a6146fc596d40d1c`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **160 ms**
- Response -> Child ID Request: **593 ms**
- Child ID Request -> Response: **69 ms**
- Full Attach: **822 ms**
- pcap parent request: `07:17:35.933` (frame 1220)
- pcap parent response: `07:17:36.093` (frame 1221)
- pcap child id request: `07:17:36.686` (frame 1229)
- pcap child id response: `07:17:36.755` (frame 1231)

#### PCAP-complete child attach 2

- log parent request: `07:17:40.302`
- log parent response: `07:17:40.463`
- log child id request: `07:17:40.708`
- log child id response: `07:17:40.798`
- parent ipv6: `fe80:0:0:0:b0ed:c4e8:8c2c:742c`
- parent extaddr: `b2edc4e88c2c742c`
- parent rloc16: `0xe800`
- child extaddr: `a6146fc596d40d1c`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **313 ms**
- Response -> Child ID Request: **76 ms**
- Child ID Request -> Response: **67 ms**
- Full Attach: **456 ms**
- pcap parent request: `07:17:40.344` (frame 1234)
- pcap parent response: `07:17:40.657` (frame 1237)
- pcap child id request: `07:17:40.733` (frame 1239)
- pcap child id response: `07:17:40.800` (frame 1241)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_child_20260629-072342-run29.log`

- manifest status: `completed`
- child extaddr: `3ec5d535a0f067c3`
- switch target extaddr(s): `7e80fcfa4cf31aad, 7e80fcfa4cf31aad, 7e80fcfa4cf31aad`

#### PCAP-complete child attach 1

- log parent request: `07:29:33.474`
- log parent response: `07:29:33.538`
- log child id request: `07:29:34.195`
- log child id response: `07:29:34.287`
- parent ipv6: `fe80:0:0:0:c02e:9319:d7e:355b`
- parent extaddr: `c22e93190d7e355b`
- parent rloc16: `0xc400`
- child extaddr: `3ec5d535a0f067c3`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **62 ms**
- Response -> Child ID Request: **687 ms**
- Child ID Request -> Response: **71 ms**
- Full Attach: **820 ms**
- pcap parent request: `07:29:33.468` (frame 1107)
- pcap parent response: `07:29:33.530` (frame 1108)
- pcap child id request: `07:29:34.217` (frame 1116)
- pcap child id response: `07:29:34.288` (frame 1118)

#### PCAP-complete child attach 2

- log parent request: `07:29:38.152`
- log parent response: `07:29:38.565`
- log child id request: `07:29:38.718`
- log child id response: `07:29:38.811`
- parent ipv6: `fe80:0:0:0:7c80:fcfa:4cf3:1aad`
- parent extaddr: `7e80fcfa4cf31aad`
- parent rloc16: `0xec00`
- child extaddr: `3ec5d535a0f067c3`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **509 ms**
- Response -> Child ID Request: **91 ms**
- Child ID Request -> Response: **69 ms**
- Full Attach: **669 ms**
- pcap parent request: `07:29:38.143` (frame 1144)
- pcap parent response: `07:29:38.652` (frame 1150)
- pcap child id request: `07:29:38.743` (frame 1152)
- pcap child id response: `07:29:38.812` (frame 1154)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_child_20260629-073540-run30.log`

- manifest status: `completed`
- child extaddr: `061ee07f583ff857`
- switch target extaddr(s): `e6a72836f61c0b33, e6a72836f61c0b33, e6a72836f61c0b33`

#### PCAP-complete child attach 1

- log parent request: `07:41:31.220`
- log parent response: `07:41:31.351`
- log child id request: `07:41:31.929`
- log child id response: `07:41:32.015`
- parent ipv6: `fe80:0:0:0:9c3f:74d2:65dd:6c1a`
- parent extaddr: `9e3f74d265dd6c1a`
- parent rloc16: `0x4400`
- child extaddr: `061ee07f583ff857`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **140 ms**
- Response -> Child ID Request: **611 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **813 ms**
- pcap parent request: `07:41:31.205` (frame 1099)
- pcap parent response: `07:41:31.345` (frame 1100)
- pcap child id request: `07:41:31.956` (frame 1108)
- pcap child id response: `07:41:32.018` (frame 1110)

#### PCAP-complete child attach 2

- log parent request: `07:41:35.885`
- log parent response: `07:41:36.033`
- log child id request: `07:41:36.270`
- log child id response: `07:41:36.364`
- parent ipv6: `fe80:0:0:0:e4a7:2836:f61c:b33`
- parent extaddr: `e6a72836f61c0b33`
- parent rloc16: `0x7800`
- child extaddr: `061ee07f583ff857`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **289 ms**
- Response -> Child ID Request: **80 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **439 ms**
- pcap parent request: `07:41:35.928` (frame 1114)
- pcap parent response: `07:41:36.217` (frame 1117)
- pcap child id request: `07:41:36.297` (frame 1119)
- pcap child id response: `07:41:36.367` (frame 1121)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_child_20260629-074738-run31.log`

- manifest status: `completed`
- child extaddr: `3e24df8be31d87e8`
- switch target extaddr(s): `5aac7d7ac73904af, 5aac7d7ac73904af, 5aac7d7ac73904af`

#### PCAP-complete child attach 1

- log parent request: `07:53:29.674`
- log parent response: `07:53:29.738`
- log child id request: `07:53:30.395`
- log child id response: `07:53:30.486`
- parent ipv6: `fe80:0:0:0:b0c4:72ae:3cef:386f`
- parent extaddr: `b2c472ae3cef386f`
- parent rloc16: `0xe800`
- child extaddr: `3e24df8be31d87e8`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **343 ms**
- Response -> Child ID Request: **408 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **821 ms**
- pcap parent request: `07:53:29.670` (frame 717)
- pcap parent response: `07:53:30.013` (frame 722)
- pcap child id request: `07:53:30.421` (frame 726)
- pcap child id response: `07:53:30.491` (frame 728)

#### PCAP-complete child attach 2

- log parent request: `07:53:33.813`
- log parent response: `07:53:33.970`
- log child id request: `07:53:34.442`
- log child id response: `07:53:34.532`
- parent ipv6: `fe80:0:0:0:58ac:7d7a:c739:4af`
- parent extaddr: `5aac7d7ac73904af`
- parent rloc16: `0xe400`
- child extaddr: `3e24df8be31d87e8`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **520 ms**
- Response -> Child ID Request: **93 ms**
- Child ID Request -> Response: **65 ms**
- Full Attach: **678 ms**
- pcap parent request: `07:53:33.858` (frame 749)
- pcap parent response: `07:53:34.378` (frame 757)
- pcap child id request: `07:53:34.471` (frame 759)
- pcap child id response: `07:53:34.536` (frame 761)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_child_20260629-075936-run32.log`

- manifest status: `completed`
- child extaddr: `5ad441d4825ad883`
- switch target extaddr(s): `8e335fbe3642ab00, 8e335fbe3642ab00, 8e335fbe3642ab00`

#### PCAP-complete child attach 1

- log parent request: `08:05:26.983`
- log parent response: `08:05:27.213`
- log child id request: `08:05:27.703`
- log child id response: `08:05:27.796`
- parent ipv6: `fe80:0:0:0:c8d6:5386:40a6:d24f`
- parent extaddr: `cad6538640a6d24f`
- parent rloc16: `0xa400`
- child extaddr: `5ad441d4825ad883`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **229 ms**
- Response -> Child ID Request: **520 ms**
- Child ID Request -> Response: **71 ms**
- Full Attach: **820 ms**
- pcap parent request: `08:05:26.980` (frame 184)
- pcap parent response: `08:05:27.209` (frame 185)
- pcap child id request: `08:05:27.729` (frame 193)
- pcap child id response: `08:05:27.800` (frame 195)

#### PCAP-complete child attach 2

- log parent request: `08:05:31.540`
- log parent response: `08:05:31.732`
- log child id request: `08:05:31.962`
- log child id response: `08:05:32.052`
- parent ipv6: `fe80:0:0:0:8c33:5fbe:3642:ab00`
- parent extaddr: `8e335fbe3642ab00`
- parent rloc16: `0x0c00`
- child extaddr: `5ad441d4825ad883`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **335 ms**
- Response -> Child ID Request: **74 ms**
- Child ID Request -> Response: **61 ms**
- Full Attach: **470 ms**
- pcap parent request: `08:05:31.585` (frame 199)
- pcap parent response: `08:05:31.920` (frame 206)
- pcap child id request: `08:05:31.994` (frame 208)
- pcap child id response: `08:05:32.055` (frame 210)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_child_20260629-081133-run33.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `f6bcaad47f636f45`
- switch target extaddr(s): `0e4aac76d5d9e86b, 0e4aac76d5d9e86b, 0e4aac76d5d9e86b`

#### PCAP-complete child attach 1

- log parent request: `08:17:25.090`
- log parent response: `08:17:25.190`
- log child id request: `08:17:25.811`
- log child id response: `08:17:25.897`
- parent ipv6: `fe80:0:0:0:5401:c786:4db6:90d6`
- parent extaddr: `5601c7864db690d6`
- parent rloc16: `0xbc00`
- child extaddr: `f6bcaad47f636f45`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **98 ms**
- Response -> Child ID Request: **652 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **814 ms**
- pcap parent request: `08:17:25.084` (frame 228)
- pcap parent response: `08:17:25.182` (frame 229)
- pcap child id request: `08:17:25.834` (frame 237)
- pcap child id response: `08:17:25.898` (frame 239)

#### PCAP-complete child attach 2

- log parent request: `08:17:29.445`
- log parent response: `08:17:29.536`
- log child id request: `08:17:29.626`
- log child id response: `08:17:29.741`
- parent ipv6: `fe80:0:0:0:c4a:ac76:d5d9:e86b`
- parent extaddr: `0e4aac76d5d9e86b`
- parent rloc16: `0x1c00`
- child extaddr: `f6bcaad47f636f45`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **91 ms**
- Response -> Child ID Request: **121 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **282 ms**
- pcap parent request: `08:17:29.439` (frame 242)
- pcap parent response: `08:17:29.530` (frame 243)
- pcap child id request: `08:17:29.651` (frame 247)
- pcap child id response: `08:17:29.721` (frame 251)

#### PCAP-complete child attach 3

- log parent request: `08:21:25.474`
- log parent response: `08:21:25.912`
- log child id request: `08:21:26.196`
- log child id response: `08:21:26.286`
- parent ipv6: `fe80:0:0:0:98b5:6daa:d14d:170d`
- parent extaddr: `9ab56daad14d170d`
- parent rloc16: `0x0800`
- child extaddr: `f6bcaad47f636f45`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **518 ms**
- Response -> Child ID Request: **231 ms**
- Child ID Request -> Response: **69 ms**
- Full Attach: **818 ms**
- pcap parent request: `08:21:25.477` (frame 602)
- pcap parent response: `08:21:25.995` (frame 605)
- pcap child id request: `08:21:26.226` (frame 609)
- pcap child id response: `08:21:26.295` (frame 611)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 3: 16, seq 4: 16, seq 5: 16, seq 6: 16
- failed tx by dst: `5601c7864db690d6`: 63

### `mcast_child_20260629-082331-run34.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `c6b40365febaed6b`
- switch target extaddr(s): `4a828a9af5d17a7d, 4a828a9af5d17a7d, 4a828a9af5d17a7d`

#### PCAP-complete child attach 1

- log parent request: `08:29:22.639`
- log parent response: `08:29:22.832`
- log child id request: `08:29:23.361`
- log child id response: `08:29:23.451`
- parent ipv6: `fe80:0:0:0:38e2:3b9:a17b:a33e`
- parent extaddr: `3ae203b9a17ba33e`
- parent rloc16: `0x1c00`
- child extaddr: `c6b40365febaed6b`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **189 ms**
- Response -> Child ID Request: **561 ms**
- Child ID Request -> Response: **67 ms**
- Full Attach: **817 ms**
- pcap parent request: `08:29:22.633` (frame 172)
- pcap parent response: `08:29:22.822` (frame 173)
- pcap child id request: `08:29:23.383` (frame 181)
- pcap child id response: `08:29:23.450` (frame 183)

#### PCAP-complete child attach 2

- log parent request: `08:29:27.317`
- log parent response: `08:29:27.469`
- log child id request: `08:29:27.772`
- log child id response: `08:29:27.858`
- parent ipv6: `fe80:0:0:0:4882:8a9a:f5d1:7a7d`
- parent extaddr: `4a828a9af5d17a7d`
- parent rloc16: `0x7c00`
- child extaddr: `c6b40365febaed6b`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **358 ms**
- Response -> Child ID Request: **80 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **500 ms**
- pcap parent request: `08:29:27.358` (frame 187)
- pcap parent response: `08:29:27.716` (frame 194)
- pcap child id request: `08:29:27.796` (frame 196)
- pcap child id response: `08:29:27.858` (frame 198)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_child_20260629-083529-run35.log`

- manifest status: `completed`
- child extaddr: `1606e3fbc47be842`
- switch target extaddr(s): `5e0d3604d1d5b41e, 5e0d3604d1d5b41e, 5e0d3604d1d5b41e`

#### PCAP-complete child attach 1

- log parent request: `08:41:20.725`
- log parent response: `08:41:20.842`
- log child id request: `08:41:21.447`
- log child id response: `08:41:21.539`
- parent ipv6: `fe80:0:0:0:e4de:8164:1168:e458`
- parent extaddr: `e6de81641168e458`
- parent rloc16: `0xe000`
- child extaddr: `1606e3fbc47be842`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **115 ms**
- Response -> Child ID Request: **634 ms**
- Child ID Request -> Response: **69 ms**
- Full Attach: **818 ms**
- pcap parent request: `08:41:20.719` (frame 188)
- pcap parent response: `08:41:20.834` (frame 189)
- pcap child id request: `08:41:21.468` (frame 197)
- pcap child id response: `08:41:21.537` (frame 199)

#### PCAP-complete child attach 2

- log parent request: `08:41:25.181`
- log parent response: `08:41:25.538`
- log child id request: `08:41:25.669`
- log child id response: `08:41:25.755`
- parent ipv6: `fe80:0:0:0:5c0d:3604:d1d5:b41e`
- parent extaddr: `5e0d3604d1d5b41e`
- parent rloc16: `0xbc00`
- child extaddr: `1606e3fbc47be842`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **358 ms**
- Response -> Child ID Request: **162 ms**
- Child ID Request -> Response: **61 ms**
- Full Attach: **581 ms**
- pcap parent request: `08:41:25.172` (frame 203)
- pcap parent response: `08:41:25.530` (frame 204)
- pcap child id request: `08:41:25.692` (frame 210)
- pcap child id response: `08:41:25.753` (frame 212)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_child_20260629-084727-run36.log`

- manifest status: `completed`
- child extaddr: `9e82bd2613a3d48a`
- switch target extaddr(s): `da2f8186fe9f4041, da2f8186fe9f4041, da2f8186fe9f4041`

#### PCAP-complete child attach 1

- log parent request: `08:53:18.888`
- log parent response: `08:53:19.088`
- log child id request: `08:53:19.656`
- log child id response: `08:53:19.747`
- parent ipv6: `fe80:0:0:0:84c4:bf5:1f2c:a165`
- parent extaddr: `86c40bf51f2ca165`
- parent rloc16: `0x9000`
- child extaddr: `9e82bd2613a3d48a`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **152 ms**
- Response -> Child ID Request: **597 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **819 ms**
- pcap parent request: `08:53:18.929` (frame 1117)
- pcap parent response: `08:53:19.081` (frame 1118)
- pcap child id request: `08:53:19.678` (frame 1126)
- pcap child id response: `08:53:19.748` (frame 1128)

#### PCAP-complete child attach 2

- log parent request: `08:53:22.996`
- log parent response: `08:53:23.146`
- log child id request: `08:53:23.564`
- log child id response: `08:53:23.657`
- parent ipv6: `fe80:0:0:0:d82f:8186:fe9f:4041`
- parent extaddr: `da2f8186fe9f4041`
- parent rloc16: `0xb000`
- child extaddr: `9e82bd2613a3d48a`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **472 ms**
- Response -> Child ID Request: **79 ms**
- Child ID Request -> Response: **69 ms**
- Full Attach: **620 ms**
- pcap parent request: `08:53:23.038` (frame 1130)
- pcap parent response: `08:53:23.510` (frame 1137)
- pcap child id request: `08:53:23.589` (frame 1139)
- pcap child id response: `08:53:23.658` (frame 1141)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_child_20260629-085925-run37.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `e635f75f8c8bd28b`
- switch target extaddr(s): `8a1bc947e80e7180, 8a1bc947e80e7180, 8a1bc947e80e7180`

#### PCAP-complete child attach 1

- log parent request: `09:05:16.145`
- log parent response: `09:05:16.283`
- log child id request: `09:05:16.867`
- log child id response: `09:05:16.951`
- parent ipv6: `fe80:0:0:0:68b6:525b:d4b4:889d`
- parent extaddr: `6ab6525bd4b4889d`
- parent rloc16: `0x4c00`
- child extaddr: `e635f75f8c8bd28b`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **137 ms**
- Response -> Child ID Request: **614 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **814 ms**
- pcap parent request: `09:05:16.137` (frame 189)
- pcap parent response: `09:05:16.274` (frame 190)
- pcap child id request: `09:05:16.888` (frame 198)
- pcap child id response: `09:05:16.951` (frame 200)

#### PCAP-complete child attach 2

- log parent request: `09:05:20.702`
- log parent response: `09:05:20.755`
- log child id request: `09:05:20.885`
- log child id response: `09:05:20.999`
- parent ipv6: `fe80:0:0:0:881b:c947:e80e:7180`
- parent extaddr: `8a1bc947e80e7180`
- parent rloc16: `0x5400`
- child extaddr: `e635f75f8c8bd28b`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **135 ms**
- Response -> Child ID Request: **80 ms**
- Child ID Request -> Response: **67 ms**
- Full Attach: **282 ms**
- pcap parent request: `09:05:20.694` (frame 203)
- pcap parent response: `09:05:20.829` (frame 206)
- pcap child id request: `09:05:20.909` (frame 208)
- pcap child id response: `09:05:20.976` (frame 212)

#### PCAP-complete child attach 3

- log parent request: `09:09:16.671`
- log parent response: `09:09:16.735`
- log child id request: `09:09:17.393`
- log child id response: `09:09:17.480`
- parent ipv6: `fe80:0:0:0:60cf:8112:1cec:ae74`
- parent extaddr: `62cf81121cecae74`
- parent rloc16: `0xc800`
- child extaddr: `e635f75f8c8bd28b`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **61 ms**
- Response -> Child ID Request: **691 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **816 ms**
- pcap parent request: `09:09:16.672` (frame 584)
- pcap parent response: `09:09:16.733` (frame 585)
- pcap child id request: `09:09:17.424` (frame 591)
- pcap child id response: `09:09:17.488` (frame 593)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 230: 16, seq 231: 16, seq 232: 16, seq 233: 16
- failed tx by dst: `6ab6525bd4b4889d`: 62

### `mcast_child_20260629-091123-run38.log`

- manifest status: `completed`
- child extaddr: `0a6ebca6268d7fbb`
- switch target extaddr(s): `7a0776f67af58220, 7a0776f67af58220, 7a0776f67af58220`

#### PCAP-complete child attach 1

- log parent request: `09:17:14.500`
- log parent response: `09:17:14.719`
- log child id request: `09:17:15.269`
- log child id response: `09:17:15.358`
- parent ipv6: `fe80:0:0:0:e8bf:1fb0:c83e:acb9`
- parent extaddr: `eabf1fb0c83eacb9`
- parent rloc16: `0xec00`
- child extaddr: `0a6ebca6268d7fbb`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **270 ms**
- Response -> Child ID Request: **482 ms**
- Child ID Request -> Response: **65 ms**
- Full Attach: **817 ms**
- pcap parent request: `09:17:14.539` (frame 478)
- pcap parent response: `09:17:14.809` (frame 481)
- pcap child id request: `09:17:15.291` (frame 487)
- pcap child id response: `09:17:15.356` (frame 489)

#### PCAP-complete child attach 2

- log parent request: `09:17:18.710`
- log parent response: `09:17:18.981`
- log child id request: `09:17:19.026`
- log child id response: `09:17:19.113`
- parent ipv6: `fe80:0:0:0:7807:76f6:7af5:8220`
- parent extaddr: `7a0776f67af58220`
- parent rloc16: `0x2800`
- child extaddr: `0a6ebca6268d7fbb`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **271 ms**
- Response -> Child ID Request: **78 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **412 ms**
- pcap parent request: `09:17:18.701` (frame 495)
- pcap parent response: `09:17:18.972` (frame 496)
- pcap child id request: `09:17:19.050` (frame 498)
- pcap child id response: `09:17:19.113` (frame 500)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_child_20260629-092321-run39.log`

- manifest status: `completed`
- child extaddr: `5aed679b9cb4ed42`
- switch target extaddr(s): `eac6dc473ab6c72c, eac6dc473ab6c72c, eac6dc473ab6c72c`

#### PCAP-complete child attach 1

- log parent request: `09:29:11.806`
- log parent response: `09:29:11.984`
- log child id request: `09:29:12.612`
- log child id response: `09:29:12.661`
- parent ipv6: `fe80:0:0:0:cca9:a452:b2b7:6a56`
- parent extaddr: `cea9a452b2b76a56`
- parent rloc16: `0x9000`
- child extaddr: `5aed679b9cb4ed42`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **126 ms**
- Response -> Child ID Request: **622 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **812 ms**
- pcap parent request: `09:29:11.850` (frame 193)
- pcap parent response: `09:29:11.976` (frame 194)
- pcap child id request: `09:29:12.598` (frame 202)
- pcap child id response: `09:29:12.662` (frame 204)

#### PCAP-complete child attach 2

- log parent request: `09:29:16.567`
- log parent response: `09:29:16.846`
- log child id request: `09:29:16.984`
- log child id response: `09:29:17.072`
- parent ipv6: `fe80:0:0:0:e8c6:dc47:3ab6:c72c`
- parent extaddr: `eac6dc473ab6c72c`
- parent rloc16: `0x0000`
- child extaddr: `5aed679b9cb4ed42`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **262 ms**
- Response -> Child ID Request: **139 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **464 ms**
- pcap parent request: `09:29:16.609` (frame 206)
- pcap parent response: `09:29:16.871` (frame 209)
- pcap child id request: `09:29:17.010` (frame 213)
- pcap child id response: `09:29:17.073` (frame 215)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_child_20260629-093519-run40.log`

- manifest status: `completed`
- child extaddr: `8ec0b3c22d7a1178`
- switch target extaddr(s): `0e0b5e984d5e9438, 0e0b5e984d5e9438, 0e0b5e984d5e9438`

#### PCAP-complete child attach 1

- log parent request: `09:41:09.935`
- log parent response: `09:41:10.111`
- log child id request: `09:41:10.655`
- log child id response: `09:41:10.740`
- parent ipv6: `fe80:0:0:0:5cac:f900:68fd:7d25`
- parent extaddr: `5eacf90068fd7d25`
- parent rloc16: `0xe800`
- child extaddr: `8ec0b3c22d7a1178`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **174 ms**
- Response -> Child ID Request: **576 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **812 ms**
- pcap parent request: `09:41:09.930` (frame 213)
- pcap parent response: `09:41:10.104` (frame 214)
- pcap child id request: `09:41:10.680` (frame 222)
- pcap child id response: `09:41:10.742` (frame 224)

#### PCAP-complete child attach 2

- log parent request: `09:41:14.364`
- log parent response: `09:41:14.508`
- log child id request: `09:41:14.977`
- log child id response: `09:41:15.070`
- parent ipv6: `fe80:0:0:0:c0b:5e98:4d5e:9438`
- parent extaddr: `0e0b5e984d5e9438`
- parent rloc16: `0xe400`
- child extaddr: `8ec0b3c22d7a1178`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **517 ms**
- Response -> Child ID Request: **82 ms**
- Child ID Request -> Response: **65 ms**
- Full Attach: **664 ms**
- pcap parent request: `09:41:14.408` (frame 226)
- pcap parent response: `09:41:14.925` (frame 231)
- pcap child id request: `09:41:15.007` (frame 233)
- pcap child id response: `09:41:15.072` (frame 235)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_child_20260629-094716-run41.log`

- manifest status: `completed`
- child extaddr: `8e75039b8cbfef38`
- switch target extaddr(s): `b2b2770142e8e6ff, b2b2770142e8e6ff, b2b2770142e8e6ff`

#### PCAP-complete child attach 1

- log parent request: `09:53:07.409`
- log parent response: `09:53:07.709`
- log child id request: `09:53:08.216`
- log child id response: `09:53:08.278`
- parent ipv6: `fe80:0:0:0:be:2e5f:7928:4b50`
- parent extaddr: `02be2e5f79284b50`
- parent rloc16: `0xe800`
- child extaddr: `8e75039b8cbfef38`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **249 ms**
- Response -> Child ID Request: **502 ms**
- Child ID Request -> Response: **75 ms**
- Full Attach: **826 ms**
- pcap parent request: `09:53:07.454` (frame 406)
- pcap parent response: `09:53:07.703` (frame 407)
- pcap child id request: `09:53:08.205` (frame 415)
- pcap child id response: `09:53:08.280` (frame 417)

#### PCAP-complete child attach 2

- log parent request: `09:53:12.213`
- log parent response: `09:53:12.263`
- log child id request: `09:53:12.462`
- log child id response: `09:53:12.548`
- parent ipv6: `fe80:0:0:0:b0b2:7701:42e8:e6ff`
- parent extaddr: `b2b2770142e8e6ff`
- parent rloc16: `0x2000`
- child extaddr: `8e75039b8cbfef38`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **150 ms**
- Response -> Child ID Request: **135 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **348 ms**
- pcap parent request: `09:53:12.204` (frame 420)
- pcap parent response: `09:53:12.354` (frame 424)
- pcap child id request: `09:53:12.489` (frame 428)
- pcap child id response: `09:53:12.552` (frame 430)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_child_20260629-095914-run42.log`

- manifest status: `completed`
- child extaddr: `2a77325b1cb53c54`
- switch target extaddr(s): `7e6522776a6ae293, 7e6522776a6ae293, 7e6522776a6ae293`

#### PCAP-complete child attach 1

- log parent request: `10:05:05.338`
- log parent response: `10:05:05.443`
- log child id request: `10:05:06.059`
- log child id response: `10:05:06.144`
- parent ipv6: `fe80:0:0:0:6475:2164:f941:d140`
- parent extaddr: `66752164f941d140`
- parent rloc16: `0x1000`
- child extaddr: `2a77325b1cb53c54`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **104 ms**
- Response -> Child ID Request: **647 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **813 ms**
- pcap parent request: `10:05:05.331` (frame 440)
- pcap parent response: `10:05:05.435` (frame 441)
- pcap child id request: `10:05:06.082` (frame 450)
- pcap child id response: `10:05:06.144` (frame 452)

#### PCAP-complete child attach 2

- log parent request: `10:05:10.018`
- log parent response: `10:05:10.113`
- log child id request: `10:05:10.158`
- log child id response: `10:05:10.252`
- parent ipv6: `fe80:0:0:0:7c65:2277:6a6a:e293`
- parent extaddr: `7e6522776a6ae293`
- parent rloc16: `0x6c00`
- child extaddr: `2a77325b1cb53c54`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **47 ms**
- Response -> Child ID Request: **77 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **194 ms**
- pcap parent request: `10:05:10.058` (frame 455)
- pcap parent response: `10:05:10.105` (frame 456)
- pcap child id request: `10:05:10.182` (frame 458)
- pcap child id response: `10:05:10.252` (frame 460)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_child_20260629-101112-run43.log`

- manifest status: `completed`
- child extaddr: `8e00c768f548d84f`
- switch target extaddr(s): `86f5e613d7c3bad3, 86f5e613d7c3bad3, 86f5e613d7c3bad3`

#### PCAP-complete child attach 1

- log parent request: `10:17:03.147`
- log parent response: `10:17:03.235`
- log child id request: `10:17:03.863`
- log child id response: `10:17:03.955`
- parent ipv6: `fe80:0:0:0:a404:76a1:6ced:828c`
- parent extaddr: `a60476a16ced828c`
- parent rloc16: `0xe800`
- child extaddr: `8e00c768f548d84f`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **366 ms**
- Response -> Child ID Request: **382 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **818 ms**
- pcap parent request: `10:17:03.137` (frame 1245)
- pcap parent response: `10:17:03.503` (frame 1248)
- pcap child id request: `10:17:03.885` (frame 1254)
- pcap child id response: `10:17:03.955` (frame 1256)

#### PCAP-complete child attach 2

- log parent request: `10:17:07.748`
- log parent response: `10:17:07.921`
- log child id request: `10:17:08.163`
- log child id response: `10:17:08.252`
- parent ipv6: `fe80:0:0:0:84f5:e613:d7c3:bad3`
- parent extaddr: `86f5e613d7c3bad3`
- parent rloc16: `0x4800`
- child extaddr: `8e00c768f548d84f`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **323 ms**
- Response -> Child ID Request: **76 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **462 ms**
- pcap parent request: `10:17:07.789` (frame 1258)
- pcap parent response: `10:17:08.112` (frame 1263)
- pcap child id request: `10:17:08.188` (frame 1265)
- pcap child id response: `10:17:08.251` (frame 1267)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_child_20260629-102310-run44.log`

- manifest status: `completed`
- child extaddr: `b285da2226f81dd6`
- switch target extaddr(s): `86efb95cfb5c0343, 86efb95cfb5c0343, 86efb95cfb5c0343`

#### PCAP-complete child attach 1

- log parent request: `10:29:01.161`
- log parent response: `10:29:01.239`
- log child id request: `10:29:01.882`
- log child id response: `10:29:01.966`
- parent ipv6: `fe80:0:0:0:e085:5afe:960b:eda2`
- parent extaddr: `e2855afe960beda2`
- parent rloc16: `0xb400`
- child extaddr: `b285da2226f81dd6`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **76 ms**
- Response -> Child ID Request: **673 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **811 ms**
- pcap parent request: `10:29:01.156` (frame 1195)
- pcap parent response: `10:29:01.232` (frame 1196)
- pcap child id request: `10:29:01.905` (frame 1204)
- pcap child id response: `10:29:01.967` (frame 1206)

#### PCAP-complete child attach 2

- log parent request: `10:29:05.349`
- log parent response: `10:29:05.534`
- log child id request: `10:29:05.799`
- log child id response: `10:29:06.260`
- parent ipv6: `fe80:0:0:0:84ef:b95c:fb5c:343`
- parent extaddr: `86efb95cfb5c0343`
- parent rloc16: `0xe400`
- child extaddr: `b285da2226f81dd6`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **323 ms**
- Response -> Child ID Request: **80 ms**
- Child ID Request -> Response: **437 ms**
- Full Attach: **840 ms**
- pcap parent request: `10:29:05.421` (frame 1209)
- pcap parent response: `10:29:05.744` (frame 1214)
- pcap child id request: `10:29:05.824` (frame 1216)
- pcap child id response: `10:29:06.261` (frame 1236)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_child_20260629-103507-run45.log`

- manifest status: `completed`
- child extaddr: `7e083b05dbdc466a`
- switch target extaddr(s): `56201546a9ee637c, 56201546a9ee637c, 56201546a9ee637c`

#### PCAP-complete child attach 1

- log parent request: `10:40:58.466`
- log parent response: `10:40:58.659`
- log child id request: `10:40:59.233`
- log child id response: `10:40:59.325`
- parent ipv6: `fe80:0:0:0:c86d:5724:d453:74b7`
- parent extaddr: `ca6d5724d45374b7`
- parent rloc16: `0x8800`
- child extaddr: `7e083b05dbdc466a`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **257 ms**
- Response -> Child ID Request: **463 ms**
- Child ID Request -> Response: **69 ms**
- Full Attach: **789 ms**
- pcap parent request: `10:40:58.539` (frame 241)
- pcap parent response: `10:40:58.796` (frame 244)
- pcap child id request: `10:40:59.259` (frame 250)
- pcap child id response: `10:40:59.328` (frame 252)

#### PCAP-complete child attach 2

- log parent request: `10:41:03.260`
- log parent response: `10:41:03.426`
- log child id request: `10:41:03.617`
- log child id response: `10:41:03.703`
- parent ipv6: `fe80:0:0:0:5420:1546:a9ee:637c`
- parent extaddr: `56201546a9ee637c`
- parent rloc16: `0x1000`
- child extaddr: `7e083b05dbdc466a`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **260 ms**
- Response -> Child ID Request: **81 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **403 ms**
- pcap parent request: `10:41:03.304` (frame 257)
- pcap parent response: `10:41:03.564` (frame 260)
- pcap child id request: `10:41:03.645` (frame 262)
- pcap child id response: `10:41:03.707` (frame 264)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_child_20260629-104705-run46.log`

- manifest status: `completed`
- child extaddr: `8eb912519d8293c8`
- switch target extaddr(s): `622f14d48b177a77, 622f14d48b177a77, 622f14d48b177a77`

#### PCAP-complete child attach 1

- log parent request: `10:52:56.977`
- log parent response: `10:52:57.047`
- log child id request: `10:52:57.703`
- log child id response: `10:52:57.787`
- parent ipv6: `fe80:0:0:0:cae:8ce4:6e34:55c2`
- parent extaddr: `0eae8ce46e3455c2`
- parent rloc16: `0x0c00`
- child extaddr: `8eb912519d8293c8`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **356 ms**
- Response -> Child ID Request: **396 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **815 ms**
- pcap parent request: `10:52:56.976` (frame 238)
- pcap parent response: `10:52:57.332` (frame 241)
- pcap child id request: `10:52:57.728` (frame 247)
- pcap child id response: `10:52:57.791` (frame 249)

#### PCAP-complete child attach 2

- log parent request: `10:53:01.121`
- log parent response: `10:53:01.454`
- log child id request: `n/a`
- log child id response: `10:53:01.742`
- parent ipv6: `fe80:0:0:0:602f:14d4:8b17:7a77`
- parent extaddr: `622f14d48b177a77`
- parent rloc16: `0x9000`
- child extaddr: `8eb912519d8293c8`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **435 ms**
- Response -> Child ID Request: **79 ms**
- Child ID Request -> Response: **100 ms**
- Full Attach: **614 ms**
- pcap parent request: `10:53:01.119` (frame 252)
- pcap parent response: `10:53:01.554` (frame 256)
- pcap child id request: `10:53:01.633` (frame 260)
- pcap child id response: `10:53:01.733` (frame 263)

#### PCAP-complete child attach 3

- log parent request: `10:56:57.529`
- log parent response: `10:56:57.619`
- log child id request: `10:56:58.250`
- log child id response: `10:56:58.342`
- parent ipv6: `fe80:0:0:0:a897:b9c2:5bd0:91a1`
- parent extaddr: `aa97b9c25bd091a1`
- parent rloc16: `0xa000`
- child extaddr: `8eb912519d8293c8`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **386 ms**
- Response -> Child ID Request: **364 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **820 ms**
- pcap parent request: `10:56:57.534` (frame 658)
- pcap parent response: `10:56:57.920` (frame 663)
- pcap child id request: `10:56:58.284` (frame 665)
- pcap child id response: `10:56:58.354` (frame 667)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `10:53:01.747`
- log child id response: `n/a`
- parent ipv6: `fe80:0:0:0:602f:14d4:8b17:7a77`
- parent extaddr: `622f14d48b177a77`
- parent rloc16: `n/a`
- child extaddr: `8eb912519d8293c8`
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
- failed tx by seqnum: seq 170: 16, seq 171: 16, seq 172: 16, seq 173: 16
- failed tx by dst: `0eae8ce46e3455c2`: 64

### `mcast_child_20260629-105903-run47.log`

- manifest status: `completed`
- child extaddr: `0a1eac940901bffe`
- switch target extaddr(s): `4a082fe9551fcad2, 4a082fe9551fcad2, 4a082fe9551fcad2`

#### PCAP-complete child attach 1

- log parent request: `11:04:54.321`
- log parent response: `11:04:54.470`
- log child id request: `11:04:55.010`
- log child id response: `11:04:55.101`
- parent ipv6: `fe80:0:0:0:7882:7b28:d3f7:cf55`
- parent extaddr: `7a827b28d3f7cf55`
- parent rloc16: `0x8800`
- child extaddr: `0a1eac940901bffe`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **153 ms**
- Response -> Child ID Request: **570 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **793 ms**
- pcap parent request: `11:04:54.313` (frame 218)
- pcap parent response: `11:04:54.466` (frame 219)
- pcap child id request: `11:04:55.036` (frame 227)
- pcap child id response: `11:04:55.106` (frame 229)

#### PCAP-complete child attach 2

- log parent request: `11:04:58.851`
- log parent response: `11:04:58.989`
- log child id request: `11:04:59.343`
- log child id response: `11:04:59.432`
- parent ipv6: `fe80:0:0:0:4808:2fe9:551f:cad2`
- parent extaddr: `4a082fe9551fcad2`
- parent rloc16: `0xa800`
- child extaddr: `0a1eac940901bffe`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **394 ms**
- Response -> Child ID Request: **80 ms**
- Child ID Request -> Response: **65 ms**
- Full Attach: **539 ms**
- pcap parent request: `11:04:58.897` (frame 231)
- pcap parent response: `11:04:59.291` (frame 236)
- pcap child id request: `11:04:59.371` (frame 238)
- pcap child id response: `11:04:59.436` (frame 240)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_child_20260629-111101-run48.log`

- manifest status: `completed`
- child extaddr: `be7b094fd0127391`
- switch target extaddr(s): `b6550801ffbd3f3d, b6550801ffbd3f3d, b6550801ffbd3f3d`

#### PCAP-complete child attach 1

- log parent request: `11:16:51.906`
- log parent response: `11:16:52.101`
- log child id request: `11:16:52.673`
- log child id response: `11:16:52.765`
- parent ipv6: `fe80:0:0:0:9057:be18:3146:41b3`
- parent extaddr: `9257be18314641b3`
- parent rloc16: `0xf000`
- child extaddr: `be7b094fd0127391`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **147 ms**
- Response -> Child ID Request: **603 ms**
- Child ID Request -> Response: **69 ms**
- Full Attach: **819 ms**
- pcap parent request: `11:16:51.950` (frame 1028)
- pcap parent response: `11:16:52.097` (frame 1029)
- pcap child id request: `11:16:52.700` (frame 1037)
- pcap child id response: `11:16:52.769` (frame 1039)

#### PCAP-complete child attach 2

- log parent request: `11:16:56.457`
- log parent response: `11:16:56.705`
- log child id request: `11:16:57.020`
- log child id response: `11:16:57.118`
- parent ipv6: `fe80:0:0:0:b455:801:ffbd:3f3d`
- parent extaddr: `b6550801ffbd3f3d`
- parent rloc16: `0x3000`
- child extaddr: `be7b094fd0127391`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **467 ms**
- Response -> Child ID Request: **79 ms**
- Child ID Request -> Response: **75 ms**
- Full Attach: **621 ms**
- pcap parent request: `11:16:56.502` (frame 1042)
- pcap parent response: `11:16:56.969` (frame 1047)
- pcap child id request: `11:16:57.048` (frame 1049)
- pcap child id response: `11:16:57.123` (frame 1051)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_child_20260629-112258-run49.log`

- manifest status: `completed`
- child extaddr: `3e828cbc07d70377`
- switch target extaddr(s): `626fdd530ce3f468, 626fdd530ce3f468, 626fdd530ce3f468`

#### PCAP-complete child attach 1

- log parent request: `11:28:49.233`
- log parent response: `11:28:49.440`
- log child id request: `11:28:50.001`
- log child id response: `11:28:50.089`
- parent ipv6: `fe80:0:0:0:6c67:fe7a:e90e:6c5e`
- parent extaddr: `6e67fe7ae90e6c5e`
- parent rloc16: `0xd800`
- child extaddr: `3e828cbc07d70377`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **129 ms**
- Response -> Child ID Request: **593 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **785 ms**
- pcap parent request: `11:28:49.307` (frame 463)
- pcap parent response: `11:28:49.436` (frame 464)
- pcap child id request: `11:28:50.029` (frame 472)
- pcap child id response: `11:28:50.092` (frame 474)

#### PCAP-complete child attach 2

- log parent request: `11:28:54.076`
- log parent response: `11:28:54.251`
- log child id request: `11:28:54.296`
- log child id response: `11:28:54.442`
- parent ipv6: `fe80:0:0:0:606f:dd53:ce3:f468`
- parent extaddr: `626fdd530ce3f468`
- parent rloc16: `0x0c00`
- child extaddr: `3e828cbc07d70377`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **172 ms**
- Response -> Child ID Request: **138 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **372 ms**
- pcap parent request: `11:28:54.073` (frame 476)
- pcap parent response: `11:28:54.245` (frame 477)
- pcap child id request: `11:28:54.383` (frame 481)
- pcap child id response: `11:28:54.445` (frame 483)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_child_20260629-113456-run50.log`

- manifest status: `completed`
- child extaddr: `f6cd2349d9d5d59c`
- switch target extaddr(s): `d2fb8704b18dd21e, d2fb8704b18dd21e, d2fb8704b18dd21e`

#### PCAP-complete child attach 1

- log parent request: `11:40:46.965`
- log parent response: `11:40:47.137`
- log child id request: `11:40:47.732`
- log child id response: `11:40:47.825`
- parent ipv6: `fe80:0:0:0:78c5:ebeb:6efe:d1a0`
- parent extaddr: `7ac5ebeb6efed1a0`
- parent rloc16: `0xc400`
- child extaddr: `f6cd2349d9d5d59c`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **131 ms**
- Response -> Child ID Request: **616 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **817 ms**
- pcap parent request: `11:40:47.012` (frame 1129)
- pcap parent response: `11:40:47.143` (frame 1132)
- pcap child id request: `11:40:47.759` (frame 1138)
- pcap child id response: `11:40:47.829` (frame 1140)

#### PCAP-complete child attach 2

- log parent request: `11:40:51.672`
- log parent response: `11:40:51.762`
- log child id request: `11:40:51.938`
- log child id response: `11:40:52.028`
- parent ipv6: `fe80:0:0:0:d0fb:8704:b18d:d21e`
- parent extaddr: `d2fb8704b18dd21e`
- parent rloc16: `0x7c00`
- child extaddr: `f6cd2349d9d5d59c`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **165 ms**
- Response -> Child ID Request: **137 ms**
- Child ID Request -> Response: **65 ms**
- Full Attach: **367 ms**
- pcap parent request: `11:40:51.664` (frame 1142)
- pcap parent response: `11:40:51.829` (frame 1145)
- pcap child id request: `11:40:51.966` (frame 1149)
- pcap child id response: `11:40:52.031` (frame 1151)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**
