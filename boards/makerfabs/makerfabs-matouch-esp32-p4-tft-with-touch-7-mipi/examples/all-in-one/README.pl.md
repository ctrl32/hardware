---
title: 'Makerfabs MaTouch ESP32-P4 7": przykład All-in-one'
slug: all-in-one
sidebar_position: 10
hardware: /hardware/boards/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/
image: img/screen.png
image_alt: Strona operatora przykładu all-in-one dla Makerfabs MaTouch ESP32-P4 7"
tags:
- esp32-p4
- display
- touch
- hmi
- ethernet
- makerfabs
- example
---

# All-in-one

Silnik sterowany z ekranu dotykowego, dwóch przycisków i Home Assistant, ze wskaźnikiem ciśnienia, wentylatorem według temperatury Modbus RTU, licznikiem mocy Modbus TCP, ramkami CAN, wykresem i alarmami.

**Pobieranie:** [all-in-one.prj32](all-in-one.prj32) - otwórz go w edytorze ctrl32 (**File → Open**).

## Co robi

Program to mały sterownik maszyny:

- **Start** pochodzi od przycisku na GPIO47, od **Start** na ekranie
  lub z Home Assistant przez MQTT; **Stop** od przycisku na GPIO48,
  od **Stop** na ekranie lub od wzrostu ciśnienia powyżej wartości
  zadanej, która przychodzi przez **CAN** (ramka 0x201).
- Podtrzymanie steruje wyjściem silnika na **GPIO33**; licznik
  zachowuje liczbę startów po zaniku zasilania.
- **Ciśnienie** to wejście analogowe przez **ADS1115** na magistrali
  I2C (0-10 V przez dzielnik 1:4, 0-10 bar) i co 100 ms wychodzi
  przez CAN (ramka 0x181).
- **Temperatura** pochodzi z czujnika **Modbus RTU** (unit 1, rejestr
  wejściowy 1, 0,1 °C); wentylator podąża za nią z histerezą.
- Licznik **Modbus TCP** podaje pobór mocy.
- Trzy **ekrany** na szkle: przegląd, wykres i alarmy; prostsza
  strona w każdej przeglądarce (WEBview).

## Program

![Program drabinkowy przykładu](img/ladder.png)

## Strona operatora

![Strona operatora w symulacji](img/screen.png)

## Otwórz i uruchom

1. Otwórz `all-in-one.prj32` w edytorze.
2. Zmień adresy (urządzenia Modbus, brokera MQTT) na adresy swojej sieci.
3. Uruchom **symulację** (pasek narzędzi), aby wypróbować projekt na PC, albo wgraj go na płytkę - zobacz [Instalacja runtime](../../install.pl.md).

## Co powinieneś zobaczyć

Na szkle pojawia się przegląd. Naciśnij **Start**: dioda silnika
świeci, a licznik startów rośnie. Wskaźnik pokazuje ciśnienie, ekran
Trend rysuje je razem z temperaturą, a na ekranie Alarms pojawia się
alarm, gdy ciśnienie przekroczy 8 bar.


---

[← Przykładowe projekty](../README.pl.md) | [Przegląd](../../README.pl.md)
