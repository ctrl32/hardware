---
title: Olimex ESP32-DevKit-LiPo
slug: olimex-esp32-devkit-lipo
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-devkit-lipo/
image: img/board-01.jpg
image_alt: Scheda Olimex ESP32-DevKit-LiPo con i suoi due connettori a pettine e il connettore micro-USB
tags:
- esp32
- wifi
- battery
- olimex
---

# Olimex ESP32-DevKit-LiPo

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32](https://img.shields.io/badge/chip-ESP32-334155) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a)

![Scheda Olimex ESP32-DevKit-LiPo con i suoi due connettori a pettine e il connettore micro-USB](img/board-01.jpg)

La Olimex ESP32-DevKit-LiPo è una scheda di sviluppo ESP32 open source con Wi-Fi, tutti i GPIO del modulo su due connettori a pettine e un caricabatterie Li-Po che la mantiene in funzione quando manca la corrente. Con ctrl32 è un piccolo PLC Wi-Fi: un programma ladder sul chip, ingressi e uscite sui suoi pin, la sua pagina operatore in qualsiasi browser (WEBview), Modbus TCP e MQTT.

**Adatta a:**

- Un controllore Wi-Fi per una stanza, una serra o una pompa
- Un data logger con batteria tampone che pubblica tramite MQTT
- Imparare ctrl32 su una breadboard

Pagina della scheda nel catalogo: [Olimex ESP32-DevKit-LiPo](https://ctrl32.com/hardware/boards/olimex-esp32-devkit-lipo/)

![Olimex ESP32-DevKit-LiPo - mappa dei pin: la funzione di ogni GPIO in ctrl32](pinout/pinout.png)

## Cosa sa fare ctrl32 su questa scheda

<!-- capabilities:start -->
| Funzione | Su questa scheda | Note |
|---|---|---|
| Chip | ESP32 (ESP32-WROOM-32E-N4) |  |
| Memoria | 4 MB flash |  |
| Dimensione del programma | 128 variabili, 32 allarmi, 128 blocchi | l'editor lo verifica prima del download |
| Ingressi / uscite digitali | 19 GPIO liberi | 4 di cui solo ingressi |
| Ingressi analogici | 6 sul chip (ADC1) | GPIO32, GPIO33, GPIO34, GPIO35, GPIO36, GPIO39 |
| Ethernet | no |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 - su pin liberi | serve un transceiver esterno |
| Modbus RTU (RS-485) | sì - su pin liberi | serve un transceiver esterno |
| Modbus TCP | client e server |  |
| MQTT | sì | rilevamento in Home Assistant |
| WEBview | sì | la pagina operatore in qualsiasi browser |
| Display / touch (HMI) | no | la pagina operatore è WEBview |
| USB | Micro-USB (CH340 USB-UART) |  |
| Alimentazione | 5 V USB, 3.7 V Li-Po / Li-Ion |  |
<!-- capabilities:end -->

### Cosa non è supportato

- Bluetooth - l'ESP32 lo ha, ctrl32 non lo usa.
- Gli ingressi di misura della batteria e dell'alimentazione (GPIO35 / GPIO39) sono in ctrl32 pin liberi, non un indicatore di carica.

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
- Olimex ESP32-S3-DevKit-Lipo - la stessa idea con l'ESP32-S3 e la PSRAM

