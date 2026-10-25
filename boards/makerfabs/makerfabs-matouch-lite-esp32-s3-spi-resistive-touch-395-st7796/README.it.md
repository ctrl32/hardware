---
title: Makerfabs MaTouch Lite ESP32-S3 3.95"
slug: makerfabs-matouch-lite-esp32-s3-spi-resistive-touch-395-st7796
sidebar_position: 10
hardware: /hardware/boards/makerfabs-matouch-lite-esp32-s3-spi-resistive-touch-395-st7796/
image: img/board-01.jpg
image_alt: Scheda Makerfabs MaTouch Lite ESP32-S3 con il suo display touch da 3,95 pollici
tags:
- esp32-s3
- display
- touch
- hmi
- wifi
- makerfabs
---

# Makerfabs MaTouch Lite ESP32-S3 3.95"

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32-S3](https://img.shields.io/badge/chip-ESP32--S3-334155) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a) ![CAN: 1](https://img.shields.io/badge/CAN-1-7c3aed) ![HMI: 320x480](https://img.shields.io/badge/HMI-320x480-0891b2)

![Scheda Makerfabs MaTouch Lite ESP32-S3 con il suo display touch da 3,95 pollici](img/board-01.jpg)

La Makerfabs MaTouch Lite è un pannello touch economico: un display da 3,95" 320 x 480 con touch resistivo su un ESP32-S3 con PSRAM e Wi-Fi. Con ctrl32 è HMI e PLC in uno - schermate disegnate nell'editor sul vetro, accanto un programma ladder, gli stessi valori in qualsiasi browser (WEBview), Modbus TCP, CAN e MQTT. Il touch resistivo funziona anche con i guanti.

**Adatta a:**

- Un piccolo pannello operatore su una macchina, usato con i guanti
- Un termostato a parete o un regolatore di stanza
- Un display CAN per un veicolo o un inverter

Pagina della scheda nel catalogo: [Makerfabs MaTouch Lite ESP32-S3 3.95"](https://ctrl32.com/hardware/boards/makerfabs-matouch-lite-esp32-s3-spi-resistive-touch-395-st7796/)

![Makerfabs MaTouch Lite ESP32-S3 3.95" - mappa dei pin: la funzione di ogni GPIO in ctrl32](pinout/pinout.png)

## Cosa sa fare ctrl32 su questa scheda

<!-- capabilities:start -->
| Funzione | Su questa scheda | Note |
|---|---|---|
| Chip | ESP32-S3 (esp32s3_wroom_1_n16r8) |  |
| Memoria | 16 MB flash, 8 MB PSRAM |  |
| Dimensione del programma | 512 variabili, 128 allarmi, 512 blocchi | l'editor lo verifica prima del download |
| Ingressi / uscite digitali | 4 GPIO liberi | vedi la mappa dei pin |
| Ingressi analogici | 4 sul chip (ADC1) | GPIO4, GPIO5, GPIO6, GPIO7 |
| Ethernet | no |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 | serve un transceiver esterno |
| Modbus RTU (RS-485) | sì | su pin liberi, serve un transceiver esterno |
| Modbus TCP | client e server |  |
| MQTT | sì (anche TLS) | rilevamento in Home Assistant |
| WEBview | sì | la pagina operatore in qualsiasi browser |
| Display / touch (HMI) | 3.95" 320x480, NS2009 |  |
| USB | USB-C (CH340K USB-UART, Native USB) |  |
| Alimentazione | 5 V USB (4.0–5.25 V), 3.7 V Li-Po / Li-Ion |  |
<!-- capabilities:end -->

### Cosa non è supportato

- Bluetooth.
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
- [Makerfabs MaTouch ESP32-P4 7"](../makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/README.it.md) - la sorella maggiore

