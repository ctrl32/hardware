---
title: 'LaskaKit ESPlan: hardvér a zapojenie'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: LaskaKit ESPlan - mapa pinov
tags:
- esp32
- ethernet
- rs485
- modbus
- laskakit
---

# Hardvér a zapojenie

## Čo treba

- LaskaKit ESPlan.
- Dátový kábel USB-C - na prvé nahratie runtime.
- Napájanie: 12 alebo 24 V DC na skrutkovej svorke (7-40 V), alebo 5 V cez USB-C.
- Sieťový kábel a voľný port v sieti.
- PC s [editorom ctrl32](https://ctrl32.com/download/) (Windows).
- Voliteľne pre príklad all-in-one: snímač teploty Modbus RTU (unit 1) na svorke RS-485; tlačidlo z GPIO16 na GND; potenciometer (10 k) medzi 3,3 V a GND s bežcom na GPIO35; 3,3 V prevodník CAN na GPIO14 (TX) / GPIO39 (RX).

## Napájanie

| Zdroj | Kde | Poznámka |
|---|---|---|
| 7-40 V DC | skrutková svorka | odporúčané 12 alebo 24 V |
| USB 5 V | konektor USB-C | cesta na prvé nahratie |
| PoE | cez voliteľný modul PoE (802.3af) | prídavný modul |

## Mapa pinov

![LaskaKit ESPlan - mapa pinov](pinout/pinout.png)

| GPIO | Funkcia v ctrl32 | Poznámka |
|---|---|---|
| 0 | free (LED0 line) | ⚠ strapping pin |
| 4 | RS485 TX |  |
| 5 | Ethernet PHY power (LAN8720A) | ⚠ používa doska |
| 6 | SPI flash modulu | ⚠ používa doska |
| 7 | SPI flash modulu | ⚠ používa doska |
| 8 | SPI flash modulu | ⚠ používa doska |
| 9 | SPI flash modulu | ⚠ používa doska |
| 10 | SPI flash modulu | ⚠ používa doska |
| 11 | SPI flash modulu | ⚠ používa doska |
| 12 | SPI MISO | ⚠ strapping pin |
| 13 | SPI MOSI |  |
| 14 | free (SPI SCLK line) |  |
| 15 | SPI CS | ⚠ strapping pin |
| 16 | voľný I/O |  |
| 17 | Ethernet 50 MHz clock (LAN8720A) | ⚠ používa doska |
| 18 | Ethernet MDIO (LAN8720A) | ⚠ používa doska |
| 19 | Ethernet RMII TXD0 (LAN8720A) | ⚠ používa doska |
| 21 | Ethernet RMII TX_EN (LAN8720A) | ⚠ používa doska |
| 22 | Ethernet RMII TXD1 (LAN8720A) | ⚠ používa doska |
| 23 | Ethernet MDC (LAN8720A) | ⚠ používa doska |
| 25 | Ethernet RMII RXD0 (LAN8720A) | ⚠ používa doska |
| 26 | Ethernet RMII RXD1 (LAN8720A) | ⚠ používa doska |
| 27 | Ethernet RMII CRS_DV (LAN8720A) | ⚠ používa doska |
| 32 | TOUCH SCL |  |
| 33 | TOUCH SDA |  |
| 35 | voľný vstup | ⚠ len vstup, ADC1 |
| 36 | RS485 RX |  |
| 39 | voľný vstup | ⚠ len vstup, ADC1 |

**RS-485:** A a B na svorke, prevodník WS3081 na GPIO4 (TX) / GPIO36 (RX);
prepojka zapína zakončenie 120 ohm - zapni ho len na dvoch koncoch linky.
Konektory **uSup** nesú I2C (GPIO33 / GPIO32) a SPI. LED dosky je na GPIO0
(strapping pin - nechaj ho ako výstup, ktorý riadi program).

## Bezpečnosť

- Doska nie je určená na bezpečnostné funkcie. Núdzové zastavenie, dverový
  spínač či svetelná závora sa zapájajú v hardvéri, nikdy cez program.
- Piny GPIO majú 3,3 V. Signál 24 V potrebuje optočlen alebo prevodník
  úrovní; cievka relé potrebuje budič (reléový modul ho má).

---

[← Prehľad](README.sk.md) | [Prehľad](README.sk.md) | [Nahratie runtime →](install.sk.md)
