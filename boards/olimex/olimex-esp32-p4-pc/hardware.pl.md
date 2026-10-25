---
title: 'Olimex ESP32-P4-PC: sprzęt i okablowanie'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-P4-PC - mapa pinów
tags:
- esp32-p4
- ethernet
- ups
- olimex
---

# Sprzęt i okablowanie

## Czego potrzebujesz

- Olimex ESP32-P4-PC.
- Kabel USB-C do transmisji danych - do wgrywania i do zasilania (5 V).
- Kabel Ethernet i wolny port w twojej sieci.
- PC z [edytorem ctrl32](https://ctrl32.com/download/) (Windows).
- Opcjonalnie: ogniwo Li-Po jako podtrzymanie bateryjne; dla przykładu all-in-one dioda LED użytkownika (GPIO2) jest na płytce, a przycisk idzie z GPIO14 do GND (EXT1); transceiver CAN 3,3 V na GPIO5 / GPIO15 i transceiver RS-485 na GPIO16 / GPIO17 / GPIO18 (DE).

## Zasilanie

| Źródło | Gdzie | Uwaga |
|---|---|---|
| USB 5 V | złącze USB-C | zasilanie, programowanie i debugowanie |
| Akumulator Li-Po | złącze akumulatora | ładowany na płytce; przejmuje zasilanie, gdy zawiedzie zasilacz (UPS) |
| PoE | przez rozszerzenie PoE | opcjonalnie |

## Mapa pinów

![Olimex ESP32-P4-PC - mapa pinów](pinout/pinout.png)

| GPIO | Funkcja w ctrl32 | Uwaga |
|---|---|---|
| 2 | free (LED0 line) |  |
| 4 | SPI SCLK |  |
| 5 | free (SPI CS line) |  |
| 14 | wolny - I/O |  |
| 15 | wolny - I/O |  |
| 16 | wolny - I/O |  |
| 17 | wolny - I/O |  |
| 18 | wolny - I/O |  |
| 19 | wolny - I/O |  |
| 20 | wolny - I/O |  |
| 21 | USB HUB RST | ⚠  |
| 22 | I2C SDA |  |
| 23 | I2C SCL |  |
| 28 | Ethernet RMII (IP101GRI) | ⚠ zajęty przez płytkę |
| 29 | Ethernet RMII (IP101GRI) | ⚠ zajęty przez płytkę |
| 30 | Ethernet RMII (IP101GRI) | ⚠ zajęty przez płytkę |
| 31 | Ethernet MDC (IP101GRI) | ⚠ zajęty przez płytkę |
| 32 | wolny - I/O |  |
| 33 | wolny - I/O |  |
| 34 | Ethernet RMII (IP101GRI) | ⚠ zajęty przez płytkę |
| 35 | Ethernet RMII (IP101GRI) | ⚠ zajęty przez płytkę |
| 36 | wolny - I/O | ⚠ pin strapping |
| 46 | wolny - I/O |  |
| 47 | wolny - I/O |  |
| 48 | wolny - I/O |  |
| 49 | Ethernet RMII (IP101GRI) | ⚠ zajęty przez płytkę |
| 50 | Ethernet RMII (IP101GRI) | ⚠ zajęty przez płytkę |
| 51 | Ethernet PHY reset (IP101GRI) | ⚠ zajęty przez płytkę |
| 52 | Ethernet MDIO (IP101GRI) | ⚠ zajęty przez płytkę |
| 53 | SPI MOSI |  |
| 54 | SPI MISO |  |

Wolne piny są na 20-pinowym złączu **EXT1**: GPIO14 do GPIO20, 32, 33,
36, 46, 47, 48 oraz dioda LED użytkownika na GPIO2. Złącze **UEXT**
wyprowadza I2C (GPIO22 / GPIO23 - współdzielone z mostkiem HDMI), SPI
(GPIO4 / 53 / 54, CS GPIO5) i UART konsoli. ESP32-P4 nie ma wejścia
analogowego, którego używa ctrl32: sygnały analogowe idą przez
przetwornik I2C (ADS1115 na UEXT) lub moduł Modbus. CAN i RS-485 trafiają
na wolne piny EXT1 z modułem transceivera 3,3 V.

## Bezpieczeństwo

- Płytka nie jest przeznaczona do funkcji bezpieczeństwa. Wyłącznik
  awaryjny, wyłącznik drzwi lub kurtyna świetlna są podłączone sprzętowo,
  nigdy przez program.
- Piny GPIO pracują na 3,3 V. Sygnał 24 V wymaga transoptora lub
  konwertera poziomów; cewka przekaźnika wymaga sterownika (moduł
  przekaźnikowy go ma).

## Zdjęcia

![Olimex ESP32-P4-PC - zdjęcie 1](img/board-01.jpg)
![Olimex ESP32-P4-PC - zdjęcie 2](img/board-02.jpg)
![Olimex ESP32-P4-PC - zdjęcie 3](img/board-03.jpg)
![Olimex ESP32-P4-PC - zdjęcie 4](img/board-04.jpg)

---

[← Przegląd](README.pl.md) | [Przegląd](README.pl.md) | [Instalacja runtime →](install.pl.md)
