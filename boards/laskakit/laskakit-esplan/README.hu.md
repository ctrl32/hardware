---
title: LaskaKit ESPlan
slug: laskakit-esplan
sidebar_position: 10
hardware: /hardware/boards/laskakit-esplan/
image: img/board-01.jpg
image_alt: A LaskaKit ESPlan panel az Ethernet aljzattal, az RS-485 sorkapoccsal és a tápsorkapoccsal
tags:
- esp32
- ethernet
- rs485
- modbus
- laskakit
---

# LaskaKit ESPlan

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32](https://img.shields.io/badge/chip-ESP32-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a)

![A LaskaKit ESPlan panel az Ethernet aljzattal, az RS-485 sorkapoccsal és a tápsorkapoccsal](img/board-01.jpg)

A LaskaKit ESPlan egy ipari ESP32 panel: 10/100-as Ethernet, védett RS-485 interfész kapcsolható lezárással, Wi-Fi és széles, 7-40 V-os tápellátás csavaros sorkapcson (vagy PoE egy kiegészítő modullal). A ctrl32-vel Modbus RTU master vagy slave egy kapcsolószekrényben - létraprogram a chipen, RS-485 eszközök olvasása és írása, az értékek Modbus TCP-n, MQTT-n és a kezelőoldalán (WEBview).

**Mire jó:**

- Modbus RTU master mérőkhöz, érzékelőkhöz és hajtásokhoz, 24 V-os táppal
- Modbus RTU / TCP átjáró saját logikával
- Épületautomatizálás egy kapcsolószekrényben

A panel oldala a katalógusban: [LaskaKit ESPlan](https://ctrl32.com/hardware/boards/laskakit-esplan/)

![LaskaKit ESPlan - lábkiosztás: minden GPIO funkciója a ctrl32-ben](pinout/pinout.png)

## Mire képes a ctrl32 ezen a panelen

<!-- capabilities:start -->
| Funkció | Ezen a panelen | Megjegyzés |
|---|---|---|
| Chip | ESP32 (ESP32-WROOM-32E-N4) |  |
| Memória | 4 MB flash |  |
| Programméret | 128 változó, 32 riasztás, 128 blokk | a szerkesztő letöltés előtt ellenőrzi |
| Digitális bemenetek / kimenetek | 5 szabad GPIO | 2 ebből csak bemenet |
| Analóg bemenetek | 2 a chipen (ADC1) | GPIO35, GPIO39 |
| Ethernet | igen - LAN8720A |  |
| Power over Ethernet | IEEE 802.3af |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 - szabad lábakon | külső adó-vevő kell hozzá |
| Modbus RTU (RS-485) | igen |  |
| Modbus TCP | kliens és szerver |  |
| MQTT | igen | Home Assistant discovery |
| WEBview | igen | a kezelőoldal bármely böngészőben |
| Kijelző / érintés (HMI) | nem | a kezelőoldal a WEBview |
| USB | USB-C (CH9102 USB-UART) |  |
| Tápellátás | 5 V USB, PoE |  |
<!-- capabilities:end -->

### Ami nem támogatott

- Bluetooth - az ESP32-ben megvan, a ctrl32 nem használja.
- A microSD foglalat - a ctrl32 a programot és a képernyőket a chip saját flash memóriájában tartja.

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

