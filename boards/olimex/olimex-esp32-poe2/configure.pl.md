---
title: Konfiguracja Olimex ESP32-POE2 w edytorze ctrl32
slug: configure
sidebar_position: 40
image: img/configure-01-board.png
image_alt: Strona płytki Olimex ESP32-POE2 w edytorze
tags:
- esp32
- ethernet
- poe
- psram
- olimex
---

# Konfiguracja płytki

## Strona płytki

Kliknij dwukrotnie płytkę w drzewie urządzeń. Strona pokazuje, co płytka ma na pokładzie, i każdy pin: wolny pin dostaje zmienną jednym kliknięciem - wejście, wyjście albo, na pinie analogowym, wejście analogowe.

![Strona płytki: wolne piny i co każdy potrafi](img/configure-01-board.png)

## Sieć

Port Ethernet startuje sam. Domyślnie płytka pobiera adres z twojego
routera (DHCP) i ogłasza się w sieci swoją nazwą (`<projekt>.local`).
Stały adres ustawia się na stronie płytki, w jej sekcji **Network**.

**Wi-Fi.** ESP32 ma też Wi-Fi (otwórz **WiFi** w drzewie urządzeń). W
szafie kabel jest lepszą drogą: przenosi też zasilanie i nie trzeba
niczego ustawiać na płytce.

## Wejścia, wyjścia i zmienne

Każdy sygnał programu jest **zmienną**. Zmienna na pinie odczytuje lub steruje pinem; zmienna analogowa mówi, co jest do niej podłączone (napięcie, 4-20 mA, termistor), oraz jej zakres w jednostkach.

![Zmienne przykładu all-in-one](img/configure-03-variables.png)

## Komunikacja

**Modbus TCP.** Urządzenie w sieci dodaje się w **Ethernet → Modbus TCP master**; jego rejestry stają się zmiennymi.

**Modbus RTU / RS-485.** Płytka nie ma transceivera RS-485: podłącz moduł transceivera 3,3 V do wolnych pinów (TX, RX i pin kierunku DE) i wskaż je na stronie płytki (Bus pins) - ctrl32 jest wtedy masterem lub slave'em Modbus RTU na tej linii. Urządzenia Modbus TCP w sieci niczego nie wymagają.

**CAN.** ESP32 ma jeden kontroler CAN (TWAI). Płytka nie ma transceivera CAN: podłącz moduł transceivera 3,3 V do dwóch wolnych pinów i wskaż je na stronie płytki (Bus pins) - działają wtedy na nim urządzenia CANopen, surowe ramki CAN i magistrale pojazdowe (J1939).

**MQTT.** Płytka publikuje wybrane zmienne do brokera; w trybie Home Assistant broker sam je znajduje, a zmienną oznaczoną *write* można stamtąd ustawić.

![Strona MQTT: broker i publikowane zmienne](img/configure-05-mqtt.png)

## WEBview

Płytka udostępnia swoją stronę operatora każdej przeglądarce w sieci - otwórz adres płytki. Stronę rysuje się w edytorze jak ekran.

![Ustawienia strony WEBview](img/configure-06-webview.png)

---

[← Instalacja runtime](install.pl.md) | [Przegląd](README.pl.md) | [Przykładowe projekty →](examples/README.pl.md)
