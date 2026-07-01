# Child Log Analysis

## ucast_fastpr_child

Files analyzed: **20**

- batch folders: `ucast_fastpr-4router-20runs-20260627-165846`

### PCAP-complete child attach summary

| Attach | Metric | M (SD), ms | n |
| --- | --- | ---: | ---: |
| 1 | Request -> Response | 108.80 (66.53) | 20 |
| 1 | Response -> Child ID Request | 641.20 (66.94) | 20 |
| 1 | Child ID Request -> Response | 66.15 (3.33) | 20 |
| 1 | Full Attach | 816.15 (3.23) | 20 |
| 2 | Request -> Response | 42.55 (2.67) | 20 |
| 2 | Response -> Child ID Request | 318.40 (2.26) | 20 |
| 2 | Child ID Request -> Response | 66.55 (3.76) | 20 |
| 2 | Full Attach | 427.50 (6.53) | 20 |

| Metric | M (SD) | n |
| --- | ---: | ---: |
| Failed TX Attempts per Log | 0.00 (0.00) | 20 |
| Log-only or Partial Sequences per Log | 0.00 (0.00) | 20 |

### `ucast_fastpr_child_20260627-165938-run01.log`

- manifest status: `completed`
- child extaddr: `1ec8e8f43486b36f`
- switch target extaddr(s): `fa02450b6b1315e8, fa02450b6b1315e8, fa02450b6b1315e8`

#### PCAP-complete child attach 1

- log parent request: `17:05:28.991`
- log parent response: `17:05:29.059`
- log child id request: `17:05:29.713`
- log child id response: `17:05:29.800`
- parent ipv6: `fe80:0:0:0:9443:ea4a:5aac:ee81`
- parent extaddr: `9643ea4a5aacee81`
- parent rloc16: `0x3800`
- child extaddr: `1ec8e8f43486b36f`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **65 ms**
- Response -> Child ID Request: **686 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **815 ms**
- pcap parent request: `17:05:28.987` (frame 328)
- pcap parent response: `17:05:29.052` (frame 329)
- pcap child id request: `17:05:29.738` (frame 337)
- pcap child id response: `17:05:29.802` (frame 339)

#### PCAP-complete child attach 2

- log parent request: `17:05:33.250`
- log parent response: `17:05:33.341`
- log child id request: `17:05:33.627`
- log child id response: `17:05:33.714`
- parent ipv6: `fe80:0:0:0:f802:450b:6b13:15e8`
- parent extaddr: `fa02450b6b1315e8`
- parent rloc16: `0xb800`
- child extaddr: `1ec8e8f43486b36f`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **40 ms**
- Response -> Child ID Request: **319 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **421 ms**
- pcap parent request: `17:05:33.294` (frame 343)
- pcap parent response: `17:05:33.334` (frame 345)
- pcap child id request: `17:05:33.653` (frame 347)
- pcap child id response: `17:05:33.715` (frame 349)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260627-171135-run02.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `363d77377c4f0564`
- switch target extaddr(s): `82a54594cbf0e823, 82a54594cbf0e823, 82a54594cbf0e823`

#### PCAP-complete child attach 1

- log parent request: `17:17:26.251`
- log parent response: `17:17:26.406`
- log child id request: `17:17:26.971`
- log child id response: `17:17:27.059`
- parent ipv6: `fe80:0:0:0:34d5:33a2:cb07:1511`
- parent extaddr: `36d533a2cb071511`
- parent rloc16: `0xb400`
- child extaddr: `363d77377c4f0564`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **154 ms**
- Response -> Child ID Request: **598 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **816 ms**
- pcap parent request: `17:17:26.244` (frame 745)
- pcap parent response: `17:17:26.398` (frame 746)
- pcap child id request: `17:17:26.996` (frame 754)
- pcap child id response: `17:17:27.060` (frame 756)

#### PCAP-complete child attach 2

- log parent request: `17:17:30.837`
- log parent response: `17:17:30.928`
- log child id request: `17:17:31.212`
- log child id response: `17:17:31.311`
- parent ipv6: `fe80:0:0:0:80a5:4594:cbf0:e823`
- parent extaddr: `82a54594cbf0e823`
- parent rloc16: `0x8800`
- child extaddr: `363d77377c4f0564`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **44 ms**
- Response -> Child ID Request: **321 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **435 ms**
- pcap parent request: `17:17:30.878` (frame 758)
- pcap parent response: `17:17:30.922` (frame 760)
- pcap child id request: `17:17:31.243` (frame 762)
- pcap child id response: `17:17:31.313` (frame 764)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260627-172333-run03.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `0627034fc9260637`
- switch target extaddr(s): `1e8f755cf29a6d6c, 1e8f755cf29a6d6c, 1e8f755cf29a6d6c`

#### PCAP-complete child attach 1

- log parent request: `17:29:23.949`
- log parent response: `17:29:24.090`
- log child id request: `17:29:24.669`
- log child id response: `17:29:24.757`
- parent ipv6: `fe80:0:0:0:783f:d40f:a179:1de0`
- parent extaddr: `7a3fd40fa1791de0`
- parent rloc16: `0xe400`
- child extaddr: `0627034fc9260637`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **139 ms**
- Response -> Child ID Request: **611 ms**
- Child ID Request -> Response: **66 ms**
- Full Attach: **816 ms**
- pcap parent request: `17:29:23.944` (frame 266)
- pcap parent response: `17:29:24.083` (frame 267)
- pcap child id request: `17:29:24.694` (frame 275)
- pcap child id response: `17:29:24.760` (frame 277)

#### PCAP-complete child attach 2

- log parent request: `17:29:28.629`
- log parent response: `17:29:28.717`
- log child id request: `17:29:29.002`
- log child id response: `17:29:29.093`
- parent ipv6: `fe80:0:0:0:1c8f:755c:f29a:6d6c`
- parent extaddr: `1e8f755cf29a6d6c`
- parent rloc16: `0x3000`
- child extaddr: `0627034fc9260637`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **39 ms**
- Response -> Child ID Request: **322 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **423 ms**
- pcap parent request: `17:29:28.672` (frame 280)
- pcap parent response: `17:29:28.711` (frame 282)
- pcap child id request: `17:29:29.033` (frame 285)
- pcap child id response: `17:29:29.095` (frame 287)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260627-173531-run04.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `7620f577d5df9a1e`
- switch target extaddr(s): `52ddb6d01dd5f1bc, 52ddb6d01dd5f1bc, 52ddb6d01dd5f1bc`

#### PCAP-complete child attach 1

- log parent request: `17:41:22.387`
- log parent response: `17:41:22.436`
- log child id request: `17:41:23.108`
- log child id response: `17:41:23.195`
- parent ipv6: `fe80:0:0:0:9c07:1007:e2d5:3b58`
- parent extaddr: `9e071007e2d53b58`
- parent rloc16: `0x9000`
- child extaddr: `7620f577d5df9a1e`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **112 ms**
- Response -> Child ID Request: **637 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **812 ms**
- pcap parent request: `17:41:22.384` (frame 192)
- pcap parent response: `17:41:22.496` (frame 195)
- pcap child id request: `17:41:23.133` (frame 201)
- pcap child id response: `17:41:23.196` (frame 203)

#### PCAP-complete child attach 2

- log parent request: `17:41:26.477`
- log parent response: `17:41:26.566`
- log child id request: `17:41:26.847`
- log child id response: `17:41:26.939`
- parent ipv6: `fe80:0:0:0:50dd:b6d0:1dd5:f1bc`
- parent extaddr: `52ddb6d01dd5f1bc`
- parent rloc16: `0xd000`
- child extaddr: `7620f577d5df9a1e`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **40 ms**
- Response -> Child ID Request: **319 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **422 ms**
- pcap parent request: `17:41:26.519` (frame 207)
- pcap parent response: `17:41:26.559` (frame 209)
- pcap child id request: `17:41:26.878` (frame 211)
- pcap child id response: `17:41:26.941` (frame 213)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260627-174728-run05.log`

- manifest status: `completed`
- child extaddr: `f65c71262f80881e`
- switch target extaddr(s): `dea055904f2894b2, dea055904f2894b2, dea055904f2894b2`

#### PCAP-complete child attach 1

- log parent request: `17:53:19.584`
- log parent response: `17:53:19.898`
- log child id request: `17:53:20.305`
- log child id response: `17:53:20.397`
- parent ipv6: `fe80:0:0:0:841a:b816:7add:53a`
- parent extaddr: `861ab8167add053a`
- parent rloc16: `0x6000`
- child extaddr: `f65c71262f80881e`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **313 ms**
- Response -> Child ID Request: **435 ms**
- Child ID Request -> Response: **71 ms**
- Full Attach: **819 ms**
- pcap parent request: `17:53:19.581` (frame 471)
- pcap parent response: `17:53:19.894` (frame 472)
- pcap child id request: `17:53:20.329` (frame 481)
- pcap child id response: `17:53:20.400` (frame 483)

#### PCAP-complete child attach 2

- log parent request: `17:53:24.180`
- log parent response: `17:53:24.270`
- log child id request: `17:53:24.553`
- log child id response: `17:53:24.640`
- parent ipv6: `fe80:0:0:0:dca0:5590:4f28:94b2`
- parent extaddr: `dea055904f2894b2`
- parent rloc16: `0xd400`
- child extaddr: `f65c71262f80881e`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **39 ms**
- Response -> Child ID Request: **318 ms**
- Child ID Request -> Response: **61 ms**
- Full Attach: **418 ms**
- pcap parent request: `17:53:24.224` (frame 485)
- pcap parent response: `17:53:24.263` (frame 487)
- pcap child id request: `17:53:24.581` (frame 489)
- pcap child id response: `17:53:24.642` (frame 491)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260627-175926-run06.log`

- manifest status: `completed`
- child extaddr: `0ef5f6dd7a169ded`
- switch target extaddr(s): `ba884e6440a3d3ae, ba884e6440a3d3ae, ba884e6440a3d3ae`

#### PCAP-complete child attach 1

- log parent request: `18:05:17.687`
- log parent response: `18:05:17.735`
- log child id request: `18:05:18.406`
- log child id response: `18:05:18.498`
- parent ipv6: `fe80:0:0:0:50cb:cca2:dffe:f98c`
- parent extaddr: `52cbcca2dffef98c`
- parent rloc16: `0xb400`
- child extaddr: `0ef5f6dd7a169ded`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **48 ms**
- Response -> Child ID Request: **702 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **820 ms**
- pcap parent request: `18:05:17.683` (frame 572)
- pcap parent response: `18:05:17.731` (frame 573)
- pcap child id request: `18:05:18.433` (frame 581)
- pcap child id response: `18:05:18.503` (frame 583)

#### PCAP-complete child attach 2

- log parent request: `18:05:22.074`
- log parent response: `18:05:22.164`
- log child id request: `18:05:22.442`
- log child id response: `18:05:22.532`
- parent ipv6: `fe80:0:0:0:b888:4e64:40a3:d3ae`
- parent extaddr: `ba884e6440a3d3ae`
- parent rloc16: `0xc000`
- child extaddr: `0ef5f6dd7a169ded`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **39 ms**
- Response -> Child ID Request: **316 ms**
- Child ID Request -> Response: **61 ms**
- Full Attach: **416 ms**
- pcap parent request: `18:05:22.119` (frame 585)
- pcap parent response: `18:05:22.158` (frame 587)
- pcap child id request: `18:05:22.474` (frame 589)
- pcap child id response: `18:05:22.535` (frame 591)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260627-181124-run07.log`

- manifest status: `completed`
- child extaddr: `5e5ee7ab433f29f8`
- switch target extaddr(s): `3e7b12a9d36d7383, 3e7b12a9d36d7383, 3e7b12a9d36d7383`

#### PCAP-complete child attach 1

- log parent request: `18:17:15.008`
- log parent response: `18:17:15.137`
- log child id request: `18:17:15.814`
- log child id response: `18:17:15.870`
- parent ipv6: `fe80:0:0:0:8486:dc94:5ff8:26e3`
- parent extaddr: `8686dc945ff826e3`
- parent rloc16: `0xc000`
- child extaddr: `5e5ee7ab433f29f8`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **78 ms**
- Response -> Child ID Request: **671 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **819 ms**
- pcap parent request: `18:17:15.054` (frame 892)
- pcap parent response: `18:17:15.132` (frame 893)
- pcap child id request: `18:17:15.803` (frame 901)
- pcap child id response: `18:17:15.873` (frame 903)

#### PCAP-complete child attach 2

- log parent request: `18:17:19.767`
- log parent response: `18:17:19.862`
- log child id request: `18:17:20.144`
- log child id response: `18:17:20.242`
- parent ipv6: `fe80:0:0:0:3c7b:12a9:d36d:7383`
- parent extaddr: `3e7b12a9d36d7383`
- parent rloc16: `0xb000`
- child extaddr: `5e5ee7ab433f29f8`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **46 ms**
- Response -> Child ID Request: **317 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **433 ms**
- pcap parent request: `18:17:19.812` (frame 906)
- pcap parent response: `18:17:19.858` (frame 908)
- pcap child id request: `18:17:20.175` (frame 910)
- pcap child id response: `18:17:20.245` (frame 912)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260627-182322-run08.log`

- manifest status: `completed`
- child extaddr: `aadda3ccdc916a56`
- switch target extaddr(s): `72fb138cae4aaffd, 72fb138cae4aaffd, 72fb138cae4aaffd`

#### PCAP-complete child attach 1

- log parent request: `18:29:13.078`
- log parent response: `18:29:13.225`
- log child id request: `18:29:13.799`
- log child id response: `18:29:13.890`
- parent ipv6: `fe80:0:0:0:acdf:8f1:137b:9b6`
- parent extaddr: `aedf08f1137b09b6`
- parent rloc16: `0x9800`
- child extaddr: `aadda3ccdc916a56`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **146 ms**
- Response -> Child ID Request: **603 ms**
- Child ID Request -> Response: **71 ms**
- Full Attach: **820 ms**
- pcap parent request: `18:29:13.075` (frame 377)
- pcap parent response: `18:29:13.221` (frame 378)
- pcap child id request: `18:29:13.824` (frame 386)
- pcap child id response: `18:29:13.895` (frame 388)

#### PCAP-complete child attach 2

- log parent request: `18:29:17.436`
- log parent response: `18:29:17.530`
- log child id request: `18:29:17.815`
- log child id response: `18:29:17.910`
- parent ipv6: `fe80:0:0:0:70fb:138c:ae4a:affd`
- parent extaddr: `72fb138cae4aaffd`
- parent rloc16: `0x4400`
- child extaddr: `aadda3ccdc916a56`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **43 ms**
- Response -> Child ID Request: **323 ms**
- Child ID Request -> Response: **68 ms**
- Full Attach: **434 ms**
- pcap parent request: `18:29:17.482` (frame 393)
- pcap parent response: `18:29:17.525` (frame 395)
- pcap child id request: `18:29:17.848` (frame 397)
- pcap child id response: `18:29:17.916` (frame 399)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260627-183519-run09.log`

- manifest status: `completed`
- child extaddr: `96163a71b1819feb`
- switch target extaddr(s): `0e82e49f9478d064, 0e82e49f9478d064, 0e82e49f9478d064`

#### PCAP-complete child attach 1

- log parent request: `18:41:11.021`
- log parent response: `18:41:11.070`
- log child id request: `18:41:11.741`
- log child id response: `18:41:11.836`
- parent ipv6: `fe80:0:0:0:d06f:7cc1:21c4:7806`
- parent extaddr: `d26f7cc121c47806`
- parent rloc16: `0xf400`
- child extaddr: `96163a71b1819feb`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **47 ms**
- Response -> Child ID Request: **703 ms**
- Child ID Request -> Response: **71 ms**
- Full Attach: **821 ms**
- pcap parent request: `18:41:11.019` (frame 184)
- pcap parent response: `18:41:11.066` (frame 185)
- pcap child id request: `18:41:11.769` (frame 193)
- pcap child id response: `18:41:11.840` (frame 195)

#### PCAP-complete child attach 2

- log parent request: `18:41:15.214`
- log parent response: `18:41:15.306`
- log child id request: `18:41:15.587`
- log child id response: `18:41:15.676`
- parent ipv6: `fe80:0:0:0:c82:e49f:9478:d064`
- parent extaddr: `0e82e49f9478d064`
- parent rloc16: `0x5000`
- child extaddr: `96163a71b1819feb`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **43 ms**
- Response -> Child ID Request: **313 ms**
- Child ID Request -> Response: **66 ms**
- Full Attach: **422 ms**
- pcap parent request: `18:41:15.259` (frame 197)
- pcap parent response: `18:41:15.302` (frame 199)
- pcap child id request: `18:41:15.615` (frame 201)
- pcap child id response: `18:41:15.681` (frame 203)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260627-184717-run10.log`

- manifest status: `completed`
- child extaddr: `de78e24f2dc0c4ae`
- switch target extaddr(s): `1e1d7cdb4d73b02f, 1e1d7cdb4d73b02f, 1e1d7cdb4d73b02f`

#### PCAP-complete child attach 1

- log parent request: `18:53:08.660`
- log parent response: `18:53:08.737`
- log child id request: `18:53:09.381`
- log child id response: `18:53:09.466`
- parent ipv6: `fe80:0:0:0:a05c:f1d3:2b1b:8dc4`
- parent extaddr: `a25cf1d32b1b8dc4`
- parent rloc16: `0xd000`
- child extaddr: `de78e24f2dc0c4ae`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **74 ms**
- Response -> Child ID Request: **674 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **810 ms**
- pcap parent request: `18:53:08.658` (frame 319)
- pcap parent response: `18:53:08.732` (frame 320)
- pcap child id request: `18:53:09.406` (frame 328)
- pcap child id response: `18:53:09.468` (frame 330)

#### PCAP-complete child attach 2

- log parent request: `18:53:12.881`
- log parent response: `18:53:12.975`
- log child id request: `18:53:13.256`
- log child id response: `18:53:13.356`
- parent ipv6: `fe80:0:0:0:1c1d:7cdb:4d73:b02f`
- parent extaddr: `1e1d7cdb4d73b02f`
- parent rloc16: `0x9000`
- child extaddr: `de78e24f2dc0c4ae`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **45 ms**
- Response -> Child ID Request: **319 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **434 ms**
- pcap parent request: `18:53:12.926` (frame 332)
- pcap parent response: `18:53:12.971` (frame 334)
- pcap child id request: `18:53:13.290` (frame 336)
- pcap child id response: `18:53:13.360` (frame 338)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260627-185915-run11.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `d2fd84be7d272bfa`
- switch target extaddr(s): `cac27fd05720306f, cac27fd05720306f, cac27fd05720306f`

#### PCAP-complete child attach 1

- log parent request: `19:05:05.837`
- log parent response: `19:05:05.977`
- log child id request: `19:05:06.605`
- log child id response: `19:05:06.693`
- parent ipv6: `fe80:0:0:0:a0b6:8f99:3885:8706`
- parent extaddr: `a2b68f9938858706`
- parent rloc16: `0x7400`
- child extaddr: `d2fd84be7d272bfa`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **90 ms**
- Response -> Child ID Request: **660 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **814 ms**
- pcap parent request: `19:05:05.882` (frame 250)
- pcap parent response: `19:05:05.972` (frame 251)
- pcap child id request: `19:05:06.632` (frame 259)
- pcap child id response: `19:05:06.696` (frame 261)

#### PCAP-complete child attach 2

- log parent request: `19:05:10.580`
- log parent response: `19:05:10.670`
- log child id request: `19:05:10.952`
- log child id response: `19:05:11.044`
- parent ipv6: `fe80:0:0:0:c8c2:7fd0:5720:306f`
- parent extaddr: `cac27fd05720306f`
- parent rloc16: `0xac00`
- child extaddr: `d2fd84be7d272bfa`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **39 ms**
- Response -> Child ID Request: **319 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **422 ms**
- pcap parent request: `19:05:10.626` (frame 263)
- pcap parent response: `19:05:10.665` (frame 265)
- pcap child id request: `19:05:10.984` (frame 267)
- pcap child id response: `19:05:11.048` (frame 269)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260627-191112-run12.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `4e1f5e3499b664d8`
- switch target extaddr(s): `62692dcfcbfb5c89, 62692dcfcbfb5c89, 62692dcfcbfb5c89`

#### PCAP-complete child attach 1

- log parent request: `19:17:03.795`
- log parent response: `19:17:03.840`
- log child id request: `19:17:04.517`
- log child id response: `19:17:04.603`
- parent ipv6: `fe80:0:0:0:8074:cd7:a5eb:6b08`
- parent extaddr: `82740cd7a5eb6b08`
- parent rloc16: `0x3800`
- child extaddr: `4e1f5e3499b664d8`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **44 ms**
- Response -> Child ID Request: **706 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **814 ms**
- pcap parent request: `19:17:03.791` (frame 195)
- pcap parent response: `19:17:03.835` (frame 196)
- pcap child id request: `19:17:04.541` (frame 204)
- pcap child id response: `19:17:04.605` (frame 206)

#### PCAP-complete child attach 2

- log parent request: `19:17:08.345`
- log parent response: `19:17:08.443`
- log child id request: `19:17:08.728`
- log child id response: `19:17:08.821`
- parent ipv6: `fe80:0:0:0:6069:2dcf:cbfb:5c89`
- parent extaddr: `62692dcfcbfb5c89`
- parent rloc16: `0x2c00`
- child extaddr: `4e1f5e3499b664d8`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **48 ms**
- Response -> Child ID Request: **317 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **435 ms**
- pcap parent request: `19:17:08.390` (frame 208)
- pcap parent response: `19:17:08.438` (frame 210)
- pcap child id request: `19:17:08.755` (frame 212)
- pcap child id response: `19:17:08.825` (frame 214)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260627-192310-run13.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `befcc0942e8edc85`
- switch target extaddr(s): `92bdfb9a6750a933, 92bdfb9a6750a933, 92bdfb9a6750a933`

#### PCAP-complete child attach 1

- log parent request: `19:29:01.428`
- log parent response: `19:29:01.488`
- log child id request: `19:29:02.149`
- log child id response: `19:29:02.235`
- parent ipv6: `fe80:0:0:0:dcce:7ece:d5b7:a761`
- parent extaddr: `dece7eced5b7a761`
- parent rloc16: `0x6800`
- child extaddr: `befcc0942e8edc85`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **59 ms**
- Response -> Child ID Request: **692 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **815 ms**
- pcap parent request: `19:29:01.423` (frame 394)
- pcap parent response: `19:29:01.482` (frame 395)
- pcap child id request: `19:29:02.174` (frame 403)
- pcap child id response: `19:29:02.238` (frame 405)

#### PCAP-complete child attach 2

- log parent request: `19:29:05.800`
- log parent response: `19:29:05.893`
- log child id request: `19:29:06.175`
- log child id response: `19:29:06.274`
- parent ipv6: `fe80:0:0:0:90bd:fb9a:6750:a933`
- parent extaddr: `92bdfb9a6750a933`
- parent rloc16: `0x1000`
- child extaddr: `befcc0942e8edc85`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **44 ms**
- Response -> Child ID Request: **320 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **434 ms**
- pcap parent request: `19:29:05.843` (frame 409)
- pcap parent response: `19:29:05.887` (frame 411)
- pcap child id request: `19:29:06.207` (frame 413)
- pcap child id response: `19:29:06.277` (frame 415)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260627-193508-run14.log`

- manifest status: `completed`
- child extaddr: `5e11c2756378d4d5`
- switch target extaddr(s): `9e99ee688009f8f1, 9e99ee688009f8f1, 9e99ee688009f8f1`

#### PCAP-complete child attach 1

- log parent request: `19:40:59.221`
- log parent response: `19:40:59.457`
- log child id request: `19:40:59.944`
- log child id response: `19:41:00.035`
- parent ipv6: `fe80:0:0:0:24d3:e3c7:678b:6de6`
- parent extaddr: `26d3e3c7678b6de6`
- parent rloc16: `0xa800`
- child extaddr: `5e11c2756378d4d5`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **234 ms**
- Response -> Child ID Request: **515 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **819 ms**
- pcap parent request: `19:40:59.219` (frame 582)
- pcap parent response: `19:40:59.453` (frame 583)
- pcap child id request: `19:40:59.968` (frame 591)
- pcap child id response: `19:41:00.038` (frame 593)

#### PCAP-complete child attach 2

- log parent request: `19:41:03.856`
- log parent response: `19:41:03.948`
- log child id request: `19:41:04.228`
- log child id response: `19:41:04.320`
- parent ipv6: `fe80:0:0:0:9c99:ee68:8009:f8f1`
- parent extaddr: `9e99ee688009f8f1`
- parent rloc16: `0xc800`
- child extaddr: `5e11c2756378d4d5`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **40 ms**
- Response -> Child ID Request: **317 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **420 ms**
- pcap parent request: `19:41:03.902` (frame 595)
- pcap parent response: `19:41:03.942` (frame 597)
- pcap child id request: `19:41:04.259` (frame 599)
- pcap child id response: `19:41:04.322` (frame 601)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260627-194706-run15.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `2e3a817961b494cf`
- switch target extaddr(s): `4e1e9c80bf7630fe, 4e1e9c80bf7630fe, 4e1e9c80bf7630fe`

#### PCAP-complete child attach 1

- log parent request: `19:52:56.950`
- log parent response: `19:52:56.994`
- log child id request: `19:52:57.671`
- log child id response: `19:52:57.756`
- parent ipv6: `fe80:0:0:0:c489:2d53:58dc:c3a`
- parent extaddr: `c6892d5358dc0c3a`
- parent rloc16: `0x6c00`
- child extaddr: `2e3a817961b494cf`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **102 ms**
- Response -> Child ID Request: **650 ms**
- Child ID Request -> Response: **65 ms**
- Full Attach: **817 ms**
- pcap parent request: `19:52:56.942` (frame 230)
- pcap parent response: `19:52:57.044` (frame 233)
- pcap child id request: `19:52:57.694` (frame 239)
- pcap child id response: `19:52:57.759` (frame 241)

#### PCAP-complete child attach 2

- log parent request: `19:53:01.661`
- log parent response: `19:53:01.701`
- log child id request: `19:53:01.985`
- log child id response: `19:53:02.078`
- parent ipv6: `fe80:0:0:0:4c1e:9c80:bf76:30fe`
- parent extaddr: `4e1e9c80bf7630fe`
- parent rloc16: `0x8000`
- child extaddr: `2e3a817961b494cf`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **44 ms**
- Response -> Child ID Request: **316 ms**
- Child ID Request -> Response: **69 ms**
- Full Attach: **429 ms**
- pcap parent request: `19:53:01.652` (frame 246)
- pcap parent response: `19:53:01.696` (frame 248)
- pcap child id request: `19:53:02.012` (frame 250)
- pcap child id response: `19:53:02.081` (frame 252)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260627-195903-run16.log`

- manifest status: `completed`
- child extaddr: `96809c6238120fd0`
- switch target extaddr(s): `96dc92e659311324, 96dc92e659311324, 96dc92e659311324`

#### PCAP-complete child attach 1

- log parent request: `20:04:55.213`
- log parent response: `20:04:55.345`
- log child id request: `20:04:55.980`
- log child id response: `20:04:56.066`
- parent ipv6: `fe80:0:0:0:70c8:9041:eb83:d09e`
- parent extaddr: `72c89041eb83d09e`
- parent rloc16: `0xf800`
- child extaddr: `96809c6238120fd0`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **121 ms**
- Response -> Child ID Request: **629 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **813 ms**
- pcap parent request: `20:04:55.256` (frame 190)
- pcap parent response: `20:04:55.377` (frame 193)
- pcap child id request: `20:04:56.006` (frame 199)
- pcap child id response: `20:04:56.069` (frame 201)

#### PCAP-complete child attach 2

- log parent request: `20:04:59.505`
- log parent response: `20:04:59.545`
- log child id request: `20:04:59.831`
- log child id response: `20:04:59.924`
- parent ipv6: `fe80:0:0:0:94dc:92e6:5931:1324`
- parent extaddr: `96dc92e659311324`
- parent rloc16: `0x2400`
- child extaddr: `96809c6238120fd0`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **43 ms**
- Response -> Child ID Request: **318 ms**
- Child ID Request -> Response: **69 ms**
- Full Attach: **430 ms**
- pcap parent request: `20:04:59.498` (frame 204)
- pcap parent response: `20:04:59.541` (frame 206)
- pcap child id request: `20:04:59.859` (frame 208)
- pcap child id response: `20:04:59.928` (frame 210)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260627-201101-run17.log`

- manifest status: `completed`
- child extaddr: `7ec0f85d3a062e04`
- switch target extaddr(s): `5ab531279e716d9d, 5ab531279e716d9d, 5ab531279e716d9d`

#### PCAP-complete child attach 1

- log parent request: `20:16:52.915`
- log parent response: `20:16:53.015`
- log child id request: `20:16:53.637`
- log child id response: `20:16:53.723`
- parent ipv6: `fe80:0:0:0:c024:8098:7159:8e7`
- parent extaddr: `c2248098715908e7`
- parent rloc16: `0x7800`
- child extaddr: `7ec0f85d3a062e04`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **99 ms**
- Response -> Child ID Request: **652 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **815 ms**
- pcap parent request: `20:16:52.911` (frame 531)
- pcap parent response: `20:16:53.010` (frame 532)
- pcap child id request: `20:16:53.662` (frame 540)
- pcap child id response: `20:16:53.726` (frame 542)

#### PCAP-complete child attach 2

- log parent request: `20:16:57.314`
- log parent response: `20:16:57.408`
- log child id request: `20:16:57.693`
- log child id response: `20:16:57.788`
- parent ipv6: `fe80:0:0:0:58b5:3127:9e71:6d9d`
- parent extaddr: `5ab531279e716d9d`
- parent rloc16: `0xd000`
- child extaddr: `7ec0f85d3a062e04`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **45 ms**
- Response -> Child ID Request: **319 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **434 ms**
- pcap parent request: `20:16:57.358` (frame 545)
- pcap parent response: `20:16:57.403` (frame 547)
- pcap child id request: `20:16:57.722` (frame 549)
- pcap child id response: `20:16:57.792` (frame 551)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260627-202259-run18.log`

- manifest status: `completed`
- child extaddr: `eaea9df64b60519b`
- switch target extaddr(s): `4a301e2d98c1494f, 4a301e2d98c1494f, 4a301e2d98c1494f`

#### PCAP-complete child attach 1

- log parent request: `20:28:50.899`
- log parent response: `20:28:50.972`
- log child id request: `20:28:51.620`
- log child id response: `20:28:51.704`
- parent ipv6: `fe80:0:0:0:a8d1:f33a:73a4:45fc`
- parent extaddr: `aad1f33a73a445fc`
- parent rloc16: `0x5400`
- child extaddr: `eaea9df64b60519b`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **78 ms**
- Response -> Child ID Request: **671 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **812 ms**
- pcap parent request: `20:28:50.894` (frame 1263)
- pcap parent response: `20:28:50.972` (frame 1266)
- pcap child id request: `20:28:51.643` (frame 1272)
- pcap child id response: `20:28:51.706` (frame 1274)

#### PCAP-complete child attach 2

- log parent request: `20:28:55.120`
- log parent response: `20:28:55.214`
- log child id request: `20:28:55.496`
- log child id response: `20:28:55.589`
- parent ipv6: `fe80:0:0:0:4830:1e2d:98c1:494f`
- parent extaddr: `4a301e2d98c1494f`
- parent rloc16: `0x1800`
- child extaddr: `eaea9df64b60519b`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **42 ms**
- Response -> Child ID Request: **320 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **426 ms**
- pcap parent request: `20:28:55.165` (frame 1276)
- pcap parent response: `20:28:55.207` (frame 1278)
- pcap child id request: `20:28:55.527` (frame 1280)
- pcap child id response: `20:28:55.591` (frame 1282)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260627-203457-run19.log`

- manifest status: `completed`
- child extaddr: `4699d660bf7e215e`
- switch target extaddr(s): `8a8f4bb370357d69, 8a8f4bb370357d69, 8a8f4bb370357d69`

#### PCAP-complete child attach 1

- log parent request: `20:40:48.580`
- log parent response: `20:40:48.686`
- log child id request: `20:40:49.348`
- log child id response: `20:40:49.441`
- parent ipv6: `fe80:0:0:0:3cde:e488:aa8d:72c8`
- parent extaddr: `3edee488aa8d72c8`
- parent rloc16: `0xd000`
- child extaddr: `4699d660bf7e215e`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **59 ms**
- Response -> Child ID Request: **692 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **821 ms**
- pcap parent request: `20:40:48.623` (frame 183)
- pcap parent response: `20:40:48.682` (frame 184)
- pcap child id request: `20:40:49.374` (frame 192)
- pcap child id response: `20:40:49.444` (frame 194)

#### PCAP-complete child attach 2

- log parent request: `20:40:52.900`
- log parent response: `20:40:52.992`
- log child id request: `20:40:53.272`
- log child id response: `20:40:53.365`
- parent ipv6: `fe80:0:0:0:888f:4bb3:7035:7d69`
- parent extaddr: `8a8f4bb370357d69`
- parent rloc16: `0x4400`
- child extaddr: `4699d660bf7e215e`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **44 ms**
- Response -> Child ID Request: **317 ms**
- Child ID Request -> Response: **66 ms**
- Full Attach: **427 ms**
- pcap parent request: `20:40:52.944` (frame 196)
- pcap parent response: `20:40:52.988` (frame 198)
- pcap child id request: `20:40:53.305` (frame 200)
- pcap child id response: `20:40:53.371` (frame 202)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260627-204655-run20.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `b6b7cb23e4f713dc`
- switch target extaddr(s): `42294c4ec7e59c1d, 42294c4ec7e59c1d, 42294c4ec7e59c1d`

#### PCAP-complete child attach 1

- log parent request: `20:52:46.378`
- log parent response: `20:52:46.541`
- log child id request: `20:52:47.144`
- log child id response: `20:52:47.232`
- parent ipv6: `fe80:0:0:0:745b:ca69:d0ef:2a32`
- parent extaddr: `765bca69d0ef2a32`
- parent rloc16: `0x1800`
- child extaddr: `b6b7cb23e4f713dc`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **114 ms**
- Response -> Child ID Request: **637 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **815 ms**
- pcap parent request: `20:52:46.420` (frame 563)
- pcap parent response: `20:52:46.534` (frame 564)
- pcap child id request: `20:52:47.171` (frame 572)
- pcap child id response: `20:52:47.235` (frame 574)

#### PCAP-complete child attach 2

- log parent request: `20:52:50.770`
- log parent response: `20:52:50.862`
- log child id request: `20:52:51.144`
- log child id response: `20:52:51.244`
- parent ipv6: `fe80:0:0:0:4029:4c4e:c7e5:9c1d`
- parent extaddr: `42294c4ec7e59c1d`
- parent rloc16: `0x1000`
- child extaddr: `b6b7cb23e4f713dc`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **44 ms**
- Response -> Child ID Request: **318 ms**
- Child ID Request -> Response: **73 ms**
- Full Attach: **435 ms**
- pcap parent request: `20:52:50.813` (frame 577)
- pcap parent response: `20:52:50.857` (frame 579)
- pcap child id request: `20:52:51.175` (frame 581)
- pcap child id response: `20:52:51.248` (frame 583)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**
