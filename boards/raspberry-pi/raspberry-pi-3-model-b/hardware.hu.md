---
title: 'Raspberry Pi 3 Model B+: hardver és bekötés'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Raspberry Pi 3 Model B+ - lábkiosztás
tags:
- raspberry-pi
- linux
- hmi
- opc-ua
---

# Hardver és bekötés

## Amire szükséged van

- Egy Raspberry Pi 3 Model B+.
- Egy microSD kártya (16 GB vagy több) és a [Raspberry Pi Imager](https://www.raspberrypi.com/software/).
- Egy 5 V / 2,5 A-es micro-USB tápegység.
- Egy Ethernet-kábel ugyanazon a hálózaton, mint a PC.
- A HMI-hez: egy HDMI monitor (teljes méretű HDMI) vagy egy DSI kijelző; érintőmonitornál annak USB-je is.
- Egy PC a [ctrl32 szerkesztővel](https://ctrl32.com/download/) (Windows).
- Opcionálisan, az all-in-one példához: egy USB-RS485 adapter egy Modbus RTU I/O modullal és egy hőmérséklet-érzékelővel; egy CAN HAT (MCP2515).

## Tápellátás

| Forrás | Hol | Megjegyzés |
|---|---|---|
| micro-USB | a tápcsatlakozó | 5 V / 2,5 A |
| PoE | PoE HAT-on keresztül | opcionális |

!!! warning "Alacsony feszültség"
    Gyengébb tápegységgel a Pi visszafogja magát és korlátozza az USB
    áramot - ilyenkor egy USB-RS485 adapter vagy egy érintőmonitor
    kieshet.

## Lábkiosztás

![Raspberry Pi 3 Model B+ - lábkiosztás](pinout/pinout.png)

| GPIO | Funkció a ctrl32-ben | Megjegyzés |
|---|---|---|
| 2 | I2C1 SDA - I2C chipek, RTC |  |
| 3 | I2C1 SCL |  |
| 4 | szabad - a ctrl32 nem használja | ⚠  |
| 8 | SPI0 CE0 - CAN HAT |  |
| 9 | SPI0 MISO - CAN HAT |  |
| 10 | SPI0 MOSI - CAN HAT |  |
| 11 | SPI0 SCLK - CAN HAT |  |
| 14 | UART TX - RS-485 HAT |  |
| 15 | UART RX - RS-485 HAT |  |
| 17 | szabad - a ctrl32 nem használja | ⚠  |
| 22 | szabad - a ctrl32 nem használja | ⚠  |
| 25 | A CAN HAT megszakítása (MCP2515) |  |
| 27 | szabad - a ctrl32 nem használja | ⚠  |

Linux panelen a buszok **eszköznevek**, nem lábak: a runtime azt nyitja
meg, amit az eszköz beállításai megneveznek - `can0` egy CAN HAT-hoz vagy
USB adapterhez, `/dev/ttyUSB0` egy USB-RS485 adapterhez (vagy a Pi saját
UART-ja egy RS-485 HAT-tal). A **Prepare a Linux device** állítja be őket
(a telepítés 3. lépése). Az EtherCAT-hez szükséges második Ethernet port
egy USB Ethernet adapter.

## Biztonság

- A panel nem biztonsági funkciókra készült. A vészleállítót, az
  ajtókapcsolót vagy a fényfüggönyt hardveresen kell bekötni, soha nem
  programon keresztül.
- Ahol lehet, állítsd le a Pi-t, mielőtt elveszed a tápját - a runtime
  biztonságban tartja a megőrzött értékeket, az operációs rendszer
  viszont a tiszta leállítást szereti.

---

[← Áttekintés](README.hu.md) | [Áttekintés](README.hu.md) | [A runtime telepítése →](install.hu.md)
