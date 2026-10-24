---
title: 'Makerfabs MaTouch ESP32-P4 7": hardvér a zapojenie'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Makerfabs MaTouch ESP32-P4 7" - mapa pinov
tags:
- esp32-p4
- display
- touch
- hmi
- ethernet
- makerfabs
---

# Hardvér a zapojenie

## Čo treba

- Makerfabs MaTouch ESP32-P4 TFT with Touch 7" MIPI.
- Dátový kábel USB-C - na prvé nahratie runtime a na napájanie.
- Napájanie: zdroj 5 V cez USB-C aspoň 2 A (väčšinu odoberá podsvietenie displeja).
- Sieťový kábel alebo Wi-Fi tvojej siete.
- PC s [editorom ctrl32](https://ctrl32.com/download/) (Windows).
- Voliteľne pre príklad all-in-one: dve tlačidlá a reléový modul na konektore J6; modul ADS1115 na zbernici I2C; 3,3 V prevodník RS-485 (napr. MAX3485) a 3,3 V prevodník CAN (napr. SN65HVD230).

## Napájanie

| Zdroj | Kde | Poznámka |
|---|---|---|
| USB 5 V | konektor USB-C | 2 A a viac - väčšinu odoberá podsvietenie 7" displeja |
| Li-Po batéria | konektor batérie | 3,7 V, nabíja sa na doske |

!!! warning "Slabý zdroj"
    Port USB v PC dosku so zapnutým podsvietením často neutiahne. Ak sa
    doska reštartuje, keď sa rozsvieti obrazovka, použi zdroj 5 V / 2 A
    alebo napájaný USB hub.

## Mapa pinov

![Makerfabs MaTouch ESP32-P4 7" - mapa pinov](pinout/pinout.png)

| GPIO | Funkcia v ctrl32 | Poznámka |
|---|---|---|
| 0 | RTC XTAL P | ⚠  |
| 1 | RTC XTAL N | ⚠  |
| 2 | voľný I/O |  |
| 3 | voľný I/O |  |
| 4 | voľný I/O |  |
| 5 | voľný I/O |  |
| 6 | C6 IO2 | ⚠  |
| 7 | TOUCH SDA |  |
| 8 | TOUCH SCL |  |
| 20 | voľný I/O |  |
| 21 | voľný I/O |  |
| 22 | TOUCH RST |  |
| 23 | TFT BL |  |
| 26 | USB1 PAIR | ⚠  |
| 27 | DSI RST |  |
| 28 | Ethernet RMII (IP101GRI) | ⚠ používa doska |
| 29 | Ethernet RMII (IP101GRI) | ⚠ používa doska |
| 30 | Ethernet RMII (IP101GRI) | ⚠ používa doska |
| 31 | Ethernet MDC (IP101GRI) | ⚠ používa doska |
| 32 | voľný I/O |  |
| 33 | voľný I/O |  |
| 34 | Ethernet RMII (IP101GRI) | ⚠ používa doska |
| 35 | Ethernet RMII (IP101GRI) | ⚠ používa doska |
| 36 | voľný I/O | ⚠ strapping pin |
| 37 | CONSOLE RX | ⚠ strapping pin |
| 38 | CONSOLE TX | ⚠ strapping pin |
| 45 | MOSFET GATE | ⚠  |
| 46 | voľný I/O |  |
| 47 | voľný I/O |  |
| 48 | voľný I/O |  |
| 49 | Ethernet RMII (IP101GRI) | ⚠ používa doska |
| 50 | Ethernet RMII (IP101GRI) | ⚠ používa doska |
| 51 | Ethernet PHY reset (IP101GRI) | ⚠ používa doska |
| 52 | Ethernet MDIO (IP101GRI) | ⚠ používa doska |
| 53 | AMP EN | ⚠  |
| 54 | C6 EN | ⚠  |

Voľné piny sú na konektoroch **J6** a **J10** a na dvoch konektoroch Grove
(**J1**, **J2**). Zbernica I2C dosky (GPIO7 / GPIO8) nesie radič dotyku a
audio kodek; ďalšie čipy I2C (ADS1115, senzor) sa pripoja na tú istú
zbernicu. CAN ani RS-485 nemajú na doske prevodník: príklad ich dáva na
voľné piny - **CAN** TX GPIO20 / RX GPIO21 (Grove J2), **RS-485** TX GPIO4
/ RX GPIO5 / DE GPIO32 (J10) - každú na 3,3 V modul prevodníka.

## Bezpečnosť

- Doska nie je určená na bezpečnostné funkcie. Núdzové zastavenie, dverový
  spínač či svetelná závora sa zapájajú v hardvéri, nikdy cez program
  alebo dotykovú obrazovku.
- Piny GPIO majú 3,3 V. Signál 24 V potrebuje optočlen; cievka relé
  potrebuje budič (reléový modul ho má).
- Kapacitný dotyk môže pri silnom zdroji rušenia (menič) zaznamenať
  falošné stlačenie. Kritické príkazy na obrazovke si pýtajú potvrdenie.

## Fotky

![Makerfabs MaTouch ESP32-P4 7" - fotka 1](img/board-01.jpg)
![Makerfabs MaTouch ESP32-P4 7" - fotka 2](img/board-02.jpg)
![Makerfabs MaTouch ESP32-P4 7" - fotka 3](img/board-03.jpg)
![Makerfabs MaTouch ESP32-P4 7" - fotka 4](img/board-04.jpg)
![Makerfabs MaTouch ESP32-P4 7" - fotka 5](img/board-05.jpg)
![Makerfabs MaTouch ESP32-P4 7" - fotka 6](img/board-06.jpg)
![Makerfabs MaTouch ESP32-P4 7" - fotka 7](img/board-07.jpg)
![Makerfabs MaTouch ESP32-P4 7" - fotka 8](img/board-08.jpg)

---

[← Prehľad](README.sk.md) | [Prehľad](README.sk.md) | [Nahratie runtime →](install.sk.md)
