---
title: Olimex ESP32-EVB
slug: olimex-esp32-evb
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-evb/
image: img/board-01.jpg
image_alt: İki rölesi, Ethernet soketi ve CAN klemensiyle Olimex ESP32-EVB kartı
tags:
- esp32
- ethernet
- can
- relay
- olimex
---

# Olimex ESP32-EVB

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32](https://img.shields.io/badge/chip-ESP32-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a) ![CAN: 1](https://img.shields.io/badge/CAN-1-7c3aed) ![HMI: 240x320](https://img.shields.io/badge/HMI-240x320-0891b2)

![İki rölesi, Ethernet soketi ve CAN klemensiyle Olimex ESP32-EVB kartı](img/board-01.jpg)

Olimex ESP32-EVB, kontrol için yapılmış bir ESP32 kartıdır: iki röle (10 A / 250 VAC), bir CAN alıcı-vericisi, Ethernet ve Wi-Fi tek kartta. ctrl32 ile hazır bir PLC'dir - röleler ve buton bir merdiven programının değişkenleridir, CAN sürücülerle ve G/Ç düğümleriyle konuşur ve operatör sayfası her tarayıcıda çalışır (WEBview). UEXT konnektörüne takılan isteğe bağlı 2,8" dokunmatik ekran onu küçük bir panele dönüştürür.

**Şunlar için uygun:**

- Ethernet'li bir röle kontrolcüsü - ısıtma, pompalar, aydınlatma
- Bir sürücü veya CANopen G/Ç düğümleri için CAN master
- İsteğe bağlı 2,8" ekranla bir termostat veya küçük bir panel

Kataloğda kartın sayfası: [Olimex ESP32-EVB](https://ctrl32.com/hardware/boards/olimex-esp32-evb/)

![Olimex ESP32-EVB - pin haritası: ctrl32'de her GPIO'nun işlevi](pinout/pinout.png)

## ctrl32 bu kartta neler yapabilir

<!-- capabilities:start -->
| Özellik | Bu kartta | Notlar |
|---|---|---|
| Çip | ESP32 (ESP32-WROOM-32E-N4) |  |
| Bellek | 4 MB flash |  |
| Program boyutu | 128 değişken, 32 alarm, 128 blok | editör yüklemeden önce kontrol eder |
| Dijital girişler / çıkışlar | 6 boş GPIO | 2 tanesi yalnızca giriş |
| Analog girişler | 4 çip üzerinde (ADC1) | GPIO32, GPIO33, GPIO34, GPIO36 |
| Ethernet | evet - LAN8710A |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 |  |
| Modbus RTU (RS-485) | evet - boş pinlerde | harici bir alıcı-verici gerektirir |
| Modbus TCP | istemci ve sunucu |  |
| MQTT | evet | Home Assistant keşfi (discovery) |
| WEBview | evet | her tarayıcıda operatör sayfası |
| Ekran / dokunmatik (HMI) | - 240x320, - |  |
| USB | Micro-USB (CH340T USB-UART) |  |
| Besleme | 5 V USB, 3.7 V Li-Po / Li-Ion |  |
<!-- capabilities:end -->

### Neler desteklenmez

- Bluetooth.
- IR alıcı ve verici - ctrl32 bu kartta bunları kullanmaz.
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

