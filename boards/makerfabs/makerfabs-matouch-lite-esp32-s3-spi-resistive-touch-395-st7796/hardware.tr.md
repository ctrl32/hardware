---
title: 'Makerfabs MaTouch Lite ESP32-S3 3.95": donanım ve kablolama'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Makerfabs MaTouch Lite ESP32-S3 3.95" - pin haritası
tags:
- esp32-s3
- display
- touch
- hmi
- wifi
- makerfabs
---

# Donanım ve kablolama

## Neye ihtiyacınız var

- Makerfabs MaTouch Lite ESP32-S3 3,95" (ST7796).
- Bir USB-C veri kablosu - yükleme ve besleme için.
- 2,4 GHz Wi-Fi ağınızın adı ve parolası.
- [ctrl32 editörü](https://ctrl32.com/download/) kurulu bir PC (Windows).
- İsteğe bağlı, all-in-one örneği için: GPIO4 üzerinde bir röle modülü veya LED, 3,3 V ile GND arasında, orta ucu GPIO5'te bir potansiyometre (10 k) (JST konnektörleri) ve GPIO6 / GPIO7 üzerinde 3,3 V'luk bir CAN alıcı-vericisi (ör. SN65HVD230).

## Besleme

| Kaynak | Nerede | Not |
|---|---|---|
| USB 5 V | USB-C konnektörü | besleme ve programlama |
| Li-Po pil | pil konnektörü | 3,7 V |

## Pin haritası

![Makerfabs MaTouch Lite ESP32-S3 3.95" - pin haritası](pinout/pinout.png)

| GPIO | ctrl32'deki işlevi | Not |
|---|---|---|
| 0 | BOOT BTN | ⚠ strapping pini |
| 1 | TFT RST |  |
| 2 | SD CMD | ⚠  |
| 4 | boş - G/Ç | ADC1 |
| 5 | boş - G/Ç | ADC1 |
| 6 | boş - G/Ç | ADC1 |
| 7 | boş - G/Ç | ADC1 |
| 13 | TFT MOSI |  |
| 14 | TFT SCLK |  |
| 15 | TFT CS |  |
| 21 | TFT DC |  |
| 38 | TOUCH SDA |  |
| 39 | TOUCH SCL |  |
| 40 | TOUCH INT |  |
| 41 | SD DO | ⚠  |
| 42 | SD SCLK | ⚠  |
| 48 | TFT BL |  |

İki **JST** konnektörü dört boş pini (GPIO4 - GPIO7) taşır - az sayıda,
bu yüzden örnek çıkışı, analog girişi ve CAN'i bunlara koyar; daha fazla
G/Ç Modbus TCP veya I2C çipleri üzerinden gelir. Ekran, dokunmatik
denetleyici ve microSD yuvası pinlerin geri kalanını kullanır.

## Güvenlik

- Kart güvenlik fonksiyonları için tasarlanmamıştır. Acil stop, kapı
  şalteri veya ışık perdesi donanımla bağlanır, asla bir program ya da
  dokunmatik ekran üzerinden değil.
- GPIO pinleri 3,3 V'tur. Bir röle bobini bir sürücü gerektirir (röle modülünde vardır).

---

[← Genel bakış](README.tr.md) | [Genel bakış](README.tr.md) | [Runtime'ı kurun →](install.tr.md)
