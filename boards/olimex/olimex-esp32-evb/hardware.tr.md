---
title: 'Olimex ESP32-EVB: donanım ve kablolama'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-EVB - pin haritası
tags:
- esp32
- ethernet
- can
- relay
- olimex
---

# Donanım ve kablolama

## Neye ihtiyacınız var

- Olimex ESP32-EVB.
- Bir micro-USB veri kablosu - runtime'ın ilk yüklemesi için.
- Besleme için: 5 V'luk bir USB adaptör ya da vidalı klemenste 5 V.
- Bir Ethernet kablosu ve ağınızda boş bir port.
- [ctrl32 editörü](https://ctrl32.com/download/) kurulu bir PC (Windows).
- İsteğe bağlı, all-in-one örneği için: 3,3 V ile GND arasında, orta ucu GPIO36'da (UEXT) bir potansiyometre (10 k); bir CAN düğümü veya CAN adaptörü ve iki adet 120 ohm sonlandırıcı.
- İsteğe bağlı: UEXT konnektöründe Olimex MOD-LCD2.8RTP ekranı (2,8 inç, 240 x 320, rezistif dokunmatik).

## Besleme

| Kaynak | Nerede | Not |
|---|---|---|
| USB 5 V | micro-USB konnektörü | ilk yüklemenin yolu |
| 5 V DC | vidalı klemens | pano için |
| Li-Po pil | pil konnektörü | kart üzerinde şarj edilir |

!!! warning "Röleler şebeke gerilimini anahtarlar"
    Röle kontaklarını yalnızca kart enerjisizken, bir muhafaza içinde ve
    şebeke tesisatlarında çalışma yetkisi olan bir kişi olarak bağlayın.
    Kontaklar 10 A / 250 VAC taşır; bunun üzerindeki bir motor veya ısıtıcı,
    röleyle sürülen bir kontaktör gerektirir.

## Pin haritası

![Olimex ESP32-EVB - pin haritası](pinout/pinout.png)

| GPIO | ctrl32'deki işlevi | Not |
|---|---|---|
| 0 | Ethernet 50 MHz clock (LAN8710A) | ⚠ kart tarafından kullanılır |
| 2 | TFT MOSI | ⚠ strapping pini |
| 2 | SPI MOSI | ⚠ strapping pini |
| 4 | free (UART TX line) |  |
| 5 | CAN TX |  |
| 6 | modülün SPI flash'ı | ⚠ kart tarafından kullanılır |
| 7 | modülün SPI flash'ı | ⚠ kart tarafından kullanılır |
| 8 | modülün SPI flash'ı | ⚠ kart tarafından kullanılır |
| 9 | modülün SPI flash'ı | ⚠ kart tarafından kullanılır |
| 10 | modülün SPI flash'ı | ⚠ kart tarafından kullanılır |
| 11 | modülün SPI flash'ı | ⚠ kart tarafından kullanılır |
| 13 | I2C SDA |  |
| 14 | TFT SCLK |  |
| 14 | SPI SCLK |  |
| 15 | TFT DC | ⚠ strapping pini |
| 15 | SPI MISO | ⚠ strapping pini |
| 16 | I2C SCL |  |
| 17 | TFT CS |  |
| 17 | free (SPI CS line) |  |
| 18 | Ethernet MDIO (LAN8710A) | ⚠ kart tarafından kullanılır |
| 19 | Ethernet RMII TXD0 (LAN8710A) | ⚠ kart tarafından kullanılır |
| 21 | Ethernet RMII TX_EN (LAN8710A) | ⚠ kart tarafından kullanılır |
| 22 | Ethernet RMII TXD1 (LAN8710A) | ⚠ kart tarafından kullanılır |
| 23 | Ethernet MDC (LAN8710A) | ⚠ kart tarafından kullanılır |
| 25 | Ethernet RMII RXD0 (LAN8710A) | ⚠ kart tarafından kullanılır |
| 26 | Ethernet RMII RXD1 (LAN8710A) | ⚠ kart tarafından kullanılır |
| 27 | Ethernet RMII CRS_DV (LAN8710A) | ⚠ kart tarafından kullanılır |
| 32 | free (REL1 line) | ADC1 |
| 33 | free (REL2 line) | ADC1 |
| 34 | boş - kartın butonu | ⚠ yalnızca giriş, ADC1 |
| 35 | CAN RX |  |
| 36 | free (UART RX line) | ⚠ yalnızca giriş, ADC1 |

**Röleler:** REL1 GPIO32'de, REL2 GPIO33'te. **Buton:** BUT1 GPIO34'te
(yalnızca giriş). **CAN:** kart üzerindeki alıcı-verici GPIO5 (TX) /
GPIO35 (RX) üzerinde, CAN_H / CAN_L klemenste - veri yolunu iki ucunda
120 ohm ile sonlandırın. **UEXT** konnektörü I2C (GPIO13 / GPIO16), SPI ve
boş bir UART (GPIO4 / GPIO36) taşır; isteğe bağlı ekran onun SPI hatlarını
kullanır.

## Güvenlik

- Kart güvenlik fonksiyonları için tasarlanmamıştır. Acil stop, kapı
  şalteri veya ışık perdesi donanımla bağlanır, asla bir program
  üzerinden değil.
- GPIO pinleri 3,3 V'tur. 24 V'luk bir sinyal bir optokuplör veya seviye
  dönüştürücü gerektirir; bir röle bobini bir sürücü gerektirir (röle
  modülünde vardır).

---

[← Genel bakış](README.tr.md) | [Genel bakış](README.tr.md) | [Runtime'ı kurun →](install.tr.md)
