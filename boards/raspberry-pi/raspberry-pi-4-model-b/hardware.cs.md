---
title: 'Raspberry Pi 4 Model B: hardware a zapojení'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Raspberry Pi 4 Model B - mapa pinů
tags:
- raspberry-pi
- linux
- hmi
- opc-ua
- ethercat
---

# Hardware a zapojení

## Co je potřeba

- Raspberry Pi 4 Model B (doporučeno 2 GB a více).
- Karta microSD (16 GB a více) a [Raspberry Pi Imager](https://www.raspberrypi.com/software/).
- Oficiální zdroj USB-C (5 V / 3 A).
- Síťový kabel ve stejné síti jako PC.
- Pro HMI: monitor HDMI (kabel micro-HDMI) nebo displej DSI; u dotykového monitoru i jeho USB.
- PC s [editorem ctrl32](https://ctrl32.com/download/) (Windows).
- Volitelně pro příklad all-in-one: adaptér USB-RS485 s I/O modulem Modbus RTU a čidlem teploty; CAN HAT (MCP2515 nebo MCP251xFD).

## Napájení

| Zdroj | Kde | Poznámka |
|---|---|---|
| USB-C | napájecí konektor | 5 V / 3 A - oficiální zdroj |
| PoE | přes PoE HAT | volitelné |

!!! warning "Podpětí"
    Se slabším zdrojem Pi zpomalí a omezí proud do USB - adaptér
    USB-RS485 nebo dotykový monitor pak může vypadnout. Použij oficiální
    zdroj.

## Mapa pinů

![Raspberry Pi 4 Model B - mapa pinů](pinout/pinout.png)

| GPIO | Funkce v ctrl32 | Poznámka |
|---|---|---|
| 2 | I2C1 SDA - čipy I2C, RTC |  |
| 3 | I2C1 SCL |  |
| 4 | volný - ctrl32 ho nepoužívá | ⚠  |
| 8 | SPI0 CE0 - CAN HAT |  |
| 9 | SPI0 MISO - CAN HAT |  |
| 10 | SPI0 MOSI - CAN HAT |  |
| 11 | SPI0 SCLK - CAN HAT |  |
| 14 | UART TX - RS-485 HAT |  |
| 15 | UART RX - RS-485 HAT |  |
| 17 | volný - ctrl32 ho nepoužívá | ⚠  |
| 22 | volný - ctrl32 ho nepoužívá | ⚠  |
| 25 | přerušení CAN HAT (MCP2515) |  |
| 27 | volný - ctrl32 ho nepoužívá | ⚠  |

Na desce s Linuxem jsou sběrnice **jména zařízení**, ne piny: runtime
otevře to, co pojmenuje nastavení zařízení - `can0` pro CAN HAT nebo USB
adaptér, `/dev/ttyUSB0` pro adaptér USB-RS485 (nebo vlastní UART Pi
s RS-485 HAT). **Prepare a Linux device** je nastaví (krok 3 instalace).
Druhý port Ethernet pro EtherCAT je USB adaptér Ethernet.

## Bezpečnost

- Deska není určena pro bezpečnostní funkce. Nouzové zastavení, dveřní
  spínač nebo světelná závora se zapojují v hardwaru, nikdy přes program.
- Kde to jde, vypni Pi dřív, než odpojíš napájení - runtime uchovávané
  hodnoty ochrání, operační systém má ale radši čisté zastavení.

---

[← Přehled](README.cs.md) | [Přehled](README.cs.md) | [Nahrání runtime →](install.cs.md)
