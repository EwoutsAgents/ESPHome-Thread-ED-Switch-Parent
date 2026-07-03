# Child Log Analysis

## ucast_fastpr_child

Files analyzed: **4**

- batch folders: `ucast_fastpr-2router-4runs-20260703-184553`

### PCAP-complete child attach summary

| Attach | Metric | M (SD), ms | n |
| --- | --- | ---: | ---: |
| 1 | Request -> Response | 93.25 (86.77) | 4 |
| 1 | Response -> Child ID Request | 659.25 (87.53) | 4 |
| 1 | Child ID Request -> Response | 14.25 (0.96) | 4 |
| 1 | Full Attach | 766.75 (2.06) | 4 |
| 2 | Request -> Response | 9.00 (1.41) | 4 |
| 2 | Response -> Child ID Request | 33.75 (0.50) | 4 |
| 2 | Child ID Request -> Response | 13.75 (0.96) | 4 |
| 2 | Full Attach | 56.50 (1.91) | 4 |

| Metric | M (SD) | n |
| --- | ---: | ---: |
| Failed TX Attempts per Log | 0.00 (0.00) | 4 |
| Log-only or Partial Sequences per Log | 1.00 (0.00) | 4 |

### `ucast_fastpr_child_20260703-184949-run01.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `ea16e5885a51c305`
- switch target extaddr(s): `f6e16678916553fc, f6e16678916553fc, f6e16678916553fc`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `9a6ccae0c102b059`
- parent rloc16: `n/a`
- child extaddr: `ea16e5885a51c305`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **15 ms**
- Response -> Child ID Request: **737 ms**
- Child ID Request -> Response: **15 ms**
- Full Attach: **767 ms**
- pcap parent request: `18:55:30.052` (frame 79)
- pcap parent response: `18:55:30.067` (frame 80)
- pcap child id request: `18:55:30.804` (frame 84)
- pcap child id response: `18:55:30.819` (frame 86)

#### PCAP-complete child attach 2

- log parent request: `18:55:34.323`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `f6e16678916553fc`
- parent rloc16: `n/a`
- child extaddr: `ea16e5885a51c305`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **10 ms**
- Response -> Child ID Request: **33 ms**
- Child ID Request -> Response: **15 ms**
- Full Attach: **58 ms**
- pcap parent request: `18:55:34.369` (frame 90)
- pcap parent response: `18:55:34.379` (frame 92)
- pcap child id request: `18:55:34.412` (frame 94)
- pcap child id response: `18:55:34.427` (frame 96)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `18:55:34.343`
- log parent response: `18:55:34.358`
- log child id request: `18:55:34.377`
- log child id response: `18:55:34.408`
- parent ipv6: `n/a`
- parent extaddr: `f6e16678916553fc`
- parent rloc16: `0xf800`
- child extaddr: `ea16e5885a51c305`
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

### `ucast_fastpr_child_20260703-190136-run02.log`

- manifest status: `completed`
- child extaddr: `bab5326ab4f6f975`
- switch target extaddr(s): `621b0a42787e4e88, 621b0a42787e4e88, 621b0a42787e4e88`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `6eb874f5813d6a31`
- parent rloc16: `n/a`
- child extaddr: `bab5326ab4f6f975`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **129 ms**
- Response -> Child ID Request: **624 ms**
- Child ID Request -> Response: **14 ms**
- Full Attach: **767 ms**
- pcap parent request: `19:07:17.339` (frame 75)
- pcap parent response: `19:07:17.468` (frame 76)
- pcap child id request: `19:07:18.092` (frame 80)
- pcap child id response: `19:07:18.106` (frame 82)

#### PCAP-complete child attach 2

- log parent request: `19:07:21.509`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `621b0a42787e4e88`
- parent rloc16: `n/a`
- child extaddr: `bab5326ab4f6f975`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **10 ms**
- Response -> Child ID Request: **34 ms**
- Child ID Request -> Response: **14 ms**
- Full Attach: **58 ms**
- pcap parent request: `19:07:21.556` (frame 85)
- pcap parent response: `19:07:21.566` (frame 87)
- pcap child id request: `19:07:21.600` (frame 89)
- pcap child id response: `19:07:21.614` (frame 91)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `19:07:21.529`
- log parent response: `19:07:21.544`
- log child id request: `19:07:21.563`
- log child id response: `19:07:21.594`
- parent ipv6: `n/a`
- parent extaddr: `621b0a42787e4e88`
- parent rloc16: `0x0c00`
- child extaddr: `bab5326ab4f6f975`
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

### `ucast_fastpr_child_20260703-191324-run03.log`

- manifest status: `completed`
- child extaddr: `0a6a29944a11dd56`
- switch target extaddr(s): `26052b560b98c447, 26052b560b98c447, 26052b560b98c447`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `1e0cc8ac1ad2af97`
- parent rloc16: `n/a`
- child extaddr: `0a6a29944a11dd56`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **30 ms**
- Response -> Child ID Request: **724 ms**
- Child ID Request -> Response: **15 ms**
- Full Attach: **769 ms**
- pcap parent request: `19:19:04.461` (frame 74)
- pcap parent response: `19:19:04.491` (frame 75)
- pcap child id request: `19:19:05.215` (frame 79)
- pcap child id response: `19:19:05.230` (frame 81)

#### PCAP-complete child attach 2

- log parent request: `19:19:08.530`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `26052b560b98c447`
- parent rloc16: `n/a`
- child extaddr: `0a6a29944a11dd56`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **9 ms**
- Response -> Child ID Request: **34 ms**
- Child ID Request -> Response: **13 ms**
- Full Attach: **56 ms**
- pcap parent request: `19:19:08.578` (frame 85)
- pcap parent response: `19:19:08.587` (frame 87)
- pcap child id request: `19:19:08.621` (frame 89)
- pcap child id response: `19:19:08.634` (frame 91)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `19:19:08.549`
- log parent response: `19:19:08.567`
- log child id request: `19:19:08.586`
- log child id response: `19:19:08.616`
- parent ipv6: `n/a`
- parent extaddr: `26052b560b98c447`
- parent rloc16: `0x8800`
- child extaddr: `0a6a29944a11dd56`
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

### `ucast_fastpr_child_20260703-192511-run04.log`

- manifest status: `completed`
- child extaddr: `6eb5967b0d70515b`
- switch target extaddr(s): `02f9566d00b1823d, 02f9566d00b1823d, 02f9566d00b1823d`

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `26bdc842c0fe4327`
- parent rloc16: `n/a`
- child extaddr: `6eb5967b0d70515b`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **199 ms**
- Response -> Child ID Request: **552 ms**
- Child ID Request -> Response: **13 ms**
- Full Attach: **764 ms**
- pcap parent request: `19:30:51.277` (frame 79)
- pcap parent response: `19:30:51.476` (frame 80)
- pcap child id request: `19:30:52.028` (frame 84)
- pcap child id response: `19:30:52.041` (frame 86)

#### PCAP-complete child attach 2

- log parent request: `19:30:55.487`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `02f9566d00b1823d`
- parent rloc16: `n/a`
- child extaddr: `6eb5967b0d70515b`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **7 ms**
- Response -> Child ID Request: **34 ms**
- Child ID Request -> Response: **13 ms**
- Full Attach: **54 ms**
- pcap parent request: `19:30:55.536` (frame 90)
- pcap parent response: `19:30:55.543` (frame 92)
- pcap child id request: `19:30:55.577` (frame 94)
- pcap child id response: `19:30:55.590` (frame 96)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `19:30:55.507`
- log parent response: `19:30:55.522`
- log child id request: `19:30:55.541`
- log child id response: `19:30:55.571`
- parent ipv6: `n/a`
- parent extaddr: `02f9566d00b1823d`
- parent rloc16: `0x1800`
- child extaddr: `6eb5967b0d70515b`
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
