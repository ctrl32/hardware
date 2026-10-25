---
title: 'Olimex ESP32-PoE-ISO: hardware a zapojení'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-PoE-ISO - mapa pinů
tags:
- esp32
- ethernet
- poe
- isolated
- olimex
---

# Hardware a zapojení

## Co je potřeba

- Olimex ESP32-PoE-ISO (varianta WROOM-32E, bez PSRAM).
- Datový kabel micro-USB - na první nahrání runtime.
- Napájení: PoE switch či injektor (IEEE 802.3af), nebo zdroj 5 V přes USB.
- Síťový kabel a volný port ve tvé síti.
- PC s [editorem ctrl32](https://ctrl32.com/download/) (Windows).
- Volitelně pro příklad all-in-one: tlačítko BUT1 je na desce; reléový modul nebo LED s rezistorem na GPIO4 (UEXT); potenciometr (10 k) mezi 3,3 V a GND s jezdcem na GPIO33 (EXT2); 3,3 V převodník CAN na GPIO5 (TX) / GPIO36 (RX).

## Napájení

| Zdroj | Kde | Poznámka |
|---|---|---|
| PoE | konektor Ethernet, z PoE switche nebo injektoru | IEEE 802.3af, oddělené |
| USB 5 V | konektor micro-USB | cesta pro první nahrání |
| Li-Po baterie | konektor baterie | nabíjí se na desce |

Napájení PoE je od desky **galvanicky oddělené**: na rozdíl od obyčejné
ESP32-PoE mohou být USB k PC a PoE zapojené současně - runtime jde nahrát
a sledovat online, zatímco deska zůstává na svém PoE switchi.

## Mapa pinů

![Olimex ESP32-PoE-ISO - mapa pinů](pinout/pinout.png)

| GPIO | Funkce v ctrl32 | Poznámka |
|---|---|---|
| 2 | SPI MOSI | ⚠ strapping pin |
| 4 | free (UART TX line) |  |
| 5 | free (SPI CS line) |  |
| 6 | SPI flash modulu | ⚠ používá deska |
| 7 | SPI flash modulu | ⚠ používá deska |
| 8 | SPI flash modulu | ⚠ používá deska |
| 9 | SPI flash modulu | ⚠ používá deska |
| 10 | SPI flash modulu | ⚠ používá deska |
| 11 | SPI flash modulu | ⚠ používá deska |
| 12 | Ethernet PHY power (LAN8710A) | ⚠ používá deska |
| 13 | I2C SDA |  |
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
| 33 | volný I/O | ADC1 |
| 34 | volný - tlačítko desky | ⚠ jen vstup, ADC1 |
| 35 | volný vstup | ⚠ jen vstup, ADC1 |
| 36 | free (UART RX line) | ⚠ jen vstup, ADC1 |

Volné piny jsou na konektorech **EXT1 / EXT2** (2,54 mm) a na konektoru
**UEXT**. GPIO34 až GPIO39 jsou pouze vstupy - výstup na nich editor
odmítne. Konektor UEXT nese I2C (GPIO13 / GPIO16) a SPI (GPIO14 / GPIO2 /
GPIO15, sdílené se slotem microSD).

## Bezpečnost

- Deska není určena pro bezpečnostní funkce. Nouzové zastavení, dveřní
  spínač nebo světelná závora se zapojují v hardwaru, nikdy přes program.
- Piny GPIO mají 3,3 V. Vstup 24 V potřebuje optočlen nebo převodník
  úrovní; cívka relé potřebuje budič (reléový modul ho má).

---

[← Přehled](README.cs.md) | [Přehled](README.cs.md) | [Nahrání runtime →](install.cs.md)
