# Child Log Analysis

## ucast_fastpr_child

Files analyzed: **20**

- batch folders: `ucast_fastpr-3router-20runs-20260706-014616`

### PCAP-complete child attach summary

| Attach | Metric | M (SD), ms | n |
| --- | --- | ---: | ---: |
| 1 | Request -> Response | 158.30 (101.99) | 20 |
| 1 | Response -> Child ID Request | 594.10 (101.54) | 20 |
| 1 | Child ID Request -> Response | 13.80 (1.06) | 20 |
| 1 | Full Attach | 766.20 (1.54) | 20 |
| 2 | Request -> Response | 8.95 (0.94) | 20 |
| 2 | Response -> Child ID Request | 31.65 (1.73) | 20 |
| 2 | Child ID Request -> Response | 13.85 (0.93) | 20 |
| 2 | Full Attach | 54.45 (2.01) | 20 |

| Metric | M (SD) | n |
| --- | ---: | ---: |
| Failed TX Attempts per Log | 0.00 (0.00) | 20 |
| Log-only or Partial Sequences per Log | 1.00 (0.00) | 20 |

### `ucast_fastpr_child_20260706-015118-run01.log`

- manifest status: `completed`
- child extaddr: `0e75dd062872ab82`
- switch target extaddr(s): `5a43dde114367947, 5a43dde114367947, 5a43dde114367947`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `5a8b0076b9350263`
- parent rloc16: `n/a`
- child extaddr: `0e75dd062872ab82`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **57 ms**
- Response -> Child ID Request: **694 ms**
- Child ID Request -> Response: **13 ms**
- Full Attach: **764 ms**
- pcap parent request: `01:57:02.808` (frame 128)
- pcap parent response: `01:57:02.865` (frame 129)
- pcap child id request: `01:57:03.559` (frame 135)
- pcap child id response: `01:57:03.572` (frame 137)

#### PCAP-complete child attach 2

- log parent request: `01:57:07.374`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `5a43dde114367947`
- parent rloc16: `n/a`
- child extaddr: `0e75dd062872ab82`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **9 ms**
- Response -> Child ID Request: **30 ms**
- Child ID Request -> Response: **16 ms**
- Full Attach: **55 ms**
- pcap parent request: `01:57:07.420` (frame 140)
- pcap parent response: `01:57:07.429` (frame 142)
- pcap child id request: `01:57:07.459` (frame 144)
- pcap child id response: `01:57:07.475` (frame 146)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `01:57:07.393`
- log parent response: `01:57:07.408`
- log child id request: `01:57:07.424`
- log child id response: `01:57:07.456`
- parent ipv6: `n/a`
- parent extaddr: `5a43dde114367947`
- parent rloc16: `0xb000`
- child extaddr: `0e75dd062872ab82`
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

### `ucast_fastpr_child_20260706-020310-run02.log`

- manifest status: `completed`
- child extaddr: `86f28ded98fa5ec7`
- switch target extaddr(s): `762e3721909f392d, 762e3721909f392d, 762e3721909f392d`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `e27870dc7f9c67f4`
- parent rloc16: `n/a`
- child extaddr: `86f28ded98fa5ec7`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **26 ms**
- Response -> Child ID Request: **725 ms**
- Child ID Request -> Response: **15 ms**
- Full Attach: **766 ms**
- pcap parent request: `02:08:54.841` (frame 133)
- pcap parent response: `02:08:54.867` (frame 134)
- pcap child id request: `02:08:55.592` (frame 140)
- pcap child id response: `02:08:55.607` (frame 142)

#### PCAP-complete child attach 2

- log parent request: `02:08:59.381`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `762e3721909f392d`
- parent rloc16: `n/a`
- child extaddr: `86f28ded98fa5ec7`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **10 ms**
- Response -> Child ID Request: **34 ms**
- Child ID Request -> Response: **15 ms**
- Full Attach: **59 ms**
- pcap parent request: `02:08:59.425` (frame 144)
- pcap parent response: `02:08:59.435` (frame 146)
- pcap child id request: `02:08:59.469` (frame 148)
- pcap child id response: `02:08:59.484` (frame 150)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `02:08:59.401`
- log parent response: `02:08:59.419`
- log child id request: `02:08:59.438`
- log child id response: `02:08:59.470`
- parent ipv6: `n/a`
- parent extaddr: `762e3721909f392d`
- parent rloc16: `0x4000`
- child extaddr: `86f28ded98fa5ec7`
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

### `ucast_fastpr_child_20260706-021501-run03.log`

- manifest status: `completed`
- child extaddr: `6edd7f7140da2f41`
- switch target extaddr(s): `d6bc22b42b439521, d6bc22b42b439521, d6bc22b42b439521`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `1aa8cab3cedebbea`
- parent rloc16: `n/a`
- child extaddr: `6edd7f7140da2f41`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **202 ms**
- Response -> Child ID Request: **551 ms**
- Child ID Request -> Response: **13 ms**
- Full Attach: **766 ms**
- pcap parent request: `02:20:46.522` (frame 126)
- pcap parent response: `02:20:46.724` (frame 127)
- pcap child id request: `02:20:47.275` (frame 133)
- pcap child id response: `02:20:47.288` (frame 135)

#### PCAP-complete child attach 2

- log parent request: `02:20:50.989`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `d6bc22b42b439521`
- parent rloc16: `n/a`
- child extaddr: `6edd7f7140da2f41`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **9 ms**
- Response -> Child ID Request: **31 ms**
- Child ID Request -> Response: **14 ms**
- Full Attach: **54 ms**
- pcap parent request: `02:20:51.034` (frame 137)
- pcap parent response: `02:20:51.043` (frame 139)
- pcap child id request: `02:20:51.074` (frame 141)
- pcap child id response: `02:20:51.088` (frame 143)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `02:20:51.008`
- log parent response: `02:20:51.022`
- log child id request: `02:20:51.038`
- log child id response: `02:20:51.069`
- parent ipv6: `n/a`
- parent extaddr: `d6bc22b42b439521`
- parent rloc16: `0x2c00`
- child extaddr: `6edd7f7140da2f41`
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

### `ucast_fastpr_child_20260706-022653-run04.log`

- manifest status: `completed`
- child extaddr: `4ef411ade7fea2fc`
- switch target extaddr(s): `5a013904330071c1, 5a013904330071c1, 5a013904330071c1`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `fe29b5d43781fcd1`
- parent rloc16: `n/a`
- child extaddr: `4ef411ade7fea2fc`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **161 ms**
- Response -> Child ID Request: **591 ms**
- Child ID Request -> Response: **13 ms**
- Full Attach: **765 ms**
- pcap parent request: `02:32:39.105` (frame 128)
- pcap parent response: `02:32:39.266` (frame 129)
- pcap child id request: `02:32:39.857` (frame 135)
- pcap child id response: `02:32:39.870` (frame 137)

#### PCAP-complete child attach 2

- log parent request: `02:32:43.022`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `5a013904330071c1`
- parent rloc16: `n/a`
- child extaddr: `4ef411ade7fea2fc`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **8 ms**
- Response -> Child ID Request: **30 ms**
- Child ID Request -> Response: **13 ms**
- Full Attach: **51 ms**
- pcap parent request: `02:32:43.068` (frame 140)
- pcap parent response: `02:32:43.076` (frame 142)
- pcap child id request: `02:32:43.106` (frame 144)
- pcap child id response: `02:32:43.119` (frame 146)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `02:32:43.041`
- log parent response: `02:32:43.055`
- log child id request: `02:32:43.071`
- log child id response: `02:32:43.100`
- parent ipv6: `n/a`
- parent extaddr: `5a013904330071c1`
- parent rloc16: `0x3c00`
- child extaddr: `4ef411ade7fea2fc`
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

### `ucast_fastpr_child_20260706-023845-run05.log`

- manifest status: `completed`
- child extaddr: `5eb6d6f239ec3218`
- switch target extaddr(s): `32e9fd1382d488e6, 32e9fd1382d488e6, 32e9fd1382d488e6`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `4ee4135083436c92`
- parent rloc16: `n/a`
- child extaddr: `5eb6d6f239ec3218`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **120 ms**
- Response -> Child ID Request: **632 ms**
- Child ID Request -> Response: **12 ms**
- Full Attach: **764 ms**
- pcap parent request: `02:44:30.564` (frame 127)
- pcap parent response: `02:44:30.684` (frame 128)
- pcap child id request: `02:44:31.316` (frame 134)
- pcap child id response: `02:44:31.328` (frame 136)

#### PCAP-complete child attach 2

- log parent request: `02:44:34.924`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `32e9fd1382d488e6`
- parent rloc16: `n/a`
- child extaddr: `5eb6d6f239ec3218`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **10 ms**
- Response -> Child ID Request: **32 ms**
- Child ID Request -> Response: **13 ms**
- Full Attach: **55 ms**
- pcap parent request: `02:44:34.969` (frame 139)
- pcap parent response: `02:44:34.979` (frame 141)
- pcap child id request: `02:44:35.011` (frame 143)
- pcap child id response: `02:44:35.024` (frame 145)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `02:44:34.942`
- log parent response: `02:44:34.957`
- log child id request: `02:44:34.974`
- log child id response: `02:44:35.004`
- parent ipv6: `n/a`
- parent extaddr: `32e9fd1382d488e6`
- parent rloc16: `0x9400`
- child extaddr: `5eb6d6f239ec3218`
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

### `ucast_fastpr_child_20260706-025037-run06.log`

- manifest status: `completed`
- child extaddr: `ae71b6606e5bb083`
- switch target extaddr(s): `767b19ce6f2b036e, 767b19ce6f2b036e, 767b19ce6f2b036e`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `3a1f146c1c5d5c5a`
- parent rloc16: `n/a`
- child extaddr: `ae71b6606e5bb083`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **34 ms**
- Response -> Child ID Request: **718 ms**
- Child ID Request -> Response: **15 ms**
- Full Attach: **767 ms**
- pcap parent request: `02:56:22.839` (frame 126)
- pcap parent response: `02:56:22.873` (frame 127)
- pcap child id request: `02:56:23.591` (frame 134)
- pcap child id response: `02:56:23.606` (frame 136)

#### PCAP-complete child attach 2

- log parent request: `02:56:26.759`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `767b19ce6f2b036e`
- parent rloc16: `n/a`
- child extaddr: `ae71b6606e5bb083`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **11 ms**
- Response -> Child ID Request: **30 ms**
- Child ID Request -> Response: **13 ms**
- Full Attach: **54 ms**
- pcap parent request: `02:56:26.803` (frame 140)
- pcap parent response: `02:56:26.814` (frame 142)
- pcap child id request: `02:56:26.844` (frame 144)
- pcap child id response: `02:56:26.857` (frame 146)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `02:56:26.778`
- log parent response: `02:56:26.793`
- log child id request: `02:56:26.809`
- log child id response: `02:56:26.838`
- parent ipv6: `n/a`
- parent extaddr: `767b19ce6f2b036e`
- parent rloc16: `0x0400`
- child extaddr: `ae71b6606e5bb083`
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

### `ucast_fastpr_child_20260706-030229-run07.log`

- manifest status: `completed`
- child extaddr: `4686783c47933cd2`
- switch target extaddr(s): `36143ce7b2687605, 36143ce7b2687605, 36143ce7b2687605`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `2a07109ce4a96752`
- parent rloc16: `n/a`
- child extaddr: `4686783c47933cd2`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **266 ms**
- Response -> Child ID Request: **488 ms**
- Child ID Request -> Response: **15 ms**
- Full Attach: **769 ms**
- pcap parent request: `03:08:14.090` (frame 130)
- pcap parent response: `03:08:14.356` (frame 131)
- pcap child id request: `03:08:14.844` (frame 138)
- pcap child id response: `03:08:14.859` (frame 140)

#### PCAP-complete child attach 2

- log parent request: `03:08:18.642`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `36143ce7b2687605`
- parent rloc16: `n/a`
- child extaddr: `4686783c47933cd2`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **9 ms**
- Response -> Child ID Request: **31 ms**
- Child ID Request -> Response: **14 ms**
- Full Attach: **54 ms**
- pcap parent request: `03:08:18.687` (frame 142)
- pcap parent response: `03:08:18.696` (frame 144)
- pcap child id request: `03:08:18.727` (frame 146)
- pcap child id response: `03:08:18.741` (frame 148)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `03:08:18.660`
- log parent response: `03:08:18.676`
- log child id request: `03:08:18.692`
- log child id response: `03:08:18.723`
- parent ipv6: `n/a`
- parent extaddr: `36143ce7b2687605`
- parent rloc16: `0x3400`
- child extaddr: `4686783c47933cd2`
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

### `ucast_fastpr_child_20260706-031421-run08.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `62a5e04fa8317138`
- switch target extaddr(s): `7235cf503606c0f3, 7235cf503606c0f3, 7235cf503606c0f3`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `32319b40ecd6f6e3`
- parent rloc16: `n/a`
- child extaddr: `62a5e04fa8317138`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **276 ms**
- Response -> Child ID Request: **477 ms**
- Child ID Request -> Response: **14 ms**
- Full Attach: **767 ms**
- pcap parent request: `03:20:06.620` (frame 124)
- pcap parent response: `03:20:06.896` (frame 125)
- pcap child id request: `03:20:07.373` (frame 131)
- pcap child id response: `03:20:07.387` (frame 133)

#### PCAP-complete child attach 2

- log parent request: `03:20:10.558`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `7235cf503606c0f3`
- parent rloc16: `n/a`
- child extaddr: `62a5e04fa8317138`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **9 ms**
- Response -> Child ID Request: **31 ms**
- Child ID Request -> Response: **13 ms**
- Full Attach: **53 ms**
- pcap parent request: `03:20:10.603` (frame 138)
- pcap parent response: `03:20:10.612` (frame 140)
- pcap child id request: `03:20:10.643` (frame 142)
- pcap child id response: `03:20:10.656` (frame 144)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `03:20:10.576`
- log parent response: `03:20:10.592`
- log child id request: `03:20:10.609`
- log child id response: `03:20:10.639`
- parent ipv6: `n/a`
- parent extaddr: `7235cf503606c0f3`
- parent rloc16: `0xc400`
- child extaddr: `62a5e04fa8317138`
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

### `ucast_fastpr_child_20260706-032613-run09.log`

- manifest status: `completed`
- child extaddr: `c23082040d13bff5`
- switch target extaddr(s): `0a4e813a3554c64f, 0a4e813a3554c64f, 0a4e813a3554c64f`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `0edbf3c48711397e`
- parent rloc16: `n/a`
- child extaddr: `c23082040d13bff5`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **326 ms**
- Response -> Child ID Request: **426 ms**
- Child ID Request -> Response: **13 ms**
- Full Attach: **765 ms**
- pcap parent request: `03:31:57.811` (frame 124)
- pcap parent response: `03:31:58.137` (frame 125)
- pcap child id request: `03:31:58.563` (frame 131)
- pcap child id response: `03:31:58.576` (frame 133)

#### PCAP-complete child attach 2

- log parent request: `03:32:02.410`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `0a4e813a3554c64f`
- parent rloc16: `n/a`
- child extaddr: `c23082040d13bff5`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **8 ms**
- Response -> Child ID Request: **31 ms**
- Child ID Request -> Response: **14 ms**
- Full Attach: **53 ms**
- pcap parent request: `03:32:02.456` (frame 136)
- pcap parent response: `03:32:02.464` (frame 138)
- pcap child id request: `03:32:02.495` (frame 140)
- pcap child id response: `03:32:02.509` (frame 142)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `03:32:02.429`
- log parent response: `03:32:02.443`
- log child id request: `03:32:02.459`
- log child id response: `03:32:02.490`
- parent ipv6: `n/a`
- parent extaddr: `0a4e813a3554c64f`
- parent rloc16: `0x2000`
- child extaddr: `c23082040d13bff5`
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

### `ucast_fastpr_child_20260706-033805-run10.log`

- manifest status: `completed`
- child extaddr: `a67248857de1c087`
- switch target extaddr(s): `22438d1c0cefcec8, 22438d1c0cefcec8, 22438d1c0cefcec8`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `7203672feb12c5cf`
- parent rloc16: `n/a`
- child extaddr: `a67248857de1c087`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **80 ms**
- Response -> Child ID Request: **674 ms**
- Child ID Request -> Response: **13 ms**
- Full Attach: **767 ms**
- pcap parent request: `03:43:50.157` (frame 127)
- pcap parent response: `03:43:50.237` (frame 128)
- pcap child id request: `03:43:50.911` (frame 134)
- pcap child id response: `03:43:50.924` (frame 136)

#### PCAP-complete child attach 2

- log parent request: `03:43:54.164`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `22438d1c0cefcec8`
- parent rloc16: `n/a`
- child extaddr: `a67248857de1c087`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **9 ms**
- Response -> Child ID Request: **34 ms**
- Child ID Request -> Response: **13 ms**
- Full Attach: **56 ms**
- pcap parent request: `03:43:54.212` (frame 138)
- pcap parent response: `03:43:54.221` (frame 140)
- pcap child id request: `03:43:54.255` (frame 142)
- pcap child id response: `03:43:54.268` (frame 144)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `03:43:54.184`
- log parent response: `03:43:54.200`
- log child id request: `03:43:54.219`
- log child id response: `03:43:54.250`
- parent ipv6: `n/a`
- parent extaddr: `22438d1c0cefcec8`
- parent rloc16: `0xb800`
- child extaddr: `a67248857de1c087`
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

### `ucast_fastpr_child_20260706-034956-run11.log`

- manifest status: `completed`
- child extaddr: `16ec0f71ce017769`
- switch target extaddr(s): `6254126350c7a245, 6254126350c7a245, 6254126350c7a245`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `a6aa949f7f64e59c`
- parent rloc16: `n/a`
- child extaddr: `16ec0f71ce017769`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **60 ms**
- Response -> Child ID Request: **694 ms**
- Child ID Request -> Response: **15 ms**
- Full Attach: **769 ms**
- pcap parent request: `03:55:41.193` (frame 129)
- pcap parent response: `03:55:41.253` (frame 130)
- pcap child id request: `03:55:41.947` (frame 136)
- pcap child id response: `03:55:41.962` (frame 138)

#### PCAP-complete child attach 2

- log parent request: `03:55:45.806`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `6254126350c7a245`
- parent rloc16: `n/a`
- child extaddr: `16ec0f71ce017769`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **9 ms**
- Response -> Child ID Request: **30 ms**
- Child ID Request -> Response: **14 ms**
- Full Attach: **53 ms**
- pcap parent request: `03:55:45.850` (frame 142)
- pcap parent response: `03:55:45.859` (frame 144)
- pcap child id request: `03:55:45.889` (frame 146)
- pcap child id response: `03:55:45.903` (frame 148)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `03:55:45.825`
- log parent response: `03:55:45.838`
- log child id request: `03:55:45.854`
- log child id response: `03:55:45.884`
- parent ipv6: `n/a`
- parent extaddr: `6254126350c7a245`
- parent rloc16: `0xb800`
- child extaddr: `16ec0f71ce017769`
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

### `ucast_fastpr_child_20260706-040148-run12.log`

- manifest status: `completed`
- child extaddr: `22d0f9c4959da25b`
- switch target extaddr(s): `329febdbc13a9a7b, 329febdbc13a9a7b, 329febdbc13a9a7b`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `9a3aab054292c3d5`
- parent rloc16: `n/a`
- child extaddr: `22d0f9c4959da25b`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **136 ms**
- Response -> Child ID Request: **616 ms**
- Child ID Request -> Response: **16 ms**
- Full Attach: **768 ms**
- pcap parent request: `04:07:33.231` (frame 124)
- pcap parent response: `04:07:33.367` (frame 125)
- pcap child id request: `04:07:33.983` (frame 131)
- pcap child id response: `04:07:33.999` (frame 133)

#### PCAP-complete child attach 2

- log parent request: `04:07:37.602`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `329febdbc13a9a7b`
- parent rloc16: `n/a`
- child extaddr: `22d0f9c4959da25b`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **8 ms**
- Response -> Child ID Request: **33 ms**
- Child ID Request -> Response: **14 ms**
- Full Attach: **55 ms**
- pcap parent request: `04:07:37.648` (frame 135)
- pcap parent response: `04:07:37.656` (frame 137)
- pcap child id request: `04:07:37.689` (frame 139)
- pcap child id response: `04:07:37.703` (frame 141)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `04:07:37.623`
- log parent response: `04:07:37.636`
- log child id request: `04:07:37.655`
- log child id response: `04:07:37.685`
- parent ipv6: `n/a`
- parent extaddr: `329febdbc13a9a7b`
- parent rloc16: `0xe000`
- child extaddr: `22d0f9c4959da25b`
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

### `ucast_fastpr_child_20260706-041340-run13.log`

- manifest status: `completed`
- child extaddr: `72cbb6a7356a1e3f`
- switch target extaddr(s): `56b42dda7bad5488, 56b42dda7bad5488, 56b42dda7bad5488`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `9a2a6bedaa722ec3`
- parent rloc16: `n/a`
- child extaddr: `72cbb6a7356a1e3f`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **280 ms**
- Response -> Child ID Request: **473 ms**
- Child ID Request -> Response: **13 ms**
- Full Attach: **766 ms**
- pcap parent request: `04:19:24.980` (frame 128)
- pcap parent response: `04:19:25.260` (frame 129)
- pcap child id request: `04:19:25.733` (frame 135)
- pcap child id response: `04:19:25.746` (frame 137)

#### PCAP-complete child attach 2

- log parent request: `04:19:29.525`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `56b42dda7bad5488`
- parent rloc16: `n/a`
- child extaddr: `72cbb6a7356a1e3f`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **8 ms**
- Response -> Child ID Request: **33 ms**
- Child ID Request -> Response: **14 ms**
- Full Attach: **55 ms**
- pcap parent request: `04:19:29.573` (frame 140)
- pcap parent response: `04:19:29.581` (frame 142)
- pcap child id request: `04:19:29.614` (frame 144)
- pcap child id response: `04:19:29.628` (frame 146)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `04:19:29.546`
- log parent response: `04:19:29.560`
- log child id request: `04:19:29.579`
- log child id response: `04:19:29.609`
- parent ipv6: `n/a`
- parent extaddr: `56b42dda7bad5488`
- parent rloc16: `0x2c00`
- child extaddr: `72cbb6a7356a1e3f`
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

### `ucast_fastpr_child_20260706-042532-run14.log`

- manifest status: `completed`
- child extaddr: `0e3a4872b7a87f78`
- switch target extaddr(s): `66909c39c64cf8da, 66909c39c64cf8da, 66909c39c64cf8da`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `928c017463c6216b`
- parent rloc16: `n/a`
- child extaddr: `0e3a4872b7a87f78`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **249 ms**
- Response -> Child ID Request: **504 ms**
- Child ID Request -> Response: **13 ms**
- Full Attach: **766 ms**
- pcap parent request: `04:31:17.214` (frame 126)
- pcap parent response: `04:31:17.463` (frame 127)
- pcap child id request: `04:31:17.967` (frame 133)
- pcap child id response: `04:31:17.980` (frame 135)

#### PCAP-complete child attach 2

- log parent request: `04:31:21.337`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `66909c39c64cf8da`
- parent rloc16: `n/a`
- child extaddr: `0e3a4872b7a87f78`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **8 ms**
- Response -> Child ID Request: **34 ms**
- Child ID Request -> Response: **14 ms**
- Full Attach: **56 ms**
- pcap parent request: `04:31:21.382` (frame 137)
- pcap parent response: `04:31:21.390` (frame 139)
- pcap child id request: `04:31:21.424` (frame 141)
- pcap child id response: `04:31:21.438` (frame 143)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `04:31:21.357`
- log parent response: `04:31:21.370`
- log child id request: `04:31:21.389`
- log child id response: `04:31:21.420`
- parent ipv6: `n/a`
- parent extaddr: `66909c39c64cf8da`
- parent rloc16: `0xc400`
- child extaddr: `0e3a4872b7a87f78`
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

### `ucast_fastpr_child_20260706-043723-run15.log`

- manifest status: `completed`
- child extaddr: `96e60dc159fdd3a8`
- switch target extaddr(s): `da68d282d0e32d6f, da68d282d0e32d6f, da68d282d0e32d6f`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `36f0d2c9dc37a9de`
- parent rloc16: `n/a`
- child extaddr: `96e60dc159fdd3a8`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **35 ms**
- Response -> Child ID Request: **717 ms**
- Child ID Request -> Response: **14 ms**
- Full Attach: **766 ms**
- pcap parent request: `04:43:09.090` (frame 126)
- pcap parent response: `04:43:09.125` (frame 127)
- pcap child id request: `04:43:09.842` (frame 133)
- pcap child id response: `04:43:09.856` (frame 135)

#### PCAP-complete child attach 2

- log parent request: `04:43:13.246`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `da68d282d0e32d6f`
- parent rloc16: `n/a`
- child extaddr: `96e60dc159fdd3a8`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **10 ms**
- Response -> Child ID Request: **29 ms**
- Child ID Request -> Response: **14 ms**
- Full Attach: **53 ms**
- pcap parent request: `04:43:13.292` (frame 137)
- pcap parent response: `04:43:13.302` (frame 139)
- pcap child id request: `04:43:13.331` (frame 141)
- pcap child id response: `04:43:13.345` (frame 143)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `04:43:13.264`
- log parent response: `04:43:13.281`
- log child id request: `04:43:13.297`
- log child id response: `04:43:13.326`
- parent ipv6: `n/a`
- parent extaddr: `da68d282d0e32d6f`
- parent rloc16: `0xf400`
- child extaddr: `96e60dc159fdd3a8`
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

### `ucast_fastpr_child_20260706-044915-run16.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `22e9132b32415aef`
- switch target extaddr(s): `c6bef3d1fef5064d, c6bef3d1fef5064d, c6bef3d1fef5064d`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `927f5828048c58b0`
- parent rloc16: `n/a`
- child extaddr: `22e9132b32415aef`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **307 ms**
- Response -> Child ID Request: **446 ms**
- Child ID Request -> Response: **14 ms**
- Full Attach: **767 ms**
- pcap parent request: `04:55:00.662` (frame 132)
- pcap parent response: `04:55:00.969` (frame 133)
- pcap child id request: `04:55:01.415` (frame 139)
- pcap child id response: `04:55:01.429` (frame 141)

#### PCAP-complete child attach 2

- log parent request: `04:55:05.217`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `c6bef3d1fef5064d`
- parent rloc16: `n/a`
- child extaddr: `22e9132b32415aef`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **10 ms**
- Response -> Child ID Request: **30 ms**
- Child ID Request -> Response: **13 ms**
- Full Attach: **53 ms**
- pcap parent request: `04:55:05.262` (frame 146)
- pcap parent response: `04:55:05.272` (frame 148)
- pcap child id request: `04:55:05.302` (frame 150)
- pcap child id response: `04:55:05.315` (frame 152)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `04:55:05.236`
- log parent response: `04:55:05.251`
- log child id request: `04:55:05.268`
- log child id response: `04:55:05.296`
- parent ipv6: `n/a`
- parent extaddr: `c6bef3d1fef5064d`
- parent rloc16: `0xbc00`
- child extaddr: `22e9132b32415aef`
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

### `ucast_fastpr_child_20260706-050107-run17.log`

- manifest status: `completed`
- child extaddr: `96c2d0102e25e3b3`
- switch target extaddr(s): `3635c7c7b155ebbf, 3635c7c7b155ebbf, 3635c7c7b155ebbf`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `82a4765094a726c5`
- parent rloc16: `n/a`
- child extaddr: `96c2d0102e25e3b3`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **183 ms**
- Response -> Child ID Request: **568 ms**
- Child ID Request -> Response: **15 ms**
- Full Attach: **766 ms**
- pcap parent request: `05:06:52.307` (frame 125)
- pcap parent response: `05:06:52.490` (frame 126)
- pcap child id request: `05:06:53.058` (frame 132)
- pcap child id response: `05:06:53.073` (frame 134)

#### PCAP-complete child attach 2

- log parent request: `05:06:56.911`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `3635c7c7b155ebbf`
- parent rloc16: `n/a`
- child extaddr: `96c2d0102e25e3b3`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **9 ms**
- Response -> Child ID Request: **32 ms**
- Child ID Request -> Response: **15 ms**
- Full Attach: **56 ms**
- pcap parent request: `05:06:56.959` (frame 136)
- pcap parent response: `05:06:56.968` (frame 138)
- pcap child id request: `05:06:57.000` (frame 140)
- pcap child id response: `05:06:57.015` (frame 142)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `05:06:56.932`
- log parent response: `05:06:56.946`
- log child id request: `05:06:56.965`
- log child id response: `05:06:56.995`
- parent ipv6: `n/a`
- parent extaddr: `3635c7c7b155ebbf`
- parent rloc16: `0x4800`
- child extaddr: `96c2d0102e25e3b3`
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

### `ucast_fastpr_child_20260706-051259-run18.log`

- manifest status: `completed`
- child extaddr: `7eb495d7fa840ace`
- switch target extaddr(s): `9eb3c71c2dc01ead, 9eb3c71c2dc01ead, 9eb3c71c2dc01ead`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `cef1c816fc474aee`
- parent rloc16: `n/a`
- child extaddr: `7eb495d7fa840ace`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **212 ms**
- Response -> Child ID Request: **541 ms**
- Child ID Request -> Response: **13 ms**
- Full Attach: **766 ms**
- pcap parent request: `05:18:44.437` (frame 133)
- pcap parent response: `05:18:44.649` (frame 134)
- pcap child id request: `05:18:45.190` (frame 140)
- pcap child id response: `05:18:45.203` (frame 142)

#### PCAP-complete child attach 2

- log parent request: `05:18:48.678`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `9eb3c71c2dc01ead`
- parent rloc16: `n/a`
- child extaddr: `7eb495d7fa840ace`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **9 ms**
- Response -> Child ID Request: **30 ms**
- Child ID Request -> Response: **12 ms**
- Full Attach: **51 ms**
- pcap parent request: `05:18:48.722` (frame 144)
- pcap parent response: `05:18:48.731` (frame 146)
- pcap child id request: `05:18:48.761` (frame 148)
- pcap child id response: `05:18:48.773` (frame 150)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `05:18:48.697`
- log parent response: `05:18:48.710`
- log child id request: `05:18:48.727`
- log child id response: `05:18:48.755`
- parent ipv6: `n/a`
- parent extaddr: `9eb3c71c2dc01ead`
- parent rloc16: `0xe800`
- child extaddr: `7eb495d7fa840ace`
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

### `ucast_fastpr_child_20260706-052451-run19.log`

- manifest status: `completed`
- child extaddr: `9a75edd6e376bd53`
- switch target extaddr(s): `2ef2741c1622c27a, 2ef2741c1622c27a, 2ef2741c1622c27a`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `22f01e1557158a8d`
- parent rloc16: `n/a`
- child extaddr: `9a75edd6e376bd53`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **125 ms**
- Response -> Child ID Request: **628 ms**
- Child ID Request -> Response: **14 ms**
- Full Attach: **767 ms**
- pcap parent request: `05:30:36.534` (frame 124)
- pcap parent response: `05:30:36.659` (frame 125)
- pcap child id request: `05:30:37.287` (frame 131)
- pcap child id response: `05:30:37.301` (frame 133)

#### PCAP-complete child attach 2

- log parent request: `05:30:40.621`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `2ef2741c1622c27a`
- parent rloc16: `n/a`
- child extaddr: `9a75edd6e376bd53`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **9 ms**
- Response -> Child ID Request: **34 ms**
- Child ID Request -> Response: **15 ms**
- Full Attach: **58 ms**
- pcap parent request: `05:30:40.669` (frame 135)
- pcap parent response: `05:30:40.678` (frame 137)
- pcap child id request: `05:30:40.712` (frame 139)
- pcap child id response: `05:30:40.727` (frame 141)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `05:30:40.642`
- log parent response: `05:30:40.657`
- log child id request: `05:30:40.676`
- log child id response: `05:30:40.708`
- parent ipv6: `n/a`
- parent extaddr: `2ef2741c1622c27a`
- parent rloc16: `0x5c00`
- child extaddr: `9a75edd6e376bd53`
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

### `ucast_fastpr_child_20260706-053643-run20.log`

- manifest status: `completed`
- child extaddr: `26b4d9f9604dd623`
- switch target extaddr(s): `be7c2a8ff6f39ae9, be7c2a8ff6f39ae9, be7c2a8ff6f39ae9`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `5ec7791bd0ff1a9d`
- parent rloc16: `n/a`
- child extaddr: `26b4d9f9604dd623`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **31 ms**
- Response -> Child ID Request: **719 ms**
- Child ID Request -> Response: **13 ms**
- Full Attach: **763 ms**
- pcap parent request: `05:42:28.380` (frame 130)
- pcap parent response: `05:42:28.411` (frame 131)
- pcap child id request: `05:42:29.130` (frame 137)
- pcap child id response: `05:42:29.143` (frame 139)

#### PCAP-complete child attach 2

- log parent request: `05:42:32.398`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `be7c2a8ff6f39ae9`
- parent rloc16: `n/a`
- child extaddr: `26b4d9f9604dd623`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **7 ms**
- Response -> Child ID Request: **34 ms**
- Child ID Request -> Response: **14 ms**
- Full Attach: **55 ms**
- pcap parent request: `05:42:32.445` (frame 142)
- pcap parent response: `05:42:32.452` (frame 144)
- pcap child id request: `05:42:32.486` (frame 146)
- pcap child id response: `05:42:32.500` (frame 148)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `05:42:32.418`
- log parent response: `05:42:32.432`
- log child id request: `05:42:32.451`
- log child id response: `05:42:32.483`
- parent ipv6: `n/a`
- parent extaddr: `be7c2a8ff6f39ae9`
- parent rloc16: `0xe800`
- child extaddr: `26b4d9f9604dd623`
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
