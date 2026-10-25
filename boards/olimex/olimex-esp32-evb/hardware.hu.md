---
title: 'Olimex ESP32-EVB: hardver és bekötés'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-EVB - lábkiosztás
tags:
- esp32
- ethernet
- can
- relay
- olimex
---

# Hardver és bekötés

## Amire szükséged van

- Az Olimex ESP32-EVB.
- Egy micro-USB adatkábel - a runtime első feltöltéséhez.
- Tápellátáshoz: egy 5 V-os USB tápegység vagy 5 V a csavaros sorkapcson.
- Egy Ethernet-kábel és egy szabad port a hálózatodon.
- Egy PC a [ctrl32 szerkesztővel](https://ctrl32.com/download/) (Windows).
- Opcionálisan, az all-in-one példához: egy potenciométer (10 k) a 3,3 V és a GND között, a csúszkája a GPIO36-on (UEXT); egy CAN csomópont vagy egy CAN adapter és két 120 ohmos lezáró.
- Opcionálisan: az Olimex MOD-LCD2.8RTP kijelző (2,8 hüvelyk, 240 x 320, rezisztív érintés) az UEXT csatlakozón.

## Tápellátás

| Forrás | Hol | Megjegyzés |
|---|---|---|
| USB 5 V | a micro-USB csatlakozó | az első feltöltés útja |
| 5 V DC | a csavaros sorkapocs | kapcsolószekrényhez |
| Li-Po akkumulátor | az akkumulátor-csatlakozó | a panelen töltődik |

!!! warning "A relék hálózati feszültséget kapcsolnak"
    A relé érintkezőit csak feszültségmentes panelnél, burkolatban, és
    csak hálózati berendezéseken dolgozni jogosult személy kösse be. Az
    érintkezők 10 A / 250 VAC-t bírnak; ennél nagyobb motorhoz vagy
    fűtőtesthez a relé által vezérelt mágneskapcsoló kell.

## Lábkiosztás

![Olimex ESP32-EVB - lábkiosztás](pinout/pinout.png)

| GPIO | Funkció a ctrl32-ben | Megjegyzés |
|---|---|---|
| 0 | Ethernet 50 MHz clock (LAN8710A) | ⚠ a panel használja |
| 2 | TFT MOSI | ⚠ strapping láb |
| 2 | SPI MOSI | ⚠ strapping láb |
| 4 | free (UART TX line) |  |
| 5 | CAN TX |  |
| 6 | a modul SPI flash memóriája | ⚠ a panel használja |
| 7 | a modul SPI flash memóriája | ⚠ a panel használja |
| 8 | a modul SPI flash memóriája | ⚠ a panel használja |
| 9 | a modul SPI flash memóriája | ⚠ a panel használja |
| 10 | a modul SPI flash memóriája | ⚠ a panel használja |
| 11 | a modul SPI flash memóriája | ⚠ a panel használja |
| 13 | I2C SDA |  |
| 14 | TFT SCLK |  |
| 14 | SPI SCLK |  |
| 15 | TFT DC | ⚠ strapping láb |
| 15 | SPI MISO | ⚠ strapping láb |
| 16 | I2C SCL |  |
| 17 | TFT CS |  |
| 17 | free (SPI CS line) |  |
| 18 | Ethernet MDIO (LAN8710A) | ⚠ a panel használja |
| 19 | Ethernet RMII TXD0 (LAN8710A) | ⚠ a panel használja |
| 21 | Ethernet RMII TX_EN (LAN8710A) | ⚠ a panel használja |
| 22 | Ethernet RMII TXD1 (LAN8710A) | ⚠ a panel használja |
| 23 | Ethernet MDC (LAN8710A) | ⚠ a panel használja |
| 25 | Ethernet RMII RXD0 (LAN8710A) | ⚠ a panel használja |
| 26 | Ethernet RMII RXD1 (LAN8710A) | ⚠ a panel használja |
| 27 | Ethernet RMII CRS_DV (LAN8710A) | ⚠ a panel használja |
| 32 | free (REL1 line) | ADC1 |
| 33 | free (REL2 line) | ADC1 |
| 34 | szabad - a panel gombja | ⚠ csak bemenet, ADC1 |
| 35 | CAN RX |  |
| 36 | free (UART RX line) | ⚠ csak bemenet, ADC1 |

**Relék:** REL1 a GPIO32-n, REL2 a GPIO33-on. **Gomb:** BUT1 a GPIO34-en
(csak bemenet). **CAN:** a panelen lévő adó-vevő a GPIO5 (TX) / GPIO35 (RX)
lábon, a CAN_H / CAN_L a sorkapcson - zárd le a buszt mindkét végén
120 ohmmal. Az **UEXT** csatlakozó I2C-t (GPIO13 / GPIO16), SPI-t és egy
szabad UART-ot (GPIO4 / GPIO36) visz; az opcionális kijelző az SPI vonalait
használja.

## Biztonság

- A panel nem biztonsági funkciókra készült. A vészleállítót, az
  ajtókapcsolót vagy a fényfüggönyt hardveresen kell bekötni, soha nem
  programon keresztül.
- A GPIO lábak 3,3 V-osak. Egy 24 V-os jelhez optocsatoló vagy
  szintillesztő kell; egy relétekercshez meghajtó kell (egy relémodulon
  van ilyen).

---

[← Áttekintés](README.hu.md) | [Áttekintés](README.hu.md) | [A runtime telepítése →](install.hu.md)
