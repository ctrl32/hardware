---
title: 'Olimex ESP32-DevKit-LiPo: sprzęt i okablowanie'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-DevKit-LiPo - mapa pinów
tags:
- esp32
- wifi
- battery
- olimex
---

# Sprzęt i okablowanie

## Czego potrzebujesz

- Olimex ESP32-DevKit-LiPo.
- Kabel micro-USB do transmisji danych - do wgrywania i do zasilania (5 V).
- Nazwa i hasło twojej sieci Wi-Fi 2,4 GHz.
- PC z [edytorem ctrl32](https://ctrl32.com/download/) (Windows).
- Opcjonalnie, dla przykładu all-in-one: przycisk z GPIO13 do GND; moduł przekaźnikowy lub dioda LED z rezystorem na GPIO4; potencjometr (10 k) między 3,3 V a GND ze ślizgaczem na GPIO32; transceiver CAN 3,3 V na GPIO14 / GPIO34 i transceiver RS-485 na GPIO16 / GPIO36 / GPIO17 (DE); ogniwo Li-Po jako podtrzymanie.

## Zasilanie

| Źródło | Gdzie | Uwaga |
|---|---|---|
| USB 5 V | złącze micro-USB | zasilanie i programowanie |
| Akumulator Li-Po | złącze akumulatora | ładowany na płytce, przejmuje zasilanie, gdy zawiedzie USB |

## Mapa pinów

![Olimex ESP32-DevKit-LiPo - mapa pinów](pinout/pinout.png)

| GPIO | Funkcja w ctrl32 | Uwaga |
|---|---|---|
| 4 | wolny - I/O |  |
| 6 | Flash SPI modułu | ⚠ zajęty przez płytkę |
| 7 | Flash SPI modułu | ⚠ zajęty przez płytkę |
| 8 | Flash SPI modułu | ⚠ zajęty przez płytkę |
| 9 | Flash SPI modułu | ⚠ zajęty przez płytkę |
| 10 | Flash SPI modułu | ⚠ zajęty przez płytkę |
| 11 | Flash SPI modułu | ⚠ zajęty przez płytkę |
| 13 | wolny - I/O |  |
| 14 | wolny - I/O |  |
| 16 | wolny - I/O |  |
| 17 | wolny - I/O |  |
| 18 | wolny - I/O |  |
| 19 | wolny - I/O |  |
| 21 | wolny - I/O |  |
| 22 | wolny - I/O |  |
| 23 | wolny - I/O |  |
| 25 | wolny - I/O |  |
| 26 | wolny - I/O |  |
| 27 | wolny - I/O |  |
| 32 | wolny - I/O | ADC1 |
| 33 | wolny - I/O | ADC1 |
| 34 | wolny - wejście | ⚠ tylko wejście, ADC1 |
| 35 | free (BAT SENSE line) | ⚠ tylko wejście, ADC1 |
| 36 | wolny - wejście | ⚠ tylko wejście, ADC1 |
| 39 | free (PWR SENSE line) | ⚠ tylko wejście, ADC1 |

Dwa złącza wyprowadzają wolne GPIO modułu. GPIO34 do GPIO39 to tylko
wejścia; GPIO0, 2, 12 i 15 to piny strapping - zostaw je na wejścia lub
przetestuj przed użyciem. Przycisk do GND nie wymaga rezystora: ctrl32
odczytuje go odwrócony z podciąganiem układu.

## Bezpieczeństwo

- Płytka nie jest przeznaczona do funkcji bezpieczeństwa. Wyłącznik
  awaryjny, wyłącznik drzwi lub kurtyna świetlna są podłączone sprzętowo,
  nigdy przez program.
- Piny GPIO pracują na 3,3 V. Sygnał 24 V wymaga transoptora lub
  konwertera poziomów; cewka przekaźnika wymaga sterownika (moduł
  przekaźnikowy go ma).

---

[← Przegląd](README.pl.md) | [Przegląd](README.pl.md) | [Instalacja runtime →](install.pl.md)
