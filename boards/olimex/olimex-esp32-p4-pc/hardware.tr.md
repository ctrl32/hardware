---
title: 'Olimex ESP32-P4-PC: donanım ve kablolama'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-P4-PC - pin haritası
tags:
- esp32-p4
- ethernet
- ups
- olimex
---

# Donanım ve kablolama

## Neye ihtiyacınız var

- Olimex ESP32-P4-PC.
- Bir USB-C veri kablosu - yükleme ve besleme (5 V) için.
- Bir Ethernet kablosu ve ağınızda boş bir port.
- [ctrl32 editörü](https://ctrl32.com/download/) kurulu bir PC (Windows).
- İsteğe bağlı: pil yedeklemesi için bir Li-Po hücre; all-in-one örneği için kullanıcı LED'i (GPIO2) karttadır ve bir buton GPIO14 ile GND arasına gider (EXT1); GPIO5 / GPIO15 üzerinde 3,3 V'luk bir CAN alıcı-vericisi ve GPIO16 / GPIO17 / GPIO18 (DE) üzerinde bir RS-485 alıcı-vericisi.

## Besleme

| Kaynak | Nerede | Not |
|---|---|---|
| USB 5 V | USB-C konnektörü | besleme, programlama ve hata ayıklama |
| Li-Po pil | pil konnektörü | kart üzerinde şarj edilir; besleme kesilince devralır (UPS) |
| PoE | PoE eklentisi üzerinden | isteğe bağlı |

## Pin haritası

![Olimex ESP32-P4-PC - pin haritası](pinout/pinout.png)

| GPIO | ctrl32'deki işlevi | Not |
|---|---|---|
| 2 | free (LED0 line) |  |
| 4 | SPI SCLK |  |
| 5 | free (SPI CS line) |  |
| 14 | boş - G/Ç |  |
| 15 | boş - G/Ç |  |
| 16 | boş - G/Ç |  |
| 17 | boş - G/Ç |  |
| 18 | boş - G/Ç |  |
| 19 | boş - G/Ç |  |
| 20 | boş - G/Ç |  |
| 21 | USB HUB RST | ⚠  |
| 22 | I2C SDA |  |
| 23 | I2C SCL |  |
| 28 | Ethernet RMII (IP101GRI) | ⚠ kart tarafından kullanılır |
| 29 | Ethernet RMII (IP101GRI) | ⚠ kart tarafından kullanılır |
| 30 | Ethernet RMII (IP101GRI) | ⚠ kart tarafından kullanılır |
| 31 | Ethernet MDC (IP101GRI) | ⚠ kart tarafından kullanılır |
| 32 | boş - G/Ç |  |
| 33 | boş - G/Ç |  |
| 34 | Ethernet RMII (IP101GRI) | ⚠ kart tarafından kullanılır |
| 35 | Ethernet RMII (IP101GRI) | ⚠ kart tarafından kullanılır |
| 36 | boş - G/Ç | ⚠ strapping pini |
| 46 | boş - G/Ç |  |
| 47 | boş - G/Ç |  |
| 48 | boş - G/Ç |  |
| 49 | Ethernet RMII (IP101GRI) | ⚠ kart tarafından kullanılır |
| 50 | Ethernet RMII (IP101GRI) | ⚠ kart tarafından kullanılır |
| 51 | Ethernet PHY reset (IP101GRI) | ⚠ kart tarafından kullanılır |
| 52 | Ethernet MDIO (IP101GRI) | ⚠ kart tarafından kullanılır |
| 53 | SPI MOSI |  |
| 54 | SPI MISO |  |

Boş pinler 20 pinli **EXT1** başlığındadır: GPIO14 - GPIO20, 32, 33, 36,
46, 47, 48 ve GPIO2'deki kullanıcı LED'i. **UEXT** konnektörü I2C (GPIO22 /
GPIO23 - HDMI köprüsüyle paylaşılır), SPI (GPIO4 / 53 / 54, CS GPIO5) ve
konsol UART'ını taşır. ESP32-P4'te ctrl32'nin kullandığı bir analog giriş
yoktur: analog sinyaller bir I2C ADC'den (UEXT'te bir ADS1115) ya da bir
Modbus modülünden geçer. CAN ve RS-485, 3,3 V'luk bir alıcı-verici
modülüyle boş EXT1 pinlerine gider.

## Güvenlik

- Kart güvenlik fonksiyonları için tasarlanmamıştır. Acil stop, kapı
  şalteri veya ışık perdesi donanımla bağlanır, asla bir program
  üzerinden değil.
- GPIO pinleri 3,3 V'tur. 24 V'luk bir sinyal bir optokuplör veya seviye
  dönüştürücü gerektirir; bir röle bobini bir sürücü gerektirir (röle
  modülünde vardır).

## Fotoğraflar

![Olimex ESP32-P4-PC - fotoğraf 1](img/board-01.jpg)
![Olimex ESP32-P4-PC - fotoğraf 2](img/board-02.jpg)
![Olimex ESP32-P4-PC - fotoğraf 3](img/board-03.jpg)
![Olimex ESP32-P4-PC - fotoğraf 4](img/board-04.jpg)

---

[← Genel bakış](README.tr.md) | [Genel bakış](README.tr.md) | [Runtime'ı kurun →](install.tr.md)
