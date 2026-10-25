---
title: Olimex ESP32-P4-PC
slug: olimex-esp32-p4-pc
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-p4-pc/
image: img/board-01.jpg
image_alt: Scheda Olimex ESP32-P4-PC con il connettore Ethernet, le porte USB e il connettore HDMI
tags:
- esp32-p4
- ethernet
- ups
- olimex
---

# Olimex ESP32-P4-PC

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32-P4](https://img.shields.io/badge/chip-ESP32--P4-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a)

![Scheda Olimex ESP32-P4-PC con il connettore Ethernet, le porte USB e il connettore HDMI](img/board-01.jpg)

L'Olimex ESP32-P4-PC è un piccolo computer basato sull'ESP32-P4 - dual core a 400 MHz con 32 MB di PSRAM - con Ethernet a 100 Mb, quattro porte USB host, HDMI, audio e una batteria Li-Po che lo mantiene in funzione in caso di mancanza di corrente. Con ctrl32 è un controllore cablato con il programma più grande che un ESP32 esegua - 4096 variabili - con la sua pagina operatore in qualsiasi browser (WEBview), Modbus TCP, MQTT con TLS e CAN o RS-485 sui pin liberi del suo connettore.

**Adatta a:**

- Un PLC cablato che supera una mancanza di corrente con la propria batteria
- Un gateway con logica impegnativa tra Modbus TCP, CAN e MQTT
- Un controllore in un contenitore, alimentato tramite PoE (con l'estensione)

Pagina della scheda nel catalogo: [Olimex ESP32-P4-PC](https://ctrl32.com/hardware/boards/olimex-esp32-p4-pc/)

![Olimex ESP32-P4-PC - mappa dei pin: la funzione di ogni GPIO in ctrl32](pinout/pinout.png)

## Cosa sa fare ctrl32 su questa scheda

<!-- capabilities:start -->
| Funzione | Su questa scheda | Note |
|---|---|---|
| Chip | ESP32-P4 (ESP32-P4NRW32) |  |
| Memoria | 16 MB flash, 32 MB PSRAM |  |
| Dimensione del programma | 4096 variabili, 512 allarmi, 1024 blocchi | l'editor lo verifica prima del download |
| Ingressi / uscite digitali | 15 GPIO liberi | vedi la mappa dei pin |
| Ingressi analogici | tramite un ADC I2C (ADS1115) |  |
| Ethernet | sì - IP101GRI |  |
| Wi-Fi | no |  |
| CAN (TWAI) | 1 - su pin liberi | serve un transceiver esterno |
| Modbus RTU (RS-485) | sì - su pin liberi | serve un transceiver esterno |
| Modbus TCP | client e server |  |
| MQTT | sì (anche TLS) | rilevamento in Home Assistant |
| WEBview | sì | la pagina operatore in qualsiasi browser |
| Display / touch (HMI) | no | la pagina operatore è WEBview |
| USB | USB-C (Native USB) |  |
| Alimentazione | 5 V USB, 3.7 V Li-Po / Li-Ion, PoE |  |
<!-- capabilities:end -->

### Cosa non è supportato

- L'uscita HDMI e i connettori MIPI DSI / CSI - in ctrl32 questa scheda funziona senza display (la pagina operatore è WEBview).
- Le porte USB host e l'uscita audio.
- Lo slot microSD - ctrl32 tiene il programma e le schermate nella flash della scheda.

## La guida

| Passo | Pagina |
|---|---|
| 1 | [Hardware e cablaggio](hardware.it.md) - cosa ti serve, alimentazione, la mappa dei pin |
| 2 | [Installare il runtime](install.it.md) - l'editor, la scheda, il primo caricamento |
| 3 | [Configurare](configure.it.md) - rete, I/O, comunicazione |
| 4 | [Progetti di esempio](examples/README.it.md) - tutto ciò che la scheda sa fare, pronto da aprire |
| - | [Risoluzione dei problemi](troubleshooting.it.md) |

## File

| File | Cosa |
|---|---|
| [pinout/pinout.svg](pinout/pinout.svg) | la mappa dei pin, vettoriale (anche [PNG](pinout/pinout.png)) |
| [olimex-esp32-p4-pc-schematic.pdf](schematics/olimex-esp32-p4-pc-schematic.pdf) | ESP32-P4-PC schematic Rev C |
| [esp32-p4-pc-rev-c-kicad.zip](schematics/esp32-p4-pc-rev-c-kicad.zip) | KiCad project |
| [olimex-esp32-p4-pc-user-manual.pdf](datasheets/olimex-esp32-p4-pc-user-manual.pdf) | ESP32-P4-PC user manual |
| [NOTICE](https://github.com/ctrl32/hardware/blob/main/NOTICE.md) | da dove provengono foto, schemi e modelli |

## Passi successivi

- [Documentazione ctrl32](https://ctrl32.com/docs/) - l'editor, i linguaggi, ogni blocco
- [Scarica l'editor](https://ctrl32.com/download/)
- [Tutte le schede testate](../../README.it.md)
- [Olimex ESP32-P4-DevKit](../olimex-esp32-p4-devkit/README.it.md) - lo stesso ESP32-P4 su una scheda più piccola

