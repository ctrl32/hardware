---
title: Konfiguracja Olimex ESP32-EVB w edytorze ctrl32
slug: configure
sidebar_position: 40
image: img/configure-01-board.png
image_alt: Strona płytki Olimex ESP32-EVB w edytorze
tags:
- esp32
- ethernet
- can
- relay
- olimex
---

# Konfiguracja płytki

## Strona płytki

Kliknij dwukrotnie płytkę w drzewie urządzeń. Strona pokazuje, co płytka ma na pokładzie, i każdy pin: wolny pin dostaje zmienną jednym kliknięciem - wejście, wyjście albo, na pinie analogowym, wejście analogowe.

![Strona płytki: wolne piny i co każdy potrafi](img/configure-01-board.png)

## Sieć

Port Ethernet startuje sam i pobiera adres z twojego routera (DHCP).
Stały adres ustawia się na stronie płytki, w jej sekcji **Network**;
Wi-Fi na stronie **WiFi** w drzewie urządzeń.


## Wejścia, wyjścia i zmienne

Każdy sygnał programu jest **zmienną**. Zmienna na pinie odczytuje lub steruje pinem; zmienna analogowa mówi, co jest do niej podłączone (napięcie, 4-20 mA, termistor), oraz jej zakres w jednostkach.

![Zmienne przykładu all-in-one](img/configure-03-variables.png)

## Komunikacja

**Modbus TCP.** Urządzenie w sieci dodaje się w **Ethernet → Modbus TCP master**; jego rejestry stają się zmiennymi.

**Modbus RTU / RS-485.** Płytka nie ma transceivera RS-485: podłącz moduł transceivera 3,3 V do wolnych pinów (TX, RX i pin kierunku DE) i wskaż je na stronie płytki (Bus pins) - ctrl32 jest wtedy masterem lub slave'em Modbus RTU na tej linii. Urządzenia Modbus TCP w sieci niczego nie wymagają.

**CAN.** ESP32 ma jeden kontroler CAN (TWAI), a ta płytka ma jego transceiver: CAN_H / CAN_L na zacisku, GPIO5 / GPIO35. Działają na nim urządzenia CANopen (napęd, węzły I/O), surowe ramki CAN i magistrale pojazdowe (J1939).

**MQTT.** Płytka publikuje wybrane zmienne do brokera; w trybie Home Assistant broker sam je znajduje, a zmienną oznaczoną *write* można stamtąd ustawić.

![Strona MQTT: broker i publikowane zmienne](img/configure-05-mqtt.png)

## Wyświetlacz i dotyk

Z MOD-LCD2.8RTP na złączu UEXT projekt może mieć ekrany (240 x 320,
pionowo lub obrócone). Płytka nie ma PSRAM: przy włączonym wyświetlaczu
runtime rezerwuje pamięć dla ekranu i prowadzi sieć tylko przez Ethernet
(bez Wi-Fi, bez MQTT). Dlatego przykład all-in-one nie ma ekranu; WEBview
działa w obu przypadkach.

![Ustawienia HMIview: ekran, na którym rysuje projekt](img/configure-04-display.png)

## WEBview

Płytka udostępnia swoją stronę operatora każdej przeglądarce w sieci - otwórz adres płytki. Stronę rysuje się w edytorze jak ekran.

![Ustawienia strony WEBview](img/configure-06-webview.png)

---

[← Instalacja runtime](install.pl.md) | [Przegląd](README.pl.md) | [Przykładowe projekty →](examples/README.pl.md)
