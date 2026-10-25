---
title: 'Olimex ESP32-GATEWAY: hardware și cablare'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-GATEWAY - harta pinilor
tags:
- esp32
- ethernet
- gateway
- olimex
---

# Hardware și cablare

## De ce ai nevoie

- Olimex ESP32-GATEWAY.
- Un cablu de date USB-C - pentru încărcare și pentru alimentare (5 V).
- Un cablu Ethernet și un port liber în rețeaua ta.
- Un PC cu [editorul ctrl32](https://ctrl32.com/download/) (Windows).
- Exemplul all-in-one folosește butonul propriu al plăcii (GPIO34) și LED-ul (GPIO33) - nu mai e nimic de cablat.

## Alimentare

| Sursă | Unde | Notă |
|---|---|---|
| USB 5 V | conectorul USB-C | alimentare și programare |

## Harta pinilor

![Olimex ESP32-GATEWAY - harta pinilor](pinout/pinout.png)

| GPIO | Funcție în ctrl32 | Notă |
|---|---|---|
| 2 | SPI MOSI | ⚠ pin de strapping |
| 5 | Ethernet PHY power (LAN8710A) | ⚠ folosit de placă |
| 6 | Flash SPI al modulului | ⚠ folosit de placă |
| 7 | Flash SPI al modulului | ⚠ folosit de placă |
| 8 | Flash SPI al modulului | ⚠ folosit de placă |
| 9 | Flash SPI al modulului | ⚠ folosit de placă |
| 10 | Flash SPI al modulului | ⚠ folosit de placă |
| 11 | Flash SPI al modulului | ⚠ folosit de placă |
| 13 | free (SPI CS line) |  |
| 14 | SPI SCLK |  |
| 15 | SPI MISO | ⚠ pin de strapping |
| 16 | I2C SCL |  |
| 17 | Ethernet 50 MHz clock (LAN8710A) | ⚠ folosit de placă |
| 18 | Ethernet MDIO (LAN8710A) | ⚠ folosit de placă |
| 19 | Ethernet RMII TXD0 (LAN8710A) | ⚠ folosit de placă |
| 21 | Ethernet RMII TX_EN (LAN8710A) | ⚠ folosit de placă |
| 22 | Ethernet RMII TXD1 (LAN8710A) | ⚠ folosit de placă |
| 23 | Ethernet MDC (LAN8710A) | ⚠ folosit de placă |
| 25 | Ethernet RMII RXD0 (LAN8710A) | ⚠ folosit de placă |
| 26 | Ethernet RMII RXD1 (LAN8710A) | ⚠ folosit de placă |
| 27 | Ethernet RMII CRS_DV (LAN8710A) | ⚠ folosit de placă |
| 32 | I2C SDA |  |
| 33 | free (LED0 line) | ADC1 |
| 34 | liber - butonul plăcii | ⚠ doar intrare, ADC1 |

Conectorul **EXT** cu 20 de pini poartă pinii liberi și liniile I2C / SPI.
LED-ul plăcii este pe GPIO33 și butonul pe GPIO34 (doar intrare). Rămân
puțini pini liberi: mai multe I/O trec prin Modbus TCP sau prin cipuri I2C.

## Siguranță

- Placa nu este destinată funcțiilor de siguranță. O oprire de urgență,
  un contact de ușă sau o barieră optică se cablează în hardware, niciodată
  printr-un program.
- Pinii GPIO sunt de 3,3 V. Un semnal de 24 V are nevoie de un optocuplor
  sau de un convertor de nivel; o bobină de releu are nevoie de un driver
  (un modul de releu are unul).

---

[← Prezentare](README.ro.md) | [Prezentare](README.ro.md) | [Instalarea runtime-ului →](install.ro.md)
