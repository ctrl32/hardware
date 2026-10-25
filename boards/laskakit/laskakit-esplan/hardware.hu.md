---
title: 'LaskaKit ESPlan: hardver és bekötés'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: LaskaKit ESPlan - lábkiosztás
tags:
- esp32
- ethernet
- rs485
- modbus
- laskakit
---

# Hardver és bekötés

## Amire szükséged van

- A LaskaKit ESPlan.
- Egy USB-C adatkábel - a runtime első feltöltéséhez.
- Tápellátáshoz: 12 vagy 24 V DC a csavaros sorkapcson (7-40 V), vagy 5 V USB-C-n.
- Egy Ethernet-kábel és egy szabad port a hálózatodon.
- Egy PC a [ctrl32 szerkesztővel](https://ctrl32.com/download/) (Windows).
- Opcionálisan, az all-in-one példához: egy Modbus RTU hőmérséklet-érzékelő (unit 1) az RS-485 sorkapcson; egy nyomógomb a GPIO16 és a GND között; egy potenciométer (10 k) a 3,3 V és a GND között, a csúszkája a GPIO35-ön; egy 3,3 V-os CAN adó-vevő a GPIO14 (TX) / GPIO39 (RX) lábon.

## Tápellátás

| Forrás | Hol | Megjegyzés |
|---|---|---|
| 7-40 V DC | a csavaros sorkapocs | 12 vagy 24 V ajánlott |
| USB 5 V | az USB-C csatlakozó | az első feltöltés útja |
| PoE | az opcionális PoE modulon keresztül (802.3af) | kiegészítő |

## Lábkiosztás

![LaskaKit ESPlan - lábkiosztás](pinout/pinout.png)

| GPIO | Funkció a ctrl32-ben | Megjegyzés |
|---|---|---|
| 0 | free (LED0 line) | ⚠ strapping láb |
| 4 | RS485 TX |  |
| 5 | Ethernet PHY power (LAN8720A) | ⚠ a panel használja |
| 6 | a modul SPI flash memóriája | ⚠ a panel használja |
| 7 | a modul SPI flash memóriája | ⚠ a panel használja |
| 8 | a modul SPI flash memóriája | ⚠ a panel használja |
| 9 | a modul SPI flash memóriája | ⚠ a panel használja |
| 10 | a modul SPI flash memóriája | ⚠ a panel használja |
| 11 | a modul SPI flash memóriája | ⚠ a panel használja |
| 12 | SPI MISO | ⚠ strapping láb |
| 13 | SPI MOSI |  |
| 14 | free (SPI SCLK line) |  |
| 15 | SPI CS | ⚠ strapping láb |
| 16 | szabad - I/O |  |
| 17 | Ethernet 50 MHz clock (LAN8720A) | ⚠ a panel használja |
| 18 | Ethernet MDIO (LAN8720A) | ⚠ a panel használja |
| 19 | Ethernet RMII TXD0 (LAN8720A) | ⚠ a panel használja |
| 21 | Ethernet RMII TX_EN (LAN8720A) | ⚠ a panel használja |
| 22 | Ethernet RMII TXD1 (LAN8720A) | ⚠ a panel használja |
| 23 | Ethernet MDC (LAN8720A) | ⚠ a panel használja |
| 25 | Ethernet RMII RXD0 (LAN8720A) | ⚠ a panel használja |
| 26 | Ethernet RMII RXD1 (LAN8720A) | ⚠ a panel használja |
| 27 | Ethernet RMII CRS_DV (LAN8720A) | ⚠ a panel használja |
| 32 | TOUCH SCL |  |
| 33 | TOUCH SDA |  |
| 35 | szabad - bemenet | ⚠ csak bemenet, ADC1 |
| 36 | RS485 RX |  |
| 39 | szabad - bemenet | ⚠ csak bemenet, ADC1 |

**RS-485:** az A és a B a sorkapcson, a WS3081 adó-vevő a GPIO4 (TX) /
GPIO36 (RX) lábon; egy jumper kapcsolja a 120 ohmos lezárást - csak a
vonal két végén állítsd be. Az **uSup** csatlakozók I2C-t (GPIO33 /
GPIO32) és SPI-t visznek. A panel LED-je a GPIO0-n van (strapping láb -
hagyd a program által vezérelt kimenetnek).

## Biztonság

- A panel nem biztonsági funkciókra készült. A vészleállítót, az
  ajtókapcsolót vagy a fényfüggönyt hardveresen kell bekötni, soha nem
  programon keresztül.
- A GPIO lábak 3,3 V-osak. Egy 24 V-os jelhez optocsatoló vagy
  szintillesztő kell; egy relétekercshez meghajtó kell (egy relémodulon
  van ilyen).

---

[← Áttekintés](README.hu.md) | [Áttekintés](README.hu.md) | [A runtime telepítése →](install.hu.md)
