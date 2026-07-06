# Child Log Analysis

## ucast_fastpr_child

Files analyzed: **3**

- batch folders: `ucast_fastpr-4router-3runs-20260703-020303`

### PCAP-complete child attach summary

| Attach | Metric | M (SD), ms | n |
| --- | --- | ---: | ---: |
| 1 | Request -> Response | 33.33 (21.08) | 3 |
| 1 | Response -> Child ID Request | 29.67 (1.15) | 3 |
| 1 | Child ID Request -> Response | 70.00 (52.72) | 3 |
| 1 | Full Attach | 133.00 (71.84) | 3 |

| Metric | M (SD) | n |
| --- | ---: | ---: |
| Failed TX Attempts per Log | 0.00 (0.00) | 3 |
| Log-only or Partial Sequences per Log | 1.00 (0.00) | 3 |

### `ucast_fastpr_child_20260703-020340-run01.log`

- manifest status: `completed`
- child extaddr: `n/a`
- switch target extaddr(s): `424a7bcc65316f1f, 424a7bcc65316f1f, 424a7bcc65316f1f`

#### PCAP-complete child attach 1

- log parent request: `02:09:34.443`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `424a7bcc65316f1f`
- parent rloc16: `n/a`
- child extaddr: `22fe85648f8d8062`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **46 ms**
- Response -> Child ID Request: **29 ms**
- Child ID Request -> Response: **83 ms**
- Full Attach: **158 ms**
- pcap parent request: `02:09:34.491` (frame 980)
- pcap parent response: `02:09:34.537` (frame 982)
- pcap child id request: `02:09:34.566` (frame 984)
- pcap child id response: `02:09:34.649` (frame 986)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `02:09:34.461`
- log parent response: `02:09:34.516`
- log child id request: `02:09:34.530`
- log child id response: `02:09:34.629`
- parent ipv6: `n/a`
- parent extaddr: `424a7bcc65316f1f`
- parent rloc16: `0xc800`
- child extaddr: `n/a`
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

### `ucast_fastpr_child_20260703-021537-run02.log`

- manifest status: `completed`
- child extaddr: `n/a`
- switch target extaddr(s): `caa42dc5fbe0c767, caa42dc5fbe0c767, caa42dc5fbe0c767`

#### PCAP-complete child attach 1

- log parent request: `02:21:31.933`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `caa42dc5fbe0c767`
- parent rloc16: `n/a`
- child extaddr: `367a2a484bb60414`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **9 ms**
- Response -> Child ID Request: **31 ms**
- Child ID Request -> Response: **12 ms**
- Full Attach: **52 ms**
- pcap parent request: `02:21:31.980` (frame 243)
- pcap parent response: `02:21:31.989` (frame 245)
- pcap child id request: `02:21:32.020` (frame 247)
- pcap child id response: `02:21:32.032` (frame 249)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `02:21:31.952`
- log parent response: `02:21:31.968`
- log child id request: `02:21:31.984`
- log child id response: `02:21:32.013`
- parent ipv6: `n/a`
- parent extaddr: `caa42dc5fbe0c767`
- parent rloc16: `0x3c00`
- child extaddr: `n/a`
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

### `ucast_fastpr_child_20260703-022734-run03.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `n/a`
- switch target extaddr(s): `92f4c167668d32e6, 92f4c167668d32e6, 92f4c167668d32e6`

#### PCAP-complete child attach 1

- log parent request: `02:33:29.165`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `92f4c167668d32e6`
- parent rloc16: `n/a`
- child extaddr: `b2c8648c06ebb6c1`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **45 ms**
- Response -> Child ID Request: **29 ms**
- Child ID Request -> Response: **115 ms**
- Full Attach: **189 ms**
- pcap parent request: `02:33:29.211` (frame 438)
- pcap parent response: `02:33:29.256` (frame 440)
- pcap child id request: `02:33:29.285` (frame 443)
- pcap child id response: `02:33:29.400` (frame 445)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `02:33:29.183`
- log parent response: `02:33:29.235`
- log child id request: `02:33:29.251`
- log child id response: `02:33:29.381`
- parent ipv6: `n/a`
- parent extaddr: `92f4c167668d32e6`
- parent rloc16: `0x8400`
- child extaddr: `n/a`
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
