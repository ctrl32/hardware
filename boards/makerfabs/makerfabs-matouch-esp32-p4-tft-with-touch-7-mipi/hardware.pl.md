---
title: 'Makerfabs MaTouch ESP32-P4 7": sprzęt i okablowanie'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Makerfabs MaTouch ESP32-P4 7" - mapa pinów
tags:
- esp32-p4
- display
- touch
- hmi
- ethernet
- makerfabs
---

# Sprzęt i okablowanie

## Czego potrzebujesz

- Makerfabs MaTouch ESP32-P4 TFT with Touch 7" MIPI.
- Kabel USB-C do transmisji danych - do pierwszego wgrania runtime i do zasilania.
- Zasilanie: zasilacz USB-C 5 V o prądzie co najmniej 2 A (większość pobiera podświetlenie wyświetlacza).
- Kabel Ethernet albo Wi-Fi twojej sieci.
- PC z [edytorem ctrl32](https://ctrl32.com/download/) (Windows).
- Opcjonalnie, dla przykładu all-in-one: dwa przyciski i moduł przekaźnikowy na złączu J6; moduł ADS1115 na magistrali I2C; transceiver RS-485 3,3 V (np. MAX3485) i transceiver CAN 3,3 V (np. SN65HVD230).

## Zasilanie

| Źródło | Gdzie | Uwaga |
|---|---|---|
| USB 5 V | złącze USB-C | 2 A lub więcej - większość pobiera podświetlenie 7" |
| Akumulator Li-Po | złącze akumulatora | 3,7 V, ładowany na płytce |

!!! warning "Słaby zasilacz"
    Port USB komputera często nie udźwignie płytki z włączonym
    podświetleniem. Jeśli płytka uruchamia się ponownie, gdy pojawia się
    ekran, użyj zasilacza 5 V / 2 A lub zasilanego huba USB.

## Mapa pinów

![Makerfabs MaTouch ESP32-P4 7" - mapa pinów](pinout/pinout.png)

| GPIO | Funkcja w ctrl32 | Uwaga |
|---|---|---|
| 0 | RTC XTAL P | ⚠  |
| 1 | RTC XTAL N | ⚠  |
| 2 | wolny - I/O |  |
| 3 | wolny - I/O |  |
| 4 | wolny - I/O |  |
| 5 | wolny - I/O |  |
| 6 | C6 IO2 | ⚠  |
| 7 | TOUCH SDA |  |
| 8 | TOUCH SCL |  |
| 20 | wolny - I/O |  |
| 21 | wolny - I/O |  |
| 22 | TOUCH RST |  |
| 23 | TFT BL |  |
| 26 | USB1 PAIR | ⚠  |
| 27 | DSI RST |  |
| 28 | Ethernet RMII (IP101GRI) | ⚠ zajęty przez płytkę |
| 29 | Ethernet RMII (IP101GRI) | ⚠ zajęty przez płytkę |
| 30 | Ethernet RMII (IP101GRI) | ⚠ zajęty przez płytkę |
| 31 | Ethernet MDC (IP101GRI) | ⚠ zajęty przez płytkę |
| 32 | wolny - I/O |  |
| 33 | wolny - I/O |  |
| 34 | Ethernet RMII (IP101GRI) | ⚠ zajęty przez płytkę |
| 35 | Ethernet RMII (IP101GRI) | ⚠ zajęty przez płytkę |
| 36 | wolny - I/O | ⚠ pin strapping |
| 37 | CONSOLE RX | ⚠ pin strapping |
| 38 | CONSOLE TX | ⚠ pin strapping |
| 45 | MOSFET GATE | ⚠  |
| 46 | wolny - I/O |  |
| 47 | wolny - I/O |  |
| 48 | wolny - I/O |  |
| 49 | Ethernet RMII (IP101GRI) | ⚠ zajęty przez płytkę |
| 50 | Ethernet RMII (IP101GRI) | ⚠ zajęty przez płytkę |
| 51 | Ethernet PHY reset (IP101GRI) | ⚠ zajęty przez płytkę |
| 52 | Ethernet MDIO (IP101GRI) | ⚠ zajęty przez płytkę |
| 53 | AMP EN | ⚠  |
| 54 | C6 EN | ⚠  |

Wolne piny są na złączach **J6** i **J10** oraz na dwóch złączach Grove
(**J1**, **J2**). Magistrala I2C płytki (GPIO7 / GPIO8) obsługuje
kontroler dotyku i kodek audio; kolejne układy I2C (ADS1115, czujnik)
dołączają do tej samej magistrali. CAN i RS-485 nie mają transceivera na
płytce: przykład umieszcza je na wolnych pinach - **CAN** TX GPIO20 / RX
GPIO21 (Grove J2), **RS-485** TX GPIO4 / RX GPIO5 / DE GPIO32 (J10) -
każdy do modułu transceivera 3,3 V.

## Bezpieczeństwo

- Płytka nie jest przeznaczona do funkcji bezpieczeństwa. Wyłącznik
  awaryjny, wyłącznik drzwi lub kurtyna świetlna są podłączone sprzętowo,
  nigdy przez program ani ekran dotykowy.
- Piny GPIO pracują na 3,3 V. Sygnał 24 V wymaga transoptora; cewka
  przekaźnika wymaga sterownika (moduł przekaźnikowy go ma).
- Dotyk pojemnościowy może zarejestrować fałszywe naciśnięcie obok
  silnego źródła zakłóceń (falownika). Krytyczne polecenia na ekranie
  wymagają potwierdzenia.

## Zdjęcia

![Makerfabs MaTouch ESP32-P4 7" - zdjęcie 1](img/board-01.jpg)
![Makerfabs MaTouch ESP32-P4 7" - zdjęcie 2](img/board-02.jpg)
![Makerfabs MaTouch ESP32-P4 7" - zdjęcie 3](img/board-03.jpg)
![Makerfabs MaTouch ESP32-P4 7" - zdjęcie 4](img/board-04.jpg)
![Makerfabs MaTouch ESP32-P4 7" - zdjęcie 5](img/board-05.jpg)
![Makerfabs MaTouch ESP32-P4 7" - zdjęcie 6](img/board-06.jpg)
![Makerfabs MaTouch ESP32-P4 7" - zdjęcie 7](img/board-07.jpg)
![Makerfabs MaTouch ESP32-P4 7" - zdjęcie 8](img/board-08.jpg)

---

[← Przegląd](README.pl.md) | [Przegląd](README.pl.md) | [Instalacja runtime →](install.pl.md)
