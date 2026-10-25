---
title: 'Olimex ESP32-GATEWAY: hardware e cablaggio'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-GATEWAY - mappa dei pin
tags:
- esp32
- ethernet
- gateway
- olimex
---

# Hardware e cablaggio

## Cosa ti serve

- La Olimex ESP32-GATEWAY.
- Un cavo dati USB-C - per il caricamento e per l'alimentazione (5 V).
- Un cavo Ethernet e una porta libera sulla tua rete.
- Un PC con l'[editor ctrl32](https://ctrl32.com/download/) (Windows).
- L'esempio all-in-one usa il pulsante (GPIO34) e il LED (GPIO33) propri della scheda - non c'è altro da cablare.

## Alimentazione

| Sorgente | Dove | Nota |
|---|---|---|
| USB 5 V | il connettore USB-C | alimentazione e programmazione |

## Mappa dei pin

![Olimex ESP32-GATEWAY - mappa dei pin](pinout/pinout.png)

| GPIO | Funzione in ctrl32 | Nota |
|---|---|---|
| 2 | SPI MOSI | ⚠ pin di strapping |
| 5 | Ethernet PHY power (LAN8710A) | ⚠ usato dalla scheda |
| 6 | flash SPI del modulo | ⚠ usato dalla scheda |
| 7 | flash SPI del modulo | ⚠ usato dalla scheda |
| 8 | flash SPI del modulo | ⚠ usato dalla scheda |
| 9 | flash SPI del modulo | ⚠ usato dalla scheda |
| 10 | flash SPI del modulo | ⚠ usato dalla scheda |
| 11 | flash SPI del modulo | ⚠ usato dalla scheda |
| 13 | free (SPI CS line) |  |
| 14 | SPI SCLK |  |
| 15 | SPI MISO | ⚠ pin di strapping |
| 16 | I2C SCL |  |
| 17 | Ethernet 50 MHz clock (LAN8710A) | ⚠ usato dalla scheda |
| 18 | Ethernet MDIO (LAN8710A) | ⚠ usato dalla scheda |
| 19 | Ethernet RMII TXD0 (LAN8710A) | ⚠ usato dalla scheda |
| 21 | Ethernet RMII TX_EN (LAN8710A) | ⚠ usato dalla scheda |
| 22 | Ethernet RMII TXD1 (LAN8710A) | ⚠ usato dalla scheda |
| 23 | Ethernet MDC (LAN8710A) | ⚠ usato dalla scheda |
| 25 | Ethernet RMII RXD0 (LAN8710A) | ⚠ usato dalla scheda |
| 26 | Ethernet RMII RXD1 (LAN8710A) | ⚠ usato dalla scheda |
| 27 | Ethernet RMII CRS_DV (LAN8710A) | ⚠ usato dalla scheda |
| 32 | I2C SDA |  |
| 33 | free (LED0 line) | ADC1 |
| 34 | libero - il pulsante della scheda | ⚠ solo ingresso, ADC1 |

Il connettore **EXT** a 20 pin porta i pin liberi e le linee I2C / SPI.
Il LED della scheda è su GPIO33 e il suo pulsante su GPIO34 (solo
ingresso). Restano liberi pochi pin: altri I/O passano tramite Modbus TCP
o chip I2C.

## Sicurezza

- La scheda non è destinata a funzioni di sicurezza. Un arresto di
  emergenza, un interruttore della porta o una barriera fotoelettrica si
  cablano in hardware, mai tramite un programma.
- I pin GPIO sono a 3,3 V. Un segnale a 24 V richiede un optoisolatore o
  un traslatore di livello; la bobina di un relè richiede un driver (un
  modulo relè ne ha uno).

---

[← Panoramica](README.it.md) | [Panoramica](README.it.md) | [Installare il runtime →](install.it.md)
