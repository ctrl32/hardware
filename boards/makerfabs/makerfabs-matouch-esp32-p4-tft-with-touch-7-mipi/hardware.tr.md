---
title: 'Makerfabs MaTouch ESP32-P4 7": donanım ve kablolama'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Makerfabs MaTouch ESP32-P4 7" - pin haritası
tags:
- esp32-p4
- display
- touch
- hmi
- ethernet
- makerfabs
---

# Donanım ve kablolama

## Neye ihtiyacınız var

- Makerfabs MaTouch ESP32-P4 TFT with Touch 7" MIPI.
- Bir USB-C veri kablosu - runtime'ın ilk yüklemesi ve besleme için.
- Besleme için: en az 2 A'lik 5 V USB-C adaptör (çoğunu ekranın arka aydınlatması çeker).
- Bir Ethernet kablosu ya da ağınızın Wi-Fi'ı.
- [ctrl32 editörü](https://ctrl32.com/download/) kurulu bir PC (Windows).
- İsteğe bağlı, all-in-one örneği için: J6 başlığında iki buton ve bir röle modülü; I2C veri yolunda bir ADS1115 modülü; 3,3 V'luk bir RS-485 alıcı-vericisi (ör. MAX3485) ve 3,3 V'luk bir CAN alıcı-vericisi (ör. SN65HVD230).

## Besleme

| Kaynak | Nerede | Not |
|---|---|---|
| USB 5 V | USB-C konnektörü | 2 A veya daha fazla - çoğunu 7" arka aydınlatma çeker |
| Li-Po pil | pil konnektörü | 3,7 V, kart üzerinde şarj edilir |

!!! warning "Zayıf bir besleme"
    Bir PC'nin USB portu, arka aydınlatma açıkken kartı çoğu zaman
    taşıyamaz. Ekran açılırken kart yeniden başlıyorsa 5 V / 2 A'lik bir
    adaptör ya da beslemeli bir USB hub kullanın.

## Pin haritası

![Makerfabs MaTouch ESP32-P4 7" - pin haritası](pinout/pinout.png)

| GPIO | ctrl32'deki işlevi | Not |
|---|---|---|
| 0 | RTC XTAL P | ⚠  |
| 1 | RTC XTAL N | ⚠  |
| 2 | boş - G/Ç |  |
| 3 | boş - G/Ç |  |
| 4 | boş - G/Ç |  |
| 5 | boş - G/Ç |  |
| 6 | C6 IO2 | ⚠  |
| 7 | TOUCH SDA |  |
| 8 | TOUCH SCL |  |
| 20 | boş - G/Ç |  |
| 21 | boş - G/Ç |  |
| 22 | TOUCH RST |  |
| 23 | TFT BL |  |
| 26 | USB1 PAIR | ⚠  |
| 27 | DSI RST |  |
| 28 | Ethernet RMII (IP101GRI) | ⚠ kart tarafından kullanılır |
| 29 | Ethernet RMII (IP101GRI) | ⚠ kart tarafından kullanılır |
| 30 | Ethernet RMII (IP101GRI) | ⚠ kart tarafından kullanılır |
| 31 | Ethernet MDC (IP101GRI) | ⚠ kart tarafından kullanılır |
| 32 | boş - G/Ç |  |
| 33 | boş - G/Ç |  |
| 34 | Ethernet RMII (IP101GRI) | ⚠ kart tarafından kullanılır |
| 35 | Ethernet RMII (IP101GRI) | ⚠ kart tarafından kullanılır |
| 36 | boş - G/Ç | ⚠ strapping pini |
| 37 | CONSOLE RX | ⚠ strapping pini |
| 38 | CONSOLE TX | ⚠ strapping pini |
| 45 | MOSFET GATE | ⚠  |
| 46 | boş - G/Ç |  |
| 47 | boş - G/Ç |  |
| 48 | boş - G/Ç |  |
| 49 | Ethernet RMII (IP101GRI) | ⚠ kart tarafından kullanılır |
| 50 | Ethernet RMII (IP101GRI) | ⚠ kart tarafından kullanılır |
| 51 | Ethernet PHY reset (IP101GRI) | ⚠ kart tarafından kullanılır |
| 52 | Ethernet MDIO (IP101GRI) | ⚠ kart tarafından kullanılır |
| 53 | AMP EN | ⚠  |
| 54 | C6 EN | ⚠  |

Boş pinler **J6** ve **J10** başlıklarında ve iki Grove konnektöründe
(**J1**, **J2**) bulunur. Kartın I2C veri yolu (GPIO7 / GPIO8) dokunmatik
denetleyiciyi ve ses codec'ini taşır; başka I2C çipleri (bir ADS1115, bir
sensör) aynı veri yoluna katılır. CAN ve RS-485'in kartta alıcı-vericisi
yoktur: örnek bunları boş pinlere koyar - **CAN** TX GPIO20 / RX GPIO21
(Grove J2), **RS-485** TX GPIO4 / RX GPIO5 / DE GPIO32 (J10) - her biri
3,3 V'luk bir alıcı-verici modülüne.

## Güvenlik

- Kart güvenlik fonksiyonları için tasarlanmamıştır. Acil stop, kapı
  şalteri veya ışık perdesi donanımla bağlanır, asla bir program ya da
  dokunmatik ekran üzerinden değil.
- GPIO pinleri 3,3 V'tur. 24 V'luk bir sinyal bir optokuplör gerektirir;
  bir röle bobini bir sürücü gerektirir (röle modülünde vardır).
- Kapasitif dokunmatik, güçlü bir parazit kaynağının (bir sürücünün)
  yanında yanlış bir basma algılayabilir. Ekrandaki kritik komutlar onay
  ister.

## Fotoğraflar

![Makerfabs MaTouch ESP32-P4 7" - fotoğraf 1](img/board-01.jpg)
![Makerfabs MaTouch ESP32-P4 7" - fotoğraf 2](img/board-02.jpg)
![Makerfabs MaTouch ESP32-P4 7" - fotoğraf 3](img/board-03.jpg)
![Makerfabs MaTouch ESP32-P4 7" - fotoğraf 4](img/board-04.jpg)
![Makerfabs MaTouch ESP32-P4 7" - fotoğraf 5](img/board-05.jpg)
![Makerfabs MaTouch ESP32-P4 7" - fotoğraf 6](img/board-06.jpg)
![Makerfabs MaTouch ESP32-P4 7" - fotoğraf 7](img/board-07.jpg)
![Makerfabs MaTouch ESP32-P4 7" - fotoğraf 8](img/board-08.jpg)

---

[← Genel bakış](README.tr.md) | [Genel bakış](README.tr.md) | [Runtime'ı kurun →](install.tr.md)
