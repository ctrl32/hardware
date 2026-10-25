---
title: Olimex ESP32-POE2
slug: olimex-esp32-poe2
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-poe2/
image: img/board-01.jpg
image_alt: Płytka Olimex ESP32-POE2 z gniazdem Ethernet i wyjściami zasilania
tags:
- esp32
- ethernet
- poe
- psram
- olimex
---

# Olimex ESP32-POE2

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32](https://img.shields.io/badge/chip-ESP32-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a)

![Płytka Olimex ESP32-POE2 z gniazdem Ethernet i wyjściami zasilania](img/board-01.jpg)

Olimex ESP32-POE2 to następna generacja ESP32-PoE: ESP32 z 8 MB PSRAM, Ethernetem i zasilaniem przez Ethernet IEEE 802.3at, które zasila także twoje urządzenia polowe - wyjścia 24 V lub 12 V, 5 V i 3,3 V, do 25 W z kabla sieciowego. Z ctrl32 jest PLC w szafie zasilanym jednym kablem: logika drabinkowa, WEBview, Modbus TCP i MQTT, z pełnym rozmiarem programu klasycznego ESP32 z PSRAM.

**Nadaje się do:**

- PLC w szafie, który zasila z PoE swoje czujniki i mały moduł przekaźnikowy
- Bramka Modbus TCP z MQTT do Home Assistant
- Automatyka budynkowa na jednym kablu na pokój

Strona płytki w katalogu: [Olimex ESP32-POE2](https://ctrl32.com/hardware/boards/olimex-esp32-poe2/)

![Olimex ESP32-POE2 - mapa pinów: funkcja każdego GPIO w ctrl32](pinout/pinout.png)

## Co ctrl32 potrafi na tej płytce

<!-- capabilities:start -->
| Funkcja | Na tej płytce | Uwagi |
|---|---|---|
| Układ | ESP32 (ESP32-WROVER-E-N4R8) |  |
| Pamięć | 4 MB flash, 8 MB PSRAM |  |
| Rozmiar programu | 512 zmiennych, 128 alarmów, 1024 bloków | edytor sprawdza to przed wgraniem |
| Wejścia / wyjścia cyfrowe | 5 wolnych GPIO | 3 z nich tylko wejścia |
| Wejścia analogowe | 3 w układzie (ADC1) | GPIO34, GPIO36, GPIO39 |
| Ethernet | tak - LAN8710A |  |
| Zasilanie przez Ethernet (PoE) | IEEE 802.3at |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 - na wolnych pinach | wymaga zewnętrznego transceivera |
| Modbus RTU (RS-485) | tak - na wolnych pinach | wymaga zewnętrznego transceivera |
| Modbus TCP | klient i serwer |  |
| MQTT | tak | wykrywanie w Home Assistant |
| WEBview | tak | strona operatora w każdej przeglądarce |
| Wyświetlacz / dotyk (HMI) | nie | strona operatora to WEBview |
| USB | USB-C |  |
| Zasilanie | 5 V USB, 3.7 V Li-Po / Li-Ion, PoE |  |
<!-- capabilities:end -->

### Czego nie obsługujemy

- Bluetooth - ESP32 go ma, ctrl32 go nie używa.
- Gniazdo microSD - ctrl32 trzyma program i ekrany we własnej pamięci flash układu.
- Wejście akumulatora działa jako własna funkcja płytki; ctrl32 nie odczytuje poziomu naładowania.

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
- [Olimex ESP32-PoE](../olimex-esp32-poe/README.pl.md) - pierwsza generacja
- [Olimex ESP32-PoE-ISO](../olimex-esp32-poe-iso/README.pl.md) - z izolowanym zasilaniem PoE

