---
title: 'Olimex ESP32-DevKit-LiPo: hardware și cablare'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-DevKit-LiPo - harta pinilor
tags:
- esp32
- wifi
- battery
- olimex
---

# Hardware și cablare

## De ce ai nevoie

- Olimex ESP32-DevKit-LiPo.
- Un cablu de date micro-USB - pentru încărcare și pentru alimentare (5 V).
- Numele și parola rețelei tale Wi-Fi de 2,4 GHz.
- Un PC cu [editorul ctrl32](https://ctrl32.com/download/) (Windows).
- Opțional, pentru exemplul all-in-one: un buton de la GPIO13 la GND; un modul de releu sau un LED cu rezistor pe GPIO4; un potențiometru (10 k) între 3,3 V și GND cu cursorul pe GPIO32; un transceiver CAN de 3,3 V pe GPIO14 / GPIO34 și un transceiver RS-485 pe GPIO16 / GPIO36 / GPIO17 (DE); o celulă Li-Po ca rezervă.

## Alimentare

| Sursă | Unde | Notă |
|---|---|---|
| USB 5 V | conectorul micro-USB | alimentare și programare |
| Acumulator Li-Po | conectorul de acumulator | încărcat pe placă, preia când pică USB |

## Harta pinilor

![Olimex ESP32-DevKit-LiPo - harta pinilor](pinout/pinout.png)

| GPIO | Funcție în ctrl32 | Notă |
|---|---|---|
| 4 | liber - I/O |  |
| 6 | Flash SPI al modulului | ⚠ folosit de placă |
| 7 | Flash SPI al modulului | ⚠ folosit de placă |
| 8 | Flash SPI al modulului | ⚠ folosit de placă |
| 9 | Flash SPI al modulului | ⚠ folosit de placă |
| 10 | Flash SPI al modulului | ⚠ folosit de placă |
| 11 | Flash SPI al modulului | ⚠ folosit de placă |
| 13 | liber - I/O |  |
| 14 | liber - I/O |  |
| 16 | liber - I/O |  |
| 17 | liber - I/O |  |
| 18 | liber - I/O |  |
| 19 | liber - I/O |  |
| 21 | liber - I/O |  |
| 22 | liber - I/O |  |
| 23 | liber - I/O |  |
| 25 | liber - I/O |  |
| 26 | liber - I/O |  |
| 27 | liber - I/O |  |
| 32 | liber - I/O | ADC1 |
| 33 | liber - I/O | ADC1 |
| 34 | liber - intrare | ⚠ doar intrare, ADC1 |
| 35 | free (BAT SENSE line) | ⚠ doar intrare, ADC1 |
| 36 | liber - intrare | ⚠ doar intrare, ADC1 |
| 39 | free (PWR SENSE line) | ⚠ doar intrare, ADC1 |

Cei doi conectori poartă GPIO-urile libere ale modulului. GPIO34 până la
GPIO39 sunt doar intrări; GPIO0, 2, 12 și 15 sunt pini de strapping -
lasă-i pentru intrări sau testează-i înainte de a-i folosi. Un buton la
GND nu are nevoie de rezistor: ctrl32 îl citește inversat cu pull-up-ul
cipului.

## Siguranță

- Placa nu este destinată funcțiilor de siguranță. O oprire de urgență,
  un contact de ușă sau o barieră optică se cablează în hardware, niciodată
  printr-un program.
- Pinii GPIO sunt de 3,3 V. Un semnal de 24 V are nevoie de un optocuplor
  sau de un convertor de nivel; o bobină de releu are nevoie de un driver
  (un modul de releu are unul).

---

[← Prezentare](README.ro.md) | [Prezentare](README.ro.md) | [Instalarea runtime-ului →](install.ro.md)
