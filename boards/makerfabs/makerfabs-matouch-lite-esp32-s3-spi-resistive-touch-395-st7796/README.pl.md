---
title: Makerfabs MaTouch Lite ESP32-S3 3.95"
slug: makerfabs-matouch-lite-esp32-s3-spi-resistive-touch-395-st7796
sidebar_position: 10
hardware: /hardware/boards/makerfabs-matouch-lite-esp32-s3-spi-resistive-touch-395-st7796/
image: img/board-01.jpg
image_alt: Płytka Makerfabs MaTouch Lite ESP32-S3 z wyświetlaczem dotykowym 3,95 cala
tags:
- esp32-s3
- display
- touch
- hmi
- wifi
- makerfabs
---

# Makerfabs MaTouch Lite ESP32-S3 3.95"

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32-S3](https://img.shields.io/badge/chip-ESP32--S3-334155) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a) ![CAN: 1](https://img.shields.io/badge/CAN-1-7c3aed) ![HMI: 320x480](https://img.shields.io/badge/HMI-320x480-0891b2)

![Płytka Makerfabs MaTouch Lite ESP32-S3 z wyświetlaczem dotykowym 3,95 cala](img/board-01.jpg)

Makerfabs MaTouch Lite to tani panel dotykowy: wyświetlacz 3,95" 320 x 480 z dotykiem rezystancyjnym na ESP32-S3 z PSRAM i Wi-Fi. Z ctrl32 jest HMI i PLC w jednym - ekrany narysowane w edytorze na szkle, obok nich program drabinkowy, te same wartości w każdej przeglądarce (WEBview), Modbus TCP, CAN i MQTT. Dotyk rezystancyjny działa także w rękawicach.

**Nadaje się do:**

- Mały panel operatorski przy maszynie, obsługiwany w rękawicach
- Termostat ścienny lub regulator pokojowy
- Wyświetlacz CAN dla pojazdu lub falownika

Strona płytki w katalogu: [Makerfabs MaTouch Lite ESP32-S3 3.95"](https://ctrl32.com/hardware/boards/makerfabs-matouch-lite-esp32-s3-spi-resistive-touch-395-st7796/)

![Makerfabs MaTouch Lite ESP32-S3 3.95" - mapa pinów: funkcja każdego GPIO w ctrl32](pinout/pinout.png)

## Co ctrl32 potrafi na tej płytce

<!-- capabilities:start -->
| Funkcja | Na tej płytce | Uwagi |
|---|---|---|
| Układ | ESP32-S3 (esp32s3_wroom_1_n16r8) |  |
| Pamięć | 16 MB flash, 8 MB PSRAM |  |
| Rozmiar programu | 512 zmiennych, 128 alarmów, 512 bloków | edytor sprawdza to przed wgraniem |
| Wejścia / wyjścia cyfrowe | 4 wolnych GPIO | zobacz mapę pinów |
| Wejścia analogowe | 4 w układzie (ADC1) | GPIO4, GPIO5, GPIO6, GPIO7 |
| Ethernet | nie |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 | wymaga zewnętrznego transceivera |
| Modbus RTU (RS-485) | tak | na wolnych pinach, wymaga zewnętrznego transceivera |
| Modbus TCP | klient i serwer |  |
| MQTT | tak (także TLS) | wykrywanie w Home Assistant |
| WEBview | tak | strona operatora w każdej przeglądarce |
| Wyświetlacz / dotyk (HMI) | 3.95" 320x480, NS2009 |  |
| USB | USB-C (CH340K USB-UART, Native USB) |  |
| Zasilanie | 5 V USB (4.0–5.25 V), 3.7 V Li-Po / Li-Ion |  |
<!-- capabilities:end -->

### Czego nie obsługujemy

- Bluetooth.
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
- [Makerfabs MaTouch ESP32-P4 7"](../makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/README.pl.md) - większe rodzeństwo

