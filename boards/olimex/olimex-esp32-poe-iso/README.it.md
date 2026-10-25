---
title: Olimex ESP32-PoE-ISO
slug: olimex-esp32-poe-iso
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-poe-iso/
image: img/board-01.jpg
image_alt: Scheda Olimex ESP32-PoE-ISO con il connettore Ethernet e l'alimentazione PoE isolata
tags:
- esp32
- ethernet
- poe
- isolated
- olimex
---

# Olimex ESP32-PoE-ISO

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32](https://img.shields.io/badge/chip-ESP32-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a)

![Scheda Olimex ESP32-PoE-ISO con il connettore Ethernet e l'alimentazione PoE isolata](img/board-01.jpg)

La Olimex ESP32-PoE-ISO è la ESP32-PoE con un'alimentazione Power over Ethernet isolata galvanicamente: un solo cavo di rete la alimenta e porta il suo collegamento, e un PC può restare collegato tramite USB mentre la scheda funziona in PoE. Con ctrl32 è un PLC compatto per quadro elettrico - un programma ladder sul chip, la sua pagina operatore in qualsiasi browser (WEBview), Modbus TCP verso contatori e moduli I/O e MQTT verso Home Assistant.

**Adatta a:**

- Un piccolo PLC in quadro elettrico, alimentato da uno switch PoE
- Un gateway Modbus TCP che legge i contatori e li pubblica tramite MQTT
- Domotica - una stanza o un locale caldaia su un solo cavo

Pagina della scheda nel catalogo: [Olimex ESP32-PoE-ISO](https://ctrl32.com/hardware/boards/olimex-esp32-poe-iso/)

![Olimex ESP32-PoE-ISO - mappa dei pin: la funzione di ogni GPIO in ctrl32](pinout/pinout.png)

## Cosa sa fare ctrl32 su questa scheda

<!-- capabilities:start -->
| Funzione | Su questa scheda | Note |
|---|---|---|
| Chip | ESP32 (ESP32-WROOM-32E-N4) |  |
| Memoria | 4 MB flash |  |
| Dimensione del programma | 128 variabili, 32 allarmi, 128 blocchi | l'editor lo verifica prima del download |
| Ingressi / uscite digitali | 6 GPIO liberi | 3 di cui solo ingressi |
| Ingressi analogici | 4 sul chip (ADC1) | GPIO33, GPIO34, GPIO35, GPIO36 |
| Ethernet | sì - LAN8710A |  |
| Power over Ethernet | IEEE 802.3af |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 - su pin liberi | serve un transceiver esterno |
| Modbus RTU (RS-485) | sì - su pin liberi | serve un transceiver esterno |
| Modbus TCP | client e server |  |
| MQTT | sì | rilevamento in Home Assistant |
| WEBview | sì | la pagina operatore in qualsiasi browser |
| Display / touch (HMI) | no | la pagina operatore è WEBview |
| USB | Micro-USB (CH340T USB-UART) |  |
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
- [Olimex ESP32-PoE](../olimex-esp32-poe/README.it.md) - la stessa scheda senza l'alimentazione isolata
- Olimex ESP32-POE2 - la generazione successiva

