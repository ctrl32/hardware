---
title: 'Olimex ESP32-PoE: donanım ve kablolama'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-PoE - pin haritası
tags:
- esp32
- ethernet
- poe
- olimex
---

# Donanım ve kablolama

## Neye ihtiyacınız var

- Olimex ESP32-PoE (WROOM-32E varyantı, PSRAM'siz).
- Bir micro-USB veri kablosu - runtime'ın ilk yüklemesi için.
- Besleme için: 5 V'luk bir USB adaptör ya da bir PoE switch / enjektör (IEEE 802.3af).
- Bir Ethernet kablosu ve ağınızda boş bir port.
- [ctrl32 editörü](https://ctrl32.com/download/) kurulu bir PC (Windows).
- İsteğe bağlı, all-in-one örneği için: kartta bir buton vardır (BUT1); GPIO33 üzerinde bir röle modülü veya dirençli bir LED; 3,3 V ile GND arasında, orta ucu GPIO35'te bir potansiyometre (10 k); UEXT konnektörünün GPIO4 (TX) / GPIO36 (RX) pinlerinde 3,3 V'luk bir CAN alıcı-vericisi (ör. SN65HVD230).

## Besleme

Kart beslemesini üç kaynaktan birinden alır:

| Kaynak | Nerede | Not |
|---|---|---|
| USB 5 V | micro-USB konnektörü | ilk yüklemenin yolu |
| PoE | Ethernet soketi, bir PoE switch veya enjektörden | IEEE 802.3af |
| Li-Po pil | pil konnektörü | kart üzerinde şarj edilir |

!!! danger "USB ve PoE'yi asla aynı anda bağlamayın"
    ESP32-PoE **galvanik olarak yalıtılmış değildir**. Kart PoE ile
    beslenirken toprağı PoE beslemesini izler - bu durumda PC'nize giden
    bir USB kablosu zarar verici bir akım taşıyabilir. Runtime'ı Ethernet
    kablosu **çıkarılmışken** (ya da PoE olmayan bir porttan) USB üzerinden
    yükleyin, ardından kartı PoE ile çalıştırın. Kart PoE'deyken bir PC'nin
    bağlı kalması gerekiyorsa
    ESP32-PoE-ISO kullanın.

## Pin haritası

![Olimex ESP32-PoE - pin haritası](pinout/pinout.png)

| GPIO | ctrl32'deki işlevi | Not |
|---|---|---|
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
| 33 | boş - G/Ç | ADC1 |
| 34 | boş - kartın butonu | ⚠ yalnızca giriş, ADC1 |
| 35 | boş - giriş | ⚠ yalnızca giriş, ADC1 |
| 36 | free (UART RX line) | ⚠ yalnızca giriş, ADC1 |

Boş pinler **EXT1 / EXT2** başlıklarında (2,54 mm) ve **UEXT**
konnektöründe bulunur. GPIO34 - GPIO39 yalnızca giriştir - orada bir
çıkışı editör reddeder. UEXT konnektörü I2C (GPIO13 / GPIO16) ve SPI
(GPIO14 / GPIO2 / GPIO15, microSD yuvasıyla paylaşılır) taşır.

## Güvenlik

- Kart güvenlik fonksiyonları için tasarlanmamıştır. Acil stop, kapı
  şalteri veya ışık perdesi donanımla bağlanır, asla bir program
  üzerinden değil.
- GPIO pinleri 3,3 V'tur. 24 V'luk bir giriş bir optokuplör veya seviye
  dönüştürücü gerektirir; bir röle bobini bir sürücü gerektirir (röle
  modülünde vardır).

---

[← Genel bakış](README.tr.md) | [Genel bakış](README.tr.md) | [Runtime'ı kurun →](install.tr.md)
