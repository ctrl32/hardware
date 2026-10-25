---
title: 'Olimex ESP32-EVB: sprzęt i okablowanie'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-EVB - mapa pinów
tags:
- esp32
- ethernet
- can
- relay
- olimex
---

# Sprzęt i okablowanie

## Czego potrzebujesz

- Olimex ESP32-EVB.
- Kabel micro-USB do transmisji danych - do pierwszego wgrania runtime.
- Zasilanie: zasilacz USB 5 V albo 5 V na zacisku śrubowym.
- Kabel Ethernet i wolny port w twojej sieci.
- PC z [edytorem ctrl32](https://ctrl32.com/download/) (Windows).
- Opcjonalnie, dla przykładu all-in-one: potencjometr (10 k) między 3,3 V a GND ze ślizgaczem na GPIO36 (UEXT); węzeł CAN lub adapter CAN i dwa terminatory 120 omów.
- Opcjonalnie: wyświetlacz Olimex MOD-LCD2.8RTP (2,8 cala, 240 x 320, dotyk rezystancyjny) na złączu UEXT.

## Zasilanie

| Źródło | Gdzie | Uwaga |
|---|---|---|
| USB 5 V | złącze micro-USB | droga do pierwszego wgrania |
| 5 V DC | zacisk śrubowy | do szafy |
| Akumulator Li-Po | złącze akumulatora | ładowany na płytce |

!!! warning "Przekaźniki przełączają napięcie sieciowe"
    Styki przekaźników podłączaj tylko przy odłączonym zasilaniu płytki,
    w obudowie, i tylko jako osoba uprawniona do prac przy instalacjach
    sieciowych. Styki wytrzymują 10 A / 250 VAC; silnik lub grzałka
    powyżej tej wartości wymaga stycznika sterowanego przez przekaźnik.

## Mapa pinów

![Olimex ESP32-EVB - mapa pinów](pinout/pinout.png)

| GPIO | Funkcja w ctrl32 | Uwaga |
|---|---|---|
| 0 | Ethernet 50 MHz clock (LAN8710A) | ⚠ zajęty przez płytkę |
| 2 | TFT MOSI | ⚠ pin strapping |
| 2 | SPI MOSI | ⚠ pin strapping |
| 4 | free (UART TX line) |  |
| 5 | CAN TX |  |
| 6 | Flash SPI modułu | ⚠ zajęty przez płytkę |
| 7 | Flash SPI modułu | ⚠ zajęty przez płytkę |
| 8 | Flash SPI modułu | ⚠ zajęty przez płytkę |
| 9 | Flash SPI modułu | ⚠ zajęty przez płytkę |
| 10 | Flash SPI modułu | ⚠ zajęty przez płytkę |
| 11 | Flash SPI modułu | ⚠ zajęty przez płytkę |
| 13 | I2C SDA |  |
| 14 | TFT SCLK |  |
| 14 | SPI SCLK |  |
| 15 | TFT DC | ⚠ pin strapping |
| 15 | SPI MISO | ⚠ pin strapping |
| 16 | I2C SCL |  |
| 17 | TFT CS |  |
| 17 | free (SPI CS line) |  |
| 18 | Ethernet MDIO (LAN8710A) | ⚠ zajęty przez płytkę |
| 19 | Ethernet RMII TXD0 (LAN8710A) | ⚠ zajęty przez płytkę |
| 21 | Ethernet RMII TX_EN (LAN8710A) | ⚠ zajęty przez płytkę |
| 22 | Ethernet RMII TXD1 (LAN8710A) | ⚠ zajęty przez płytkę |
| 23 | Ethernet MDC (LAN8710A) | ⚠ zajęty przez płytkę |
| 25 | Ethernet RMII RXD0 (LAN8710A) | ⚠ zajęty przez płytkę |
| 26 | Ethernet RMII RXD1 (LAN8710A) | ⚠ zajęty przez płytkę |
| 27 | Ethernet RMII CRS_DV (LAN8710A) | ⚠ zajęty przez płytkę |
| 32 | free (REL1 line) | ADC1 |
| 33 | free (REL2 line) | ADC1 |
| 34 | wolny - przycisk płytki | ⚠ tylko wejście, ADC1 |
| 35 | CAN RX |  |
| 36 | free (UART RX line) | ⚠ tylko wejście, ADC1 |

**Przekaźniki:** REL1 na GPIO32, REL2 na GPIO33. **Przycisk:** BUT1 na
GPIO34 (tylko wejście). **CAN:** transceiver na płytce na GPIO5 (TX) /
GPIO35 (RX), CAN_H / CAN_L na zacisku - zakończ magistralę rezystorem
120 omów na obu końcach. Złącze **UEXT** wyprowadza I2C (GPIO13 / GPIO16),
SPI i wolny UART (GPIO4 / GPIO36); opcjonalny wyświetlacz używa jego
linii SPI.

## Bezpieczeństwo

- Płytka nie jest przeznaczona do funkcji bezpieczeństwa. Wyłącznik
  awaryjny, wyłącznik drzwi lub kurtyna świetlna są podłączone sprzętowo,
  nigdy przez program.
- Piny GPIO pracują na 3,3 V. Sygnał 24 V wymaga transoptora lub
  konwertera poziomów; cewka przekaźnika wymaga sterownika (moduł
  przekaźnikowy go ma).

---

[← Przegląd](README.pl.md) | [Przegląd](README.pl.md) | [Instalacja runtime →](install.pl.md)
