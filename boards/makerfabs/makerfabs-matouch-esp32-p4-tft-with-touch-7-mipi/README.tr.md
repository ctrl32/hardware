---
title: Makerfabs MaTouch ESP32-P4 7"
slug: makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi
sidebar_position: 10
hardware: /hardware/boards/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/
image: img/board-01.jpg
image_alt: 1024x600 dokunmatik ekranıyla Makerfabs MaTouch ESP32-P4 7 inç kartı
tags:
- esp32-p4
- display
- touch
- hmi
- ethernet
- makerfabs
---

# Makerfabs MaTouch ESP32-P4 7"

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32-P4](https://img.shields.io/badge/chip-ESP32--P4-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a) ![CAN: 1](https://img.shields.io/badge/CAN-1-7c3aed) ![HMI: 1024x600](https://img.shields.io/badge/HMI-1024x600-0891b2)

![1024x600 dokunmatik ekranıyla Makerfabs MaTouch ESP32-P4 7 inç kartı](img/board-01.jpg)

Makerfabs MaTouch ESP32-P4 7", tek kart üzerinde eksiksiz bir dokunmatik paneldir: kapasitif dokunmatik 1024 x 600 MIPI ekran, 32 MB PSRAM'li çift çekirdekli ESP32-P4, Ethernet ve bir ESP32-C6 üzerinden Wi-Fi 6. ctrl32 ile HMI ve PLC bir aradadır - editörde çizilen ekranlar camda çalışır, yanında bir merdiven programı çalışır ve aynı değerler her tarayıcıya (WEBview), Modbus cihazlarına, CAN'e ve MQTT'ye ulaşır.

**Şunlar için uygun:**

- Kendi mantığı olan, bir makine üzerinde operatör paneli
- Duvarda bir akıllı ev veya bina kontrol paneli
- Ekranlı bir Modbus / CAN ağ geçidi

Kataloğda kartın sayfası: [Makerfabs MaTouch ESP32-P4 7"](https://ctrl32.com/hardware/boards/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/)

![Makerfabs MaTouch ESP32-P4 7" - pin haritası: ctrl32'de her GPIO'nun işlevi](pinout/pinout.png)

## ctrl32 bu kartta neler yapabilir

<!-- capabilities:start -->
| Özellik | Bu kartta | Notlar |
|---|---|---|
| Çip | ESP32-P4 (ESP32-P4NRW32) |  |
| Bellek | 16 MB flash, 32 MB PSRAM |  |
| Program boyutu | 4096 değişken, 512 alarm, 512 blok | editör yüklemeden önce kontrol eder |
| Dijital girişler / çıkışlar | 12 boş GPIO | pin haritasına bakın |
| Analog girişler | bir I2C ADC üzerinden (ADS1115) |  |
| Ethernet | evet - IP101GRI |  |
| Wi-Fi | Wi-Fi 6 (2.4 GHz) |  |
| CAN (TWAI) | 1 | harici bir alıcı-verici gerektirir |
| Modbus RTU (RS-485) | evet | boş pinlerde, harici bir alıcı-verici gerektirir |
| Modbus TCP | istemci ve sunucu |  |
| MQTT | evet (TLS de) | Home Assistant keşfi (discovery) |
| WEBview | evet | her tarayıcıda operatör sayfası |
| Ekran / dokunmatik (HMI) | 7" 1024x600, GT911 |  |
| USB | USB-C (CH340K USB-UART, Native USB) |  |
| Besleme | 5 V USB (4.0–5.25 V), 3.7 V Li-Po / Li-Ion |  |
<!-- capabilities:end -->

### Neler desteklenmez

- Kamera (MIPI CSI üzerinde SC2336) - ctrl32 görüntü işlemeyi yalnızca 64 bit Linux runtime'da çalıştırır.
- Ses codec'i, mikrofon ve hoparlör çıkışı.
- ESP32-C6'nın Bluetooth'u.
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
| [makerfabs-matouch_esp32-p4_tft_with_touch_7_v1.2.pdf](schematics/makerfabs-matouch_esp32-p4_tft_with_touch_7_v1.2.pdf) | MaTouch ESP32-P4 TFT with Touch 7“ V1.2 |
| [makerfabs-matouch-p4-7-display-datasheet.pdf](datasheets/makerfabs-matouch-p4-7-display-datasheet.pdf) | 7" 1024x600 MIPI display AML070JGI50 datasheet |
| [makerfabs-matouch-p4-es8311-datasheet.pdf](datasheets/makerfabs-matouch-p4-es8311-datasheet.pdf) | ES8311 audio codec datasheet |
| [esp32-p4-datasheet.pdf](datasheets/esp32-p4-datasheet.pdf) | ESP32-P4 datasheet (pre-release) |
| [makerfabs-matouch-p4-sc2336-camera-datasheet.pdf](datasheets/makerfabs-matouch-p4-sc2336-camera-datasheet.pdf) | SC2336 2 MP MIPI camera module datasheet |
| [NOTICE](https://github.com/ctrl32/hardware/blob/main/NOTICE.md) | fotoğrafların, şemaların ve modellerin nereden geldiği |

## Sonraki adımlar

- [ctrl32 belgeleri](https://ctrl32.com/docs/) - editör, diller, her blok
- [Editörü indirin](https://ctrl32.com/download/)
- Tüm test edilmiş kartlar
- Makerfabs MaTouch Lite ESP32-S3 3.95" - küçük kardeşi
- [MaTouch ESP32-P4 üzerinde akıllı ev kontrol paneli](https://ctrl32.com/examples/smart-home-control-panel-on-an-esp32-p4-7-touch-display/) - web'de eksiksiz bir örnek

