---
title: 'Makerfabs MaTouch ESP32-P4 7": troubleshooting'
slug: troubleshooting
sidebar_position: 90
image: img/board-01.jpg
image_alt: Makerfabs MaTouch ESP32-P4 7"
tags:
- esp32-p4
- display
- touch
- hmi
- ethernet
- makerfabs
- troubleshooting
---

# Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| The COM port does not appear | The cable carries power only, or the CH340 driver is missing | Use a USB-C data cable; install the CH340 driver (WCH CH341SER); try another USB port. |
| The board restarts when the screen comes up | The supply cannot carry the backlight | Use a 5 V / 2 A supply or a powered USB hub. |
| The screen stays dark after the runtime was written | No project on the board yet | Download the project (F5); a board without a project shows nothing on the glass. |
| Touch does not respond, or responds in the wrong place | The project's orientation differs from the way the board is mounted | Set the orientation on the HMIview page and download again. |
| The network does not come up | No DHCP server, or no link on the port | Check the link LEDs on the jack; set a fixed address on the board page; for Wi-Fi check the network name and the password. |
| CAN stays silent | No transceiver, no 120 ohm termination, or a different bit rate | Check the transceiver on GPIO20 / GPIO21, a 120 ohm resistor at both ends of the bus, and the same bit rate on every node. |
| A Modbus RTU value stays at 0 | A, B swapped, a wrong unit or baud rate, or the DE pin missing | Swap A and B; check the unit, the baud rate and the parity; check that DE is wired and named. |

The editor's **Messages** pane and the board's **diagnostic buffer** (Online → Diagnostics) say what the runtime decided and why - read them first.

---

[← Example projects](examples/README.md) | [Overview](README.md)
