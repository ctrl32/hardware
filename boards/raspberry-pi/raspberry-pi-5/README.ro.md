---
title: Raspberry Pi 5
slug: raspberry-pi-5
sidebar_position: 10
hardware: /hardware/boards/raspberry-pi-5/
image: img/board-01.jpg
image_alt: Placa Raspberry Pi 5, vedere de sus
tags:
- raspberry-pi
- linux
- hmi
- opc-ua
- ethercat
---

# Raspberry Pi 5

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: Linux](https://img.shields.io/badge/chip-Linux-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a) ![CAN: 1](https://img.shields.io/badge/CAN-1-7c3aed)

![Placa Raspberry Pi 5, vedere de sus](img/board-01.jpg)

Raspberry Pi 5 rulează runtime-ul Linux ctrl32 - cea mai mare țintă ctrl32: zeci de mii de variabile, un HMI pe monitorul HDMI, un server OPC UA pentru SCADA, acționări EtherCAT, CAN și RS-485 prin HAT-uri sau adaptoare USB și vedere artificială cu o cameră. Editorul instalează runtime-ul prin rețea; apoi Pi-ul îl pornește la fiecare boot.

**Potrivit pentru:**

- Un controler de linie cu un HMI pe un monitor HDMI și OPC UA către SCADA
- Un master EtherCAT pentru servoacționări
- Un gateway între Modbus, CAN, OPC UA și MQTT

Pagina plăcii în catalog: [Raspberry Pi 5](https://ctrl32.com/hardware/boards/raspberry-pi-5/)

![Raspberry Pi 5 - harta pinilor: funcția fiecărui GPIO în ctrl32](pinout/pinout.png)

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
| USB | USB-C |  |
| Alimentare | USB-C PD 5 V / 5 A |  |
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

| Fișier | Ce |
|---|---|
| [pinout/pinout.svg](pinout/pinout.svg) | harta pinilor, vectorial (și ca [PNG](pinout/pinout.png)) |
| [raspberry-pi-5-mechanical-drawing.pdf](datasheets/raspberry-pi-5-mechanical-drawing.pdf) | Raspberry Pi 5 mechanical drawing |
| [raspberry-pi-5-rp1-peripherals.pdf](datasheets/raspberry-pi-5-rp1-peripherals.pdf) | RP1 peripherals |
| [raspberry-pi-5-3d.zip](3d/raspberry-pi-5-3d.zip) | Model 3D (GLB, arhivat zip) |
| [NOTICE](https://github.com/ctrl32/hardware/blob/main/NOTICE.md) | de unde provin fotografiile, schemele și modelele |

## Pașii următori

- [Documentația ctrl32](https://ctrl32.com/docs/) - editorul, limbajele, fiecare bloc
- [Descarcă editorul](https://ctrl32.com/download/)
- Toate plăcile testate
- Raspberry Pi 4 Model B
- Raspberry Pi 3 Model B+
- [Runtime-ul Linux](https://ctrl32.com/docs/linux-runtime/) - ce face și limitele lui

