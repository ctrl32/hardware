---
title: Olimex ESP32-S3-DevKit-Lipo
slug: olimex-esp32-s3-devkit-lipo
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-s3-devkit-lipo/
image: img/board-01.jpg
image_alt: Scheda Olimex ESP32-S3-DevKit-Lipo con i suoi due connettori USB-C e i connettori a pettine
tags:
- esp32-s3
- wifi
- psram
- battery
- olimex
---

# Olimex ESP32-S3-DevKit-Lipo

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32-S3](https://img.shields.io/badge/chip-ESP32--S3-334155) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a)

![Scheda Olimex ESP32-S3-DevKit-Lipo con i suoi due connettori USB-C e i connettori a pettine](img/board-01.jpg)

La Olimex ESP32-S3-DevKit-Lipo è una scheda ESP32-S3 open source con 8 MB di flash, 8 MB di PSRAM, Wi-Fi, due porte USB-C e un caricabatterie Li-Po. L'S3 con PSRAM è il chip di riferimento di ctrl32: un programma ladder con la dimensione di programma completa, la sua pagina operatore in qualsiasi browser (WEBview), Modbus TCP e MQTT con TLS - tutto tramite Wi-Fi.

**Adatta a:**

- Un PLC Wi-Fi con spazio per crescere - 512 variabili, TLS verso un broker cloud
- Un controllore con batteria tampone che continua a funzionare in caso di mancanza di corrente
- Lo sviluppo di una tua scheda sull'ESP32-S3

Pagina della scheda nel catalogo: [Olimex ESP32-S3-DevKit-Lipo](https://ctrl32.com/hardware/boards/olimex-esp32-s3-devkit-lipo/)

![Olimex ESP32-S3-DevKit-Lipo - mappa dei pin: la funzione di ogni GPIO in ctrl32](pinout/pinout.png)

## Cosa sa fare ctrl32 su questa scheda

<!-- capabilities:start -->
| Funzione | Su questa scheda | Note |
|---|---|---|
| Chip | ESP32-S3 (ESP32-S3-WROOM-1-N8R8) |  |
| Memoria | 8 MB flash, 8 MB PSRAM |  |
| Dimensione del programma | 512 variabili, 128 allarmi, 1024 blocchi | l'editor lo verifica prima del download |
| Ingressi / uscite digitali | 21 GPIO liberi | vedi la mappa dei pin |
| Ingressi analogici | 9 sul chip (ADC1) | GPIO1, GPIO2, GPIO4, GPIO5, GPIO6, GPIO7, GPIO8, GPIO9, GPIO10 |
| Ethernet | no |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 - su pin liberi | serve un transceiver esterno |
| Modbus RTU (RS-485) | sì - su pin liberi | serve un transceiver esterno |
| Modbus TCP | client e server |  |
| MQTT | sì (anche TLS) | rilevamento in Home Assistant |
| WEBview | sì | la pagina operatore in qualsiasi browser |
| Display / touch (HMI) | no | la pagina operatore è WEBview |
| USB | USB-C (CH340X USB-UART, Native USB) |  |
| Alimentazione | 5 V USB, 3.7 V Li-Po / Li-Ion |  |
<!-- capabilities:end -->

### Cosa non è supportato

- Bluetooth - l'ESP32-S3 lo ha, ctrl32 non lo usa.
- Gli ingressi di misura della batteria e dell'alimentazione (GPIO5 / GPIO6) sono in ctrl32 pin liberi, non un indicatore di carica.

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
- [Olimex ESP32-DevKit-LiPo](../olimex-esp32-devkit-lipo/README.it.md) - la versione con l'ESP32 classico

