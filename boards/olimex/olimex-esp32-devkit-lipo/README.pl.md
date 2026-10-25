---
title: Olimex ESP32-DevKit-LiPo
slug: olimex-esp32-devkit-lipo
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-devkit-lipo/
image: img/board-01.jpg
image_alt: Płytka Olimex ESP32-DevKit-LiPo z dwoma złączami pinów i złączem micro-USB
tags:
- esp32
- wifi
- battery
- olimex
---

# Olimex ESP32-DevKit-LiPo

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32](https://img.shields.io/badge/chip-ESP32-334155) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a)

![Płytka Olimex ESP32-DevKit-LiPo z dwoma złączami pinów i złączem micro-USB](img/board-01.jpg)

Olimex ESP32-DevKit-LiPo to otwarta płytka rozwojowa z ESP32 z Wi-Fi, wszystkimi GPIO modułu na dwóch złączach i ładowarką Li-Po, która utrzymuje ją w działaniu przy zaniku zasilania. Z ctrl32 jest małym PLC z Wi-Fi: program drabinkowy w układzie, wejścia i wyjścia na pinach, strona operatora w każdej przeglądarce (WEBview), Modbus TCP i MQTT.

**Nadaje się do:**

- Sterownik Wi-Fi dla pokoju, szklarni lub pompy
- Rejestrator danych z podtrzymaniem bateryjnym, publikujący przez MQTT
- Nauka ctrl32 na płytce stykowej

Strona płytki w katalogu: [Olimex ESP32-DevKit-LiPo](https://ctrl32.com/hardware/boards/olimex-esp32-devkit-lipo/)

![Olimex ESP32-DevKit-LiPo - mapa pinów: funkcja każdego GPIO w ctrl32](pinout/pinout.png)

## Co ctrl32 potrafi na tej płytce

<!-- capabilities:start -->
| Funkcja | Na tej płytce | Uwagi |
|---|---|---|
| Układ | ESP32 (ESP32-WROOM-32E-N4) |  |
| Pamięć | 4 MB flash |  |
| Rozmiar programu | 128 zmiennych, 32 alarmów, 128 bloków | edytor sprawdza to przed wgraniem |
| Wejścia / wyjścia cyfrowe | 19 wolnych GPIO | 4 z nich tylko wejścia |
| Wejścia analogowe | 6 w układzie (ADC1) | GPIO32, GPIO33, GPIO34, GPIO35, GPIO36, GPIO39 |
| Ethernet | nie |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 - na wolnych pinach | wymaga zewnętrznego transceivera |
| Modbus RTU (RS-485) | tak - na wolnych pinach | wymaga zewnętrznego transceivera |
| Modbus TCP | klient i serwer |  |
| MQTT | tak | wykrywanie w Home Assistant |
| WEBview | tak | strona operatora w każdej przeglądarce |
| Wyświetlacz / dotyk (HMI) | nie | strona operatora to WEBview |
| USB | Micro-USB (CH340 USB-UART) |  |
| Zasilanie | 5 V USB, 3.7 V Li-Po / Li-Ion |  |
<!-- capabilities:end -->

### Czego nie obsługujemy

- Bluetooth - ESP32 go ma, ctrl32 go nie używa.
- Wejścia pomiaru akumulatora i zasilania (GPIO35 / GPIO39) są w ctrl32 wolnymi pinami, a nie wskaźnikiem akumulatora.

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
- Olimex ESP32-S3-DevKit-Lipo - ten sam pomysł z ESP32-S3 i PSRAM

