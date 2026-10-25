---
title: 'Raspberry Pi 3 Model B+: donanım ve kablolama'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Raspberry Pi 3 Model B+ - pin haritası
tags:
- raspberry-pi
- linux
- hmi
- opc-ua
---

# Donanım ve kablolama

## Neye ihtiyacınız var

- Bir Raspberry Pi 3 Model B+.
- Bir microSD kart (16 GB veya daha büyük) ve [Raspberry Pi Imager](https://www.raspberrypi.com/software/).
- 5 V / 2,5 A'lik bir micro-USB güç adaptörü.
- PC ile aynı ağda bir Ethernet kablosu.
- HMI için: bir HDMI monitör (tam boy HDMI) veya bir DSI ekran; dokunmatik bir monitörde onun USB'si de.
- [ctrl32 editörü](https://ctrl32.com/download/) kurulu bir PC (Windows).
- İsteğe bağlı, all-in-one örneği için: bir Modbus RTU G/Ç modülü ve bir sıcaklık sensörüyle bir USB-RS485 adaptörü; bir CAN HAT (MCP2515).

## Besleme

| Kaynak | Nerede | Not |
|---|---|---|
| micro-USB | güç konnektörü | 5 V / 2,5 A |
| PoE | bir PoE HAT üzerinden | isteğe bağlı |

!!! warning "Düşük gerilim"
    Daha zayıf bir adaptör Pi'nin hızını düşürmesine ve USB akımını
    sınırlamasına neden olur - bu durumda bir USB-RS485 adaptörü veya
    dokunmatik monitör devre dışı kalabilir.

## Pin haritası

![Raspberry Pi 3 Model B+ - pin haritası](pinout/pinout.png)

| GPIO | ctrl32'deki işlevi | Not |
|---|---|---|
| 2 | I2C1 SDA - I2C çipleri, RTC |  |
| 3 | I2C1 SCL |  |
| 4 | boş - ctrl32 tarafından kullanılmaz | ⚠  |
| 8 | SPI0 CE0 - CAN HAT |  |
| 9 | SPI0 MISO - CAN HAT |  |
| 10 | SPI0 MOSI - CAN HAT |  |
| 11 | SPI0 SCLK - CAN HAT |  |
| 14 | UART TX - RS-485 HAT |  |
| 15 | UART RX - RS-485 HAT |  |
| 17 | boş - ctrl32 tarafından kullanılmaz | ⚠  |
| 22 | boş - ctrl32 tarafından kullanılmaz | ⚠  |
| 25 | CAN HAT kesmesi (MCP2515) |  |
| 27 | boş - ctrl32 tarafından kullanılmaz | ⚠  |

Bir Linux kartında veri yolları pin değil **cihaz adlarıdır**: runtime,
cihazın ayarlarında adı geçeni açar - bir CAN HAT veya USB adaptörü için
`can0`, bir USB-RS485 adaptörü için `/dev/ttyUSB0` (ya da bir RS-485 HAT
ile Pi'nin kendi UART'ı). **Prepare a Linux device** bunları kurar
(kurulumun 3. adımı). EtherCAT için ikinci Ethernet portu bir USB Ethernet
adaptörüdür.

## Güvenlik

- Kart güvenlik fonksiyonları için tasarlanmamıştır. Acil stop, kapı
  şalteri veya ışık perdesi donanımla bağlanır, asla bir program
  üzerinden değil.
- Mümkün olduğunda beslemesini kesmeden önce Pi'yi kapatın - runtime
  kalıcı değerleri güvende tutar, işletim sistemi ise temiz bir kapanışı
  tercih eder.

---

[← Genel bakış](README.tr.md) | [Genel bakış](README.tr.md) | [Runtime'ı kurun →](install.tr.md)
