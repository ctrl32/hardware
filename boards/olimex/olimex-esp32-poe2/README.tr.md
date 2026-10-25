---
title: Olimex ESP32-POE2
slug: olimex-esp32-poe2
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-poe2/
image: img/board-01.jpg
image_alt: Ethernet soketi ve besleme çıkışlarıyla Olimex ESP32-POE2 kartı
tags:
- esp32
- ethernet
- poe
- psram
- olimex
---

# Olimex ESP32-POE2

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32](https://img.shields.io/badge/chip-ESP32-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a)

![Ethernet soketi ve besleme çıkışlarıyla Olimex ESP32-POE2 kartı](img/board-01.jpg)

Olimex ESP32-POE2, ESP32-PoE'nin yeni neslidir: 8 MB PSRAM'li bir ESP32, Ethernet ve saha cihazlarınızı da besleyen IEEE 802.3at Power over Ethernet - 24 V veya 12 V, 5 V ve 3,3 V çıkışlar, ağ kablosundan 25 W'a kadar. ctrl32 ile tek kabloyla beslenen, panoda bir PLC'dir: merdiven mantığı, WEBview, Modbus TCP ve MQTT, PSRAM'li klasik bir ESP32'nin tam program boyutuyla.

**Şunlar için uygun:**

- Sensörlerini ve küçük bir röle modülünü PoE'den besleyen bir pano PLC'si
- Home Assistant'a MQTT'li bir Modbus TCP ağ geçidi
- Oda başına tek kabloyla bina otomasyonu

Kataloğda kartın sayfası: [Olimex ESP32-POE2](https://ctrl32.com/hardware/boards/olimex-esp32-poe2/)

![Olimex ESP32-POE2 - pin haritası: ctrl32'de her GPIO'nun işlevi](pinout/pinout.png)

## ctrl32 bu kartta neler yapabilir

<!-- capabilities:start -->
| Özellik | Bu kartta | Notlar |
|---|---|---|
| Çip | ESP32 (ESP32-WROVER-E-N4R8) |  |
| Bellek | 4 MB flash, 8 MB PSRAM |  |
| Program boyutu | 512 değişken, 128 alarm, 1024 blok | editör yüklemeden önce kontrol eder |
| Dijital girişler / çıkışlar | 5 boş GPIO | 3 tanesi yalnızca giriş |
| Analog girişler | 3 çip üzerinde (ADC1) | GPIO34, GPIO36, GPIO39 |
| Ethernet | evet - LAN8710A |  |
| Power over Ethernet | IEEE 802.3at |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 - boş pinlerde | harici bir alıcı-verici gerektirir |
| Modbus RTU (RS-485) | evet - boş pinlerde | harici bir alıcı-verici gerektirir |
| Modbus TCP | istemci ve sunucu |  |
| MQTT | evet | Home Assistant keşfi (discovery) |
| WEBview | evet | her tarayıcıda operatör sayfası |
| Ekran / dokunmatik (HMI) | hayır | operatör sayfası WEBview'dur |
| USB | USB-C |  |
| Besleme | 5 V USB, 3.7 V Li-Po / Li-Ion, PoE |  |
<!-- capabilities:end -->

### Neler desteklenmez

- Bluetooth - ESP32'de var, ctrl32 kullanmaz.
- microSD yuvası - ctrl32 programı ve ekranları çipin kendi flash belleğinde tutar.
- Pil girişi kartın kendi özelliği olarak çalışır; ctrl32 pil seviyesini okumaz.

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
- [Olimex ESP32-PoE](../olimex-esp32-poe/README.tr.md) - ilk nesil
- [Olimex ESP32-PoE-ISO](../olimex-esp32-poe-iso/README.tr.md) - yalıtılmış PoE beslemeli

