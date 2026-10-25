---
title: Raspberry Pi 3 Model B+
slug: raspberry-pi-3-model-b
sidebar_position: 10
hardware: /hardware/boards/raspberry-pi-3-model-b/
image: img/board-01.jpg
image_alt: Scheda Raspberry Pi 3 Model B+ vista dall'alto
tags:
- raspberry-pi
- linux
- hmi
- opc-ua
---

# Raspberry Pi 3 Model B+

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: Linux](https://img.shields.io/badge/chip-Linux-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a) ![CAN: 1](https://img.shields.io/badge/CAN-1-7c3aed)

![Scheda Raspberry Pi 3 Model B+ vista dall'alto](img/board-01.jpg)

Il Raspberry Pi 3 Model B+ esegue il runtime Linux di ctrl32: un programma grande, un HMI sul monitor HDMI, un server OPC UA per lo SCADA, CAN e RS-485 tramite HAT o adattatori USB, Modbus e MQTT. Con 1 GB di memoria e un Cortex-A53 quad core è adatto a un controllore di linea o a un gateway; la visione con una fotocamera richiede un Raspberry Pi 4 o 5.

**Adatta a:**

- Un controllore di linea con un HMI su un monitor HDMI e OPC UA verso lo SCADA
- Un master EtherCAT per servoazionamenti
- Un gateway tra Modbus, CAN, OPC UA e MQTT

Pagina della scheda nel catalogo: [Raspberry Pi 3 Model B+](https://ctrl32.com/hardware/boards/raspberry-pi-3-model-b/)

![Raspberry Pi 3 Model B+ - mappa dei pin: la funzione di ogni GPIO in ctrl32](pinout/pinout.png)

## Cosa sa fare ctrl32 su questa scheda

<!-- capabilities:start -->
| Funzione | Su questa scheda | Note |
|---|---|---|
| Chip | Linux |  |
| Dimensione del programma | 20480 variabili, 4096 allarmi, 40960 blocchi | l'editor lo verifica prima del download |
| Ingressi / uscite digitali | tramite moduli I/O | Modbus, CANopen, EtherCAT |
| Ethernet | sì |  |
| Wi-Fi | Wi-Fi 5 (2.4 + 5 GHz) |  |
| CAN | tramite un CAN HAT o un adattatore USB | SocketCAN, fino a 4 bus |
| Modbus RTU (RS-485) | sì | un adattatore USB o un HAT |
| Modbus TCP | client e server |  |
| MQTT | sì (anche TLS) | rilevamento in Home Assistant |
| WEBview | sì | la pagina operatore in qualsiasi browser |
| Server OPC UA | sì |  |
| EtherCAT master | sì | su una seconda porta Ethernet |
| Display (HMI) | HDMI o un pannello DSI | oppure senza display con WEBview |
| USB | Micro-USB |  |
| Alimentazione | 5 V USB |  |
<!-- capabilities:end -->

### Cosa non è supportato

- Il connettore GPIO a 40 pin come I/O del programma - ingressi e uscite passano tramite moduli I/O (Modbus RTU / TCP, CANopen, EtherCAT); il connettore porta i bus degli HAT.
- Bluetooth.
- Un ambiente desktop - il runtime disegna lo schermo da solo; il sistema che richiede è Raspberry Pi OS Lite.

## La guida

| Passo | Pagina |
|---|---|
| 1 | [Hardware e cablaggio](hardware.it.md) - cosa ti serve, alimentazione, la mappa dei pin |
| 2 | [Installare il runtime](install.it.md) - l'editor, la scheda, il primo caricamento |
| 3 | [Configurare](configure.it.md) - rete, I/O, comunicazione |
| 4 | [Progetti di esempio](examples/README.it.md) - tutto ciò che la scheda sa fare, pronto da aprire |
| - | [Risoluzione dei problemi](troubleshooting.it.md) |

## File

-

## Passi successivi

- [Documentazione ctrl32](https://ctrl32.com/docs/) - l'editor, i linguaggi, ogni blocco
- [Scarica l'editor](https://ctrl32.com/download/)
- [Tutte le schede testate](../../README.it.md)
- [Raspberry Pi 5](../raspberry-pi-5/README.it.md)
- [Raspberry Pi 4 Model B](../raspberry-pi-4-model-b/README.it.md)
- [Il runtime Linux](https://ctrl32.com/docs/linux-runtime/) - cosa fa e i suoi limiti

