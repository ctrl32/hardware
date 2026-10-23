---
title: 'Olimex ESP32-POE2: troubleshooting'
slug: troubleshooting
sidebar_position: 90
image: img/board-01.jpg
image_alt: Olimex ESP32-POE2
tags:
- esp32
- ethernet
- poe
- psram
- olimex
- troubleshooting
---

# Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| The COM port does not appear, the port picker stays empty | The cable carries power only, or the USB driver is missing | Use a data cable; install the driver of the board's USB chip; try another USB port. |
| Flash runtime stops while connecting | Another program holds the port | Close the serial monitor or the other tool that has the port open, then try again. |
| The board restarts every few seconds | The USB port cannot supply the current | Use a powered USB hub or a 5 V supply of at least 1 A. |
| The network does not come up | No DHCP server, or no link on the port | Check the link LEDs on the jack; set a fixed address on the board page; try another port of the switch. |
| The board is not found by its .local name | The network blocks mDNS (multicast) | Use the board's IP address - the router's list of clients and the editor's Find devices show it. |
| An output does nothing | The pin is an input only, or the wrong pin was named | Check the pin on the board page - input-only pins are marked; move the output to a free I/O pin. |
| A Modbus value stays at 0 | The device address, the unit or the register is wrong | Check the device's IP and unit in the device tree and the register in the device's manual. |
| USB disconnects or the PC complains when the PoE cable is plugged in | USB and PoE connected at the same time on a board that is not isolated | Unplug one of them at once. Upload over USB first, then run on PoE. |
| The 24 V / 12 V output stays off | The board runs from USB - the outputs come from PoE only | Power the board over PoE (802.3at). |

The editor's **Messages** pane and the board's **diagnostic buffer** (Online → Diagnostics) say what the runtime decided and why - read them first.

---

[← Example projects](examples/README.md) | [Overview](README.md)
