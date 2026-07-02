# Child Log Analysis

## ucast_fastpr_child

Files analyzed: **5**

- batch folders: `ucast_fastpr-2router-5runs-20260702-071037`

### PCAP-complete child attach summary

| Attach | Metric | M (SD), ms | n |
| --- | --- | ---: | ---: |
| 1 | Request -> Response | 250.40 (163.57) | 5 |
| 1 | Response -> Child ID Request | 500.60 (163.90) | 5 |
| 1 | Child ID Request -> Response | 64.60 (2.30) | 5 |
| 1 | Full Attach | 815.60 (2.51) | 5 |
| 2 | Request -> Response | 40.80 (0.84) | 5 |
| 2 | Response -> Child ID Request | 115.40 (2.41) | 5 |
| 2 | Child ID Request -> Response | 63.60 (2.30) | 5 |
| 2 | Full Attach | 219.80 (2.77) | 5 |

| Metric | M (SD) | n |
| --- | ---: | ---: |
| Failed TX Attempts per Log | 0.00 (0.00) | 5 |
| Log-only or Partial Sequences per Log | 0.00 (0.00) | 5 |

### `ucast_fastpr_child_20260702-071102-run01.log`

- manifest status: `completed`
- child extaddr: `e65f391d267b7aac`
- switch target extaddr(s): `eefb8632d1304538, eefb8632d1304538, eefb8632d1304538`

#### PCAP-complete child attach 1

- log parent request: `07:16:44.183`
- log parent response: `07:16:44.397`
- log child id request: `07:16:44.957`
- log child id response: `07:16:45.046`
- parent ipv6: `fe80:0:0:0:48ce:d3c0:90a4:51a0`
- parent extaddr: `4aced3c090a451a0`
- parent rloc16: `0x9c00`
- child extaddr: `e65f391d267b7aac`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **153 ms**
- Response -> Child ID Request: **598 ms**
- Child ID Request -> Response: **61 ms**
- Full Attach: **812 ms**
- pcap parent request: `07:16:44.228` (frame 79)
- pcap parent response: `07:16:44.381` (frame 80)
- pcap child id request: `07:16:44.979` (frame 84)
- pcap child id response: `07:16:45.040` (frame 86)

#### PCAP-complete child attach 2

- log parent request: `07:16:48.677`
- log parent response: `07:16:48.766`
- log child id request: `07:16:48.829`
- log child id response: `07:16:48.929`
- parent ipv6: `fe80:0:0:0:ecfb:8632:d130:4538`
- parent extaddr: `eefb8632d1304538`
- parent rloc16: `0x5c00`
- child extaddr: `e65f391d267b7aac`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **40 ms**
- Response -> Child ID Request: **112 ms**
- Child ID Request -> Response: **65 ms**
- Full Attach: **217 ms**
- pcap parent request: `07:16:48.701` (frame 88)
- pcap parent response: `07:16:48.741` (frame 90)
- pcap child id request: `07:16:48.853` (frame 92)
- pcap child id response: `07:16:48.918` (frame 94)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260702-072251-run02.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `7e9ed6c86e403bc6`
- switch target extaddr(s): `26cccd4e98fe4863, 26cccd4e98fe4863, 26cccd4e98fe4863`

#### PCAP-complete child attach 1

- log parent request: `07:28:32.224`
- log parent response: `07:28:32.551`
- log child id request: `07:28:32.998`
- log child id response: `07:28:33.089`
- parent ipv6: `fe80:0:0:0:e6:e9c6:8bea:6063`
- parent extaddr: `02e6e9c68bea6063`
- parent rloc16: `0x2000`
- child extaddr: `7e9ed6c86e403bc6`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **266 ms**
- Response -> Child ID Request: **485 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **815 ms**
- pcap parent request: `07:28:32.270` (frame 80)
- pcap parent response: `07:28:32.536` (frame 81)
- pcap child id request: `07:28:33.021` (frame 85)
- pcap child id response: `07:28:33.085` (frame 87)

#### PCAP-complete child attach 2

- log parent request: `07:28:36.416`
- log parent response: `07:28:36.506`
- log child id request: `07:28:36.572`
- log child id response: `07:28:36.674`
- parent ipv6: `fe80:0:0:0:24cc:cd4e:98fe:4863`
- parent extaddr: `26cccd4e98fe4863`
- parent rloc16: `0x3000`
- child extaddr: `7e9ed6c86e403bc6`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **40 ms**
- Response -> Child ID Request: **117 ms**
- Child ID Request -> Response: **67 ms**
- Full Attach: **224 ms**
- pcap parent request: `07:28:36.442` (frame 90)
- pcap parent response: `07:28:36.482` (frame 92)
- pcap child id request: `07:28:36.599` (frame 94)
- pcap child id response: `07:28:36.666` (frame 96)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260702-073438-run03.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `56836f62d15dca45`
- switch target extaddr(s): `6a1ab1e95554f88b, 6a1ab1e95554f88b, 6a1ab1e95554f88b`

#### PCAP-complete child attach 1

- log parent request: `07:40:19.681`
- log parent response: `07:40:19.951`
- log child id request: `07:40:20.508`
- log child id response: `07:40:20.547`
- parent ipv6: `fe80:0:0:0:1819:e61a:642a:9c03`
- parent extaddr: `1a19e61a642a9c03`
- parent rloc16: `0x7000`
- child extaddr: `56836f62d15dca45`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **208 ms**
- Response -> Child ID Request: **541 ms**
- Child ID Request -> Response: **66 ms**
- Full Attach: **815 ms**
- pcap parent request: `07:40:19.730` (frame 77)
- pcap parent response: `07:40:19.938` (frame 78)
- pcap child id request: `07:40:20.479` (frame 82)
- pcap child id response: `07:40:20.545` (frame 84)

#### PCAP-complete child attach 2

- log parent request: `07:40:23.829`
- log parent response: `07:40:23.919`
- log child id request: `07:40:23.986`
- log child id response: `07:40:24.087`
- parent ipv6: `fe80:0:0:0:681a:b1e9:5554:f88b`
- parent extaddr: `6a1ab1e95554f88b`
- parent rloc16: `0x6000`
- child extaddr: `56836f62d15dca45`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **41 ms**
- Response -> Child ID Request: **118 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **221 ms**
- pcap parent request: `07:40:23.855` (frame 87)
- pcap parent response: `07:40:23.896` (frame 89)
- pcap child id request: `07:40:24.014` (frame 91)
- pcap child id response: `07:40:24.076` (frame 93)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260702-074626-run04.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `6e49d55bc201a1d9`
- switch target extaddr(s): `5edca43e0914e776, 5edca43e0914e776, 5edca43e0914e776`

#### PCAP-complete child attach 1

- log parent request: `07:52:07.050`
- log parent response: `07:52:07.217`
- log child id request: `07:52:07.829`
- log child id response: `07:52:07.919`
- parent ipv6: `fe80:0:0:0:502b:98a7:17:2ce9`
- parent extaddr: `522b98a700172ce9`
- parent rloc16: `0x6c00`
- child extaddr: `6e49d55bc201a1d9`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **103 ms**
- Response -> Child ID Request: **650 ms**
- Child ID Request -> Response: **65 ms**
- Full Attach: **818 ms**
- pcap parent request: `07:52:07.099` (frame 79)
- pcap parent response: `07:52:07.202` (frame 80)
- pcap child id request: `07:52:07.852` (frame 84)
- pcap child id response: `07:52:07.917` (frame 86)

#### PCAP-complete child attach 2

- log parent request: `07:52:11.166`
- log parent response: `07:52:11.257`
- log child id request: `07:52:11.318`
- log child id response: `07:52:11.423`
- parent ipv6: `fe80:0:0:0:5cdc:a43e:914:e776`
- parent extaddr: `5edca43e0914e776`
- parent rloc16: `0xb400`
- child extaddr: `6e49d55bc201a1d9`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **41 ms**
- Response -> Child ID Request: **116 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **219 ms**
- pcap parent request: `07:52:11.194` (frame 89)
- pcap parent response: `07:52:11.235` (frame 91)
- pcap child id request: `07:52:11.351` (frame 93)
- pcap child id response: `07:52:11.413` (frame 95)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `ucast_fastpr_child_20260702-075813-run05.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `925d093fef3e3975`
- switch target extaddr(s): `0a56a56da33eef7a, 0a56a56da33eef7a, 0a56a56da33eef7a`

#### PCAP-complete child attach 1

- log parent request: `08:03:54.646`
- log parent response: `08:03:55.229`
- log child id request: `08:03:55.421`
- log child id response: `08:03:55.515`
- parent ipv6: `fe80:0:0:0:206b:8875:4e23:52ce`
- parent extaddr: `226b88754e2352ce`
- parent rloc16: `0x8800`
- child extaddr: `925d093fef3e3975`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **522 ms**
- Response -> Child ID Request: **229 ms**
- Child ID Request -> Response: **67 ms**
- Full Attach: **818 ms**
- pcap parent request: `08:03:54.691` (frame 76)
- pcap parent response: `08:03:55.213` (frame 77)
- pcap child id request: `08:03:55.442` (frame 81)
- pcap child id response: `08:03:55.509` (frame 83)

#### PCAP-complete child attach 2

- log parent request: `08:03:58.615`
- log parent response: `08:03:58.705`
- log child id request: `08:03:58.770`
- log child id response: `08:03:58.870`
- parent ipv6: `fe80:0:0:0:856:a56d:a33e:ef7a`
- parent extaddr: `0a56a56da33eef7a`
- parent rloc16: `0xec00`
- child extaddr: `925d093fef3e3975`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **42 ms**
- Response -> Child ID Request: **114 ms**
- Child ID Request -> Response: **62 ms**
- Full Attach: **218 ms**
- pcap parent request: `08:03:58.638` (frame 85)
- pcap parent response: `08:03:58.680` (frame 87)
- pcap child id request: `08:03:58.794` (frame 89)
- pcap child id response: `08:03:58.856` (frame 91)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**
