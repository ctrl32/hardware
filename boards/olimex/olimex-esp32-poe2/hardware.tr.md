---
title: 'Olimex ESP32-POE2: donanım ve kablolama'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-POE2 - pin haritası
tags:
- esp32
- ethernet
- poe
- psram
- olimex
---

# Donanım ve kablolama

## Neye ihtiyacınız var

- Olimex ESP32-POE2.
- Bir USB-C veri kablosu - runtime'ın ilk yüklemesi için.
- Besleme için: bir PoE switch / enjektör (IEEE 802.3at, tam 25 W için sınıf 4) ya da 5 V'luk bir USB adaptör.
- Bir Ethernet kablosu ve ağınızda boş bir port.
- [ctrl32 editörü](https://ctrl32.com/download/) kurulu bir PC (Windows).
- İsteğe bağlı, all-in-one örneği için: BUT1 butonu karttadır; GPIO4 (UEXT) üzerinde bir röle modülü veya LED; 3,3 V ile GND arasında, orta ucu GPIO36'da bir potansiyometre (10 k); GPIO5 (TX) / GPIO39 (RX) üzerinde 3,3 V'luk bir CAN alıcı-vericisi.

## Besleme

| Kaynak | Nerede | Not |
|---|---|---|
| PoE | Ethernet soketi | IEEE 802.3at sınıf 4, 25 W'a kadar |
| USB 5 V | USB-C konnektörü | ilk yüklemenin yolu |
| Li-Po pil | pil konnektörü | kart üzerinde şarj edilir |

Ethernet üzerinden beslendiğinde kart harici devreleri besler: **24 V /
0,75 A veya 12 V / 1,5 A** (bir jumper seçer), **5 V / 1,5 A** ve
**3,3 V / 1 A**, toplam 25 W.

!!! danger "USB ve PoE'yi asla aynı anda bağlamayın"
    ESP32-POE2, Ethernet beslemesinden **galvanik olarak yalıtılmış
    değildir**. Runtime'ı Ethernet kablosu çıkarılmışken (ya da PoE
    olmayan bir porttan) USB üzerinden yükleyin, ardından kartı PoE ile
    çalıştırın.

## Pin haritası

![Olimex ESP32-POE2 - pin haritası](pinout/pinout.png)

| GPIO | ctrl32'deki işlevi | Not |
|---|---|---|
| 0 | Ethernet 50 MHz clock (LAN8710A) | ⚠ kart tarafından kullanılır |
| 2 | SPI MOSI | ⚠ strapping pini |
| 4 | free (UART TX line) |  |
| 5 | free (SPI CS line) |  |
| 6 | modülün SPI flash'ı | ⚠ kart tarafından kullanılır |
| 7 | modülün SPI flash'ı | ⚠ kart tarafından kullanılır |
| 8 | modülün SPI flash'ı | ⚠ kart tarafından kullanılır |
| 9 | modülün SPI flash'ı | ⚠ kart tarafından kullanılır |
| 10 | modülün SPI flash'ı | ⚠ kart tarafından kullanılır |
| 11 | modülün SPI flash'ı | ⚠ kart tarafından kullanılır |
| 12 | Ethernet PHY power (LAN8710A) | ⚠ kart tarafından kullanılır |
| 13 | I2C SDA |  |
| 14 | SPI SCLK |  |
| 15 | SPI MISO | ⚠ strapping pini |
| 18 | Ethernet MDIO (LAN8710A) | ⚠ kart tarafından kullanılır |
| 19 | Ethernet RMII TXD0 (LAN8710A) | ⚠ kart tarafından kullanılır |
| 21 | Ethernet RMII TX_EN (LAN8710A) | ⚠ kart tarafından kullanılır |
| 22 | Ethernet RMII TXD1 (LAN8710A) | ⚠ kart tarafından kullanılır |
| 23 | Ethernet MDC (LAN8710A) | ⚠ kart tarafından kullanılır |
| 25 | Ethernet RMII RXD0 (LAN8710A) | ⚠ kart tarafından kullanılır |
| 26 | Ethernet RMII RXD1 (LAN8710A) | ⚠ kart tarafından kullanılır |
| 27 | Ethernet RMII CRS_DV (LAN8710A) | ⚠ kart tarafından kullanılır |
| 33 | I2C SCL |  |
| 34 | boş - kartın butonu | ⚠ yalnızca giriş, ADC1 |
| 36 | free (UART RX line) | ⚠ yalnızca giriş, ADC1 |
| 39 | boş - giriş | ⚠ yalnızca giriş, ADC1 |

Boş pinler **EXT** başlıklarında ve **UEXT** konnektöründe bulunur.
GPIO34 - GPIO39 yalnızca giriştir. Modülün PSRAM'i GPIO16 / GPIO17'yi
kullanır, bu yüzden Ethernet saati GPIO0'da çalışır ve I2C GPIO13 /
GPIO33'ü kullanır.

## Güvenlik

- Kart güvenlik fonksiyonları için tasarlanmamıştır. Acil stop, kapı
  şalteri veya ışık perdesi donanımla bağlanır, asla bir program
  üzerinden değil.
- GPIO pinleri 3,3 V'tur. 24 V'luk bir giriş bir optokuplör veya seviye
  dönüştürücü gerektirir; bir röle bobini bir sürücü gerektirir (röle
  modülünde vardır).

---

[← Genel bakış](README.tr.md) | [Genel bakış](README.tr.md) | [Runtime'ı kurun →](install.tr.md)
