---
title: Olimex ESP32-PoE-ISO
slug: olimex-esp32-poe-iso
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-poe-iso/
image: img/board-01.jpg
image_alt: Olimex ESP32-PoE-ISO board with the Ethernet jack and the isolated PoE supply
tags:
- esp32
- ethernet
- poe
- isolated
- olimex
---

# Olimex ESP32-PoE-ISO

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32](https://img.shields.io/badge/chip-ESP32-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a)

![Olimex ESP32-PoE-ISO board with the Ethernet jack and the isolated PoE supply](img/board-01.jpg)

The Olimex ESP32-PoE-ISO is the ESP32-PoE with a galvanically isolated Power-over-Ethernet supply: one network cable powers it and carries its link, and a PC can stay connected over USB while the board runs on PoE. With ctrl32 it is a compact PLC for a cabinet - a ladder program on the chip, its operator page in any browser (WEBview), Modbus TCP to meters and I/O modules, and MQTT to Home Assistant.

**Good for:**

- A small PLC in a cabinet, powered from a PoE switch
- A Modbus TCP gateway that reads meters and publishes them over MQTT
- Home automation - a room or a boiler room on one cable

Board page in the catalog: [Olimex ESP32-PoE-ISO](https://ctrl32.com/hardware/boards/olimex-esp32-poe-iso/)

![Olimex ESP32-PoE-ISO pin map: the function of every GPIO in ctrl32](pinout/pinout.png)

## What ctrl32 can do on this board

<!-- capabilities:start -->
| Feature | On this board | Notes |
|---|---|---|
| Chip | ESP32 (ESP32-WROOM-32E-N4) |  |
| Memory | 4 MB flash |  |
| Program size | 128 variables, 32 alarms, 128 blocks | checked by the editor before a download |
| Digital inputs / outputs | 6 free GPIO | 3 of them inputs only |
| Analog inputs | 4 on the chip (ADC1) | GPIO33, GPIO34, GPIO35, GPIO36 |
| Ethernet | yes - LAN8710A |  |
| Power over Ethernet | IEEE 802.3af |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 on the chip - not brought out on this board |  |
| Modbus RTU (RS-485) | no transceiver on the board |  |
| Modbus TCP | client and server |  |
| MQTT | yes | Home Assistant discovery |
| WEBview | yes | the operator page in any browser |
| Display / touch (HMI) | no | the operator page is WEBview |
| USB | Micro-USB (CH340T USB-UART) |  |
| Power | 5 V USB, 3.7 V Li-Po / Li-Ion, PoE |  |
<!-- capabilities:end -->

### What is not supported

- Bluetooth - the ESP32 has it, ctrl32 does not use it.
- The microSD slot - ctrl32 keeps the program and the screens in the chip's own flash.
- The battery input works as the board's own feature; ctrl32 does not read the battery level.

## The guide

| Step | Page |
|---|---|
| 1 | [Hardware and wiring](hardware.md) - what you need, power, the pin map |
| 2 | [Install the runtime](install.md) - the editor, the board, the first upload |
| 3 | [Configure](configure.md) - network, I/O, communication |
| 4 | [Example projects](examples/README.md) - everything the board does, ready to open |
| - | [Troubleshooting](troubleshooting.md) |

## Files

-

## Next steps

- [ctrl32 documentation](https://ctrl32.com/docs/) - the editor, the languages, every block
- [Download the editor](https://ctrl32.com/download/)
- [All tested boards](../../README.md)
- [Olimex ESP32-PoE](../olimex-esp32-poe/README.md) - the same board without the isolated supply
- [Olimex ESP32-POE2](../olimex-esp32-poe2/README.md) - the next generation

