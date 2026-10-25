---
title: 'Olimex ESP32-S3-DevKit-Lipo: hardware și cablare'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-S3-DevKit-Lipo - harta pinilor
tags:
- esp32-s3
- wifi
- psram
- battery
- olimex
---

# Hardware și cablare

## De ce ai nevoie

- Olimex ESP32-S3-DevKit-Lipo.
- Un cablu de date USB-C - pe conectorul marcat UART (CH340X) pentru încărcare.
- Numele și parola rețelei tale Wi-Fi de 2,4 GHz.
- Un PC cu [editorul ctrl32](https://ctrl32.com/download/) (Windows).
- Opțional, pentru exemplul all-in-one: butonul Boot/User (GPIO0) și LED-ul (GPIO38) sunt pe placă; un potențiometru (10 k) între 3,3 V și GND cu cursorul pe GPIO1; un transceiver CAN de 3,3 V pe GPIO10 / GPIO17 și un transceiver RS-485 pe GPIO18 / GPIO2 / GPIO4 (DE).

## Alimentare

| Sursă | Unde | Notă |
|---|---|---|
| USB 5 V | oricare dintre conectorii USB-C | alimentare și programare |
| Acumulator Li-Po | conectorul de acumulator | încărcat pe placă, comutare automată |

## Harta pinilor

![Olimex ESP32-S3-DevKit-Lipo - harta pinilor](pinout/pinout.png)

| GPIO | Funcție în ctrl32 | Notă |
|---|---|---|
| 0 | liber - butonul plăcii | ⚠ pin de strapping |
| 1 | liber - I/O | ADC1 |
| 2 | liber - I/O | ADC1 |
| 4 | liber - I/O | ADC1 |
| 5 | free (PWR SENSE line) | ADC1 |
| 6 | free (BAT SENSE line) | ADC1 |
| 7 | liber - I/O | ADC1 |
| 8 | liber - I/O | ADC1 |
| 9 | liber - I/O | ADC1 |
| 10 | free (SPI CS line) | ADC1 |
| 11 | SPI MOSI |  |
| 12 | SPI SCLK |  |
| 13 | SPI MISO |  |
| 14 | liber - I/O |  |
| 15 | liber - I/O |  |
| 16 | liber - I/O |  |
| 17 | free (UART TX line) |  |
| 18 | free (UART RX line) |  |
| 21 | liber - I/O |  |
| 38 | free (LED0 line) |  |
| 39 | liber - I/O |  |
| 40 | liber - I/O |  |
| 41 | liber - I/O |  |
| 42 | liber - I/O |  |
| 47 | I2C SCL |  |
| 48 | I2C SDA |  |

Conectorii poartă GPIO-urile libere; ADC1 (intrările analogice pe care le
folosește ctrl32) este pe GPIO1 până la GPIO10. GPIO0 este butonul
Boot/User - o intrare în program, iar ținut apăsat la pornire lansează
modul de descărcare al cipului. Conectorul pUEXT poartă I2C (GPIO48 /
GPIO47) și SPI.

## Siguranță

- Placa nu este destinată funcțiilor de siguranță. O oprire de urgență,
  un contact de ușă sau o barieră optică se cablează în hardware, niciodată
  printr-un program.
- Pinii GPIO sunt de 3,3 V. Un semnal de 24 V are nevoie de un optocuplor
  sau de un convertor de nivel; o bobină de releu are nevoie de un driver
  (un modul de releu are unul).

---

[← Prezentare](README.ro.md) | [Prezentare](README.ro.md) | [Instalarea runtime-ului →](install.ro.md)
