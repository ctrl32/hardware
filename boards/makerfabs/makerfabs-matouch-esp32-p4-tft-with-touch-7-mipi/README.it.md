---
title: Makerfabs MaTouch ESP32-P4 7"
slug: makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi
sidebar_position: 10
hardware: /hardware/boards/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/
image: img/board-01.jpg
image_alt: Scheda Makerfabs MaTouch ESP32-P4 7" con il suo display touch 1024x600
tags:
- esp32-p4
- display
- touch
- hmi
- ethernet
- makerfabs
---

# Makerfabs MaTouch ESP32-P4 7"

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32-P4](https://img.shields.io/badge/chip-ESP32--P4-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a) ![CAN: 1](https://img.shields.io/badge/CAN-1-7c3aed) ![HMI: 1024x600](https://img.shields.io/badge/HMI-1024x600-0891b2)

![Scheda Makerfabs MaTouch ESP32-P4 7" con il suo display touch 1024x600](img/board-01.jpg)

La Makerfabs MaTouch ESP32-P4 7" è un pannello touch completo su una sola scheda: un display MIPI 1024 x 600 con touch capacitivo, l'ESP32-P4 dual core con 32 MB di PSRAM, Ethernet e Wi-Fi 6 tramite un ESP32-C6. Con ctrl32 è HMI e PLC in uno - le schermate disegnate nell'editor girano sul vetro, accanto gira un programma ladder, e gli stessi valori raggiungono qualsiasi browser (WEBview), dispositivi Modbus, CAN e MQTT.

**Adatta a:**

- Un pannello operatore su una macchina, con logica propria
- Un pannello di controllo smart home o building a parete
- Un gateway Modbus / CAN con schermo

Pagina della scheda nel catalogo: [Makerfabs MaTouch ESP32-P4 7"](https://ctrl32.com/hardware/boards/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/)

![Makerfabs MaTouch ESP32-P4 7" - mappa dei pin: la funzione di ogni GPIO in ctrl32](pinout/pinout.png)

## Cosa sa fare ctrl32 su questa scheda

<!-- capabilities:start -->
| Funzione | Su questa scheda | Note |
|---|---|---|
| Chip | ESP32-P4 (ESP32-P4NRW32) |  |
| Memoria | 16 MB flash, 32 MB PSRAM |  |
| Dimensione del programma | 4096 variabili, 512 allarmi, 512 blocchi | l'editor lo verifica prima del download |
| Ingressi / uscite digitali | 12 GPIO liberi | vedi la mappa dei pin |
| Ingressi analogici | tramite un ADC I2C (ADS1115) |  |
| Ethernet | sì - IP101GRI |  |
| Wi-Fi | Wi-Fi 6 (2.4 GHz) |  |
| CAN (TWAI) | 1 | serve un transceiver esterno |
| Modbus RTU (RS-485) | sì | su pin liberi, serve un transceiver esterno |
| Modbus TCP | client e server |  |
| MQTT | sì (anche TLS) | rilevamento in Home Assistant |
| WEBview | sì | la pagina operatore in qualsiasi browser |
| Display / touch (HMI) | 7" 1024x600, GT911 |  |
| USB | USB-C (CH340K USB-UART, Native USB) |  |
| Alimentazione | 5 V USB (4.0–5.25 V), 3.7 V Li-Po / Li-Ion |  |
<!-- capabilities:end -->

### Cosa non è supportato

- La fotocamera (SC2336 su MIPI CSI) - ctrl32 esegue la visione solo sul runtime Linux a 64 bit.
- Il codec audio, il microfono e l'uscita altoparlante.
- Il Bluetooth dell'ESP32-C6.
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
| [makerfabs-matouch_esp32-p4_tft_with_touch_7_v1.2.pdf](schematics/makerfabs-matouch_esp32-p4_tft_with_touch_7_v1.2.pdf) | MaTouch ESP32-P4 TFT with Touch 7“ V1.2 |
| [makerfabs-matouch-p4-7-display-datasheet.pdf](datasheets/makerfabs-matouch-p4-7-display-datasheet.pdf) | 7" 1024x600 MIPI display AML070JGI50 datasheet |
| [makerfabs-matouch-p4-es8311-datasheet.pdf](datasheets/makerfabs-matouch-p4-es8311-datasheet.pdf) | ES8311 audio codec datasheet |
| [esp32-p4-datasheet.pdf](datasheets/esp32-p4-datasheet.pdf) | ESP32-P4 datasheet (pre-release) |
| [makerfabs-matouch-p4-sc2336-camera-datasheet.pdf](datasheets/makerfabs-matouch-p4-sc2336-camera-datasheet.pdf) | SC2336 2 MP MIPI camera module datasheet |
| [NOTICE](https://github.com/ctrl32/hardware/blob/main/NOTICE.md) | da dove provengono foto, schemi e modelli |

## Passi successivi

- [Documentazione ctrl32](https://ctrl32.com/docs/) - l'editor, i linguaggi, ogni blocco
- [Scarica l'editor](https://ctrl32.com/download/)
- Tutte le schede testate
- Makerfabs MaTouch Lite ESP32-S3 3.95" - la sorella minore
- [Pannello di controllo smart home sulla MaTouch ESP32-P4](https://ctrl32.com/examples/smart-home-control-panel-on-an-esp32-p4-7-touch-display/) - un esempio completo sul web

