---
title: 'Makerfabs MaTouch ESP32-P4 7": przykład Car cockpit'
slug: car-cockpit
sidebar_position: 10
hardware: /hardware/boards/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/
image: img/screen.png
image_alt: Strona operatora przykładu car cockpit dla Makerfabs MaTouch ESP32-P4 7"
tags:
- esp32-p4
- display
- touch
- hmi
- ethernet
- makerfabs
- example
---

# Car cockpit

Zestaw wskaźników na magistrali pojazdowej J1939 - prędkościomierz i obrotomierz, bieg, paliwo, płyn chłodzący, lampki ostrzegawcze, sterowniki na magistrali, aktywny kod błędu opisany słowami i ustawienia kierowcy.

**Pobieranie:** [car-cockpit.prj32](car-cockpit.prj32) - otwórz go w edytorze ctrl32 (**File → Open**).

## Co robi

Pięć ekranów na szkle 7":

- **Cockpit** - prędkościomierz i obrotomierz, bieg, paliwo, płyn
  chłodzący i akumulator, licznik kilometrów i licznik dzienny,
  zegar, kierunkowskazy i lampki ostrzegawcze.
- **Engine** - wartości silnika w szczegółach.
- **Bus** - sieć **J1939**: węzeł panelu, silnik, skrzynia biegów i
  hamulce oraz to, czy odpowiadają, lampki DM1, każdy sygnał z jego
  grupą parametrów.
- **Faults** - lista alarmów i aktywny kod błędu silnika
  (SPN / FMI / liczba) z jego znaczeniem opisanym słowami.
- **Settings** - tryb demo, jednostki, ostrzeżenie o prędkości,
  czerwone pole obrotomierza, ostrzeżenia o płynie chłodzącym i
  paliwie, interwał serwisowy.

Komunikacja to **SAE J1939** na CAN płytki (transceiver 3,3 V na
GPIO47 / GPIO48, 250 kbit/s): silnik, skrzynia biegów i hamulce
rozgłaszają swoje grupy parametrów, a panel je odczytuje - żeby
wartość dotarła, nie potrzeba żadnego programu. W **trybie demo**
(domyślnie włączonym) program SIM jedzie cykl: rusza, zmienia biegi,
jedzie ze stałą prędkością, hamuje, zatrzymuje się - a od czasu do
czasu pojawia się błąd.

## Ekrany

**Kokpit**

![Ekran Cockpit: prędkościomierz i obrotomierz, bieg, paliwo, płyn chłodzący i lampki ostrzegawcze](img/cockpit.png)

**Magistrala**

![Ekran Bus z siecią J1939: sterowniki i sygnały, które odczytuje panel](img/bus.png)

**Błędy**

![Ekran Faults: lista alarmów i aktywny kod błędu](img/faults.png)

## Otwórz i uruchom

1. Otwórz `car-cockpit.prj32` w edytorze.
2. Uruchom go bez zmian w trybie demo; w pojeździe podłącz transceiver CAN do GPIO47 / GPIO48 i wyłącz tryb demo na ekranie Settings.
3. Uruchom **symulację** (pasek narzędzi), aby wypróbować projekt na PC, albo wgraj go na płytkę - zobacz [Instalacja runtime](../../install.pl.md).

## Co powinieneś zobaczyć

Zestaw wskaźników uruchamia się w trybie demo: wskazówki przechodzą
przez cykl jazdy, bieg się zmienia, kierunkowskazy migają. Wyłącz tryb
demo na ekranie Settings i podłącz magistralę - wskaźniki pokazują
wtedy pojazd.


---

[← Przykładowe projekty](../README.pl.md) | [Przegląd](../../README.pl.md)
