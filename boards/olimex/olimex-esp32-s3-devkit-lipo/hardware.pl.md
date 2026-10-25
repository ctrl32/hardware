---
title: 'Olimex ESP32-S3-DevKit-Lipo: sprzęt i okablowanie'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-S3-DevKit-Lipo - mapa pinów
tags:
- esp32-s3
- wifi
- psram
- battery
- olimex
---

# Sprzęt i okablowanie

## Czego potrzebujesz

- Olimex ESP32-S3-DevKit-Lipo.
- Kabel USB-C do transmisji danych - do wgrywania na złączu oznaczonym UART (CH340X).
- Nazwa i hasło twojej sieci Wi-Fi 2,4 GHz.
- PC z [edytorem ctrl32](https://ctrl32.com/download/) (Windows).
- Opcjonalnie, dla przykładu all-in-one: przycisk Boot/User (GPIO0) i dioda LED (GPIO38) są na płytce; potencjometr (10 k) między 3,3 V a GND ze ślizgaczem na GPIO1; transceiver CAN 3,3 V na GPIO10 / GPIO17 i transceiver RS-485 na GPIO18 / GPIO2 / GPIO4 (DE).

## Zasilanie

| Źródło | Gdzie | Uwaga |
|---|---|---|
| USB 5 V | dowolne złącze USB-C | zasilanie i programowanie |
| Akumulator Li-Po | złącze akumulatora | ładowany na płytce, automatyczne przełączanie |

## Mapa pinów

![Olimex ESP32-S3-DevKit-Lipo - mapa pinów](pinout/pinout.png)

| GPIO | Funkcja w ctrl32 | Uwaga |
|---|---|---|
| 0 | wolny - przycisk płytki | ⚠ pin strapping |
| 1 | wolny - I/O | ADC1 |
| 2 | wolny - I/O | ADC1 |
| 4 | wolny - I/O | ADC1 |
| 5 | free (PWR SENSE line) | ADC1 |
| 6 | free (BAT SENSE line) | ADC1 |
| 7 | wolny - I/O | ADC1 |
| 8 | wolny - I/O | ADC1 |
| 9 | wolny - I/O | ADC1 |
| 10 | free (SPI CS line) | ADC1 |
| 11 | SPI MOSI |  |
| 12 | SPI SCLK |  |
| 13 | SPI MISO |  |
| 14 | wolny - I/O |  |
| 15 | wolny - I/O |  |
| 16 | wolny - I/O |  |
| 17 | free (UART TX line) |  |
| 18 | free (UART RX line) |  |
| 21 | wolny - I/O |  |
| 38 | free (LED0 line) |  |
| 39 | wolny - I/O |  |
| 40 | wolny - I/O |  |
| 41 | wolny - I/O |  |
| 42 | wolny - I/O |  |
| 47 | I2C SCL |  |
| 48 | I2C SDA |  |

Złącza wyprowadzają wolne GPIO; ADC1 (wejścia analogowe, których używa
ctrl32) jest na GPIO1 do GPIO10. GPIO0 to przycisk Boot/User - w
programie wejście, a przytrzymany przy włączaniu uruchamia tryb
wgrywania układu. Złącze pUEXT wyprowadza I2C (GPIO48 / GPIO47) i SPI.

## Bezpieczeństwo

- Płytka nie jest przeznaczona do funkcji bezpieczeństwa. Wyłącznik
  awaryjny, wyłącznik drzwi lub kurtyna świetlna są podłączone sprzętowo,
  nigdy przez program.
- Piny GPIO pracują na 3,3 V. Sygnał 24 V wymaga transoptora lub
  konwertera poziomów; cewka przekaźnika wymaga sterownika (moduł
  przekaźnikowy go ma).

---

[← Przegląd](README.pl.md) | [Przegląd](README.pl.md) | [Instalacja runtime →](install.pl.md)
