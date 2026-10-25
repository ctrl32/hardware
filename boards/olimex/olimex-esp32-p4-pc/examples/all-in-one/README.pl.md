---
title: 'Olimex ESP32-P4-PC: przykład All-in-one'
slug: all-in-one
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-p4-pc/
image: img/screen.png
image_alt: Strona operatora przykładu all-in-one dla Olimex ESP32-P4-PC
tags:
- esp32-p4
- ethernet
- ups
- olimex
- example
---

# All-in-one

Wyjście silnika ze start / stop, czasem pracy, temperaturą Modbus RTU, ramkami CAN, licznikiem Modbus TCP, MQTT i stroną operatora w przeglądarce.

**Pobieranie:** [all-in-one.prj32](all-in-one.prj32) - otwórz go w edytorze ctrl32 (**File → Open**).

## Co robi

Program to mały sterownik maszyny - kształt większości maszyn:

- **Start** pochodzi od przycisku na GPIO14, od **Start** na stronie operatora lub z Home Assistant przez MQTT.
- **Stop** pochodzi od **Stop**, od niskiego poziomu lub od upływu czasu pracy - podtrzymanie wyłącza wyjście na **GPIO2**.
- **Czas pracy** ustawia się w minutach i jest zachowywany po zaniku zasilania.
- **Poziom** to zmienna ustawiana na stronie (płytce nie został wolny pin analogowy).
- Czujnik **Modbus RTU** na RS-485 płytki podaje temperaturę (unit 1, rejestr wejściowy 1).
- **CAN** co 100 ms wysyła poziom i stan wyjścia w ramce 0x181 i odbiera wartość zadaną w ramce 0x201.
- Licznik energii **Modbus TCP** w sieci podaje pobór mocy (192.168.1.60 - zmień na adres swojego licznika).
- **MQTT** publikuje wartości do brokera Home Assistant, który sam je znajduje; wyjście można też uruchomić z Home Assistant.
- **WEBview** udostępnia stronę operatora każdej przeglądarce w sieci.

## Program

![Program drabinkowy przykładu](img/ladder.png)

## Strona operatora

![Strona operatora w symulacji](img/screen.png)

## Otwórz i uruchom

1. Otwórz `all-in-one.prj32` w edytorze.
2. Zmień adresy (urządzenia Modbus, brokera MQTT) na adresy swojej sieci.
3. Uruchom **symulację** (pasek narzędzi), aby wypróbować projekt na PC, albo wgraj go na płytkę - zobacz [Instalacja runtime](../../install.pl.md).

## Co powinieneś zobaczyć

Naciśnij przycisk na GPIO14: wyjście na GPIO2 włącza się, a jego dioda na stronie świeci. Po upływie czasu pracy wyłącza się samo. W Home Assistant płytka pojawia się ze swoimi wartościami.


---

[← Przykładowe projekty](../README.pl.md) | [Przegląd](../../README.pl.md)
