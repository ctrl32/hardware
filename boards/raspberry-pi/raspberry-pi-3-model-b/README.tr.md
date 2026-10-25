---
title: Raspberry Pi 3 Model B+
slug: raspberry-pi-3-model-b
sidebar_position: 10
hardware: /hardware/boards/raspberry-pi-3-model-b/
image: img/board-01.jpg
image_alt: Raspberry Pi 3 Model B+ kartı, üstten görünüm
tags:
- raspberry-pi
- linux
- hmi
- opc-ua
---

# Raspberry Pi 3 Model B+

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: Linux](https://img.shields.io/badge/chip-Linux-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a) ![CAN: 1](https://img.shields.io/badge/CAN-1-7c3aed)

![Raspberry Pi 3 Model B+ kartı, üstten görünüm](img/board-01.jpg)

Raspberry Pi 3 Model B+ ctrl32 Linux runtime'ı çalıştırır: büyük bir program, HDMI monitörde bir HMI, SCADA için bir OPC UA sunucusu, HAT'ler veya USB adaptörleri üzerinden CAN ve RS-485, Modbus ve MQTT. 1 GB bellek ve dört çekirdekli Cortex-A53 ile bir hat kontrolcüsüne veya bir ağ geçidine uygundur; kamerayla görüntü işleme için bir Raspberry Pi 4 veya 5 gerekir.

**Şunlar için uygun:**

- HDMI monitörde HMI'ı ve SCADA'ya OPC UA'sı olan bir hat kontrolcüsü
- Servo sürücüler için bir EtherCAT master
- Modbus, CAN, OPC UA ve MQTT arasında bir ağ geçidi

Kataloğda kartın sayfası: [Raspberry Pi 3 Model B+](https://ctrl32.com/hardware/boards/raspberry-pi-3-model-b/)

![Raspberry Pi 3 Model B+ - pin haritası: ctrl32'de her GPIO'nun işlevi](pinout/pinout.png)

## ctrl32 bu kartta neler yapabilir

<!-- capabilities:start -->
| Özellik | Bu kartta | Notlar |
|---|---|---|
| Çip | Linux |  |
| Program boyutu | 20480 değişken, 4096 alarm, 40960 blok | editör yüklemeden önce kontrol eder |
| Dijital girişler / çıkışlar | G/Ç modülleri üzerinden | Modbus, CANopen, EtherCAT |
| Ethernet | evet |  |
| Wi-Fi | Wi-Fi 5 (2.4 + 5 GHz) |  |
| CAN | bir CAN HAT veya USB adaptörü üzerinden | SocketCAN, 4 veri yoluna kadar |
| Modbus RTU (RS-485) | evet | bir USB adaptörü veya bir HAT |
| Modbus TCP | istemci ve sunucu |  |
| MQTT | evet (TLS de) | Home Assistant keşfi (discovery) |
| WEBview | evet | her tarayıcıda operatör sayfası |
| OPC UA sunucusu | evet |  |
| EtherCAT master | evet | ikinci bir Ethernet portunda |
| Ekran (HMI) | HDMI veya bir DSI panel | ya da WEBview ile ekransız |
| USB | Micro-USB |  |
| Besleme | 5 V USB |  |
<!-- capabilities:end -->

### Neler desteklenmez

- Programın G/Ç'si olarak 40 pinli GPIO başlığı - girişler ve çıkışlar G/Ç modülleri üzerinden gelir (Modbus RTU / TCP, CANopen, EtherCAT); başlık HAT'lerin veri yollarını taşır.
- Bluetooth.
- Bir masaüstü ortamı - runtime ekranı kendisi çizer; istediği sistem Raspberry Pi OS Lite'tır.

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
- [Raspberry Pi 5](../raspberry-pi-5/README.tr.md)
- [Raspberry Pi 4 Model B](../raspberry-pi-4-model-b/README.tr.md)
- [Linux runtime](https://ctrl32.com/docs/linux-runtime/) - ne yaptığı ve sınırları

