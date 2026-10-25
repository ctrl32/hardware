---
title: 'Olimex ESP32-EVB: hardware a zapojení'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-EVB - mapa pinů
tags:
- esp32
- ethernet
- can
- relay
- olimex
---

# Hardware a zapojení

## Co je potřeba

- Olimex ESP32-EVB.
- Datový kabel micro-USB - na první nahrání runtime.
- Napájení: zdroj 5 V přes USB, nebo 5 V na šroubové svorce.
- Síťový kabel a volný port ve tvé síti.
- PC s [editorem ctrl32](https://ctrl32.com/download/) (Windows).
- Volitelně pro příklad all-in-one: potenciometr (10 k) mezi 3,3 V a GND s jezdcem na GPIO36 (UEXT); uzel CAN nebo CAN adaptér a dva zakončovací odpory 120 ohm.
- Volitelně: displej Olimex MOD-LCD2.8RTP (2,8 palce, 240 x 320, odporový dotyk) na konektoru UEXT.

## Napájení

| Zdroj | Kde | Poznámka |
|---|---|---|
| USB 5 V | konektor micro-USB | cesta pro první nahrání |
| 5 V DC | šroubová svorka | do rozvaděče |
| Li-Po baterie | konektor baterie | nabíjí se na desce |

!!! warning "Relé spínají síťové napětí"
    Kontakty relé zapojuj jen při odpojené desce, v uzavřené krabici, a smí
    to dělat jen osoba oprávněná pracovat na síťových instalacích. Kontakty
    snesou 10 A / 250 VAC; motor nebo topné těleso nad tuto hodnotu
    potřebuje stykač spínaný relé.

## Mapa pinů

![Olimex ESP32-EVB - mapa pinů](pinout/pinout.png)

| GPIO | Funkce v ctrl32 | Poznámka |
|---|---|---|
| 0 | Ethernet 50 MHz clock (LAN8710A) | ⚠ používá deska |
| 2 | TFT MOSI | ⚠ strapping pin |
| 2 | SPI MOSI | ⚠ strapping pin |
| 4 | free (UART TX line) |  |
| 5 | CAN TX |  |
| 6 | SPI flash modulu | ⚠ používá deska |
| 7 | SPI flash modulu | ⚠ používá deska |
| 8 | SPI flash modulu | ⚠ používá deska |
| 9 | SPI flash modulu | ⚠ používá deska |
| 10 | SPI flash modulu | ⚠ používá deska |
| 11 | SPI flash modulu | ⚠ používá deska |
| 13 | I2C SDA |  |
| 14 | TFT SCLK |  |
| 14 | SPI SCLK |  |
| 15 | TFT DC | ⚠ strapping pin |
| 15 | SPI MISO | ⚠ strapping pin |
| 16 | I2C SCL |  |
| 17 | TFT CS |  |
| 17 | free (SPI CS line) |  |
| 18 | Ethernet MDIO (LAN8710A) | ⚠ používá deska |
| 19 | Ethernet RMII TXD0 (LAN8710A) | ⚠ používá deska |
| 21 | Ethernet RMII TX_EN (LAN8710A) | ⚠ používá deska |
| 22 | Ethernet RMII TXD1 (LAN8710A) | ⚠ používá deska |
| 23 | Ethernet MDC (LAN8710A) | ⚠ používá deska |
| 25 | Ethernet RMII RXD0 (LAN8710A) | ⚠ používá deska |
| 26 | Ethernet RMII RXD1 (LAN8710A) | ⚠ používá deska |
| 27 | Ethernet RMII CRS_DV (LAN8710A) | ⚠ používá deska |
| 32 | free (REL1 line) | ADC1 |
| 33 | free (REL2 line) | ADC1 |
| 34 | volný - tlačítko desky | ⚠ jen vstup, ADC1 |
| 35 | CAN RX |  |
| 36 | free (UART RX line) | ⚠ jen vstup, ADC1 |

**Relé:** REL1 na GPIO32, REL2 na GPIO33. **Tlačítko:** BUT1 na GPIO34
(pouze vstup). **CAN:** převodník na desce na GPIO5 (TX) / GPIO35 (RX),
CAN_H / CAN_L na svorce - sběrnici zakonči odporem 120 ohm na obou
koncích. Konektor **UEXT** nese I2C (GPIO13 / GPIO16), SPI a volný UART
(GPIO4 / GPIO36); volitelný displej používá jeho linky SPI.

## Bezpečnost

- Deska není určena pro bezpečnostní funkce. Nouzové zastavení, dveřní
  spínač nebo světelná závora se zapojují v hardwaru, nikdy přes program.
- Piny GPIO mají 3,3 V. Signál 24 V potřebuje optočlen nebo převodník
  úrovní; cívka relé potřebuje budič (reléový modul ho má).

---

[← Přehled](README.cs.md) | [Přehled](README.cs.md) | [Nahrání runtime →](install.cs.md)
