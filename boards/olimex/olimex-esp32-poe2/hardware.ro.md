---
title: 'Olimex ESP32-POE2: hardware și cablare'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-POE2 - harta pinilor
tags:
- esp32
- ethernet
- poe
- psram
- olimex
---

# Hardware și cablare

## De ce ai nevoie

- Olimex ESP32-POE2.
- Un cablu de date USB-C - pentru prima încărcare a runtime-ului.
- Pentru alimentare: un switch / injector PoE (IEEE 802.3at, clasa 4 pentru cei 25 W completi) sau o sursă USB de 5 V.
- Un cablu Ethernet și un port liber în rețeaua ta.
- Un PC cu [editorul ctrl32](https://ctrl32.com/download/) (Windows).
- Opțional, pentru exemplul all-in-one: butonul BUT1 este pe placă; un modul de releu sau un LED pe GPIO4 (UEXT); un potențiometru (10 k) între 3,3 V și GND cu cursorul pe GPIO36; un transceiver CAN de 3,3 V pe GPIO5 (TX) / GPIO39 (RX).

## Alimentare

| Sursă | Unde | Notă |
|---|---|---|
| PoE | mufa Ethernet | IEEE 802.3at clasa 4, până la 25 W |
| USB 5 V | conectorul USB-C | calea pentru prima încărcare |
| Acumulator Li-Po | conectorul de acumulator | încărcat pe placă |

Alimentată prin Ethernet, placa alimentează circuite externe: **24 V /
0,75 A sau 12 V / 1,5 A** (un jumper alege), **5 V / 1,5 A** și
**3,3 V / 1 A**, în total 25 W.

!!! danger "Nu conecta niciodată USB și PoE în același timp"
    ESP32-POE2 **nu este izolată galvanic** de alimentarea Ethernet.
    Încarcă runtime-ul prin USB cu cablul Ethernet deconectat (sau de pe
    un port fără PoE), apoi rulează placa pe PoE.

## Harta pinilor

![Olimex ESP32-POE2 - harta pinilor](pinout/pinout.png)

| GPIO | Funcție în ctrl32 | Notă |
|---|---|---|
| 0 | Ethernet 50 MHz clock (LAN8710A) | ⚠ folosit de placă |
| 2 | SPI MOSI | ⚠ pin de strapping |
| 4 | free (UART TX line) |  |
| 5 | free (SPI CS line) |  |
| 6 | Flash SPI al modulului | ⚠ folosit de placă |
| 7 | Flash SPI al modulului | ⚠ folosit de placă |
| 8 | Flash SPI al modulului | ⚠ folosit de placă |
| 9 | Flash SPI al modulului | ⚠ folosit de placă |
| 10 | Flash SPI al modulului | ⚠ folosit de placă |
| 11 | Flash SPI al modulului | ⚠ folosit de placă |
| 12 | Ethernet PHY power (LAN8710A) | ⚠ folosit de placă |
| 13 | I2C SDA |  |
| 14 | SPI SCLK |  |
| 15 | SPI MISO | ⚠ pin de strapping |
| 18 | Ethernet MDIO (LAN8710A) | ⚠ folosit de placă |
| 19 | Ethernet RMII TXD0 (LAN8710A) | ⚠ folosit de placă |
| 21 | Ethernet RMII TX_EN (LAN8710A) | ⚠ folosit de placă |
| 22 | Ethernet RMII TXD1 (LAN8710A) | ⚠ folosit de placă |
| 23 | Ethernet MDC (LAN8710A) | ⚠ folosit de placă |
| 25 | Ethernet RMII RXD0 (LAN8710A) | ⚠ folosit de placă |
| 26 | Ethernet RMII RXD1 (LAN8710A) | ⚠ folosit de placă |
| 27 | Ethernet RMII CRS_DV (LAN8710A) | ⚠ folosit de placă |
| 33 | I2C SCL |  |
| 34 | liber - butonul plăcii | ⚠ doar intrare, ADC1 |
| 36 | free (UART RX line) | ⚠ doar intrare, ADC1 |
| 39 | liber - intrare | ⚠ doar intrare, ADC1 |

Pinii liberi se află pe conectorii **EXT** și pe conectorul **UEXT**.
GPIO34 până la GPIO39 sunt doar intrări. PSRAM-ul modulului ocupă GPIO16 /
GPIO17, așa că ceasul Ethernet rulează pe GPIO0, iar I2C folosește
GPIO13 / GPIO33.

## Siguranță

- Placa nu este destinată funcțiilor de siguranță. O oprire de urgență,
  un contact de ușă sau o barieră optică se cablează în hardware,
  niciodată printr-un program.
- Pinii GPIO sunt de 3,3 V. O intrare de 24 V are nevoie de un optocuplor
  sau de un convertor de nivel; o bobină de releu are nevoie de un driver
  (un modul de releu are unul).

---

[← Prezentare](README.ro.md) | [Prezentare](README.ro.md) | [Instalarea runtime-ului →](install.ro.md)
