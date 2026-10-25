---
title: 'Olimex ESP32-DevKit-LiPo: hardver és bekötés'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-DevKit-LiPo - lábkiosztás
tags:
- esp32
- wifi
- battery
- olimex
---

# Hardver és bekötés

## Amire szükséged van

- Az Olimex ESP32-DevKit-LiPo.
- Egy micro-USB adatkábel - a feltöltéshez és a tápellátáshoz (5 V).
- A 2,4 GHz-es Wi-Fi-hálózatod neve és jelszava.
- Egy PC a [ctrl32 szerkesztővel](https://ctrl32.com/download/) (Windows).
- Opcionálisan, az all-in-one példához: egy nyomógomb a GPIO13 és a GND között; egy relémodul vagy egy LED ellenállással a GPIO4-en; egy potenciométer (10 k) a 3,3 V és a GND között, a csúszkája a GPIO32-n; egy 3,3 V-os CAN adó-vevő a GPIO14 / GPIO34 lábon és egy RS-485 adó-vevő a GPIO16 / GPIO36 / GPIO17 (DE) lábon; egy Li-Po cella tartaléknak.

## Tápellátás

| Forrás | Hol | Megjegyzés |
|---|---|---|
| USB 5 V | a micro-USB csatlakozó | tápellátás és programozás |
| Li-Po akkumulátor | az akkumulátor-csatlakozó | a panelen töltődik, átveszi a tápot, ha az USB kiesik |

## Lábkiosztás

![Olimex ESP32-DevKit-LiPo - lábkiosztás](pinout/pinout.png)

| GPIO | Funkció a ctrl32-ben | Megjegyzés |
|---|---|---|
| 4 | szabad - I/O |  |
| 6 | a modul SPI flash memóriája | ⚠ a panel használja |
| 7 | a modul SPI flash memóriája | ⚠ a panel használja |
| 8 | a modul SPI flash memóriája | ⚠ a panel használja |
| 9 | a modul SPI flash memóriája | ⚠ a panel használja |
| 10 | a modul SPI flash memóriája | ⚠ a panel használja |
| 11 | a modul SPI flash memóriája | ⚠ a panel használja |
| 13 | szabad - I/O |  |
| 14 | szabad - I/O |  |
| 16 | szabad - I/O |  |
| 17 | szabad - I/O |  |
| 18 | szabad - I/O |  |
| 19 | szabad - I/O |  |
| 21 | szabad - I/O |  |
| 22 | szabad - I/O |  |
| 23 | szabad - I/O |  |
| 25 | szabad - I/O |  |
| 26 | szabad - I/O |  |
| 27 | szabad - I/O |  |
| 32 | szabad - I/O | ADC1 |
| 33 | szabad - I/O | ADC1 |
| 34 | szabad - bemenet | ⚠ csak bemenet, ADC1 |
| 35 | free (BAT SENSE line) | ⚠ csak bemenet, ADC1 |
| 36 | szabad - bemenet | ⚠ csak bemenet, ADC1 |
| 39 | free (PWR SENSE line) | ⚠ csak bemenet, ADC1 |

A két tüskesor viszi a modul szabad GPIO-it. A GPIO34-GPIO39 csak bemenet;
a GPIO0, 2, 12 és 15 strapping lábak - hagyd őket bemeneteknek, vagy
használat előtt teszteld őket. Egy GND-re kötött gombhoz nem kell
ellenállás: a ctrl32 a chip felhúzó ellenállásával invertálva olvassa.

## Biztonság

- A panel nem biztonsági funkciókra készült. A vészleállítót, az
  ajtókapcsolót vagy a fényfüggönyt hardveresen kell bekötni, soha nem
  programon keresztül.
- A GPIO lábak 3,3 V-osak. Egy 24 V-os jelhez optocsatoló vagy
  szintillesztő kell; egy relétekercshez meghajtó kell (egy relémodulon
  van ilyen).

---

[← Áttekintés](README.hu.md) | [Áttekintés](README.hu.md) | [A runtime telepítése →](install.hu.md)
