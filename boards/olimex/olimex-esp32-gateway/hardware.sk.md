---
title: 'Olimex ESP32-GATEWAY: hardvér a zapojenie'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-GATEWAY - mapa pinov
tags:
- esp32
- ethernet
- gateway
- olimex
---

# Hardvér a zapojenie

## Čo treba

- Olimex ESP32-GATEWAY.
- Dátový kábel USB-C - na nahratie aj napájanie (5 V).
- Sieťový kábel a voľný port v sieti.
- PC s [editorom ctrl32](https://ctrl32.com/download/) (Windows).
- Príklad all-in-one používa vlastné tlačidlo dosky (GPIO34) a LED (GPIO33) - nič iné netreba zapájať.

## Napájanie

| Zdroj | Kde | Poznámka |
|---|---|---|
| USB 5 V | konektor USB-C | napájanie a programovanie |

## Mapa pinov

![Olimex ESP32-GATEWAY - mapa pinov](pinout/pinout.png)

| GPIO | Funkcia v ctrl32 | Poznámka |
|---|---|---|
| 2 | SPI MOSI | ⚠ strapping pin |
| 5 | Ethernet PHY power (LAN8710A) | ⚠ používa doska |
| 6 | SPI flash modulu | ⚠ používa doska |
| 7 | SPI flash modulu | ⚠ používa doska |
| 8 | SPI flash modulu | ⚠ používa doska |
| 9 | SPI flash modulu | ⚠ používa doska |
| 10 | SPI flash modulu | ⚠ používa doska |
| 11 | SPI flash modulu | ⚠ používa doska |
| 13 | free (SPI CS line) |  |
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
| 32 | I2C SDA |  |
| 33 | free (LED0 line) | ADC1 |
| 34 | voľný - tlačidlo dosky | ⚠ len vstup, ADC1 |

20-pinový konektor **EXT** nesie voľné piny a linky I2C / SPI. LED dosky je
na GPIO33 a jej tlačidlo na GPIO34 (len vstup). Voľných pinov ostáva málo:
ďalšie I/O idú cez Modbus TCP alebo čipy na I2C.

## Bezpečnosť

- Doska nie je určená na bezpečnostné funkcie. Núdzové zastavenie, dverový
  spínač či svetelná závora sa zapájajú v hardvéri, nikdy cez program.
- Piny GPIO majú 3,3 V. Signál 24 V potrebuje optočlen alebo prevodník
  úrovní; cievka relé potrebuje budič (reléový modul ho má).

---

[← Prehľad](README.sk.md) | [Prehľad](README.sk.md) | [Nahratie runtime →](install.sk.md)
