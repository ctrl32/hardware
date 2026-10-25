---
title: 'Olimex ESP32-S3-DevKit-Lipo: hardware e cablaggio'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-S3-DevKit-Lipo - mappa dei pin
tags:
- esp32-s3
- wifi
- psram
- battery
- olimex
---

# Hardware e cablaggio

## Cosa ti serve

- La Olimex ESP32-S3-DevKit-Lipo.
- Un cavo dati USB-C - sul connettore con la scritta UART (il CH340X) per il caricamento.
- Il nome e la password del tuo Wi-Fi a 2,4 GHz.
- Un PC con l'[editor ctrl32](https://ctrl32.com/download/) (Windows).
- Opzionale, per l'esempio all-in-one: il pulsante Boot/User (GPIO0) e il LED (GPIO38) sono sulla scheda; un potenziometro (10 k) tra 3,3 V e GND con il cursore su GPIO1; un transceiver CAN a 3,3 V su GPIO10 / GPIO17 e un transceiver RS-485 su GPIO18 / GPIO2 / GPIO4 (DE).

## Alimentazione

| Sorgente | Dove | Nota |
|---|---|---|
| USB 5 V | uno qualsiasi dei due connettori USB-C | alimentazione e programmazione |
| Batteria Li-Po | il connettore della batteria | ricaricata sulla scheda, commutazione automatica |

## Mappa dei pin

![Olimex ESP32-S3-DevKit-Lipo - mappa dei pin](pinout/pinout.png)

| GPIO | Funzione in ctrl32 | Nota |
|---|---|---|
| 0 | libero - il pulsante della scheda | ⚠ pin di strapping |
| 1 | libero - I/O | ADC1 |
| 2 | libero - I/O | ADC1 |
| 4 | libero - I/O | ADC1 |
| 5 | free (PWR SENSE line) | ADC1 |
| 6 | free (BAT SENSE line) | ADC1 |
| 7 | libero - I/O | ADC1 |
| 8 | libero - I/O | ADC1 |
| 9 | libero - I/O | ADC1 |
| 10 | free (SPI CS line) | ADC1 |
| 11 | SPI MOSI |  |
| 12 | SPI SCLK |  |
| 13 | SPI MISO |  |
| 14 | libero - I/O |  |
| 15 | libero - I/O |  |
| 16 | libero - I/O |  |
| 17 | free (UART TX line) |  |
| 18 | free (UART RX line) |  |
| 21 | libero - I/O |  |
| 38 | free (LED0 line) |  |
| 39 | libero - I/O |  |
| 40 | libero - I/O |  |
| 41 | libero - I/O |  |
| 42 | libero - I/O |  |
| 47 | I2C SCL |  |
| 48 | I2C SDA |  |

I connettori a pettine portano i GPIO liberi; ADC1 (gli ingressi
analogici che ctrl32 usa) è da GPIO1 a GPIO10. GPIO0 è il pulsante
Boot/User - un ingresso nel programma, e tenuto premuto all'accensione
avvia la modalità download del chip. Il connettore pUEXT porta I2C
(GPIO48 / GPIO47) e SPI.

## Sicurezza

- La scheda non è destinata a funzioni di sicurezza. Un arresto di
  emergenza, un interruttore della porta o una barriera fotoelettrica si
  cablano in hardware, mai tramite un programma.
- I pin GPIO sono a 3,3 V. Un segnale a 24 V richiede un optoisolatore o
  un traslatore di livello; la bobina di un relè richiede un driver (un
  modulo relè ne ha uno).

---

[← Panoramica](README.it.md) | [Panoramica](README.it.md) | [Installare il runtime →](install.it.md)
