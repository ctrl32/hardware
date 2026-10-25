---
title: Olimex ESP32-P4-DevKit
slug: olimex-esp32-p4-devkit
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-p4-devkit/
image: img/board-01.jpg
image_alt: Scheda Olimex ESP32-P4-DevKit con il connettore Ethernet e i connettori a pettine
tags:
- esp32-p4
- ethernet
- olimex
---

# Olimex ESP32-P4-DevKit

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32-P4](https://img.shields.io/badge/chip-ESP32--P4-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a)

![Scheda Olimex ESP32-P4-DevKit con il connettore Ethernet e i connettori a pettine](img/board-01.jpg)

La Olimex ESP32-P4-DevKit è una piccola scheda open source con l'ESP32-P4 - l'ESP32 più veloce, dual core a 400 MHz con 32 MB di PSRAM - ed Ethernet a 100 Mb. Non ha Wi-Fi: è un controllore cablato. Con ctrl32 esegue i programmi più grandi che un ESP32 può eseguire - 4096 variabili - con la sua pagina operatore in qualsiasi browser (WEBview), Modbus TCP e MQTT con TLS.

**Adatta a:**

- Un PLC cablato con un programma grande e molti dispositivi Modbus
- Un gateway con logica impegnativa tra Modbus TCP e MQTT
- Lo sviluppo di una tua scheda P4

Pagina della scheda nel catalogo: [Olimex ESP32-P4-DevKit](https://ctrl32.com/hardware/boards/olimex-esp32-p4-devkit/)

![Olimex ESP32-P4-DevKit - mappa dei pin: la funzione di ogni GPIO in ctrl32](pinout/pinout.png)

## Cosa sa fare ctrl32 su questa scheda

<!-- capabilities:start -->
| Funzione | Su questa scheda | Note |
|---|---|---|
| Chip | ESP32-P4 (ESP32-P4NRW32) |  |
| Memoria | 16 MB flash, 32 MB PSRAM |  |
| Dimensione del programma | 4096 variabili, 512 allarmi, 1024 blocchi | l'editor lo verifica prima del download |
| Ingressi / uscite digitali | 11 GPIO liberi | vedi la mappa dei pin |
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
| Alimentazione | 5 V USB, PoE |  |
<!-- capabilities:end -->

### Cosa non è supportato

- I connettori per il display MIPI DSI e la fotocamera CSI - in ctrl32 questa scheda funziona senza display (la pagina operatore è WEBview).
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

-

## Passi successivi

- [Documentazione ctrl32](https://ctrl32.com/docs/) - l'editor, i linguaggi, ogni blocco
- [Scarica l'editor](https://ctrl32.com/download/)
- [Tutte le schede testate](../../README.it.md)
- [Makerfabs MaTouch ESP32-P4 7"](../../makerfabs/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/README.it.md) - l'ESP32-P4 con uno schermo touch da 7"

