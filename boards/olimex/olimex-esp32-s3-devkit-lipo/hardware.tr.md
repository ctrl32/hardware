---
title: 'Olimex ESP32-S3-DevKit-Lipo: donanım ve kablolama'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-S3-DevKit-Lipo - pin haritası
tags:
- esp32-s3
- wifi
- psram
- battery
- olimex
---

# Donanım ve kablolama

## Neye ihtiyacınız var

- Olimex ESP32-S3-DevKit-Lipo.
- Bir USB-C veri kablosu - yükleme için UART işaretli konnektörde (CH340X).
- 2,4 GHz Wi-Fi ağınızın adı ve parolası.
- [ctrl32 editörü](https://ctrl32.com/download/) kurulu bir PC (Windows).
- İsteğe bağlı, all-in-one örneği için: Boot/User butonu (GPIO0) ve LED (GPIO38) karttadır; 3,3 V ile GND arasında, orta ucu GPIO1'de bir potansiyometre (10 k); GPIO10 / GPIO17 üzerinde 3,3 V'luk bir CAN alıcı-vericisi ve GPIO18 / GPIO2 / GPIO4 (DE) üzerinde bir RS-485 alıcı-vericisi.

## Besleme

| Kaynak | Nerede | Not |
|---|---|---|
| USB 5 V | iki USB-C konnektöründen herhangi biri | besleme ve programlama |
| Li-Po pil | pil konnektörü | kart üzerinde şarj edilir, otomatik geçiş |

## Pin haritası

![Olimex ESP32-S3-DevKit-Lipo - pin haritası](pinout/pinout.png)

| GPIO | ctrl32'deki işlevi | Not |
|---|---|---|
| 0 | boş - kartın butonu | ⚠ strapping pini |
| 1 | boş - G/Ç | ADC1 |
| 2 | boş - G/Ç | ADC1 |
| 4 | boş - G/Ç | ADC1 |
| 5 | free (PWR SENSE line) | ADC1 |
| 6 | free (BAT SENSE line) | ADC1 |
| 7 | boş - G/Ç | ADC1 |
| 8 | boş - G/Ç | ADC1 |
| 9 | boş - G/Ç | ADC1 |
| 10 | free (SPI CS line) | ADC1 |
| 11 | SPI MOSI |  |
| 12 | SPI SCLK |  |
| 13 | SPI MISO |  |
| 14 | boş - G/Ç |  |
| 15 | boş - G/Ç |  |
| 16 | boş - G/Ç |  |
| 17 | free (UART TX line) |  |
| 18 | free (UART RX line) |  |
| 21 | boş - G/Ç |  |
| 38 | free (LED0 line) |  |
| 39 | boş - G/Ç |  |
| 40 | boş - G/Ç |  |
| 41 | boş - G/Ç |  |
| 42 | boş - G/Ç |  |
| 47 | I2C SCL |  |
| 48 | I2C SDA |  |

Başlıklar boş GPIO'ları taşır; ADC1 (ctrl32'nin kullandığı analog girişler)
GPIO1 - GPIO10 üzerindedir. GPIO0, Boot/User butonudur - programda bir
giriştir ve açılışta basılı tutulursa çipin indirme modunu başlatır. pUEXT
konnektörü I2C (GPIO48 / GPIO47) ve SPI taşır.

## Güvenlik

- Kart güvenlik fonksiyonları için tasarlanmamıştır. Acil stop, kapı
  şalteri veya ışık perdesi donanımla bağlanır, asla bir program
  üzerinden değil.
- GPIO pinleri 3,3 V'tur. 24 V'luk bir sinyal bir optokuplör veya seviye
  dönüştürücü gerektirir; bir röle bobini bir sürücü gerektirir (röle
  modülünde vardır).

---

[← Genel bakış](README.tr.md) | [Genel bakış](README.tr.md) | [Runtime'ı kurun →](install.tr.md)
