---
title: 'Olimex ESP32-GATEWAY: donanım ve kablolama'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-GATEWAY - pin haritası
tags:
- esp32
- ethernet
- gateway
- olimex
---

# Donanım ve kablolama

## Neye ihtiyacınız var

- Olimex ESP32-GATEWAY.
- Bir USB-C veri kablosu - yükleme ve besleme (5 V) için.
- Bir Ethernet kablosu ve ağınızda boş bir port.
- [ctrl32 editörü](https://ctrl32.com/download/) kurulu bir PC (Windows).
- all-in-one örneği kartın kendi butonunu (GPIO34) ve LED'ini (GPIO33) kullanır - başka bağlanacak bir şey yoktur.

## Besleme

| Kaynak | Nerede | Not |
|---|---|---|
| USB 5 V | USB-C konnektörü | besleme ve programlama |

## Pin haritası

![Olimex ESP32-GATEWAY - pin haritası](pinout/pinout.png)

| GPIO | ctrl32'deki işlevi | Not |
|---|---|---|
| 2 | SPI MOSI | ⚠ strapping pini |
| 5 | Ethernet PHY power (LAN8710A) | ⚠ kart tarafından kullanılır |
| 6 | modülün SPI flash'ı | ⚠ kart tarafından kullanılır |
| 7 | modülün SPI flash'ı | ⚠ kart tarafından kullanılır |
| 8 | modülün SPI flash'ı | ⚠ kart tarafından kullanılır |
| 9 | modülün SPI flash'ı | ⚠ kart tarafından kullanılır |
| 10 | modülün SPI flash'ı | ⚠ kart tarafından kullanılır |
| 11 | modülün SPI flash'ı | ⚠ kart tarafından kullanılır |
| 13 | free (SPI CS line) |  |
| 14 | SPI SCLK |  |
| 15 | SPI MISO | ⚠ strapping pini |
| 16 | I2C SCL |  |
| 17 | Ethernet 50 MHz clock (LAN8710A) | ⚠ kart tarafından kullanılır |
| 18 | Ethernet MDIO (LAN8710A) | ⚠ kart tarafından kullanılır |
| 19 | Ethernet RMII TXD0 (LAN8710A) | ⚠ kart tarafından kullanılır |
| 21 | Ethernet RMII TX_EN (LAN8710A) | ⚠ kart tarafından kullanılır |
| 22 | Ethernet RMII TXD1 (LAN8710A) | ⚠ kart tarafından kullanılır |
| 23 | Ethernet MDC (LAN8710A) | ⚠ kart tarafından kullanılır |
| 25 | Ethernet RMII RXD0 (LAN8710A) | ⚠ kart tarafından kullanılır |
| 26 | Ethernet RMII RXD1 (LAN8710A) | ⚠ kart tarafından kullanılır |
| 27 | Ethernet RMII CRS_DV (LAN8710A) | ⚠ kart tarafından kullanılır |
| 32 | I2C SDA |  |
| 33 | free (LED0 line) | ADC1 |
| 34 | boş - kartın butonu | ⚠ yalnızca giriş, ADC1 |

20 pinli **EXT** başlığı boş pinleri ve I2C / SPI hatlarını taşır. Kartın
LED'i GPIO33'te, butonu GPIO34'tedir (yalnızca giriş). Az sayıda pin boş
kalır: daha fazla G/Ç Modbus TCP veya I2C çipleri üzerinden gelir.

## Güvenlik

- Kart güvenlik fonksiyonları için tasarlanmamıştır. Acil stop, kapı
  şalteri veya ışık perdesi donanımla bağlanır, asla bir program
  üzerinden değil.
- GPIO pinleri 3,3 V'tur. 24 V'luk bir sinyal bir optokuplör veya seviye
  dönüştürücü gerektirir; bir röle bobini bir sürücü gerektirir (röle
  modülünde vardır).

---

[← Genel bakış](README.tr.md) | [Genel bakış](README.tr.md) | [Runtime'ı kurun →](install.tr.md)
