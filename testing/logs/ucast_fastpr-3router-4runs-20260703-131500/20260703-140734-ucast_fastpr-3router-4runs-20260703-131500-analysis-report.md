# Child Log Analysis

## ucast_fastpr_child

Files analyzed: **4**

- batch folders: `ucast_fastpr-3router-4runs-20260703-131500`

### PCAP-complete child attach summary

| Attach | Metric | M (SD), ms | n |
| --- | --- | ---: | ---: |
| 1 | Request -> Response | 62.25 (20.12) | 4 |
| 1 | Response -> Child ID Request | 690.25 (19.26) | 4 |
| 1 | Child ID Request -> Response | 14.25 (0.96) | 4 |
| 1 | Full Attach | 766.75 (1.50) | 4 |
| 2 | Request -> Response | 48.75 (0.96) | 4 |
| 2 | Response -> Child ID Request | 28.75 (0.50) | 4 |
| 2 | Child ID Request -> Response | 92.75 (0.96) | 4 |
| 2 | Full Attach | 170.25 (0.96) | 4 |

| Metric | M (SD) | n |
| --- | ---: | ---: |
| Failed TX Attempts per Log | 0.00 (0.00) | 4 |
| Log-only or Partial Sequences per Log | 1.00 (0.00) | 4 |

### `ucast_fastpr_child_20260703-132003-run01.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `5edbd7096351c349`
- switch target extaddr(s): `6e20240e216a8cdf, 6e20240e216a8cdf, 6e20240e216a8cdf`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `7e1ecead2921848e`
- parent rloc16: `n/a`
- child extaddr: `5edbd7096351c349`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **63 ms**
- Response -> Child ID Request: **688 ms**
- Child ID Request -> Response: **15 ms**
- Full Attach: **766 ms**
- pcap parent request: `13:25:47.745` (frame 133)
- pcap parent response: `13:25:47.808` (frame 134)
- pcap child id request: `13:25:48.496` (frame 140)
- pcap child id response: `13:25:48.511` (frame 142)

#### PCAP-complete child attach 2

- log parent request: `13:25:51.887`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `6e20240e216a8cdf`
- parent rloc16: `n/a`
- child extaddr: `5edbd7096351c349`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **48 ms**
- Response -> Child ID Request: **29 ms**
- Child ID Request -> Response: **92 ms**
- Full Attach: **169 ms**
- pcap parent request: `13:25:51.933` (frame 144)
- pcap parent response: `13:25:51.981` (frame 146)
- pcap child id request: `13:25:52.010` (frame 148)
- pcap child id response: `13:25:52.102` (frame 150)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `13:25:51.906`
- log parent response: `13:25:51.960`
- log child id request: `13:25:51.975`
- log child id response: `13:25:52.083`
- parent ipv6: `n/a`
- parent extaddr: `6e20240e216a8cdf`
- parent rloc16: `0xb400`
- child extaddr: `5edbd7096351c349`
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

### `ucast_fastpr_child_20260703-133154-run02.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `ca6214766e262c8b`
- switch target extaddr(s): `ba579a70fa6e0743, ba579a70fa6e0743, ba579a70fa6e0743`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `e24c82cc62fb4809`
- parent rloc16: `n/a`
- child extaddr: `ca6214766e262c8b`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **85 ms**
- Response -> Child ID Request: **668 ms**
- Child ID Request -> Response: **13 ms**
- Full Attach: **766 ms**
- pcap parent request: `13:37:39.349` (frame 127)
- pcap parent response: `13:37:39.434` (frame 128)
- pcap child id request: `13:37:40.102` (frame 134)
- pcap child id response: `13:37:40.115` (frame 136)

#### PCAP-complete child attach 2

- log parent request: `13:37:43.975`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `ba579a70fa6e0743`
- parent rloc16: `n/a`
- child extaddr: `ca6214766e262c8b`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **50 ms**
- Response -> Child ID Request: **28 ms**
- Child ID Request -> Response: **93 ms**
- Full Attach: **171 ms**
- pcap parent request: `13:37:44.020` (frame 138)
- pcap parent response: `13:37:44.070` (frame 140)
- pcap child id request: `13:37:44.098` (frame 142)
- pcap child id response: `13:37:44.191` (frame 144)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `13:37:43.993`
- log parent response: `13:37:44.050`
- log child id request: `13:37:44.064`
- log child id response: `13:37:44.173`
- parent ipv6: `n/a`
- parent extaddr: `ba579a70fa6e0743`
- parent rloc16: `0x1c00`
- child extaddr: `ca6214766e262c8b`
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

### `ucast_fastpr_child_20260703-134346-run03.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `b2648796be2d3f18`
- switch target extaddr(s): `0a01ee997399959b, 0a01ee997399959b, 0a01ee997399959b`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `8a3f02516ab155dd`
- parent rloc16: `n/a`
- child extaddr: `b2648796be2d3f18`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **36 ms**
- Response -> Child ID Request: **715 ms**
- Child ID Request -> Response: **15 ms**
- Full Attach: **766 ms**
- pcap parent request: `13:49:31.817` (frame 128)
- pcap parent response: `13:49:31.853` (frame 129)
- pcap child id request: `13:49:32.568` (frame 135)
- pcap child id response: `13:49:32.583` (frame 137)

#### PCAP-complete child attach 2

- log parent request: `13:49:36.111`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `0a01ee997399959b`
- parent rloc16: `n/a`
- child extaddr: `b2648796be2d3f18`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **49 ms**
- Response -> Child ID Request: **29 ms**
- Child ID Request -> Response: **92 ms**
- Full Attach: **170 ms**
- pcap parent request: `13:49:36.155` (frame 139)
- pcap parent response: `13:49:36.204` (frame 141)
- pcap child id request: `13:49:36.233` (frame 143)
- pcap child id response: `13:49:36.325` (frame 145)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `13:49:36.129`
- log parent response: `13:49:36.185`
- log child id request: `13:49:36.200`
- log child id response: `13:49:36.308`
- parent ipv6: `n/a`
- parent extaddr: `0a01ee997399959b`
- parent rloc16: `0xf800`
- child extaddr: `b2648796be2d3f18`
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

### `ucast_fastpr_child_20260703-135538-run04.log`

- manifest status: `completed`
- child extaddr: `deb3faafdf8a7cfe`
- switch target extaddr(s): `467fe556b7ee5aa1, 467fe556b7ee5aa1, 467fe556b7ee5aa1`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `8a25c2b8d1189103`
- parent rloc16: `n/a`
- child extaddr: `deb3faafdf8a7cfe`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **65 ms**
- Response -> Child ID Request: **690 ms**
- Child ID Request -> Response: **14 ms**
- Full Attach: **769 ms**
- pcap parent request: `14:01:23.548` (frame 127)
- pcap parent response: `14:01:23.613` (frame 128)
- pcap child id request: `14:01:24.303` (frame 134)
- pcap child id response: `14:01:24.317` (frame 136)

#### PCAP-complete child attach 2

- log parent request: `14:01:28.128`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `467fe556b7ee5aa1`
- parent rloc16: `n/a`
- child extaddr: `deb3faafdf8a7cfe`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **48 ms**
- Response -> Child ID Request: **29 ms**
- Child ID Request -> Response: **94 ms**
- Full Attach: **171 ms**
- pcap parent request: `14:01:28.173` (frame 140)
- pcap parent response: `14:01:28.221` (frame 142)
- pcap child id request: `14:01:28.250` (frame 144)
- pcap child id response: `14:01:28.344` (frame 146)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `14:01:28.147`
- log parent response: `14:01:28.201`
- log child id request: `14:01:28.216`
- log child id response: `14:01:28.327`
- parent ipv6: `n/a`
- parent extaddr: `467fe556b7ee5aa1`
- parent rloc16: `0x6800`
- child extaddr: `deb3faafdf8a7cfe`
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
