---
title: 'Olimex ESP32-POE2: hardware a zapojení'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-POE2 - mapa pinů
tags:
- esp32
- ethernet
- poe
- psram
- olimex
---

# Hardware a zapojení

## Co je potřeba

- Olimex ESP32-POE2.
- Datový kabel USB-C - na první nahrání runtime.
- Napájení: PoE switch či injektor (IEEE 802.3at, třída 4 pro plných 25 W), nebo zdroj 5 V přes USB.
- Síťový kabel a volný port ve tvé síti.
- PC s [editorem ctrl32](https://ctrl32.com/download/) (Windows).
- Volitelně pro příklad all-in-one: tlačítko BUT1 je na desce; reléový modul nebo LED na GPIO4 (UEXT); potenciometr (10 k) mezi 3,3 V a GND s jezdcem na GPIO36; 3,3 V převodník CAN na GPIO5 (TX) / GPIO39 (RX).

## Napájení

| Zdroj | Kde | Poznámka |
|---|---|---|
| PoE | konektor Ethernet | IEEE 802.3at třída 4, až 25 W |
| USB 5 V | konektor USB-C | cesta pro první nahrání |
| Li-Po baterie | konektor baterie | nabíjí se na desce |

Při napájení přes Ethernet deska napájí i vnější obvody: **24 V / 0,75 A
nebo 12 V / 1,5 A** (volí propojka), **5 V / 1,5 A** a **3,3 V / 1 A**,
celkem 25 W.

!!! danger "Nikdy nepřipojuj USB a PoE současně"
    ESP32-POE2 **není galvanicky oddělená** od napájení z Ethernetu.
    Runtime nahraj přes USB s odpojeným síťovým kabelem (nebo z portu bez
    PoE) a teprve potom desku napájej z PoE.

## Mapa pinů

![Olimex ESP32-POE2 - mapa pinů](pinout/pinout.png)

| GPIO | Funkce v ctrl32 | Poznámka |
|---|---|---|
| 0 | Ethernet 50 MHz clock (LAN8710A) | ⚠ používá deska |
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
| 18 | Ethernet MDIO (LAN8710A) | ⚠ používá deska |
| 19 | Ethernet RMII TXD0 (LAN8710A) | ⚠ používá deska |
| 21 | Ethernet RMII TX_EN (LAN8710A) | ⚠ používá deska |
| 22 | Ethernet RMII TXD1 (LAN8710A) | ⚠ používá deska |
| 23 | Ethernet MDC (LAN8710A) | ⚠ používá deska |
| 25 | Ethernet RMII RXD0 (LAN8710A) | ⚠ používá deska |
| 26 | Ethernet RMII RXD1 (LAN8710A) | ⚠ používá deska |
| 27 | Ethernet RMII CRS_DV (LAN8710A) | ⚠ používá deska |
| 33 | I2C SCL |  |
| 34 | volný - tlačítko desky | ⚠ jen vstup, ADC1 |
| 36 | free (UART RX line) | ⚠ jen vstup, ADC1 |
| 39 | volný vstup | ⚠ jen vstup, ADC1 |

Volné piny jsou na konektorech **EXT** a na konektoru **UEXT**. GPIO34 až
GPIO39 jsou pouze vstupy. PSRAM modulu zabírá GPIO16 / GPIO17, proto
hodiny Ethernetu běží na GPIO0 a I2C používá GPIO13 / GPIO33.

## Bezpečnost

- Deska není určena pro bezpečnostní funkce. Nouzové zastavení, dveřní
  spínač nebo světelná závora se zapojují v hardwaru, nikdy přes program.
- Piny GPIO mají 3,3 V. Vstup 24 V potřebuje optočlen nebo převodník
  úrovní; cívka relé potřebuje budič (reléový modul ho má).

---

[← Přehled](README.cs.md) | [Přehled](README.cs.md) | [Nahrání runtime →](install.cs.md)
