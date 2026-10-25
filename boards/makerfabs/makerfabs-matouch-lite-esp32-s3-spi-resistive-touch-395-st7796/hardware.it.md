---
title: 'Makerfabs MaTouch Lite ESP32-S3 3.95": hardware e cablaggio'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Makerfabs MaTouch Lite ESP32-S3 3.95" - mappa dei pin
tags:
- esp32-s3
- display
- touch
- hmi
- wifi
- makerfabs
---

# Hardware e cablaggio

## Cosa ti serve

- La Makerfabs MaTouch Lite ESP32-S3 3,95" (ST7796).
- Un cavo dati USB-C - per il caricamento e per l'alimentazione.
- Il nome e la password del tuo Wi-Fi a 2,4 GHz.
- Un PC con l'[editor ctrl32](https://ctrl32.com/download/) (Windows).
- Opzionale, per l'esempio all-in-one: un modulo relè o un LED su GPIO4, un potenziometro (10 k) tra 3,3 V e GND con il cursore su GPIO5 (i connettori JST) e un transceiver CAN a 3,3 V (ad es. SN65HVD230) su GPIO6 / GPIO7.

## Alimentazione

| Sorgente | Dove | Nota |
|---|---|---|
| USB 5 V | il connettore USB-C | alimentazione e programmazione |
| Batteria Li-Po | il connettore della batteria | 3,7 V |

## Mappa dei pin

![Makerfabs MaTouch Lite ESP32-S3 3.95" - mappa dei pin](pinout/pinout.png)

| GPIO | Funzione in ctrl32 | Nota |
|---|---|---|
| 0 | BOOT BTN | ⚠ pin di strapping |
| 1 | TFT RST |  |
| 2 | SD CMD | ⚠  |
| 4 | libero - I/O | ADC1 |
| 5 | libero - I/O | ADC1 |
| 6 | libero - I/O | ADC1 |
| 7 | libero - I/O | ADC1 |
| 13 | TFT MOSI |  |
| 14 | TFT SCLK |  |
| 15 | TFT CS |  |
| 21 | TFT DC |  |
| 38 | TOUCH SDA |  |
| 39 | TOUCH SCL |  |
| 40 | TOUCH INT |  |
| 41 | SD DO | ⚠  |
| 42 | SD SCLK | ⚠  |
| 48 | TFT BL |  |

I due connettori **JST** portano i quattro pin liberi (da GPIO4 a GPIO7) -
pochi, quindi l'esempio vi mette l'uscita, l'ingresso analogico e il CAN;
altri I/O passano tramite Modbus TCP o chip I2C. Il display, il
controller touch e lo slot microSD occupano il resto dei pin.

## Sicurezza

- La scheda non è destinata a funzioni di sicurezza. Un arresto di
  emergenza, un interruttore della porta o una barriera fotoelettrica si
  cablano in hardware, mai tramite un programma o uno schermo touch.
- I pin GPIO sono a 3,3 V. La bobina di un relè richiede un driver (un modulo relè ne ha uno).

---

[← Panoramica](README.it.md) | [Panoramica](README.it.md) | [Installare il runtime →](install.it.md)
