---
title: Olimex ESP32-P4-PC
slug: olimex-esp32-p4-pc
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-p4-pc/
image: img/board-01.jpg
image_alt: Ethernet soketi, USB portları ve HDMI konnektörüyle Olimex ESP32-P4-PC kartı
tags:
- esp32-p4
- ethernet
- ups
- olimex
---

# Olimex ESP32-P4-PC

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32-P4](https://img.shields.io/badge/chip-ESP32--P4-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a)

![Ethernet soketi, USB portları ve HDMI konnektörüyle Olimex ESP32-P4-PC kartı](img/board-01.jpg)

Olimex ESP32-P4-PC, ESP32-P4 üzerinde küçük bir bilgisayardır - 32 MB PSRAM'li çift çekirdekli 400 MHz - 100 Mb Ethernet, dört USB host, HDMI, ses ve elektrik kesintisinde onu çalışır tutan bir Li-Po pil ile. ctrl32 ile bir ESP32'nin çalıştırdığı en büyük programa sahip kablolu bir kontrolcüdür - 4096 değişken - operatör sayfası her tarayıcıda (WEBview), Modbus TCP, TLS'li MQTT ve başlığının boş pinlerinde CAN veya RS-485 ile.

**Şunlar için uygun:**

- Elektrik kesintisini kendi piliyle atlatan kablolu bir PLC
- Modbus TCP, CAN ve MQTT arasında yoğun mantığı olan bir ağ geçidi
- Bir muhafaza içinde, PoE ile beslenen bir kontrolcü (eklentiyle)

Kataloğda kartın sayfası: [Olimex ESP32-P4-PC](https://ctrl32.com/hardware/boards/olimex-esp32-p4-pc/)

![Olimex ESP32-P4-PC - pin haritası: ctrl32'de her GPIO'nun işlevi](pinout/pinout.png)

## ctrl32 bu kartta neler yapabilir

<!-- capabilities:start -->
| Özellik | Bu kartta | Notlar |
|---|---|---|
| Çip | ESP32-P4 (ESP32-P4NRW32) |  |
| Bellek | 16 MB flash, 32 MB PSRAM |  |
| Program boyutu | 4096 değişken, 512 alarm, 1024 blok | editör yüklemeden önce kontrol eder |
| Dijital girişler / çıkışlar | 15 boş GPIO | pin haritasına bakın |
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
| Besleme | 5 V USB, 3.7 V Li-Po / Li-Ion, PoE |  |
<!-- capabilities:end -->

### Neler desteklenmez

- HDMI çıkışı ve MIPI DSI / CSI konnektörleri - bu kart ctrl32'de ekransız çalışır (operatör sayfası WEBview'dur).
- USB host portları ve ses çıkışı.
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

| Dosya | Ne |
|---|---|
| [pinout/pinout.svg](pinout/pinout.svg) | pin haritası, vektörel (ayrıca [PNG](pinout/pinout.png)) |
| [olimex-esp32-p4-pc-schematic.pdf](schematics/olimex-esp32-p4-pc-schematic.pdf) | ESP32-P4-PC schematic Rev C |
| [esp32-p4-pc-rev-c-kicad.zip](schematics/esp32-p4-pc-rev-c-kicad.zip) | KiCad project |
| [olimex-esp32-p4-pc-user-manual.pdf](datasheets/olimex-esp32-p4-pc-user-manual.pdf) | ESP32-P4-PC user manual |
| [NOTICE](https://github.com/ctrl32/hardware/blob/main/NOTICE.md) | fotoğrafların, şemaların ve modellerin nereden geldiği |

## Sonraki adımlar

- [ctrl32 belgeleri](https://ctrl32.com/docs/) - editör, diller, her blok
- [Editörü indirin](https://ctrl32.com/download/)
- [Tüm test edilmiş kartlar](../../README.tr.md)
- [Olimex ESP32-P4-DevKit](../olimex-esp32-p4-devkit/README.tr.md) - daha küçük bir kartta aynı ESP32-P4

