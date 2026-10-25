---
title: 'Olimex ESP32-P4-PC: hardware a zapojení'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-P4-PC - mapa pinů
tags:
- esp32-p4
- ethernet
- ups
- olimex
---

# Hardware a zapojení

## Co je potřeba

- Olimex ESP32-P4-PC.
- Datový kabel USB-C - pro nahrání i napájení (5 V).
- Síťový kabel a volný port v síti.
- PC s [editorem ctrl32](https://ctrl32.com/download/) (Windows).
- Volitelně: článek Li-Po pro zálohu baterií; pro příklad all-in-one je uživatelská LED (GPIO2) na desce a tlačítko jde z GPIO14 na GND (EXT1); 3,3 V převodník CAN na GPIO5 / GPIO15 a převodník RS-485 na GPIO16 / GPIO17 / GPIO18 (DE).

## Napájení

| Zdroj | Kde | Poznámka |
|---|---|---|
| USB 5 V | konektor USB-C | napájení, programování a ladění |
| Li-Po baterie | konektor baterie | nabíjí se na desce; při výpadku zdroje převezme napájení (UPS) |
| PoE | přes rozšiřující modul PoE | volitelně |

## Mapa pinů

![Olimex ESP32-P4-PC - mapa pinů](pinout/pinout.png)

| GPIO | Funkce v ctrl32 | Poznámka |
|---|---|---|
| 2 | free (LED0 line) |  |
| 4 | SPI SCLK |  |
| 5 | free (SPI CS line) |  |
| 14 | volný I/O |  |
| 15 | volný I/O |  |
| 16 | volný I/O |  |
| 17 | volný I/O |  |
| 18 | volný I/O |  |
| 19 | volný I/O |  |
| 20 | volný I/O |  |
| 21 | USB HUB RST | ⚠  |
| 22 | I2C SDA |  |
| 23 | I2C SCL |  |
| 28 | Ethernet RMII (IP101GRI) | ⚠ používá deska |
| 29 | Ethernet RMII (IP101GRI) | ⚠ používá deska |
| 30 | Ethernet RMII (IP101GRI) | ⚠ používá deska |
| 31 | Ethernet MDC (IP101GRI) | ⚠ používá deska |
| 32 | volný I/O |  |
| 33 | volný I/O |  |
| 34 | Ethernet RMII (IP101GRI) | ⚠ používá deska |
| 35 | Ethernet RMII (IP101GRI) | ⚠ používá deska |
| 36 | volný I/O | ⚠ strapping pin |
| 46 | volný I/O |  |
| 47 | volný I/O |  |
| 48 | volný I/O |  |
| 49 | Ethernet RMII (IP101GRI) | ⚠ používá deska |
| 50 | Ethernet RMII (IP101GRI) | ⚠ používá deska |
| 51 | Ethernet PHY reset (IP101GRI) | ⚠ používá deska |
| 52 | Ethernet MDIO (IP101GRI) | ⚠ používá deska |
| 53 | SPI MOSI |  |
| 54 | SPI MISO |  |

Volné piny jsou na 20pinové liště **EXT1**: GPIO14 až GPIO20, 32, 33, 36,
46, 47, 48 a uživatelská LED na GPIO2. Konektor **UEXT** nese I2C
(GPIO22 / GPIO23 - sdílené s můstkem HDMI), SPI (GPIO4 / 53 / 54, CS
GPIO5) a UART konzole. ESP32-P4 nemá analogový vstup, který by ctrl32
používal: analogové signály jdou přes I2C převodník ADC (ADS1115 na UEXT)
nebo přes modul Modbus. CAN a RS-485 jdou na volné piny EXT1 s 3,3 V
modulem převodníku.

## Bezpečnost

- Deska není určena pro bezpečnostní funkce. Nouzové zastavení, dveřní
  spínač nebo světelná závora se zapojují v hardwaru, nikdy přes program.
- Piny GPIO mají 3,3 V. Signál 24 V potřebuje optočlen nebo převodník
  úrovní; cívka relé potřebuje budič (reléový modul ho má).

## Fotky

![Olimex ESP32-P4-PC - fotka 1](img/board-01.jpg)
![Olimex ESP32-P4-PC - fotka 2](img/board-02.jpg)
![Olimex ESP32-P4-PC - fotka 3](img/board-03.jpg)
![Olimex ESP32-P4-PC - fotka 4](img/board-04.jpg)

---

[← Přehled](README.cs.md) | [Přehled](README.cs.md) | [Nahrání runtime →](install.cs.md)
