---
title: Olimex ESP32-DevKit-LiPo
slug: olimex-esp32-devkit-lipo
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-devkit-lipo/
image: img/board-01.jpg
image_alt: İki pin başlığı ve micro-USB konnektörüyle Olimex ESP32-DevKit-LiPo kartı
tags:
- esp32
- wifi
- battery
- olimex
---

# Olimex ESP32-DevKit-LiPo

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32](https://img.shields.io/badge/chip-ESP32-334155) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a)

![İki pin başlığı ve micro-USB konnektörüyle Olimex ESP32-DevKit-LiPo kartı](img/board-01.jpg)

Olimex ESP32-DevKit-LiPo, Wi-Fi'lı, modülün tüm GPIO'larını iki pin başlığında sunan ve elektrik kesildiğinde onu çalışır tutan bir Li-Po şarj devresine sahip açık kaynaklı bir ESP32 geliştirme kartıdır. ctrl32 ile küçük bir Wi-Fi PLC'dir: çipte bir merdiven programı, pinlerinde girişler ve çıkışlar, her tarayıcıda operatör sayfası (WEBview), Modbus TCP ve MQTT.

**Şunlar için uygun:**

- Bir oda, sera veya pompa için Wi-Fi kontrolcüsü
- MQTT üzerinden yayın yapan, pil destekli bir veri kaydedici
- ctrl32'yi breadboard üzerinde öğrenmek

Kataloğda kartın sayfası: [Olimex ESP32-DevKit-LiPo](https://ctrl32.com/hardware/boards/olimex-esp32-devkit-lipo/)

![Olimex ESP32-DevKit-LiPo - pin haritası: ctrl32'de her GPIO'nun işlevi](pinout/pinout.png)

## ctrl32 bu kartta neler yapabilir

<!-- capabilities:start -->
| Özellik | Bu kartta | Notlar |
|---|---|---|
| Çip | ESP32 (ESP32-WROOM-32E-N4) |  |
| Bellek | 4 MB flash |  |
| Program boyutu | 128 değişken, 32 alarm, 128 blok | editör yüklemeden önce kontrol eder |
| Dijital girişler / çıkışlar | 19 boş GPIO | 4 tanesi yalnızca giriş |
| Analog girişler | 6 çip üzerinde (ADC1) | GPIO32, GPIO33, GPIO34, GPIO35, GPIO36, GPIO39 |
| Ethernet | hayır |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 - boş pinlerde | harici bir alıcı-verici gerektirir |
| Modbus RTU (RS-485) | evet - boş pinlerde | harici bir alıcı-verici gerektirir |
| Modbus TCP | istemci ve sunucu |  |
| MQTT | evet | Home Assistant keşfi (discovery) |
| WEBview | evet | her tarayıcıda operatör sayfası |
| Ekran / dokunmatik (HMI) | hayır | operatör sayfası WEBview'dur |
| USB | Micro-USB (CH340 USB-UART) |  |
| Besleme | 5 V USB, 3.7 V Li-Po / Li-Ion |  |
<!-- capabilities:end -->

### Neler desteklenmez

- Bluetooth - ESP32'de var, ctrl32 kullanmaz.
- Pil ve besleme algılama girişleri (GPIO35 / GPIO39) ctrl32'de boş pinlerdir, bir pil göstergesi değil.

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
- Olimex ESP32-S3-DevKit-Lipo - ESP32-S3 ve PSRAM ile aynı fikir

