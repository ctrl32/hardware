---
title: Raspberry Pi 4 Model B
slug: raspberry-pi-4-model-b
sidebar_position: 10
hardware: /hardware/boards/raspberry-pi-4-model-b/
image: img/board-01.jpg
image_alt: Doska Raspberry Pi 4 Model B zhora
tags:
- raspberry-pi
- linux
- hmi
- opc-ua
- ethercat
---

# Raspberry Pi 4 Model B

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: Linux](https://img.shields.io/badge/chip-Linux-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a) ![CAN: 1](https://img.shields.io/badge/CAN-1-7c3aed)

![Doska Raspberry Pi 4 Model B zhora](img/board-01.jpg)

Raspberry Pi 4 Model B prevádzkuje Linux runtime ctrl32 - najväčší cieľ ctrl32: desaťtisíce premenných, HMI na monitore HDMI, server OPC UA pre SCADA, meniče na EtherCAT, CAN a RS-485 cez HAT alebo USB adaptéry a strojové videnie s kamerou. Editor nainštaluje runtime cez sieť; Pi ho potom spúšťa pri každom štarte.

**Hodí sa na:**

- Riadenie linky s HMI na monitore HDMI a OPC UA do SCADA
- Master EtherCAT pre servomeniče
- Brána medzi Modbus, CAN, OPC UA a MQTT

Stránka dosky v katalógu: [Raspberry Pi 4 Model B](https://ctrl32.com/hardware/boards/raspberry-pi-4-model-b/)

![Raspberry Pi 4 Model B - mapa pinov: funkcia každého GPIO v ctrl32](pinout/pinout.png)

## Čo ctrl32 na tejto doske dokáže

<!-- capabilities:start -->
| Vlastnosť | Na tejto doske | Poznámka |
|---|---|---|
| Čip | Linux |  |
| Veľkosť programu | 20480 premenných, 4096 alarmov, 40960 blokov | editor ho overí pred nahratím |
| Digitálne vstupy / výstupy | cez I/O moduly | Modbus, CANopen, EtherCAT |
| Ethernet | áno |  |
| Wi-Fi | Wi-Fi 5 (2.4 + 5 GHz) |  |
| CAN | cez CAN HAT alebo USB adaptér | SocketCAN, až 4 zbernice |
| Modbus RTU (RS-485) | áno | USB prevodník alebo HAT |
| Modbus TCP | klient aj server |  |
| MQTT | áno (aj TLS) | objavenie v Home Assistant |
| WEBview | áno | stránka operátora v každom prehliadači |
| Server OPC UA | áno |  |
| EtherCAT master | áno | na druhom porte Ethernet |
| Displej (HMI) | HDMI alebo panel DSI | alebo bez displeja s WEBview |
| USB | USB-C |  |
| Napájanie | 5 V USB |  |
<!-- capabilities:end -->

### Čo nie je podporované

- 40-pinový konektor GPIO ako vstupy a výstupy programu - vstupy a výstupy idú cez I/O moduly (Modbus RTU / TCP, CANopen, EtherCAT); konektor nesie zbernice HAT-ov.
- Bluetooth.
- Grafické prostredie (desktop) - runtime kreslí obrazovku sám; systém, ktorý chce, je Raspberry Pi OS Lite.

## Návod

| Krok | Stránka |
|---|---|
| 1 | [Hardvér a zapojenie](hardware.sk.md) - čo treba, napájanie, mapa pinov |
| 2 | [Nahratie runtime](install.sk.md) - editor, doska, prvé nahratie |
| 3 | [Nastavenie](configure.sk.md) - sieť, vstupy a výstupy, komunikácia |
| 4 | [Vzorové projekty](examples/README.sk.md) - všetko, čo doska dokáže, pripravené na otvorenie |
| - | [Riešenie problémov](troubleshooting.sk.md) |

## Súbory

-

## Ďalej

- [Dokumentácia ctrl32](https://ctrl32.com/docs/) - editor, jazyky, každý blok
- [Stiahni editor](https://ctrl32.com/download/)
- [Všetky otestované dosky](../../README.sk.md)
- [Raspberry Pi 5](../raspberry-pi-5/README.sk.md)
- Raspberry Pi 3 Model B+
- [Linux runtime](https://ctrl32.com/docs/linux-runtime/) - čo robí a jeho limity

