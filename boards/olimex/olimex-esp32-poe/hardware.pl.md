---
title: 'Olimex ESP32-PoE: sprzęt i okablowanie'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-PoE - mapa pinów
tags:
- esp32
- ethernet
- poe
- olimex
---

# Sprzęt i okablowanie

## Czego potrzebujesz

- Olimex ESP32-PoE (wariant WROOM-32E, bez PSRAM).
- Kabel micro-USB do transmisji danych - do pierwszego wgrania runtime.
- Zasilanie: zasilacz USB 5 V albo switch / injector PoE (IEEE 802.3af).
- Kabel Ethernet i wolny port w twojej sieci.
- PC z [edytorem ctrl32](https://ctrl32.com/download/) (Windows).
- Opcjonalnie, dla przykładu all-in-one: przycisk jest na płytce (BUT1); moduł przekaźnikowy lub dioda LED z rezystorem na GPIO33; potencjometr (10 k) między 3,3 V a GND ze ślizgaczem na GPIO35; transceiver CAN 3,3 V (np. SN65HVD230) na GPIO4 (TX) / GPIO36 (RX) złącza UEXT.

## Zasilanie

Płytka pobiera zasilanie z jednego z trzech źródeł:

| Źródło | Gdzie | Uwaga |
|---|---|---|
| USB 5 V | złącze micro-USB | droga do pierwszego wgrania |
| PoE | gniazdo Ethernet, ze switcha lub injectora PoE | IEEE 802.3af |
| Akumulator Li-Po | złącze akumulatora | ładowany na płytce |

!!! danger "Nigdy nie podłączaj USB i PoE jednocześnie"
    ESP32-PoE **nie jest izolowana galwanicznie**. Gdy płytka jest
    zasilana przez PoE, jej masa podąża za zasilaniem PoE - kabel USB do
    twojego PC może wtedy przewodzić niszczący prąd. Wgraj runtime przez
    USB przy **odłączonym** kablu Ethernet (lub z portu bez PoE), a
    dopiero potem uruchom płytkę na PoE. Tam, gdzie PC musi pozostać
    podłączony, gdy płytka jest na PoE, użyj
    ESP32-PoE-ISO.

## Mapa pinów

![Olimex ESP32-PoE - mapa pinów](pinout/pinout.png)

| GPIO | Funkcja w ctrl32 | Uwaga |
|---|---|---|
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
| 16 | I2C SCL |  |
| 17 | Ethernet 50 MHz clock (LAN8710A) | ⚠ zajęty przez płytkę |
| 18 | Ethernet MDIO (LAN8710A) | ⚠ zajęty przez płytkę |
| 19 | Ethernet RMII TXD0 (LAN8710A) | ⚠ zajęty przez płytkę |
| 21 | Ethernet RMII TX_EN (LAN8710A) | ⚠ zajęty przez płytkę |
| 22 | Ethernet RMII TXD1 (LAN8710A) | ⚠ zajęty przez płytkę |
| 23 | Ethernet MDC (LAN8710A) | ⚠ zajęty przez płytkę |
| 25 | Ethernet RMII RXD0 (LAN8710A) | ⚠ zajęty przez płytkę |
| 26 | Ethernet RMII RXD1 (LAN8710A) | ⚠ zajęty przez płytkę |
| 27 | Ethernet RMII CRS_DV (LAN8710A) | ⚠ zajęty przez płytkę |
| 33 | wolny - I/O | ADC1 |
| 34 | wolny - przycisk płytki | ⚠ tylko wejście, ADC1 |
| 35 | wolny - wejście | ⚠ tylko wejście, ADC1 |
| 36 | free (UART RX line) | ⚠ tylko wejście, ADC1 |

Wolne piny są na złączach **EXT1 / EXT2** (2,54 mm) i na złączu **UEXT**.
GPIO34 do GPIO39 to tylko wejścia - wyjście na nich edytor odrzuca.
Złącze UEXT wyprowadza I2C (GPIO13 / GPIO16) i SPI (GPIO14 / GPIO2 /
GPIO15, współdzielone z gniazdem microSD).

## Bezpieczeństwo

- Płytka nie jest przeznaczona do funkcji bezpieczeństwa. Wyłącznik
  awaryjny, wyłącznik drzwi lub kurtyna świetlna są podłączone sprzętowo,
  nigdy przez program.
- Piny GPIO pracują na 3,3 V. Wejście 24 V wymaga transoptora lub
  konwertera poziomów; cewka przekaźnika wymaga sterownika (moduł
  przekaźnikowy go ma).

---

[← Przegląd](README.pl.md) | [Przegląd](README.pl.md) | [Instalacja runtime →](install.pl.md)
