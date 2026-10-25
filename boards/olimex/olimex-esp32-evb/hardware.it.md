---
title: 'Olimex ESP32-EVB: hardware e cablaggio'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-EVB - mappa dei pin
tags:
- esp32
- ethernet
- can
- relay
- olimex
---

# Hardware e cablaggio

## Cosa ti serve

- La Olimex ESP32-EVB.
- Un cavo dati micro-USB - per il primo caricamento del runtime.
- Per l'alimentazione: un alimentatore USB da 5 V, oppure 5 V sul morsetto a vite.
- Un cavo Ethernet e una porta libera sulla tua rete.
- Un PC con l'[editor ctrl32](https://ctrl32.com/download/) (Windows).
- Opzionale, per l'esempio all-in-one: un potenziometro (10 k) tra 3,3 V e GND con il cursore su GPIO36 (UEXT); un nodo CAN o un adattatore CAN e due terminazioni da 120 ohm.
- Opzionale: il display Olimex MOD-LCD2.8RTP (2,8 pollici, 240 x 320, touch resistivo) sul connettore UEXT.

## Alimentazione

| Sorgente | Dove | Nota |
|---|---|---|
| USB 5 V | il connettore micro-USB | la via per il primo caricamento |
| 5 V DC | il morsetto a vite | per un quadro elettrico |
| Batteria Li-Po | il connettore della batteria | ricaricata sulla scheda |

!!! warning "I relè commutano la tensione di rete"
    Cabla i contatti dei relè solo con la scheda non alimentata, in un
    contenitore, e solo se sei una persona abilitata a lavorare su impianti
    di rete. I contatti reggono 10 A / 250 VAC; un motore o un
    riscaldatore oltre questo valore richiede un contattore comandato dal
    relè.

## Mappa dei pin

![Olimex ESP32-EVB - mappa dei pin](pinout/pinout.png)

| GPIO | Funzione in ctrl32 | Nota |
|---|---|---|
| 0 | Ethernet 50 MHz clock (LAN8710A) | ⚠ usato dalla scheda |
| 2 | TFT MOSI | ⚠ pin di strapping |
| 2 | SPI MOSI | ⚠ pin di strapping |
| 4 | free (UART TX line) |  |
| 5 | CAN TX |  |
| 6 | flash SPI del modulo | ⚠ usato dalla scheda |
| 7 | flash SPI del modulo | ⚠ usato dalla scheda |
| 8 | flash SPI del modulo | ⚠ usato dalla scheda |
| 9 | flash SPI del modulo | ⚠ usato dalla scheda |
| 10 | flash SPI del modulo | ⚠ usato dalla scheda |
| 11 | flash SPI del modulo | ⚠ usato dalla scheda |
| 13 | I2C SDA |  |
| 14 | TFT SCLK |  |
| 14 | SPI SCLK |  |
| 15 | TFT DC | ⚠ pin di strapping |
| 15 | SPI MISO | ⚠ pin di strapping |
| 16 | I2C SCL |  |
| 17 | TFT CS |  |
| 17 | free (SPI CS line) |  |
| 18 | Ethernet MDIO (LAN8710A) | ⚠ usato dalla scheda |
| 19 | Ethernet RMII TXD0 (LAN8710A) | ⚠ usato dalla scheda |
| 21 | Ethernet RMII TX_EN (LAN8710A) | ⚠ usato dalla scheda |
| 22 | Ethernet RMII TXD1 (LAN8710A) | ⚠ usato dalla scheda |
| 23 | Ethernet MDC (LAN8710A) | ⚠ usato dalla scheda |
| 25 | Ethernet RMII RXD0 (LAN8710A) | ⚠ usato dalla scheda |
| 26 | Ethernet RMII RXD1 (LAN8710A) | ⚠ usato dalla scheda |
| 27 | Ethernet RMII CRS_DV (LAN8710A) | ⚠ usato dalla scheda |
| 32 | free (REL1 line) | ADC1 |
| 33 | free (REL2 line) | ADC1 |
| 34 | libero - il pulsante della scheda | ⚠ solo ingresso, ADC1 |
| 35 | CAN RX |  |
| 36 | free (UART RX line) | ⚠ solo ingresso, ADC1 |

**Relè:** REL1 su GPIO32, REL2 su GPIO33. **Pulsante:** BUT1 su GPIO34
(solo ingresso). **CAN:** il transceiver sulla scheda su GPIO5 (TX) /
GPIO35 (RX), CAN_H / CAN_L sul morsetto - termina il bus con 120 ohm a
entrambe le estremità. Il connettore **UEXT** porta I2C (GPIO13 / GPIO16),
SPI e una UART libera (GPIO4 / GPIO36); il display opzionale usa le sue
linee SPI.

## Sicurezza

- La scheda non è destinata a funzioni di sicurezza. Un arresto di
  emergenza, un interruttore della porta o una barriera fotoelettrica si
  cablano in hardware, mai tramite un programma.
- I pin GPIO sono a 3,3 V. Un segnale a 24 V richiede un optoisolatore o
  un traslatore di livello; la bobina di un relè richiede un driver (un
  modulo relè ne ha uno).

---

[← Panoramica](README.it.md) | [Panoramica](README.it.md) | [Installare il runtime →](install.it.md)
