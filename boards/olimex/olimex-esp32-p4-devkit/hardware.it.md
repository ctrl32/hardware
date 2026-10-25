---
title: 'Olimex ESP32-P4-DevKit: hardware e cablaggio'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-P4-DevKit - mappa dei pin
tags:
- esp32-p4
- ethernet
- olimex
---

# Hardware e cablaggio

## Cosa ti serve

- La Olimex ESP32-P4-DevKit.
- Un cavo dati USB-C - per il caricamento e per l'alimentazione (5 V).
- Un cavo Ethernet e una porta libera sulla tua rete.
- Un PC con l'[editor ctrl32](https://ctrl32.com/download/) (Windows).
- Opzionale, per l'esempio all-in-one: il LED (GPIO2) è sulla scheda; un pulsante da GPIO20 a GND; un transceiver CAN a 3,3 V su GPIO5 / GPIO21 e un transceiver RS-485 su GPIO22 / GPIO23 / GPIO32 (DE).

## Alimentazione

| Sorgente | Dove | Nota |
|---|---|---|
| USB 5 V | il connettore USB-C | alimentazione, programmazione e debug |
| PoE | tramite l'estensione PoE | opzionale |

## Mappa dei pin

![Olimex ESP32-P4-DevKit - mappa dei pin](pinout/pinout.png)

| GPIO | Funzione in ctrl32 | Nota |
|---|---|---|
| 2 | free (LED0 line) |  |
| 4 | SPI SCLK |  |
| 5 | free (SPI CS line) |  |
| 7 | I2C SDA |  |
| 8 | I2C SCL |  |
| 20 | libero - I/O |  |
| 21 | libero - I/O |  |
| 22 | libero - I/O |  |
| 23 | libero - I/O |  |
| 28 | Ethernet RMII (IP101GRI) | ⚠ usato dalla scheda |
| 29 | Ethernet RMII (IP101GRI) | ⚠ usato dalla scheda |
| 30 | Ethernet RMII (IP101GRI) | ⚠ usato dalla scheda |
| 31 | Ethernet MDC (IP101GRI) | ⚠ usato dalla scheda |
| 32 | libero - I/O |  |
| 33 | libero - I/O |  |
| 34 | Ethernet RMII (IP101GRI) | ⚠ usato dalla scheda |
| 35 | Ethernet RMII (IP101GRI) | ⚠ usato dalla scheda |
| 46 | libero - I/O |  |
| 47 | libero - I/O |  |
| 48 | libero - I/O |  |
| 49 | Ethernet RMII (IP101GRI) | ⚠ usato dalla scheda |
| 50 | Ethernet RMII (IP101GRI) | ⚠ usato dalla scheda |
| 51 | Ethernet PHY reset (IP101GRI) | ⚠ usato dalla scheda |
| 52 | Ethernet MDIO (IP101GRI) | ⚠ usato dalla scheda |
| 53 | SPI MOSI |  |
| 54 | SPI MISO |  |

Tutti i GPIO sono sui due connettori a pettine da 20 pin. L'ESP32-P4 non
ha un ingresso analogico che ctrl32 usi: i segnali analogici passano
tramite un ADC I2C (un ADS1115 sul connettore pUEXT, I2C GPIO7 / GPIO8) o
un modulo Modbus.

## Sicurezza

- La scheda non è destinata a funzioni di sicurezza. Un arresto di
  emergenza, un interruttore della porta o una barriera fotoelettrica si
  cablano in hardware, mai tramite un programma.
- I pin GPIO sono a 3,3 V. Un segnale a 24 V richiede un optoisolatore o
  un traslatore di livello; la bobina di un relè richiede un driver (un
  modulo relè ne ha uno).

---

[← Panoramica](README.it.md) | [Panoramica](README.it.md) | [Installare il runtime →](install.it.md)
