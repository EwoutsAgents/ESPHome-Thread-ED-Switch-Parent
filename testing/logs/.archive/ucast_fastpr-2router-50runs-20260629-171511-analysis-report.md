# Child Log Analysis

## ucast_fastpr_child

Files analyzed: **50**

- batch folders: `ucast_fastpr-2router-50runs-20260629-171511`

### PCAP-complete child attach summary

| Attach | Metric | M (SD), ms | n |
| --- | --- | ---: | ---: |
| 1 | Request -> Response | 209.48 (123.27) | 50 |
| 1 | Response -> Child ID Request | 537.08 (123.62) | 50 |
| 1 | Child ID Request -> Response | 63.34 (1.78) | 50 |
| 1 | Full Attach | 809.90 (10.26) | 50 |
| 2 | Request -> Response | 40.22 (1.04) | 50 |
| 2 | Response -> Child ID Request | 105.18 (8.18) | 50 |
| 2 | Child ID Request -> Response | 64.08 (5.10) | 50 |
| 2 | Full Attach | 209.48 (10.12) | 50 |

| Metric | M (SD) | n |
| --- | ---: | ---: |
| Failed TX Attempts per Log | 0.00 (0.00) | 50 |
| Log-only or Partial Sequences per Log | 0.00 (0.00) | 50 |

### `ucast_fastpr_child_20260629-171538-run01.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `7e310b1424e709e7`
- switch target extaddr(s): `9aea862f60ed3caf, 9aea862f60ed3caf, 9aea862f60ed3caf`

#### PCAP-complete child attach 1

- log parent request: `17:21:21.147`
- log parent response: `17:21:21.472`
- log child id request: `17:21:21.918`
- log child id response: `17:21:22.008`
- parent ipv6: `fe80:0:0:0:cc78:e85d:a45:2b61`
- parent extaddr: `ce78e85d0a452b61`
- parent rloc16: `0xec00`
- child extaddr: `7e310b1424e709e7`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **267 ms**
- Response -> Child ID Request: **483 ms**
- Child ID Request -> Response: **65 ms**
- Full Attach: **815 ms**
- pcap parent request: `17:21:21.192` (frame 80)
- pcap parent response: `17:21:21.459` (frame 81)
- pcap child id request: `17:21:21.942` (frame 85)
- pcap child id response: `17:21:22.007` (frame 87)

#### PCAP-complete child attach 2

- log parent request: `17:21:25.519`
- log parent response: `17:21:25.624`
- log child id request: `17:21:25.679`
- log child id response: `17:21:25.772`
- parent ipv6: `fe80:0:0:0:98ea:862f:60ed:3caf`
- parent extaddr: `9aea862f60ed3caf`
- parent rloc16: `0xb400`
- child extaddr: `7e310b1424e709e7`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **40 ms**
- Response -> Child ID Request: **100 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **203 ms**
- pcap parent request: `17:21:25.566` (frame 89)
- pcap parent response: `17:21:25.606` (frame 91)
- pcap child id request: `17:21:25.706` (frame 93)
- pcap child id response: `17:21:25.769` (frame 95)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260629-172727-run02.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `6e3ca2d080c117ce`
- switch target extaddr(s): `82ecc376f774089f, 82ecc376f774089f, 82ecc376f774089f`

#### PCAP-complete child attach 1

- log parent request: `17:33:08.758`
- log parent response: `17:33:09.259`
- log child id request: `17:33:09.529`
- log child id response: `17:33:09.618`
- parent ipv6: `fe80:0:0:0:34ef:6b70:ddaa:3f86`
- parent extaddr: `36ef6b70ddaa3f86`
- parent rloc16: `0xdc00`
- child extaddr: `6e3ca2d080c117ce`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **444 ms**
- Response -> Child ID Request: **306 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **814 ms**
- pcap parent request: `17:33:08.801` (frame 80)
- pcap parent response: `17:33:09.245` (frame 81)
- pcap child id request: `17:33:09.551` (frame 85)
- pcap child id response: `17:33:09.615` (frame 87)

#### PCAP-complete child attach 2

- log parent request: `17:33:13.060`
- log parent response: `17:33:13.167`
- log child id request: `17:33:13.226`
- log child id response: `17:33:13.321`
- parent ipv6: `fe80:0:0:0:80ec:c376:f774:89f`
- parent extaddr: `82ecc376f774089f`
- parent rloc16: `0x5c00`
- child extaddr: `6e3ca2d080c117ce`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **39 ms**
- Response -> Child ID Request: **106 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **208 ms**
- pcap parent request: `17:33:13.107` (frame 89)
- pcap parent response: `17:33:13.146` (frame 91)
- pcap child id request: `17:33:13.252` (frame 93)
- pcap child id response: `17:33:13.315` (frame 95)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260629-173915-run03.log`

- manifest status: `completed`
- child extaddr: `fa9443ff25814c99`
- switch target extaddr(s): `722cbc15853ab750, 722cbc15853ab750, 722cbc15853ab750`

#### PCAP-complete child attach 1

- log parent request: `17:44:55.747`
- log parent response: `17:44:55.970`
- log child id request: `17:44:56.566`
- log child id response: `17:44:56.609`
- parent ipv6: `fe80:0:0:0:6015:246b:721a:b36e`
- parent extaddr: `6215246b721ab36e`
- parent rloc16: `0x2000`
- child extaddr: `fa9443ff25814c99`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **126 ms**
- Response -> Child ID Request: **589 ms**
- Child ID Request -> Response: **61 ms**
- Full Attach: **776 ms**
- pcap parent request: `17:44:55.829` (frame 71)
- pcap parent response: `17:44:55.955` (frame 72)
- pcap child id request: `17:44:56.544` (frame 76)
- pcap child id response: `17:44:56.605` (frame 78)

#### PCAP-complete child attach 2

- log parent request: `17:45:00.507`
- log parent response: `17:45:00.611`
- log child id request: `17:45:00.668`
- log child id response: `17:45:00.761`
- parent ipv6: `fe80:0:0:0:702c:bc15:853a:b750`
- parent extaddr: `722cbc15853ab750`
- parent rloc16: `0xa400`
- child extaddr: `fa9443ff25814c99`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **40 ms**
- Response -> Child ID Request: **102 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **206 ms**
- pcap parent request: `17:45:00.552` (frame 82)
- pcap parent response: `17:45:00.592` (frame 84)
- pcap child id request: `17:45:00.694` (frame 86)
- pcap child id response: `17:45:00.758` (frame 88)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260629-175102-run04.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `7e583ee7b1cb24e0`
- switch target extaddr(s): `869b2a0225d13ecf, 869b2a0225d13ecf, 869b2a0225d13ecf`

#### PCAP-complete child attach 1

- log parent request: `17:56:43.692`
- log parent response: `17:56:43.931`
- log child id request: `17:56:44.405`
- log child id response: `17:56:44.496`
- parent ipv6: `fe80:0:0:0:5471:e4d3:5f55:428b`
- parent extaddr: `5671e4d35f55428b`
- parent rloc16: `0xac00`
- child extaddr: `7e583ee7b1cb24e0`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **239 ms**
- Response -> Child ID Request: **509 ms**
- Child ID Request -> Response: **65 ms**
- Full Attach: **813 ms**
- pcap parent request: `17:56:43.679` (frame 79)
- pcap parent response: `17:56:43.918` (frame 80)
- pcap child id request: `17:56:44.427` (frame 84)
- pcap child id response: `17:56:44.492` (frame 86)

#### PCAP-complete child attach 2

- log parent request: `17:56:48.023`
- log parent response: `17:56:48.130`
- log child id request: `17:56:48.184`
- log child id response: `17:56:48.282`
- parent ipv6: `fe80:0:0:0:849b:2a02:25d1:3ecf`
- parent extaddr: `869b2a0225d13ecf`
- parent rloc16: `0xd000`
- child extaddr: `7e583ee7b1cb24e0`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **40 ms**
- Response -> Child ID Request: **103 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **205 ms**
- pcap parent request: `17:56:48.072` (frame 88)
- pcap parent response: `17:56:48.112` (frame 90)
- pcap child id request: `17:56:48.215` (frame 92)
- pcap child id response: `17:56:48.277` (frame 94)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260629-180250-run05.log`

- manifest status: `completed`
- child extaddr: `2a7e37ddeaec934d`
- switch target extaddr(s): `8604e4f7c833c2b9, 8604e4f7c833c2b9, 8604e4f7c833c2b9`

#### PCAP-complete child attach 1

- log parent request: `18:08:30.605`
- log parent response: `18:08:30.739`
- log child id request: `18:08:31.377`
- log child id response: `18:08:31.464`
- parent ipv6: `fe80:0:0:0:341f:e932:c785:ed35`
- parent extaddr: `361fe932c785ed35`
- parent rloc16: `0x3000`
- child extaddr: `2a7e37ddeaec934d`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **56 ms**
- Response -> Child ID Request: **689 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **807 ms**
- pcap parent request: `18:08:30.655` (frame 73)
- pcap parent response: `18:08:30.711` (frame 74)
- pcap child id request: `18:08:31.400` (frame 78)
- pcap child id response: `18:08:31.462` (frame 80)

#### PCAP-complete child attach 2

- log parent request: `18:08:35.293`
- log parent response: `18:08:35.401`
- log child id request: `18:08:35.459`
- log child id response: `18:08:35.555`
- parent ipv6: `fe80:0:0:0:8404:e4f7:c833:c2b9`
- parent extaddr: `8604e4f7c833c2b9`
- parent rloc16: `0xa800`
- child extaddr: `2a7e37ddeaec934d`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **40 ms**
- Response -> Child ID Request: **107 ms**
- Child ID Request -> Response: **65 ms**
- Full Attach: **212 ms**
- pcap parent request: `18:08:35.339` (frame 82)
- pcap parent response: `18:08:35.379` (frame 84)
- pcap child id request: `18:08:35.486` (frame 86)
- pcap child id response: `18:08:35.551` (frame 88)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260629-181437-run06.log`

- manifest status: `completed`
- child extaddr: `1ea9155b9d10e572`
- switch target extaddr(s): `d61381e9bac52a56, d61381e9bac52a56, d61381e9bac52a56`

#### PCAP-complete child attach 1

- log parent request: `18:20:18.706`
- log parent response: `18:20:19.067`
- log child id request: `18:20:19.477`
- log child id response: `18:20:19.569`
- parent ipv6: `fe80:0:0:0:44ab:a8f0:81f3:8c5b`
- parent extaddr: `46aba8f081f38c5b`
- parent rloc16: `0x3000`
- child extaddr: `1ea9155b9d10e572`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **304 ms**
- Response -> Child ID Request: **446 ms**
- Child ID Request -> Response: **66 ms**
- Full Attach: **816 ms**
- pcap parent request: `18:20:18.751` (frame 72)
- pcap parent response: `18:20:19.055` (frame 73)
- pcap child id request: `18:20:19.501` (frame 77)
- pcap child id response: `18:20:19.567` (frame 79)

#### PCAP-complete child attach 2

- log parent request: `18:20:23.010`
- log parent response: `18:20:23.116`
- log child id request: `18:20:23.175`
- log child id response: `18:20:23.310`
- parent ipv6: `fe80:0:0:0:d413:81e9:bac5:2a56`
- parent extaddr: `d61381e9bac52a56`
- parent rloc16: `0xd400`
- child extaddr: `1ea9155b9d10e572`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **40 ms**
- Response -> Child ID Request: **107 ms**
- Child ID Request -> Response: **98 ms**
- Full Attach: **245 ms**
- pcap parent request: `18:20:23.057` (frame 83)
- pcap parent response: `18:20:23.097` (frame 85)
- pcap child id request: `18:20:23.204` (frame 87)
- pcap child id response: `18:20:23.302` (frame 90)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260629-182625-run07.log`

- manifest status: `completed`
- child extaddr: `5607207bcfaa7a07`
- switch target extaddr(s): `762b0012fb681f90, 762b0012fb681f90, 762b0012fb681f90`

#### PCAP-complete child attach 1

- log parent request: `18:32:06.115`
- log parent response: `18:32:06.317`
- log child id request: `18:32:06.887`
- log child id response: `18:32:06.975`
- parent ipv6: `fe80:0:0:0:a467:d2b5:164b:3eac`
- parent extaddr: `a667d2b5164b3eac`
- parent rloc16: `0x8400`
- child extaddr: `5607207bcfaa7a07`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **144 ms**
- Response -> Child ID Request: **606 ms**
- Child ID Request -> Response: **61 ms**
- Full Attach: **811 ms**
- pcap parent request: `18:32:06.160` (frame 74)
- pcap parent response: `18:32:06.304` (frame 75)
- pcap child id request: `18:32:06.910` (frame 79)
- pcap child id response: `18:32:06.971` (frame 81)

#### PCAP-complete child attach 2

- log parent request: `18:32:10.517`
- log parent response: `18:32:10.623`
- log child id request: `18:32:10.677`
- log child id response: `18:32:10.775`
- parent ipv6: `fe80:0:0:0:742b:12:fb68:1f90`
- parent extaddr: `762b0012fb681f90`
- parent rloc16: `0x6400`
- child extaddr: `5607207bcfaa7a07`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **41 ms**
- Response -> Child ID Request: **104 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **208 ms**
- pcap parent request: `18:32:10.564` (frame 84)
- pcap parent response: `18:32:10.605` (frame 86)
- pcap child id request: `18:32:10.709` (frame 88)
- pcap child id response: `18:32:10.772` (frame 90)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260629-183812-run08.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `b62749f26e8a233c`
- switch target extaddr(s): `8652b6bdc0aebb5b, 8652b6bdc0aebb5b, 8652b6bdc0aebb5b`

#### PCAP-complete child attach 1

- log parent request: `18:43:53.257`
- log parent response: `18:43:53.760`
- log child id request: `18:43:54.074`
- log child id response: `18:43:54.120`
- parent ipv6: `fe80:0:0:0:d8e6:9d5c:4ebb:1721`
- parent extaddr: `dae69d5c4ebb1721`
- parent rloc16: `0xd800`
- child extaddr: `b62749f26e8a233c`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **409 ms**
- Response -> Child ID Request: **305 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **778 ms**
- pcap parent request: `18:43:53.338` (frame 73)
- pcap parent response: `18:43:53.747` (frame 74)
- pcap child id request: `18:43:54.052` (frame 79)
- pcap child id response: `18:43:54.116` (frame 81)

#### PCAP-complete child attach 2

- log parent request: `18:43:57.850`
- log parent response: `18:43:57.953`
- log child id request: `18:43:58.011`
- log child id response: `18:43:58.108`
- parent ipv6: `fe80:0:0:0:8452:b6bd:c0ae:bb5b`
- parent extaddr: `8652b6bdc0aebb5b`
- parent rloc16: `0xb400`
- child extaddr: `b62749f26e8a233c`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **41 ms**
- Response -> Child ID Request: **101 ms**
- Child ID Request -> Response: **66 ms**
- Full Attach: **208 ms**
- pcap parent request: `18:43:57.895` (frame 83)
- pcap parent response: `18:43:57.936` (frame 85)
- pcap child id request: `18:43:58.037` (frame 87)
- pcap child id response: `18:43:58.103` (frame 89)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260629-185000-run09.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `42e64abf3187c4a4`
- switch target extaddr(s): `1ec7cadcac670d39, 1ec7cadcac670d39, 1ec7cadcac670d39`

#### PCAP-complete child attach 1

- log parent request: `18:55:41.055`
- log parent response: `18:55:41.101`
- log child id request: `18:55:41.766`
- log child id response: `18:55:41.855`
- parent ipv6: `fe80:0:0:0:f025:81ab:b35e:5011`
- parent extaddr: `f22581abb35e5011`
- parent rloc16: `0x7800`
- child extaddr: `42e64abf3187c4a4`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **48 ms**
- Response -> Child ID Request: **702 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **813 ms**
- pcap parent request: `18:55:41.039` (frame 74)
- pcap parent response: `18:55:41.087` (frame 75)
- pcap child id request: `18:55:41.789` (frame 79)
- pcap child id response: `18:55:41.852` (frame 81)

#### PCAP-complete child attach 2

- log parent request: `18:55:45.680`
- log parent response: `18:55:45.786`
- log child id request: `18:55:45.839`
- log child id response: `18:55:45.939`
- parent ipv6: `fe80:0:0:0:1cc7:cadc:ac67:d39`
- parent extaddr: `1ec7cadcac670d39`
- parent rloc16: `0x9800`
- child extaddr: `42e64abf3187c4a4`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **39 ms**
- Response -> Child ID Request: **104 ms**
- Child ID Request -> Response: **65 ms**
- Full Attach: **208 ms**
- pcap parent request: `18:55:45.728` (frame 83)
- pcap parent response: `18:55:45.767` (frame 85)
- pcap child id request: `18:55:45.871` (frame 87)
- pcap child id response: `18:55:45.936` (frame 89)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260629-190148-run10.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `f2613fb5c4e17416`
- switch target extaddr(s): `f2278ec155684e47, f2278ec155684e47, f2278ec155684e47`

#### PCAP-complete child attach 1

- log parent request: `19:07:28.658`
- log parent response: `19:07:28.705`
- log child id request: `19:07:29.367`
- log child id response: `19:07:29.456`
- parent ipv6: `fe80:0:0:0:28cb:7def:831e:5f2e`
- parent extaddr: `2acb7def831e5f2e`
- parent rloc16: `0x4800`
- child extaddr: `f2613fb5c4e17416`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **53 ms**
- Response -> Child ID Request: **697 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **814 ms**
- pcap parent request: `19:07:28.640` (frame 76)
- pcap parent response: `19:07:28.693` (frame 77)
- pcap child id request: `19:07:29.390` (frame 81)
- pcap child id response: `19:07:29.454` (frame 83)

#### PCAP-complete child attach 2

- log parent request: `19:07:33.179`
- log parent response: `19:07:33.283`
- log child id request: `19:07:33.383`
- log child id response: `19:07:33.477`
- parent ipv6: `fe80:0:0:0:f027:8ec1:5568:4e47`
- parent extaddr: `f2278ec155684e47`
- parent rloc16: `0x9800`
- child extaddr: `f2613fb5c4e17416`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **40 ms**
- Response -> Child ID Request: **145 ms**
- Child ID Request -> Response: **65 ms**
- Full Attach: **250 ms**
- pcap parent request: `19:07:33.225` (frame 85)
- pcap parent response: `19:07:33.265` (frame 87)
- pcap child id request: `19:07:33.410` (frame 90)
- pcap child id response: `19:07:33.475` (frame 92)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260629-191335-run11.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `7ec73b80ef0536c4`
- switch target extaddr(s): `723c243d56f080a5, 723c243d56f080a5, 723c243d56f080a5`

#### PCAP-complete child attach 1

- log parent request: `19:19:16.435`
- log parent response: `19:19:16.728`
- log child id request: `19:19:17.207`
- log child id response: `19:19:17.303`
- parent ipv6: `fe80:0:0:0:1c0d:bf7a:c9ad:803b`
- parent extaddr: `1e0dbf7ac9ad803b`
- parent rloc16: `0x2400`
- child extaddr: `7ec73b80ef0536c4`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **236 ms**
- Response -> Child ID Request: **516 ms**
- Child ID Request -> Response: **71 ms**
- Full Attach: **823 ms**
- pcap parent request: `19:19:16.480` (frame 72)
- pcap parent response: `19:19:16.716` (frame 73)
- pcap child id request: `19:19:17.232` (frame 77)
- pcap child id response: `19:19:17.303` (frame 79)

#### PCAP-complete child attach 2

- log parent request: `19:19:20.599`
- log parent response: `19:19:20.703`
- log child id request: `19:19:20.759`
- log child id response: `19:19:20.858`
- parent ipv6: `fe80:0:0:0:703c:243d:56f0:80a5`
- parent extaddr: `723c243d56f080a5`
- parent rloc16: `0x1c00`
- child extaddr: `7ec73b80ef0536c4`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **39 ms**
- Response -> Child ID Request: **108 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **209 ms**
- pcap parent request: `19:19:20.646` (frame 81)
- pcap parent response: `19:19:20.685` (frame 83)
- pcap child id request: `19:19:20.793` (frame 85)
- pcap child id response: `19:19:20.855` (frame 87)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260629-192522-run12.log`

- manifest status: `completed`
- child extaddr: `7e8bd24327132e32`
- switch target extaddr(s): `86c3e232edadc05e, 86c3e232edadc05e, 86c3e232edadc05e`

#### PCAP-complete child attach 1

- log parent request: `19:31:03.726`
- log parent response: `19:31:03.895`
- log child id request: `19:31:04.437`
- log child id response: `19:31:04.525`
- parent ipv6: `fe80:0:0:0:f8f1:844e:a56c:87f9`
- parent extaddr: `faf1844ea56c87f9`
- parent rloc16: `0x1800`
- child extaddr: `7e8bd24327132e32`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **172 ms**
- Response -> Child ID Request: **577 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **812 ms**
- pcap parent request: `19:31:03.712` (frame 80)
- pcap parent response: `19:31:03.884` (frame 81)
- pcap child id request: `19:31:04.461` (frame 85)
- pcap child id response: `19:31:04.524` (frame 87)

#### PCAP-complete child attach 2

- log parent request: `19:31:07.928`
- log parent response: `19:31:08.033`
- log child id request: `19:31:08.093`
- log child id response: `19:31:08.189`
- parent ipv6: `fe80:0:0:0:84c3:e232:edad:c05e`
- parent extaddr: `86c3e232edadc05e`
- parent rloc16: `0x2800`
- child extaddr: `7e8bd24327132e32`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **40 ms**
- Response -> Child ID Request: **106 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **210 ms**
- pcap parent request: `19:31:07.976` (frame 90)
- pcap parent response: `19:31:08.016` (frame 92)
- pcap child id request: `19:31:08.122` (frame 94)
- pcap child id response: `19:31:08.186` (frame 96)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260629-193710-run13.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `0a3191bba07ab1a4`
- switch target extaddr(s): `ce865dd9a1d0ff99, ce865dd9a1d0ff99, ce865dd9a1d0ff99`

#### PCAP-complete child attach 1

- log parent request: `19:42:50.931`
- log parent response: `19:42:51.151`
- log child id request: `19:42:51.701`
- log child id response: `19:42:51.792`
- parent ipv6: `fe80:0:0:0:94d7:90a9:da99:3db4`
- parent extaddr: `96d790a9da993db4`
- parent rloc16: `0x0000`
- child extaddr: `0a3191bba07ab1a4`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **164 ms**
- Response -> Child ID Request: **586 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **814 ms**
- pcap parent request: `19:42:50.975` (frame 80)
- pcap parent response: `19:42:51.139` (frame 81)
- pcap child id request: `19:42:51.725` (frame 86)
- pcap child id response: `19:42:51.789` (frame 88)

#### PCAP-complete child attach 2

- log parent request: `19:42:55.168`
- log parent response: `19:42:55.272`
- log child id request: `19:42:55.329`
- log child id response: `19:42:55.427`
- parent ipv6: `fe80:0:0:0:cc86:5dd9:a1d0:ff99`
- parent extaddr: `ce865dd9a1d0ff99`
- parent rloc16: `0x7800`
- child extaddr: `0a3191bba07ab1a4`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **42 ms**
- Response -> Child ID Request: **99 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **204 ms**
- pcap parent request: `19:42:55.215` (frame 90)
- pcap parent response: `19:42:55.257` (frame 92)
- pcap child id request: `19:42:55.356` (frame 94)
- pcap child id response: `19:42:55.419` (frame 96)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260629-194857-run14.log`

- manifest status: `completed`
- child extaddr: `9219a90e2caa9ee9`
- switch target extaddr(s): `f2eacc909e2cd62c, f2eacc909e2cd62c, f2eacc909e2cd62c`

#### PCAP-complete child attach 1

- log parent request: `19:54:38.335`
- log parent response: `19:54:38.492`
- log child id request: `19:54:39.045`
- log child id response: `19:54:39.132`
- parent ipv6: `fe80:0:0:0:f83d:5393:c974:385f`
- parent extaddr: `fa3d5393c974385f`
- parent rloc16: `0xe800`
- child extaddr: `9219a90e2caa9ee9`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **159 ms**
- Response -> Child ID Request: **589 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **810 ms**
- pcap parent request: `19:54:38.319` (frame 81)
- pcap parent response: `19:54:38.478` (frame 82)
- pcap child id request: `19:54:39.067` (frame 86)
- pcap child id response: `19:54:39.129` (frame 88)

#### PCAP-complete child attach 2

- log parent request: `19:54:42.800`
- log parent response: `19:54:42.906`
- log child id request: `19:54:42.963`
- log child id response: `19:54:43.058`
- parent ipv6: `fe80:0:0:0:f0ea:cc90:9e2c:d62c`
- parent extaddr: `f2eacc909e2cd62c`
- parent rloc16: `0x6400`
- child extaddr: `9219a90e2caa9ee9`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **40 ms**
- Response -> Child ID Request: **101 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **204 ms**
- pcap parent request: `19:54:42.848` (frame 90)
- pcap parent response: `19:54:42.888` (frame 92)
- pcap child id request: `19:54:42.989` (frame 94)
- pcap child id response: `19:54:43.052` (frame 96)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260629-200045-run15.log`

- manifest status: `completed`
- child extaddr: `0eb1f503421203a6`
- switch target extaddr(s): `1a515152d0629239, 1a515152d0629239, 1a515152d0629239`

#### PCAP-complete child attach 1

- log parent request: `20:06:26.139`
- log parent response: `20:06:26.236`
- log child id request: `20:06:26.848`
- log child id response: `20:06:26.939`
- parent ipv6: `fe80:0:0:0:8040:7b5c:3e5:9a15`
- parent extaddr: `82407b5c03e59a15`
- parent rloc16: `0xb000`
- child extaddr: `0eb1f503421203a6`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **100 ms**
- Response -> Child ID Request: **652 ms**
- Child ID Request -> Response: **61 ms**
- Full Attach: **813 ms**
- pcap parent request: `20:06:26.123` (frame 77)
- pcap parent response: `20:06:26.223` (frame 78)
- pcap child id request: `20:06:26.875` (frame 82)
- pcap child id response: `20:06:26.936` (frame 84)

#### PCAP-complete child attach 2

- log parent request: `20:06:30.263`
- log parent response: `20:06:30.370`
- log child id request: `20:06:30.423`
- log child id response: `20:06:30.522`
- parent ipv6: `fe80:0:0:0:1851:5152:d062:9239`
- parent extaddr: `1a515152d0629239`
- parent rloc16: `0x8c00`
- child extaddr: `0eb1f503421203a6`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **40 ms**
- Response -> Child ID Request: **102 ms**
- Child ID Request -> Response: **65 ms**
- Full Attach: **207 ms**
- pcap parent request: `20:06:30.313` (frame 88)
- pcap parent response: `20:06:30.353` (frame 90)
- pcap child id request: `20:06:30.455` (frame 92)
- pcap child id response: `20:06:30.520` (frame 94)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260629-201232-run16.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `ee21129be0fce76f`
- switch target extaddr(s): `465ff51e7a33fa7a, 465ff51e7a33fa7a, 465ff51e7a33fa7a`

#### PCAP-complete child attach 1

- log parent request: `20:18:13.401`
- log parent response: `20:18:13.587`
- log child id request: `20:18:14.113`
- log child id response: `20:18:14.203`
- parent ipv6: `fe80:0:0:0:f87c:5abe:a929:11f1`
- parent extaddr: `fa7c5abea92911f1`
- parent rloc16: `0xb000`
- child extaddr: `ee21129be0fce76f`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **188 ms**
- Response -> Child ID Request: **563 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **815 ms**
- pcap parent request: `20:18:13.385` (frame 76)
- pcap parent response: `20:18:13.573` (frame 77)
- pcap child id request: `20:18:14.136` (frame 81)
- pcap child id response: `20:18:14.200` (frame 83)

#### PCAP-complete child attach 2

- log parent request: `20:18:17.689`
- log parent response: `20:18:17.793`
- log child id request: `20:18:17.850`
- log child id response: `20:18:17.943`
- parent ipv6: `fe80:0:0:0:445f:f51e:7a33:fa7a`
- parent extaddr: `465ff51e7a33fa7a`
- parent rloc16: `0xcc00`
- child extaddr: `ee21129be0fce76f`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **39 ms**
- Response -> Child ID Request: **104 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **206 ms**
- pcap parent request: `20:18:17.734` (frame 86)
- pcap parent response: `20:18:17.773` (frame 88)
- pcap child id request: `20:18:17.877` (frame 90)
- pcap child id response: `20:18:17.940` (frame 92)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260629-202420-run17.log`

- manifest status: `completed`
- child extaddr: `2e7d9de55f746281`
- switch target extaddr(s): `364290ca4e0ad252, 364290ca4e0ad252, 364290ca4e0ad252`

#### PCAP-complete child attach 1

- log parent request: `20:30:00.527`
- log parent response: `20:30:00.855`
- log child id request: `20:30:01.299`
- log child id response: `20:30:01.387`
- parent ipv6: `fe80:0:0:0:bc2e:cba1:bb69:438e`
- parent extaddr: `be2ecba1bb69438e`
- parent rloc16: `0x1400`
- child extaddr: `2e7d9de55f746281`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **264 ms**
- Response -> Child ID Request: **480 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **806 ms**
- pcap parent request: `20:30:00.577` (frame 71)
- pcap parent response: `20:30:00.841` (frame 72)
- pcap child id request: `20:30:01.321` (frame 76)
- pcap child id response: `20:30:01.383` (frame 78)

#### PCAP-complete child attach 2

- log parent request: `20:30:05.251`
- log parent response: `20:30:05.357`
- log child id request: `20:30:05.413`
- log child id response: `20:30:05.508`
- parent ipv6: `fe80:0:0:0:3442:90ca:4e0a:d252`
- parent extaddr: `364290ca4e0ad252`
- parent rloc16: `0xf800`
- child extaddr: `2e7d9de55f746281`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **40 ms**
- Response -> Child ID Request: **101 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **205 ms**
- pcap parent request: `20:30:05.298` (frame 81)
- pcap parent response: `20:30:05.338` (frame 83)
- pcap child id request: `20:30:05.439` (frame 85)
- pcap child id response: `20:30:05.503` (frame 87)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260629-203607-run18.log`

- manifest status: `completed`
- child extaddr: `56e88ca178d8ba97`
- switch target extaddr(s): `f6ab0a56c37ed44e, f6ab0a56c37ed44e, f6ab0a56c37ed44e`

#### PCAP-complete child attach 1

- log parent request: `20:41:48.360`
- log parent response: `20:41:48.534`
- log child id request: `20:41:49.066`
- log child id response: `20:41:49.154`
- parent ipv6: `fe80:0:0:0:c47c:287a:7500:c49a`
- parent extaddr: `c67c287a7500c49a`
- parent rloc16: `0xa400`
- child extaddr: `56e88ca178d8ba97`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **183 ms**
- Response -> Child ID Request: **567 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **812 ms**
- pcap parent request: `20:41:48.339` (frame 72)
- pcap parent response: `20:41:48.522` (frame 73)
- pcap child id request: `20:41:49.089` (frame 77)
- pcap child id response: `20:41:49.151` (frame 79)

#### PCAP-complete child attach 2

- log parent request: `20:41:52.751`
- log parent response: `20:41:52.857`
- log child id request: `20:41:52.947`
- log child id response: `20:41:53.050`
- parent ipv6: `fe80:0:0:0:f4ab:a56:c37e:d44e`
- parent extaddr: `f6ab0a56c37ed44e`
- parent rloc16: `0x0000`
- child extaddr: `56e88ca178d8ba97`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **41 ms**
- Response -> Child ID Request: **141 ms**
- Child ID Request -> Response: **66 ms**
- Full Attach: **248 ms**
- pcap parent request: `20:41:52.798` (frame 81)
- pcap parent response: `20:41:52.839` (frame 83)
- pcap child id request: `20:41:52.980` (frame 86)
- pcap child id response: `20:41:53.046` (frame 88)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260629-204755-run19.log`

- manifest status: `completed`
- child extaddr: `a2f7c88ccdf4e38d`
- switch target extaddr(s): `466916ed03da468d, 466916ed03da468d, 466916ed03da468d`

#### PCAP-complete child attach 1

- log parent request: `20:53:35.464`
- log parent response: `20:53:35.779`
- log child id request: `20:53:36.282`
- log child id response: `20:53:36.326`
- parent ipv6: `fe80:0:0:0:eccf:f1c:e925:ff2d`
- parent extaddr: `eecf0f1ce925ff2d`
- parent rloc16: `0x5800`
- child extaddr: `a2f7c88ccdf4e38d`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **220 ms**
- Response -> Child ID Request: **493 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **776 ms**
- pcap parent request: `20:53:35.546` (frame 73)
- pcap parent response: `20:53:35.766` (frame 74)
- pcap child id request: `20:53:36.259` (frame 78)
- pcap child id response: `20:53:36.322` (frame 80)

#### PCAP-complete child attach 2

- log parent request: `20:53:40.223`
- log parent response: `20:53:40.328`
- log child id request: `20:53:40.382`
- log child id response: `20:53:40.481`
- parent ipv6: `fe80:0:0:0:4469:16ed:3da:468d`
- parent extaddr: `466916ed03da468d`
- parent rloc16: `0x8400`
- child extaddr: `a2f7c88ccdf4e38d`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **41 ms**
- Response -> Child ID Request: **102 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **207 ms**
- pcap parent request: `20:53:40.270` (frame 82)
- pcap parent response: `20:53:40.311` (frame 84)
- pcap child id request: `20:53:40.413` (frame 86)
- pcap child id response: `20:53:40.477` (frame 88)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260629-205942-run20.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `725d809d480ae449`
- switch target extaddr(s): `fec3ad0361b667fc, fec3ad0361b667fc, fec3ad0361b667fc`

#### PCAP-complete child attach 1

- log parent request: `21:05:23.732`
- log parent response: `21:05:23.858`
- log child id request: `21:05:24.444`
- log child id response: `21:05:24.533`
- parent ipv6: `fe80:0:0:0:a465:ad29:ad11:85b9`
- parent extaddr: `a665ad29ad1185b9`
- parent rloc16: `0x5400`
- child extaddr: `725d809d480ae449`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **128 ms**
- Response -> Child ID Request: **622 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **814 ms**
- pcap parent request: `21:05:23.716` (frame 77)
- pcap parent response: `21:05:23.844` (frame 78)
- pcap child id request: `21:05:24.466` (frame 82)
- pcap child id response: `21:05:24.530` (frame 84)

#### PCAP-complete child attach 2

- log parent request: `21:05:27.798`
- log parent response: `21:05:27.903`
- log child id request: `21:05:27.960`
- log child id response: `21:05:28.052`
- parent ipv6: `fe80:0:0:0:fcc3:ad03:61b6:67fc`
- parent extaddr: `fec3ad0361b667fc`
- parent rloc16: `0x2400`
- child extaddr: `725d809d480ae449`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **39 ms**
- Response -> Child ID Request: **103 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **204 ms**
- pcap parent request: `21:05:27.844` (frame 86)
- pcap parent response: `21:05:27.883` (frame 88)
- pcap child id request: `21:05:27.986` (frame 90)
- pcap child id response: `21:05:28.048` (frame 92)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260629-211130-run21.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `12506523a15d2ad7`
- switch target extaddr(s): `ded6ea1f8e43547d, ded6ea1f8e43547d, ded6ea1f8e43547d`

#### PCAP-complete child attach 1

- log parent request: `21:17:10.771`
- log parent response: `21:17:11.009`
- log child id request: `21:17:11.541`
- log child id response: `21:17:11.631`
- parent ipv6: `fe80:0:0:0:6c98:1c00:7522:3dc3`
- parent extaddr: `6e981c0075223dc3`
- parent rloc16: `0xa000`
- child extaddr: `12506523a15d2ad7`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **182 ms**
- Response -> Child ID Request: **568 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **813 ms**
- pcap parent request: `21:17:10.814` (frame 78)
- pcap parent response: `21:17:10.996` (frame 79)
- pcap child id request: `21:17:11.564` (frame 83)
- pcap child id response: `21:17:11.627` (frame 85)

#### PCAP-complete child attach 2

- log parent request: `21:17:15.389`
- log parent response: `21:17:15.494`
- log child id request: `21:17:15.551`
- log child id response: `21:17:15.645`
- parent ipv6: `fe80:0:0:0:dcd6:ea1f:8e43:547d`
- parent extaddr: `ded6ea1f8e43547d`
- parent rloc16: `0x0c00`
- child extaddr: `12506523a15d2ad7`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **39 ms**
- Response -> Child ID Request: **102 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **203 ms**
- pcap parent request: `21:17:15.436` (frame 87)
- pcap parent response: `21:17:15.475` (frame 89)
- pcap child id request: `21:17:15.577` (frame 91)
- pcap child id response: `21:17:15.639` (frame 93)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260629-212317-run22.log`

- manifest status: `completed`
- child extaddr: `cab05458c6d2cf49`
- switch target extaddr(s): `b656180b95eca781, b656180b95eca781, b656180b95eca781`

#### PCAP-complete child attach 1

- log parent request: `21:28:58.709`
- log parent response: `21:28:58.784`
- log child id request: `21:28:59.421`
- log child id response: `21:28:59.509`
- parent ipv6: `fe80:0:0:0:9095:14c1:dc9b:68df`
- parent extaddr: `929514c1dc9b68df`
- parent rloc16: `0x1c00`
- child extaddr: `cab05458c6d2cf49`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **76 ms**
- Response -> Child ID Request: **674 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **812 ms**
- pcap parent request: `21:28:58.695` (frame 78)
- pcap parent response: `21:28:58.771` (frame 79)
- pcap child id request: `21:28:59.445` (frame 83)
- pcap child id response: `21:28:59.507` (frame 85)

#### PCAP-complete child attach 2

- log parent request: `21:29:02.886`
- log parent response: `21:29:02.990`
- log child id request: `21:29:03.051`
- log child id response: `21:29:03.145`
- parent ipv6: `fe80:0:0:0:b456:180b:95ec:a781`
- parent extaddr: `b656180b95eca781`
- parent rloc16: `0x2800`
- child extaddr: `cab05458c6d2cf49`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **40 ms**
- Response -> Child ID Request: **105 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **208 ms**
- pcap parent request: `21:29:02.933` (frame 88)
- pcap parent response: `21:29:02.973` (frame 90)
- pcap child id request: `21:29:03.078` (frame 92)
- pcap child id response: `21:29:03.141` (frame 94)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260629-213505-run23.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `8a6c64add0df100b`
- switch target extaddr(s): `56df15597dd6a846, 56df15597dd6a846, 56df15597dd6a846`

#### PCAP-complete child attach 1

- log parent request: `21:40:46.103`
- log parent response: `21:40:46.325`
- log child id request: `21:40:46.814`
- log child id response: `21:40:46.904`
- parent ipv6: `fe80:0:0:0:a4f3:68f4:2698:180e`
- parent extaddr: `a6f368f42698180e`
- parent rloc16: `0xa400`
- child extaddr: `8a6c64add0df100b`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **225 ms**
- Response -> Child ID Request: **525 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **813 ms**
- pcap parent request: `21:40:46.088` (frame 79)
- pcap parent response: `21:40:46.313` (frame 80)
- pcap child id request: `21:40:46.838` (frame 85)
- pcap child id response: `21:40:46.901` (frame 87)

#### PCAP-complete child attach 2

- log parent request: `21:40:50.390`
- log parent response: `21:40:50.494`
- log child id request: `21:40:50.554`
- log child id response: `21:40:50.649`
- parent ipv6: `fe80:0:0:0:54df:1559:7dd6:a846`
- parent extaddr: `56df15597dd6a846`
- parent rloc16: `0x7800`
- child extaddr: `8a6c64add0df100b`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **39 ms**
- Response -> Child ID Request: **107 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **208 ms**
- pcap parent request: `21:40:50.436` (frame 90)
- pcap parent response: `21:40:50.475` (frame 92)
- pcap child id request: `21:40:50.582` (frame 94)
- pcap child id response: `21:40:50.644` (frame 96)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260629-214652-run24.log`

- manifest status: `completed`
- child extaddr: `4a0c455eac96f6af`
- switch target extaddr(s): `def8e32dc6ae2b3d, def8e32dc6ae2b3d, def8e32dc6ae2b3d`

#### PCAP-complete child attach 1

- log parent request: `21:52:33.697`
- log parent response: `21:52:33.741`
- log child id request: `21:52:34.408`
- log child id response: `21:52:34.496`
- parent ipv6: `fe80:0:0:0:44c2:5990:7dd9:7bbf`
- parent extaddr: `46c259907dd97bbf`
- parent rloc16: `0x4800`
- child extaddr: `4a0c455eac96f6af`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **47 ms**
- Response -> Child ID Request: **703 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **812 ms**
- pcap parent request: `21:52:33.682` (frame 72)
- pcap parent response: `21:52:33.729` (frame 73)
- pcap child id request: `21:52:34.432` (frame 77)
- pcap child id response: `21:52:34.494` (frame 79)

#### PCAP-complete child attach 2

- log parent request: `21:52:37.702`
- log parent response: `21:52:37.849`
- log child id request: `21:52:37.903`
- log child id response: `21:52:38.002`
- parent ipv6: `fe80:0:0:0:dcf8:e32d:c6ae:2b3d`
- parent extaddr: `def8e32dc6ae2b3d`
- parent rloc16: `0xc800`
- child extaddr: `4a0c455eac96f6af`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **41 ms**
- Response -> Child ID Request: **107 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **212 ms**
- pcap parent request: `21:52:37.788` (frame 82)
- pcap parent response: `21:52:37.829` (frame 84)
- pcap child id request: `21:52:37.936` (frame 86)
- pcap child id response: `21:52:38.000` (frame 88)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260629-215840-run25.log`

- manifest status: `completed`
- child extaddr: `5afbe546e1af50e7`
- switch target extaddr(s): `8eb13c1679b3824c, 8eb13c1679b3824c, 8eb13c1679b3824c`

#### PCAP-complete child attach 1

- log parent request: `22:04:20.595`
- log parent response: `22:04:20.762`
- log child id request: `22:04:21.414`
- log child id response: `22:04:21.457`
- parent ipv6: `fe80:0:0:0:acc2:fcd8:a4c:52ae`
- parent extaddr: `aec2fcd80a4c52ae`
- parent rloc16: `0xc000`
- child extaddr: `5afbe546e1af50e7`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **62 ms**
- Response -> Child ID Request: **653 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **777 ms**
- pcap parent request: `22:04:20.676` (frame 73)
- pcap parent response: `22:04:20.738` (frame 74)
- pcap child id request: `22:04:21.391` (frame 78)
- pcap child id response: `22:04:21.453` (frame 80)

#### PCAP-complete child attach 2

- log parent request: `22:04:25.354`
- log parent response: `22:04:25.461`
- log child id request: `22:04:25.513`
- log child id response: `22:04:25.612`
- parent ipv6: `fe80:0:0:0:8cb1:3c16:79b3:824c`
- parent extaddr: `8eb13c1679b3824c`
- parent rloc16: `0xb400`
- child extaddr: `5afbe546e1af50e7`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **40 ms**
- Response -> Child ID Request: **102 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **206 ms**
- pcap parent request: `22:04:25.401` (frame 83)
- pcap parent response: `22:04:25.441` (frame 85)
- pcap child id request: `22:04:25.543` (frame 87)
- pcap child id response: `22:04:25.607` (frame 89)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260629-221027-run26.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `f23665e362779f95`
- switch target extaddr(s): `36d273f861a58ec3, 36d273f861a58ec3, 36d273f861a58ec3`

#### PCAP-complete child attach 1

- log parent request: `22:16:08.518`
- log parent response: `22:16:08.691`
- log child id request: `22:16:09.290`
- log child id response: `22:16:09.382`
- parent ipv6: `fe80:0:0:0:e4e8:ac9b:4e5c:bbd9`
- parent extaddr: `e6e8ac9b4e5cbbd9`
- parent rloc16: `0x2000`
- child extaddr: `f23665e362779f95`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **115 ms**
- Response -> Child ID Request: **636 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **815 ms**
- pcap parent request: `22:16:08.561` (frame 76)
- pcap parent response: `22:16:08.676` (frame 77)
- pcap child id request: `22:16:09.312` (frame 82)
- pcap child id response: `22:16:09.376` (frame 84)

#### PCAP-complete child attach 2

- log parent request: `22:16:12.891`
- log parent response: `n/a`
- log child id request: `22:16:12.930`
- log child id response: `22:16:13.022`
- parent ipv6: `fe80:0:0:0:34d2:73f8:61a5:8ec3`
- parent extaddr: `36d273f861a58ec3`
- parent rloc16: `0x2c00`
- child extaddr: `f23665e362779f95`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **40 ms**
- Response -> Child ID Request: **102 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **204 ms**
- pcap parent request: `22:16:12.812` (frame 87)
- pcap parent response: `22:16:12.852` (frame 89)
- pcap child id request: `22:16:12.954` (frame 91)
- pcap child id response: `22:16:13.016` (frame 93)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260629-222215-run27.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `d62d5aaab2c7ca9e`
- switch target extaddr(s): `ae9e2d80c26b4835, ae9e2d80c26b4835, ae9e2d80c26b4835`

#### PCAP-complete child attach 1

- log parent request: `22:27:55.805`
- log parent response: `22:27:56.277`
- log child id request: `22:27:56.624`
- log child id response: `22:27:56.666`
- parent ipv6: `fe80:0:0:0:2c14:2c6d:9de1:dfb0`
- parent extaddr: `2e142c6d9de1dfb0`
- parent rloc16: `0xc400`
- child extaddr: `d62d5aaab2c7ca9e`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **413 ms**
- Response -> Child ID Request: **336 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **813 ms**
- pcap parent request: `22:27:55.849` (frame 78)
- pcap parent response: `22:27:56.262` (frame 79)
- pcap child id request: `22:27:56.598` (frame 83)
- pcap child id response: `22:27:56.662` (frame 85)

#### PCAP-complete child attach 2

- log parent request: `22:28:00.290`
- log parent response: `22:28:00.394`
- log child id request: `22:28:00.452`
- log child id response: `22:28:00.542`
- parent ipv6: `fe80:0:0:0:ac9e:2d80:c26b:4835`
- parent extaddr: `ae9e2d80c26b4835`
- parent rloc16: `0x9800`
- child extaddr: `d62d5aaab2c7ca9e`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **40 ms**
- Response -> Child ID Request: **102 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **205 ms**
- pcap parent request: `22:28:00.335` (frame 87)
- pcap parent response: `22:28:00.375` (frame 89)
- pcap child id request: `22:28:00.477` (frame 91)
- pcap child id response: `22:28:00.540` (frame 93)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260629-223402-run28.log`

- manifest status: `completed`
- child extaddr: `02961b7662a7a312`
- switch target extaddr(s): `cee57509431b7b61, cee57509431b7b61, cee57509431b7b61`

#### PCAP-complete child attach 1

- log parent request: `22:39:43.092`
- log parent response: `22:39:43.280`
- log child id request: `22:39:43.797`
- log child id response: `22:39:43.884`
- parent ipv6: `fe80:0:0:0:548f:4804:b08:f7d9`
- parent extaddr: `568f48040b08f7d9`
- parent rloc16: `0x2000`
- child extaddr: `02961b7662a7a312`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **197 ms**
- Response -> Child ID Request: **553 ms**
- Child ID Request -> Response: **61 ms**
- Full Attach: **811 ms**
- pcap parent request: `22:39:43.071` (frame 75)
- pcap parent response: `22:39:43.268` (frame 76)
- pcap child id request: `22:39:43.821` (frame 80)
- pcap child id response: `22:39:43.882` (frame 82)

#### PCAP-complete child attach 2

- log parent request: `22:39:47.665`
- log parent response: `22:39:47.771`
- log child id request: `22:39:47.828`
- log child id response: `22:39:47.922`
- parent ipv6: `fe80:0:0:0:cce5:7509:431b:7b61`
- parent extaddr: `cee57509431b7b61`
- parent rloc16: `0x5000`
- child extaddr: `02961b7662a7a312`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **43 ms**
- Response -> Child ID Request: **100 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **207 ms**
- pcap parent request: `22:39:47.713` (frame 84)
- pcap parent response: `22:39:47.756` (frame 86)
- pcap child id request: `22:39:47.856` (frame 88)
- pcap child id response: `22:39:47.920` (frame 90)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260629-224550-run29.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `8ee0d98776cb9b9f`
- switch target extaddr(s): `42d7361dbd9f5260, 42d7361dbd9f5260, 42d7361dbd9f5260`

#### PCAP-complete child attach 1

- log parent request: `22:51:30.512`
- log parent response: `22:51:30.873`
- log child id request: `22:51:31.283`
- log child id response: `22:51:31.373`
- parent ipv6: `fe80:0:0:0:a46b:66cb:d70:8a42`
- parent extaddr: `a66b66cb0d708a42`
- parent rloc16: `0x5400`
- child extaddr: `8ee0d98776cb9b9f`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **297 ms**
- Response -> Child ID Request: **446 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **806 ms**
- pcap parent request: `22:51:30.565` (frame 79)
- pcap parent response: `22:51:30.862` (frame 80)
- pcap child id request: `22:51:31.308` (frame 84)
- pcap child id response: `22:51:31.371` (frame 86)

#### PCAP-complete child attach 2

- log parent request: `22:51:35.234`
- log parent response: `22:51:35.342`
- log child id request: `22:51:35.399`
- log child id response: `22:51:35.494`
- parent ipv6: `fe80:0:0:0:40d7:361d:bd9f:5260`
- parent extaddr: `42d7361dbd9f5260`
- parent rloc16: `0xa000`
- child extaddr: `8ee0d98776cb9b9f`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **39 ms**
- Response -> Child ID Request: **102 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **204 ms**
- pcap parent request: `22:51:35.286` (frame 88)
- pcap parent response: `22:51:35.325` (frame 90)
- pcap child id request: `22:51:35.427` (frame 92)
- pcap child id response: `22:51:35.490` (frame 94)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260629-225737-run30.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `4a1d2a0f5126dbc6`
- switch target extaddr(s): `86c64bca5b87e921, 86c64bca5b87e921, 86c64bca5b87e921`

#### PCAP-complete child attach 1

- log parent request: `23:03:18.001`
- log parent response: `23:03:18.329`
- log child id request: `23:03:18.773`
- log child id response: `23:03:18.863`
- parent ipv6: `fe80:0:0:0:867:6eaf:dbe5:19dd`
- parent extaddr: `0a676eafdbe519dd`
- parent rloc16: `0xf800`
- child extaddr: `4a1d2a0f5126dbc6`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **267 ms**
- Response -> Child ID Request: **480 ms**
- Child ID Request -> Response: **65 ms**
- Full Attach: **812 ms**
- pcap parent request: `23:03:18.049` (frame 81)
- pcap parent response: `23:03:18.316` (frame 82)
- pcap child id request: `23:03:18.796` (frame 86)
- pcap child id response: `23:03:18.861` (frame 88)

#### PCAP-complete child attach 2

- log parent request: `23:03:22.837`
- log parent response: `n/a`
- log child id request: `23:03:22.871`
- log child id response: `23:03:22.967`
- parent ipv6: `fe80:0:0:0:84c6:4bca:5b87:e921`
- parent extaddr: `86c64bca5b87e921`
- parent rloc16: `0x4400`
- child extaddr: `4a1d2a0f5126dbc6`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **39 ms**
- Response -> Child ID Request: **105 ms**
- Child ID Request -> Response: **61 ms**
- Full Attach: **205 ms**
- pcap parent request: `23:03:22.760` (frame 90)
- pcap parent response: `23:03:22.799` (frame 92)
- pcap child id request: `23:03:22.904` (frame 94)
- pcap child id response: `23:03:22.965` (frame 96)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260629-230925-run31.log`

- manifest status: `completed`
- child extaddr: `664ac46cf1bc537d`
- switch target extaddr(s): `7e786efe09923059, 7e786efe09923059, 7e786efe09923059`

#### PCAP-complete child attach 1

- log parent request: `23:15:05.960`
- log parent response: `23:15:06.123`
- log child id request: `23:15:06.733`
- log child id response: `23:15:06.826`
- parent ipv6: `fe80:0:0:0:940b:a17b:1b0b:7692`
- parent extaddr: `960ba17b1b0b7692`
- parent rloc16: `0xcc00`
- child extaddr: `664ac46cf1bc537d`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **106 ms**
- Response -> Child ID Request: **646 ms**
- Child ID Request -> Response: **66 ms**
- Full Attach: **818 ms**
- pcap parent request: `23:15:06.004` (frame 78)
- pcap parent response: `23:15:06.110` (frame 79)
- pcap child id request: `23:15:06.756` (frame 84)
- pcap child id response: `23:15:06.822` (frame 86)

#### PCAP-complete child attach 2

- log parent request: `23:15:10.258`
- log parent response: `23:15:10.365`
- log child id request: `23:15:10.421`
- log child id response: `23:15:10.516`
- parent ipv6: `fe80:0:0:0:7c78:6efe:992:3059`
- parent extaddr: `7e786efe09923059`
- parent rloc16: `0x9800`
- child extaddr: `664ac46cf1bc537d`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **41 ms**
- Response -> Child ID Request: **104 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **208 ms**
- pcap parent request: `23:15:10.304` (frame 88)
- pcap parent response: `23:15:10.345` (frame 90)
- pcap child id request: `23:15:10.449` (frame 92)
- pcap child id response: `23:15:10.512` (frame 94)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260629-232112-run32.log`

- manifest status: `completed`
- child extaddr: `02b1e0ee836b6bf8`
- switch target extaddr(s): `d6a6e7baa79943b1, d6a6e7baa79943b1, d6a6e7baa79943b1`

#### PCAP-complete child attach 1

- log parent request: `23:26:53.421`
- log parent response: `23:26:53.583`
- log child id request: `23:26:54.132`
- log child id response: `23:26:54.220`
- parent ipv6: `fe80:0:0:0:9456:d054:e4b2:2a24`
- parent extaddr: `9656d054e4b22a24`
- parent rloc16: `0x0000`
- child extaddr: `02b1e0ee836b6bf8`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **164 ms**
- Response -> Child ID Request: **586 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **812 ms**
- pcap parent request: `23:26:53.405` (frame 72)
- pcap parent response: `23:26:53.569` (frame 73)
- pcap child id request: `23:26:54.155` (frame 77)
- pcap child id response: `23:26:54.217` (frame 79)

#### PCAP-complete child attach 2

- log parent request: `23:26:57.739`
- log parent response: `23:26:57.844`
- log child id request: `23:26:57.898`
- log child id response: `23:26:57.997`
- parent ipv6: `fe80:0:0:0:d4a6:e7ba:a799:43b1`
- parent extaddr: `d6a6e7baa79943b1`
- parent rloc16: `0x2400`
- child extaddr: `02b1e0ee836b6bf8`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **40 ms**
- Response -> Child ID Request: **105 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **209 ms**
- pcap parent request: `23:26:57.785` (frame 81)
- pcap parent response: `23:26:57.825` (frame 83)
- pcap child id request: `23:26:57.930` (frame 85)
- pcap child id response: `23:26:57.994` (frame 87)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260629-233300-run33.log`

- manifest status: `completed`
- child extaddr: `d6e722f2a32d4a1a`
- switch target extaddr(s): `be66d6d98db7da67, be66d6d98db7da67, be66d6d98db7da67`

#### PCAP-complete child attach 1

- log parent request: `23:38:41.261`
- log parent response: `23:38:41.583`
- log child id request: `23:38:41.971`
- log child id response: `23:38:42.058`
- parent ipv6: `fe80:0:0:0:7ca5:b9e6:57ea:89e9`
- parent extaddr: `7ea5b9e657ea89e9`
- parent rloc16: `0xf400`
- child extaddr: `d6e722f2a32d4a1a`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **324 ms**
- Response -> Child ID Request: **424 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **810 ms**
- pcap parent request: `23:38:41.245` (frame 73)
- pcap parent response: `23:38:41.569` (frame 74)
- pcap child id request: `23:38:41.993` (frame 78)
- pcap child id response: `23:38:42.055` (frame 80)

#### PCAP-complete child attach 2

- log parent request: `23:38:45.155`
- log parent response: `23:38:45.260`
- log child id request: `23:38:45.313`
- log child id response: `23:38:45.415`
- parent ipv6: `fe80:0:0:0:bc66:d6d9:8db7:da67`
- parent extaddr: `be66d6d98db7da67`
- parent rloc16: `0x2800`
- child extaddr: `d6e722f2a32d4a1a`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **40 ms**
- Response -> Child ID Request: **103 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **206 ms**
- pcap parent request: `23:38:45.202` (frame 84)
- pcap parent response: `23:38:45.242` (frame 86)
- pcap child id request: `23:38:45.345` (frame 88)
- pcap child id response: `23:38:45.408` (frame 90)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260629-234447-run34.log`

- manifest status: `completed`
- child extaddr: `aa96066d607afc78`
- switch target extaddr(s): `5ee515ebc23e8d6a, 5ee515ebc23e8d6a, 5ee515ebc23e8d6a`

#### PCAP-complete child attach 1

- log parent request: `23:50:28.068`
- log parent response: `23:50:28.270`
- log child id request: `23:50:28.842`
- log child id response: `23:50:28.931`
- parent ipv6: `fe80:0:0:0:b484:7685:4f19:60b4`
- parent extaddr: `b68476854f1960b4`
- parent rloc16: `0x6c00`
- child extaddr: `aa96066d607afc78`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **142 ms**
- Response -> Child ID Request: **607 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **812 ms**
- pcap parent request: `23:50:28.116` (frame 78)
- pcap parent response: `23:50:28.258` (frame 79)
- pcap child id request: `23:50:28.865` (frame 84)
- pcap child id response: `23:50:28.928` (frame 86)

#### PCAP-complete child attach 2

- log parent request: `23:50:32.705`
- log parent response: `23:50:32.811`
- log child id request: `23:50:32.871`
- log child id response: `23:50:32.966`
- parent ipv6: `fe80:0:0:0:5ce5:15eb:c23e:8d6a`
- parent extaddr: `5ee515ebc23e8d6a`
- parent rloc16: `0x2400`
- child extaddr: `aa96066d607afc78`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **41 ms**
- Response -> Child ID Request: **105 ms**
- Child ID Request -> Response: **66 ms**
- Full Attach: **212 ms**
- pcap parent request: `23:50:32.752` (frame 88)
- pcap parent response: `23:50:32.793` (frame 90)
- pcap child id request: `23:50:32.898` (frame 92)
- pcap child id response: `23:50:32.964` (frame 94)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260629-235635-run35.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `72f5f0ae2c7d09ed`
- switch target extaddr(s): `9a4b268ac9c64a06, 9a4b268ac9c64a06, 9a4b268ac9c64a06`

#### PCAP-complete child attach 1

- log parent request: `00:02:16.080`
- log parent response: `00:02:16.582`
- log child id request: `00:02:16.791`
- log child id response: `00:02:16.880`
- parent ipv6: `fe80:0:0:0:3428:178c:5cf7:b6f5`
- parent extaddr: `3628178c5cf7b6f5`
- parent rloc16: `0x8400`
- child extaddr: `72f5f0ae2c7d09ed`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **504 ms**
- Response -> Child ID Request: **246 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **812 ms**
- pcap parent request: `00:02:16.065` (frame 72)
- pcap parent response: `00:02:16.569` (frame 74)
- pcap child id request: `00:02:16.815` (frame 78)
- pcap child id response: `00:02:16.877` (frame 80)

#### PCAP-complete child attach 2

- log parent request: `00:02:20.190`
- log parent response: `00:02:20.297`
- log child id request: `00:02:20.354`
- log child id response: `00:02:20.449`
- parent ipv6: `fe80:0:0:0:984b:268a:c9c6:4a06`
- parent extaddr: `9a4b268ac9c64a06`
- parent rloc16: `0x0000`
- child extaddr: `72f5f0ae2c7d09ed`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **39 ms**
- Response -> Child ID Request: **105 ms**
- Child ID Request -> Response: **61 ms**
- Full Attach: **205 ms**
- pcap parent request: `00:02:20.238` (frame 82)
- pcap parent response: `00:02:20.277` (frame 84)
- pcap child id request: `00:02:20.382` (frame 86)
- pcap child id response: `00:02:20.443` (frame 88)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260630-000822-run36.log`

- manifest status: `completed`
- child extaddr: `5e9ef1e5ac5fb4cc`
- switch target extaddr(s): `820f7e772a072f82, 820f7e772a072f82, 820f7e772a072f82`

#### PCAP-complete child attach 1

- log parent request: `00:14:03.089`
- log parent response: `00:14:03.145`
- log child id request: `00:14:03.801`
- log child id response: `00:14:03.890`
- parent ipv6: `fe80:0:0:0:7c4b:5e8a:92ec:3116`
- parent extaddr: `7e4b5e8a92ec3116`
- parent rloc16: `0xb000`
- child extaddr: `5e9ef1e5ac5fb4cc`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **58 ms**
- Response -> Child ID Request: **692 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **813 ms**
- pcap parent request: `00:14:03.075` (frame 72)
- pcap parent response: `00:14:03.133` (frame 73)
- pcap child id request: `00:14:03.825` (frame 77)
- pcap child id response: `00:14:03.888` (frame 79)

#### PCAP-complete child attach 2

- log parent request: `00:14:07.626`
- log parent response: `00:14:07.730`
- log child id request: `00:14:07.787`
- log child id response: `00:14:07.881`
- parent ipv6: `fe80:0:0:0:800f:7e77:2a07:2f82`
- parent extaddr: `820f7e772a072f82`
- parent rloc16: `0x2000`
- child extaddr: `5e9ef1e5ac5fb4cc`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **43 ms**
- Response -> Child ID Request: **98 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **205 ms**
- pcap parent request: `00:14:07.673` (frame 81)
- pcap parent response: `00:14:07.716` (frame 83)
- pcap child id request: `00:14:07.814` (frame 85)
- pcap child id response: `00:14:07.878` (frame 87)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260630-002009-run37.log`

- manifest status: `completed`
- child extaddr: `468b2bd7bea14c67`
- switch target extaddr(s): `ee68e71e212345d3, ee68e71e212345d3, ee68e71e212345d3`

#### PCAP-complete child attach 1

- log parent request: `00:25:50.425`
- log parent response: `00:25:50.699`
- log child id request: `00:25:51.196`
- log child id response: `00:25:51.288`
- parent ipv6: `fe80:0:0:0:7805:fe80:cc62:ee92`
- parent extaddr: `7a05fe80cc62ee92`
- parent rloc16: `0xb400`
- child extaddr: `468b2bd7bea14c67`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **212 ms**
- Response -> Child ID Request: **533 ms**
- Child ID Request -> Response: **66 ms**
- Full Attach: **811 ms**
- pcap parent request: `00:25:50.475` (frame 75)
- pcap parent response: `00:25:50.687` (frame 76)
- pcap child id request: `00:25:51.220` (frame 80)
- pcap child id response: `00:25:51.286` (frame 82)

#### PCAP-complete child attach 2

- log parent request: `00:25:55.149`
- log parent response: `00:25:55.255`
- log child id request: `00:25:55.311`
- log child id response: `00:25:55.412`
- parent ipv6: `fe80:0:0:0:ec68:e71e:2123:45d3`
- parent extaddr: `ee68e71e212345d3`
- parent rloc16: `0x9800`
- child extaddr: `468b2bd7bea14c67`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **40 ms**
- Response -> Child ID Request: **106 ms**
- Child ID Request -> Response: **67 ms**
- Full Attach: **213 ms**
- pcap parent request: `00:25:55.197` (frame 86)
- pcap parent response: `00:25:55.237` (frame 88)
- pcap child id request: `00:25:55.343` (frame 90)
- pcap child id response: `00:25:55.410` (frame 92)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260630-003157-run38.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `363cd187ad2cbbcc`
- switch target extaddr(s): `f20ebcb4c7510481, f20ebcb4c7510481, f20ebcb4c7510481`

#### PCAP-complete child attach 1

- log parent request: `00:37:37.950`
- log parent response: `00:37:38.286`
- log child id request: `00:37:38.722`
- log child id response: `00:37:38.812`
- parent ipv6: `fe80:0:0:0:c7c:dfd:655:4313`
- parent extaddr: `0e7c0dfd06554313`
- parent rloc16: `0x9800`
- child extaddr: `363cd187ad2cbbcc`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **278 ms**
- Response -> Child ID Request: **471 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **813 ms**
- pcap parent request: `00:37:37.997` (frame 77)
- pcap parent response: `00:37:38.275` (frame 78)
- pcap child id request: `00:37:38.746` (frame 82)
- pcap child id response: `00:37:38.810` (frame 84)

#### PCAP-complete child attach 2

- log parent request: `00:37:42.636`
- log parent response: `00:37:42.742`
- log child id request: `00:37:42.799`
- log child id response: `00:37:42.893`
- parent ipv6: `fe80:0:0:0:f00e:bcb4:c751:481`
- parent extaddr: `f20ebcb4c7510481`
- parent rloc16: `0x0400`
- child extaddr: `363cd187ad2cbbcc`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **39 ms**
- Response -> Child ID Request: **104 ms**
- Child ID Request -> Response: **61 ms**
- Full Attach: **204 ms**
- pcap parent request: `00:37:42.685` (frame 86)
- pcap parent response: `00:37:42.724` (frame 88)
- pcap child id request: `00:37:42.828` (frame 90)
- pcap child id response: `00:37:42.889` (frame 92)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260630-004344-run39.log`

- manifest status: `completed`
- child extaddr: `be26ca4c61139e92`
- switch target extaddr(s): `fe9a928d6f609d5d, fe9a928d6f609d5d, fe9a928d6f609d5d`

#### PCAP-complete child attach 1

- log parent request: `00:49:25.720`
- log parent response: `00:49:25.823`
- log child id request: `00:49:26.491`
- log child id response: `00:49:26.579`
- parent ipv6: `fe80:0:0:0:c804:c6e3:a286:272b`
- parent extaddr: `ca04c6e3a286272b`
- parent rloc16: `0x2800`
- child extaddr: `be26ca4c61139e92`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **46 ms**
- Response -> Child ID Request: **704 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **813 ms**
- pcap parent request: `00:49:25.764` (frame 80)
- pcap parent response: `00:49:25.810` (frame 81)
- pcap child id request: `00:49:26.514` (frame 85)
- pcap child id response: `00:49:26.577` (frame 87)

#### PCAP-complete child attach 2

- log parent request: `00:49:30.020`
- log parent response: `00:49:30.126`
- log child id request: `00:49:30.182`
- log child id response: `00:49:30.281`
- parent ipv6: `fe80:0:0:0:fc9a:928d:6f60:9d5d`
- parent extaddr: `fe9a928d6f609d5d`
- parent rloc16: `0x7000`
- child extaddr: `be26ca4c61139e92`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **41 ms**
- Response -> Child ID Request: **105 ms**
- Child ID Request -> Response: **65 ms**
- Full Attach: **211 ms**
- pcap parent request: `00:49:30.068` (frame 90)
- pcap parent response: `00:49:30.109` (frame 92)
- pcap child id request: `00:49:30.214` (frame 94)
- pcap child id response: `00:49:30.279` (frame 96)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260630-005532-run40.log`

- manifest status: `completed`
- child extaddr: `9e0ce2b33f581db1`
- switch target extaddr(s): `72f890f7eb291dfa, 72f890f7eb291dfa, 72f890f7eb291dfa`

#### PCAP-complete child attach 1

- log parent request: `01:01:13.143`
- log parent response: `01:01:13.551`
- log child id request: `01:01:13.855`
- log child id response: `01:01:13.943`
- parent ipv6: `fe80:0:0:0:6cf1:4dff:8bd5:9671`
- parent extaddr: `6ef14dff8bd59671`
- parent rloc16: `0x8400`
- child extaddr: `9e0ce2b33f581db1`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **410 ms**
- Response -> Child ID Request: **340 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **812 ms**
- pcap parent request: `01:01:13.128` (frame 75)
- pcap parent response: `01:01:13.538` (frame 77)
- pcap child id request: `01:01:13.878` (frame 81)
- pcap child id response: `01:01:13.940` (frame 83)

#### PCAP-complete child attach 2

- log parent request: `01:01:17.483`
- log parent response: `01:01:17.588`
- log child id request: `01:01:17.648`
- log child id response: `01:01:17.742`
- parent ipv6: `fe80:0:0:0:70f8:90f7:eb29:1dfa`
- parent extaddr: `72f890f7eb291dfa`
- parent rloc16: `0x0c00`
- child extaddr: `9e0ce2b33f581db1`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **41 ms**
- Response -> Child ID Request: **103 ms**
- Child ID Request -> Response: **66 ms**
- Full Attach: **210 ms**
- pcap parent request: `01:01:17.530` (frame 85)
- pcap parent response: `01:01:17.571` (frame 87)
- pcap child id request: `01:01:17.674` (frame 89)
- pcap child id response: `01:01:17.740` (frame 91)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260630-010719-run41.log`

- manifest status: `completed`
- child extaddr: `b21730a08e9b8bee`
- switch target extaddr(s): `a68eaa7ac34aa141, a68eaa7ac34aa141, a68eaa7ac34aa141`

#### PCAP-complete child attach 1

- log parent request: `01:13:00.849`
- log parent response: `01:13:01.090`
- log child id request: `01:13:01.560`
- log child id response: `01:13:01.648`
- parent ipv6: `fe80:0:0:0:5c18:e8f:aaa7:71b3`
- parent extaddr: `5e180e8faaa771b3`
- parent rloc16: `0x6800`
- child extaddr: `b21730a08e9b8bee`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **244 ms**
- Response -> Child ID Request: **506 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **812 ms**
- pcap parent request: `01:13:00.833` (frame 80)
- pcap parent response: `01:13:01.077` (frame 81)
- pcap child id request: `01:13:01.583` (frame 85)
- pcap child id response: `01:13:01.645` (frame 87)

#### PCAP-complete child attach 2

- log parent request: `01:13:04.943`
- log parent response: `01:13:05.048`
- log child id request: `01:13:05.109`
- log child id response: `01:13:05.203`
- parent ipv6: `fe80:0:0:0:a48e:aa7a:c34a:a141`
- parent extaddr: `a68eaa7ac34aa141`
- parent rloc16: `0x3800`
- child extaddr: `b21730a08e9b8bee`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **40 ms**
- Response -> Child ID Request: **107 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **210 ms**
- pcap parent request: `01:13:04.989` (frame 89)
- pcap parent response: `01:13:05.029` (frame 91)
- pcap child id request: `01:13:05.136` (frame 93)
- pcap child id response: `01:13:05.199` (frame 95)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260630-011907-run42.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `f67161d9f10ce3a3`
- switch target extaddr(s): `0a73bd3772f4f01c, 0a73bd3772f4f01c, 0a73bd3772f4f01c`

#### PCAP-complete child attach 1

- log parent request: `01:24:48.091`
- log parent response: `01:24:48.501`
- log child id request: `01:24:48.861`
- log child id response: `01:24:48.953`
- parent ipv6: `fe80:0:0:0:5883:dd12:a5d5:f036`
- parent extaddr: `5a83dd12a5d5f036`
- parent rloc16: `0xf400`
- child extaddr: `f67161d9f10ce3a3`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **353 ms**
- Response -> Child ID Request: **399 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **816 ms**
- pcap parent request: `01:24:48.133` (frame 79)
- pcap parent response: `01:24:48.486` (frame 80)
- pcap child id request: `01:24:48.885` (frame 84)
- pcap child id response: `01:24:48.949` (frame 86)

#### PCAP-complete child attach 2

- log parent request: `01:24:52.435`
- log parent response: `01:24:52.539`
- log child id request: `01:24:52.599`
- log child id response: `01:24:52.693`
- parent ipv6: `fe80:0:0:0:873:bd37:72f4:f01c`
- parent extaddr: `0a73bd3772f4f01c`
- parent rloc16: `0xd400`
- child extaddr: `f67161d9f10ce3a3`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **41 ms**
- Response -> Child ID Request: **104 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **208 ms**
- pcap parent request: `01:24:52.478` (frame 90)
- pcap parent response: `01:24:52.519` (frame 92)
- pcap child id request: `01:24:52.623` (frame 94)
- pcap child id response: `01:24:52.686` (frame 96)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260630-013054-run43.log`

- manifest status: `completed`
- child extaddr: `a20f8c08d311f73f`
- switch target extaddr(s): `f292da4c31f71f34, f292da4c31f71f34, f292da4c31f71f34`

#### PCAP-complete child attach 1

- log parent request: `01:36:36.004`
- log parent response: `01:36:36.105`
- log child id request: `01:36:36.714`
- log child id response: `01:36:36.806`
- parent ipv6: `fe80:0:0:0:2018:6219:915:193e`
- parent extaddr: `221862190915193e`
- parent rloc16: `0xdc00`
- child extaddr: `a20f8c08d311f73f`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **105 ms**
- Response -> Child ID Request: **645 ms**
- Child ID Request -> Response: **66 ms**
- Full Attach: **816 ms**
- pcap parent request: `01:36:35.985` (frame 78)
- pcap parent response: `01:36:36.090` (frame 79)
- pcap child id request: `01:36:36.735` (frame 83)
- pcap child id response: `01:36:36.801` (frame 85)

#### PCAP-complete child attach 2

- log parent request: `01:36:40.041`
- log parent response: `01:36:40.188`
- log child id request: `01:36:40.243`
- log child id response: `01:36:40.340`
- parent ipv6: `fe80:0:0:0:f092:da4c:31f7:1f34`
- parent extaddr: `f292da4c31f71f34`
- parent rloc16: `0x2400`
- child extaddr: `a20f8c08d311f73f`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **40 ms**
- Response -> Child ID Request: **108 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **211 ms**
- pcap parent request: `01:36:40.124` (frame 88)
- pcap parent response: `01:36:40.164` (frame 90)
- pcap child id request: `01:36:40.272` (frame 92)
- pcap child id response: `01:36:40.335` (frame 94)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260630-014242-run44.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `823195092069c52b`
- switch target extaddr(s): `8eccf14d5eb02b5f, 8eccf14d5eb02b5f, 8eccf14d5eb02b5f`

#### PCAP-complete child attach 1

- log parent request: `01:48:23.133`
- log parent response: `01:48:23.582`
- log child id request: `01:48:23.846`
- log child id response: `01:48:23.934`
- parent ipv6: `fe80:0:0:0:c871:1967:d018:ec09`
- parent extaddr: `ca711967d018ec09`
- parent rloc16: `0x2000`
- child extaddr: `823195092069c52b`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **451 ms**
- Response -> Child ID Request: **299 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **813 ms**
- pcap parent request: `01:48:23.116` (frame 79)
- pcap parent response: `01:48:23.567` (frame 80)
- pcap child id request: `01:48:23.866` (frame 84)
- pcap child id response: `01:48:23.929` (frame 86)

#### PCAP-complete child attach 2

- log parent request: `01:48:27.590`
- log parent response: `01:48:27.698`
- log child id request: `01:48:27.754`
- log child id response: `01:48:27.849`
- parent ipv6: `fe80:0:0:0:8ccc:f14d:5eb0:2b5f`
- parent extaddr: `8eccf14d5eb02b5f`
- parent rloc16: `0x1800`
- child extaddr: `823195092069c52b`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **40 ms**
- Response -> Child ID Request: **103 ms**
- Child ID Request -> Response: **61 ms**
- Full Attach: **204 ms**
- pcap parent request: `01:48:27.635` (frame 89)
- pcap parent response: `01:48:27.675` (frame 91)
- pcap child id request: `01:48:27.778` (frame 93)
- pcap child id response: `01:48:27.839` (frame 95)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260630-015429-run45.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `e25118f8971fca5e`
- switch target extaddr(s): `a291a2d7f5706e22, a291a2d7f5706e22, a291a2d7f5706e22`

#### PCAP-complete child attach 1

- log parent request: `02:00:10.855`
- log parent response: `02:00:11.045`
- log child id request: `02:00:11.628`
- log child id response: `02:00:11.716`
- parent ipv6: `fe80:0:0:0:3ccf:208f:7dda:fdc`
- parent extaddr: `3ecf208f7dda0fdc`
- parent rloc16: `0x7800`
- child extaddr: `e25118f8971fca5e`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **130 ms**
- Response -> Child ID Request: **619 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **812 ms**
- pcap parent request: `02:00:10.900` (frame 72)
- pcap parent response: `02:00:11.030` (frame 73)
- pcap child id request: `02:00:11.649` (frame 77)
- pcap child id response: `02:00:11.712` (frame 79)

#### PCAP-complete child attach 2

- log parent request: `02:00:15.163`
- log parent response: `02:00:15.268`
- log child id request: `02:00:15.326`
- log child id response: `02:00:15.420`
- parent ipv6: `fe80:0:0:0:a091:a2d7:f570:6e22`
- parent extaddr: `a291a2d7f5706e22`
- parent rloc16: `0xac00`
- child extaddr: `e25118f8971fca5e`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **39 ms**
- Response -> Child ID Request: **104 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **205 ms**
- pcap parent request: `02:00:15.208` (frame 82)
- pcap parent response: `02:00:15.247` (frame 84)
- pcap child id request: `02:00:15.351` (frame 86)
- pcap child id response: `02:00:15.413` (frame 88)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260630-020617-run46.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `e6e6059817f7f208`
- switch target extaddr(s): `423788e3171a18a9, 423788e3171a18a9, 423788e3171a18a9`

#### PCAP-complete child attach 1

- log parent request: `02:11:58.399`
- log parent response: `02:11:58.579`
- log child id request: `02:11:59.110`
- log child id response: `02:11:59.204`
- parent ipv6: `fe80:0:0:0:c49c:4f89:4d1d:46b7`
- parent extaddr: `c69c4f894d1d46b7`
- parent rloc16: `0xd800`
- child extaddr: `e6e6059817f7f208`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **181 ms**
- Response -> Child ID Request: **568 ms**
- Child ID Request -> Response: **65 ms**
- Full Attach: **814 ms**
- pcap parent request: `02:11:58.381` (frame 79)
- pcap parent response: `02:11:58.562` (frame 80)
- pcap child id request: `02:11:59.130` (frame 84)
- pcap child id response: `02:11:59.195` (frame 86)

#### PCAP-complete child attach 2

- log parent request: `02:12:02.532`
- log parent response: `02:12:02.638`
- log child id request: `02:12:02.691`
- log child id response: `02:12:02.789`
- parent ipv6: `fe80:0:0:0:4037:88e3:171a:18a9`
- parent extaddr: `423788e3171a18a9`
- parent rloc16: `0x0c00`
- child extaddr: `e6e6059817f7f208`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **43 ms**
- Response -> Child ID Request: **99 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **205 ms**
- pcap parent request: `02:12:02.578` (frame 90)
- pcap parent response: `02:12:02.621` (frame 92)
- pcap child id request: `02:12:02.720` (frame 94)
- pcap child id response: `02:12:02.783` (frame 96)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260630-021804-run47.log`

- manifest status: `completed`
- child extaddr: `9244e4c0b47afc23`
- switch target extaddr(s): `bed9afa10f8ac208, bed9afa10f8ac208, bed9afa10f8ac208`

#### PCAP-complete child attach 1

- log parent request: `02:23:45.543`
- log parent response: `02:23:45.668`
- log child id request: `02:23:46.252`
- log child id response: `02:23:46.339`
- parent ipv6: `fe80:0:0:0:887c:7ccd:3ba2:7a31`
- parent extaddr: `8a7c7ccd3ba27a31`
- parent rloc16: `0x5400`
- child extaddr: `9244e4c0b47afc23`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **131 ms**
- Response -> Child ID Request: **619 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **812 ms**
- pcap parent request: `02:23:45.523` (frame 77)
- pcap parent response: `02:23:45.654` (frame 78)
- pcap child id request: `02:23:46.273` (frame 82)
- pcap child id response: `02:23:46.335` (frame 84)

#### PCAP-complete child attach 2

- log parent request: `02:23:49.900`
- log parent response: `02:23:50.046`
- log child id request: `02:23:50.104`
- log child id response: `02:23:50.199`
- parent ipv6: `fe80:0:0:0:bcd9:afa1:f8a:c208`
- parent extaddr: `bed9afa10f8ac208`
- parent rloc16: `0xd800`
- child extaddr: `9244e4c0b47afc23`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **41 ms**
- Response -> Child ID Request: **106 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **211 ms**
- pcap parent request: `02:23:49.983` (frame 88)
- pcap parent response: `02:23:50.024` (frame 90)
- pcap child id request: `02:23:50.130` (frame 92)
- pcap child id response: `02:23:50.194` (frame 94)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260630-022952-run48.log`

- manifest status: `completed`
- child extaddr: `4e84db2788772dbc`
- switch target extaddr(s): `f275cffcb22c95e3, f275cffcb22c95e3, f275cffcb22c95e3`

#### PCAP-complete child attach 1

- log parent request: `02:35:32.829`
- log parent response: `02:35:32.971`
- log child id request: `02:35:33.534`
- log child id response: `02:35:33.625`
- parent ipv6: `fe80:0:0:0:2ce6:c900:66d2:40f2`
- parent extaddr: `2ee6c90066d240f2`
- parent rloc16: `0x0400`
- child extaddr: `4e84db2788772dbc`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **148 ms**
- Response -> Child ID Request: **602 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **812 ms**
- pcap parent request: `02:35:32.812` (frame 78)
- pcap parent response: `02:35:32.960` (frame 79)
- pcap child id request: `02:35:33.562` (frame 83)
- pcap child id response: `02:35:33.624` (frame 85)

#### PCAP-complete child attach 2

- log parent request: `02:35:37.422`
- log parent response: `02:35:37.526`
- log child id request: `02:35:37.586`
- log child id response: `02:35:37.681`
- parent ipv6: `fe80:0:0:0:f075:cffc:b22c:95e3`
- parent extaddr: `f275cffcb22c95e3`
- parent rloc16: `0xa800`
- child extaddr: `4e84db2788772dbc`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **40 ms**
- Response -> Child ID Request: **106 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **209 ms**
- pcap parent request: `02:35:37.469` (frame 89)
- pcap parent response: `02:35:37.509` (frame 91)
- pcap child id request: `02:35:37.615` (frame 93)
- pcap child id response: `02:35:37.678` (frame 95)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260630-024139-run49.log`

- manifest status: `completed`
- child extaddr: `7a0acbf9c1fcfcab`
- switch target extaddr(s): `c2893d2e60b13459, c2893d2e60b13459, c2893d2e60b13459`

#### PCAP-complete child attach 1

- log parent request: `02:47:20.820`
- log parent response: `02:47:21.041`
- log child id request: `02:47:21.529`
- log child id response: `02:47:21.617`
- parent ipv6: `fe80:0:0:0:7cb2:3bf3:bd6b:85be`
- parent extaddr: `7eb23bf3bd6b85be`
- parent rloc16: `0x0800`
- child extaddr: `7a0acbf9c1fcfcab`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **222 ms**
- Response -> Child ID Request: **525 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **809 ms**
- pcap parent request: `02:47:20.808` (frame 76)
- pcap parent response: `02:47:21.030` (frame 77)
- pcap child id request: `02:47:21.555` (frame 81)
- pcap child id response: `02:47:21.617` (frame 83)

#### PCAP-complete child attach 2

- log parent request: `02:47:24.896`
- log parent response: `02:47:25.003`
- log child id request: `02:47:25.060`
- log child id response: `02:47:25.151`
- parent ipv6: `fe80:0:0:0:c089:3d2e:60b1:3459`
- parent extaddr: `c2893d2e60b13459`
- parent rloc16: `0x5400`
- child extaddr: `7a0acbf9c1fcfcab`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **41 ms**
- Response -> Child ID Request: **101 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **205 ms**
- pcap parent request: `02:47:24.947` (frame 85)
- pcap parent response: `02:47:24.988` (frame 87)
- pcap child id request: `02:47:25.089` (frame 89)
- pcap child id response: `02:47:25.152` (frame 91)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260630-025327-run50.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `961cef05baea5c5a`
- switch target extaddr(s): `f216f883337a9a86, f216f883337a9a86, f216f883337a9a86`

#### PCAP-complete child attach 1

- log parent request: `02:59:08.173`
- log parent response: `02:59:08.710`
- log child id request: `02:59:08.944`
- log child id response: `02:59:09.036`
- parent ipv6: `fe80:0:0:0:647a:24d9:713c:177a`
- parent extaddr: `667a24d9713c177a`
- parent rloc16: `0xa000`
- child extaddr: `961cef05baea5c5a`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **480 ms**
- Response -> Child ID Request: **272 ms**
- Child ID Request -> Response: **65 ms**
- Full Attach: **817 ms**
- pcap parent request: `02:59:08.219` (frame 81)
- pcap parent response: `02:59:08.699` (frame 82)
- pcap child id request: `02:59:08.971` (frame 86)
- pcap child id response: `02:59:09.036` (frame 88)

#### PCAP-complete child attach 2

- log parent request: `02:59:12.356`
- log parent response: `02:59:12.465`
- log child id request: `02:59:12.521`
- log child id response: `02:59:12.616`
- parent ipv6: `fe80:0:0:0:f016:f883:337a:9a86`
- parent extaddr: `f216f883337a9a86`
- parent rloc16: `0xe400`
- child extaddr: `961cef05baea5c5a`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **40 ms**
- Response -> Child ID Request: **103 ms**
- Child ID Request -> Response: **61 ms**
- Full Attach: **204 ms**
- pcap parent request: `02:59:12.407` (frame 90)
- pcap parent response: `02:59:12.447` (frame 92)
- pcap child id request: `02:59:12.550` (frame 94)
- pcap child id response: `02:59:12.611` (frame 96)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**
