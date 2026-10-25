---
title: 'LaskaKit ESPlan: sprzęt i okablowanie'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: LaskaKit ESPlan - mapa pinów
tags:
- esp32
- ethernet
- rs485
- modbus
- laskakit
---

# Sprzęt i okablowanie

## Czego potrzebujesz

- LaskaKit ESPlan.
- Kabel USB-C do transmisji danych - do pierwszego wgrania runtime.
- Zasilanie: 12 lub 24 V DC na zacisku śrubowym (7-40 V) albo 5 V przez USB-C.
- Kabel Ethernet i wolny port w twojej sieci.
- PC z [edytorem ctrl32](https://ctrl32.com/download/) (Windows).
- Opcjonalnie, dla przykładu all-in-one: czujnik temperatury Modbus RTU (unit 1) na zacisku RS-485; przycisk z GPIO16 do GND; potencjometr (10 k) między 3,3 V a GND ze ślizgaczem na GPIO35; transceiver CAN 3,3 V na GPIO14 (TX) / GPIO39 (RX).

## Zasilanie

| Źródło | Gdzie | Uwaga |
|---|---|---|
| 7-40 V DC | zacisk śrubowy | zalecane 12 lub 24 V |
| USB 5 V | złącze USB-C | droga do pierwszego wgrania |
| PoE | przez opcjonalny moduł PoE (802.3af) | dodatek |

## Mapa pinów

![LaskaKit ESPlan - mapa pinów](pinout/pinout.png)

| GPIO | Funkcja w ctrl32 | Uwaga |
|---|---|---|
| 0 | free (LED0 line) | ⚠ pin strapping |
| 4 | RS485 TX |  |
| 5 | Ethernet PHY power (LAN8720A) | ⚠ zajęty przez płytkę |
| 6 | Flash SPI modułu | ⚠ zajęty przez płytkę |
| 7 | Flash SPI modułu | ⚠ zajęty przez płytkę |
| 8 | Flash SPI modułu | ⚠ zajęty przez płytkę |
| 9 | Flash SPI modułu | ⚠ zajęty przez płytkę |
| 10 | Flash SPI modułu | ⚠ zajęty przez płytkę |
| 11 | Flash SPI modułu | ⚠ zajęty przez płytkę |
| 12 | SPI MISO | ⚠ pin strapping |
| 13 | SPI MOSI |  |
| 14 | free (SPI SCLK line) |  |
| 15 | SPI CS | ⚠ pin strapping |
| 16 | wolny - I/O |  |
| 17 | Ethernet 50 MHz clock (LAN8720A) | ⚠ zajęty przez płytkę |
| 18 | Ethernet MDIO (LAN8720A) | ⚠ zajęty przez płytkę |
| 19 | Ethernet RMII TXD0 (LAN8720A) | ⚠ zajęty przez płytkę |
| 21 | Ethernet RMII TX_EN (LAN8720A) | ⚠ zajęty przez płytkę |
| 22 | Ethernet RMII TXD1 (LAN8720A) | ⚠ zajęty przez płytkę |
| 23 | Ethernet MDC (LAN8720A) | ⚠ zajęty przez płytkę |
| 25 | Ethernet RMII RXD0 (LAN8720A) | ⚠ zajęty przez płytkę |
| 26 | Ethernet RMII RXD1 (LAN8720A) | ⚠ zajęty przez płytkę |
| 27 | Ethernet RMII CRS_DV (LAN8720A) | ⚠ zajęty przez płytkę |
| 32 | TOUCH SCL |  |
| 33 | TOUCH SDA |  |
| 35 | wolny - wejście | ⚠ tylko wejście, ADC1 |
| 36 | RS485 RX |  |
| 39 | wolny - wejście | ⚠ tylko wejście, ADC1 |

**RS-485:** A i B na zacisku, transceiver WS3081 na GPIO4 (TX) /
GPIO36 (RX); zworka włącza terminację 120 omów - ustaw ją tylko na obu
końcach linii. Złącza **uSup** wyprowadzają I2C (GPIO33 / GPIO32) i SPI.
Dioda LED płytki jest na GPIO0 (pin strapping - zostaw go jako wyjście
sterowane przez program).

## Bezpieczeństwo

- Płytka nie jest przeznaczona do funkcji bezpieczeństwa. Wyłącznik
  awaryjny, wyłącznik drzwi lub kurtyna świetlna są podłączone sprzętowo,
  nigdy przez program.
- Piny GPIO pracują na 3,3 V. Sygnał 24 V wymaga transoptora lub
  konwertera poziomów; cewka przekaźnika wymaga sterownika (moduł
  przekaźnikowy go ma).

---

[← Przegląd](README.pl.md) | [Przegląd](README.pl.md) | [Instalacja runtime →](install.pl.md)
