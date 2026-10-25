---
title: 'Olimex ESP32-GATEWAY: sprzęt i okablowanie'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-GATEWAY - mapa pinów
tags:
- esp32
- ethernet
- gateway
- olimex
---

# Sprzęt i okablowanie

## Czego potrzebujesz

- Olimex ESP32-GATEWAY.
- Kabel USB-C do transmisji danych - do wgrywania i do zasilania (5 V).
- Kabel Ethernet i wolny port w twojej sieci.
- PC z [edytorem ctrl32](https://ctrl32.com/download/) (Windows).
- Przykład all-in-one używa własnego przycisku (GPIO34) i diody LED (GPIO33) płytki - nic więcej nie trzeba podłączać.

## Zasilanie

| Źródło | Gdzie | Uwaga |
|---|---|---|
| USB 5 V | złącze USB-C | zasilanie i programowanie |

## Mapa pinów

![Olimex ESP32-GATEWAY - mapa pinów](pinout/pinout.png)

| GPIO | Funkcja w ctrl32 | Uwaga |
|---|---|---|
| 2 | SPI MOSI | ⚠ pin strapping |
| 5 | Ethernet PHY power (LAN8710A) | ⚠ zajęty przez płytkę |
| 6 | Flash SPI modułu | ⚠ zajęty przez płytkę |
| 7 | Flash SPI modułu | ⚠ zajęty przez płytkę |
| 8 | Flash SPI modułu | ⚠ zajęty przez płytkę |
| 9 | Flash SPI modułu | ⚠ zajęty przez płytkę |
| 10 | Flash SPI modułu | ⚠ zajęty przez płytkę |
| 11 | Flash SPI modułu | ⚠ zajęty przez płytkę |
| 13 | free (SPI CS line) |  |
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
| 32 | I2C SDA |  |
| 33 | free (LED0 line) | ADC1 |
| 34 | wolny - przycisk płytki | ⚠ tylko wejście, ADC1 |

20-pinowe złącze **EXT** wyprowadza wolne piny i linie I2C / SPI. Dioda
LED płytki jest na GPIO33, a jej przycisk na GPIO34 (tylko wejście).
Wolnych pinów zostaje niewiele: kolejne I/O idą przez Modbus TCP lub
układy I2C.

## Bezpieczeństwo

- Płytka nie jest przeznaczona do funkcji bezpieczeństwa. Wyłącznik
  awaryjny, wyłącznik drzwi lub kurtyna świetlna są podłączone sprzętowo,
  nigdy przez program.
- Piny GPIO pracują na 3,3 V. Sygnał 24 V wymaga transoptora lub
  konwertera poziomów; cewka przekaźnika wymaga sterownika (moduł
  przekaźnikowy go ma).

---

[← Przegląd](README.pl.md) | [Przegląd](README.pl.md) | [Instalacja runtime →](install.pl.md)
