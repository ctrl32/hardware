---
title: 'Olimex ESP32-PoE: hardware e cablaggio'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-PoE - mappa dei pin
tags:
- esp32
- ethernet
- poe
- olimex
---

# Hardware e cablaggio

## Cosa ti serve

- La Olimex ESP32-PoE (la variante WROOM-32E, senza PSRAM).
- Un cavo dati micro-USB - per il primo caricamento del runtime.
- Per l'alimentazione: un alimentatore USB da 5 V, oppure uno switch / iniettore PoE (IEEE 802.3af).
- Un cavo Ethernet e una porta libera sulla tua rete.
- Un PC con l'[editor ctrl32](https://ctrl32.com/download/) (Windows).
- Opzionale, per l'esempio all-in-one: un pulsante è sulla scheda (BUT1); un modulo relè o un LED con resistenza su GPIO33; un potenziometro (10 k) tra 3,3 V e GND con il cursore su GPIO35; un transceiver CAN a 3,3 V (ad es. SN65HVD230) su GPIO4 (TX) / GPIO36 (RX) del connettore UEXT.

## Alimentazione

La scheda prende l'alimentazione da una di tre sorgenti:

| Sorgente | Dove | Nota |
|---|---|---|
| USB 5 V | il connettore micro-USB | la via per il primo caricamento |
| PoE | il connettore Ethernet, da uno switch o iniettore PoE | IEEE 802.3af |
| Batteria Li-Po | il connettore della batteria | ricaricata sulla scheda |

!!! danger "Non collegare mai USB e PoE contemporaneamente"
    La ESP32-PoE **non è isolata galvanicamente**. Mentre la scheda è
    alimentata in PoE, la sua massa segue l'alimentazione PoE - un cavo
    USB verso il tuo PC può allora portare una corrente dannosa. Carica il
    runtime tramite USB con il cavo Ethernet **scollegato** (o da una
    porta senza PoE), poi fai funzionare la scheda in PoE. Dove un PC deve
    restare collegato mentre la scheda è in PoE, usa la
    ESP32-PoE-ISO.

## Mappa dei pin

![Olimex ESP32-PoE - mappa dei pin](pinout/pinout.png)

| GPIO | Funzione in ctrl32 | Nota |
|---|---|---|
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
| 33 | libero - I/O | ADC1 |
| 34 | libero - il pulsante della scheda | ⚠ solo ingresso, ADC1 |
| 35 | libero - ingresso | ⚠ solo ingresso, ADC1 |
| 36 | free (UART RX line) | ⚠ solo ingresso, ADC1 |

I pin liberi si trovano sui connettori **EXT1 / EXT2** (2,54 mm) e sul
connettore **UEXT**. Da GPIO34 a GPIO39 sono solo ingressi - un'uscita lì
viene rifiutata dall'editor. Il connettore UEXT porta I2C (GPIO13 /
GPIO16) e SPI (GPIO14 / GPIO2 / GPIO15, condiviso con lo slot microSD).

## Sicurezza

- La scheda non è destinata a funzioni di sicurezza. Un arresto di
  emergenza, un interruttore della porta o una barriera fotoelettrica si
  cablano in hardware, mai tramite un programma.
- I pin GPIO sono a 3,3 V. Un ingresso a 24 V richiede un optoisolatore o
  un traslatore di livello; la bobina di un relè richiede un driver (un
  modulo relè ne ha uno).

---

[← Panoramica](README.it.md) | [Panoramica](README.it.md) | [Installare il runtime →](install.it.md)
