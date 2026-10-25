---
title: LaskaKit ESPlan
slug: laskakit-esplan
sidebar_position: 10
hardware: /hardware/boards/laskakit-esplan/
image: img/board-01.jpg
image_alt: Scheda LaskaKit ESPlan con il connettore Ethernet, il morsetto RS-485 e il morsetto di alimentazione
tags:
- esp32
- ethernet
- rs485
- modbus
- laskakit
---

# LaskaKit ESPlan

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32](https://img.shields.io/badge/chip-ESP32-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a)

![Scheda LaskaKit ESPlan con il connettore Ethernet, il morsetto RS-485 e il morsetto di alimentazione](img/board-01.jpg)

La LaskaKit ESPlan è una scheda industriale con ESP32: Ethernet 10/100, un'interfaccia RS-485 protetta con terminazione inseribile, Wi-Fi e un'alimentazione ad ampio campo 7-40 V su morsetto a vite (oppure PoE con un modulo aggiuntivo). Con ctrl32 è un master o slave Modbus RTU in quadro elettrico - un programma ladder sul chip, dispositivi RS-485 letti e scritti, i valori su Modbus TCP, MQTT e la sua pagina operatore (WEBview).

**Adatta a:**

- Un master Modbus RTU per contatori, sensori e inverter, alimentato a 24 V
- Un gateway Modbus RTU / TCP con logica propria
- Building automation in quadro elettrico

Pagina della scheda nel catalogo: [LaskaKit ESPlan](https://ctrl32.com/hardware/boards/laskakit-esplan/)

![LaskaKit ESPlan - mappa dei pin: la funzione di ogni GPIO in ctrl32](pinout/pinout.png)

## Cosa sa fare ctrl32 su questa scheda

<!-- capabilities:start -->
| Funzione | Su questa scheda | Note |
|---|---|---|
| Chip | ESP32 (ESP32-WROOM-32E-N4) |  |
| Memoria | 4 MB flash |  |
| Dimensione del programma | 128 variabili, 32 allarmi, 128 blocchi | l'editor lo verifica prima del download |
| Ingressi / uscite digitali | 5 GPIO liberi | 2 di cui solo ingressi |
| Ingressi analogici | 2 sul chip (ADC1) | GPIO35, GPIO39 |
| Ethernet | sì - LAN8720A |  |
| Power over Ethernet | IEEE 802.3af |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 - su pin liberi | serve un transceiver esterno |
| Modbus RTU (RS-485) | sì |  |
| Modbus TCP | client e server |  |
| MQTT | sì | rilevamento in Home Assistant |
| WEBview | sì | la pagina operatore in qualsiasi browser |
| Display / touch (HMI) | no | la pagina operatore è WEBview |
| USB | USB-C (CH9102 USB-UART) |  |
| Alimentazione | 5 V USB, PoE |  |
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

