---
title: Olimex ESP32-GATEWAY
slug: olimex-esp32-gateway
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-gateway/
image: img/board-01.jpg
image_alt: Scheda Olimex ESP32-GATEWAY con il connettore Ethernet e il connettore USB-C
tags:
- esp32
- ethernet
- gateway
- olimex
---

# Olimex ESP32-GATEWAY

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32](https://img.shields.io/badge/chip-ESP32-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a)

![Scheda Olimex ESP32-GATEWAY con il connettore Ethernet e il connettore USB-C](img/board-01.jpg)

La Olimex ESP32-GATEWAY è una scheda ESP32 compatta con Ethernet a 100 Mb e Wi-Fi - abbastanza piccola per una scatola di derivazione. Con ctrl32 è un gateway con logica propria: dispositivi Modbus TCP letti e pubblicati tramite MQTT, un programma ladder sul chip e la sua pagina operatore in qualsiasi browser (WEBview).

**Adatta a:**

- Un gateway da Modbus TCP a MQTT con logica propria
- Un piccolo controllore in una scatola di derivazione, su Ethernet
- Domotica - lettura di contatori, comandi tramite moduli I/O Modbus

Pagina della scheda nel catalogo: [Olimex ESP32-GATEWAY](https://ctrl32.com/hardware/boards/olimex-esp32-gateway/)

![Olimex ESP32-GATEWAY - mappa dei pin: la funzione di ogni GPIO in ctrl32](pinout/pinout.png)

## Cosa sa fare ctrl32 su questa scheda

<!-- capabilities:start -->
| Funzione | Su questa scheda | Note |
|---|---|---|
| Chip | ESP32 (ESP32-WROOM-32E-N4) |  |
| Memoria | 4 MB flash |  |
| Dimensione del programma | 128 variabili, 32 allarmi, 128 blocchi | l'editor lo verifica prima del download |
| Ingressi / uscite digitali | 3 GPIO liberi | 1 di cui solo ingressi |
| Ingressi analogici | 2 sul chip (ADC1) | GPIO33, GPIO34 |
| Ethernet | sì - LAN8710A |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 - su pin liberi | serve un transceiver esterno |
| Modbus RTU (RS-485) | sì - su pin liberi | serve un transceiver esterno |
| Modbus TCP | client e server |  |
| MQTT | sì | rilevamento in Home Assistant |
| WEBview | sì | la pagina operatore in qualsiasi browser |
| Display / touch (HMI) | no | la pagina operatore è WEBview |
| USB | USB-C (CH340 USB-UART) |  |
| Alimentazione | 5 V USB |  |
<!-- capabilities:end -->

### Cosa non è supportato

- Bluetooth - l'ESP32 lo ha, ctrl32 non lo usa.
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

