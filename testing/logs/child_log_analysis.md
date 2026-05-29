# Child Log Analysis

## stock_child

### Group summary

| Attach | Parent Request → Response (ms) | Parent Response → Child ID Req (ms) | Child ID Req → Response (ms) | Full attach (ms) | n |
| --- | ---: | ---: | ---: | ---: | ---: |
| 1 | 227.40 ± 119.64 | 518.00 ± 124.41 | 78.75 ± 0.50 | 825.20 ± 34.42 | 5 |
| 2 | 335.80 ± 66.72 | 456.00 ± 0.00 | 79.00 ± 0.00 | 790.20 ± 0.84 | 5 |

| Failed TX attempts per log | n |
| ---: | ---: |
| 64.00 ± 0.00 | 5 |

### `stock_child_20260529-134804.log`

#### Attach sequence 1

- parent request: `13:48:04.629`
- parent response: `13:48:04.959`
- child id request: `13:48:05.401`
- child id response: `13:48:05.480`
- parent ipv6: `fe80:0:0:0:2463:4d1a:7d18:34b5`
- parent extaddr: `26634d1a7d1834b5`
- parent rloc16: `0xcc00`
- request -> response: **330 ms**
- response -> child id request: **442 ms**
- child id request -> response: **79 ms**
- full attach quartet: **851 ms**

#### Attach sequence 2

- parent request: `13:52:05.546`
- parent response: `13:52:05.802`
- child id request: `13:52:06.258`
- child id response: `13:52:06.337`
- parent ipv6: `fe80:0:0:0:6876:c095:4bb4:31f0`
- parent extaddr: `6a76c0954bb431f0`
- parent rloc16: `0xe000`
- request -> response: **256 ms**
- response -> child id request: **456 ms**
- child id request -> response: **79 ms**
- full attach quartet: **791 ms**

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 138: 16, seq 139: 16, seq 140: 16, seq 141: 16
- failed tx by dst: `26634d1a7d1834b5`: 56

### `stock_child_20260529-172638.log`

#### Attach sequence 1

- parent request: `17:26:39.186`
- parent response: `17:26:39.562`
- child id request: `17:26:39.957`
- child id response: `17:26:40.036`
- parent ipv6: `fe80:0:0:0:f408:f30c:b9a3:42bb`
- parent extaddr: `f608f30cb9a342bb`
- parent rloc16: `0x1400`
- request -> response: **376 ms**
- response -> child id request: **395 ms**
- child id request -> response: **79 ms**
- full attach quartet: **850 ms**

#### Attach sequence 2

- parent request: `17:30:39.694`
- parent response: `17:30:40.121`
- child id request: `None`
- child id response: `17:30:40.483`
- parent ipv6: `fe80:0:0:0:64e7:dec6:a974:b8d8`
- parent extaddr: `66e7dec6a974b8d8`
- parent rloc16: `0x4400`
- request -> response: **427 ms**
- response -> child id request: **None ms**
- child id request -> response: **None ms**
- full attach quartet: **789 ms**

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 171: 16, seq 172: 16, seq 173: 16, seq 174: 16
- failed tx by dst: `f608f30cb9a342bb`: 53

### `stock_child_20260529-173408.log`

#### Attach sequence 1

- parent request: `17:34:09.161`
- parent response: `17:34:09.305`
- child id request: `17:34:09.869`
- child id response: `17:34:09.948`
- parent ipv6: `fe80:0:0:0:10e2:81a0:61e3:5b4a`
- parent extaddr: `12e281a061e35b4a`
- parent rloc16: `0xd400`
- request -> response: **144 ms**
- response -> child id request: **564 ms**
- child id request -> response: **79 ms**
- full attach quartet: **787 ms**

#### Attach sequence 2

- parent request: `17:38:10.308`
- parent response: `17:38:10.658`
- child id request: `None`
- child id response: `17:38:11.099`
- parent ipv6: `fe80:0:0:0:1c7e:1a3e:192c:6420`
- parent extaddr: `1e7e1a3e192c6420`
- parent rloc16: `0xc800`
- request -> response: **350 ms**
- response -> child id request: **None ms**
- child id request -> response: **None ms**
- full attach quartet: **791 ms**

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 118: 16, seq 119: 16, seq 120: 16, seq 121: 16
- failed tx by dst: `12e281a061e35b4a`: 57

### `stock_child_20260529-174138.log`

#### Attach sequence 1

- parent request: `17:41:39.264`
- parent response: `17:41:39.450`
- child id request: `None`
- child id response: `17:41:40.052`
- parent ipv6: `fe80:0:0:0:88e2:3f4:9e4c:df19`
- parent extaddr: `8ae203f49e4cdf19`
- parent rloc16: `0x1c00`
- request -> response: **186 ms**
- response -> child id request: **None ms**
- child id request -> response: **None ms**
- full attach quartet: **788 ms**

#### Attach sequence 2

- parent request: `17:45:39.822`
- parent response: `17:45:40.109`
- child id request: `None`
- child id response: `17:45:40.612`
- parent ipv6: `fe80:0:0:0:5895:4d1f:4810:f98`
- parent extaddr: `5a954d1f48100f98`
- parent rloc16: `0xa400`
- request -> response: **287 ms**
- response -> child id request: **None ms**
- child id request -> response: **None ms**
- full attach quartet: **790 ms**

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 239: 16, seq 240: 16, seq 241: 16, seq 242: 16
- failed tx by dst: `8ae203f49e4cdf19`: 58

### `stock_child_20260529-174908.log`

#### Attach sequence 1

- parent request: `17:49:09.544`
- parent response: `17:49:09.645`
- child id request: `17:49:10.316`
- child id response: `17:49:10.394`
- parent ipv6: `fe80:0:0:0:50d9:1d21:977f:729d`
- parent extaddr: `52d91d21977f729d`
- parent rloc16: `0x9000`
- request -> response: **101 ms**
- response -> child id request: **671 ms**
- child id request -> response: **78 ms**
- full attach quartet: **850 ms**

#### Attach sequence 2

- parent request: `17:53:10.275`
- parent response: `17:53:10.634`
- child id request: `None`
- child id response: `17:53:11.065`
- parent ipv6: `fe80:0:0:0:3c76:9423:294d:4c2`
- parent extaddr: `3e769423294d04c2`
- parent rloc16: `0x5000`
- request -> response: **359 ms**
- response -> child id request: **None ms**
- child id request -> response: **None ms**
- full attach quartet: **790 ms**

#### Failed TX summary

- failed tx attempts: **64**
- highest attempt number seen: **16/16**
- failed tx by seqnum: seq 193: 16, seq 194: 16, seq 195: 16, seq 196: 16
- failed tx by dst: `52d91d21977f729d`: 54
