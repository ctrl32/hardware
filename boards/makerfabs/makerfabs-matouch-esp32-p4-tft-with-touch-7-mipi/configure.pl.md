---
title: Konfiguracja Makerfabs MaTouch ESP32-P4 7" w edytorze ctrl32
slug: configure
sidebar_position: 40
image: img/configure-01-board.png
image_alt: Strona płytki Makerfabs MaTouch ESP32-P4 7" w edytorze
tags:
- esp32-p4
- display
- touch
- hmi
- ethernet
- makerfabs
---

# Konfiguracja płytki

## Strona płytki

Kliknij dwukrotnie płytkę w drzewie urządzeń. Strona pokazuje, co płytka ma na pokładzie, i każdy pin: wolny pin dostaje zmienną jednym kliknięciem - wejście, wyjście albo, na pinie analogowym, wejście analogowe.

![Strona płytki: wolne piny i co każdy potrafi](img/configure-01-board.png)

## Sieć

Port Ethernet startuje sam i pobiera adres z twojego routera (DHCP).
Wi-Fi układu ESP32-C6 ustawia się na stronie **WiFi** w drzewie urządzeń -
nazwę sieci i hasło. Stały adres ustawia się na stronie płytki, w jej
sekcji **Network**.


## Wejścia, wyjścia i zmienne

Każdy sygnał programu jest **zmienną**. Zmienna na pinie odczytuje lub steruje pinem; zmienna analogowa mówi, co jest do niej podłączone (napięcie, 4-20 mA, termistor), oraz jej zakres w jednostkach.

![Zmienne przykładu all-in-one](img/configure-03-variables.png)

## Komunikacja

**Modbus TCP.** Urządzenie w sieci dodaje się w **Ethernet → Modbus TCP master**; jego rejestry stają się zmiennymi.

**Modbus RTU / RS-485.** Płytka nie ma transceivera RS-485: podłącz moduł transceivera 3,3 V do wolnych pinów (TX, RX i pin kierunku DE) i wskaż je na stronie płytki - przykład używa GPIO4 / GPIO5 / GPIO32. ctrl32 jest wtedy masterem lub slave'em Modbus RTU na tej linii.

**CAN.** ESP32-P4 ma jeden kontroler CAN (TWAI). Płytka nie ma transceivera CAN: podłącz moduł transceivera 3,3 V do dwóch wolnych pinów i wskaż je na stronie płytki (**Bus pins**) - przykład używa GPIO20 / GPIO21. Działają na nim urządzenia CANopen, surowe ramki CAN i magistrale pojazdowe (J1939).

**MQTT.** Płytka publikuje wybrane zmienne do brokera; w trybie Home Assistant broker sam je znajduje, a zmienną oznaczoną *write* można stamtąd ustawić.

![Strona MQTT: broker i publikowane zmienne](img/configure-05-mqtt.png)

## Wyświetlacz i dotyk

Projekt jest rysowany we własnej rozdzielczości szkła 1024 x 600. Strona
HMIview ustawia orientację (jak zamontowano lub obróconą - dotyk podąża
za nią), rozmiar płótna WEBview i ekran startowy. Dotyk nie wymaga
konfiguracji: kontroler GT911 jest częścią płytki.

![Ustawienia HMIview: ekran, na którym rysuje projekt](img/configure-04-display.png)

## WEBview

Płytka udostępnia swoją stronę operatora każdej przeglądarce w sieci - otwórz adres płytki. Stronę rysuje się w edytorze jak ekran.

![Ustawienia strony WEBview](img/configure-06-webview.png)

---

[← Instalacja runtime](install.pl.md) | [Przegląd](README.pl.md) | [Przykładowe projekty →](examples/README.pl.md)
