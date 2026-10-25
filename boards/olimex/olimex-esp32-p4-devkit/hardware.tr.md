---
title: 'Olimex ESP32-P4-DevKit: donanım ve kablolama'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-P4-DevKit - pin haritası
tags:
- esp32-p4
- ethernet
- olimex
---

# Donanım ve kablolama

## Neye ihtiyacınız var

- Olimex ESP32-P4-DevKit.
- Bir USB-C veri kablosu - yükleme ve besleme (5 V) için.
- Bir Ethernet kablosu ve ağınızda boş bir port.
- [ctrl32 editörü](https://ctrl32.com/download/) kurulu bir PC (Windows).
- İsteğe bağlı, all-in-one örneği için: LED (GPIO2) karttadır; GPIO20 ile GND arasında bir buton; GPIO5 / GPIO21 üzerinde 3,3 V'luk bir CAN alıcı-vericisi ve GPIO22 / GPIO23 / GPIO32 (DE) üzerinde bir RS-485 alıcı-vericisi.

## Besleme

| Kaynak | Nerede | Not |
|---|---|---|
| USB 5 V | USB-C konnektörü | besleme, programlama ve hata ayıklama |
| PoE | PoE eklentisi üzerinden | isteğe bağlı |

## Pin haritası

![Olimex ESP32-P4-DevKit - pin haritası](pinout/pinout.png)

| GPIO | ctrl32'deki işlevi | Not |
|---|---|---|
| 2 | free (LED0 line) |  |
| 4 | SPI SCLK |  |
| 5 | free (SPI CS line) |  |
| 7 | I2C SDA |  |
| 8 | I2C SCL |  |
| 20 | boş - G/Ç |  |
| 21 | boş - G/Ç |  |
| 22 | boş - G/Ç |  |
| 23 | boş - G/Ç |  |
| 28 | Ethernet RMII (IP101GRI) | ⚠ kart tarafından kullanılır |
| 29 | Ethernet RMII (IP101GRI) | ⚠ kart tarafından kullanılır |
| 30 | Ethernet RMII (IP101GRI) | ⚠ kart tarafından kullanılır |
| 31 | Ethernet MDC (IP101GRI) | ⚠ kart tarafından kullanılır |
| 32 | boş - G/Ç |  |
| 33 | boş - G/Ç |  |
| 34 | Ethernet RMII (IP101GRI) | ⚠ kart tarafından kullanılır |
| 35 | Ethernet RMII (IP101GRI) | ⚠ kart tarafından kullanılır |
| 46 | boş - G/Ç |  |
| 47 | boş - G/Ç |  |
| 48 | boş - G/Ç |  |
| 49 | Ethernet RMII (IP101GRI) | ⚠ kart tarafından kullanılır |
| 50 | Ethernet RMII (IP101GRI) | ⚠ kart tarafından kullanılır |
| 51 | Ethernet PHY reset (IP101GRI) | ⚠ kart tarafından kullanılır |
| 52 | Ethernet MDIO (IP101GRI) | ⚠ kart tarafından kullanılır |
| 53 | SPI MOSI |  |
| 54 | SPI MISO |  |

Tüm GPIO'lar iki adet 20 pinli başlıktadır. ESP32-P4'te ctrl32'nin
kullandığı bir analog giriş yoktur: analog sinyaller bir I2C ADC'den
(pUEXT konnektöründe bir ADS1115, I2C GPIO7 / GPIO8) ya da bir Modbus
modülünden geçer.

## Güvenlik

- Kart güvenlik fonksiyonları için tasarlanmamıştır. Acil stop, kapı
  şalteri veya ışık perdesi donanımla bağlanır, asla bir program
  üzerinden değil.
- GPIO pinleri 3,3 V'tur. 24 V'luk bir sinyal bir optokuplör veya seviye
  dönüştürücü gerektirir; bir röle bobini bir sürücü gerektirir (röle
  modülünde vardır).

---

[← Genel bakış](README.tr.md) | [Genel bakış](README.tr.md) | [Runtime'ı kurun →](install.tr.md)
