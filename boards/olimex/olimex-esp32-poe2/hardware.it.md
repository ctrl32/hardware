---
title: 'Olimex ESP32-POE2: hardware e cablaggio'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-POE2 - mappa dei pin
tags:
- esp32
- ethernet
- poe
- psram
- olimex
---

# Hardware e cablaggio

## Cosa ti serve

- La Olimex ESP32-POE2.
- Un cavo dati USB-C - per il primo caricamento del runtime.
- Per l'alimentazione: uno switch / iniettore PoE (IEEE 802.3at, classe 4 per tutti i 25 W), oppure un alimentatore USB da 5 V.
- Un cavo Ethernet e una porta libera sulla tua rete.
- Un PC con l'[editor ctrl32](https://ctrl32.com/download/) (Windows).
- Opzionale, per l'esempio all-in-one: il pulsante BUT1 è sulla scheda; un modulo relè o un LED su GPIO4 (UEXT); un potenziometro (10 k) tra 3,3 V e GND con il cursore su GPIO36; un transceiver CAN a 3,3 V su GPIO5 (TX) / GPIO39 (RX).

## Alimentazione

| Sorgente | Dove | Nota |
|---|---|---|
| PoE | il connettore Ethernet | IEEE 802.3at classe 4, fino a 25 W |
| USB 5 V | il connettore USB-C | la via per il primo caricamento |
| Batteria Li-Po | il connettore della batteria | ricaricata sulla scheda |

Alimentata tramite Ethernet, la scheda alimenta circuiti esterni: **24 V /
0,75 A oppure 12 V / 1,5 A** (un jumper seleziona), **5 V / 1,5 A** e
**3,3 V / 1 A**, 25 W in totale.

!!! danger "Non collegare mai USB e PoE contemporaneamente"
    La ESP32-POE2 **non è isolata galvanicamente** dall'alimentazione
    Ethernet. Carica il runtime tramite USB con il cavo Ethernet
    scollegato (o da una porta senza PoE), poi fai funzionare la scheda in
    PoE.

## Mappa dei pin

![Olimex ESP32-POE2 - mappa dei pin](pinout/pinout.png)

| GPIO | Funzione in ctrl32 | Nota |
|---|---|---|
| 0 | Ethernet 50 MHz clock (LAN8710A) | ⚠ usato dalla scheda |
| 2 | SPI MOSI | ⚠ pin di strapping |
| 4 | free (UART TX line) |  |
| 5 | free (SPI CS line) |  |
| 6 | flash SPI del modulo | ⚠ usato dalla scheda |
| 7 | flash SPI del modulo | ⚠ usato dalla scheda |
| 8 | flash SPI del modulo | ⚠ usato dalla scheda |
| 9 | flash SPI del modulo | ⚠ usato dalla scheda |
| 10 | flash SPI del modulo | ⚠ usato dalla scheda |
| 11 | flash SPI del modulo | ⚠ usato dalla scheda |
| 12 | Ethernet PHY power (LAN8710A) | ⚠ usato dalla scheda |
| 13 | I2C SDA |  |
| 14 | SPI SCLK |  |
| 15 | SPI MISO | ⚠ pin di strapping |
| 18 | Ethernet MDIO (LAN8710A) | ⚠ usato dalla scheda |
| 19 | Ethernet RMII TXD0 (LAN8710A) | ⚠ usato dalla scheda |
| 21 | Ethernet RMII TX_EN (LAN8710A) | ⚠ usato dalla scheda |
| 22 | Ethernet RMII TXD1 (LAN8710A) | ⚠ usato dalla scheda |
| 23 | Ethernet MDC (LAN8710A) | ⚠ usato dalla scheda |
| 25 | Ethernet RMII RXD0 (LAN8710A) | ⚠ usato dalla scheda |
| 26 | Ethernet RMII RXD1 (LAN8710A) | ⚠ usato dalla scheda |
| 27 | Ethernet RMII CRS_DV (LAN8710A) | ⚠ usato dalla scheda |
| 33 | I2C SCL |  |
| 34 | libero - il pulsante della scheda | ⚠ solo ingresso, ADC1 |
| 36 | free (UART RX line) | ⚠ solo ingresso, ADC1 |
| 39 | libero - ingresso | ⚠ solo ingresso, ADC1 |

I pin liberi si trovano sui connettori **EXT** e sul connettore **UEXT**.
Da GPIO34 a GPIO39 sono solo ingressi. La PSRAM del modulo occupa GPIO16 /
GPIO17, quindi il clock Ethernet usa GPIO0 e l'I2C usa GPIO13 / GPIO33.

## Sicurezza

- La scheda non è destinata a funzioni di sicurezza. Un arresto di
  emergenza, un interruttore della porta o una barriera fotoelettrica si
  cablano in hardware, mai tramite un programma.
- I pin GPIO sono a 3,3 V. Un ingresso a 24 V richiede un optoisolatore o
  un traslatore di livello; la bobina di un relè richiede un driver (un
  modulo relè ne ha uno).

---

[← Panoramica](README.it.md) | [Panoramica](README.it.md) | [Installare il runtime →](install.it.md)
