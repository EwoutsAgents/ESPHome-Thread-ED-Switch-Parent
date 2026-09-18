# Hardware map

The campaigns retained the same ESP32-C6 assignment:

- Router 1: `58:8C:81:5D:B0:C4`
- Child: `58:8C:81:5D:B0:E0`
- Router 2: `58:8C:81:5D:B1:54`
- Router 3: `58:8C:81:5F:D8:C4`
- Router 4: `58:8C:81:5F:D9:28`

Packet captures were collected through the `rpi-802154-sniffer` host. Run manifests record the complete serial paths, configurations, isolated PlatformIO paths, firmware hashes, and role mapping.

For `stock-low-power`, routers 1 and 2 use 0 dBm output power; routers 3 and 4 use -15 dBm.
