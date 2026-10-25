---
title: 'Olimex ESP32-POE2: hardver és bekötés'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-POE2 - lábkiosztás
tags:
- esp32
- ethernet
- poe
- psram
- olimex
---

# Hardver és bekötés

## Amire szükséged van

- Az Olimex ESP32-POE2.
- Egy USB-C adatkábel - a runtime első feltöltéséhez.
- Tápellátáshoz: egy PoE switch / injektor (IEEE 802.3at, 4-es osztály a teljes 25 W-hoz) vagy egy 5 V-os USB tápegység.
- Egy Ethernet-kábel és egy szabad port a hálózatodon.
- Egy PC a [ctrl32 szerkesztővel](https://ctrl32.com/download/) (Windows).
- Opcionálisan, az all-in-one példához: a BUT1 gomb a panelen van; egy relémodul vagy egy LED a GPIO4-en (UEXT); egy potenciométer (10 k) a 3,3 V és a GND között, a csúszkája a GPIO36-on; egy 3,3 V-os CAN adó-vevő a GPIO5 (TX) / GPIO39 (RX) lábon.

## Tápellátás

| Forrás | Hol | Megjegyzés |
|---|---|---|
| PoE | az Ethernet aljzat | IEEE 802.3at, 4-es osztály, akár 25 W |
| USB 5 V | az USB-C csatlakozó | az első feltöltés útja |
| Li-Po akkumulátor | az akkumulátor-csatlakozó | a panelen töltődik |

Etherneten keresztül táplálva a panel külső áramköröket is ellát:
**24 V / 0,75 A vagy 12 V / 1,5 A** (jumperrel választható),
**5 V / 1,5 A** és **3,3 V / 1 A**, összesen 25 W.

!!! danger "Soha ne csatlakoztasd egyszerre az USB-t és a PoE-t"
    Az ESP32-POE2 **nincs galvanikusan leválasztva** az Ethernet táptól.
    A runtime-ot USB-n töltsd fel kihúzott Ethernet-kábellel (vagy egy PoE
    nélküli portról), és csak utána üzemeltesd a panelt PoE-ről.

## Lábkiosztás

![Olimex ESP32-POE2 - lábkiosztás](pinout/pinout.png)

| GPIO | Funkció a ctrl32-ben | Megjegyzés |
|---|---|---|
| 0 | Ethernet 50 MHz clock (LAN8710A) | ⚠ a panel használja |
| 2 | SPI MOSI | ⚠ strapping láb |
| 4 | free (UART TX line) |  |
| 5 | free (SPI CS line) |  |
| 6 | a modul SPI flash memóriája | ⚠ a panel használja |
| 7 | a modul SPI flash memóriája | ⚠ a panel használja |
| 8 | a modul SPI flash memóriája | ⚠ a panel használja |
| 9 | a modul SPI flash memóriája | ⚠ a panel használja |
| 10 | a modul SPI flash memóriája | ⚠ a panel használja |
| 11 | a modul SPI flash memóriája | ⚠ a panel használja |
| 12 | Ethernet PHY power (LAN8710A) | ⚠ a panel használja |
| 13 | I2C SDA |  |
| 14 | SPI SCLK |  |
| 15 | SPI MISO | ⚠ strapping láb |
| 18 | Ethernet MDIO (LAN8710A) | ⚠ a panel használja |
| 19 | Ethernet RMII TXD0 (LAN8710A) | ⚠ a panel használja |
| 21 | Ethernet RMII TX_EN (LAN8710A) | ⚠ a panel használja |
| 22 | Ethernet RMII TXD1 (LAN8710A) | ⚠ a panel használja |
| 23 | Ethernet MDC (LAN8710A) | ⚠ a panel használja |
| 25 | Ethernet RMII RXD0 (LAN8710A) | ⚠ a panel használja |
| 26 | Ethernet RMII RXD1 (LAN8710A) | ⚠ a panel használja |
| 27 | Ethernet RMII CRS_DV (LAN8710A) | ⚠ a panel használja |
| 33 | I2C SCL |  |
| 34 | szabad - a panel gombja | ⚠ csak bemenet, ADC1 |
| 36 | free (UART RX line) | ⚠ csak bemenet, ADC1 |
| 39 | szabad - bemenet | ⚠ csak bemenet, ADC1 |

A szabad lábak az **EXT** tüskesorokon és az **UEXT** csatlakozón vannak.
A GPIO34-GPIO39 csak bemenet. A modul PSRAM-ja foglalja a GPIO16 / GPIO17
lábat, ezért az Ethernet órajel a GPIO0-n fut, az I2C pedig a GPIO13 /
GPIO33 lábat használja.

## Biztonság

- A panel nem biztonsági funkciókra készült. A vészleállítót, az
  ajtókapcsolót vagy a fényfüggönyt hardveresen kell bekötni, soha nem
  programon keresztül.
- A GPIO lábak 3,3 V-osak. Egy 24 V-os bemenethez optocsatoló vagy
  szintillesztő kell; egy relétekercshez meghajtó kell (egy relémodulon
  van ilyen).

---

[← Áttekintés](README.hu.md) | [Áttekintés](README.hu.md) | [A runtime telepítése →](install.hu.md)
