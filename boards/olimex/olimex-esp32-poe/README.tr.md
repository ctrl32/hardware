---
title: Olimex ESP32-PoE
slug: olimex-esp32-poe
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-poe/
image: img/board-01.jpg
image_alt: Olimex ESP32-PoE kartı, üstten görünüm, Ethernet soketi ve USB konnektörüyle
tags:
- esp32
- ethernet
- poe
- olimex
---

# Olimex ESP32-PoE

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32](https://img.shields.io/badge/chip-ESP32-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a)

![Olimex ESP32-PoE kartı, üstten görünüm, Ethernet soketi ve USB konnektörüyle](img/board-01.jpg)

Olimex ESP32-PoE, Ethernet ve Power over Ethernet özellikli, açık kaynaklı bir ESP32 kartıdır: tek bir ağ kablosu onu besler ve bağlantısını taşır. ctrl32 ile bir pano veya duvar kutusu için kompakt bir PLC olur - çipte bir merdiven programı, ağdaki her tarayıcıya sunulan operatör sayfası (WEBview), sayaçlara ve G/Ç modüllerine Modbus TCP ve Home Assistant'a ya da herhangi bir broker'a MQTT.

**Şunlar için uygun:**

- Bir PoE switch'ten beslenen, panoda küçük bir PLC
- Sayaçları okuyup MQTT üzerinden yayınlayan bir Modbus TCP ağ geçidi
- Ev otomasyonu - tek kabloda bir oda veya bir kazan dairesi

Kataloğda kartın sayfası: [Olimex ESP32-PoE](https://ctrl32.com/hardware/boards/olimex-esp32-poe/)

![Olimex ESP32-PoE - pin haritası: ctrl32'de her GPIO'nun işlevi](pinout/pinout.png)

## ctrl32 bu kartta neler yapabilir

<!-- capabilities:start -->
| Özellik | Bu kartta | Notlar |
|---|---|---|
| Çip | ESP32 (ESP32-WROOM-32E-N4) |  |
| Bellek | 4 MB flash |  |
| Program boyutu | 128 değişken, 32 alarm, 128 blok | editör yüklemeden önce kontrol eder |
| Dijital girişler / çıkışlar | 6 boş GPIO | 3 tanesi yalnızca giriş |
| Analog girişler | 4 çip üzerinde (ADC1) | GPIO33, GPIO34, GPIO35, GPIO36 |
| Ethernet | evet - LAN8710A |  |
| Power over Ethernet | IEEE 802.3af |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 - boş pinlerde | harici bir alıcı-verici gerektirir |
| Modbus RTU (RS-485) | evet - boş pinlerde | harici bir alıcı-verici gerektirir |
| Modbus TCP | istemci ve sunucu |  |
| MQTT | evet | Home Assistant keşfi (discovery) |
| WEBview | evet | her tarayıcıda operatör sayfası |
| Ekran / dokunmatik (HMI) | hayır | operatör sayfası WEBview'dur |
| USB | Micro-USB (CH340T USB-UART) |  |
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

| Dosya | Ne |
|---|---|
| [pinout/pinout.svg](pinout/pinout.svg) | pin haritası, vektörel (ayrıca [PNG](pinout/pinout.png)) |
| [olimex-esp32-poe-schematic.pdf](schematics/olimex-esp32-poe-schematic.pdf) | ESP32-PoE schematic Rev M2 |
| [esp32-poe-revm2.zip](schematics/esp32-poe-revm2.zip) | KiCad project |
| [olimex-esp32-poe-user-manual.pdf](datasheets/olimex-esp32-poe-user-manual.pdf) | ESP32-PoE user manual |
| [olimex-esp32-poe.zip](3d/olimex-esp32-poe.zip) | 3D model (STEP, zip olarak) |
| [NOTICE](https://github.com/ctrl32/hardware/blob/main/NOTICE.md) | fotoğrafların, şemaların ve modellerin nereden geldiği |

## Sonraki adımlar

- [ctrl32 belgeleri](https://ctrl32.com/docs/) - editör, diller, her blok
- [Editörü indirin](https://ctrl32.com/download/)
- Tüm test edilmiş kartlar
- Olimex ESP32-PoE-ISO - yalıtılmış PoE beslemeli aynı kart
- Olimex ESP32-POE2 - yeni nesil

