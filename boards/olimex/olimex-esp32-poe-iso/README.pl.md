---
title: Olimex ESP32-PoE-ISO
slug: olimex-esp32-poe-iso
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-poe-iso/
image: img/board-01.jpg
image_alt: Płytka Olimex ESP32-PoE-ISO z gniazdem Ethernet i izolowanym zasilaniem PoE
tags:
- esp32
- ethernet
- poe
- isolated
- olimex
---

# Olimex ESP32-PoE-ISO

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32](https://img.shields.io/badge/chip-ESP32-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a)

![Płytka Olimex ESP32-PoE-ISO z gniazdem Ethernet i izolowanym zasilaniem PoE](img/board-01.jpg)

Olimex ESP32-PoE-ISO to ESP32-PoE z izolowanym galwanicznie zasilaniem przez Ethernet: jeden kabel sieciowy ją zasila i przenosi jej połączenie, a PC może pozostać podłączony przez USB, gdy płytka pracuje na PoE. Z ctrl32 jest kompaktowym PLC do szafy - program drabinkowy w układzie, strona operatora w każdej przeglądarce (WEBview), Modbus TCP do liczników i modułów I/O oraz MQTT do Home Assistant.

**Nadaje się do:**

- Mały PLC w szafie, zasilany ze switcha PoE
- Bramka Modbus TCP, która odczytuje liczniki i publikuje je przez MQTT
- Automatyka domowa - pokój lub kotłownia na jednym kablu

Strona płytki w katalogu: [Olimex ESP32-PoE-ISO](https://ctrl32.com/hardware/boards/olimex-esp32-poe-iso/)

![Olimex ESP32-PoE-ISO - mapa pinów: funkcja każdego GPIO w ctrl32](pinout/pinout.png)

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

-

## Dalsze kroki

- [Dokumentacja ctrl32](https://ctrl32.com/docs/) - edytor, języki, każdy blok
- [Pobierz edytor](https://ctrl32.com/download/)
- [Wszystkie przetestowane płytki](../../README.pl.md)
- [Olimex ESP32-PoE](../olimex-esp32-poe/README.pl.md) - ta sama płytka bez izolowanego zasilania
- Olimex ESP32-POE2 - następna generacja

