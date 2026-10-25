---
title: 'Makerfabs MaTouch ESP32-P4 7": hardver és bekötés'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Makerfabs MaTouch ESP32-P4 7" - lábkiosztás
tags:
- esp32-p4
- display
- touch
- hmi
- ethernet
- makerfabs
---

# Hardver és bekötés

## Amire szükséged van

- A Makerfabs MaTouch ESP32-P4 TFT with Touch 7" MIPI.
- Egy USB-C adatkábel - a runtime első feltöltéséhez és a tápellátáshoz.
- Tápellátáshoz: egy legalább 2 A-es 5 V-os USB-C tápegység (a legtöbbet a kijelző háttérvilágítása veszi fel).
- Egy Ethernet-kábel vagy a hálózatod Wi-Fi-je.
- Egy PC a [ctrl32 szerkesztővel](https://ctrl32.com/download/) (Windows).
- Opcionálisan, az all-in-one példához: két nyomógomb és egy relémodul a J6 tüskesoron; egy ADS1115 modul az I2C buszon; egy 3,3 V-os RS-485 adó-vevő (pl. MAX3485) és egy 3,3 V-os CAN adó-vevő (pl. SN65HVD230).

## Tápellátás

| Forrás | Hol | Megjegyzés |
|---|---|---|
| USB 5 V | az USB-C csatlakozó | 2 A vagy több - a legtöbbet a 7"-os háttérvilágítás veszi fel |
| Li-Po akkumulátor | az akkumulátor-csatlakozó | 3,7 V, a panelen töltődik |

!!! warning "Gyenge tápegység"
    Egy PC USB portja gyakran nem bírja el a panelt bekapcsolt
    háttérvilágítással. Ha a panel újraindul, amikor a képernyő
    megjelenik, használj 5 V / 2 A-es tápegységet vagy saját tápos USB
    hubot.

## Lábkiosztás

![Makerfabs MaTouch ESP32-P4 7" - lábkiosztás](pinout/pinout.png)

| GPIO | Funkció a ctrl32-ben | Megjegyzés |
|---|---|---|
| 0 | RTC XTAL P | ⚠  |
| 1 | RTC XTAL N | ⚠  |
| 2 | szabad - I/O |  |
| 3 | szabad - I/O |  |
| 4 | szabad - I/O |  |
| 5 | szabad - I/O |  |
| 6 | C6 IO2 | ⚠  |
| 7 | TOUCH SDA |  |
| 8 | TOUCH SCL |  |
| 20 | szabad - I/O |  |
| 21 | szabad - I/O |  |
| 22 | TOUCH RST |  |
| 23 | TFT BL |  |
| 26 | USB1 PAIR | ⚠  |
| 27 | DSI RST |  |
| 28 | Ethernet RMII (IP101GRI) | ⚠ a panel használja |
| 29 | Ethernet RMII (IP101GRI) | ⚠ a panel használja |
| 30 | Ethernet RMII (IP101GRI) | ⚠ a panel használja |
| 31 | Ethernet MDC (IP101GRI) | ⚠ a panel használja |
| 32 | szabad - I/O |  |
| 33 | szabad - I/O |  |
| 34 | Ethernet RMII (IP101GRI) | ⚠ a panel használja |
| 35 | Ethernet RMII (IP101GRI) | ⚠ a panel használja |
| 36 | szabad - I/O | ⚠ strapping láb |
| 37 | CONSOLE RX | ⚠ strapping láb |
| 38 | CONSOLE TX | ⚠ strapping láb |
| 45 | MOSFET GATE | ⚠  |
| 46 | szabad - I/O |  |
| 47 | szabad - I/O |  |
| 48 | szabad - I/O |  |
| 49 | Ethernet RMII (IP101GRI) | ⚠ a panel használja |
| 50 | Ethernet RMII (IP101GRI) | ⚠ a panel használja |
| 51 | Ethernet PHY reset (IP101GRI) | ⚠ a panel használja |
| 52 | Ethernet MDIO (IP101GRI) | ⚠ a panel használja |
| 53 | AMP EN | ⚠  |
| 54 | C6 EN | ⚠  |

A szabad lábak a **J6** és **J10** tüskesorokon és a két Grove
csatlakozón (**J1**, **J2**) vannak. A panel I2C busza (GPIO7 / GPIO8)
viszi az érintésvezérlőt és az audiokodeket; további I2C chipek (egy
ADS1115, egy érzékelő) ugyanarra a buszra kerülnek. A CAN-nak és az
RS-485-nek nincs adó-vevője a panelen: a példa szabad lábakra teszi őket -
**CAN** TX GPIO20 / RX GPIO21 (Grove J2), **RS-485** TX GPIO4 / RX GPIO5 /
DE GPIO32 (J10) - mindegyiket egy 3,3 V-os adó-vevő modulhoz.

## Biztonság

- A panel nem biztonsági funkciókra készült. A vészleállítót, az
  ajtókapcsolót vagy a fényfüggönyt hardveresen kell bekötni, soha nem
  programon vagy érintőképernyőn keresztül.
- A GPIO lábak 3,3 V-osak. Egy 24 V-os jelhez optocsatoló kell; egy
  relétekercshez meghajtó kell (egy relémodulon van ilyen).
- A kapacitív érintés egy erős zavarforrás (egy hajtás) mellett hamis
  érintést érzékelhet. A kritikus parancsok a képernyőn megerősítést
  kérnek.

## Fotók

![Makerfabs MaTouch ESP32-P4 7" - 1. fotó](img/board-01.jpg)
![Makerfabs MaTouch ESP32-P4 7" - 2. fotó](img/board-02.jpg)
![Makerfabs MaTouch ESP32-P4 7" - 3. fotó](img/board-03.jpg)
![Makerfabs MaTouch ESP32-P4 7" - 4. fotó](img/board-04.jpg)
![Makerfabs MaTouch ESP32-P4 7" - 5. fotó](img/board-05.jpg)
![Makerfabs MaTouch ESP32-P4 7" - 6. fotó](img/board-06.jpg)
![Makerfabs MaTouch ESP32-P4 7" - 7. fotó](img/board-07.jpg)
![Makerfabs MaTouch ESP32-P4 7" - 8. fotó](img/board-08.jpg)

---

[← Áttekintés](README.hu.md) | [Áttekintés](README.hu.md) | [A runtime telepítése →](install.hu.md)
