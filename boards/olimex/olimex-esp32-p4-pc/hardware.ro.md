---
title: 'Olimex ESP32-P4-PC: hardware și cablare'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-P4-PC - harta pinilor
tags:
- esp32-p4
- ethernet
- ups
- olimex
---

# Hardware și cablare

## De ce ai nevoie

- Olimex ESP32-P4-PC.
- Un cablu de date USB-C - pentru încărcare și pentru alimentare (5 V).
- Un cablu Ethernet și un port liber în rețeaua ta.
- Un PC cu [editorul ctrl32](https://ctrl32.com/download/) (Windows).
- Opțional: o celulă Li-Po pentru rezerva de acumulator; pentru exemplul all-in-one LED-ul utilizatorului (GPIO2) este pe placă, iar un buton merge de la GPIO14 la GND (EXT1); un transceiver CAN de 3,3 V pe GPIO5 / GPIO15 și un transceiver RS-485 pe GPIO16 / GPIO17 / GPIO18 (DE).

## Alimentare

| Sursă | Unde | Notă |
|---|---|---|
| USB 5 V | conectorul USB-C | alimentare, programare și depanare |
| Acumulator Li-Po | conectorul de acumulator | încărcat pe placă; preia când pică alimentarea (UPS) |
| PoE | prin extensia PoE | opțional |

## Harta pinilor

![Olimex ESP32-P4-PC - harta pinilor](pinout/pinout.png)

| GPIO | Funcție în ctrl32 | Notă |
|---|---|---|
| 2 | free (LED0 line) |  |
| 4 | SPI SCLK |  |
| 5 | free (SPI CS line) |  |
| 14 | liber - I/O |  |
| 15 | liber - I/O |  |
| 16 | liber - I/O |  |
| 17 | liber - I/O |  |
| 18 | liber - I/O |  |
| 19 | liber - I/O |  |
| 20 | liber - I/O |  |
| 21 | USB HUB RST | ⚠  |
| 22 | I2C SDA |  |
| 23 | I2C SCL |  |
| 28 | Ethernet RMII (IP101GRI) | ⚠ folosit de placă |
| 29 | Ethernet RMII (IP101GRI) | ⚠ folosit de placă |
| 30 | Ethernet RMII (IP101GRI) | ⚠ folosit de placă |
| 31 | Ethernet MDC (IP101GRI) | ⚠ folosit de placă |
| 32 | liber - I/O |  |
| 33 | liber - I/O |  |
| 34 | Ethernet RMII (IP101GRI) | ⚠ folosit de placă |
| 35 | Ethernet RMII (IP101GRI) | ⚠ folosit de placă |
| 36 | liber - I/O | ⚠ pin de strapping |
| 46 | liber - I/O |  |
| 47 | liber - I/O |  |
| 48 | liber - I/O |  |
| 49 | Ethernet RMII (IP101GRI) | ⚠ folosit de placă |
| 50 | Ethernet RMII (IP101GRI) | ⚠ folosit de placă |
| 51 | Ethernet PHY reset (IP101GRI) | ⚠ folosit de placă |
| 52 | Ethernet MDIO (IP101GRI) | ⚠ folosit de placă |
| 53 | SPI MOSI |  |
| 54 | SPI MISO |  |

Pinii liberi sunt pe conectorul **EXT1** cu 20 de pini: GPIO14 până la
GPIO20, 32, 33, 36, 46, 47, 48 și LED-ul utilizatorului pe GPIO2.
Conectorul **UEXT** poartă I2C (GPIO22 / GPIO23 - partajat cu puntea
HDMI), SPI (GPIO4 / 53 / 54, CS GPIO5) și UART-ul de consolă. ESP32-P4 nu
are nicio intrare analogică pe care să o folosească ctrl32: semnalele
analogice trec printr-un ADC I2C (un ADS1115 pe UEXT) sau printr-un modul
Modbus. CAN și RS-485 se pun pe pini EXT1 liberi cu un modul transceiver
de 3,3 V.

## Siguranță

- Placa nu este destinată funcțiilor de siguranță. O oprire de urgență,
  un contact de ușă sau o barieră optică se cablează în hardware, niciodată
  printr-un program.
- Pinii GPIO sunt de 3,3 V. Un semnal de 24 V are nevoie de un optocuplor
  sau de un convertor de nivel; o bobină de releu are nevoie de un driver
  (un modul de releu are unul).

## Fotografii

![Olimex ESP32-P4-PC - fotografia 1](img/board-01.jpg)
![Olimex ESP32-P4-PC - fotografia 2](img/board-02.jpg)
![Olimex ESP32-P4-PC - fotografia 3](img/board-03.jpg)
![Olimex ESP32-P4-PC - fotografia 4](img/board-04.jpg)

---

[← Prezentare](README.ro.md) | [Prezentare](README.ro.md) | [Instalarea runtime-ului →](install.ro.md)
