# Child Log Analysis

## mcast_child

Files analyzed: **20**

- batch folders: `mcast-4router-20runs-20260628-214706`

### PCAP-complete child attach summary

| Attach | Metric | M (SD), ms | n |
| --- | --- | ---: | ---: |
| 1 | Request -> Response | 138.80 (84.28) | 20 |
| 1 | Response -> Child ID Request | 610.90 (84.06) | 20 |
| 1 | Child ID Request -> Response | 66.20 (4.81) | 20 |
| 1 | Full Attach | 815.90 (4.36) | 20 |
| 2 | Request -> Response | 270.65 (151.24) | 20 |
| 2 | Response -> Child ID Request | 106.70 (22.16) | 20 |
| 2 | Child ID Request -> Response | 68.75 (6.42) | 20 |
| 2 | Full Attach | 446.10 (145.88) | 20 |
| 3 | Request -> Response | 295.67 (150.75) | 3 |
| 3 | Response -> Child ID Request | 453.33 (150.17) | 3 |
| 3 | Child ID Request -> Response | 72.67 (3.79) | 3 |
| 3 | Full Attach | 821.67 (4.62) | 3 |

| Metric | M (SD) | n |
| --- | ---: | ---: |
| Failed TX Attempts per Log | 9.60 (23.45) | 20 |
| Log-only or Partial Sequences per Log | 0.05 (0.22) | 20 |

### `mcast_child_20260628-214817-run01.log`

- manifest status: `completed`
- child extaddr: `7619233dcf41a20f`
- switch target extaddr(s): `bac96402c5ea43e6, bac96402c5ea43e6, bac96402c5ea43e6`

#### PCAP-complete child attach 1

- log parent request: `21:54:08.258`
- log parent response: `21:54:08.466`
- log child id request: `21:54:09.062`
- log child id response: `21:54:09.116`
- parent ipv6: `fe80:0:0:0:e4ab:c408:c70b:278e`
- parent extaddr: `e6abc408c70b278e`
- parent rloc16: `0x5000`
- child extaddr: `7619233dcf41a20f`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **157 ms**
- Response -> Child ID Request: **589 ms**
- Child ID Request -> Response: **69 ms**
- Full Attach: **815 ms**
- pcap parent request: `21:54:08.305` (frame 743)
- pcap parent response: `21:54:08.462` (frame 744)
- pcap child id request: `21:54:09.051` (frame 752)
- pcap child id response: `21:54:09.120` (frame 754)

#### PCAP-complete child attach 2

- log parent request: `21:54:13.024`
- log parent response: `21:54:13.310`
- log child id request: `21:54:13.528`
- log child id response: `21:54:13.621`
- parent ipv6: `fe80:0:0:0:b8c9:6402:c5ea:43e6`
- parent extaddr: `bac96402c5ea43e6`
- parent rloc16: `0x8000`
- child extaddr: `7619233dcf41a20f`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **408 ms**
- Response -> Child ID Request: **78 ms**
- Child ID Request -> Response: **69 ms**
- Full Attach: **555 ms**
- pcap parent request: `21:54:13.070` (frame 757)
- pcap parent response: `21:54:13.478` (frame 762)
- pcap child id request: `21:54:13.556` (frame 764)
- pcap child id response: `21:54:13.625` (frame 766)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_child_20260628-220015-run02.log`

- manifest status: `completed`
- child extaddr: `1680e28c1d1e0a97`
- switch target extaddr(s): `ae9a1d500bea283d, ae9a1d500bea283d, ae9a1d500bea283d`

#### PCAP-complete child attach 1

- log parent request: `22:06:06.200`
- log parent response: `22:06:06.399`
- log child id request: `22:06:06.922`
- log child id response: `22:06:07.019`
- parent ipv6: `fe80:0:0:0:a448:be64:7349:1505`
- parent extaddr: `a648be6473491505`
- parent rloc16: `0x8c00`
- child extaddr: `1680e28c1d1e0a97`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **197 ms**
- Response -> Child ID Request: **552 ms**
- Child ID Request -> Response: **76 ms**
- Full Attach: **825 ms**
- pcap parent request: `22:06:06.196` (frame 193)
- pcap parent response: `22:06:06.393` (frame 194)
- pcap child id request: `22:06:06.945` (frame 203)
- pcap child id response: `22:06:07.021` (frame 205)

#### PCAP-complete child attach 2

- log parent request: `22:06:10.794`
- log parent response: `22:06:10.958`
- log child id request: `22:06:11.046`
- log child id response: `22:06:11.144`
- parent ipv6: `fe80:0:0:0:ac9a:1d50:bea:283d`
- parent extaddr: `ae9a1d500bea283d`
- parent rloc16: `0x6000`
- child extaddr: `1680e28c1d1e0a97`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **146 ms**
- Response -> Child ID Request: **92 ms**
- Child ID Request -> Response: **69 ms**
- Full Attach: **307 ms**
- pcap parent request: `22:06:10.838` (frame 207)
- pcap parent response: `22:06:10.984` (frame 210)
- pcap child id request: `22:06:11.076` (frame 212)
- pcap child id response: `22:06:11.145` (frame 214)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_child_20260628-221213-run03.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `c651f65117c68110`
- switch target extaddr(s): `c2d114c8c43ae008, c2d114c8c43ae008, c2d114c8c43ae008`

#### PCAP-complete child attach 1

- log parent request: `22:18:04.020`
- log parent response: `22:18:04.068`
- log child id request: `22:18:04.743`
- log child id response: `22:18:04.828`
- parent ipv6: `fe80:0:0:0:98a1:7fe4:c631:1df3`
- parent extaddr: `9aa17fe4c6311df3`
- parent rloc16: `0x7c00`
- child extaddr: `c651f65117c68110`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **45 ms**
- Response -> Child ID Request: **705 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **813 ms**
- pcap parent request: `22:18:04.014` (frame 234)
- pcap parent response: `22:18:04.059` (frame 235)
- pcap child id request: `22:18:04.764` (frame 243)
- pcap child id response: `22:18:04.827` (frame 245)

#### PCAP-complete child attach 2

- log parent request: `22:18:08.587`
- log parent response: `22:18:08.898`
- log child id request: `22:18:08.985`
- log child id response: `22:18:09.105`
- parent ipv6: `fe80:0:0:0:c0d1:14c8:c43a:e008`
- parent extaddr: `c2d114c8c43ae008`
- parent rloc16: `0x5800`
- child extaddr: `c651f65117c68110`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **289 ms**
- Response -> Child ID Request: **97 ms**
- Child ID Request -> Response: **71 ms**
- Full Attach: **457 ms**
- pcap parent request: `22:18:08.628` (frame 247)
- pcap parent response: `22:18:08.917` (frame 250)
- pcap child id request: `22:18:09.014` (frame 252)
- pcap child id response: `22:18:09.085` (frame 256)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_child_20260628-222410-run04.log`

- manifest status: `completed`
- child extaddr: `428a257812bffe7f`
- switch target extaddr(s): `124e9fce2fbe7019, 124e9fce2fbe7019, 124e9fce2fbe7019`

#### PCAP-complete child attach 1

- log parent request: `22:30:02.314`
- log parent response: `22:30:02.394`
- log child id request: `22:30:03.036`
- log child id response: `22:30:03.127`
- parent ipv6: `fe80:0:0:0:9ca9:ad2a:d1c8:a35b`
- parent extaddr: `9ea9ad2ad1c8a35b`
- parent rloc16: `0x6c00`
- child extaddr: `428a257812bffe7f`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **78 ms**
- Response -> Child ID Request: **671 ms**
- Child ID Request -> Response: **71 ms**
- Full Attach: **820 ms**
- pcap parent request: `22:30:02.307` (frame 270)
- pcap parent response: `22:30:02.385` (frame 271)
- pcap child id request: `22:30:03.056` (frame 279)
- pcap child id response: `22:30:03.127` (frame 281)

#### PCAP-complete child attach 2

- log parent request: `22:30:06.375`
- log parent response: `22:30:06.607`
- log child id request: `22:30:06.648`
- log child id response: `22:30:06.737`
- parent ipv6: `fe80:0:0:0:104e:9fce:2fbe:7019`
- parent extaddr: `124e9fce2fbe7019`
- parent rloc16: `0x1c00`
- child extaddr: `428a257812bffe7f`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **181 ms**
- Response -> Child ID Request: **79 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **323 ms**
- pcap parent request: `22:30:06.416` (frame 283)
- pcap parent response: `22:30:06.597` (frame 284)
- pcap child id request: `22:30:06.676` (frame 286)
- pcap child id response: `22:30:06.739` (frame 288)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_child_20260628-223608-run05.log`

- manifest status: `completed`
- child extaddr: `a2ff3ff9e52c77f3`
- switch target extaddr(s): `4a2203248268156e, 4a2203248268156e, 4a2203248268156e`

#### PCAP-complete child attach 1

- log parent request: `22:42:00.150`
- log parent response: `22:42:00.244`
- log child id request: `22:42:00.918`
- log child id response: `22:42:01.002`
- parent ipv6: `fe80:0:0:0:a44e:bf5:4cf5:524`
- parent extaddr: `a64e0bf54cf50524`
- parent rloc16: `0xc800`
- child extaddr: `a2ff3ff9e52c77f3`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **246 ms**
- Response -> Child ID Request: **505 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **813 ms**
- pcap parent request: `22:42:00.188` (frame 291)
- pcap parent response: `22:42:00.434` (frame 294)
- pcap child id request: `22:42:00.939` (frame 300)
- pcap child id response: `22:42:01.001` (frame 302)

#### PCAP-complete child attach 2

- log parent request: `22:42:04.259`
- log parent response: `22:42:04.355`
- log child id request: `22:42:04.810`
- log child id response: `22:42:04.903`
- parent ipv6: `fe80:0:0:0:4822:324:8268:156e`
- parent extaddr: `4a2203248268156e`
- parent rloc16: `0xf400`
- child extaddr: `a2ff3ff9e52c77f3`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **455 ms**
- Response -> Child ID Request: **79 ms**
- Child ID Request -> Response: **69 ms**
- Full Attach: **603 ms**
- pcap parent request: `22:42:04.300` (frame 305)
- pcap parent response: `22:42:04.755` (frame 310)
- pcap child id request: `22:42:04.834` (frame 312)
- pcap child id response: `22:42:04.903` (frame 314)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_child_20260628-224806-run06.log`

- manifest status: `completed`
- child extaddr: `a279c2117930417a`
- switch target extaddr(s): `0af80cfcfb27db2d, 0af80cfcfb27db2d, 0af80cfcfb27db2d`

#### PCAP-complete child attach 1

- log parent request: `22:53:57.894`
- log parent response: `22:53:57.971`
- log child id request: `22:53:58.616`
- log child id response: `22:53:58.700`
- parent ipv6: `fe80:0:0:0:c0f2:e09b:9518:e454`
- parent extaddr: `c2f2e09b9518e454`
- parent rloc16: `0xac00`
- child extaddr: `a279c2117930417a`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **76 ms**
- Response -> Child ID Request: **676 ms**
- Child ID Request -> Response: **61 ms**
- Full Attach: **813 ms**
- pcap parent request: `22:53:57.887` (frame 1249)
- pcap parent response: `22:53:57.963` (frame 1250)
- pcap child id request: `22:53:58.639` (frame 1258)
- pcap child id response: `22:53:58.700` (frame 1260)

#### PCAP-complete child attach 2

- log parent request: `22:54:02.078`
- log parent response: `22:54:02.272`
- log child id request: `22:54:02.637`
- log child id response: `22:54:02.732`
- parent ipv6: `fe80:0:0:0:8f8:cfc:fb27:db2d`
- parent extaddr: `0af80cfcfb27db2d`
- parent rloc16: `0x9000`
- child extaddr: `a279c2117930417a`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **463 ms**
- Response -> Child ID Request: **80 ms**
- Child ID Request -> Response: **71 ms**
- Full Attach: **614 ms**
- pcap parent request: `22:54:02.119` (frame 1262)
- pcap parent response: `22:54:02.582` (frame 1267)
- pcap child id request: `22:54:02.662` (frame 1269)
- pcap child id response: `22:54:02.733` (frame 1271)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_child_20260628-230004-run07.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `52578c3f60aea7a9`
- switch target extaddr(s): `f22e5e7a8b00838b, f22e5e7a8b00838b, f22e5e7a8b00838b`

#### PCAP-complete child attach 1

- log parent request: `23:05:55.971`
- log parent response: `23:05:56.016`
- log child id request: `23:05:56.692`
- log child id response: `23:05:56.779`
- parent ipv6: `fe80:0:0:0:c8a2:d6cf:96e2:eb74`
- parent extaddr: `caa2d6cf96e2eb74`
- parent rloc16: `0x4400`
- child extaddr: `52578c3f60aea7a9`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **44 ms**
- Response -> Child ID Request: **707 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **814 ms**
- pcap parent request: `23:05:55.964` (frame 249)
- pcap parent response: `23:05:56.008` (frame 250)
- pcap child id request: `23:05:56.715` (frame 258)
- pcap child id response: `23:05:56.778` (frame 260)

#### PCAP-complete child attach 2

- log parent request: `23:06:00.089`
- log parent response: `23:06:00.328`
- log child id request: `23:06:00.423`
- log child id response: `23:06:00.516`
- parent ipv6: `fe80:0:0:0:f02e:5e7a:8b00:838b`
- parent extaddr: `f22e5e7a8b00838b`
- parent rloc16: `0x1800`
- child extaddr: `52578c3f60aea7a9`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **191 ms**
- Response -> Child ID Request: **126 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **387 ms**
- pcap parent request: `23:06:00.130` (frame 266)
- pcap parent response: `23:06:00.321` (frame 267)
- pcap child id request: `23:06:00.447` (frame 271)
- pcap child id response: `23:06:00.517` (frame 273)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_child_20260628-231202-run08.log`

- manifest status: `completed`
- child extaddr: `3afd25394c6b34c7`
- switch target extaddr(s): `926f6995f4bf4a90, 926f6995f4bf4a90, 926f6995f4bf4a90`

#### PCAP-complete child attach 1

- log parent request: `23:17:53.242`
- log parent response: `23:17:53.375`
- log child id request: `23:17:54.011`
- log child id response: `23:17:54.103`
- parent ipv6: `fe80:0:0:0:f407:49ad:9e69:80c9`
- parent extaddr: `f60749ad9e6980c9`
- parent rloc16: `0xf000`
- child extaddr: `3afd25394c6b34c7`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **82 ms**
- Response -> Child ID Request: **665 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **817 ms**
- pcap parent request: `23:17:53.287` (frame 1153)
- pcap parent response: `23:17:53.369` (frame 1154)
- pcap child id request: `23:17:54.034` (frame 1162)
- pcap child id response: `23:17:54.104` (frame 1164)

#### PCAP-complete child attach 2

- log parent request: `23:17:57.986`
- log parent response: `23:17:58.344`
- log child id request: `23:17:58.424`
- log child id response: `23:17:58.511`
- parent ipv6: `fe80:0:0:0:906f:6995:f4bf:4a90`
- parent extaddr: `926f6995f4bf4a90`
- parent rloc16: `0x6800`
- child extaddr: `3afd25394c6b34c7`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **311 ms**
- Response -> Child ID Request: **112 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **486 ms**
- pcap parent request: `23:17:58.027` (frame 1203)
- pcap parent response: `23:17:58.338` (frame 1204)
- pcap child id request: `23:17:58.450` (frame 1208)
- pcap child id response: `23:17:58.513` (frame 1210)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_child_20260628-232400-run09.log`

- manifest status: `completed`
- child extaddr: `923bc5a025c63285`
- switch target extaddr(s): `5ebcb7d782690bc7, 5ebcb7d782690bc7, 5ebcb7d782690bc7`

#### PCAP-complete child attach 1

- log parent request: `23:29:51.350`
- log parent response: `23:29:51.494`
- log child id request: `23:29:52.068`
- log child id response: `23:29:52.162`
- parent ipv6: `fe80:0:0:0:ec4a:e274:77f4:3ff8`
- parent extaddr: `ee4ae27477f43ff8`
- parent rloc16: `0xe000`
- child extaddr: `923bc5a025c63285`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **144 ms**
- Response -> Child ID Request: **606 ms**
- Child ID Request -> Response: **69 ms**
- Full Attach: **819 ms**
- pcap parent request: `23:29:51.345` (frame 436)
- pcap parent response: `23:29:51.489` (frame 437)
- pcap child id request: `23:29:52.095` (frame 446)
- pcap child id response: `23:29:52.164` (frame 448)

#### PCAP-complete child attach 2

- log parent request: `23:29:55.903`
- log parent response: `23:29:56.291`
- log child id request: `23:29:56.423`
- log child id response: `23:29:56.508`
- parent ipv6: `fe80:0:0:0:5cbc:b7d7:8269:bc7`
- parent extaddr: `5ebcb7d782690bc7`
- parent rloc16: `0xa000`
- child extaddr: `923bc5a025c63285`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **374 ms**
- Response -> Child ID Request: **129 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **565 ms**
- pcap parent request: `23:29:55.946` (frame 451)
- pcap parent response: `23:29:56.320` (frame 456)
- pcap child id request: `23:29:56.449` (frame 458)
- pcap child id response: `23:29:56.511` (frame 460)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_child_20260628-233558-run10.log`

- manifest status: `completed`
- child extaddr: `464d25677c1a0d91`
- switch target extaddr(s): `326686e6d084a374, 326686e6d084a374, 326686e6d084a374`

#### PCAP-complete child attach 1

- log parent request: `23:41:49.962`
- log parent response: `23:41:50.016`
- log child id request: `23:41:50.684`
- log child id response: `23:41:50.769`
- parent ipv6: `fe80:0:0:0:509c:f90d:5ee7:ad7b`
- parent extaddr: `529cf90d5ee7ad7b`
- parent rloc16: `0x2800`
- child extaddr: `464d25677c1a0d91`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **53 ms**
- Response -> Child ID Request: **698 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **815 ms**
- pcap parent request: `23:41:49.957` (frame 383)
- pcap parent response: `23:41:50.010` (frame 384)
- pcap child id request: `23:41:50.708` (frame 392)
- pcap child id response: `23:41:50.772` (frame 394)

#### PCAP-complete child attach 2

- log parent request: `23:41:54.123`
- log parent response: `23:41:54.189`
- log child id request: `23:41:54.656`
- log child id response: `23:41:54.742`
- parent ipv6: `fe80:0:0:0:3066:86e6:d084:a374`
- parent extaddr: `326686e6d084a374`
- parent rloc16: `0x0800`
- child extaddr: `464d25677c1a0d91`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **454 ms**
- Response -> Child ID Request: **111 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **627 ms**
- pcap parent request: `23:41:54.118` (frame 397)
- pcap parent response: `23:41:54.572` (frame 402)
- pcap child id request: `23:41:54.683` (frame 405)
- pcap child id response: `23:41:54.745` (frame 407)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_child_20260628-234756-run11.log`

- manifest status: `completed`
- child extaddr: `c283b3aa0b72423a`
- switch target extaddr(s): `6e2f88dc7afc4dc2, 6e2f88dc7afc4dc2, 6e2f88dc7afc4dc2`

#### PCAP-complete child attach 1

- log parent request: `23:53:47.527`
- log parent response: `23:53:47.646`
- log child id request: `23:53:48.245`
- log child id response: `23:53:48.330`
- parent ipv6: `fe80:0:0:0:4c8c:5894:3d8b:dd01`
- parent extaddr: `4e8c58943d8bdd01`
- parent rloc16: `0xd000`
- child extaddr: `c283b3aa0b72423a`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **120 ms**
- Response -> Child ID Request: **631 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **813 ms**
- pcap parent request: `23:53:47.521` (frame 181)
- pcap parent response: `23:53:47.641` (frame 182)
- pcap child id request: `23:53:48.272` (frame 190)
- pcap child id response: `23:53:48.334` (frame 192)

#### PCAP-complete child attach 2

- log parent request: `23:53:52.037`
- log parent response: `23:53:52.183`
- log child id request: `23:53:52.303`
- log child id response: `23:53:52.396`
- parent ipv6: `fe80:0:0:0:6c2f:88dc:7afc:4dc2`
- parent extaddr: `6e2f88dc7afc4dc2`
- parent rloc16: `0x2400`
- child extaddr: `c283b3aa0b72423a`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **98 ms**
- Response -> Child ID Request: **151 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **319 ms**
- pcap parent request: `23:53:52.082` (frame 196)
- pcap parent response: `23:53:52.180` (frame 197)
- pcap child id request: `23:53:52.331` (frame 202)
- pcap child id response: `23:53:52.401` (frame 204)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_child_20260628-235954-run12.log`

- manifest status: `completed`
- child extaddr: `62efeb0b9892c557`
- switch target extaddr(s): `faeb8b79f1235aac, faeb8b79f1235aac, faeb8b79f1235aac`

#### PCAP-complete child attach 1

- log parent request: `00:05:45.586`
- log parent response: `00:05:45.799`
- log child id request: `00:05:46.354`
- log child id response: `00:05:46.440`
- parent ipv6: `fe80:0:0:0:c85b:c9a:aea2:706a`
- parent extaddr: `ca5b0c9aaea2706a`
- parent rloc16: `0x4800`
- child extaddr: `62efeb0b9892c557`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **162 ms**
- Response -> Child ID Request: **587 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **811 ms**
- pcap parent request: `00:05:45.632` (frame 208)
- pcap parent response: `00:05:45.794` (frame 210)
- pcap child id request: `00:05:46.381` (frame 218)
- pcap child id response: `00:05:46.443` (frame 220)

#### PCAP-complete child attach 2

- log parent request: `00:05:50.221`
- log parent response: `00:05:50.329`
- log child id request: `00:05:50.422`
- log child id response: `00:05:50.536`
- parent ipv6: `fe80:0:0:0:f8eb:8b79:f123:5aac`
- parent extaddr: `faeb8b79f1235aac`
- parent rloc16: `0x7c00`
- child extaddr: `62efeb0b9892c557`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **127 ms**
- Response -> Child ID Request: **107 ms**
- Child ID Request -> Response: **68 ms**
- Full Attach: **302 ms**
- pcap parent request: `00:05:50.217` (frame 223)
- pcap parent response: `00:05:50.344` (frame 226)
- pcap child id request: `00:05:50.451` (frame 228)
- pcap child id response: `00:05:50.519` (frame 232)

#### PCAP-complete child attach 3

- log parent request: `00:09:46.387`
- log parent response: `00:09:46.450`
- log child id request: `00:09:47.108`
- log child id response: `00:09:47.199`
- parent ipv6: `fe80:0:0:0:3c9a:e67:1da8:4d7`
- parent extaddr: `3e9a0e671da804d7`
- parent rloc16: `0x2800`
- child extaddr: `62efeb0b9892c557`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **137 ms**
- Response -> Child ID Request: **611 ms**
- Child ID Request -> Response: **71 ms**
- Full Attach: **819 ms**
- pcap parent request: `00:09:46.394` (frame 639)
- pcap parent response: `00:09:46.531` (frame 642)
- pcap child id request: `00:09:47.142` (frame 646)
- pcap child id response: `00:09:47.213` (frame 648)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 79: 16, seq 80: 16, seq 81: 16, seq 82: 16
- failed tx by dst: `ca5b0c9aaea2706a`: 63

### `mcast_child_20260629-001152-run13.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `5a50f9606803cfa2`
- switch target extaddr(s): `323e10a703a21b72, 323e10a703a21b72, 323e10a703a21b72`

#### PCAP-complete child attach 1

- log parent request: `00:17:43.734`
- log parent response: `00:17:43.898`
- log child id request: `00:17:44.456`
- log child id response: `00:17:44.542`
- parent ipv6: `fe80:0:0:0:cb7:3f3f:75e1:36c3`
- parent extaddr: `0eb73f3f75e136c3`
- parent rloc16: `0xc000`
- child extaddr: `5a50f9606803cfa2`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **161 ms**
- Response -> Child ID Request: **590 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **814 ms**
- pcap parent request: `00:17:43.733` (frame 206)
- pcap parent response: `00:17:43.894` (frame 207)
- pcap child id request: `00:17:44.484` (frame 215)
- pcap child id response: `00:17:44.547` (frame 217)

#### PCAP-complete child attach 2

- log parent request: `00:17:47.942`
- log parent response: `00:17:48.301`
- log child id request: `00:17:48.525`
- log child id response: `00:17:48.620`
- parent ipv6: `fe80:0:0:0:303e:10a7:3a2:1b72`
- parent extaddr: `323e10a703a21b72`
- parent rloc16: `0x5800`
- child extaddr: `5a50f9606803cfa2`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **443 ms**
- Response -> Child ID Request: **122 ms**
- Child ID Request -> Response: **71 ms**
- Full Attach: **636 ms**
- pcap parent request: `00:17:47.989` (frame 220)
- pcap parent response: `00:17:48.432` (frame 223)
- pcap child id request: `00:17:48.554` (frame 227)
- pcap child id response: `00:17:48.625` (frame 229)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_child_20260629-002350-run14.log`

- manifest status: `completed`
- child extaddr: `aad2a83f8b27e64a`
- switch target extaddr(s): `2ada68be23ae2afd, 2ada68be23ae2afd, 2ada68be23ae2afd`

#### PCAP-complete child attach 1

- log parent request: `00:29:41.848`
- log parent response: `00:29:42.051`
- log child id request: `00:29:42.617`
- log child id response: `00:29:42.713`
- parent ipv6: `fe80:0:0:0:f084:efc8:ce93:f3f6`
- parent extaddr: `f284efc8ce93f3f6`
- parent rloc16: `0x1000`
- child extaddr: `aad2a83f8b27e64a`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **328 ms**
- Response -> Child ID Request: **423 ms**
- Child ID Request -> Response: **76 ms**
- Full Attach: **827 ms**
- pcap parent request: `00:29:41.893` (frame 187)
- pcap parent response: `00:29:42.221` (frame 190)
- pcap child id request: `00:29:42.644` (frame 196)
- pcap child id response: `00:29:42.720` (frame 198)

#### PCAP-complete child attach 2

- log parent request: `00:29:46.071`
- log parent response: `00:29:46.187`
- log child id request: `00:29:46.277`
- log child id response: `00:29:46.370`
- parent ipv6: `fe80:0:0:0:28da:68be:23ae:2afd`
- parent extaddr: `2ada68be23ae2afd`
- parent rloc16: `0xd800`
- child extaddr: `aad2a83f8b27e64a`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **67 ms**
- Response -> Child ID Request: **122 ms**
- Child ID Request -> Response: **71 ms**
- Full Attach: **260 ms**
- pcap parent request: `00:29:46.118` (frame 201)
- pcap parent response: `00:29:46.185` (frame 202)
- pcap child id request: `00:29:46.307` (frame 206)
- pcap child id response: `00:29:46.378` (frame 208)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_child_20260629-003548-run15.log`

- manifest status: `completed`
- child extaddr: `da5b1c28b080a2b1`
- switch target extaddr(s): `5a842feb7662ddbb, 5a842feb7662ddbb, 5a842feb7662ddbb`

#### PCAP-complete child attach 1

- log parent request: `00:41:39.886`
- log parent response: `00:41:40.044`
- log child id request: `00:41:40.607`
- log child id response: `00:41:40.698`
- parent ipv6: `fe80:0:0:0:1c97:8568:c808:9d4e`
- parent extaddr: `1e978568c8089d4e`
- parent rloc16: `0x6000`
- child extaddr: `da5b1c28b080a2b1`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **157 ms**
- Response -> Child ID Request: **593 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **820 ms**
- pcap parent request: `00:41:39.884` (frame 1100)
- pcap parent response: `00:41:40.041` (frame 1101)
- pcap child id request: `00:41:40.634` (frame 1110)
- pcap child id response: `00:41:40.704` (frame 1112)

#### PCAP-complete child attach 2

- log parent request: `00:41:43.959`
- log parent response: `00:41:44.185`
- log child id request: `00:41:44.509`
- log child id response: `00:41:44.607`
- parent ipv6: `fe80:0:0:0:5884:2feb:7662:ddbb`
- parent extaddr: `5a842feb7662ddbb`
- parent rloc16: `0xf800`
- child extaddr: `da5b1c28b080a2b1`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **405 ms**
- Response -> Child ID Request: **125 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **600 ms**
- pcap parent request: `00:41:44.013` (frame 1149)
- pcap parent response: `00:41:44.418` (frame 1155)
- pcap child id request: `00:41:44.543` (frame 1159)
- pcap child id response: `00:41:44.613` (frame 1161)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_child_20260629-004746-run16.log`

- manifest status: `completed`
- child extaddr: `fe884ce10658220c`
- switch target extaddr(s): `2eb316127ffde622, 2eb316127ffde622, 2eb316127ffde622`

#### PCAP-complete child attach 1

- log parent request: `00:53:37.283`
- log parent response: `00:53:37.327`
- log child id request: `00:53:37.999`
- log child id response: `00:53:38.084`
- parent ipv6: `fe80:0:0:0:ecc0:2d30:ed95:2684`
- parent extaddr: `eec02d30ed952684`
- parent rloc16: `0x1400`
- child extaddr: `fe884ce10658220c`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **329 ms**
- Response -> Child ID Request: **421 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **813 ms**
- pcap parent request: `00:53:37.274` (frame 1130)
- pcap parent response: `00:53:37.603` (frame 1135)
- pcap child id request: `00:53:38.024` (frame 1139)
- pcap child id response: `00:53:38.087` (frame 1141)

#### PCAP-complete child attach 2

- log parent request: `00:53:41.985`
- log parent response: `00:53:42.103`
- log child id request: `n/a`
- log child id response: `00:53:42.288`
- parent ipv6: `fe80:0:0:0:2cb3:1612:7ffd:e622`
- parent extaddr: `2eb316127ffde622`
- parent rloc16: `0x3800`
- child extaddr: `fe884ce10658220c`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **119 ms**
- Response -> Child ID Request: **77 ms**
- Child ID Request -> Response: **92 ms**
- Full Attach: **288 ms**
- pcap parent request: `00:53:41.980` (frame 1152)
- pcap parent response: `00:53:42.099` (frame 1153)
- pcap child id request: `00:53:42.176` (frame 1156)
- pcap child id response: `00:53:42.268` (frame 1160)

#### PCAP-complete child attach 3

- log parent request: `00:57:37.891`
- log parent response: `00:57:38.110`
- log child id request: `00:57:38.614`
- log child id response: `00:57:38.705`
- parent ipv6: `fe80:0:0:0:a88c:8539:e9d:5187`
- parent extaddr: `aa8c85390e9d5187`
- parent rloc16: `0x6000`
- child extaddr: `fe884ce10658220c`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **437 ms**
- Response -> Child ID Request: **312 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **819 ms**
- pcap parent request: `00:57:37.897` (frame 1501)
- pcap parent response: `00:57:38.334` (frame 1504)
- pcap child id request: `00:57:38.646` (frame 1508)
- pcap child id response: `00:57:38.716` (frame 1510)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `n/a`
- log parent response: `00:53:42.331`
- log child id request: `00:53:42.293`
- log child id response: `n/a`
- parent ipv6: `fe80:0:0:0:2cb3:1612:7ffd:e622`
- parent extaddr: `2eb316127ffde622`
- parent rloc16: `0x6000`
- child extaddr: `fe884ce10658220c`
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
- failed tx by seqnum: seq 93: 16, seq 94: 16, seq 95: 16, seq 96: 16
- failed tx by dst: `eec02d30ed952684`: 64

### `mcast_child_20260629-005944-run17.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `ae1305647671d0a5`
- switch target extaddr(s): `0a07785cbbdefada, 0a07785cbbdefada, 0a07785cbbdefada`

#### PCAP-complete child attach 1

- log parent request: `01:05:35.288`
- log parent response: `01:05:35.420`
- log child id request: `01:05:36.003`
- log child id response: `01:05:36.087`
- parent ipv6: `fe80:0:0:0:882b:34fa:e43f:6a7d`
- parent extaddr: `8a2b34fae43f6a7d`
- parent rloc16: `0x2c00`
- child extaddr: `ae1305647671d0a5`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **137 ms**
- Response -> Child ID Request: **613 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **813 ms**
- pcap parent request: `01:05:35.275` (frame 316)
- pcap parent response: `01:05:35.412` (frame 318)
- pcap child id request: `01:05:36.025` (frame 326)
- pcap child id response: `01:05:36.088` (frame 328)

#### PCAP-complete child attach 2

- log parent request: `01:05:39.983`
- log parent response: `01:05:40.059`
- log child id request: `01:05:40.152`
- log child id response: `01:05:40.241`
- parent ipv6: `fe80:0:0:0:807:785c:bbde:fada`
- parent extaddr: `0a07785cbbdefada`
- parent rloc16: `0x6800`
- child extaddr: `ae1305647671d0a5`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **76 ms**
- Response -> Child ID Request: **126 ms**
- Child ID Request -> Response: **65 ms**
- Full Attach: **267 ms**
- pcap parent request: `01:05:39.975` (frame 331)
- pcap parent response: `01:05:40.051` (frame 332)
- pcap child id request: `01:05:40.177` (frame 336)
- pcap child id response: `01:05:40.242` (frame 338)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_child_20260629-011142-run18.log`

- manifest status: `completed`
- child extaddr: `9e1f2c28d4c01f1e`
- switch target extaddr(s): `0a1db66d4970fe24, 0a1db66d4970fe24, 0a1db66d4970fe24`

#### PCAP-complete child attach 1

- log parent request: `01:17:33.206`
- log parent response: `01:17:33.315`
- log child id request: `01:17:34.011`
- log child id response: `01:17:34.069`
- parent ipv6: `fe80:0:0:0:ec30:6150:920d:ff90`
- parent extaddr: `ee306150920dff90`
- parent rloc16: `0x5000`
- child extaddr: `9e1f2c28d4c01f1e`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **56 ms**
- Response -> Child ID Request: **691 ms**
- Child ID Request -> Response: **71 ms**
- Full Attach: **818 ms**
- pcap parent request: `01:17:33.252` (frame 172)
- pcap parent response: `01:17:33.308` (frame 173)
- pcap child id request: `01:17:33.999` (frame 182)
- pcap child id response: `01:17:34.070` (frame 184)

#### PCAP-complete child attach 2

- log parent request: `01:17:37.971`
- log parent response: `01:17:38.068`
- log child id request: `01:17:38.165`
- log child id response: `01:17:38.251`
- parent ipv6: `fe80:0:0:0:81d:b66d:4970:fe24`
- parent extaddr: `0a1db66d4970fe24`
- parent rloc16: `0x8000`
- child extaddr: `9e1f2c28d4c01f1e`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **56 ms**
- Response -> Child ID Request: **119 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **237 ms**
- pcap parent request: `01:17:38.015` (frame 188)
- pcap parent response: `01:17:38.071` (frame 191)
- pcap child id request: `01:17:38.190` (frame 193)
- pcap child id response: `01:17:38.252` (frame 195)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_child_20260629-012340-run19.log`

- manifest status: `completed`
- child extaddr: `b2666febdce64c3c`
- switch target extaddr(s): `226fc3e2271c2771, 226fc3e2271c2771, 226fc3e2271c2771`

#### PCAP-complete child attach 1

- log parent request: `01:29:31.088`
- log parent response: `01:29:31.174`
- log child id request: `01:29:31.805`
- log child id response: `01:29:31.890`
- parent ipv6: `fe80:0:0:0:b422:87b5:fb75:9058`
- parent extaddr: `b62287b5fb759058`
- parent rloc16: `0x0c00`
- child extaddr: `b2666febdce64c3c`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **87 ms**
- Response -> Child ID Request: **662 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **812 ms**
- pcap parent request: `01:29:31.081` (frame 241)
- pcap parent response: `01:29:31.168` (frame 242)
- pcap child id request: `01:29:31.830` (frame 250)
- pcap child id response: `01:29:31.893` (frame 252)

#### PCAP-complete child attach 2

- log parent request: `01:29:35.754`
- log parent response: `01:29:35.851`
- log child id request: `01:29:36.164`
- log child id response: `01:29:36.262`
- parent ipv6: `fe80:0:0:0:206f:c3e2:271c:2771`
- parent extaddr: `226fc3e2271c2771`
- parent rloc16: `0xac00`
- child extaddr: `b2666febdce64c3c`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **366 ms**
- Response -> Child ID Request: **81 ms**
- Child ID Request -> Response: **69 ms**
- Full Attach: **516 ms**
- pcap parent request: `01:29:35.750` (frame 254)
- pcap parent response: `01:29:36.116` (frame 259)
- pcap child id request: `01:29:36.197` (frame 261)
- pcap child id response: `01:29:36.266` (frame 263)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_child_20260629-013538-run20.log`

- manifest status: `completed`
- child extaddr: `ea807b918f1cad28`
- switch target extaddr(s): `c2432ddedebf6704, c2432ddedebf6704, c2432ddedebf6704`

#### PCAP-complete child attach 1

- log parent request: `01:41:29.354`
- log parent response: `01:41:29.469`
- log child id request: `01:41:30.072`
- log child id response: `01:41:30.158`
- parent ipv6: `fe80:0:0:0:a404:b8e7:13c4:d8ce`
- parent extaddr: `a604b8e713c4d8ce`
- parent rloc16: `0xa800`
- child extaddr: `ea807b918f1cad28`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **117 ms**
- Response -> Child ID Request: **633 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **813 ms**
- pcap parent request: `01:41:29.350` (frame 187)
- pcap parent response: `01:41:29.467` (frame 188)
- pcap child id request: `01:41:30.100` (frame 197)
- pcap child id response: `01:41:30.163` (frame 199)

#### PCAP-complete child attach 2

- log parent request: `01:41:33.857`
- log parent response: `01:41:34.288`
- log child id request: `01:41:34.378`
- log child id response: `01:41:34.491`
- parent ipv6: `fe80:0:0:0:c043:2dde:debf:6704`
- parent extaddr: `c2432ddedebf6704`
- parent rloc16: `0x2c00`
- child extaddr: `ea807b918f1cad28`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **384 ms**
- Response -> Child ID Request: **121 ms**
- Child ID Request -> Response: **68 ms**
- Full Attach: **573 ms**
- pcap parent request: `01:41:33.903` (frame 203)
- pcap parent response: `01:41:34.287` (frame 204)
- pcap child id request: `01:41:34.408` (frame 208)
- pcap child id response: `01:41:34.476` (frame 212)

#### PCAP-complete child attach 3

- log parent request: `01:45:29.935`
- log parent response: `01:45:30.180`
- log child id request: `01:45:30.657`
- log child id response: `01:45:30.756`
- parent ipv6: `fe80:0:0:0:c043:2dde:debf:6704`
- parent extaddr: `c2432ddedebf6704`
- parent rloc16: `0x2c00`
- child extaddr: `ea807b918f1cad28`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **313 ms**
- Response -> Child ID Request: **437 ms**
- Child ID Request -> Response: **77 ms**
- Full Attach: **827 ms**
- pcap parent request: `01:45:29.943` (frame 626)
- pcap parent response: `01:45:30.256` (frame 629)
- pcap child id request: `01:45:30.693` (frame 633)
- pcap child id response: `01:45:30.770` (frame 635)

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 68: 16, seq 69: 16, seq 70: 16, seq 71: 16
- failed tx by dst: `a604b8e713c4d8ce`: 64
