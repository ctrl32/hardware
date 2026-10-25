---
title: Olimex ESP32-POE2
slug: olimex-esp32-poe2
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-poe2/
image: img/board-01.jpg
image_alt: Scheda Olimex ESP32-POE2 con il connettore Ethernet e le uscite di alimentazione
tags:
- esp32
- ethernet
- poe
- psram
- olimex
---

# Olimex ESP32-POE2

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32](https://img.shields.io/badge/chip-ESP32-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a)

![Scheda Olimex ESP32-POE2 con il connettore Ethernet e le uscite di alimentazione](img/board-01.jpg)

La Olimex ESP32-POE2 è la generazione successiva della ESP32-PoE: un ESP32 con 8 MB di PSRAM, Ethernet e Power over Ethernet IEEE 802.3at che alimenta anche i tuoi dispositivi di campo - uscite a 24 V o 12 V, 5 V e 3,3 V, fino a 25 W dal cavo di rete. Con ctrl32 è un PLC in quadro elettrico alimentato da un solo cavo: logica ladder, WEBview, Modbus TCP e MQTT, con la dimensione di programma completa di un ESP32 classico con PSRAM.

**Adatta a:**

- Un PLC da quadro che alimenta i suoi sensori e un piccolo modulo relè dal PoE
- Un gateway Modbus TCP con MQTT verso Home Assistant
- Building automation con un cavo per stanza

Pagina della scheda nel catalogo: [Olimex ESP32-POE2](https://ctrl32.com/hardware/boards/olimex-esp32-poe2/)

![Olimex ESP32-POE2 - mappa dei pin: la funzione di ogni GPIO in ctrl32](pinout/pinout.png)

## Cosa sa fare ctrl32 su questa scheda

<!-- capabilities:start -->
| Funzione | Su questa scheda | Note |
|---|---|---|
| Chip | ESP32 (ESP32-WROVER-E-N4R8) |  |
| Memoria | 4 MB flash, 8 MB PSRAM |  |
| Dimensione del programma | 512 variabili, 128 allarmi, 1024 blocchi | l'editor lo verifica prima del download |
| Ingressi / uscite digitali | 5 GPIO liberi | 3 di cui solo ingressi |
| Ingressi analogici | 3 sul chip (ADC1) | GPIO34, GPIO36, GPIO39 |
| Ethernet | sì - LAN8710A |  |
| Power over Ethernet | IEEE 802.3at |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 - su pin liberi | serve un transceiver esterno |
| Modbus RTU (RS-485) | sì - su pin liberi | serve un transceiver esterno |
| Modbus TCP | client e server |  |
| MQTT | sì | rilevamento in Home Assistant |
| WEBview | sì | la pagina operatore in qualsiasi browser |
| Display / touch (HMI) | no | la pagina operatore è WEBview |
| USB | USB-C |  |
| Alimentazione | 5 V USB, 3.7 V Li-Po / Li-Ion, PoE |  |
<!-- capabilities:end -->

### Cosa non è supportato

- Bluetooth - l'ESP32 lo ha, ctrl32 non lo usa.
- Lo slot microSD - ctrl32 tiene il programma e le schermate nella flash propria del chip.
- L'ingresso della batteria funziona come funzione propria della scheda; ctrl32 non legge il livello della batteria.

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
- [Olimex ESP32-PoE](../olimex-esp32-poe/README.it.md) - la prima generazione
- [Olimex ESP32-PoE-ISO](../olimex-esp32-poe-iso/README.it.md) - con un'alimentazione PoE isolata

