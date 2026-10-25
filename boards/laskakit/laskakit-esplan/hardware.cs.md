---
title: 'LaskaKit ESPlan: hardware a zapojení'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: LaskaKit ESPlan - mapa pinů
tags:
- esp32
- ethernet
- rs485
- modbus
- laskakit
---

# Hardware a zapojení

## Co je potřeba

- LaskaKit ESPlan.
- Datový kabel USB-C - pro první nahrání runtime.
- Napájení: 12 nebo 24 V DC na šroubovací svorce (7-40 V), nebo 5 V přes USB-C.
- Síťový kabel a volný port v síti.
- PC s [editorem ctrl32](https://ctrl32.com/download/) (Windows).
- Volitelně pro příklad all-in-one: čidlo teploty Modbus RTU (unit 1) na svorce RS-485; tlačítko z GPIO16 na GND; potenciometr (10 k) mezi 3,3 V a GND s jezdcem na GPIO35; 3,3 V převodník CAN na GPIO14 (TX) / GPIO39 (RX).

## Napájení

| Zdroj | Kde | Poznámka |
|---|---|---|
| 7-40 V DC | šroubovací svorka | doporučeno 12 nebo 24 V |
| USB 5 V | konektor USB-C | cesta pro první nahrání |
| PoE | přes volitelný modul PoE (802.3af) | přídavný modul |

## Mapa pinů

![LaskaKit ESPlan - mapa pinů](pinout/pinout.png)

| GPIO | Funkce v ctrl32 | Poznámka |
|---|---|---|
| 0 | free (LED0 line) | ⚠ strapping pin |
| 4 | RS485 TX |  |
| 5 | Ethernet PHY power (LAN8720A) | ⚠ používá deska |
| 6 | SPI flash modulu | ⚠ používá deska |
| 7 | SPI flash modulu | ⚠ používá deska |
| 8 | SPI flash modulu | ⚠ používá deska |
| 9 | SPI flash modulu | ⚠ používá deska |
| 10 | SPI flash modulu | ⚠ používá deska |
| 11 | SPI flash modulu | ⚠ používá deska |
| 12 | SPI MISO | ⚠ strapping pin |
| 13 | SPI MOSI |  |
| 14 | free (SPI SCLK line) |  |
| 15 | SPI CS | ⚠ strapping pin |
| 16 | volný I/O |  |
| 17 | Ethernet 50 MHz clock (LAN8720A) | ⚠ používá deska |
| 18 | Ethernet MDIO (LAN8720A) | ⚠ používá deska |
| 19 | Ethernet RMII TXD0 (LAN8720A) | ⚠ používá deska |
| 21 | Ethernet RMII TX_EN (LAN8720A) | ⚠ používá deska |
| 22 | Ethernet RMII TXD1 (LAN8720A) | ⚠ používá deska |
| 23 | Ethernet MDC (LAN8720A) | ⚠ používá deska |
| 25 | Ethernet RMII RXD0 (LAN8720A) | ⚠ používá deska |
| 26 | Ethernet RMII RXD1 (LAN8720A) | ⚠ používá deska |
| 27 | Ethernet RMII CRS_DV (LAN8720A) | ⚠ používá deska |
| 32 | TOUCH SCL |  |
| 33 | TOUCH SDA |  |
| 35 | volný vstup | ⚠ jen vstup, ADC1 |
| 36 | RS485 RX |  |
| 39 | volný vstup | ⚠ jen vstup, ADC1 |

**RS-485:** A a B na svorce, převodník WS3081 na GPIO4 (TX) / GPIO36 (RX);
propojka zapíná zakončovací odpor 120 ohm - zapni ho jen na obou koncích
linky. Konektory **uSup** nesou I2C (GPIO33 / GPIO32) a SPI. LED desky je
na GPIO0 (strapping pin - nech ho jako výstup, který řídí program).

## Bezpečnost

- Deska není určena pro bezpečnostní funkce. Nouzové zastavení, dveřní
  spínač nebo světelná závora se zapojují v hardwaru, nikdy přes program.
- Piny GPIO mají 3,3 V. Signál 24 V potřebuje optočlen nebo převodník
  úrovní; cívka relé potřebuje budič (reléový modul ho má).

---

[← Přehled](README.cs.md) | [Přehled](README.cs.md) | [Nahrání runtime →](install.cs.md)
