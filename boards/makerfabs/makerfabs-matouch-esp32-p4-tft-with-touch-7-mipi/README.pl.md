---
title: Makerfabs MaTouch ESP32-P4 7"
slug: makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi
sidebar_position: 10
hardware: /hardware/boards/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/
image: img/board-01.jpg
image_alt: Płytka Makerfabs MaTouch ESP32-P4 7" z wyświetlaczem dotykowym 1024x600
tags:
- esp32-p4
- display
- touch
- hmi
- ethernet
- makerfabs
---

# Makerfabs MaTouch ESP32-P4 7"

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32-P4](https://img.shields.io/badge/chip-ESP32--P4-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a) ![CAN: 1](https://img.shields.io/badge/CAN-1-7c3aed) ![HMI: 1024x600](https://img.shields.io/badge/HMI-1024x600-0891b2)

![Płytka Makerfabs MaTouch ESP32-P4 7" z wyświetlaczem dotykowym 1024x600](img/board-01.jpg)

Makerfabs MaTouch ESP32-P4 7" to kompletny panel dotykowy na jednej płytce: wyświetlacz MIPI 1024 x 600 z dotykiem pojemnościowym, dwurdzeniowy ESP32-P4 z 32 MB PSRAM, Ethernet i Wi-Fi 6 przez ESP32-C6. Z ctrl32 jest HMI i PLC w jednym - ekrany narysowane w edytorze działają na szkle, obok nich działa program drabinkowy, a te same wartości trafiają do każdej przeglądarki (WEBview), urządzeń Modbus, CAN i MQTT.

**Nadaje się do:**

- Panel operatorski przy maszynie, z własną logiką
- Ścienny panel inteligentnego domu lub sterowania budynkiem
- Bramka Modbus / CAN z ekranem

Strona płytki w katalogu: [Makerfabs MaTouch ESP32-P4 7"](https://ctrl32.com/hardware/boards/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/)

![Makerfabs MaTouch ESP32-P4 7" - mapa pinów: funkcja każdego GPIO w ctrl32](pinout/pinout.png)

## Co ctrl32 potrafi na tej płytce

<!-- capabilities:start -->
| Funkcja | Na tej płytce | Uwagi |
|---|---|---|
| Układ | ESP32-P4 (ESP32-P4NRW32) |  |
| Pamięć | 16 MB flash, 32 MB PSRAM |  |
| Rozmiar programu | 4096 zmiennych, 512 alarmów, 512 bloków | edytor sprawdza to przed wgraniem |
| Wejścia / wyjścia cyfrowe | 12 wolnych GPIO | zobacz mapę pinów |
| Wejścia analogowe | przez przetwornik I2C (ADS1115) |  |
| Ethernet | tak - IP101GRI |  |
| Wi-Fi | Wi-Fi 6 (2.4 GHz) |  |
| CAN (TWAI) | 1 | wymaga zewnętrznego transceivera |
| Modbus RTU (RS-485) | tak | na wolnych pinach, wymaga zewnętrznego transceivera |
| Modbus TCP | klient i serwer |  |
| MQTT | tak (także TLS) | wykrywanie w Home Assistant |
| WEBview | tak | strona operatora w każdej przeglądarce |
| Wyświetlacz / dotyk (HMI) | 7" 1024x600, GT911 |  |
| USB | USB-C (CH340K USB-UART, Native USB) |  |
| Zasilanie | 5 V USB (4.0–5.25 V), 3.7 V Li-Po / Li-Ion |  |
<!-- capabilities:end -->

### Czego nie obsługujemy

- Kamera (SC2336 na MIPI CSI) - ctrl32 uruchamia przetwarzanie obrazu tylko w 64-bitowym runtime dla Linuksa.
- Kodek audio, mikrofon i wyjście głośnikowe.
- Bluetooth układu ESP32-C6.
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
| [makerfabs-matouch_esp32-p4_tft_with_touch_7_v1.2.pdf](schematics/makerfabs-matouch_esp32-p4_tft_with_touch_7_v1.2.pdf) | MaTouch ESP32-P4 TFT with Touch 7“ V1.2 |
| [makerfabs-matouch-p4-7-display-datasheet.pdf](datasheets/makerfabs-matouch-p4-7-display-datasheet.pdf) | 7" 1024x600 MIPI display AML070JGI50 datasheet |
| [makerfabs-matouch-p4-es8311-datasheet.pdf](datasheets/makerfabs-matouch-p4-es8311-datasheet.pdf) | ES8311 audio codec datasheet |
| [esp32-p4-datasheet.pdf](datasheets/esp32-p4-datasheet.pdf) | ESP32-P4 datasheet (pre-release) |
| [makerfabs-matouch-p4-sc2336-camera-datasheet.pdf](datasheets/makerfabs-matouch-p4-sc2336-camera-datasheet.pdf) | SC2336 2 MP MIPI camera module datasheet |
| [NOTICE](https://github.com/ctrl32/hardware/blob/main/NOTICE.md) | skąd pochodzą zdjęcia, schematy i modele |

## Dalsze kroki

- [Dokumentacja ctrl32](https://ctrl32.com/docs/) - edytor, języki, każdy blok
- [Pobierz edytor](https://ctrl32.com/download/)
- Wszystkie przetestowane płytki
- Makerfabs MaTouch Lite ESP32-S3 3.95" - mniejsze rodzeństwo
- [Panel sterowania inteligentnym domem na MaTouch ESP32-P4](https://ctrl32.com/examples/smart-home-control-panel-on-an-esp32-p4-7-touch-display/) - pełny przykład w sieci

