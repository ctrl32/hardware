---
title: 'Makerfabs MaTouch Lite ESP32-S3 3.95": hardware and wiring'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Makerfabs MaTouch Lite ESP32-S3 3.95" pin map
tags:
- esp32-s3
- display
- touch
- hmi
- wifi
- makerfabs
---

# Hardware and wiring

## What you need

- The Makerfabs MaTouch Lite ESP32-S3 3.95" (ST7796).
- A USB-C data cable - for the upload and for power.
- The name and the password of your 2.4 GHz Wi-Fi.
- A PC with the [ctrl32 editor](https://ctrl32.com/download/) (Windows).
- Optional, for the all-in-one example: a relay module or an LED on GPIO4, a potentiometer (10 k) between 3.3 V and GND with its wiper on GPIO5 (the JST connectors), and a 3.3 V CAN transceiver (e.g. SN65HVD230) on GPIO6 / GPIO7.

## Power

| Source | Where | Note |
|---|---|---|
| USB 5 V | the USB-C connector | power and programming |
| Li-Po battery | the battery connector | 3.7 V |

## Pin map

![Makerfabs MaTouch Lite ESP32-S3 3.95" pin map](pinout/pinout.png)

| GPIO | Function in ctrl32 | Note |
|---|---|---|
| 0 | BOOT BTN | ⚠ strapping pin |
| 1 | TFT RST |  |
| 2 | SD CMD | ⚠  |
| 4 | free I/O | ADC1 |
| 5 | free I/O | ADC1 |
| 6 | free I/O | ADC1 |
| 7 | free I/O | ADC1 |
| 13 | TFT MOSI |  |
| 14 | TFT SCLK |  |
| 15 | TFT CS |  |
| 21 | TFT DC |  |
| 38 | TOUCH SDA |  |
| 39 | TOUCH SCL |  |
| 40 | TOUCH INT |  |
| 41 | SD DO | ⚠  |
| 42 | SD SCLK | ⚠  |
| 48 | TFT BL |  |

The two **JST** connectors carry the four free pins (GPIO4 to GPIO7) - few,
so the example puts the output, the analog input and CAN on them; more
I/O goes through Modbus TCP or I2C chips. The display, the touch controller
and the microSD slot take the rest of the pins.

## Safety

- The board is not intended for safety functions. An emergency stop, a
  door switch or a light curtain is wired in hardware, never through a
  program or a touch screen.
- The GPIO pins are 3.3 V. A relay coil needs a driver (a relay module has one).

---

[← Overview](README.md) | [Overview](README.md) | [Install the runtime →](install.md)
