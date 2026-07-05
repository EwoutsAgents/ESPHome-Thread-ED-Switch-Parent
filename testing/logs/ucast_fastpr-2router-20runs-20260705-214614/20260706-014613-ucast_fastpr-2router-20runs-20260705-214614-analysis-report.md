# Child Log Analysis

## ucast_fastpr_child

Files analyzed: **20**

- batch folders: `ucast_fastpr-2router-20runs-20260705-214614`

### PCAP-complete child attach summary

| Attach | Metric | M (SD), ms | n |
| --- | --- | ---: | ---: |
| 1 | Request -> Response | 171.45 (114.42) | 20 |
| 1 | Response -> Child ID Request | 580.50 (114.19) | 20 |
| 1 | Child ID Request -> Response | 13.75 (1.07) | 20 |
| 1 | Full Attach | 765.70 (1.87) | 20 |
| 2 | Request -> Response | 8.90 (0.85) | 20 |
| 2 | Response -> Child ID Request | 33.25 (0.91) | 20 |
| 2 | Child ID Request -> Response | 13.90 (1.07) | 20 |
| 2 | Full Attach | 56.05 (1.19) | 20 |

| Metric | M (SD) | n |
| --- | ---: | ---: |
| Failed TX Attempts per Log | 0.00 (0.00) | 20 |
| Log-only or Partial Sequences per Log | 1.00 (0.00) | 20 |

### `ucast_fastpr_child_20260705-215010-run01.log`

- manifest status: `completed`
- child extaddr: `cec01b3608d1fc35`
- switch target extaddr(s): `821382b4904ee947, 821382b4904ee947, 821382b4904ee947`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `86ffbbd48a9020da`
- parent rloc16: `n/a`
- child extaddr: `cec01b3608d1fc35`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **118 ms**
- Response -> Child ID Request: **635 ms**
- Child ID Request -> Response: **12 ms**
- Full Attach: **765 ms**
- pcap parent request: `21:55:51.648` (frame 79)
- pcap parent response: `21:55:51.766` (frame 80)
- pcap child id request: `21:55:52.401` (frame 84)
- pcap child id response: `21:55:52.413` (frame 86)

#### PCAP-complete child attach 2

- log parent request: `21:55:56.259`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `821382b4904ee947`
- parent rloc16: `n/a`
- child extaddr: `cec01b3608d1fc35`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **7 ms**
- Response -> Child ID Request: **34 ms**
- Child ID Request -> Response: **13 ms**
- Full Attach: **54 ms**
- pcap parent request: `21:55:56.307` (frame 89)
- pcap parent response: `21:55:56.314` (frame 91)
- pcap child id request: `21:55:56.348` (frame 93)
- pcap child id response: `21:55:56.361` (frame 95)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `21:55:56.278`
- log parent response: `21:55:56.293`
- log child id request: `21:55:56.312`
- log child id response: `21:55:56.342`
- parent ipv6: `n/a`
- parent extaddr: `821382b4904ee947`
- parent rloc16: `0x3400`
- child extaddr: `cec01b3608d1fc35`
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

### `ucast_fastpr_child_20260705-220158-run02.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `d6d1834ffef7b701`
- switch target extaddr(s): `7a3c8b2681fcaee1, 7a3c8b2681fcaee1, 7a3c8b2681fcaee1`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `1a2f87225b8ca9e7`
- parent rloc16: `n/a`
- child extaddr: `d6d1834ffef7b701`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **359 ms**
- Response -> Child ID Request: **392 ms**
- Child ID Request -> Response: **14 ms**
- Full Attach: **765 ms**
- pcap parent request: `22:07:39.236` (frame 76)
- pcap parent response: `22:07:39.595` (frame 77)
- pcap child id request: `22:07:39.987` (frame 81)
- pcap child id response: `22:07:40.001` (frame 83)

#### PCAP-complete child attach 2

- log parent request: `22:07:43.580`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `7a3c8b2681fcaee1`
- parent rloc16: `n/a`
- child extaddr: `d6d1834ffef7b701`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **8 ms**
- Response -> Child ID Request: **32 ms**
- Child ID Request -> Response: **16 ms**
- Full Attach: **56 ms**
- pcap parent request: `22:07:43.627` (frame 85)
- pcap parent response: `22:07:43.635` (frame 87)
- pcap child id request: `22:07:43.667` (frame 89)
- pcap child id response: `22:07:43.683` (frame 91)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `22:07:43.601`
- log parent response: `22:07:43.614`
- log child id request: `22:07:43.633`
- log child id response: `22:07:43.665`
- parent ipv6: `n/a`
- parent extaddr: `7a3c8b2681fcaee1`
- parent rloc16: `0x5000`
- child extaddr: `d6d1834ffef7b701`
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

### `ucast_fastpr_child_20260705-221346-run03.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `9edcf94bb694dce1`
- switch target extaddr(s): `8ee71843872d41a5, 8ee71843872d41a5, 8ee71843872d41a5`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `2a8e78ad58557a82`
- parent rloc16: `n/a`
- child extaddr: `9edcf94bb694dce1`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **247 ms**
- Response -> Child ID Request: **504 ms**
- Child ID Request -> Response: **12 ms**
- Full Attach: **763 ms**
- pcap parent request: `22:19:26.683` (frame 75)
- pcap parent response: `22:19:26.930` (frame 76)
- pcap child id request: `22:19:27.434` (frame 80)
- pcap child id response: `22:19:27.446` (frame 82)

#### PCAP-complete child attach 2

- log parent request: `22:19:30.795`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `8ee71843872d41a5`
- parent rloc16: `n/a`
- child extaddr: `9edcf94bb694dce1`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **9 ms**
- Response -> Child ID Request: **32 ms**
- Child ID Request -> Response: **16 ms**
- Full Attach: **57 ms**
- pcap parent request: `22:19:30.842` (frame 86)
- pcap parent response: `22:19:30.851` (frame 88)
- pcap child id request: `22:19:30.883` (frame 90)
- pcap child id response: `22:19:30.899` (frame 92)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `22:19:30.815`
- log parent response: `22:19:30.830`
- log child id request: `22:19:30.849`
- log child id response: `22:19:30.880`
- parent ipv6: `n/a`
- parent extaddr: `8ee71843872d41a5`
- parent rloc16: `0x9c00`
- child extaddr: `9edcf94bb694dce1`
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

### `ucast_fastpr_child_20260705-222533-run04.log`

- manifest status: `completed`
- child extaddr: `b6922cbf51b6f796`
- switch target extaddr(s): `4abb690ad7c19ced, 4abb690ad7c19ced, 4abb690ad7c19ced`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `76e0e7eeb208310d`
- parent rloc16: `n/a`
- child extaddr: `b6922cbf51b6f796`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **42 ms**
- Response -> Child ID Request: **709 ms**
- Child ID Request -> Response: **15 ms**
- Full Attach: **766 ms**
- pcap parent request: `22:31:13.288` (frame 74)
- pcap parent response: `22:31:13.330` (frame 75)
- pcap child id request: `22:31:14.039` (frame 80)
- pcap child id response: `22:31:14.054` (frame 82)

#### PCAP-complete child attach 2

- log parent request: `22:31:17.901`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `4abb690ad7c19ced`
- parent rloc16: `n/a`
- child extaddr: `b6922cbf51b6f796`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **9 ms**
- Response -> Child ID Request: **33 ms**
- Child ID Request -> Response: **13 ms**
- Full Attach: **55 ms**
- pcap parent request: `22:31:17.946` (frame 84)
- pcap parent response: `22:31:17.955` (frame 86)
- pcap child id request: `22:31:17.988` (frame 88)
- pcap child id response: `22:31:18.001` (frame 90)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `22:31:17.921`
- log parent response: `22:31:17.937`
- log child id request: `22:31:17.956`
- log child id response: `22:31:17.985`
- parent ipv6: `n/a`
- parent extaddr: `4abb690ad7c19ced`
- parent rloc16: `0xe800`
- child extaddr: `b6922cbf51b6f796`
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

### `ucast_fastpr_child_20260705-223720-run05.log`

- manifest status: `completed`
- child extaddr: `724fe4c4e92c9167`
- switch target extaddr(s): `c69d34f97c58d425, c69d34f97c58d425, c69d34f97c58d425`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `665e216e054400b1`
- parent rloc16: `n/a`
- child extaddr: `724fe4c4e92c9167`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **67 ms**
- Response -> Child ID Request: **686 ms**
- Child ID Request -> Response: **15 ms**
- Full Attach: **768 ms**
- pcap parent request: `22:43:00.595` (frame 77)
- pcap parent response: `22:43:00.662` (frame 78)
- pcap child id request: `22:43:01.348` (frame 82)
- pcap child id response: `22:43:01.363` (frame 84)

#### PCAP-complete child attach 2

- log parent request: `22:43:05.086`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `c69d34f97c58d425`
- parent rloc16: `n/a`
- child extaddr: `724fe4c4e92c9167`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **10 ms**
- Response -> Child ID Request: **32 ms**
- Child ID Request -> Response: **13 ms**
- Full Attach: **55 ms**
- pcap parent request: `22:43:05.129` (frame 86)
- pcap parent response: `22:43:05.139` (frame 88)
- pcap child id request: `22:43:05.171` (frame 90)
- pcap child id response: `22:43:05.184` (frame 92)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `22:43:05.107`
- log parent response: `22:43:05.122`
- log child id request: `22:43:05.141`
- log child id response: `22:43:05.170`
- parent ipv6: `n/a`
- parent extaddr: `c69d34f97c58d425`
- parent rloc16: `0x8400`
- child extaddr: `724fe4c4e92c9167`
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

### `ucast_fastpr_child_20260705-224907-run06.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `6a4768bfd6f26538`
- switch target extaddr(s): `eafde9b27043df13, eafde9b27043df13, eafde9b27043df13`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `a6d7190cbdab706f`
- parent rloc16: `n/a`
- child extaddr: `6a4768bfd6f26538`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **303 ms**
- Response -> Child ID Request: **449 ms**
- Child ID Request -> Response: **13 ms**
- Full Attach: **765 ms**
- pcap parent request: `22:54:48.052` (frame 75)
- pcap parent response: `22:54:48.355` (frame 76)
- pcap child id request: `22:54:48.804` (frame 81)
- pcap child id response: `22:54:48.817` (frame 83)

#### PCAP-complete child attach 2

- log parent request: `22:54:52.233`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `eafde9b27043df13`
- parent rloc16: `n/a`
- child extaddr: `6a4768bfd6f26538`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **9 ms**
- Response -> Child ID Request: **34 ms**
- Child ID Request -> Response: **14 ms**
- Full Attach: **57 ms**
- pcap parent request: `22:54:52.276` (frame 86)
- pcap parent response: `22:54:52.285` (frame 88)
- pcap child id request: `22:54:52.319` (frame 90)
- pcap child id response: `22:54:52.333` (frame 92)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `22:54:52.253`
- log parent response: `22:54:52.268`
- log child id request: `22:54:52.287`
- log child id response: `22:54:52.318`
- parent ipv6: `n/a`
- parent extaddr: `eafde9b27043df13`
- parent rloc16: `0x0000`
- child extaddr: `6a4768bfd6f26538`
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

### `ucast_fastpr_child_20260705-230054-run07.log`

- manifest status: `completed`
- child extaddr: `0ab58ae82c00ddf8`
- switch target extaddr(s): `3ed720659dc84c8e, 3ed720659dc84c8e, 3ed720659dc84c8e`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `be47e3bdbab7c87f`
- parent rloc16: `n/a`
- child extaddr: `0ab58ae82c00ddf8`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **133 ms**
- Response -> Child ID Request: **619 ms**
- Child ID Request -> Response: **15 ms**
- Full Attach: **767 ms**
- pcap parent request: `23:06:35.281` (frame 78)
- pcap parent response: `23:06:35.414` (frame 79)
- pcap child id request: `23:06:36.033` (frame 83)
- pcap child id response: `23:06:36.048` (frame 85)

#### PCAP-complete child attach 2

- log parent request: `23:06:39.379`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `3ed720659dc84c8e`
- parent rloc16: `n/a`
- child extaddr: `0ab58ae82c00ddf8`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **9 ms**
- Response -> Child ID Request: **34 ms**
- Child ID Request -> Response: **14 ms**
- Full Attach: **57 ms**
- pcap parent request: `23:06:39.423` (frame 89)
- pcap parent response: `23:06:39.432` (frame 91)
- pcap child id request: `23:06:39.466` (frame 93)
- pcap child id response: `23:06:39.480` (frame 95)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `23:06:39.399`
- log parent response: `23:06:39.413`
- log child id request: `23:06:39.432`
- log child id response: `23:06:39.464`
- parent ipv6: `n/a`
- parent extaddr: `3ed720659dc84c8e`
- parent rloc16: `0x5800`
- child extaddr: `0ab58ae82c00ddf8`
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

### `ucast_fastpr_child_20260705-231242-run08.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `76d6360e6696b9b1`
- switch target extaddr(s): `6e7364e907636cbd, 6e7364e907636cbd, 6e7364e907636cbd`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `feeb7e5ff1bf8a96`
- parent rloc16: `n/a`
- child extaddr: `76d6360e6696b9b1`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **389 ms**
- Response -> Child ID Request: **366 ms**
- Child ID Request -> Response: **14 ms**
- Full Attach: **769 ms**
- pcap parent request: `23:18:21.951` (frame 73)
- pcap parent response: `23:18:22.340` (frame 74)
- pcap child id request: `23:18:22.706` (frame 78)
- pcap child id response: `23:18:22.720` (frame 80)

#### PCAP-complete child attach 2

- log parent request: `23:18:26.472`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `6e7364e907636cbd`
- parent rloc16: `n/a`
- child extaddr: `76d6360e6696b9b1`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **9 ms**
- Response -> Child ID Request: **35 ms**
- Child ID Request -> Response: **14 ms**
- Full Attach: **58 ms**
- pcap parent request: `23:18:26.516` (frame 83)
- pcap parent response: `23:18:26.525` (frame 85)
- pcap child id request: `23:18:26.560` (frame 87)
- pcap child id response: `23:18:26.574` (frame 89)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `23:18:26.492`
- log parent response: `23:18:26.506`
- log child id request: `23:18:26.525`
- log child id response: `23:18:26.558`
- parent ipv6: `n/a`
- parent extaddr: `6e7364e907636cbd`
- parent rloc16: `0x9c00`
- child extaddr: `76d6360e6696b9b1`
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

### `ucast_fastpr_child_20260705-232429-run09.log`

- manifest status: `completed`
- child extaddr: `1ae41f724d56f42e`
- switch target extaddr(s): `b2f4a38b50e54b45, b2f4a38b50e54b45, b2f4a38b50e54b45`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `9effaf75675e39c9`
- parent rloc16: `n/a`
- child extaddr: `1ae41f724d56f42e`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **37 ms**
- Response -> Child ID Request: **717 ms**
- Child ID Request -> Response: **14 ms**
- Full Attach: **768 ms**
- pcap parent request: `23:30:09.526` (frame 77)
- pcap parent response: `23:30:09.563` (frame 78)
- pcap child id request: `23:30:10.280` (frame 82)
- pcap child id response: `23:30:10.294` (frame 84)

#### PCAP-complete child attach 2

- log parent request: `23:30:13.617`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `b2f4a38b50e54b45`
- parent rloc16: `n/a`
- child extaddr: `1ae41f724d56f42e`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **10 ms**
- Response -> Child ID Request: **33 ms**
- Child ID Request -> Response: **13 ms**
- Full Attach: **56 ms**
- pcap parent request: `23:30:13.663` (frame 86)
- pcap parent response: `23:30:13.673` (frame 88)
- pcap child id request: `23:30:13.706` (frame 90)
- pcap child id response: `23:30:13.719` (frame 92)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `23:30:13.637`
- log parent response: `23:30:13.653`
- log child id request: `23:30:13.671`
- log child id response: `23:30:13.701`
- parent ipv6: `n/a`
- parent extaddr: `b2f4a38b50e54b45`
- parent rloc16: `0xa800`
- child extaddr: `1ae41f724d56f42e`
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

### `ucast_fastpr_child_20260705-233616-run10.log`

- manifest status: `completed`
- child extaddr: `9664c3b10bdf083c`
- switch target extaddr(s): `2efe98dfe67cc28c, 2efe98dfe67cc28c, 2efe98dfe67cc28c`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `26b3e06939ea076e`
- parent rloc16: `n/a`
- child extaddr: `9664c3b10bdf083c`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **197 ms**
- Response -> Child ID Request: **553 ms**
- Child ID Request -> Response: **14 ms**
- Full Attach: **764 ms**
- pcap parent request: `23:41:56.077` (frame 77)
- pcap parent response: `23:41:56.274` (frame 78)
- pcap child id request: `23:41:56.827` (frame 82)
- pcap child id response: `23:41:56.841` (frame 84)

#### PCAP-complete child attach 2

- log parent request: `23:42:00.703`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `2efe98dfe67cc28c`
- parent rloc16: `n/a`
- child extaddr: `9664c3b10bdf083c`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **8 ms**
- Response -> Child ID Request: **33 ms**
- Child ID Request -> Response: **13 ms**
- Full Attach: **54 ms**
- pcap parent request: `23:42:00.749` (frame 87)
- pcap parent response: `23:42:00.757` (frame 89)
- pcap child id request: `23:42:00.790` (frame 91)
- pcap child id response: `23:42:00.803` (frame 93)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `23:42:00.722`
- log parent response: `23:42:00.737`
- log child id request: `23:42:00.756`
- log child id response: `23:42:00.786`
- parent ipv6: `n/a`
- parent extaddr: `2efe98dfe67cc28c`
- parent rloc16: `0x9800`
- child extaddr: `9664c3b10bdf083c`
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

### `ucast_fastpr_child_20260705-234803-run11.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `52f90f2f8b4e2f86`
- switch target extaddr(s): `5e48d072c8878c48, 5e48d072c8878c48, 5e48d072c8878c48`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `c60dd0246884fe04`
- parent rloc16: `n/a`
- child extaddr: `52f90f2f8b4e2f86`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **178 ms**
- Response -> Child ID Request: **573 ms**
- Child ID Request -> Response: **14 ms**
- Full Attach: **765 ms**
- pcap parent request: `23:53:43.436` (frame 80)
- pcap parent response: `23:53:43.614` (frame 81)
- pcap child id request: `23:53:44.187` (frame 85)
- pcap child id response: `23:53:44.201` (frame 87)

#### PCAP-complete child attach 2

- log parent request: `23:53:47.766`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `5e48d072c8878c48`
- parent rloc16: `n/a`
- child extaddr: `52f90f2f8b4e2f86`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **10 ms**
- Response -> Child ID Request: **34 ms**
- Child ID Request -> Response: **14 ms**
- Full Attach: **58 ms**
- pcap parent request: `23:53:47.812` (frame 91)
- pcap parent response: `23:53:47.822` (frame 93)
- pcap child id request: `23:53:47.856` (frame 95)
- pcap child id response: `23:53:47.870` (frame 97)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `23:53:47.786`
- log parent response: `23:53:47.802`
- log child id request: `23:53:47.821`
- log child id response: `23:53:47.852`
- parent ipv6: `n/a`
- parent extaddr: `5e48d072c8878c48`
- parent rloc16: `0xe800`
- child extaddr: `52f90f2f8b4e2f86`
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

### `ucast_fastpr_child_20260705-235950-run12.log`

- manifest status: `completed`
- child extaddr: `a2ee91ffabeb30c9`
- switch target extaddr(s): `ce090b43ed234c89, ce090b43ed234c89, ce090b43ed234c89`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `aaff10cd7cdf2cf7`
- parent rloc16: `n/a`
- child extaddr: `a2ee91ffabeb30c9`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **246 ms**
- Response -> Child ID Request: **506 ms**
- Child ID Request -> Response: **13 ms**
- Full Attach: **765 ms**
- pcap parent request: `00:05:30.571` (frame 80)
- pcap parent response: `00:05:30.817` (frame 81)
- pcap child id request: `00:05:31.323` (frame 86)
- pcap child id response: `00:05:31.336` (frame 88)

#### PCAP-complete child attach 2

- log parent request: `00:05:34.853`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `ce090b43ed234c89`
- parent rloc16: `n/a`
- child extaddr: `a2ee91ffabeb30c9`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **9 ms**
- Response -> Child ID Request: **33 ms**
- Child ID Request -> Response: **14 ms**
- Full Attach: **56 ms**
- pcap parent request: `00:05:34.899` (frame 90)
- pcap parent response: `00:05:34.908` (frame 92)
- pcap child id request: `00:05:34.941` (frame 94)
- pcap child id response: `00:05:34.955` (frame 96)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `00:05:34.874`
- log parent response: `00:05:34.888`
- log child id request: `00:05:34.906`
- log child id response: `00:05:34.937`
- parent ipv6: `n/a`
- parent extaddr: `ce090b43ed234c89`
- parent rloc16: `0x3400`
- child extaddr: `a2ee91ffabeb30c9`
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

### `ucast_fastpr_child_20260706-001137-run13.log`

- manifest status: `completed`
- child extaddr: `4e9c6f2823f89a3f`
- switch target extaddr(s): `ca19ba0a23f19003, ca19ba0a23f19003, ca19ba0a23f19003`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `164f09ef614af61d`
- parent rloc16: `n/a`
- child extaddr: `4e9c6f2823f89a3f`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **41 ms**
- Response -> Child ID Request: **712 ms**
- Child ID Request -> Response: **14 ms**
- Full Attach: **767 ms**
- pcap parent request: `00:17:17.354` (frame 74)
- pcap parent response: `00:17:17.395` (frame 75)
- pcap child id request: `00:17:18.107` (frame 79)
- pcap child id response: `00:17:18.121` (frame 81)

#### PCAP-complete child attach 2

- log parent request: `00:17:21.971`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `ca19ba0a23f19003`
- parent rloc16: `n/a`
- child extaddr: `4e9c6f2823f89a3f`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **10 ms**
- Response -> Child ID Request: **32 ms**
- Child ID Request -> Response: **13 ms**
- Full Attach: **55 ms**
- pcap parent request: `00:17:22.016` (frame 85)
- pcap parent response: `00:17:22.026` (frame 87)
- pcap child id request: `00:17:22.058` (frame 89)
- pcap child id response: `00:17:22.071` (frame 91)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `00:17:21.991`
- log parent response: `00:17:22.007`
- log child id request: `00:17:22.026`
- log child id response: `00:17:22.055`
- parent ipv6: `n/a`
- parent extaddr: `ca19ba0a23f19003`
- parent rloc16: `0xc800`
- child extaddr: `4e9c6f2823f89a3f`
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

### `ucast_fastpr_child_20260706-002324-run14.log`

- manifest status: `completed`
- child extaddr: `fec5a5ef751a388d`
- switch target extaddr(s): `bafec7253cfdb260, bafec7253cfdb260, bafec7253cfdb260`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `daf7c57d169f970b`
- parent rloc16: `n/a`
- child extaddr: `fec5a5ef751a388d`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **227 ms**
- Response -> Child ID Request: **525 ms**
- Child ID Request -> Response: **15 ms**
- Full Attach: **767 ms**
- pcap parent request: `00:29:04.907` (frame 79)
- pcap parent response: `00:29:05.134` (frame 80)
- pcap child id request: `00:29:05.659` (frame 84)
- pcap child id response: `00:29:05.674` (frame 86)

#### PCAP-complete child attach 2

- log parent request: `00:29:08.875`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `bafec7253cfdb260`
- parent rloc16: `n/a`
- child extaddr: `fec5a5ef751a388d`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **10 ms**
- Response -> Child ID Request: **33 ms**
- Child ID Request -> Response: **14 ms**
- Full Attach: **57 ms**
- pcap parent request: `00:29:08.917` (frame 88)
- pcap parent response: `00:29:08.927` (frame 90)
- pcap child id request: `00:29:08.960` (frame 92)
- pcap child id response: `00:29:08.974` (frame 94)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `00:29:08.895`
- log parent response: `00:29:08.910`
- log child id request: `00:29:08.929`
- log child id response: `00:29:08.959`
- parent ipv6: `n/a`
- parent extaddr: `bafec7253cfdb260`
- parent rloc16: `0x2c00`
- child extaddr: `fec5a5ef751a388d`
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

### `ucast_fastpr_child_20260706-003511-run15.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `bed3feb896347471`
- switch target extaddr(s): `5ef2057ff5d7c2e5, 5ef2057ff5d7c2e5, 5ef2057ff5d7c2e5`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `c2e8ce85c6da48ea`
- parent rloc16: `n/a`
- child extaddr: `bed3feb896347471`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **57 ms**
- Response -> Child ID Request: **693 ms**
- Child ID Request -> Response: **12 ms**
- Full Attach: **762 ms**
- pcap parent request: `00:40:51.560` (frame 81)
- pcap parent response: `00:40:51.617` (frame 82)
- pcap child id request: `00:40:52.310` (frame 86)
- pcap child id response: `00:40:52.322` (frame 88)

#### PCAP-complete child attach 2

- log parent request: `00:40:55.737`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `5ef2057ff5d7c2e5`
- parent rloc16: `n/a`
- child extaddr: `bed3feb896347471`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **9 ms**
- Response -> Child ID Request: **34 ms**
- Child ID Request -> Response: **13 ms**
- Full Attach: **56 ms**
- pcap parent request: `00:40:55.782` (frame 90)
- pcap parent response: `00:40:55.791` (frame 92)
- pcap child id request: `00:40:55.825` (frame 94)
- pcap child id response: `00:40:55.838` (frame 96)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `00:40:55.757`
- log parent response: `00:40:55.773`
- log child id request: `00:40:55.792`
- log child id response: `00:40:55.822`
- parent ipv6: `n/a`
- parent extaddr: `5ef2057ff5d7c2e5`
- parent rloc16: `0x4c00`
- child extaddr: `bed3feb896347471`
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

### `ucast_fastpr_child_20260706-004658-run16.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `ba1823c28d417468`
- switch target extaddr(s): `9241b37813ddd122, 9241b37813ddd122, 9241b37813ddd122`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `4a9dfd64c3c6092f`
- parent rloc16: `n/a`
- child extaddr: `ba1823c28d417468`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **358 ms**
- Response -> Child ID Request: **395 ms**
- Child ID Request -> Response: **13 ms**
- Full Attach: **766 ms**
- pcap parent request: `00:52:37.970` (frame 77)
- pcap parent response: `00:52:38.328` (frame 78)
- pcap child id request: `00:52:38.723` (frame 82)
- pcap child id response: `00:52:38.736` (frame 84)

#### PCAP-complete child attach 2

- log parent request: `00:52:42.572`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `9241b37813ddd122`
- parent rloc16: `n/a`
- child extaddr: `ba1823c28d417468`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **8 ms**
- Response -> Child ID Request: **34 ms**
- Child ID Request -> Response: **15 ms**
- Full Attach: **57 ms**
- pcap parent request: `00:52:42.616` (frame 86)
- pcap parent response: `00:52:42.624` (frame 88)
- pcap child id request: `00:52:42.658` (frame 90)
- pcap child id response: `00:52:42.673` (frame 92)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `00:52:42.592`
- log parent response: `00:52:42.606`
- log child id request: `00:52:42.624`
- log child id response: `00:52:42.657`
- parent ipv6: `n/a`
- parent extaddr: `9241b37813ddd122`
- parent rloc16: `0x1c00`
- child extaddr: `ba1823c28d417468`
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

### `ucast_fastpr_child_20260706-005845-run17.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `ca57fe16065533cc`
- switch target extaddr(s): `469125086361ad0e, 469125086361ad0e, 469125086361ad0e`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `2293ee55ad77a606`
- parent rloc16: `n/a`
- child extaddr: `ca57fe16065533cc`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **105 ms**
- Response -> Child ID Request: **645 ms**
- Child ID Request -> Response: **13 ms**
- Full Attach: **763 ms**
- pcap parent request: `01:04:25.198` (frame 78)
- pcap parent response: `01:04:25.303` (frame 79)
- pcap child id request: `01:04:25.948` (frame 83)
- pcap child id response: `01:04:25.961` (frame 85)

#### PCAP-complete child attach 2

- log parent request: `01:04:29.488`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `469125086361ad0e`
- parent rloc16: `n/a`
- child extaddr: `ca57fe16065533cc`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **9 ms**
- Response -> Child ID Request: **34 ms**
- Child ID Request -> Response: **12 ms**
- Full Attach: **55 ms**
- pcap parent request: `01:04:29.534` (frame 87)
- pcap parent response: `01:04:29.543` (frame 89)
- pcap child id request: `01:04:29.577` (frame 91)
- pcap child id response: `01:04:29.589` (frame 93)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `01:04:29.509`
- log parent response: `01:04:29.524`
- log child id request: `01:04:29.543`
- log child id response: `01:04:29.573`
- parent ipv6: `n/a`
- parent extaddr: `469125086361ad0e`
- parent rloc16: `0x9c00`
- child extaddr: `ca57fe16065533cc`
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

### `ucast_fastpr_child_20260706-011032-run18.log`

- manifest status: `completed`
- child extaddr: `cac6d0d3b802b18e`
- switch target extaddr(s): `52b38f1925cb4e73, 52b38f1925cb4e73, 52b38f1925cb4e73`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `5e180b9679f56f17`
- parent rloc16: `n/a`
- child extaddr: `cac6d0d3b802b18e`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **69 ms**
- Response -> Child ID Request: **682 ms**
- Child ID Request -> Response: **15 ms**
- Full Attach: **766 ms**
- pcap parent request: `01:16:11.718` (frame 80)
- pcap parent response: `01:16:11.787` (frame 81)
- pcap child id request: `01:16:12.469` (frame 86)
- pcap child id response: `01:16:12.484` (frame 88)

#### PCAP-complete child attach 2

- log parent request: `01:16:16.313`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `52b38f1925cb4e73`
- parent rloc16: `n/a`
- child extaddr: `cac6d0d3b802b18e`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **8 ms**
- Response -> Child ID Request: **34 ms**
- Child ID Request -> Response: **15 ms**
- Full Attach: **57 ms**
- pcap parent request: `01:16:16.359` (frame 90)
- pcap parent response: `01:16:16.367` (frame 92)
- pcap child id request: `01:16:16.401` (frame 94)
- pcap child id response: `01:16:16.416` (frame 96)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `01:16:16.334`
- log parent response: `01:16:16.348`
- log child id request: `01:16:16.367`
- log child id response: `01:16:16.399`
- parent ipv6: `n/a`
- parent extaddr: `52b38f1925cb4e73`
- parent rloc16: `0xa000`
- child extaddr: `cac6d0d3b802b18e`
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

### `ucast_fastpr_child_20260706-012218-run19.log`

- manifest status: `completed`
- child extaddr: `366621e9f654b2ae`
- switch target extaddr(s): `96f884f9db914956, 96f884f9db914956, 96f884f9db914956`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `726560f48f5d5740`
- parent rloc16: `n/a`
- child extaddr: `366621e9f654b2ae`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **118 ms**
- Response -> Child ID Request: **634 ms**
- Child ID Request -> Response: **13 ms**
- Full Attach: **765 ms**
- pcap parent request: `01:27:58.931` (frame 75)
- pcap parent response: `01:27:59.049` (frame 76)
- pcap child id request: `01:27:59.683` (frame 80)
- pcap child id response: `01:27:59.696` (frame 82)

#### PCAP-complete child attach 2

- log parent request: `01:28:03.422`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `96f884f9db914956`
- parent rloc16: `n/a`
- child extaddr: `366621e9f654b2ae`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **8 ms**
- Response -> Child ID Request: **33 ms**
- Child ID Request -> Response: **14 ms**
- Full Attach: **55 ms**
- pcap parent request: `01:28:03.465` (frame 85)
- pcap parent response: `01:28:03.473` (frame 87)
- pcap child id request: `01:28:03.506` (frame 89)
- pcap child id response: `01:28:03.520` (frame 91)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `01:28:03.443`
- log parent response: `01:28:03.457`
- log child id request: `01:28:03.475`
- log child id response: `01:28:03.506`
- parent ipv6: `n/a`
- parent extaddr: `96f884f9db914956`
- parent rloc16: `0xcc00`
- child extaddr: `366621e9f654b2ae`
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

### `ucast_fastpr_child_20260706-013406-run20.log`

- manifest status: `completed`
- child extaddr: `823ad16360feb7c8`
- switch target extaddr(s): `968eb5292208d351, 968eb5292208d351, 968eb5292208d351`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `161054483da8c63f`
- parent rloc16: `n/a`
- child extaddr: `823ad16360feb7c8`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **138 ms**
- Response -> Child ID Request: **615 ms**
- Child ID Request -> Response: **15 ms**
- Full Attach: **768 ms**
- pcap parent request: `01:39:46.473` (frame 79)
- pcap parent response: `01:39:46.611` (frame 80)
- pcap child id request: `01:39:47.226` (frame 84)
- pcap child id response: `01:39:47.241` (frame 86)

#### PCAP-complete child attach 2

- log parent request: `01:39:50.423`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `968eb5292208d351`
- parent rloc16: `n/a`
- child extaddr: `823ad16360feb7c8`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **9 ms**
- Response -> Child ID Request: **32 ms**
- Child ID Request -> Response: **15 ms**
- Full Attach: **56 ms**
- pcap parent request: `01:39:50.466` (frame 89)
- pcap parent response: `01:39:50.475` (frame 91)
- pcap child id request: `01:39:50.507` (frame 93)
- pcap child id response: `01:39:50.522` (frame 95)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `01:39:50.444`
- log parent response: `01:39:50.458`
- log child id request: `01:39:50.477`
- log child id response: `01:39:50.507`
- parent ipv6: `n/a`
- parent extaddr: `968eb5292208d351`
- parent rloc16: `0x4400`
- child extaddr: `823ad16360feb7c8`
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
