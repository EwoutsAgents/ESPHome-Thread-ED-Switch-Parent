# Child Log Analysis

## ucast_fastpr_child

Files analyzed: **1**

- batch folders: `ucast_fastpr-4router-1runs-20260628-041905`

### PCAP-complete child attach summary

| Attach | Metric | M (SD), ms | n |
| --- | --- | ---: | ---: |
| 1 | Request -> Response | 44.00 (0.00) | 1 |
| 1 | Response -> Child ID Request | 706.00 (0.00) | 1 |
| 1 | Child ID Request -> Response | 64.00 (0.00) | 1 |
| 1 | Full Attach | 814.00 (0.00) | 1 |
| 2 | Request -> Response | 45.00 (0.00) | 1 |
| 2 | Response -> Child ID Request | 79.00 (0.00) | 1 |
| 2 | Child ID Request -> Response | 70.00 (0.00) | 1 |
| 2 | Full Attach | 194.00 (0.00) | 1 |

| Metric | M (SD) | n |
| --- | ---: | ---: |
| Failed TX Attempts per Log | 0.00 (0.00) | 1 |
| Log-only or Partial Sequences per Log | 0.00 (0.00) | 1 |

### `ucast_fastpr_child_20260628-041953-run01.log`

- manifest status: `completed`
- labels: `SKIP_PARENT_IS_LEADER`
- child extaddr: `322adc24274911d4`
- switch target extaddr(s): `fa022c1a2605dcdc, fa022c1a2605dcdc, fa022c1a2605dcdc`

#### PCAP-complete child attach 1

- log parent request: `04:25:44.194`
- log parent response: `04:25:44.238`
- log child id request: `04:25:44.914`
- log child id response: `04:25:45.001`
- parent ipv6: `fe80:0:0:0:88c5:d62c:b216:517b`
- parent extaddr: `8ac5d62cb216517b`
- parent rloc16: `0x2800`
- child extaddr: `322adc24274911d4`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **44 ms**
- Response -> Child ID Request: **706 ms**
- Child ID Request -> Response: **64 ms**
- Full Attach: **814 ms**
- pcap parent request: `04:25:44.191` (frame 183)
- pcap parent response: `04:25:44.235` (frame 184)
- pcap child id request: `04:25:44.941` (frame 193)
- pcap child id response: `04:25:45.005` (frame 195)

#### PCAP-complete child attach 2

- log parent request: `04:25:48.469`
- log parent response: `04:25:48.564`
- log child id request: `04:25:48.609`
- log child id response: `04:25:48.703`
- parent ipv6: `fe80:0:0:0:f802:2c1a:2605:dcdc`
- parent extaddr: `fa022c1a2605dcdc`
- parent rloc16: `0xa400`
- child extaddr: `322adc24274911d4`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **True**
- complete pcap attach: **True**
- Request -> Response: **45 ms**
- Response -> Child ID Request: **79 ms**
- Child ID Request -> Response: **70 ms**
- Full Attach: **194 ms**
- pcap parent request: `04:25:48.515` (frame 198)
- pcap parent response: `04:25:48.560` (frame 200)
- pcap child id request: `04:25:48.639` (frame 202)
- pcap child id response: `04:25:48.709` (frame 204)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**
