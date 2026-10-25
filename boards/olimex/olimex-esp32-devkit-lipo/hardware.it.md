---
title: 'Olimex ESP32-DevKit-LiPo: hardware e cablaggio'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-DevKit-LiPo - mappa dei pin
tags:
- esp32
- wifi
- battery
- olimex
---

# Hardware e cablaggio

## Cosa ti serve

- La Olimex ESP32-DevKit-LiPo.
- Un cavo dati micro-USB - per il caricamento e per l'alimentazione (5 V).
- Il nome e la password del tuo Wi-Fi a 2,4 GHz.
- Un PC con l'[editor ctrl32](https://ctrl32.com/download/) (Windows).
- Opzionale, per l'esempio all-in-one: un pulsante da GPIO13 a GND; un modulo relè o un LED con resistenza su GPIO4; un potenziometro (10 k) tra 3,3 V e GND con il cursore su GPIO32; un transceiver CAN a 3,3 V su GPIO14 / GPIO34 e un transceiver RS-485 su GPIO16 / GPIO36 / GPIO17 (DE); una cella Li-Po come riserva.

## Alimentazione

| Sorgente | Dove | Nota |
|---|---|---|
| USB 5 V | il connettore micro-USB | alimentazione e programmazione |
| Batteria Li-Po | il connettore della batteria | ricaricata sulla scheda, subentra quando manca l'USB |

## Mappa dei pin

![Olimex ESP32-DevKit-LiPo - mappa dei pin](pinout/pinout.png)

| GPIO | Funzione in ctrl32 | Nota |
|---|---|---|
| 4 | libero - I/O |  |
| 6 | flash SPI del modulo | ⚠ usato dalla scheda |
| 7 | flash SPI del modulo | ⚠ usato dalla scheda |
| 8 | flash SPI del modulo | ⚠ usato dalla scheda |
| 9 | flash SPI del modulo | ⚠ usato dalla scheda |
| 10 | flash SPI del modulo | ⚠ usato dalla scheda |
| 11 | flash SPI del modulo | ⚠ usato dalla scheda |
| 13 | libero - I/O |  |
| 14 | libero - I/O |  |
| 16 | libero - I/O |  |
| 17 | libero - I/O |  |
| 18 | libero - I/O |  |
| 19 | libero - I/O |  |
| 21 | libero - I/O |  |
| 22 | libero - I/O |  |
| 23 | libero - I/O |  |
| 25 | libero - I/O |  |
| 26 | libero - I/O |  |
| 27 | libero - I/O |  |
| 32 | libero - I/O | ADC1 |
| 33 | libero - I/O | ADC1 |
| 34 | libero - ingresso | ⚠ solo ingresso, ADC1 |
| 35 | free (BAT SENSE line) | ⚠ solo ingresso, ADC1 |
| 36 | libero - ingresso | ⚠ solo ingresso, ADC1 |
| 39 | free (PWR SENSE line) | ⚠ solo ingresso, ADC1 |

I due connettori a pettine portano i GPIO liberi del modulo. Da GPIO34 a
GPIO39 sono solo ingressi; GPIO0, 2, 12 e 15 sono pin di strapping -
lasciali per gli ingressi o provali prima di usarli. Un pulsante verso
GND non richiede resistenza: ctrl32 lo legge invertito con il pull-up del
chip.

## Sicurezza

- La scheda non è destinata a funzioni di sicurezza. Un arresto di
  emergenza, un interruttore della porta o una barriera fotoelettrica si
  cablano in hardware, mai tramite un programma.
- I pin GPIO sono a 3,3 V. Un segnale a 24 V richiede un optoisolatore o
  un traslatore di livello; la bobina di un relè richiede un driver (un
  modulo relè ne ha uno).

---

[← Panoramica](README.it.md) | [Panoramica](README.it.md) | [Installare il runtime →](install.it.md)
