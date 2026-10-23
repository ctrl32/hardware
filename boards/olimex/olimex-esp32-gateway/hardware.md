---
title: 'Olimex ESP32-GATEWAY: hardware and wiring'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-GATEWAY pin map
tags:
- esp32
- ethernet
- gateway
- olimex
---

# Hardware and wiring

## What you need

- The Olimex ESP32-GATEWAY.
- A USB-C data cable - for the upload and for power (5 V).
- An Ethernet cable and a free port on your network.
- A PC with the [ctrl32 editor](https://ctrl32.com/download/) (Windows).
- The all-in-one example uses the board's own button (GPIO34) and LED (GPIO33) - nothing else to wire.

## Power

| Source | Where | Note |
|---|---|---|
| USB 5 V | the USB-C connector | power and programming |

## Pin map

![Olimex ESP32-GATEWAY pin map](pinout/pinout.png)

| GPIO | Function in ctrl32 | Note |
|---|---|---|
| 2 | SPI MOSI | ⚠ strapping pin |
| 5 | Ethernet PHY power (LAN8710A) | ⚠ used by the board |
| 6 | SPI flash of the module | ⚠ used by the board |
| 7 | SPI flash of the module | ⚠ used by the board |
| 8 | SPI flash of the module | ⚠ used by the board |
| 9 | SPI flash of the module | ⚠ used by the board |
| 10 | SPI flash of the module | ⚠ used by the board |
| 11 | SPI flash of the module | ⚠ used by the board |
| 13 | free (SPI CS line) |  |
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
| 32 | I2C SDA |  |
| 33 | free (LED0 line) | ADC1 |
| 34 | free - the board's button | ⚠ input only, ADC1 |

The 20-pin **EXT** header carries the free pins and the I2C / SPI lines.
The board's LED is on GPIO33 and its button on GPIO34 (an input only).
Few pins are left free: more I/O goes through Modbus TCP or I2C chips.

## Safety

- The board is not intended for safety functions. An emergency stop, a
  door switch or a light curtain is wired in hardware, never through a
  program.
- The GPIO pins are 3.3 V. A 24 V signal needs an opto-coupler or a level
  shifter; a relay coil needs a driver (a relay module has one).

---

[← Overview](README.md) | [Overview](README.md) | [Install the runtime →](install.md)
