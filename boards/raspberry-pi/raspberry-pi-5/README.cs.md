---
title: Raspberry Pi 5
slug: raspberry-pi-5
sidebar_position: 10
hardware: /hardware/boards/raspberry-pi-5/
image: img/board-01.jpg
image_alt: Deska Raspberry Pi 5 shora
tags:
- raspberry-pi
- linux
- hmi
- opc-ua
- ethercat
---

# Raspberry Pi 5

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: Linux](https://img.shields.io/badge/chip-Linux-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a) ![CAN: 1](https://img.shields.io/badge/CAN-1-7c3aed)

![Deska Raspberry Pi 5 shora](img/board-01.jpg)

Na Raspberry Pi 5 běží Linux runtime ctrl32 - největší cílová platforma ctrl32: desetitisíce proměnných, HMI na monitoru HDMI, server OPC UA pro SCADA, měniče na EtherCAT, CAN a RS-485 přes HAT nebo USB adaptéry a strojové vidění s kamerou. Editor nainstaluje runtime po síti; Pi ho pak spouští při každém startu.

**Hodí se na:**

- Řízení linky s HMI na monitoru HDMI a OPC UA do SCADA
- Master EtherCAT pro servoměniče
- Brána mezi Modbus, CAN, OPC UA a MQTT

Stránka desky v katalogu: [Raspberry Pi 5](https://ctrl32.com/hardware/boards/raspberry-pi-5/)

![Raspberry Pi 5 - mapa pinů: funkce každého GPIO v ctrl32](pinout/pinout.png)

## Co ctrl32 na této desce umí

<!-- capabilities:start -->
| Vlastnost | Na této desce | Poznámka |
|---|---|---|
| Čip | Linux |  |
| Velikost programu | 20480 proměnných, 4096 alarmů, 40960 bloků | editor ji ověří před nahráním |
| Digitální vstupy / výstupy | přes I/O moduly | Modbus, CANopen, EtherCAT |
| Ethernet | ano |  |
| Wi-Fi | Wi-Fi 5 (2.4 + 5 GHz) |  |
| CAN | přes CAN HAT nebo USB adaptér | SocketCAN, až 4 sběrnice |
| Modbus RTU (RS-485) | ano | USB převodník nebo HAT |
| Modbus TCP | klient i server |  |
| MQTT | ano (i TLS) | objevení v Home Assistant |
| WEBview | ano | stránka operátora v každém prohlížeči |
| Server OPC UA | ano |  |
| EtherCAT master | ano | na druhém portu Ethernet |
| Displej (HMI) | HDMI nebo panel DSI | nebo bez displeje s WEBview |
| USB | USB-C |  |
| Napájení | USB-C PD 5 V / 5 A |  |
<!-- capabilities:end -->

### Co není podporováno

- 40pinový konektor GPIO jako vstupy a výstupy programu - vstupy a výstupy jdou přes I/O moduly (Modbus RTU / TCP, CANopen, EtherCAT); konektor nese sběrnice HATů.
- Bluetooth.
- Grafické prostředí (desktop) - runtime kreslí obrazovku sám; systém, který chce, je Raspberry Pi OS Lite.

## Návod

| Krok | Stránka |
|---|---|
| 1 | [Hardware a zapojení](hardware.cs.md) - co je potřeba, napájení, mapa pinů |
| 2 | [Nahrání runtime](install.cs.md) - editor, deska, první nahrání |
| 3 | [Nastavení](configure.cs.md) - síť, vstupy a výstupy, komunikace |
| 4 | [Vzorové projekty](examples/README.cs.md) - všechno, co deska umí, připravené k otevření |
| - | [Řešení problémů](troubleshooting.cs.md) |

## Soubory

| Soubor | Co |
|---|---|
| [pinout/pinout.svg](pinout/pinout.svg) | mapa pinů, vektorová (i [PNG](pinout/pinout.png)) |
| [raspberry-pi-5-mechanical-drawing.pdf](datasheets/raspberry-pi-5-mechanical-drawing.pdf) | Raspberry Pi 5 mechanical drawing |
| [raspberry-pi-5-rp1-peripherals.pdf](datasheets/raspberry-pi-5-rp1-peripherals.pdf) | RP1 peripherals |
| [raspberry-pi-5-3d.zip](3d/raspberry-pi-5-3d.zip) | 3D model (GLB, v zipu) |
| [NOTICE](https://github.com/ctrl32/hardware/blob/main/NOTICE.md) | odkud jsou fotky, schémata a modely |

## Dále

- [Dokumentace ctrl32](https://ctrl32.com/docs/) - editor, jazyky, každý blok
- [Stáhni editor](https://ctrl32.com/download/)
- Všechny otestované desky
- Raspberry Pi 4 Model B
- Raspberry Pi 3 Model B+
- [Linux runtime](https://ctrl32.com/docs/linux-runtime/) - co dělá a jaké má limity

