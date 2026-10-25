---
title: 'Olimex ESP32-POE2: sprzęt i okablowanie'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-POE2 - mapa pinów
tags:
- esp32
- ethernet
- poe
- psram
- olimex
---

# Sprzęt i okablowanie

## Czego potrzebujesz

- Olimex ESP32-POE2.
- Kabel USB-C do transmisji danych - do pierwszego wgrania runtime.
- Zasilanie: switch / injector PoE (IEEE 802.3at, klasa 4 dla pełnych 25 W) albo zasilacz USB 5 V.
- Kabel Ethernet i wolny port w twojej sieci.
- PC z [edytorem ctrl32](https://ctrl32.com/download/) (Windows).
- Opcjonalnie, dla przykładu all-in-one: przycisk BUT1 jest na płytce; moduł przekaźnikowy lub dioda LED na GPIO4 (UEXT); potencjometr (10 k) między 3,3 V a GND ze ślizgaczem na GPIO36; transceiver CAN 3,3 V na GPIO5 (TX) / GPIO39 (RX).

## Zasilanie

| Źródło | Gdzie | Uwaga |
|---|---|---|
| PoE | gniazdo Ethernet | IEEE 802.3at klasa 4, do 25 W |
| USB 5 V | złącze USB-C | droga do pierwszego wgrania |
| Akumulator Li-Po | złącze akumulatora | ładowany na płytce |

Zasilana przez Ethernet płytka zasila obwody zewnętrzne: **24 V / 0,75 A
lub 12 V / 1,5 A** (wybiera zworka), **5 V / 1,5 A** i **3,3 V / 1 A**,
łącznie 25 W.

!!! danger "Nigdy nie podłączaj USB i PoE jednocześnie"
    ESP32-POE2 **nie jest izolowana galwanicznie** od zasilania
    Ethernet. Wgraj runtime przez USB przy odłączonym kablu Ethernet (lub
    z portu bez PoE), a dopiero potem uruchom płytkę na PoE.

## Mapa pinów

![Olimex ESP32-POE2 - mapa pinów](pinout/pinout.png)

| GPIO | Funkcja w ctrl32 | Uwaga |
|---|---|---|
| 0 | Ethernet 50 MHz clock (LAN8710A) | ⚠ zajęty przez płytkę |
| 2 | SPI MOSI | ⚠ pin strapping |
| 4 | free (UART TX line) |  |
| 5 | free (SPI CS line) |  |
| 6 | Flash SPI modułu | ⚠ zajęty przez płytkę |
| 7 | Flash SPI modułu | ⚠ zajęty przez płytkę |
| 8 | Flash SPI modułu | ⚠ zajęty przez płytkę |
| 9 | Flash SPI modułu | ⚠ zajęty przez płytkę |
| 10 | Flash SPI modułu | ⚠ zajęty przez płytkę |
| 11 | Flash SPI modułu | ⚠ zajęty przez płytkę |
| 12 | Ethernet PHY power (LAN8710A) | ⚠ zajęty przez płytkę |
| 13 | I2C SDA |  |
| 14 | SPI SCLK |  |
| 15 | SPI MISO | ⚠ pin strapping |
| 18 | Ethernet MDIO (LAN8710A) | ⚠ zajęty przez płytkę |
| 19 | Ethernet RMII TXD0 (LAN8710A) | ⚠ zajęty przez płytkę |
| 21 | Ethernet RMII TX_EN (LAN8710A) | ⚠ zajęty przez płytkę |
| 22 | Ethernet RMII TXD1 (LAN8710A) | ⚠ zajęty przez płytkę |
| 23 | Ethernet MDC (LAN8710A) | ⚠ zajęty przez płytkę |
| 25 | Ethernet RMII RXD0 (LAN8710A) | ⚠ zajęty przez płytkę |
| 26 | Ethernet RMII RXD1 (LAN8710A) | ⚠ zajęty przez płytkę |
| 27 | Ethernet RMII CRS_DV (LAN8710A) | ⚠ zajęty przez płytkę |
| 33 | I2C SCL |  |
| 34 | wolny - przycisk płytki | ⚠ tylko wejście, ADC1 |
| 36 | free (UART RX line) | ⚠ tylko wejście, ADC1 |
| 39 | wolny - wejście | ⚠ tylko wejście, ADC1 |

Wolne piny są na złączach **EXT** i na złączu **UEXT**. GPIO34 do GPIO39
to tylko wejścia. PSRAM modułu zajmuje GPIO16 / GPIO17, dlatego zegar
Ethernetu pracuje na GPIO0, a I2C używa GPIO13 / GPIO33.

## Bezpieczeństwo

- Płytka nie jest przeznaczona do funkcji bezpieczeństwa. Wyłącznik
  awaryjny, wyłącznik drzwi lub kurtyna świetlna są podłączone sprzętowo,
  nigdy przez program.
- Piny GPIO pracują na 3,3 V. Wejście 24 V wymaga transoptora lub
  konwertera poziomów; cewka przekaźnika wymaga sterownika (moduł
  przekaźnikowy go ma).

---

[← Przegląd](README.pl.md) | [Przegląd](README.pl.md) | [Instalacja runtime →](install.pl.md)
