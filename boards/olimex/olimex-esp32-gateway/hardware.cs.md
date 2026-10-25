---
title: 'Olimex ESP32-GATEWAY: hardware a zapojení'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-GATEWAY - mapa pinů
tags:
- esp32
- ethernet
- gateway
- olimex
---

# Hardware a zapojení

## Co je potřeba

- Olimex ESP32-GATEWAY.
- Datový kabel USB-C - na nahrání i napájení (5 V).
- Síťový kabel a volný port ve tvé síti.
- PC s [editorem ctrl32](https://ctrl32.com/download/) (Windows).
- Příklad all-in-one používá vlastní tlačítko desky (GPIO34) a LED (GPIO33) - nic dalšího není třeba zapojovat.

## Napájení

| Zdroj | Kde | Poznámka |
|---|---|---|
| USB 5 V | konektor USB-C | napájení a programování |

## Mapa pinů

![Olimex ESP32-GATEWAY - mapa pinů](pinout/pinout.png)

| GPIO | Funkce v ctrl32 | Poznámka |
|---|---|---|
| 2 | SPI MOSI | ⚠ strapping pin |
| 5 | Ethernet PHY power (LAN8710A) | ⚠ používá deska |
| 6 | SPI flash modulu | ⚠ používá deska |
| 7 | SPI flash modulu | ⚠ používá deska |
| 8 | SPI flash modulu | ⚠ používá deska |
| 9 | SPI flash modulu | ⚠ používá deska |
| 10 | SPI flash modulu | ⚠ používá deska |
| 11 | SPI flash modulu | ⚠ používá deska |
| 13 | free (SPI CS line) |  |
| 14 | SPI SCLK |  |
| 15 | SPI MISO | ⚠ strapping pin |
| 16 | I2C SCL |  |
| 17 | Ethernet 50 MHz clock (LAN8710A) | ⚠ používá deska |
| 18 | Ethernet MDIO (LAN8710A) | ⚠ používá deska |
| 19 | Ethernet RMII TXD0 (LAN8710A) | ⚠ používá deska |
| 21 | Ethernet RMII TX_EN (LAN8710A) | ⚠ používá deska |
| 22 | Ethernet RMII TXD1 (LAN8710A) | ⚠ používá deska |
| 23 | Ethernet MDC (LAN8710A) | ⚠ používá deska |
| 25 | Ethernet RMII RXD0 (LAN8710A) | ⚠ používá deska |
| 26 | Ethernet RMII RXD1 (LAN8710A) | ⚠ používá deska |
| 27 | Ethernet RMII CRS_DV (LAN8710A) | ⚠ používá deska |
| 32 | I2C SDA |  |
| 33 | free (LED0 line) | ADC1 |
| 34 | volný - tlačítko desky | ⚠ jen vstup, ADC1 |

20pinový konektor **EXT** nese volné piny a linky I2C / SPI. LED desky je
na GPIO33 a její tlačítko na GPIO34 (pouze vstup). Volných pinů zbývá
málo: další I/O jdou přes Modbus TCP nebo čipy na I2C.

## Bezpečnost

- Deska není určena pro bezpečnostní funkce. Nouzové zastavení, dveřní
  spínač nebo světelná závora se zapojují v hardwaru, nikdy přes program.
- Piny GPIO mají 3,3 V. Signál 24 V potřebuje optočlen nebo převodník
  úrovní; cívka relé potřebuje budič (reléový modul ho má).

---

[← Přehled](README.cs.md) | [Přehled](README.cs.md) | [Nahrání runtime →](install.cs.md)
