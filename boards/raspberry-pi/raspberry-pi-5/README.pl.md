---
title: Raspberry Pi 5
slug: raspberry-pi-5
sidebar_position: 10
hardware: /hardware/boards/raspberry-pi-5/
image: img/board-01.jpg
image_alt: Płytka Raspberry Pi 5, widok z góry
tags:
- raspberry-pi
- linux
- hmi
- opc-ua
- ethercat
---

# Raspberry Pi 5

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: Linux](https://img.shields.io/badge/chip-Linux-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a) ![CAN: 1](https://img.shields.io/badge/CAN-1-7c3aed)

![Płytka Raspberry Pi 5, widok z góry](img/board-01.jpg)

Raspberry Pi 5 uruchamia runtime ctrl32 dla Linuksa - największy cel ctrl32: dziesiątki tysięcy zmiennych, HMI na monitorze HDMI, serwer OPC UA dla systemu SCADA, napędy EtherCAT, CAN i RS-485 przez nakładki HAT lub adaptery USB oraz przetwarzanie obrazu z kamerą. Edytor instaluje runtime przez sieć; Pi uruchamia go potem przy każdym starcie.

**Nadaje się do:**

- Sterownik linii z HMI na monitorze HDMI i OPC UA do systemu SCADA
- Master EtherCAT dla serwonapędów
- Bramka między Modbus, CAN, OPC UA i MQTT

Strona płytki w katalogu: [Raspberry Pi 5](https://ctrl32.com/hardware/boards/raspberry-pi-5/)

![Raspberry Pi 5 - mapa pinów: funkcja każdego GPIO w ctrl32](pinout/pinout.png)

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
| USB | USB-C |  |
| Zasilanie | USB-C PD 5 V / 5 A |  |
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

| Plik | Co |
|---|---|
| [pinout/pinout.svg](pinout/pinout.svg) | mapa pinów, wektorowo (także [PNG](pinout/pinout.png)) |
| [raspberry-pi-5-mechanical-drawing.pdf](datasheets/raspberry-pi-5-mechanical-drawing.pdf) | Raspberry Pi 5 mechanical drawing |
| [raspberry-pi-5-rp1-peripherals.pdf](datasheets/raspberry-pi-5-rp1-peripherals.pdf) | RP1 peripherals |
| [raspberry-pi-5-3d.zip](3d/raspberry-pi-5-3d.zip) | Model 3D (GLB, spakowany) |
| [NOTICE](https://github.com/ctrl32/hardware/blob/main/NOTICE.md) | skąd pochodzą zdjęcia, schematy i modele |

## Dalsze kroki

- [Dokumentacja ctrl32](https://ctrl32.com/docs/) - edytor, języki, każdy blok
- [Pobierz edytor](https://ctrl32.com/download/)
- Wszystkie przetestowane płytki
- Raspberry Pi 4 Model B
- Raspberry Pi 3 Model B+
- [Runtime dla Linuksa](https://ctrl32.com/docs/linux-runtime/) - co robi i jakie ma limity

