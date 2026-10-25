---
title: Olimex ESP32-PoE
slug: olimex-esp32-poe
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-poe/
image: img/board-01.jpg
image_alt: Płytka Olimex ESP32-PoE, widok z góry, z gniazdem Ethernet i złączem USB
tags:
- esp32
- ethernet
- poe
- olimex
---

# Olimex ESP32-PoE

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32](https://img.shields.io/badge/chip-ESP32-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a)

![Płytka Olimex ESP32-PoE, widok z góry, z gniazdem Ethernet i złączem USB](img/board-01.jpg)

Olimex ESP32-PoE to otwarta płytka z ESP32 z Ethernetem i zasilaniem przez Ethernet (PoE): jeden kabel sieciowy ją zasila i przenosi jej połączenie. Z ctrl32 staje się kompaktowym PLC do szafy lub puszki ściennej - program drabinkowy w układzie, strona operatora udostępniana każdej przeglądarce w sieci (WEBview), Modbus TCP do liczników i modułów I/O oraz MQTT do Home Assistant lub dowolnego brokera.

**Nadaje się do:**

- Mały PLC w szafie, zasilany ze switcha PoE
- Bramka Modbus TCP, która odczytuje liczniki i publikuje je przez MQTT
- Automatyka domowa - pokój lub kotłownia na jednym kablu

Strona płytki w katalogu: [Olimex ESP32-PoE](https://ctrl32.com/hardware/boards/olimex-esp32-poe/)

![Olimex ESP32-PoE - mapa pinów: funkcja każdego GPIO w ctrl32](pinout/pinout.png)

## Co ctrl32 potrafi na tej płytce

<!-- capabilities:start -->
| Funkcja | Na tej płytce | Uwagi |
|---|---|---|
| Układ | ESP32 (ESP32-WROOM-32E-N4) |  |
| Pamięć | 4 MB flash |  |
| Rozmiar programu | 128 zmiennych, 32 alarmów, 128 bloków | edytor sprawdza to przed wgraniem |
| Wejścia / wyjścia cyfrowe | 6 wolnych GPIO | 3 z nich tylko wejścia |
| Wejścia analogowe | 4 w układzie (ADC1) | GPIO33, GPIO34, GPIO35, GPIO36 |
| Ethernet | tak - LAN8710A |  |
| Zasilanie przez Ethernet (PoE) | IEEE 802.3af |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 - na wolnych pinach | wymaga zewnętrznego transceivera |
| Modbus RTU (RS-485) | tak - na wolnych pinach | wymaga zewnętrznego transceivera |
| Modbus TCP | klient i serwer |  |
| MQTT | tak | wykrywanie w Home Assistant |
| WEBview | tak | strona operatora w każdej przeglądarce |
| Wyświetlacz / dotyk (HMI) | nie | strona operatora to WEBview |
| USB | Micro-USB (CH340T USB-UART) |  |
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

| Plik | Co |
|---|---|
| [pinout/pinout.svg](pinout/pinout.svg) | mapa pinów, wektorowo (także [PNG](pinout/pinout.png)) |
| [olimex-esp32-poe-schematic.pdf](schematics/olimex-esp32-poe-schematic.pdf) | ESP32-PoE schematic Rev M2 |
| [esp32-poe-revm2.zip](schematics/esp32-poe-revm2.zip) | KiCad project |
| [olimex-esp32-poe-user-manual.pdf](datasheets/olimex-esp32-poe-user-manual.pdf) | ESP32-PoE user manual |
| [olimex-esp32-poe.zip](3d/olimex-esp32-poe.zip) | Model 3D (STEP, spakowany) |
| [NOTICE](https://github.com/ctrl32/hardware/blob/main/NOTICE.md) | skąd pochodzą zdjęcia, schematy i modele |

## Dalsze kroki

- [Dokumentacja ctrl32](https://ctrl32.com/docs/) - edytor, języki, każdy blok
- [Pobierz edytor](https://ctrl32.com/download/)
- Wszystkie przetestowane płytki
- Olimex ESP32-PoE-ISO - ta sama płytka z izolowanym zasilaniem PoE
- Olimex ESP32-POE2 - następna generacja

