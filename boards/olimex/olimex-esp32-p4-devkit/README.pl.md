---
title: Olimex ESP32-P4-DevKit
slug: olimex-esp32-p4-devkit
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-p4-devkit/
image: img/board-01.jpg
image_alt: Płytka Olimex ESP32-P4-DevKit z gniazdem Ethernet i złączami pinów
tags:
- esp32-p4
- ethernet
- olimex
---

# Olimex ESP32-P4-DevKit

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32-P4](https://img.shields.io/badge/chip-ESP32--P4-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a)

![Płytka Olimex ESP32-P4-DevKit z gniazdem Ethernet i złączami pinów](img/board-01.jpg)

Olimex ESP32-P4-DevKit to mała otwarta płytka z ESP32-P4 - najszybszym ESP32, dwa rdzenie 400 MHz i 32 MB PSRAM - oraz Ethernetem 100 Mb. Nie ma Wi-Fi: to sterownik przewodowy. Z ctrl32 uruchamia największe programy, jakie potrafi ESP32 - 4096 zmiennych - ze stroną operatora w każdej przeglądarce (WEBview), Modbus TCP i MQTT z TLS.

**Nadaje się do:**

- Przewodowy PLC z dużym programem i wieloma urządzeniami Modbus
- Bramka z rozbudowaną logiką między Modbus TCP a MQTT
- Rozwój własnej płytki z P4

Strona płytki w katalogu: [Olimex ESP32-P4-DevKit](https://ctrl32.com/hardware/boards/olimex-esp32-p4-devkit/)

![Olimex ESP32-P4-DevKit - mapa pinów: funkcja każdego GPIO w ctrl32](pinout/pinout.png)

## Co ctrl32 potrafi na tej płytce

<!-- capabilities:start -->
| Funkcja | Na tej płytce | Uwagi |
|---|---|---|
| Układ | ESP32-P4 (ESP32-P4NRW32) |  |
| Pamięć | 16 MB flash, 32 MB PSRAM |  |
| Rozmiar programu | 4096 zmiennych, 512 alarmów, 1024 bloków | edytor sprawdza to przed wgraniem |
| Wejścia / wyjścia cyfrowe | 11 wolnych GPIO | zobacz mapę pinów |
| Wejścia analogowe | przez przetwornik I2C (ADS1115) |  |
| Ethernet | tak - IP101GRI |  |
| Wi-Fi | nie |  |
| CAN (TWAI) | 1 - na wolnych pinach | wymaga zewnętrznego transceivera |
| Modbus RTU (RS-485) | tak - na wolnych pinach | wymaga zewnętrznego transceivera |
| Modbus TCP | klient i serwer |  |
| MQTT | tak (także TLS) | wykrywanie w Home Assistant |
| WEBview | tak | strona operatora w każdej przeglądarce |
| Wyświetlacz / dotyk (HMI) | nie | strona operatora to WEBview |
| USB | USB-C (Native USB) |  |
| Zasilanie | 5 V USB, PoE |  |
<!-- capabilities:end -->

### Czego nie obsługujemy

- Złącza wyświetlacza MIPI DSI i kamery CSI - ta płytka działa w ctrl32 bez wyświetlacza (strona operatora to WEBview).
- Gniazdo microSD - ctrl32 trzyma program i ekrany w pamięci flash płytki.

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
- [Makerfabs MaTouch ESP32-P4 7"](../../makerfabs/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/README.pl.md) - ESP32-P4 z ekranem dotykowym 7"

