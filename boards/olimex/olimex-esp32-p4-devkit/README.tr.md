---
title: Olimex ESP32-P4-DevKit
slug: olimex-esp32-p4-devkit
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-p4-devkit/
image: img/board-01.jpg
image_alt: Ethernet soketi ve pin başlıklarıyla Olimex ESP32-P4-DevKit kartı
tags:
- esp32-p4
- ethernet
- olimex
---

# Olimex ESP32-P4-DevKit

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32-P4](https://img.shields.io/badge/chip-ESP32--P4-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a)

![Ethernet soketi ve pin başlıklarıyla Olimex ESP32-P4-DevKit kartı](img/board-01.jpg)

Olimex ESP32-P4-DevKit, ESP32-P4'lü küçük, açık kaynaklı bir karttır - en hızlı ESP32, 32 MB PSRAM'li çift çekirdekli 400 MHz - ve 100 Mb Ethernet. Wi-Fi'ı yoktur: kablolu bir kontrolcüdür. ctrl32 ile bir ESP32'nin çalıştırabileceği en büyük programları çalıştırır - 4096 değişken - operatör sayfası her tarayıcıda (WEBview), Modbus TCP ve TLS'li MQTT ile.

**Şunlar için uygun:**

- Büyük bir programı ve çok sayıda Modbus cihazı olan kablolu bir PLC
- Modbus TCP ile MQTT arasında yoğun mantığı olan bir ağ geçidi
- Kendi P4 kartınızın geliştirilmesi

Kataloğda kartın sayfası: [Olimex ESP32-P4-DevKit](https://ctrl32.com/hardware/boards/olimex-esp32-p4-devkit/)

![Olimex ESP32-P4-DevKit - pin haritası: ctrl32'de her GPIO'nun işlevi](pinout/pinout.png)

## ctrl32 bu kartta neler yapabilir

<!-- capabilities:start -->
| Özellik | Bu kartta | Notlar |
|---|---|---|
| Çip | ESP32-P4 (ESP32-P4NRW32) |  |
| Bellek | 16 MB flash, 32 MB PSRAM |  |
| Program boyutu | 4096 değişken, 512 alarm, 1024 blok | editör yüklemeden önce kontrol eder |
| Dijital girişler / çıkışlar | 11 boş GPIO | pin haritasına bakın |
| Analog girişler | bir I2C ADC üzerinden (ADS1115) |  |
| Ethernet | evet - IP101GRI |  |
| Wi-Fi | hayır |  |
| CAN (TWAI) | 1 - boş pinlerde | harici bir alıcı-verici gerektirir |
| Modbus RTU (RS-485) | evet - boş pinlerde | harici bir alıcı-verici gerektirir |
| Modbus TCP | istemci ve sunucu |  |
| MQTT | evet (TLS de) | Home Assistant keşfi (discovery) |
| WEBview | evet | her tarayıcıda operatör sayfası |
| Ekran / dokunmatik (HMI) | hayır | operatör sayfası WEBview'dur |
| USB | USB-C (Native USB) |  |
| Besleme | 5 V USB, PoE |  |
<!-- capabilities:end -->

### Neler desteklenmez

- MIPI DSI ekran ve CSI kamera konnektörleri - bu kart ctrl32'de ekransız çalışır (operatör sayfası WEBview'dur).
- microSD yuvası - ctrl32 programı ve ekranları kartın flash belleğinde tutar.

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
- [Makerfabs MaTouch ESP32-P4 7"](../../makerfabs/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/README.tr.md) - 7" dokunmatik ekranlı ESP32-P4

