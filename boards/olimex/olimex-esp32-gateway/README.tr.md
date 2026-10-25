---
title: Olimex ESP32-GATEWAY
slug: olimex-esp32-gateway
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-gateway/
image: img/board-01.jpg
image_alt: Ethernet soketi ve USB-C konnektörüyle Olimex ESP32-GATEWAY kartı
tags:
- esp32
- ethernet
- gateway
- olimex
---

# Olimex ESP32-GATEWAY

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32](https://img.shields.io/badge/chip-ESP32-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a)

![Ethernet soketi ve USB-C konnektörüyle Olimex ESP32-GATEWAY kartı](img/board-01.jpg)

Olimex ESP32-GATEWAY, 100 Mb Ethernet ve Wi-Fi'lı kompakt bir ESP32 kartıdır - bir buat kutusuna sığacak kadar küçük. ctrl32 ile kendi mantığı olan bir ağ geçididir: Modbus TCP cihazları okunur ve MQTT üzerinden yayınlanır, çipte bir merdiven programı çalışır ve operatör sayfası her tarayıcıda açılır (WEBview).

**Şunlar için uygun:**

- Kendi mantığı olan bir Modbus TCP - MQTT ağ geçidi
- Bir buat kutusunda, Ethernet üzerinde küçük bir kontrolcü
- Ev otomasyonu - sayaçları okumak, Modbus G/Ç modülleri üzerinden anahtarlamak

Kataloğda kartın sayfası: [Olimex ESP32-GATEWAY](https://ctrl32.com/hardware/boards/olimex-esp32-gateway/)

![Olimex ESP32-GATEWAY - pin haritası: ctrl32'de her GPIO'nun işlevi](pinout/pinout.png)

## ctrl32 bu kartta neler yapabilir

<!-- capabilities:start -->
| Özellik | Bu kartta | Notlar |
|---|---|---|
| Çip | ESP32 (ESP32-WROOM-32E-N4) |  |
| Bellek | 4 MB flash |  |
| Program boyutu | 128 değişken, 32 alarm, 128 blok | editör yüklemeden önce kontrol eder |
| Dijital girişler / çıkışlar | 3 boş GPIO | 1 tanesi yalnızca giriş |
| Analog girişler | 2 çip üzerinde (ADC1) | GPIO33, GPIO34 |
| Ethernet | evet - LAN8710A |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 - boş pinlerde | harici bir alıcı-verici gerektirir |
| Modbus RTU (RS-485) | evet - boş pinlerde | harici bir alıcı-verici gerektirir |
| Modbus TCP | istemci ve sunucu |  |
| MQTT | evet | Home Assistant keşfi (discovery) |
| WEBview | evet | her tarayıcıda operatör sayfası |
| Ekran / dokunmatik (HMI) | hayır | operatör sayfası WEBview'dur |
| USB | USB-C (CH340 USB-UART) |  |
| Besleme | 5 V USB |  |
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
- [Olimex ESP32-PoE](../olimex-esp32-poe/README.tr.md) - Ethernet ve Power over Ethernet

