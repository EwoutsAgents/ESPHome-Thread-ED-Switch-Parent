# Child Log Analysis

## stock_child

### Group summary

- request -> response: avg **293.00 ms**, stdev **52.33 ms**, n=2
- response -> child id request: avg **449.00 ms**, stdev **9.90 ms**, n=2
- child id request -> response: avg **79.00 ms**, stdev **0.00 ms**, n=2
- full attach quartet: avg **821.00 ms**, stdev **42.43 ms**, n=2
- failed tx attempts per log: avg **64.00**, stdev **0.00**, n=1

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
