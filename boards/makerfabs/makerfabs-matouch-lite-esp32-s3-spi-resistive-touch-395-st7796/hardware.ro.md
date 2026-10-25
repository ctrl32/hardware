---
title: 'Makerfabs MaTouch Lite ESP32-S3 3.95": hardware și cablare'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Makerfabs MaTouch Lite ESP32-S3 3.95" - harta pinilor
tags:
- esp32-s3
- display
- touch
- hmi
- wifi
- makerfabs
---

# Hardware și cablare

## De ce ai nevoie

- Makerfabs MaTouch Lite ESP32-S3 3,95" (ST7796).
- Un cablu de date USB-C - pentru încărcare și pentru alimentare.
- Numele și parola rețelei tale Wi-Fi de 2,4 GHz.
- Un PC cu [editorul ctrl32](https://ctrl32.com/download/) (Windows).
- Opțional, pentru exemplul all-in-one: un modul de releu sau un LED pe GPIO4, un potențiometru (10 k) între 3,3 V și GND cu cursorul pe GPIO5 (conectorii JST) și un transceiver CAN de 3,3 V (de ex. SN65HVD230) pe GPIO6 / GPIO7.

## Alimentare

| Sursă | Unde | Notă |
|---|---|---|
| USB 5 V | conectorul USB-C | alimentare și programare |
| Acumulator Li-Po | conectorul de acumulator | 3,7 V |

## Harta pinilor

![Makerfabs MaTouch Lite ESP32-S3 3.95" - harta pinilor](pinout/pinout.png)

| GPIO | Funcție în ctrl32 | Notă |
|---|---|---|
| 0 | BOOT BTN | ⚠ pin de strapping |
| 1 | TFT RST |  |
| 2 | SD CMD | ⚠  |
| 4 | liber - I/O | ADC1 |
| 5 | liber - I/O | ADC1 |
| 6 | liber - I/O | ADC1 |
| 7 | liber - I/O | ADC1 |
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

Cei doi conectori **JST** poartă cei patru pini liberi (GPIO4 până la
GPIO7) - puțini, așa că exemplul pune pe ei ieșirea, intrarea analogică și
CAN; mai multe I/O trec prin Modbus TCP sau prin cipuri I2C. Display-ul,
controlerul de touch și slotul microSD ocupă restul pinilor.

## Siguranță

- Placa nu este destinată funcțiilor de siguranță. O oprire de urgență,
  un contact de ușă sau o barieră optică se cablează în hardware,
  niciodată printr-un program sau un ecran tactil.
- Pinii GPIO sunt de 3,3 V. O bobină de releu are nevoie de un driver (un modul de releu are unul).

---

[← Prezentare](README.ro.md) | [Prezentare](README.ro.md) | [Instalarea runtime-ului →](install.ro.md)
