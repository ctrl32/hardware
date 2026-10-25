---
title: Olimex ESP32-S3-DevKit-Lipo
slug: olimex-esp32-s3-devkit-lipo
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-s3-devkit-lipo/
image: img/board-01.jpg
image_alt: Płytka Olimex ESP32-S3-DevKit-Lipo z dwoma złączami USB-C i złączami pinów
tags:
- esp32-s3
- wifi
- psram
- battery
- olimex
---

# Olimex ESP32-S3-DevKit-Lipo

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32-S3](https://img.shields.io/badge/chip-ESP32--S3-334155) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a)

![Płytka Olimex ESP32-S3-DevKit-Lipo z dwoma złączami USB-C i złączami pinów](img/board-01.jpg)

Olimex ESP32-S3-DevKit-Lipo to otwarta płytka z ESP32-S3 z 8 MB flash, 8 MB PSRAM, Wi-Fi, dwoma portami USB-C i ładowarką Li-Po. S3 z PSRAM to układ referencyjny ctrl32: program drabinkowy z pełnym rozmiarem programu, strona operatora w każdej przeglądarce (WEBview), Modbus TCP i MQTT z TLS - wszystko przez Wi-Fi.

**Nadaje się do:**

- PLC z Wi-Fi z zapasem na rozwój - 512 zmiennych, TLS do brokera w chmurze
- Sterownik z podtrzymaniem bateryjnym, który działa dalej przy zaniku zasilania
- Rozwój własnej płytki z ESP32-S3

Strona płytki w katalogu: [Olimex ESP32-S3-DevKit-Lipo](https://ctrl32.com/hardware/boards/olimex-esp32-s3-devkit-lipo/)

![Olimex ESP32-S3-DevKit-Lipo - mapa pinów: funkcja każdego GPIO w ctrl32](pinout/pinout.png)

## Co ctrl32 potrafi na tej płytce

<!-- capabilities:start -->
| Funkcja | Na tej płytce | Uwagi |
|---|---|---|
| Układ | ESP32-S3 (ESP32-S3-WROOM-1-N8R8) |  |
| Pamięć | 8 MB flash, 8 MB PSRAM |  |
| Rozmiar programu | 512 zmiennych, 128 alarmów, 1024 bloków | edytor sprawdza to przed wgraniem |
| Wejścia / wyjścia cyfrowe | 21 wolnych GPIO | zobacz mapę pinów |
| Wejścia analogowe | 9 w układzie (ADC1) | GPIO1, GPIO2, GPIO4, GPIO5, GPIO6, GPIO7, GPIO8, GPIO9, GPIO10 |
| Ethernet | nie |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 - na wolnych pinach | wymaga zewnętrznego transceivera |
| Modbus RTU (RS-485) | tak - na wolnych pinach | wymaga zewnętrznego transceivera |
| Modbus TCP | klient i serwer |  |
| MQTT | tak (także TLS) | wykrywanie w Home Assistant |
| WEBview | tak | strona operatora w każdej przeglądarce |
| Wyświetlacz / dotyk (HMI) | nie | strona operatora to WEBview |
| USB | USB-C (CH340X USB-UART, Native USB) |  |
| Zasilanie | 5 V USB, 3.7 V Li-Po / Li-Ion |  |
<!-- capabilities:end -->

### Czego nie obsługujemy

- Bluetooth - ESP32-S3 go ma, ctrl32 go nie używa.
- Wejścia pomiaru akumulatora i zasilania (GPIO5 / GPIO6) są w ctrl32 wolnymi pinami, a nie wskaźnikiem akumulatora.

## Poradnik

| Krok | Strona |
|---|---|
| 1 | [Sprzęt i okablowanie](hardware.pl.md) - czego potrzebujesz, zasilanie, mapa pinów |
| 2 | [Instalacja runtime](install.pl.md) - edytor, płytka, pierwsze wgranie |
| 3 | [Konfiguracja](configure.pl.md) - sieć, I/O, komunikacja |
| 4 | [Przykładowe projekty](examples/README.pl.md) - wszystko, co płytka potrafi, gotowe do otwarcia |
| - | [Rozwiązywanie problemów](troubleshooting.pl.md) |

## Pliki

-

## Dalsze kroki

- [Dokumentacja ctrl32](https://ctrl32.com/docs/) - edytor, języki, każdy blok
- [Pobierz edytor](https://ctrl32.com/download/)
- [Wszystkie przetestowane płytki](../../README.pl.md)
- [Olimex ESP32-DevKit-LiPo](../olimex-esp32-devkit-lipo/README.pl.md) - wersja z klasycznym ESP32

