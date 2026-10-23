---
title: 'Raspberry Pi 4 Model B: troubleshooting'
slug: troubleshooting
sidebar_position: 90
image: img/board-01.jpg
image_alt: Raspberry Pi 4 Model B
tags:
- raspberry-pi
- linux
- hmi
- opc-ua
- ethercat
- troubleshooting
---

# Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| Look at the device cannot connect | SSH is off, the address is wrong, or the PC is in another network | Enable SSH in the Imager's settings and write the card again; ping the address from the PC. |
| Prepare offers no installation | The ctrl32 runtime is already installed on the Pi | An installed runtime is updated with Flash runtime and the Pi's address in the port picker. |
| The monitor stays black after the download | The monitor was connected after the boot, or the project has no screen | Connect the monitor before powering the Pi; add a screen to the project. |
| WEBview does not open | The wrong port | Open http://<address>:8080 - the runtime serves on 8080. |
| The USB-RS485 adapter disappears | Undervoltage - the supply is too weak | Use the official 27 W supply. |
| CAN stays silent | The HAT's driver is not loaded, no termination, or a different bit rate | Tick the HAT in Prepare a Linux device; a 120 ohm resistor at both ends of the bus; the same bit rate on every node. |
| An OPC UA client sees no variables | The variable is kept off the server, or a firewall blocks port 4840 | Check the OPC UA tick in the variable list; open port 4840. |

The editor's **Messages** pane and the board's **diagnostic buffer** (Online → Diagnostics) say what the runtime decided and why - read them first.

---

[← Example projects](examples/README.md) | [Overview](README.md)
