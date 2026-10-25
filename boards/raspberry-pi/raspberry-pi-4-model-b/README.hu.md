---
title: Raspberry Pi 4 Model B
slug: raspberry-pi-4-model-b
sidebar_position: 10
hardware: /hardware/boards/raspberry-pi-4-model-b/
image: img/board-01.jpg
image_alt: A Raspberry Pi 4 Model B panel felülnézetből
tags:
- raspberry-pi
- linux
- hmi
- opc-ua
- ethercat
---

# Raspberry Pi 4 Model B

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: Linux](https://img.shields.io/badge/chip-Linux-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a) ![CAN: 1](https://img.shields.io/badge/CAN-1-7c3aed)

![A Raspberry Pi 4 Model B panel felülnézetből](img/board-01.jpg)

A Raspberry Pi 4 Model B a ctrl32 Linux runtime-ot futtatja - ez a ctrl32 legnagyobb célpontja: több tízezer változó, HMI a HDMI monitoron, OPC UA szerver a SCADA számára, EtherCAT hajtások, CAN és RS-485 HAT-okon vagy USB adaptereken keresztül, és gépi látás kamerával. A szerkesztő hálózaton telepíti a runtime-ot; a Pi ezután minden indításkor elindítja.

**Mire jó:**

- Gyártósor-vezérlés HMI-vel egy HDMI monitoron és OPC UA kapcsolattal a SCADA felé
- EtherCAT master szervohajtásokhoz
- Átjáró a Modbus, a CAN, az OPC UA és az MQTT között

A panel oldala a katalógusban: [Raspberry Pi 4 Model B](https://ctrl32.com/hardware/boards/raspberry-pi-4-model-b/)

![Raspberry Pi 4 Model B - lábkiosztás: minden GPIO funkciója a ctrl32-ben](pinout/pinout.png)

## Mire képes a ctrl32 ezen a panelen

<!-- capabilities:start -->
| Funkció | Ezen a panelen | Megjegyzés |
|---|---|---|
| Chip | Linux |  |
| Programméret | 20480 változó, 4096 riasztás, 40960 blokk | a szerkesztő letöltés előtt ellenőrzi |
| Digitális bemenetek / kimenetek | I/O modulokon keresztül | Modbus, CANopen, EtherCAT |
| Ethernet | igen |  |
| Wi-Fi | Wi-Fi 5 (2.4 + 5 GHz) |  |
| CAN | CAN HAT-on vagy USB adapteren keresztül | SocketCAN, akár 4 busz |
| Modbus RTU (RS-485) | igen | USB adapter vagy HAT |
| Modbus TCP | kliens és szerver |  |
| MQTT | igen (TLS is) | Home Assistant discovery |
| WEBview | igen | a kezelőoldal bármely böngészőben |
| OPC UA szerver | igen |  |
| EtherCAT master | igen | egy második Ethernet porton |
| Kijelző (HMI) | HDMI vagy DSI kijelző | vagy kijelző nélkül, WEBview-val |
| USB | USB-C |  |
| Tápellátás | 5 V USB |  |
<!-- capabilities:end -->

### Ami nem támogatott

- A 40 tűs GPIO csatlakozó mint a program bemenetei és kimenetei - a bemenetek és kimenetek I/O modulokon keresztül mennek (Modbus RTU / TCP, CANopen, EtherCAT); a csatlakozó a HAT-ok buszait viszi.
- Bluetooth.
- Asztali környezet - a runtime maga rajzolja a képernyőt; a Raspberry Pi OS Lite az a rendszer, amelyet igényel.

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
- [Raspberry Pi 5](../raspberry-pi-5/README.hu.md)
- Raspberry Pi 3 Model B+
- [A Linux runtime](https://ctrl32.com/docs/linux-runtime/) - mire képes és mik a korlátai

