---
title: 'Olimex ESP32-EVB: hardware și cablare'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-EVB - harta pinilor
tags:
- esp32
- ethernet
- can
- relay
- olimex
---

# Hardware și cablare

## De ce ai nevoie

- Olimex ESP32-EVB.
- Un cablu de date micro-USB - pentru prima încărcare a runtime-ului.
- Pentru alimentare: o sursă USB de 5 V sau 5 V pe clema cu șurub.
- Un cablu Ethernet și un port liber în rețeaua ta.
- Un PC cu [editorul ctrl32](https://ctrl32.com/download/) (Windows).
- Opțional, pentru exemplul all-in-one: un potențiometru (10 k) între 3,3 V și GND cu cursorul pe GPIO36 (UEXT); un nod CAN sau un adaptor CAN și două terminatoare de 120 ohm.
- Opțional: display-ul Olimex MOD-LCD2.8RTP (2,8 inch, 240 x 320, touch rezistiv) pe conectorul UEXT.

## Alimentare

| Sursă | Unde | Notă |
|---|---|---|
| USB 5 V | conectorul micro-USB | calea pentru prima încărcare |
| 5 V DC | clema cu șurub | pentru un dulap |
| Acumulator Li-Po | conectorul de acumulator | încărcat pe placă |

!!! warning "Releele comută tensiunea rețelei"
    Cablează contactele releelor doar cu placa nealimentată, într-o
    carcasă, și doar dacă ai voie să lucrezi la instalații de rețea.
    Contactele suportă 10 A / 250 VAC; un motor sau un încălzitor peste
    atât are nevoie de un contactor comandat de releu.

## Harta pinilor

![Olimex ESP32-EVB - harta pinilor](pinout/pinout.png)

| GPIO | Funcție în ctrl32 | Notă |
|---|---|---|
| 0 | Ethernet 50 MHz clock (LAN8710A) | ⚠ folosit de placă |
| 2 | TFT MOSI | ⚠ pin de strapping |
| 2 | SPI MOSI | ⚠ pin de strapping |
| 4 | free (UART TX line) |  |
| 5 | CAN TX |  |
| 6 | Flash SPI al modulului | ⚠ folosit de placă |
| 7 | Flash SPI al modulului | ⚠ folosit de placă |
| 8 | Flash SPI al modulului | ⚠ folosit de placă |
| 9 | Flash SPI al modulului | ⚠ folosit de placă |
| 10 | Flash SPI al modulului | ⚠ folosit de placă |
| 11 | Flash SPI al modulului | ⚠ folosit de placă |
| 13 | I2C SDA |  |
| 14 | TFT SCLK |  |
| 14 | SPI SCLK |  |
| 15 | TFT DC | ⚠ pin de strapping |
| 15 | SPI MISO | ⚠ pin de strapping |
| 16 | I2C SCL |  |
| 17 | TFT CS |  |
| 17 | free (SPI CS line) |  |
| 18 | Ethernet MDIO (LAN8710A) | ⚠ folosit de placă |
| 19 | Ethernet RMII TXD0 (LAN8710A) | ⚠ folosit de placă |
| 21 | Ethernet RMII TX_EN (LAN8710A) | ⚠ folosit de placă |
| 22 | Ethernet RMII TXD1 (LAN8710A) | ⚠ folosit de placă |
| 23 | Ethernet MDC (LAN8710A) | ⚠ folosit de placă |
| 25 | Ethernet RMII RXD0 (LAN8710A) | ⚠ folosit de placă |
| 26 | Ethernet RMII RXD1 (LAN8710A) | ⚠ folosit de placă |
| 27 | Ethernet RMII CRS_DV (LAN8710A) | ⚠ folosit de placă |
| 32 | free (REL1 line) | ADC1 |
| 33 | free (REL2 line) | ADC1 |
| 34 | liber - butonul plăcii | ⚠ doar intrare, ADC1 |
| 35 | CAN RX |  |
| 36 | free (UART RX line) | ⚠ doar intrare, ADC1 |

**Relee:** REL1 pe GPIO32, REL2 pe GPIO33. **Buton:** BUT1 pe GPIO34
(doar intrare). **CAN:** transceiverul de pe placă pe GPIO5 (TX) / GPIO35
(RX), CAN_H / CAN_L pe clemă - termină magistrala cu 120 ohm la ambele
capete. Conectorul **UEXT** poartă I2C (GPIO13 / GPIO16), SPI și un UART
liber (GPIO4 / GPIO36); display-ul opțional folosește liniile lui SPI.

## Siguranță

- Placa nu este destinată funcțiilor de siguranță. O oprire de urgență,
  un contact de ușă sau o barieră optică se cablează în hardware, niciodată
  printr-un program.
- Pinii GPIO sunt de 3,3 V. Un semnal de 24 V are nevoie de un optocuplor
  sau de un convertor de nivel; o bobină de releu are nevoie de un driver
  (un modul de releu are unul).

---

[← Prezentare](README.ro.md) | [Prezentare](README.ro.md) | [Instalarea runtime-ului →](install.ro.md)
