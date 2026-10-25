---
title: LaskaKit ESPlan
slug: laskakit-esplan
sidebar_position: 10
hardware: /hardware/boards/laskakit-esplan/
image: img/board-01.jpg
image_alt: Ethernet soketi, RS-485 klemensi ve besleme klemensiyle LaskaKit ESPlan kartı
tags:
- esp32
- ethernet
- rs485
- modbus
- laskakit
---

# LaskaKit ESPlan

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32](https://img.shields.io/badge/chip-ESP32-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a)

![Ethernet soketi, RS-485 klemensi ve besleme klemensiyle LaskaKit ESPlan kartı](img/board-01.jpg)

LaskaKit ESPlan, ESP32 tabanlı endüstriyel bir karttır: 10/100 Ethernet, korumalı ve sonlandırması anahtarlanabilen bir RS-485 arayüzü, Wi-Fi ve vidalı klemens üzerinden geniş 7-40 V besleme (ya da bir ek modülle PoE). ctrl32 ile panodaki bir Modbus RTU master veya slave olur - çipte bir merdiven programı, okunan ve yazılan RS-485 cihazları, değerler Modbus TCP, MQTT ve kartın operatör sayfasında (WEBview).

**Şunlar için uygun:**

- Sayaçlar, sensörler ve sürücüler için 24 V beslemeli bir Modbus RTU master
- Kendi mantığı olan bir Modbus RTU / TCP ağ geçidi
- Panoda bina otomasyonu

Kataloğda kartın sayfası: [LaskaKit ESPlan](https://ctrl32.com/hardware/boards/laskakit-esplan/)

![LaskaKit ESPlan - pin haritası: ctrl32'de her GPIO'nun işlevi](pinout/pinout.png)

## ctrl32 bu kartta neler yapabilir

<!-- capabilities:start -->
| Özellik | Bu kartta | Notlar |
|---|---|---|
| Çip | ESP32 (ESP32-WROOM-32E-N4) |  |
| Bellek | 4 MB flash |  |
| Program boyutu | 128 değişken, 32 alarm, 128 blok | editör yüklemeden önce kontrol eder |
| Dijital girişler / çıkışlar | 5 boş GPIO | 2 tanesi yalnızca giriş |
| Analog girişler | 2 çip üzerinde (ADC1) | GPIO35, GPIO39 |
| Ethernet | evet - LAN8720A |  |
| Power over Ethernet | IEEE 802.3af |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 - boş pinlerde | harici bir alıcı-verici gerektirir |
| Modbus RTU (RS-485) | evet |  |
| Modbus TCP | istemci ve sunucu |  |
| MQTT | evet | Home Assistant keşfi (discovery) |
| WEBview | evet | her tarayıcıda operatör sayfası |
| Ekran / dokunmatik (HMI) | hayır | operatör sayfası WEBview'dur |
| USB | USB-C (CH9102 USB-UART) |  |
| Besleme | 5 V USB, PoE |  |
<!-- capabilities:end -->

### Neler desteklenmez

- Bluetooth - ESP32'de var, ctrl32 kullanmaz.
- microSD yuvası - ctrl32 programı ve ekranları çipin kendi flash belleğinde tutar.

## Kılavuz

| Adım | Sayfa |
|---|---|
| 1 | [Donanım ve kablolama](hardware.tr.md) - neye ihtiyacınız var, besleme, pin haritası |
| 2 | [Runtime'ı kurun](install.tr.md) - editör, kart, ilk yükleme |
| 3 | [Yapılandırma](configure.tr.md) - ağ, G/Ç, iletişim |
| 4 | [Örnek projeler](examples/README.tr.md) - kartın yaptığı her şey, açılmaya hazır |
| - | [Sorun giderme](troubleshooting.tr.md) |

## Dosyalar

-

## Sonraki adımlar

- [ctrl32 belgeleri](https://ctrl32.com/docs/) - editör, diller, her blok
- [Editörü indirin](https://ctrl32.com/download/)
- [Tüm test edilmiş kartlar](../../README.tr.md)

