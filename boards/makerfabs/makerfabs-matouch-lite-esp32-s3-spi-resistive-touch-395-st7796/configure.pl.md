---
title: Konfiguracja Makerfabs MaTouch Lite ESP32-S3 3.95" w edytorze ctrl32
slug: configure
sidebar_position: 40
image: img/configure-01-board.png
image_alt: Strona płytki Makerfabs MaTouch Lite ESP32-S3 3.95" w edytorze
tags:
- esp32-s3
- display
- touch
- hmi
- wifi
- makerfabs
---

# Konfiguracja płytki

## Strona płytki

Kliknij dwukrotnie płytkę w drzewie urządzeń. Strona pokazuje, co płytka ma na pokładzie, i każdy pin: wolny pin dostaje zmienną jednym kliknięciem - wejście, wyjście albo, na pinie analogowym, wejście analogowe.

![Strona płytki: wolne piny i co każdy potrafi](img/configure-01-board.png)

## Sieć

Płytka łączy się z twoją siecią Wi-Fi: otwórz stronę **WiFi** w drzewie
urządzeń i wpisz nazwę i hasło sieci (przykład zawiera wartości
zastępcze). Stały adres ustawia się na stronie płytki, w jej sekcji
**Network**.


## Wejścia, wyjścia i zmienne

Każdy sygnał programu jest **zmienną**. Zmienna na pinie odczytuje lub steruje pinem; zmienna analogowa mówi, co jest do niej podłączone (napięcie, 4-20 mA, termistor), oraz jej zakres w jednostkach.

![Zmienne przykładu all-in-one](img/configure-03-variables.png)

## Komunikacja

**Modbus TCP.** Urządzenie w sieci dodaje się w **Ethernet → Modbus TCP master**; jego rejestry stają się zmiennymi.

**Modbus RTU / RS-485.** Płytka nie ma transceivera RS-485, a obok I/O przykładu ma na niego za mało wolnych pinów; urządzenia Modbus są osiągane przez Modbus TCP w sieci Wi-Fi.

**CAN.** ESP32-S3 ma jeden kontroler CAN (TWAI). Płytka nie ma transceivera: podłącz moduł transceivera 3,3 V do dwóch wolnych pinów i wskaż je na stronie płytki (**Bus pins**); przykład używa GPIO6 / GPIO7.

**MQTT.** Płytka publikuje wybrane zmienne do brokera; w trybie Home Assistant broker sam je znajduje, a zmienną oznaczoną *write* można stamtąd ustawić.

![Strona MQTT: broker i publikowane zmienne](img/configure-05-mqtt.png)

## Wyświetlacz i dotyk

Szkło ma 320 x 480, pionowo tak, jak zamontowano; strona HMIview obraca
obraz (dotyk podąża za nim) i ustawia ekran startowy. Dotyk rezystancyjny
wymaga mocnego nacisku - rysuj przyciski o wysokości co najmniej 40 px.

![Ustawienia HMIview: ekran, na którym rysuje projekt](img/configure-04-display.png)

## WEBview

Płytka udostępnia swoją stronę operatora każdej przeglądarce w sieci - otwórz adres płytki. Stronę rysuje się w edytorze jak ekran.

![Ustawienia strony WEBview](img/configure-06-webview.png)

---

[← Instalacja runtime](install.pl.md) | [Przegląd](README.pl.md) | [Przykładowe projekty →](examples/README.pl.md)
