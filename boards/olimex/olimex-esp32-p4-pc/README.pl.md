---
title: Olimex ESP32-P4-PC
slug: olimex-esp32-p4-pc
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-p4-pc/
image: img/board-01.jpg
image_alt: Płytka Olimex ESP32-P4-PC z gniazdem Ethernet, portami USB i złączem HDMI
tags:
- esp32-p4
- ethernet
- ups
- olimex
---

# Olimex ESP32-P4-PC

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32-P4](https://img.shields.io/badge/chip-ESP32--P4-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a)

![Płytka Olimex ESP32-P4-PC z gniazdem Ethernet, portami USB i złączem HDMI](img/board-01.jpg)

Olimex ESP32-P4-PC to mały komputer na ESP32-P4 - dwa rdzenie 400 MHz i 32 MB PSRAM - z Ethernetem 100 Mb, czterema portami USB host, HDMI, audio i akumulatorem Li-Po, który utrzymuje go w działaniu przy zaniku zasilania. Z ctrl32 jest przewodowym sterownikiem z największym programem, jaki uruchamia ESP32 - 4096 zmiennych - ze stroną operatora w każdej przeglądarce (WEBview), Modbus TCP, MQTT z TLS oraz CAN lub RS-485 na wolnych pinach złącza.

**Nadaje się do:**

- Przewodowy PLC, który przetrwa zanik zasilania na własnym akumulatorze
- Bramka z rozbudowaną logiką między Modbus TCP, CAN i MQTT
- Sterownik w obudowie, zasilany przez PoE (z rozszerzeniem)

Strona płytki w katalogu: [Olimex ESP32-P4-PC](https://ctrl32.com/hardware/boards/olimex-esp32-p4-pc/)

![Olimex ESP32-P4-PC - mapa pinów: funkcja każdego GPIO w ctrl32](pinout/pinout.png)

## Co ctrl32 potrafi na tej płytce

<!-- capabilities:start -->
| Funkcja | Na tej płytce | Uwagi |
|---|---|---|
| Układ | ESP32-P4 (ESP32-P4NRW32) |  |
| Pamięć | 16 MB flash, 32 MB PSRAM |  |
| Rozmiar programu | 4096 zmiennych, 512 alarmów, 1024 bloków | edytor sprawdza to przed wgraniem |
| Wejścia / wyjścia cyfrowe | 15 wolnych GPIO | zobacz mapę pinów |
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
| Zasilanie | 5 V USB, 3.7 V Li-Po / Li-Ion, PoE |  |
<!-- capabilities:end -->

### Czego nie obsługujemy

- Wyjście HDMI i złącza MIPI DSI / CSI - ta płytka działa w ctrl32 bez wyświetlacza (strona operatora to WEBview).
- Porty USB host i wyjście audio.
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

| Plik | Co |
|---|---|
| [pinout/pinout.svg](pinout/pinout.svg) | mapa pinów, wektorowo (także [PNG](pinout/pinout.png)) |
| [olimex-esp32-p4-pc-schematic.pdf](schematics/olimex-esp32-p4-pc-schematic.pdf) | ESP32-P4-PC schematic Rev C |
| [esp32-p4-pc-rev-c-kicad.zip](schematics/esp32-p4-pc-rev-c-kicad.zip) | KiCad project |
| [olimex-esp32-p4-pc-user-manual.pdf](datasheets/olimex-esp32-p4-pc-user-manual.pdf) | ESP32-P4-PC user manual |
| [NOTICE](https://github.com/ctrl32/hardware/blob/main/NOTICE.md) | skąd pochodzą zdjęcia, schematy i modele |

## Dalsze kroki

- [Dokumentacja ctrl32](https://ctrl32.com/docs/) - edytor, języki, każdy blok
- [Pobierz edytor](https://ctrl32.com/download/)
- [Wszystkie przetestowane płytki](../../README.pl.md)
- [Olimex ESP32-P4-DevKit](../olimex-esp32-p4-devkit/README.pl.md) - ten sam ESP32-P4 na mniejszej płytce

