---
title: 'Olimex ESP32-POE2: hardvér a zapojenie'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-POE2 - mapa pinov
tags:
- esp32
- ethernet
- poe
- psram
- olimex
---

# Hardvér a zapojenie

## Čo treba

- Olimex ESP32-POE2.
- Dátový kábel USB-C - na prvé nahratie runtime.
- Napájanie: PoE switch či injektor (IEEE 802.3at, trieda 4 pre plných 25 W), alebo zdroj 5 V cez USB.
- Sieťový kábel a voľný port v sieti.
- PC s [editorom ctrl32](https://ctrl32.com/download/) (Windows).
- Voliteľne pre príklad all-in-one: tlačidlo BUT1 je na doske; reléový modul alebo LED na GPIO4 (UEXT); potenciometer (10 k) medzi 3,3 V a GND s bežcom na GPIO36; 3,3 V prevodník CAN na GPIO5 (TX) / GPIO39 (RX).

## Napájanie

| Zdroj | Kde | Poznámka |
|---|---|---|
| PoE | konektor Ethernet | IEEE 802.3at trieda 4, až 25 W |
| USB 5 V | konektor USB-C | cesta na prvé nahratie |
| Li-Po batéria | konektor batérie | nabíja sa na doske |

Pri napájaní cez Ethernet doska napája aj vonkajšie obvody: **24 V / 0,75 A
alebo 12 V / 1,5 A** (volí prepojka), **5 V / 1,5 A** a **3,3 V / 1 A**,
spolu 25 W.

!!! danger "Nikdy nepripájaj USB a PoE naraz"
    ESP32-POE2 **nie je galvanicky oddelená** od napájania z Ethernetu.
    Runtime nahraj cez USB s odpojeným sieťovým káblom (alebo z portu bez
    PoE) a až potom dosku napájaj cez PoE.

## Mapa pinov

![Olimex ESP32-POE2 - mapa pinov](pinout/pinout.png)

| GPIO | Funkcia v ctrl32 | Poznámka |
|---|---|---|
| 0 | Ethernet 50 MHz clock (LAN8710A) | ⚠ používa doska |
| 2 | SPI MOSI | ⚠ strapping pin |
| 4 | free (UART TX line) |  |
| 5 | free (SPI CS line) |  |
| 6 | SPI flash modulu | ⚠ používa doska |
| 7 | SPI flash modulu | ⚠ používa doska |
| 8 | SPI flash modulu | ⚠ používa doska |
| 9 | SPI flash modulu | ⚠ používa doska |
| 10 | SPI flash modulu | ⚠ používa doska |
| 11 | SPI flash modulu | ⚠ používa doska |
| 12 | Ethernet PHY power (LAN8710A) | ⚠ používa doska |
| 13 | I2C SDA |  |
| 14 | SPI SCLK |  |
| 15 | SPI MISO | ⚠ strapping pin |
| 18 | Ethernet MDIO (LAN8710A) | ⚠ používa doska |
| 19 | Ethernet RMII TXD0 (LAN8710A) | ⚠ používa doska |
| 21 | Ethernet RMII TX_EN (LAN8710A) | ⚠ používa doska |
| 22 | Ethernet RMII TXD1 (LAN8710A) | ⚠ používa doska |
| 23 | Ethernet MDC (LAN8710A) | ⚠ používa doska |
| 25 | Ethernet RMII RXD0 (LAN8710A) | ⚠ používa doska |
| 26 | Ethernet RMII RXD1 (LAN8710A) | ⚠ používa doska |
| 27 | Ethernet RMII CRS_DV (LAN8710A) | ⚠ používa doska |
| 33 | I2C SCL |  |
| 34 | voľný - tlačidlo dosky | ⚠ len vstup, ADC1 |
| 36 | free (UART RX line) | ⚠ len vstup, ADC1 |
| 39 | voľný vstup | ⚠ len vstup, ADC1 |

Voľné piny sú na konektoroch **EXT** a na konektore **UEXT**. GPIO34 až
GPIO39 sú len vstupy. PSRAM modulu zaberá GPIO16 / GPIO17, preto hodiny
Ethernetu idú na GPIO0 a I2C používa GPIO13 / GPIO33.

## Bezpečnosť

- Doska nie je určená na bezpečnostné funkcie. Núdzové zastavenie, dverový
  spínač či svetelná závora sa zapájajú v hardvéri, nikdy cez program.
- Piny GPIO majú 3,3 V. Vstup 24 V potrebuje optočlen alebo prevodník
  úrovní; cievka relé potrebuje budič (reléový modul ho má).

---

[← Prehľad](README.sk.md) | [Prehľad](README.sk.md) | [Nahratie runtime →](install.sk.md)
