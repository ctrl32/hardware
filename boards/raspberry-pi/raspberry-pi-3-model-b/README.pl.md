---
title: Raspberry Pi 3 Model B+
slug: raspberry-pi-3-model-b
sidebar_position: 10
hardware: /hardware/boards/raspberry-pi-3-model-b/
image: img/board-01.jpg
image_alt: Płytka Raspberry Pi 3 Model B+, widok z góry
tags:
- raspberry-pi
- linux
- hmi
- opc-ua
---

# Raspberry Pi 3 Model B+

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: Linux](https://img.shields.io/badge/chip-Linux-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a) ![CAN: 1](https://img.shields.io/badge/CAN-1-7c3aed)

![Płytka Raspberry Pi 3 Model B+, widok z góry](img/board-01.jpg)

Raspberry Pi 3 Model B+ uruchamia runtime ctrl32 dla Linuksa: duży program, HMI na monitorze HDMI, serwer OPC UA dla systemu SCADA, CAN i RS-485 przez nakładki HAT lub adaptery USB, Modbus i MQTT. Z 1 GB pamięci i czterordzeniowym Cortex-A53 nadaje się na sterownik linii lub bramkę; przetwarzanie obrazu z kamerą wymaga Raspberry Pi 4 lub 5.

**Nadaje się do:**

- Sterownik linii z HMI na monitorze HDMI i OPC UA do systemu SCADA
- Master EtherCAT dla serwonapędów
- Bramka między Modbus, CAN, OPC UA i MQTT

Strona płytki w katalogu: [Raspberry Pi 3 Model B+](https://ctrl32.com/hardware/boards/raspberry-pi-3-model-b/)

![Raspberry Pi 3 Model B+ - mapa pinów: funkcja każdego GPIO w ctrl32](pinout/pinout.png)

## Co ctrl32 potrafi na tej płytce

<!-- capabilities:start -->
| Funkcja | Na tej płytce | Uwagi |
|---|---|---|
| Układ | Linux |  |
| Rozmiar programu | 20480 zmiennych, 4096 alarmów, 40960 bloków | edytor sprawdza to przed wgraniem |
| Wejścia / wyjścia cyfrowe | przez moduły I/O | Modbus, CANopen, EtherCAT |
| Ethernet | tak |  |
| Wi-Fi | Wi-Fi 5 (2.4 + 5 GHz) |  |
| CAN | przez CAN HAT lub adapter USB | SocketCAN, do 4 magistral |
| Modbus RTU (RS-485) | tak | adapter USB lub HAT |
| Modbus TCP | klient i serwer |  |
| MQTT | tak (także TLS) | wykrywanie w Home Assistant |
| WEBview | tak | strona operatora w każdej przeglądarce |
| Serwer OPC UA | tak |  |
| EtherCAT master | tak | na drugim porcie Ethernet |
| Wyświetlacz (HMI) | HDMI lub panel DSI | lub bez wyświetlacza z WEBview |
| USB | Micro-USB |  |
| Zasilanie | 5 V USB |  |
<!-- capabilities:end -->

### Czego nie obsługujemy

- 40-pinowe złącze GPIO jako wejścia i wyjścia programu - wejścia i wyjścia idą przez moduły I/O (Modbus RTU / TCP, CANopen, EtherCAT); złącze przenosi magistrale nakładek HAT.
- Bluetooth.
- Środowisko graficzne - runtime sam rysuje ekran; system, którego oczekuje, to Raspberry Pi OS Lite.

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
- [Raspberry Pi 5](../raspberry-pi-5/README.pl.md)
- [Raspberry Pi 4 Model B](../raspberry-pi-4-model-b/README.pl.md)
- [Runtime dla Linuksa](https://ctrl32.com/docs/linux-runtime/) - co robi i jakie ma limity

