---
title: 'Olimex ESP32-PoE: hardvér a zapojenie'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-PoE - mapa pinov
tags:
- esp32
- ethernet
- poe
- olimex
---

# Hardvér a zapojenie

## Čo treba

- Olimex ESP32-PoE (variant WROOM-32E, bez PSRAM).
- Dátový kábel micro-USB - na prvé nahratie runtime.
- Napájanie: zdroj 5 V cez USB, alebo PoE switch či injektor (IEEE 802.3af).
- Sieťový kábel a voľný port v sieti.
- PC s [editorom ctrl32](https://ctrl32.com/download/) (Windows).
- Voliteľne pre príklad all-in-one: tlačidlo BUT1 je na doske; reléový modul alebo LED s rezistorom na GPIO33; potenciometer (10 k) medzi 3,3 V a GND s bežcom na GPIO35; 3,3 V prevodník CAN (napr. SN65HVD230) na GPIO4 (TX) / GPIO36 (RX) konektora UEXT.

## Napájanie

Doska sa napája z jedného z troch zdrojov:

| Zdroj | Kde | Poznámka |
|---|---|---|
| USB 5 V | konektor micro-USB | cesta na prvé nahratie |
| PoE | konektor Ethernet, z PoE switcha alebo injektora | IEEE 802.3af |
| Li-Po batéria | konektor batérie | nabíja sa na doske |

!!! danger "Nikdy nepripájaj USB a PoE naraz"
    ESP32-PoE **nie je galvanicky oddelená**. Keď je doska napájaná cez
    PoE, jej zem sleduje zdroj PoE - kábel USB k PC potom môže viesť prúd,
    ktorý poškodí zariadenia. Runtime nahraj cez USB s **odpojeným**
    sieťovým káblom (alebo z portu bez PoE) a až potom dosku napájaj cez
    PoE. Ak musí byť PC pripojené aj počas PoE, použi
    [ESP32-PoE-ISO](../olimex-esp32-poe-iso/README.sk.md).

## Mapa pinov

![Olimex ESP32-PoE - mapa pinov](pinout/pinout.png)

| GPIO | Funkcia v ctrl32 | Poznámka |
|---|---|---|
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
| 16 | I2C SCL |  |
| 17 | Ethernet 50 MHz clock (LAN8710A) | ⚠ používa doska |
| 18 | Ethernet MDIO (LAN8710A) | ⚠ používa doska |
| 19 | Ethernet RMII TXD0 (LAN8710A) | ⚠ používa doska |
| 21 | Ethernet RMII TX_EN (LAN8710A) | ⚠ používa doska |
| 22 | Ethernet RMII TXD1 (LAN8710A) | ⚠ používa doska |
| 23 | Ethernet MDC (LAN8710A) | ⚠ používa doska |
| 25 | Ethernet RMII RXD0 (LAN8710A) | ⚠ používa doska |
| 26 | Ethernet RMII RXD1 (LAN8710A) | ⚠ používa doska |
| 27 | Ethernet RMII CRS_DV (LAN8710A) | ⚠ používa doska |
| 33 | voľný I/O | ADC1 |
| 34 | voľný - tlačidlo dosky | ⚠ len vstup, ADC1 |
| 35 | voľný vstup | ⚠ len vstup, ADC1 |
| 36 | free (UART RX line) | ⚠ len vstup, ADC1 |

Voľné piny sú na konektoroch **EXT1 / EXT2** (2,54 mm) a na konektore
**UEXT**. GPIO34 až GPIO39 sú len vstupy - výstup na nich editor odmietne.
Konektor UEXT nesie I2C (GPIO13 / GPIO16) a SPI (GPIO14 / GPIO2 / GPIO15,
zdieľané so slotom microSD).

## Bezpečnosť

- Doska nie je určená na bezpečnostné funkcie. Núdzové zastavenie, dverový
  spínač či svetelná závora sa zapájajú v hardvéri, nikdy cez program.
- Piny GPIO majú 3,3 V. Vstup 24 V potrebuje optočlen alebo prevodník
  úrovní; cievka relé potrebuje budič (reléový modul ho má).

---

[← Prehľad](README.sk.md) | [Prehľad](README.sk.md) | [Nahratie runtime →](install.sk.md)
