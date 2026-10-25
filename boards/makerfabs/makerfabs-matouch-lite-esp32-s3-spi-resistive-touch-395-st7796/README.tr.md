---
title: Makerfabs MaTouch Lite ESP32-S3 3.95"
slug: makerfabs-matouch-lite-esp32-s3-spi-resistive-touch-395-st7796
sidebar_position: 10
hardware: /hardware/boards/makerfabs-matouch-lite-esp32-s3-spi-resistive-touch-395-st7796/
image: img/board-01.jpg
image_alt: 3,95 inç dokunmatik ekranıyla Makerfabs MaTouch Lite ESP32-S3 kartı
tags:
- esp32-s3
- display
- touch
- hmi
- wifi
- makerfabs
---

# Makerfabs MaTouch Lite ESP32-S3 3.95"

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32-S3](https://img.shields.io/badge/chip-ESP32--S3-334155) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a) ![CAN: 1](https://img.shields.io/badge/CAN-1-7c3aed) ![HMI: 320x480](https://img.shields.io/badge/HMI-320x480-0891b2)

![3,95 inç dokunmatik ekranıyla Makerfabs MaTouch Lite ESP32-S3 kartı](img/board-01.jpg)

Makerfabs MaTouch Lite düşük maliyetli bir dokunmatik paneldir: PSRAM ve Wi-Fi'lı bir ESP32-S3 üzerinde rezistif dokunmatikli 3,95" 320 x 480 ekran. ctrl32 ile HMI ve PLC bir aradadır - editörde çizilen ekranlar camda, yanında bir merdiven programı, aynı değerler her tarayıcıda (WEBview), Modbus TCP, CAN ve MQTT. Rezistif dokunmatik eldivenle de çalışır.

**Şunlar için uygun:**

- Bir makine üzerinde eldivenle kullanılan küçük bir operatör paneli
- Bir duvar termostatı veya oda kontrolcüsü
- Bir araç veya sürücü için CAN ekranı

Kataloğda kartın sayfası: [Makerfabs MaTouch Lite ESP32-S3 3.95"](https://ctrl32.com/hardware/boards/makerfabs-matouch-lite-esp32-s3-spi-resistive-touch-395-st7796/)

![Makerfabs MaTouch Lite ESP32-S3 3.95" - pin haritası: ctrl32'de her GPIO'nun işlevi](pinout/pinout.png)

## ctrl32 bu kartta neler yapabilir

<!-- capabilities:start -->
| Özellik | Bu kartta | Notlar |
|---|---|---|
| Çip | ESP32-S3 (esp32s3_wroom_1_n16r8) |  |
| Bellek | 16 MB flash, 8 MB PSRAM |  |
| Program boyutu | 512 değişken, 128 alarm, 512 blok | editör yüklemeden önce kontrol eder |
| Dijital girişler / çıkışlar | 4 boş GPIO | pin haritasına bakın |
| Analog girişler | 4 çip üzerinde (ADC1) | GPIO4, GPIO5, GPIO6, GPIO7 |
| Ethernet | hayır |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 | harici bir alıcı-verici gerektirir |
| Modbus RTU (RS-485) | evet | boş pinlerde, harici bir alıcı-verici gerektirir |
| Modbus TCP | istemci ve sunucu |  |
| MQTT | evet (TLS de) | Home Assistant keşfi (discovery) |
| WEBview | evet | her tarayıcıda operatör sayfası |
| Ekran / dokunmatik (HMI) | 3.95" 320x480, NS2009 |  |
| USB | USB-C (CH340K USB-UART, Native USB) |  |
| Besleme | 5 V USB (4.0–5.25 V), 3.7 V Li-Po / Li-Ion |  |
<!-- capabilities:end -->

### Neler desteklenmez

- Bluetooth.
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
- [Makerfabs MaTouch ESP32-P4 7"](../makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/README.tr.md) - büyük kardeşi

