---
title: Olimex ESP32-DevKit-LiPo
slug: olimex-esp32-devkit-lipo
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-devkit-lipo/
image: img/board-01.jpg
image_alt: Az Olimex ESP32-DevKit-LiPo panel a két tüskesorával és a micro-USB csatlakozóval
tags:
- esp32
- wifi
- battery
- olimex
---

# Olimex ESP32-DevKit-LiPo

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32](https://img.shields.io/badge/chip-ESP32-334155) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a)

![Az Olimex ESP32-DevKit-LiPo panel a két tüskesorával és a micro-USB csatlakozóval](img/board-01.jpg)

Az Olimex ESP32-DevKit-LiPo egy nyílt forrású ESP32 fejlesztőpanel Wi-Fi-vel, a modul összes GPIO-jával két tüskesoron és egy Li-Po töltővel, amely áramszünetkor is működésben tartja. A ctrl32-vel kis Wi-Fi-s PLC: létraprogram a chipen, bemenetek és kimenetek a lábain, a kezelőoldala bármely böngészőben (WEBview), Modbus TCP és MQTT.

**Mire jó:**

- Wi-Fi-s vezérlés egy szobához, egy üvegházhoz vagy egy szivattyúhoz
- Akkumulátoros adatgyűjtő, amely MQTT-n tesz közzé
- A ctrl32 megismerése próbapanelen

A panel oldala a katalógusban: [Olimex ESP32-DevKit-LiPo](https://ctrl32.com/hardware/boards/olimex-esp32-devkit-lipo/)

![Olimex ESP32-DevKit-LiPo - lábkiosztás: minden GPIO funkciója a ctrl32-ben](pinout/pinout.png)

## Mire képes a ctrl32 ezen a panelen

<!-- capabilities:start -->
| Funkció | Ezen a panelen | Megjegyzés |
|---|---|---|
| Chip | ESP32 (ESP32-WROOM-32E-N4) |  |
| Memória | 4 MB flash |  |
| Programméret | 128 változó, 32 riasztás, 128 blokk | a szerkesztő letöltés előtt ellenőrzi |
| Digitális bemenetek / kimenetek | 19 szabad GPIO | 4 ebből csak bemenet |
| Analóg bemenetek | 6 a chipen (ADC1) | GPIO32, GPIO33, GPIO34, GPIO35, GPIO36, GPIO39 |
| Ethernet | nem |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 - szabad lábakon | külső adó-vevő kell hozzá |
| Modbus RTU (RS-485) | igen - szabad lábakon | külső adó-vevő kell hozzá |
| Modbus TCP | kliens és szerver |  |
| MQTT | igen | Home Assistant discovery |
| WEBview | igen | a kezelőoldal bármely böngészőben |
| Kijelző / érintés (HMI) | nem | a kezelőoldal a WEBview |
| USB | Micro-USB (CH340 USB-UART) |  |
| Tápellátás | 5 V USB, 3.7 V Li-Po / Li-Ion |  |
<!-- capabilities:end -->

### Ami nem támogatott

- Bluetooth - az ESP32-ben megvan, a ctrl32 nem használja.
- Az akkumulátor- és tápfigyelő bemenetek (GPIO35 / GPIO39) a ctrl32-ben szabad lábak, nem töltöttségjelzők.

## Az útmutató

| Lépés | Oldal |
|---|---|
| 1 | [Hardver és bekötés](hardware.hu.md) - amire szükséged van, tápellátás, lábkiosztás |
| 2 | [A runtime telepítése](install.hu.md) - a szerkesztő, a panel, az első feltöltés |
| 3 | [Beállítás](configure.hu.md) - hálózat, I/O, kommunikáció |
| 4 | [Példaprojektek](examples/README.hu.md) - minden, amire a panel képes, megnyitásra készen |
| - | [Hibaelhárítás](troubleshooting.hu.md) |

## Fájlok

-

## Tovább

- [ctrl32 dokumentáció](https://ctrl32.com/docs/) - a szerkesztő, a nyelvek, minden blokk
- [A szerkesztő letöltése](https://ctrl32.com/download/)
- [Minden tesztelt panel](../../README.hu.md)
- Olimex ESP32-S3-DevKit-Lipo - ugyanez az ötlet ESP32-S3-mal és PSRAM-mal

