---
title: 'Olimex ESP32-P4-DevKit: sprzęt i okablowanie'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-P4-DevKit - mapa pinów
tags:
- esp32-p4
- ethernet
- olimex
---

# Sprzęt i okablowanie

## Czego potrzebujesz

- Olimex ESP32-P4-DevKit.
- Kabel USB-C do transmisji danych - do wgrywania i do zasilania (5 V).
- Kabel Ethernet i wolny port w twojej sieci.
- PC z [edytorem ctrl32](https://ctrl32.com/download/) (Windows).
- Opcjonalnie, dla przykładu all-in-one: dioda LED (GPIO2) jest na płytce; przycisk z GPIO20 do GND; transceiver CAN 3,3 V na GPIO5 / GPIO21 i transceiver RS-485 na GPIO22 / GPIO23 / GPIO32 (DE).

## Zasilanie

| Źródło | Gdzie | Uwaga |
|---|---|---|
| USB 5 V | złącze USB-C | zasilanie, programowanie i debugowanie |
| PoE | przez rozszerzenie PoE | opcjonalnie |

## Mapa pinów

![Olimex ESP32-P4-DevKit - mapa pinów](pinout/pinout.png)

| GPIO | Funkcja w ctrl32 | Uwaga |
|---|---|---|
| 2 | free (LED0 line) |  |
| 4 | SPI SCLK |  |
| 5 | free (SPI CS line) |  |
| 7 | I2C SDA |  |
| 8 | I2C SCL |  |
| 20 | wolny - I/O |  |
| 21 | wolny - I/O |  |
| 22 | wolny - I/O |  |
| 23 | wolny - I/O |  |
| 28 | Ethernet RMII (IP101GRI) | ⚠ zajęty przez płytkę |
| 29 | Ethernet RMII (IP101GRI) | ⚠ zajęty przez płytkę |
| 30 | Ethernet RMII (IP101GRI) | ⚠ zajęty przez płytkę |
| 31 | Ethernet MDC (IP101GRI) | ⚠ zajęty przez płytkę |
| 32 | wolny - I/O |  |
| 33 | wolny - I/O |  |
| 34 | Ethernet RMII (IP101GRI) | ⚠ zajęty przez płytkę |
| 35 | Ethernet RMII (IP101GRI) | ⚠ zajęty przez płytkę |
| 46 | wolny - I/O |  |
| 47 | wolny - I/O |  |
| 48 | wolny - I/O |  |
| 49 | Ethernet RMII (IP101GRI) | ⚠ zajęty przez płytkę |
| 50 | Ethernet RMII (IP101GRI) | ⚠ zajęty przez płytkę |
| 51 | Ethernet PHY reset (IP101GRI) | ⚠ zajęty przez płytkę |
| 52 | Ethernet MDIO (IP101GRI) | ⚠ zajęty przez płytkę |
| 53 | SPI MOSI |  |
| 54 | SPI MISO |  |

Wszystkie GPIO są na dwóch 20-pinowych złączach. ESP32-P4 nie ma wejścia
analogowego, którego używa ctrl32: sygnały analogowe idą przez
przetwornik I2C (ADS1115 na złączu pUEXT, I2C GPIO7 / GPIO8) lub moduł
Modbus.

## Bezpieczeństwo

- Płytka nie jest przeznaczona do funkcji bezpieczeństwa. Wyłącznik
  awaryjny, wyłącznik drzwi lub kurtyna świetlna są podłączone sprzętowo,
  nigdy przez program.
- Piny GPIO pracują na 3,3 V. Sygnał 24 V wymaga transoptora lub
  konwertera poziomów; cewka przekaźnika wymaga sterownika (moduł
  przekaźnikowy go ma).

---

[← Przegląd](README.pl.md) | [Przegląd](README.pl.md) | [Instalacja runtime →](install.pl.md)
