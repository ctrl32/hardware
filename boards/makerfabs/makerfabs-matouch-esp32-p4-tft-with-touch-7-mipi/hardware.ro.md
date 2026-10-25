---
title: 'Makerfabs MaTouch ESP32-P4 7": hardware și cablare'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Makerfabs MaTouch ESP32-P4 7" - harta pinilor
tags:
- esp32-p4
- display
- touch
- hmi
- ethernet
- makerfabs
---

# Hardware și cablare

## De ce ai nevoie

- Makerfabs MaTouch ESP32-P4 TFT with Touch 7" MIPI.
- Un cablu de date USB-C - pentru prima încărcare a runtime-ului și pentru alimentare.
- Pentru alimentare: o sursă USB-C de 5 V de cel puțin 2 A (iluminarea de fundal a display-ului consumă cea mai mare parte).
- Un cablu Ethernet sau Wi-Fi-ul rețelei tale.
- Un PC cu [editorul ctrl32](https://ctrl32.com/download/) (Windows).
- Opțional, pentru exemplul all-in-one: două butoane și un modul de releu pe conectorul J6; un modul ADS1115 pe magistrala I2C; un transceiver RS-485 de 3,3 V (de ex. MAX3485) și un transceiver CAN de 3,3 V (de ex. SN65HVD230).

## Alimentare

| Sursă | Unde | Notă |
|---|---|---|
| USB 5 V | conectorul USB-C | 2 A sau mai mult - iluminarea de fundal de 7" consumă cea mai mare parte |
| Acumulator Li-Po | conectorul de acumulator | 3,7 V, încărcat pe placă |

!!! warning "O sursă slabă"
    Portul USB al unui PC adesea nu poate duce placa cu iluminarea de
    fundal pornită. Dacă placa repornește când apare ecranul, folosește o
    sursă de 5 V / 2 A sau un hub USB alimentat.

## Harta pinilor

![Makerfabs MaTouch ESP32-P4 7" - harta pinilor](pinout/pinout.png)

| GPIO | Funcție în ctrl32 | Notă |
|---|---|---|
| 0 | RTC XTAL P | ⚠  |
| 1 | RTC XTAL N | ⚠  |
| 2 | liber - I/O |  |
| 3 | liber - I/O |  |
| 4 | liber - I/O |  |
| 5 | liber - I/O |  |
| 6 | C6 IO2 | ⚠  |
| 7 | TOUCH SDA |  |
| 8 | TOUCH SCL |  |
| 20 | liber - I/O |  |
| 21 | liber - I/O |  |
| 22 | TOUCH RST |  |
| 23 | TFT BL |  |
| 26 | USB1 PAIR | ⚠  |
| 27 | DSI RST |  |
| 28 | Ethernet RMII (IP101GRI) | ⚠ folosit de placă |
| 29 | Ethernet RMII (IP101GRI) | ⚠ folosit de placă |
| 30 | Ethernet RMII (IP101GRI) | ⚠ folosit de placă |
| 31 | Ethernet MDC (IP101GRI) | ⚠ folosit de placă |
| 32 | liber - I/O |  |
| 33 | liber - I/O |  |
| 34 | Ethernet RMII (IP101GRI) | ⚠ folosit de placă |
| 35 | Ethernet RMII (IP101GRI) | ⚠ folosit de placă |
| 36 | liber - I/O | ⚠ pin de strapping |
| 37 | CONSOLE RX | ⚠ pin de strapping |
| 38 | CONSOLE TX | ⚠ pin de strapping |
| 45 | MOSFET GATE | ⚠  |
| 46 | liber - I/O |  |
| 47 | liber - I/O |  |
| 48 | liber - I/O |  |
| 49 | Ethernet RMII (IP101GRI) | ⚠ folosit de placă |
| 50 | Ethernet RMII (IP101GRI) | ⚠ folosit de placă |
| 51 | Ethernet PHY reset (IP101GRI) | ⚠ folosit de placă |
| 52 | Ethernet MDIO (IP101GRI) | ⚠ folosit de placă |
| 53 | AMP EN | ⚠  |
| 54 | C6 EN | ⚠  |

Pinii liberi se află pe conectorii **J6** și **J10** și pe cei doi
conectori Grove (**J1**, **J2**). Magistrala I2C a plăcii (GPIO7 / GPIO8)
poartă controlerul de touch și codecul audio; alte cipuri I2C (un ADS1115,
un senzor) se conectează pe aceeași magistrală. CAN și RS-485 nu au
transceiver pe placă: exemplul le pune pe pini liberi - **CAN** TX GPIO20 /
RX GPIO21 (Grove J2), **RS-485** TX GPIO4 / RX GPIO5 / DE GPIO32 (J10) -
fiecare la un modul transceiver de 3,3 V.

## Siguranță

- Placa nu este destinată funcțiilor de siguranță. O oprire de urgență,
  un contact de ușă sau o barieră optică se cablează în hardware,
  niciodată printr-un program sau un ecran tactil.
- Pinii GPIO sunt de 3,3 V. Un semnal de 24 V are nevoie de un
  optocuplor; o bobină de releu are nevoie de un driver (un modul de releu
  are unul).
- Touch-ul capacitiv poate înregistra o apăsare falsă lângă o sursă
  puternică de interferențe (o acționare). Comenzile critice de pe un
  ecran cer o confirmare.

## Fotografii

![Makerfabs MaTouch ESP32-P4 7" - fotografia 1](img/board-01.jpg)
![Makerfabs MaTouch ESP32-P4 7" - fotografia 2](img/board-02.jpg)
![Makerfabs MaTouch ESP32-P4 7" - fotografia 3](img/board-03.jpg)
![Makerfabs MaTouch ESP32-P4 7" - fotografia 4](img/board-04.jpg)
![Makerfabs MaTouch ESP32-P4 7" - fotografia 5](img/board-05.jpg)
![Makerfabs MaTouch ESP32-P4 7" - fotografia 6](img/board-06.jpg)
![Makerfabs MaTouch ESP32-P4 7" - fotografia 7](img/board-07.jpg)
![Makerfabs MaTouch ESP32-P4 7" - fotografia 8](img/board-08.jpg)

---

[← Prezentare](README.ro.md) | [Prezentare](README.ro.md) | [Instalarea runtime-ului →](install.ro.md)
