---
title: LaskaKit ESPlan
slug: laskakit-esplan
sidebar_position: 10
hardware: /hardware/boards/laskakit-esplan/
image: img/board-01.jpg
image_alt: Płytka LaskaKit ESPlan z gniazdem Ethernet, zaciskiem RS-485 i zaciskiem zasilania
tags:
- esp32
- ethernet
- rs485
- modbus
- laskakit
---

# LaskaKit ESPlan

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32](https://img.shields.io/badge/chip-ESP32-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a)

![Płytka LaskaKit ESPlan z gniazdem Ethernet, zaciskiem RS-485 i zaciskiem zasilania](img/board-01.jpg)

LaskaKit ESPlan to przemysłowa płytka z ESP32: Ethernet 10/100, interfejs RS-485 z zabezpieczeniem i przełączaną terminacją, Wi-Fi oraz szeroki zakres zasilania 7-40 V na zacisku śrubowym (lub PoE z dodatkowym modułem). Z ctrl32 jest masterem lub slave'em Modbus RTU w szafie - program drabinkowy w układzie, urządzenia RS-485 odczytywane i zapisywane, wartości w Modbus TCP, MQTT i na jej stronie operatora (WEBview).

**Nadaje się do:**

- Master Modbus RTU dla liczników, czujników i falowników, zasilany 24 V
- Bramka Modbus RTU / TCP z własną logiką
- Automatyka budynkowa w szafie

Strona płytki w katalogu: [LaskaKit ESPlan](https://ctrl32.com/hardware/boards/laskakit-esplan/)

![LaskaKit ESPlan - mapa pinów: funkcja każdego GPIO w ctrl32](pinout/pinout.png)

## Co ctrl32 potrafi na tej płytce

<!-- capabilities:start -->
| Funkcja | Na tej płytce | Uwagi |
|---|---|---|
| Układ | ESP32 (ESP32-WROOM-32E-N4) |  |
| Pamięć | 4 MB flash |  |
| Rozmiar programu | 128 zmiennych, 32 alarmów, 128 bloków | edytor sprawdza to przed wgraniem |
| Wejścia / wyjścia cyfrowe | 5 wolnych GPIO | 2 z nich tylko wejścia |
| Wejścia analogowe | 2 w układzie (ADC1) | GPIO35, GPIO39 |
| Ethernet | tak - LAN8720A |  |
| Zasilanie przez Ethernet (PoE) | IEEE 802.3af |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 - na wolnych pinach | wymaga zewnętrznego transceivera |
| Modbus RTU (RS-485) | tak |  |
| Modbus TCP | klient i serwer |  |
| MQTT | tak | wykrywanie w Home Assistant |
| WEBview | tak | strona operatora w każdej przeglądarce |
| Wyświetlacz / dotyk (HMI) | nie | strona operatora to WEBview |
| USB | USB-C (CH9102 USB-UART) |  |
| Zasilanie | 5 V USB, PoE |  |
<!-- capabilities:end -->

### Czego nie obsługujemy

- Bluetooth - ESP32 go ma, ctrl32 go nie używa.
- Gniazdo microSD - ctrl32 trzyma program i ekrany we własnej pamięci flash układu.

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

