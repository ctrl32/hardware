---
title: 'Olimex ESP32-PoE-ISO: hardver és bekötés'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-PoE-ISO - lábkiosztás
tags:
- esp32
- ethernet
- poe
- isolated
- olimex
---

# Hardver és bekötés

## Amire szükséged van

- Az Olimex ESP32-PoE-ISO (a WROOM-32E változat, PSRAM nélkül).
- Egy micro-USB adatkábel - a runtime első feltöltéséhez.
- Tápellátáshoz: egy PoE switch / injektor (IEEE 802.3af) vagy egy 5 V-os USB tápegység.
- Egy Ethernet-kábel és egy szabad port a hálózatodon.
- Egy PC a [ctrl32 szerkesztővel](https://ctrl32.com/download/) (Windows).
- Opcionálisan, az all-in-one példához: a BUT1 gomb a panelen van; egy relémodul vagy egy LED ellenállással a GPIO4-en (UEXT); egy potenciométer (10 k) a 3,3 V és a GND között, a csúszkája a GPIO33-on (EXT2); egy 3,3 V-os CAN adó-vevő a GPIO5 (TX) / GPIO36 (RX) lábon.

## Tápellátás

| Forrás | Hol | Megjegyzés |
|---|---|---|
| PoE | az Ethernet aljzat, PoE switchről vagy injektorról | IEEE 802.3af, leválasztott |
| USB 5 V | a micro-USB csatlakozó | az első feltöltés útja |
| Li-Po akkumulátor | az akkumulátor-csatlakozó | a panelen töltődik |

A PoE táp **galvanikusan le van választva** a panelről: a sima
ESP32-PoE-vel ellentétben a PC felé menő USB és a PoE egyszerre is
csatlakoztatható - a runtime feltölthető és online figyelhető, miközben a
panel a PoE switchén marad.

## Lábkiosztás

![Olimex ESP32-PoE-ISO - lábkiosztás](pinout/pinout.png)

| GPIO | Funkció a ctrl32-ben | Megjegyzés |
|---|---|---|
| 2 | SPI MOSI | ⚠ strapping láb |
| 4 | free (UART TX line) |  |
| 5 | free (SPI CS line) |  |
| 6 | a modul SPI flash memóriája | ⚠ a panel használja |
| 7 | a modul SPI flash memóriája | ⚠ a panel használja |
| 8 | a modul SPI flash memóriája | ⚠ a panel használja |
| 9 | a modul SPI flash memóriája | ⚠ a panel használja |
| 10 | a modul SPI flash memóriája | ⚠ a panel használja |
| 11 | a modul SPI flash memóriája | ⚠ a panel használja |
| 12 | Ethernet PHY power (LAN8710A) | ⚠ a panel használja |
| 13 | I2C SDA |  |
| 14 | SPI SCLK |  |
| 15 | SPI MISO | ⚠ strapping láb |
| 16 | I2C SCL |  |
| 17 | Ethernet 50 MHz clock (LAN8710A) | ⚠ a panel használja |
| 18 | Ethernet MDIO (LAN8710A) | ⚠ a panel használja |
| 19 | Ethernet RMII TXD0 (LAN8710A) | ⚠ a panel használja |
| 21 | Ethernet RMII TX_EN (LAN8710A) | ⚠ a panel használja |
| 22 | Ethernet RMII TXD1 (LAN8710A) | ⚠ a panel használja |
| 23 | Ethernet MDC (LAN8710A) | ⚠ a panel használja |
| 25 | Ethernet RMII RXD0 (LAN8710A) | ⚠ a panel használja |
| 26 | Ethernet RMII RXD1 (LAN8710A) | ⚠ a panel használja |
| 27 | Ethernet RMII CRS_DV (LAN8710A) | ⚠ a panel használja |
| 33 | szabad - I/O | ADC1 |
| 34 | szabad - a panel gombja | ⚠ csak bemenet, ADC1 |
| 35 | szabad - bemenet | ⚠ csak bemenet, ADC1 |
| 36 | free (UART RX line) | ⚠ csak bemenet, ADC1 |

A szabad lábak az **EXT1 / EXT2** tüskesorokon (2,54 mm) és az **UEXT**
csatlakozón vannak. A GPIO34-GPIO39 csak bemenet - az ottani kimenetet a
szerkesztő elutasítja. Az UEXT csatlakozó I2C-t (GPIO13 / GPIO16) és SPI-t
(GPIO14 / GPIO2 / GPIO15, a microSD foglalattal közösen) visz.

## Biztonság

- A panel nem biztonsági funkciókra készült. A vészleállítót, az
  ajtókapcsolót vagy a fényfüggönyt hardveresen kell bekötni, soha nem
  programon keresztül.
- A GPIO lábak 3,3 V-osak. Egy 24 V-os bemenethez optocsatoló vagy
  szintillesztő kell; egy relétekercshez meghajtó kell (egy relémodulon
  van ilyen).

---

[← Áttekintés](README.hu.md) | [Áttekintés](README.hu.md) | [A runtime telepítése →](install.hu.md)
