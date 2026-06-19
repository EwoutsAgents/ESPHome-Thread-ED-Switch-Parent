# Child Log Analysis

## mcast_no_early_attach_child

Files analyzed: **9**

### PCAP-complete child attach summary

| Attach | Metric | M (SD), ms | n |
| --- | --- | ---: | ---: |
| 1 | Request -> Response | 270.11 (182.58) | 9 |
| 1 | Response -> Child ID Request | 471.00 (194.31) | 9 |
| 1 | Child ID Request -> Response | 63.89 (1.05) | 9 |
| 1 | Full Attach | 805.00 (16.53) | 9 |
| 2 | Request -> Response | 44.00 (0.00) | 1 |
| 2 | Response -> Child ID Request | 308.00 (0.00) | 1 |
| 2 | Child ID Request -> Response | 66.00 (0.00) | 1 |
| 2 | Full Attach | 418.00 (0.00) | 1 |

| Metric | M (SD) | n |
| --- | ---: | ---: |
| Failed TX Attempts per Log | 0.00 (0.00) | 9 |
| Log-only or Partial Sequences per Log | 0.67 (0.50) | 9 |

### `mcast_no_early_attach_child_20260618-220418.log`

- child extaddr: `7291b6b6b37c3cb8`
- switch target extaddr(s): `a6e0b8ab2066d1bc`

#### PCAP-complete child attach 1

- log parent request: `22:04:58.510`
- log parent response: `22:04:58.563`
- log child id request: `22:04:59.217`
- log child id response: `22:04:59.310`
- parent ipv6: `fe80:0:0:0:b06e:6306:cb5d:7ee0`
- parent extaddr: `b26e6306cb5d7ee0`
- parent rloc16: `0x4800`
- child extaddr: `7291b6b6b37c3cb8`
- timing source: **pcap**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **57 ms**
- Response -> Child ID Request: **694 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **814 ms**
- pcap parent request: `22:04:58.484` (frame 10)
- pcap parent response: `22:04:58.541` (frame 11)
- pcap child id request: `22:04:59.235` (frame 13)
- pcap child id response: `22:04:59.298` (frame 15)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `22:06:53.629`
- log parent response: `22:06:54.012`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `fe80:0:0:0:b06e:6306:cb5d:7ee0`
- parent extaddr: `b26e6306cb5d7ee0`
- parent rloc16: `0x4800`
- child extaddr: `7291b6b6b37c3cb8`
- timing source: **unavailable**
- complete log attach: **False**
- complete pcap attach: **False**
- Request -> Response: **None ms**
- Response -> Child ID Request: **None ms**
- Child ID Request -> Response: **None ms**
- Full Attach: **None ms**

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_no_early_attach_child_20260618-220952.log`

- child extaddr: `2a7e93c68473e736`
- switch target extaddr(s): `1a40bd7c25e76b17`

#### PCAP-complete child attach 1

- log parent request: `22:10:32.361`
- log parent response: `22:10:32.569`
- log child id request: `22:10:33.133`
- log child id response: `22:10:33.223`
- parent ipv6: `fe80:0:0:0:24b3:29a:6889:bbb5`
- parent extaddr: `26b3029a6889bbb5`
- parent rloc16: `0xd000`
- child extaddr: `2a7e93c68473e736`
- timing source: **pcap**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **149 ms**
- Response -> Child ID Request: **601 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **813 ms**
- pcap parent request: `22:10:32.397` (frame 10)
- pcap parent response: `22:10:32.546` (frame 11)
- pcap child id request: `22:10:33.147` (frame 13)
- pcap child id response: `22:10:33.210` (frame 15)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_no_early_attach_child_20260618-221526.log`

- child extaddr: `86cfdeb05548028a`
- switch target extaddr(s): `16702f40df61fc3a, 16702f40df61fc3a`

#### PCAP-complete child attach 1

- log parent request: `22:16:06.459`
- log parent response: `22:16:06.689`
- log child id request: `22:16:07.212`
- log child id response: `22:16:07.259`
- parent ipv6: `fe80:0:0:0:a076:bd8e:969e:c060`
- parent extaddr: `a276bd8e969ec060`
- parent rloc16: `0xb800`
- child extaddr: `86cfdeb05548028a`
- timing source: **pcap**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **234 ms**
- Response -> Child ID Request: **515 ms**
- Child ID Request -> Response: **65 ms**
- Full Attach: **814 ms**
- pcap parent request: `22:16:06.433` (frame 10)
- pcap parent response: `22:16:06.667` (frame 11)
- pcap child id request: `22:16:07.182` (frame 13)
- pcap child id response: `22:16:07.247` (frame 15)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `22:18:03.062`
- log parent response: `22:18:03.385`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `fe80:0:0:0:a076:bd8e:969e:c060`
- parent extaddr: `a276bd8e969ec060`
- parent rloc16: `0xb800`
- child extaddr: `86cfdeb05548028a`
- timing source: **unavailable**
- complete log attach: **False**
- complete pcap attach: **False**
- Request -> Response: **None ms**
- Response -> Child ID Request: **None ms**
- Child ID Request -> Response: **None ms**
- Full Attach: **None ms**

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_no_early_attach_child_20260618-222100.log`

- child extaddr: `4e086f7ce848fb55`
- switch target extaddr(s): `5a8860f9f9155f35`

#### PCAP-complete child attach 1

- log parent request: `22:21:40.405`
- log parent response: `22:21:40.975`
- log child id request: `22:21:41.177`
- log child id response: `22:21:41.267`
- parent ipv6: `fe80:0:0:0:2875:befc:dff5:bf29`
- parent extaddr: `2a75befcdff5bf29`
- parent rloc16: `0x5800`
- child extaddr: `4e086f7ce848fb55`
- timing source: **pcap**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **472 ms**
- Response -> Child ID Request: **238 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **774 ms**
- pcap parent request: `22:21:40.482` (frame 10)
- pcap parent response: `22:21:40.954` (frame 11)
- pcap child id request: `22:21:41.192` (frame 13)
- pcap child id response: `22:21:41.256` (frame 15)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `22:23:34.904`
- log parent response: `22:23:34.977`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `fe80:0:0:0:5888:60f9:f915:5f35`
- parent extaddr: `5a8860f9f9155f35`
- parent rloc16: `0x3000`
- child extaddr: `4e086f7ce848fb55`
- timing source: **unavailable**
- complete log attach: **False**
- complete pcap attach: **False**
- Request -> Response: **None ms**
- Response -> Child ID Request: **None ms**
- Child ID Request -> Response: **None ms**
- Full Attach: **None ms**

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_no_early_attach_child_20260618-222634.log`

- child extaddr: `5ef71ddb9dfa3f5f`
- switch target extaddr(s): `f23f3e565f067219`

#### PCAP-complete child attach 1

- log parent request: `22:27:14.583`
- log parent response: `22:27:14.949`
- log child id request: `22:27:15.293`
- log child id response: `22:27:15.383`
- parent ipv6: `fe80:0:0:0:d80d:838f:7239:a6d2`
- parent extaddr: `da0d838f7239a6d2`
- parent rloc16: `0x1800`
- child extaddr: `5ef71ddb9dfa3f5f`
- timing source: **pcap**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **369 ms**
- Response -> Child ID Request: **381 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **813 ms**
- pcap parent request: `22:27:14.557` (frame 10)
- pcap parent response: `22:27:14.926` (frame 11)
- pcap child id request: `22:27:15.307` (frame 13)
- pcap child id response: `22:27:15.370` (frame 15)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `22:29:09.259`
- log parent response: `22:29:09.510`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `fe80:0:0:0:d80d:838f:7239:a6d2`
- parent extaddr: `da0d838f7239a6d2`
- parent rloc16: `0x1800`
- child extaddr: `5ef71ddb9dfa3f5f`
- timing source: **unavailable**
- complete log attach: **False**
- complete pcap attach: **False**
- Request -> Response: **None ms**
- Response -> Child ID Request: **None ms**
- Child ID Request -> Response: **None ms**
- Full Attach: **None ms**

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_no_early_attach_child_20260618-223208.log`

- child extaddr: `7e9e2049c56ed831`
- switch target extaddr(s): `da55d9944b7def37, da55d9944b7def37`

#### PCAP-complete child attach 1

- log parent request: `22:32:48.456`
- log parent response: `22:32:48.990`
- log child id request: `22:32:49.228`
- log child id response: `22:32:49.319`
- parent ipv6: `fe80:0:0:0:b0b7:44c7:9899:1d3f`
- parent extaddr: `b2b744c798991d3f`
- parent rloc16: `0xa800`
- child extaddr: `7e9e2049c56ed831`
- timing source: **pcap**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **472 ms**
- Response -> Child ID Request: **275 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **811 ms**
- pcap parent request: `22:32:48.494` (frame 10)
- pcap parent response: `22:32:48.966` (frame 11)
- pcap child id request: `22:32:49.241` (frame 13)
- pcap child id response: `22:32:49.305` (frame 15)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_no_early_attach_child_20260618-223742.log`

- child extaddr: `6616c36ed90f6a9f`
- switch target extaddr(s): `b26f1928f1790ee5`

#### PCAP-complete child attach 1

- log parent request: `22:38:22.514`
- log parent response: `22:38:23.099`
- log child id request: `22:38:23.335`
- log child id response: `22:38:23.378`
- parent ipv6: `fe80:0:0:0:2028:f5f5:4a2e:76e7`
- parent extaddr: `2228f5f54a2e76e7`
- parent rloc16: `0x2000`
- child extaddr: `6616c36ed90f6a9f`
- timing source: **pcap**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **488 ms**
- Response -> Child ID Request: **226 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **778 ms**
- pcap parent request: `22:38:22.587` (frame 10)
- pcap parent response: `22:38:23.075` (frame 11)
- pcap child id request: `22:38:23.301` (frame 13)
- pcap child id response: `22:38:23.365` (frame 15)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `b26f1928f1790ee5`
- parent rloc16: `n/a`
- child extaddr: `6616c36ed90f6a9f`
- timing source: **pcap**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **44 ms**
- Response -> Child ID Request: **308 ms**
- Child ID Request -> Response: **66 ms**
- Full Attach: **418 ms**
- pcap parent request: `22:40:14.843` (frame 53)
- pcap parent response: `22:40:14.887` (frame 54)
- pcap child id request: `22:40:15.195` (frame 58)
- pcap child id response: `22:40:15.261` (frame 60)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_no_early_attach_child_20260618-224316.log`

- child extaddr: `824a937342c50ff6`
- switch target extaddr(s): `8ae4fab22c06fd8d`

#### PCAP-complete child attach 1

- log parent request: `22:43:56.893`
- log parent response: `22:43:57.036`
- log child id request: `22:43:57.603`
- log child id response: `22:43:57.693`
- parent ipv6: `fe80:0:0:0:e4e2:84c:b4c6:cd0f`
- parent extaddr: `e6e2084cb4c6cd0f`
- parent rloc16: `0x4000`
- child extaddr: `824a937342c50ff6`
- timing source: **pcap**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **146 ms**
- Response -> Child ID Request: **603 ms**
- Child ID Request -> Response: **63 ms**
- Full Attach: **812 ms**
- pcap parent request: `22:43:56.866` (frame 9)
- pcap parent response: `22:43:57.012` (frame 10)
- pcap child id request: `22:43:57.615` (frame 13)
- pcap child id response: `22:43:57.678` (frame 15)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `22:45:56.464`
- log parent response: `22:45:56.905`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `fe80:0:0:0:e4e2:84c:b4c6:cd0f`
- parent extaddr: `e6e2084cb4c6cd0f`
- parent rloc16: `0x4000`
- child extaddr: `824a937342c50ff6`
- timing source: **unavailable**
- complete log attach: **False**
- complete pcap attach: **False**
- Request -> Response: **None ms**
- Response -> Child ID Request: **None ms**
- Child ID Request -> Response: **None ms**
- Full Attach: **None ms**

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**

### `mcast_no_early_attach_child_20260618-224851.log`

- child extaddr: `f2385d19d656f481`
- switch target extaddr(s): `6e2253510b0ae7f5`

#### PCAP-complete child attach 1

- log parent request: `22:49:31.098`
- log parent response: `22:49:31.139`
- log child id request: `22:49:31.852`
- log child id response: `22:49:31.900`
- parent ipv6: `fe80:0:0:0:6430:fbda:4377:ad3e`
- parent extaddr: `6630fbda4377ad3e`
- parent rloc16: `0xf800`
- child extaddr: `f2385d19d656f481`
- timing source: **pcap**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **44 ms**
- Response -> Child ID Request: **706 ms**
- Child ID Request -> Response: **66 ms**
- Full Attach: **816 ms**
- pcap parent request: `22:49:31.071` (frame 9)
- pcap parent response: `22:49:31.115` (frame 10)
- pcap child id request: `22:49:31.821` (frame 13)
- pcap child id response: `22:49:31.887` (frame 15)

#### Log-only or partial sequences

These are not counted as completed attaches because they do not have a complete pcap sequence.

##### Not-counted sequence 1

- log parent request: `22:51:26.032`
- log parent response: `22:51:26.119`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `fe80:0:0:0:6430:fbda:4377:ad3e`
- parent extaddr: `6630fbda4377ad3e`
- parent rloc16: `0xf800`
- child extaddr: `f2385d19d656f481`
- timing source: **unavailable**
- complete log attach: **False**
- complete pcap attach: **False**
- Request -> Response: **None ms**
- Response -> Child ID Request: **None ms**
- Child ID Request -> Response: **None ms**
- Full Attach: **None ms**

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**
