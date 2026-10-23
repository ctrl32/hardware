---
title: 'Olimex ESP32-PoE: troubleshooting'
slug: troubleshooting
sidebar_position: 90
image: img/board-01.jpg
image_alt: Olimex ESP32-PoE
tags:
- esp32
- ethernet
- poe
- olimex
- troubleshooting
---

# Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| The COM port does not appear, the port picker stays empty | The cable carries power only, or the CH340 driver is missing | Use a data cable; install the CH340 driver (WCH CH341SER); try another USB port. |
| Flash runtime stops while connecting | Another program holds the port | Close the serial monitor or the other tool that has the port open, then try again. |
| The board restarts every few seconds | The USB port cannot supply the current while Ethernet starts | Use a powered USB hub or a 5 V supply of at least 1 A, or run the board on PoE (without USB). |
| The network does not come up | No DHCP server, or no link on the port | Check the link LEDs on the jack; set a fixed address on the Ethernet page; try another port of the switch. |
| The board is not found by its .local name | The network blocks mDNS (multicast) | Use the board's IP address - the router's list of clients and the editor's Find devices show it. |
| USB disconnects or the PC complains when the PoE cable is plugged in | USB and PoE connected at the same time on a board that is not isolated | Unplug one of them at once. Upload over USB first, then run on PoE - or use the ESP32-PoE-ISO. |
| An output on GPIO34 to GPIO39 does nothing | These pins are inputs only | Move the output to GPIO33, GPIO4 or GPIO5. |
| A Modbus value stays at 0 | The device address, the unit or the register is wrong, or the device is in another subnet | Check the device's IP and unit in the device tree and the register in the device's manual; ping the device from the PC. |

The editor's **Messages** pane and the board's **diagnostic buffer** (Online → Diagnostics) say what the runtime decided and why - read them first.

---

[← Example projects](examples/README.md) | [Overview](README.md)
