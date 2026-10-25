---
title: 'Makerfabs MaTouch ESP32-P4 7": przykład Home dashboard'
slug: home-dashboard
sidebar_position: 10
hardware: /hardware/boards/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/
image: img/screen.jpg
image_alt: Strona operatora przykładu home dashboard dla Makerfabs MaTouch ESP32-P4 7"
tags:
- esp32-p4
- display
- touch
- hmi
- ethernet
- makerfabs
- example
---

# Home dashboard

Panel sterowania całym domem w ciemnym stylu matowego szkła - ogrzewanie w każdym pokoju, energia z fotowoltaiką i akumulatorem, oświetlenie, garaż i pogoda - z symulowanym domem w tle.

**Pobieranie:** [home-dashboard.prj32](home-dashboard.prj32) - otwórz go w edytorze ctrl32 (**File → Open**).

## Co robi

Sześć ekranów na zdjęciach domu, każdy to zestaw kart z matowego
szkła:

- **Home** - godzina, pogoda, pokoje, alarm i sceny.
- **Weather** - dziś i kolejne dni.
- **Climate** - sześć pokoi, każdy z temperaturą, wartością zadaną i
  ogrzewaniem; pompa ciepła i zasobnik ciepłej wody.
- **Energy** - moc fotowoltaiki, zużycie domu, akumulator i sieć,
  kWh z dnia.
- **Lights** - oświetlenie pokoi i jego sceny.
- **Access** - brama garażowa, ładowarka samochodu, alarm.

Program **SIM** to dom: temperatura zewnętrzna podąża za porą dnia,
moc fotowoltaiki za słońcem, zużycie ma szczyty rano i wieczorem, a
pokoje grzeją się z histerezą do swoich wartości zadanych. Zastąp jego
zmienne swoimi urządzeniami Modbus, MQTT lub CAN, aby sterować
prawdziwym domem.

## Ekrany

**Start**

![Ekran Home panelu: godzina, pogoda, pokoje, alarm i sceny](img/home.jpg)

**Klimat**

![Ekran Climate: sześć pokoi z temperaturami i wartościami zadanymi](img/climate.png)

**Energia**

![Ekran Energy: fotowoltaika, zużycie domu, akumulator i sieć](img/energy.jpg)

## Otwórz i uruchom

1. Otwórz `home-dashboard.prj32` w edytorze.
2. Uruchom go bez zmian - dom jest symulowany; dla prawdziwego domu zastąp zmienne programu SIM swoimi urządzeniami.
3. Uruchom **symulację** (pasek narzędzi), aby wypróbować projekt na PC, albo wgraj go na płytkę - zobacz [Instalacja runtime](../../install.pl.md).

## Co powinieneś zobaczyć

Pojawia się ekran Home z godziną, pogodą i pokojami; wartości zmieniają
się wraz z upływem symulowanego dnia. Dotknięcie wartości zadanej
pokoju zmienia ją, a pokój się do niej nagrzewa.


---

[← Przykładowe projekty](../README.pl.md) | [Przegląd](../../README.pl.md)
