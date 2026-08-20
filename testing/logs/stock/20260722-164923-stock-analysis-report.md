# Child Log Analysis

## stock_child

Files analyzed: **1**

- batch folders: `stock`

### PCAP-complete child attach summary

| Attach | Metric | M (SD), ms | n |
| --- | --- | ---: | ---: |
| 1 | Request -> Response | 328.45 (0.00) | 1 |
| 1 | Response -> Child ID Request | 422.56 (0.00) | 1 |
| 1 | Child ID Request -> Response | 12.95 (0.00) | 1 |
| 1 | Full Attach | 763.96 (0.00) | 1 |
| 2 | Request -> Response | 34.43 (0.00) | 1 |
| 2 | Response -> Child ID Request | 717.57 (0.00) | 1 |
| 2 | Child ID Request -> Response | 14.47 (0.00) | 1 |
| 2 | Full Attach | 766.47 (0.00) | 1 |

| Metric | M (SD) | n |
| --- | ---: | ---: |
| Failed TX Attempts per Log | 0.00 (0.00) | 1 |
| Log-only or Partial Sequences per Log | 0.00 (0.00) | 1 |

### `stock_child_20260722-164923.log`

- manifest status: `completed`
- child extaddr: `6eef9f009e7b5d90`

#### Firmware Provenance

| Field | Value |
| --- | --- |
| PLATFORMIO_CORE_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock` |
| PLATFORMIO_PACKAGES_DIR | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock/packages` |
| OpenThread core | `/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent/testing/.platformio-core/stock/packages/framework-espidf/components/openthread/openthread/src/core` |
| mle_ftd.cpp SHA-256 | `2f7071c89b0230d98eb36bdea1089514467b0ca5849d9a0bf1ff802e5253fa8b` |
| fast unicast Parent Response marker | `False` |
| expected for variant | `False` |
| contamination check | `PASS` |

#### PCAP-complete child attach 1

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `8e0be12a97c07be5`
- parent rloc16: `n/a`
- child extaddr: `6eef9f009e7b5d90`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **328.449 ms**
- Response -> Child ID Request: **422.56 ms**
- Child ID Request -> Response: **12.95 ms**
- Full Attach: **763.959 ms**
- pcap parent request: `16:54:30.439` (frame 52)
- pcap parent response: `16:54:30.768` (frame 53)
- pcap child id request: `16:54:31.190` (frame 57)
- pcap child id response: `16:54:31.203` (frame 59)

#### PCAP-complete child attach 2

- log parent request: `n/a`
- log parent response: `n/a`
- log child id request: `n/a`
- log child id response: `n/a`
- parent ipv6: `n/a`
- parent extaddr: `82950e4001cb1ada`
- parent rloc16: `n/a`
- child extaddr: `6eef9f009e7b5d90`
- timing source: **pcap-csv-tlv-generated**
- complete log attach: **False**
- complete pcap attach: **True**
- Request -> Response: **34.434 ms**
- Response -> Child ID Request: **717.568 ms**
- Child ID Request -> Response: **14.47 ms**
- Full Attach: **766.472 ms**
- pcap parent request: `16:58:30.506` (frame 201)
- pcap parent response: `16:58:30.541` (frame 202)
- pcap child id request: `16:58:31.258` (frame 204)
- pcap child id response: `16:58:31.273` (frame 206)

#### Failed TX summary

- failed tx attempts: **0**
- highest attempt number seen: **0/0**
