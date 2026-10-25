---
title: 'Olimex ESP32-GATEWAY: hardver és bekötés'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-GATEWAY - lábkiosztás
tags:
- esp32
- ethernet
- gateway
- olimex
---

# Hardver és bekötés

## Amire szükséged van

- Az Olimex ESP32-GATEWAY.
- Egy USB-C adatkábel - a feltöltéshez és a tápellátáshoz (5 V).
- Egy Ethernet-kábel és egy szabad port a hálózatodon.
- Egy PC a [ctrl32 szerkesztővel](https://ctrl32.com/download/) (Windows).
- Az all-in-one példa a panel saját gombját (GPIO34) és LED-jét (GPIO33) használja - mást nem kell bekötni.

## Tápellátás

| Forrás | Hol | Megjegyzés |
|---|---|---|
| USB 5 V | az USB-C csatlakozó | tápellátás és programozás |

## Lábkiosztás

![Olimex ESP32-GATEWAY - lábkiosztás](pinout/pinout.png)

| GPIO | Funkció a ctrl32-ben | Megjegyzés |
|---|---|---|
| 2 | SPI MOSI | ⚠ strapping láb |
| 5 | Ethernet PHY power (LAN8710A) | ⚠ a panel használja |
| 6 | a modul SPI flash memóriája | ⚠ a panel használja |
| 7 | a modul SPI flash memóriája | ⚠ a panel használja |
| 8 | a modul SPI flash memóriája | ⚠ a panel használja |
| 9 | a modul SPI flash memóriája | ⚠ a panel használja |
| 10 | a modul SPI flash memóriája | ⚠ a panel használja |
| 11 | a modul SPI flash memóriája | ⚠ a panel használja |
| 13 | free (SPI CS line) |  |
| 14 | SPI SCLK |  |
| 15 | SPI MISO | ⚠ strapping láb |
| 16 | I2C SCL |  |
| 17 | Ethernet 50 MHz clock (LAN8710A) | ⚠ a panel használja |
| 18 | Ethernet MDIO (LAN8710A) | ⚠ a panel használja |
| 19 | Ethernet RMII TXD0 (LAN8710A) | ⚠ a panel használja |
| 21 | Ethernet RMII TX_EN (LAN8710A) | ⚠ a panel használja |
| 22 | Ethernet RMII TXD1 (LAN8710A) | ⚠ a panel használja |
| 23 | Ethernet MDC (LAN8710A) | ⚠ a panel használja |
| 25 | Ethernet RMII RXD0 (LAN8710A) | ⚠ a panel használja |
| 26 | Ethernet RMII RXD1 (LAN8710A) | ⚠ a panel használja |
| 27 | Ethernet RMII CRS_DV (LAN8710A) | ⚠ a panel használja |
| 32 | I2C SDA |  |
| 33 | free (LED0 line) | ADC1 |
| 34 | szabad - a panel gombja | ⚠ csak bemenet, ADC1 |

A 20 tűs **EXT** tüskesor viszi a szabad lábakat és az I2C / SPI vonalakat.
A panel LED-je a GPIO33-on, a gombja a GPIO34-en van (csak bemenet). Kevés
láb marad szabadon: a további I/O Modbus TCP-n vagy I2C chipeken keresztül
megy.

## Biztonság

- A panel nem biztonsági funkciókra készült. A vészleállítót, az
  ajtókapcsolót vagy a fényfüggönyt hardveresen kell bekötni, soha nem
  programon keresztül.
- A GPIO lábak 3,3 V-osak. Egy 24 V-os jelhez optocsatoló vagy
  szintillesztő kell; egy relétekercshez meghajtó kell (egy relémodulon
  van ilyen).

---

[← Áttekintés](README.hu.md) | [Áttekintés](README.hu.md) | [A runtime telepítése →](install.hu.md)
