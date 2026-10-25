---
title: 'Olimex ESP32-DevKit-LiPo: donanım ve kablolama'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-DevKit-LiPo - pin haritası
tags:
- esp32
- wifi
- battery
- olimex
---

# Donanım ve kablolama

## Neye ihtiyacınız var

- Olimex ESP32-DevKit-LiPo.
- Bir micro-USB veri kablosu - yükleme ve besleme (5 V) için.
- 2,4 GHz Wi-Fi ağınızın adı ve parolası.
- [ctrl32 editörü](https://ctrl32.com/download/) kurulu bir PC (Windows).
- İsteğe bağlı, all-in-one örneği için: GPIO13 ile GND arasında bir buton; GPIO4 üzerinde bir röle modülü veya dirençli bir LED; 3,3 V ile GND arasında, orta ucu GPIO32'de bir potansiyometre (10 k); GPIO14 / GPIO34 üzerinde 3,3 V'luk bir CAN alıcı-vericisi ve GPIO16 / GPIO36 / GPIO17 (DE) üzerinde bir RS-485 alıcı-vericisi; yedek için bir Li-Po hücre.

## Besleme

| Kaynak | Nerede | Not |
|---|---|---|
| USB 5 V | micro-USB konnektörü | besleme ve programlama |
| Li-Po pil | pil konnektörü | kart üzerinde şarj edilir, USB kesilince devralır |

## Pin haritası

![Olimex ESP32-DevKit-LiPo - pin haritası](pinout/pinout.png)

| GPIO | ctrl32'deki işlevi | Not |
|---|---|---|
| 4 | boş - G/Ç |  |
| 6 | modülün SPI flash'ı | ⚠ kart tarafından kullanılır |
| 7 | modülün SPI flash'ı | ⚠ kart tarafından kullanılır |
| 8 | modülün SPI flash'ı | ⚠ kart tarafından kullanılır |
| 9 | modülün SPI flash'ı | ⚠ kart tarafından kullanılır |
| 10 | modülün SPI flash'ı | ⚠ kart tarafından kullanılır |
| 11 | modülün SPI flash'ı | ⚠ kart tarafından kullanılır |
| 13 | boş - G/Ç |  |
| 14 | boş - G/Ç |  |
| 16 | boş - G/Ç |  |
| 17 | boş - G/Ç |  |
| 18 | boş - G/Ç |  |
| 19 | boş - G/Ç |  |
| 21 | boş - G/Ç |  |
| 22 | boş - G/Ç |  |
| 23 | boş - G/Ç |  |
| 25 | boş - G/Ç |  |
| 26 | boş - G/Ç |  |
| 27 | boş - G/Ç |  |
| 32 | boş - G/Ç | ADC1 |
| 33 | boş - G/Ç | ADC1 |
| 34 | boş - giriş | ⚠ yalnızca giriş, ADC1 |
| 35 | free (BAT SENSE line) | ⚠ yalnızca giriş, ADC1 |
| 36 | boş - giriş | ⚠ yalnızca giriş, ADC1 |
| 39 | free (PWR SENSE line) | ⚠ yalnızca giriş, ADC1 |

İki başlık modülün boş GPIO'larını taşır. GPIO34 - GPIO39 yalnızca
giriştir; GPIO0, 2, 12 ve 15 strapping pinleridir - bunları girişlere
bırakın ya da kullanmadan önce test edin. GND'ye bağlı bir buton direnç
gerektirmez: ctrl32 onu çipin pull-up'ıyla ters çevrilmiş olarak okur.

## Güvenlik

- Kart güvenlik fonksiyonları için tasarlanmamıştır. Acil stop, kapı
  şalteri veya ışık perdesi donanımla bağlanır, asla bir program
  üzerinden değil.
- GPIO pinleri 3,3 V'tur. 24 V'luk bir sinyal bir optokuplör veya seviye
  dönüştürücü gerektirir; bir röle bobini bir sürücü gerektirir (röle
  modülünde vardır).

---

[← Genel bakış](README.tr.md) | [Genel bakış](README.tr.md) | [Runtime'ı kurun →](install.tr.md)
