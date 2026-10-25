---
title: 'Olimex ESP32-P4-PC: hardware e cablaggio'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-P4-PC - mappa dei pin
tags:
- esp32-p4
- ethernet
- ups
- olimex
---

# Hardware e cablaggio

## Cosa ti serve

- L'Olimex ESP32-P4-PC.
- Un cavo dati USB-C - per il caricamento e per l'alimentazione (5 V).
- Un cavo Ethernet e una porta libera sulla tua rete.
- Un PC con l'[editor ctrl32](https://ctrl32.com/download/) (Windows).
- Opzionale: una cella Li-Po per la batteria tampone; per l'esempio all-in-one il LED utente (GPIO2) è sulla scheda e un pulsante va da GPIO14 a GND (EXT1); un transceiver CAN a 3,3 V su GPIO5 / GPIO15 e un transceiver RS-485 su GPIO16 / GPIO17 / GPIO18 (DE).

## Alimentazione

| Sorgente | Dove | Nota |
|---|---|---|
| USB 5 V | il connettore USB-C | alimentazione, programmazione e debug |
| Batteria Li-Po | il connettore della batteria | ricaricata sulla scheda; subentra quando manca l'alimentazione (UPS) |
| PoE | tramite l'estensione PoE | opzionale |

## Mappa dei pin

![Olimex ESP32-P4-PC - mappa dei pin](pinout/pinout.png)

| GPIO | Funzione in ctrl32 | Nota |
|---|---|---|
| 2 | free (LED0 line) |  |
| 4 | SPI SCLK |  |
| 5 | free (SPI CS line) |  |
| 14 | libero - I/O |  |
| 15 | libero - I/O |  |
| 16 | libero - I/O |  |
| 17 | libero - I/O |  |
| 18 | libero - I/O |  |
| 19 | libero - I/O |  |
| 20 | libero - I/O |  |
| 21 | USB HUB RST | ⚠  |
| 22 | I2C SDA |  |
| 23 | I2C SCL |  |
| 28 | Ethernet RMII (IP101GRI) | ⚠ usato dalla scheda |
| 29 | Ethernet RMII (IP101GRI) | ⚠ usato dalla scheda |
| 30 | Ethernet RMII (IP101GRI) | ⚠ usato dalla scheda |
| 31 | Ethernet MDC (IP101GRI) | ⚠ usato dalla scheda |
| 32 | libero - I/O |  |
| 33 | libero - I/O |  |
| 34 | Ethernet RMII (IP101GRI) | ⚠ usato dalla scheda |
| 35 | Ethernet RMII (IP101GRI) | ⚠ usato dalla scheda |
| 36 | libero - I/O | ⚠ pin di strapping |
| 46 | libero - I/O |  |
| 47 | libero - I/O |  |
| 48 | libero - I/O |  |
| 49 | Ethernet RMII (IP101GRI) | ⚠ usato dalla scheda |
| 50 | Ethernet RMII (IP101GRI) | ⚠ usato dalla scheda |
| 51 | Ethernet PHY reset (IP101GRI) | ⚠ usato dalla scheda |
| 52 | Ethernet MDIO (IP101GRI) | ⚠ usato dalla scheda |
| 53 | SPI MOSI |  |
| 54 | SPI MISO |  |

I pin liberi sono sul connettore **EXT1** a 20 pin: da GPIO14 a GPIO20,
32, 33, 36, 46, 47, 48 e il LED utente su GPIO2. Il connettore **UEXT**
porta I2C (GPIO22 / GPIO23 - condiviso con il bridge HDMI), SPI (GPIO4 /
53 / 54, CS GPIO5) e la UART della console. L'ESP32-P4 non ha un ingresso
analogico che ctrl32 usi: i segnali analogici passano tramite un ADC I2C
(un ADS1115 su UEXT) o un modulo Modbus. CAN e RS-485 vanno su pin EXT1
liberi con un modulo transceiver a 3,3 V.

## Sicurezza

- La scheda non è destinata a funzioni di sicurezza. Un arresto di
  emergenza, un interruttore della porta o una barriera fotoelettrica si
  cablano in hardware, mai tramite un programma.
- I pin GPIO sono a 3,3 V. Un segnale a 24 V richiede un optoisolatore o
  un traslatore di livello; la bobina di un relè richiede un driver (un
  modulo relè ne ha uno).

## Foto

![Olimex ESP32-P4-PC - foto 1](img/board-01.jpg)
![Olimex ESP32-P4-PC - foto 2](img/board-02.jpg)
![Olimex ESP32-P4-PC - foto 3](img/board-03.jpg)
![Olimex ESP32-P4-PC - foto 4](img/board-04.jpg)

---

[← Panoramica](README.it.md) | [Panoramica](README.it.md) | [Installare il runtime →](install.it.md)
