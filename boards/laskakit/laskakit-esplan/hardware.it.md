---
title: 'LaskaKit ESPlan: hardware e cablaggio'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: LaskaKit ESPlan - mappa dei pin
tags:
- esp32
- ethernet
- rs485
- modbus
- laskakit
---

# Hardware e cablaggio

## Cosa ti serve

- La LaskaKit ESPlan.
- Un cavo dati USB-C - per il primo caricamento del runtime.
- Per l'alimentazione: 12 o 24 V DC sul morsetto a vite (7-40 V), oppure 5 V tramite USB-C.
- Un cavo Ethernet e una porta libera sulla tua rete.
- Un PC con l'[editor ctrl32](https://ctrl32.com/download/) (Windows).
- Opzionale, per l'esempio all-in-one: un sensore di temperatura Modbus RTU (unit 1) sul morsetto RS-485; un pulsante da GPIO16 a GND; un potenziometro (10 k) tra 3,3 V e GND con il cursore su GPIO35; un transceiver CAN a 3,3 V su GPIO14 (TX) / GPIO39 (RX).

## Alimentazione

| Sorgente | Dove | Nota |
|---|---|---|
| 7-40 V DC | il morsetto a vite | consigliati 12 o 24 V |
| USB 5 V | il connettore USB-C | la via per il primo caricamento |
| PoE | tramite il modulo PoE opzionale (802.3af) | modulo aggiuntivo |

## Mappa dei pin

![LaskaKit ESPlan - mappa dei pin](pinout/pinout.png)

| GPIO | Funzione in ctrl32 | Nota |
|---|---|---|
| 0 | free (LED0 line) | ⚠ pin di strapping |
| 4 | RS485 TX |  |
| 5 | Ethernet PHY power (LAN8720A) | ⚠ usato dalla scheda |
| 6 | flash SPI del modulo | ⚠ usato dalla scheda |
| 7 | flash SPI del modulo | ⚠ usato dalla scheda |
| 8 | flash SPI del modulo | ⚠ usato dalla scheda |
| 9 | flash SPI del modulo | ⚠ usato dalla scheda |
| 10 | flash SPI del modulo | ⚠ usato dalla scheda |
| 11 | flash SPI del modulo | ⚠ usato dalla scheda |
| 12 | SPI MISO | ⚠ pin di strapping |
| 13 | SPI MOSI |  |
| 14 | free (SPI SCLK line) |  |
| 15 | SPI CS | ⚠ pin di strapping |
| 16 | libero - I/O |  |
| 17 | Ethernet 50 MHz clock (LAN8720A) | ⚠ usato dalla scheda |
| 18 | Ethernet MDIO (LAN8720A) | ⚠ usato dalla scheda |
| 19 | Ethernet RMII TXD0 (LAN8720A) | ⚠ usato dalla scheda |
| 21 | Ethernet RMII TX_EN (LAN8720A) | ⚠ usato dalla scheda |
| 22 | Ethernet RMII TXD1 (LAN8720A) | ⚠ usato dalla scheda |
| 23 | Ethernet MDC (LAN8720A) | ⚠ usato dalla scheda |
| 25 | Ethernet RMII RXD0 (LAN8720A) | ⚠ usato dalla scheda |
| 26 | Ethernet RMII RXD1 (LAN8720A) | ⚠ usato dalla scheda |
| 27 | Ethernet RMII CRS_DV (LAN8720A) | ⚠ usato dalla scheda |
| 32 | TOUCH SCL |  |
| 33 | TOUCH SDA |  |
| 35 | libero - ingresso | ⚠ solo ingresso, ADC1 |
| 36 | RS485 RX |  |
| 39 | libero - ingresso | ⚠ solo ingresso, ADC1 |

**RS-485:** A e B sul morsetto, il transceiver WS3081 su GPIO4 (TX) /
GPIO36 (RX); un jumper inserisce la terminazione da 120 ohm - mettila solo
alle due estremità della linea. I connettori **uSup** portano I2C (GPIO33 /
GPIO32) e SPI. Il LED della scheda è su GPIO0 (un pin di strapping -
lascialo come uscita pilotata dal programma).

## Sicurezza

- La scheda non è destinata a funzioni di sicurezza. Un arresto di
  emergenza, un interruttore della porta o una barriera fotoelettrica si
  cablano in hardware, mai tramite un programma.
- I pin GPIO sono a 3,3 V. Un segnale a 24 V richiede un optoisolatore o
  un traslatore di livello; la bobina di un relè richiede un driver (un
  modulo relè ne ha uno).

---

[← Panoramica](README.it.md) | [Panoramica](README.it.md) | [Installare il runtime →](install.it.md)
