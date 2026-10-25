---
title: 'Makerfabs MaTouch Lite ESP32-S3 3.95": sprzęt i okablowanie'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Makerfabs MaTouch Lite ESP32-S3 3.95" - mapa pinów
tags:
- esp32-s3
- display
- touch
- hmi
- wifi
- makerfabs
---

# Sprzęt i okablowanie

## Czego potrzebujesz

- Makerfabs MaTouch Lite ESP32-S3 3,95" (ST7796).
- Kabel USB-C do transmisji danych - do wgrywania i do zasilania.
- Nazwa i hasło twojej sieci Wi-Fi 2,4 GHz.
- PC z [edytorem ctrl32](https://ctrl32.com/download/) (Windows).
- Opcjonalnie, dla przykładu all-in-one: moduł przekaźnikowy lub dioda LED na GPIO4, potencjometr (10 k) między 3,3 V a GND ze ślizgaczem na GPIO5 (złącza JST) oraz transceiver CAN 3,3 V (np. SN65HVD230) na GPIO6 / GPIO7.

## Zasilanie

| Źródło | Gdzie | Uwaga |
|---|---|---|
| USB 5 V | złącze USB-C | zasilanie i programowanie |
| Akumulator Li-Po | złącze akumulatora | 3,7 V |

## Mapa pinów

![Makerfabs MaTouch Lite ESP32-S3 3.95" - mapa pinów](pinout/pinout.png)

| GPIO | Funkcja w ctrl32 | Uwaga |
|---|---|---|
| 0 | BOOT BTN | ⚠ pin strapping |
| 1 | TFT RST |  |
| 2 | SD CMD | ⚠  |
| 4 | wolny - I/O | ADC1 |
| 5 | wolny - I/O | ADC1 |
| 6 | wolny - I/O | ADC1 |
| 7 | wolny - I/O | ADC1 |
| 13 | TFT MOSI |  |
| 14 | TFT SCLK |  |
| 15 | TFT CS |  |
| 21 | TFT DC |  |
| 38 | TOUCH SDA |  |
| 39 | TOUCH SCL |  |
| 40 | TOUCH INT |  |
| 41 | SD DO | ⚠  |
| 42 | SD SCLK | ⚠  |
| 48 | TFT BL |  |

Dwa złącza **JST** wyprowadzają cztery wolne piny (GPIO4 do GPIO7) - to
niewiele, więc przykład umieszcza na nich wyjście, wejście analogowe i
CAN; kolejne I/O idą przez Modbus TCP lub układy I2C. Wyświetlacz,
kontroler dotyku i gniazdo microSD zajmują pozostałe piny.

## Bezpieczeństwo

- Płytka nie jest przeznaczona do funkcji bezpieczeństwa. Wyłącznik
  awaryjny, wyłącznik drzwi lub kurtyna świetlna są podłączone sprzętowo,
  nigdy przez program ani ekran dotykowy.
- Piny GPIO pracują na 3,3 V. Cewka przekaźnika wymaga sterownika (moduł przekaźnikowy go ma).

---

[← Przegląd](README.pl.md) | [Przegląd](README.pl.md) | [Instalacja runtime →](install.pl.md)
