---
title: 'LaskaKit ESPlan: hardware și cablare'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: LaskaKit ESPlan - harta pinilor
tags:
- esp32
- ethernet
- rs485
- modbus
- laskakit
---

# Hardware și cablare

## De ce ai nevoie

- LaskaKit ESPlan.
- Un cablu de date USB-C - pentru prima încărcare a runtime-ului.
- Pentru alimentare: 12 sau 24 V DC pe clema cu șurub (7-40 V) sau 5 V prin USB-C.
- Un cablu Ethernet și un port liber în rețeaua ta.
- Un PC cu [editorul ctrl32](https://ctrl32.com/download/) (Windows).
- Opțional, pentru exemplul all-in-one: un senzor de temperatură Modbus RTU (unit 1) pe clema RS-485; un buton de la GPIO16 la GND; un potențiometru (10 k) între 3,3 V și GND cu cursorul pe GPIO35; un transceiver CAN de 3,3 V pe GPIO14 (TX) / GPIO39 (RX).

## Alimentare

| Sursă | Unde | Notă |
|---|---|---|
| 7-40 V DC | clema cu șurub | recomandat 12 sau 24 V |
| USB 5 V | conectorul USB-C | calea pentru prima încărcare |
| PoE | prin modulul PoE opțional (802.3af) | supliment |

## Harta pinilor

![LaskaKit ESPlan - harta pinilor](pinout/pinout.png)

| GPIO | Funcție în ctrl32 | Notă |
|---|---|---|
| 0 | free (LED0 line) | ⚠ pin de strapping |
| 4 | RS485 TX |  |
| 5 | Ethernet PHY power (LAN8720A) | ⚠ folosit de placă |
| 6 | Flash SPI al modulului | ⚠ folosit de placă |
| 7 | Flash SPI al modulului | ⚠ folosit de placă |
| 8 | Flash SPI al modulului | ⚠ folosit de placă |
| 9 | Flash SPI al modulului | ⚠ folosit de placă |
| 10 | Flash SPI al modulului | ⚠ folosit de placă |
| 11 | Flash SPI al modulului | ⚠ folosit de placă |
| 12 | SPI MISO | ⚠ pin de strapping |
| 13 | SPI MOSI |  |
| 14 | free (SPI SCLK line) |  |
| 15 | SPI CS | ⚠ pin de strapping |
| 16 | liber - I/O |  |
| 17 | Ethernet 50 MHz clock (LAN8720A) | ⚠ folosit de placă |
| 18 | Ethernet MDIO (LAN8720A) | ⚠ folosit de placă |
| 19 | Ethernet RMII TXD0 (LAN8720A) | ⚠ folosit de placă |
| 21 | Ethernet RMII TX_EN (LAN8720A) | ⚠ folosit de placă |
| 22 | Ethernet RMII TXD1 (LAN8720A) | ⚠ folosit de placă |
| 23 | Ethernet MDC (LAN8720A) | ⚠ folosit de placă |
| 25 | Ethernet RMII RXD0 (LAN8720A) | ⚠ folosit de placă |
| 26 | Ethernet RMII RXD1 (LAN8720A) | ⚠ folosit de placă |
| 27 | Ethernet RMII CRS_DV (LAN8720A) | ⚠ folosit de placă |
| 32 | TOUCH SCL |  |
| 33 | TOUCH SDA |  |
| 35 | liber - intrare | ⚠ doar intrare, ADC1 |
| 36 | RS485 RX |  |
| 39 | liber - intrare | ⚠ doar intrare, ADC1 |

**RS-485:** A și B pe clemă, transceiverul WS3081 pe GPIO4 (TX) /
GPIO36 (RX); un jumper comută terminația de 120 ohm - pune-o doar la cele
două capete ale liniei. Conectorii **uSup** poartă I2C (GPIO33 / GPIO32)
și SPI. LED-ul plăcii este pe GPIO0 (un pin de strapping - păstrează-l ca
ieșire comandată de program).

## Siguranță

- Placa nu este destinată funcțiilor de siguranță. O oprire de urgență,
  un contact de ușă sau o barieră optică se cablează în hardware, niciodată
  printr-un program.
- Pinii GPIO sunt de 3,3 V. Un semnal de 24 V are nevoie de un optocuplor
  sau de un convertor de nivel; o bobină de releu are nevoie de un driver
  (un modul de releu are unul).

---

[← Prezentare](README.ro.md) | [Prezentare](README.ro.md) | [Instalarea runtime-ului →](install.ro.md)
