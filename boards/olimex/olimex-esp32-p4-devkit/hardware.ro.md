---
title: 'Olimex ESP32-P4-DevKit: hardware și cablare'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-P4-DevKit - harta pinilor
tags:
- esp32-p4
- ethernet
- olimex
---

# Hardware și cablare

## De ce ai nevoie

- Olimex ESP32-P4-DevKit.
- Un cablu de date USB-C - pentru încărcare și pentru alimentare (5 V).
- Un cablu Ethernet și un port liber în rețeaua ta.
- Un PC cu [editorul ctrl32](https://ctrl32.com/download/) (Windows).
- Opțional, pentru exemplul all-in-one: LED-ul (GPIO2) este pe placă; un buton de la GPIO20 la GND; un transceiver CAN de 3,3 V pe GPIO5 / GPIO21 și un transceiver RS-485 pe GPIO22 / GPIO23 / GPIO32 (DE).

## Alimentare

| Sursă | Unde | Notă |
|---|---|---|
| USB 5 V | conectorul USB-C | alimentare, programare și depanare |
| PoE | prin extensia PoE | opțional |

## Harta pinilor

![Olimex ESP32-P4-DevKit - harta pinilor](pinout/pinout.png)

| GPIO | Funcție în ctrl32 | Notă |
|---|---|---|
| 2 | free (LED0 line) |  |
| 4 | SPI SCLK |  |
| 5 | free (SPI CS line) |  |
| 7 | I2C SDA |  |
| 8 | I2C SCL |  |
| 20 | liber - I/O |  |
| 21 | liber - I/O |  |
| 22 | liber - I/O |  |
| 23 | liber - I/O |  |
| 28 | Ethernet RMII (IP101GRI) | ⚠ folosit de placă |
| 29 | Ethernet RMII (IP101GRI) | ⚠ folosit de placă |
| 30 | Ethernet RMII (IP101GRI) | ⚠ folosit de placă |
| 31 | Ethernet MDC (IP101GRI) | ⚠ folosit de placă |
| 32 | liber - I/O |  |
| 33 | liber - I/O |  |
| 34 | Ethernet RMII (IP101GRI) | ⚠ folosit de placă |
| 35 | Ethernet RMII (IP101GRI) | ⚠ folosit de placă |
| 46 | liber - I/O |  |
| 47 | liber - I/O |  |
| 48 | liber - I/O |  |
| 49 | Ethernet RMII (IP101GRI) | ⚠ folosit de placă |
| 50 | Ethernet RMII (IP101GRI) | ⚠ folosit de placă |
| 51 | Ethernet PHY reset (IP101GRI) | ⚠ folosit de placă |
| 52 | Ethernet MDIO (IP101GRI) | ⚠ folosit de placă |
| 53 | SPI MOSI |  |
| 54 | SPI MISO |  |

Toate GPIO-urile sunt pe cei doi conectori cu 20 de pini. ESP32-P4 nu are
nicio intrare analogică pe care să o folosească ctrl32: semnalele
analogice trec printr-un ADC I2C (un ADS1115 pe conectorul pUEXT, I2C
GPIO7 / GPIO8) sau printr-un modul Modbus.

## Siguranță

- Placa nu este destinată funcțiilor de siguranță. O oprire de urgență,
  un contact de ușă sau o barieră optică se cablează în hardware, niciodată
  printr-un program.
- Pinii GPIO sunt de 3,3 V. Un semnal de 24 V are nevoie de un optocuplor
  sau de un convertor de nivel; o bobină de releu are nevoie de un driver
  (un modul de releu are unul).

---

[← Prezentare](README.ro.md) | [Prezentare](README.ro.md) | [Instalarea runtime-ului →](install.ro.md)
