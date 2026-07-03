# Child Log Analysis

## ucast_fastpr_child

Files analyzed: **4**

- batch folders: `ucast_fastpr-4router-4runs-20260703-140737`

### PCAP-complete child attach summary

| Attach | Metric | M (SD), ms | n |
| --- | --- | ---: | ---: |
| 1 | Request -> Response | 228.25 (107.87) | 4 |
| 1 | Response -> Child ID Request | 524.00 (107.62) | 4 |
| 1 | Child ID Request -> Response | 42.50 (33.49) | 4 |
| 1 | Full Attach | 794.75 (33.78) | 4 |
| 2 | Request -> Response | 20.25 (20.50) | 4 |
| 2 | Response -> Child ID Request | 29.25 (1.26) | 4 |
| 2 | Child ID Request -> Response | 31.25 (35.18) | 4 |
| 2 | Full Attach | 80.75 (54.87) | 4 |

| Metric | M (SD) | n |
| --- | ---: | ---: |
| Failed TX Attempts per Log | 0.00 (0.00) | 4 |
| Log-only or Partial Sequences per Log | 1.00 (0.00) | 4 |

### `ucast_fastpr_child_20260703-141349-run01.log`

- manifest status: `completed`
- child extaddr: `526288aced297f86`
- switch target extaddr(s): `ee362c3385eaa7f9, ee362c3385eaa7f9, ee362c3385eaa7f9`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `4e634c01a79a119f`
- parent rloc16: `n/a`
- child extaddr: `526288aced297f86`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **188 ms**
- Response -> Child ID Request: **564 ms**
- Child ID Request -> Response: **13 ms**
- Full Attach: **765 ms**
- pcap parent request: `14:19:39.266` (frame 188)
- pcap parent response: `14:19:39.454` (frame 189)
- pcap child id request: `14:19:40.018` (frame 197)
- pcap child id response: `14:19:40.031` (frame 199)

#### PCAP-complete child attach 2

- log parent request: `14:19:43.505`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `ee362c3385eaa7f9`
- parent rloc16: `n/a`
- child extaddr: `526288aced297f86`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **10 ms**
- Response -> Child ID Request: **29 ms**
- Child ID Request -> Response: **13 ms**
- Full Attach: **52 ms**
- pcap parent request: `14:19:43.548` (frame 203)
- pcap parent response: `14:19:43.558` (frame 205)
- pcap child id request: `14:19:43.587` (frame 207)
- pcap child id response: `14:19:43.600` (frame 209)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `14:19:43.523`
- log parent response: `14:19:43.538`
- log child id request: `14:19:43.552`
- log child id response: `14:19:43.582`
- parent ipv6: `n/a`
- parent extaddr: `ee362c3385eaa7f9`
- parent rloc16: `0x4400`
- child extaddr: `526288aced297f86`
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

### `ucast_fastpr_child_20260703-142546-run02.log`

- manifest status: `completed`
- child extaddr: `c6f4f17d0cef13c7`
- switch target extaddr(s): `d6c6fdbbe5a56f1a, d6c6fdbbe5a56f1a, d6c6fdbbe5a56f1a`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `fae76ea9b63d5415`
- parent rloc16: `n/a`
- child extaddr: `c6f4f17d0cef13c7`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **320 ms**
- Response -> Child ID Request: **432 ms**
- Child ID Request -> Response: **14 ms**
- Full Attach: **766 ms**
- pcap parent request: `14:31:36.346` (frame 189)
- pcap parent response: `14:31:36.666` (frame 190)
- pcap child id request: `14:31:37.098` (frame 198)
- pcap child id response: `14:31:37.112` (frame 200)

#### PCAP-complete child attach 2

- log parent request: `14:31:40.846`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `d6c6fdbbe5a56f1a`
- parent rloc16: `n/a`
- child extaddr: `c6f4f17d0cef13c7`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **51 ms**
- Response -> Child ID Request: **28 ms**
- Child ID Request -> Response: **84 ms**
- Full Attach: **163 ms**
- pcap parent request: `14:31:40.893` (frame 202)
- pcap parent response: `14:31:40.944` (frame 204)
- pcap child id request: `14:31:40.972` (frame 206)
- pcap child id response: `14:31:41.056` (frame 208)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `14:31:40.864`
- log parent response: `14:31:40.923`
- log child id request: `14:31:40.937`
- log child id response: `14:31:41.037`
- parent ipv6: `n/a`
- parent extaddr: `d6c6fdbbe5a56f1a`
- parent rloc16: `0x2000`
- child extaddr: `c6f4f17d0cef13c7`
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

### `ucast_fastpr_child_20260703-143743-run03.log`

- manifest status: `completed`
- child extaddr: `1e81bb3e6eaf5739`
- switch target extaddr(s): `a249945099b7e6f5, a249945099b7e6f5, a249945099b7e6f5`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `7a425486fc64d00e`
- parent rloc16: `n/a`
- child extaddr: `1e81bb3e6eaf5739`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **94 ms**
- Response -> Child ID Request: **658 ms**
- Child ID Request -> Response: **72 ms**
- Full Attach: **824 ms**
- pcap parent request: `14:43:34.338` (frame 233)
- pcap parent response: `14:43:34.432` (frame 234)
- pcap child id request: `14:43:35.090` (frame 242)
- pcap child id response: `14:43:35.162` (frame 244)

#### PCAP-complete child attach 2

- log parent request: `14:43:38.392`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `a249945099b7e6f5`
- parent rloc16: `n/a`
- child extaddr: `1e81bb3e6eaf5739`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **10 ms**
- Response -> Child ID Request: **31 ms**
- Child ID Request -> Response: **15 ms**
- Full Attach: **56 ms**
- pcap parent request: `14:43:38.438` (frame 246)
- pcap parent response: `14:43:38.448` (frame 248)
- pcap child id request: `14:43:38.479` (frame 250)
- pcap child id response: `14:43:38.494` (frame 252)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `14:43:38.411`
- log parent response: `14:43:38.428`
- log child id request: `14:43:38.444`
- log child id response: `14:43:38.476`
- parent ipv6: `n/a`
- parent extaddr: `a249945099b7e6f5`
- parent rloc16: `0xdc00`
- child extaddr: `1e81bb3e6eaf5739`
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

### `ucast_fastpr_child_20260703-144940-run04.log`

- manifest status: `completed`
- child extaddr: `ae4e0f908130b4f8`
- switch target extaddr(s): `7a1afcbbd4ed71ea, 7a1afcbbd4ed71ea, 7a1afcbbd4ed71ea`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `8252d7122d2daa6c`
- parent rloc16: `n/a`
- child extaddr: `ae4e0f908130b4f8`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **311 ms**
- Response -> Child ID Request: **442 ms**
- Child ID Request -> Response: **71 ms**
- Full Attach: **824 ms**
- pcap parent request: `14:55:31.523` (frame 183)
- pcap parent response: `14:55:31.834` (frame 186)
- pcap child id request: `14:55:32.276` (frame 192)
- pcap child id response: `14:55:32.347` (frame 194)

#### PCAP-complete child attach 2

- log parent request: `14:55:35.789`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `7a1afcbbd4ed71ea`
- parent rloc16: `n/a`
- child extaddr: `ae4e0f908130b4f8`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **10 ms**
- Response -> Child ID Request: **29 ms**
- Child ID Request -> Response: **13 ms**
- Full Attach: **52 ms**
- pcap parent request: `14:55:35.835` (frame 197)
- pcap parent response: `14:55:35.845` (frame 199)
- pcap child id request: `14:55:35.874` (frame 201)
- pcap child id response: `14:55:35.887` (frame 203)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `14:55:35.808`
- log parent response: `14:55:35.824`
- log child id request: `14:55:35.841`
- log child id response: `14:55:35.868`
- parent ipv6: `n/a`
- parent extaddr: `7a1afcbbd4ed71ea`
- parent rloc16: `0x0000`
- child extaddr: `ae4e0f908130b4f8`
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
