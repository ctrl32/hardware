---
title: 'Olimex ESP32-P4-PC: hardver és bekötés'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-P4-PC - lábkiosztás
tags:
- esp32-p4
- ethernet
- ups
- olimex
---

# Hardver és bekötés

## Amire szükséged van

- Az Olimex ESP32-P4-PC.
- Egy USB-C adatkábel - a feltöltéshez és a tápellátáshoz (5 V).
- Egy Ethernet-kábel és egy szabad port a hálózatodon.
- Egy PC a [ctrl32 szerkesztővel](https://ctrl32.com/download/) (Windows).
- Opcionálisan: egy Li-Po cella az akkumulátoros tartalékhoz; az all-in-one példához a felhasználói LED (GPIO2) a panelen van, egy nyomógomb pedig a GPIO14 és a GND közé kerül (EXT1); egy 3,3 V-os CAN adó-vevő a GPIO5 / GPIO15 lábon és egy RS-485 adó-vevő a GPIO16 / GPIO17 / GPIO18 (DE) lábon.

## Tápellátás

| Forrás | Hol | Megjegyzés |
|---|---|---|
| USB 5 V | az USB-C csatlakozó | tápellátás, programozás és hibakeresés |
| Li-Po akkumulátor | az akkumulátor-csatlakozó | a panelen töltődik; átveszi a tápot, ha a táp kiesik (UPS) |
| PoE | a PoE bővítményen keresztül | opcionális |

## Lábkiosztás

![Olimex ESP32-P4-PC - lábkiosztás](pinout/pinout.png)

| GPIO | Funkció a ctrl32-ben | Megjegyzés |
|---|---|---|
| 2 | free (LED0 line) |  |
| 4 | SPI SCLK |  |
| 5 | free (SPI CS line) |  |
| 14 | szabad - I/O |  |
| 15 | szabad - I/O |  |
| 16 | szabad - I/O |  |
| 17 | szabad - I/O |  |
| 18 | szabad - I/O |  |
| 19 | szabad - I/O |  |
| 20 | szabad - I/O |  |
| 21 | USB HUB RST | ⚠  |
| 22 | I2C SDA |  |
| 23 | I2C SCL |  |
| 28 | Ethernet RMII (IP101GRI) | ⚠ a panel használja |
| 29 | Ethernet RMII (IP101GRI) | ⚠ a panel használja |
| 30 | Ethernet RMII (IP101GRI) | ⚠ a panel használja |
| 31 | Ethernet MDC (IP101GRI) | ⚠ a panel használja |
| 32 | szabad - I/O |  |
| 33 | szabad - I/O |  |
| 34 | Ethernet RMII (IP101GRI) | ⚠ a panel használja |
| 35 | Ethernet RMII (IP101GRI) | ⚠ a panel használja |
| 36 | szabad - I/O | ⚠ strapping láb |
| 46 | szabad - I/O |  |
| 47 | szabad - I/O |  |
| 48 | szabad - I/O |  |
| 49 | Ethernet RMII (IP101GRI) | ⚠ a panel használja |
| 50 | Ethernet RMII (IP101GRI) | ⚠ a panel használja |
| 51 | Ethernet PHY reset (IP101GRI) | ⚠ a panel használja |
| 52 | Ethernet MDIO (IP101GRI) | ⚠ a panel használja |
| 53 | SPI MOSI |  |
| 54 | SPI MISO |  |

A szabad lábak a 20 tűs **EXT1** tüskesoron vannak: GPIO14-GPIO20, 32, 33,
36, 46, 47, 48 és a felhasználói LED a GPIO2-n. Az **UEXT** csatlakozó
I2C-t (GPIO22 / GPIO23 - a HDMI híddal közösen), SPI-t (GPIO4 / 53 / 54, CS
GPIO5) és a konzol UART-ot visz. Az ESP32-P4-nek nincs olyan analóg
bemenete, amelyet a ctrl32 használ: az analóg jelek egy I2C ADC-n (egy
ADS1115 az UEXT-en) vagy egy Modbus modulon keresztül mennek. A CAN és az
RS-485 szabad EXT1 lábakra kerül egy 3,3 V-os adó-vevő modullal.

## Biztonság

- A panel nem biztonsági funkciókra készült. A vészleállítót, az
  ajtókapcsolót vagy a fényfüggönyt hardveresen kell bekötni, soha nem
  programon keresztül.
- A GPIO lábak 3,3 V-osak. Egy 24 V-os jelhez optocsatoló vagy
  szintillesztő kell; egy relétekercshez meghajtó kell (egy relémodulon
  van ilyen).

## Fotók

![Olimex ESP32-P4-PC - 1. fotó](img/board-01.jpg)
![Olimex ESP32-P4-PC - 2. fotó](img/board-02.jpg)
![Olimex ESP32-P4-PC - 3. fotó](img/board-03.jpg)
![Olimex ESP32-P4-PC - 4. fotó](img/board-04.jpg)

---

[← Áttekintés](README.hu.md) | [Áttekintés](README.hu.md) | [A runtime telepítése →](install.hu.md)
