---
title: 'Olimex ESP32-PoE: przykład All-in-one'
slug: all-in-one
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-poe/
image: img/screen.png
image_alt: Strona operatora przykładu all-in-one dla Olimex ESP32-PoE
tags:
- esp32
- ethernet
- poe
- olimex
- example
---

# All-in-one

Pompa sterowana przyciskiem płytki, stroną operatora i Home Assistant, z wejściem poziomu, czasem pracy, alarmem poziomu i licznikiem energii Modbus TCP.

**Pobieranie:** [all-in-one.prj32](all-in-one.prj32) - otwórz go w edytorze ctrl32 (**File → Open**).

## Co robi

Program to mały sterownik pompy - kształt większości maszyn:

- **Start** pochodzi od przycisku płytki (BUT1), od przycisku
  **Start** na stronie operatora lub z Home Assistant przez MQTT.
- **Stop** pochodzi od przycisku **Stop**, od niskiego poziomu lub od
  upływu czasu pracy - podtrzymanie wyłącza wyjście na GPIO33.
- **Poziom** to wejście analogowe na GPIO35 (0 do 3,3 V przeskalowane
  na 0 do 100 %). Poniżej 10 % pompa się zatrzymuje i zgłaszany jest
  alarm; powyżej 15 % może ruszyć ponownie (histereza).
- **Czas pracy** ustawia się na stronie w minutach i jest zachowywany
  po zaniku zasilania (zmienna retencyjna).
- Licznik energii **Modbus TCP** w sieci podaje napięcie sieci
  (rejestr 0, rejestry wejściowe, unit 1 pod 192.168.1.60 - zmień na
  adres swojego licznika). Powyżej 253 V zgłaszany jest alarm.
- **CAN** (transceiver na GPIO4 / GPIO36) co 100 ms wysyła poziom i
  stan pompy w ramce 0x181 i odbiera wartość zadaną w 0x201.
- **MQTT** publikuje poziom, stan pompy i napięcie do brokera Home
  Assistant, który sam je znajduje (discovery); pompę można
  uruchomić z Home Assistant.
- **WEBview** udostępnia stronę operatora - pompę, poziom, jego
  wykres i alarmy - każdej przeglądarce w sieci.

## Program

![Program drabinkowy przykładu](img/ladder.png)

## Strona operatora

![Strona operatora w symulacji](img/screen.png)

## Otwórz i uruchom

1. Otwórz `all-in-one.prj32` w edytorze.
2. Zmień adresy (urządzenia Modbus, brokera MQTT) na adresy swojej sieci.
3. Uruchom **symulację** (pasek narzędzi), aby wypróbować projekt na PC, albo wgraj go na płytkę - zobacz [Instalacja runtime](../../install.pl.md).

## Co powinieneś zobaczyć

Przy podkręconym potencjometrze naciśnij BUT1: przekaźnik na GPIO33
włącza się, a dioda pompy na stronie świeci. Skręć potencjometr
poniżej 10 %: pompa się zatrzymuje, a alarm pojawia się w tabeli. W
Home Assistant płytka pojawia się z poziomem, pompą i napięciem.


---

[← Przykładowe projekty](../README.pl.md) | [Przegląd](../../README.pl.md)
