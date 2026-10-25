---
title: Olimex ESP32-EVB
slug: olimex-esp32-evb
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-evb/
image: img/board-01.jpg
image_alt: Scheda Olimex ESP32-EVB con i suoi due relè, il connettore Ethernet e il morsetto CAN
tags:
- esp32
- ethernet
- can
- relay
- olimex
---

# Olimex ESP32-EVB

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32](https://img.shields.io/badge/chip-ESP32-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a) ![CAN: 1](https://img.shields.io/badge/CAN-1-7c3aed) ![HMI: 240x320](https://img.shields.io/badge/HMI-240x320-0891b2)

![Scheda Olimex ESP32-EVB con i suoi due relè, il connettore Ethernet e il morsetto CAN](img/board-01.jpg)

La Olimex ESP32-EVB è una scheda ESP32 costruita per il controllo: due relè (10 A / 250 VAC), un transceiver CAN, Ethernet e Wi-Fi su una sola scheda. Con ctrl32 è un PLC pronto - i relè e il pulsante sono variabili di un programma ladder, il CAN parla con azionamenti e nodi I/O, e la pagina operatore gira in qualsiasi browser (WEBview). Un display touch opzionale da 2,8" sul connettore UEXT la trasforma in un piccolo pannello.

**Adatta a:**

- Un controllore a relè - riscaldamento, pompe, luci - con Ethernet
- Un master CAN per un azionamento o nodi I/O CANopen
- Un termostato o un piccolo pannello con il display opzionale da 2,8"

Pagina della scheda nel catalogo: [Olimex ESP32-EVB](https://ctrl32.com/hardware/boards/olimex-esp32-evb/)

![Olimex ESP32-EVB - mappa dei pin: la funzione di ogni GPIO in ctrl32](pinout/pinout.png)

## Cosa sa fare ctrl32 su questa scheda

<!-- capabilities:start -->
| Funzione | Su questa scheda | Note |
|---|---|---|
| Chip | ESP32 (ESP32-WROOM-32E-N4) |  |
| Memoria | 4 MB flash |  |
| Dimensione del programma | 128 variabili, 32 allarmi, 128 blocchi | l'editor lo verifica prima del download |
| Ingressi / uscite digitali | 6 GPIO liberi | 2 di cui solo ingressi |
| Ingressi analogici | 4 sul chip (ADC1) | GPIO32, GPIO33, GPIO34, GPIO36 |
| Ethernet | sì - LAN8710A |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 |  |
| Modbus RTU (RS-485) | sì - su pin liberi | serve un transceiver esterno |
| Modbus TCP | client e server |  |
| MQTT | sì | rilevamento in Home Assistant |
| WEBview | sì | la pagina operatore in qualsiasi browser |
| Display / touch (HMI) | - 240x320, - |  |
| USB | Micro-USB (CH340T USB-UART) |  |
| Alimentazione | 5 V USB, 3.7 V Li-Po / Li-Ion |  |
<!-- capabilities:end -->

### Cosa non è supportato

- Bluetooth.
- Il ricevitore e il trasmettitore IR - ctrl32 non li usa su questa scheda.
- Lo slot microSD - ctrl32 tiene il programma e le schermate nella flash propria del chip.

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
- [Olimex ESP32-PoE](../olimex-esp32-poe/README.it.md) - Ethernet e Power over Ethernet

