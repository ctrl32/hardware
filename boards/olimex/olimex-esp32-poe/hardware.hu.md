---
title: 'Olimex ESP32-PoE: hardver és bekötés'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-PoE - lábkiosztás
tags:
- esp32
- ethernet
- poe
- olimex
---

# Hardver és bekötés

## Amire szükséged van

- Az Olimex ESP32-PoE (a WROOM-32E változat, PSRAM nélkül).
- Egy micro-USB adatkábel - a runtime első feltöltéséhez.
- Tápellátáshoz: egy 5 V-os USB tápegység vagy egy PoE switch / injektor (IEEE 802.3af).
- Egy Ethernet-kábel és egy szabad port a hálózatodon.
- Egy PC a [ctrl32 szerkesztővel](https://ctrl32.com/download/) (Windows).
- Opcionálisan, az all-in-one példához: egy nyomógomb a panelen van (BUT1); egy relémodul vagy egy LED ellenállással a GPIO33-on; egy potenciométer (10 k) a 3,3 V és a GND között, a csúszkája a GPIO35-ön; egy 3,3 V-os CAN adó-vevő (pl. SN65HVD230) az UEXT csatlakozó GPIO4 (TX) / GPIO36 (RX) lábán.

## Tápellátás

A panel három forrás egyikéből kapja a tápját:

| Forrás | Hol | Megjegyzés |
|---|---|---|
| USB 5 V | a micro-USB csatlakozó | az első feltöltés útja |
| PoE | az Ethernet aljzat, PoE switchről vagy injektorról | IEEE 802.3af |
| Li-Po akkumulátor | az akkumulátor-csatlakozó | a panelen töltődik |

!!! danger "Soha ne csatlakoztasd egyszerre az USB-t és a PoE-t"
    Az ESP32-PoE **nincs galvanikusan leválasztva**. Amíg a panel PoE-ről
    kap tápot, a földje a PoE tápot követi - ilyenkor egy a PC-dhez menő
    USB-kábelen károsító áram folyhat. A runtime-ot USB-n töltsd fel
    **kihúzott** Ethernet-kábellel (vagy egy PoE nélküli portról), és csak
    utána üzemeltesd a panelt PoE-ről. Ahol egy PC-nek csatlakoztatva kell
    maradnia, miközben a panel PoE-n van, használd az
    ESP32-PoE-ISO panelt.

## Lábkiosztás

![Olimex ESP32-PoE - lábkiosztás](pinout/pinout.png)

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
