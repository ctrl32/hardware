---
title: 'Olimex ESP32-P4-DevKit: hardvér a zapojenie'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-P4-DevKit - mapa pinov
tags:
- esp32-p4
- ethernet
- olimex
---

# Hardvér a zapojenie

## Čo treba

- Olimex ESP32-P4-DevKit.
- Dátový kábel USB-C - na nahratie aj napájanie (5 V).
- Sieťový kábel a voľný port v sieti.
- PC s [editorom ctrl32](https://ctrl32.com/download/) (Windows).
- Voliteľne pre príklad all-in-one: LED (GPIO2) je na doske; tlačidlo z GPIO20 na GND; 3,3 V prevodník CAN na GPIO5 / GPIO21 a prevodník RS-485 na GPIO22 / GPIO23 / GPIO32 (DE).

## Napájanie

| Zdroj | Kde | Poznámka |
|---|---|---|
| USB 5 V | konektor USB-C | napájanie, programovanie a ladenie |
| PoE | cez rozširujúci modul PoE | voliteľne |

## Mapa pinov

![Olimex ESP32-P4-DevKit - mapa pinov](pinout/pinout.png)

| GPIO | Funkcia v ctrl32 | Poznámka |
|---|---|---|
| 2 | free (LED0 line) |  |
| 4 | SPI SCLK |  |
| 5 | free (SPI CS line) |  |
| 7 | I2C SDA |  |
| 8 | I2C SCL |  |
| 20 | voľný I/O |  |
| 21 | voľný I/O |  |
| 22 | voľný I/O |  |
| 23 | voľný I/O |  |
| 28 | Ethernet RMII (IP101GRI) | ⚠ používa doska |
| 29 | Ethernet RMII (IP101GRI) | ⚠ používa doska |
| 30 | Ethernet RMII (IP101GRI) | ⚠ používa doska |
| 31 | Ethernet MDC (IP101GRI) | ⚠ používa doska |
| 32 | voľný I/O |  |
| 33 | voľný I/O |  |
| 34 | Ethernet RMII (IP101GRI) | ⚠ používa doska |
| 35 | Ethernet RMII (IP101GRI) | ⚠ používa doska |
| 46 | voľný I/O |  |
| 47 | voľný I/O |  |
| 48 | voľný I/O |  |
| 49 | Ethernet RMII (IP101GRI) | ⚠ používa doska |
| 50 | Ethernet RMII (IP101GRI) | ⚠ používa doska |
| 51 | Ethernet PHY reset (IP101GRI) | ⚠ používa doska |
| 52 | Ethernet MDIO (IP101GRI) | ⚠ používa doska |
| 53 | SPI MOSI |  |
| 54 | SPI MISO |  |

Všetky GPIO sú na dvoch 20-pinových lištách. ESP32-P4 nemá analógový vstup,
ktorý by ctrl32 používal: analógové signály idú cez I2C prevodník ADC
(ADS1115 na konektore pUEXT, I2C GPIO7 / GPIO8) alebo cez modul Modbus.

## Bezpečnosť

- Doska nie je určená na bezpečnostné funkcie. Núdzové zastavenie, dverový
  spínač či svetelná závora sa zapájajú v hardvéri, nikdy cez program.
- Piny GPIO majú 3,3 V. Signál 24 V potrebuje optočlen alebo prevodník
  úrovní; cievka relé potrebuje budič (reléový modul ho má).

---

[← Prehľad](README.sk.md) | [Prehľad](README.sk.md) | [Nahratie runtime →](install.sk.md)
