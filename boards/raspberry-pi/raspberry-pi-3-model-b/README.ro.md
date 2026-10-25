---
title: Raspberry Pi 3 Model B+
slug: raspberry-pi-3-model-b
sidebar_position: 10
hardware: /hardware/boards/raspberry-pi-3-model-b/
image: img/board-01.jpg
image_alt: Placa Raspberry Pi 3 Model B+, vedere de sus
tags:
- raspberry-pi
- linux
- hmi
- opc-ua
---

# Raspberry Pi 3 Model B+

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: Linux](https://img.shields.io/badge/chip-Linux-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a) ![CAN: 1](https://img.shields.io/badge/CAN-1-7c3aed)

![Placa Raspberry Pi 3 Model B+, vedere de sus](img/board-01.jpg)

Raspberry Pi 3 Model B+ rulează runtime-ul Linux ctrl32: un program mare, un HMI pe monitorul HDMI, un server OPC UA pentru SCADA, CAN și RS-485 prin HAT-uri sau adaptoare USB, Modbus și MQTT. Cu 1 GB de memorie și un Cortex-A53 cu patru nuclee se potrivește pentru un controler de linie sau un gateway; vision cu o cameră cere un Raspberry Pi 4 sau 5.

**Potrivit pentru:**

- Un controler de linie cu un HMI pe un monitor HDMI și OPC UA către SCADA
- Un master EtherCAT pentru servoacționări
- Un gateway între Modbus, CAN, OPC UA și MQTT

Pagina plăcii în catalog: [Raspberry Pi 3 Model B+](https://ctrl32.com/hardware/boards/raspberry-pi-3-model-b/)

![Raspberry Pi 3 Model B+ - harta pinilor: funcția fiecărui GPIO în ctrl32](pinout/pinout.png)

## Ce poate face ctrl32 pe această placă

<!-- capabilities:start -->
| Funcție | Pe această placă | Note |
|---|---|---|
| Cip | Linux |  |
| Mărimea programului | 20480 variabile, 4096 alarme, 40960 blocuri | verificat de editor înainte de descărcare |
| Intrări / ieșiri digitale | prin module I/O | Modbus, CANopen, EtherCAT |
| Ethernet | da |  |
| Wi-Fi | Wi-Fi 5 (2.4 + 5 GHz) |  |
| CAN | printr-un HAT CAN sau un adaptor USB | SocketCAN, până la 4 magistrale |
| Modbus RTU (RS-485) | da | un adaptor USB sau un HAT |
| Modbus TCP | client și server |  |
| MQTT | da (și TLS) | descoperire în Home Assistant |
| WEBview | da | pagina operatorului în orice browser |
| Server OPC UA | da |  |
| EtherCAT master | da | pe un al doilea port Ethernet |
| Afișaj (HMI) | HDMI sau un afișaj DSI | sau fără afișaj, cu WEBview |
| USB | Micro-USB |  |
| Alimentare | 5 V USB |  |
<!-- capabilities:end -->

### Ce nu este suportat

- Conectorul GPIO cu 40 de pini ca I/O al programului - intrările și ieșirile trec prin module I/O (Modbus RTU / TCP, CANopen, EtherCAT); conectorul poartă magistralele HAT-urilor.
- Bluetooth.
- Un mediu desktop - runtime-ul desenează singur ecranul; sistemul pe care îl vrea este Raspberry Pi OS Lite.

## Ghidul

| Pas | Pagină |
|---|---|
| 1 | [Hardware și cablare](hardware.ro.md) - de ce ai nevoie, alimentarea, harta pinilor |
| 2 | [Instalarea runtime-ului](install.ro.md) - editorul, placa, prima încărcare |
| 3 | [Configurare](configure.ro.md) - rețea, I/O, comunicație |
| 4 | [Proiecte exemplu](examples/README.ro.md) - tot ce face placa, gata de deschis |
| - | [Depanare](troubleshooting.ro.md) |

## Fișiere

-

## Pașii următori

- [Documentația ctrl32](https://ctrl32.com/docs/) - editorul, limbajele, fiecare bloc
- [Descarcă editorul](https://ctrl32.com/download/)
- [Toate plăcile testate](../../README.ro.md)
- [Raspberry Pi 5](../raspberry-pi-5/README.ro.md)
- [Raspberry Pi 4 Model B](../raspberry-pi-4-model-b/README.ro.md)
- [Runtime-ul Linux](https://ctrl32.com/docs/linux-runtime/) - ce face și limitele lui

