---
title: 'Olimex ESP32-P4-DevKit: hardver és bekötés'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-P4-DevKit - lábkiosztás
tags:
- esp32-p4
- ethernet
- olimex
---

# Hardver és bekötés

## Amire szükséged van

- Az Olimex ESP32-P4-DevKit.
- Egy USB-C adatkábel - a feltöltéshez és a tápellátáshoz (5 V).
- Egy Ethernet-kábel és egy szabad port a hálózatodon.
- Egy PC a [ctrl32 szerkesztővel](https://ctrl32.com/download/) (Windows).
- Opcionálisan, az all-in-one példához: a LED (GPIO2) a panelen van; egy nyomógomb a GPIO20 és a GND között; egy 3,3 V-os CAN adó-vevő a GPIO5 / GPIO21 lábon és egy RS-485 adó-vevő a GPIO22 / GPIO23 / GPIO32 (DE) lábon.

## Tápellátás

| Forrás | Hol | Megjegyzés |
|---|---|---|
| USB 5 V | az USB-C csatlakozó | tápellátás, programozás és hibakeresés |
| PoE | a PoE bővítményen keresztül | opcionális |

## Lábkiosztás

![Olimex ESP32-P4-DevKit - lábkiosztás](pinout/pinout.png)

| GPIO | Funkció a ctrl32-ben | Megjegyzés |
|---|---|---|
| 2 | free (LED0 line) |  |
| 4 | SPI SCLK |  |
| 5 | free (SPI CS line) |  |
| 7 | I2C SDA |  |
| 8 | I2C SCL |  |
| 20 | szabad - I/O |  |
| 21 | szabad - I/O |  |
| 22 | szabad - I/O |  |
| 23 | szabad - I/O |  |
| 28 | Ethernet RMII (IP101GRI) | ⚠ a panel használja |
| 29 | Ethernet RMII (IP101GRI) | ⚠ a panel használja |
| 30 | Ethernet RMII (IP101GRI) | ⚠ a panel használja |
| 31 | Ethernet MDC (IP101GRI) | ⚠ a panel használja |
| 32 | szabad - I/O |  |
| 33 | szabad - I/O |  |
| 34 | Ethernet RMII (IP101GRI) | ⚠ a panel használja |
| 35 | Ethernet RMII (IP101GRI) | ⚠ a panel használja |
| 46 | szabad - I/O |  |
| 47 | szabad - I/O |  |
| 48 | szabad - I/O |  |
| 49 | Ethernet RMII (IP101GRI) | ⚠ a panel használja |
| 50 | Ethernet RMII (IP101GRI) | ⚠ a panel használja |
| 51 | Ethernet PHY reset (IP101GRI) | ⚠ a panel használja |
| 52 | Ethernet MDIO (IP101GRI) | ⚠ a panel használja |
| 53 | SPI MOSI |  |
| 54 | SPI MISO |  |

Minden GPIO a két 20 tűs tüskesoron van. Az ESP32-P4-nek nincs olyan
analóg bemenete, amelyet a ctrl32 használ: az analóg jelek egy I2C ADC-n
(egy ADS1115 a pUEXT csatlakozón, I2C GPIO7 / GPIO8) vagy egy Modbus
modulon keresztül mennek.

## Biztonság

- A panel nem biztonsági funkciókra készült. A vészleállítót, az
  ajtókapcsolót vagy a fényfüggönyt hardveresen kell bekötni, soha nem
  programon keresztül.
- A GPIO lábak 3,3 V-osak. Egy 24 V-os jelhez optocsatoló vagy
  szintillesztő kell; egy relétekercshez meghajtó kell (egy relémodulon
  van ilyen).

---

[← Áttekintés](README.hu.md) | [Áttekintés](README.hu.md) | [A runtime telepítése →](install.hu.md)
