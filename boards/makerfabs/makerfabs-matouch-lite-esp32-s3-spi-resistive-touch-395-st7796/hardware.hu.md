---
title: 'Makerfabs MaTouch Lite ESP32-S3 3.95": hardver és bekötés'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Makerfabs MaTouch Lite ESP32-S3 3.95" - lábkiosztás
tags:
- esp32-s3
- display
- touch
- hmi
- wifi
- makerfabs
---

# Hardver és bekötés

## Amire szükséged van

- A Makerfabs MaTouch Lite ESP32-S3 3,95" (ST7796).
- Egy USB-C adatkábel - a feltöltéshez és a tápellátáshoz.
- A 2,4 GHz-es Wi-Fi-hálózatod neve és jelszava.
- Egy PC a [ctrl32 szerkesztővel](https://ctrl32.com/download/) (Windows).
- Opcionálisan, az all-in-one példához: egy relémodul vagy egy LED a GPIO4-en, egy potenciométer (10 k) a 3,3 V és a GND között, a csúszkája a GPIO5-ön (a JST csatlakozók), és egy 3,3 V-os CAN adó-vevő (pl. SN65HVD230) a GPIO6 / GPIO7 lábon.

## Tápellátás

| Forrás | Hol | Megjegyzés |
|---|---|---|
| USB 5 V | az USB-C csatlakozó | tápellátás és programozás |
| Li-Po akkumulátor | az akkumulátor-csatlakozó | 3,7 V |

## Lábkiosztás

![Makerfabs MaTouch Lite ESP32-S3 3.95" - lábkiosztás](pinout/pinout.png)

| GPIO | Funkció a ctrl32-ben | Megjegyzés |
|---|---|---|
| 0 | BOOT BTN | ⚠ strapping láb |
| 1 | TFT RST |  |
| 2 | SD CMD | ⚠  |
| 4 | szabad - I/O | ADC1 |
| 5 | szabad - I/O | ADC1 |
| 6 | szabad - I/O | ADC1 |
| 7 | szabad - I/O | ADC1 |
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

A két **JST** csatlakozó viszi a négy szabad lábat (GPIO4-GPIO7) - kevés
van belőlük, ezért a példa a kimenetet, az analóg bemenetet és a CAN-t
teszi rájuk; a további I/O Modbus TCP-n vagy I2C chipeken keresztül megy. A
kijelző, az érintésvezérlő és a microSD foglalat foglalja a többi lábat.

## Biztonság

- A panel nem biztonsági funkciókra készült. A vészleállítót, az
  ajtókapcsolót vagy a fényfüggönyt hardveresen kell bekötni, soha nem
  programon vagy érintőképernyőn keresztül.
- A GPIO lábak 3,3 V-osak. Egy relétekercshez meghajtó kell (egy relémodulon van ilyen).

---

[← Áttekintés](README.hu.md) | [Áttekintés](README.hu.md) | [A runtime telepítése →](install.hu.md)
