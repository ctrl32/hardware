---
title: 'Olimex ESP32-PoE: hardware and wiring'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-PoE pin map
tags:
- esp32
- ethernet
- poe
- olimex
---

# Hardware and wiring

## What you need

- The Olimex ESP32-PoE (the WROOM-32E variant, without PSRAM).
- A micro-USB data cable - for the first upload of the runtime.
- For power: a 5 V USB supply, or a PoE switch / injector (IEEE 802.3af).
- An Ethernet cable and a free port on your network.
- A PC with the [ctrl32 editor](https://ctrl32.com/download/) (Windows).
- Optional, for the all-in-one example: a push-button is on the board (BUT1); a relay module or an LED with a resistor on GPIO33; a potentiometer (10 k) between 3.3 V and GND with its wiper on GPIO35.

## Power

The board takes its power from one of three sources:

| Source | Where | Note |
|---|---|---|
| USB 5 V | the micro-USB connector | the road for the first upload |
| PoE | the Ethernet jack, from a PoE switch or injector | IEEE 802.3af |
| Li-Po battery | the battery connector | charged on board |

!!! danger "Never connect USB and PoE at the same time"
    The ESP32-PoE is **not galvanically isolated**. While the board is
    powered over PoE, its ground follows the PoE supply - a USB cable to
    your PC can then carry a damaging current. Upload the runtime over USB
    with the Ethernet cable **unplugged** (or from a non-PoE port), then
    run the board on PoE. Where a PC must stay connected while the board is
    on PoE, use the ESP32-PoE-ISO.

## Pin map

![Olimex ESP32-PoE pin map](pinout/pinout.png)

| GPIO | Function in ctrl32 | Note |
|---|---|---|
| 2 | SPI MOSI | ⚠ strapping pin |
| 4 | free (UART TX line) |  |
| 5 | free (SPI CS line) |  |
| 6 | SPI flash of the module | ⚠ used by the board |
| 7 | SPI flash of the module | ⚠ used by the board |
| 8 | SPI flash of the module | ⚠ used by the board |
| 9 | SPI flash of the module | ⚠ used by the board |
| 10 | SPI flash of the module | ⚠ used by the board |
| 11 | SPI flash of the module | ⚠ used by the board |
| 12 | Ethernet PHY power (LAN8710A) | ⚠ used by the board |
| 13 | I2C SDA |  |
| 14 | SPI SCLK |  |
| 15 | SPI MISO | ⚠ strapping pin |
| 16 | I2C SCL |  |
| 17 | Ethernet 50 MHz clock (LAN8710A) | ⚠ used by the board |
| 18 | Ethernet MDIO (LAN8710A) | ⚠ used by the board |
| 19 | Ethernet RMII TXD0 (LAN8710A) | ⚠ used by the board |
| 21 | Ethernet RMII TX_EN (LAN8710A) | ⚠ used by the board |
| 22 | Ethernet RMII TXD1 (LAN8710A) | ⚠ used by the board |
| 23 | Ethernet MDC (LAN8710A) | ⚠ used by the board |
| 25 | Ethernet RMII RXD0 (LAN8710A) | ⚠ used by the board |
| 26 | Ethernet RMII RXD1 (LAN8710A) | ⚠ used by the board |
| 27 | Ethernet RMII CRS_DV (LAN8710A) | ⚠ used by the board |
| 33 | free I/O | ADC1 |
| 34 | free - the board's button | ⚠ input only, ADC1 |
| 35 | free input | ⚠ input only, ADC1 |
| 36 | free (UART RX line) | ⚠ input only, ADC1 |

The free pins sit on the **EXT1 / EXT2** headers (2.54 mm) and on the
**UEXT** connector. GPIO34 to GPIO39 are inputs only - an output there is
refused by the editor. The UEXT connector carries I2C (GPIO13 / GPIO16)
and SPI (GPIO14 / GPIO2 / GPIO15, shared with the microSD slot).

## Safety

- The board is not intended for safety functions. An emergency stop, a
  door switch or a light curtain is wired in hardware, never through a
  program.
- The GPIO pins are 3.3 V. A 24 V input needs an opto-coupler or a level
  shifter; a relay coil needs a driver (a relay module has one).

---

[← Overview](README.md) | [Overview](README.md) | [Install the runtime →](install.md)
