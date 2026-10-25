---
title: Raspberry Pi 5
slug: raspberry-pi-5
sidebar_position: 10
hardware: /hardware/boards/raspberry-pi-5/
image: img/board-01.jpg
image_alt: Raspberry Pi 5 kartı, üstten görünüm
tags:
- raspberry-pi
- linux
- hmi
- opc-ua
- ethercat
---

# Raspberry Pi 5

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: Linux](https://img.shields.io/badge/chip-Linux-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a) ![CAN: 1](https://img.shields.io/badge/CAN-1-7c3aed)

![Raspberry Pi 5 kartı, üstten görünüm](img/board-01.jpg)

Raspberry Pi 5 ctrl32 Linux runtime'ı çalıştırır - ctrl32'nin en büyük hedefi: on binlerce değişken, HDMI monitörde bir HMI, SCADA için bir OPC UA sunucusu, EtherCAT sürücüler, HAT'ler veya USB adaptörleri üzerinden CAN ve RS-485 ve kamerayla makine görüşü. Editör runtime'ı ağ üzerinden kurar; Pi ardından onu her açılışta başlatır.

**Şunlar için uygun:**

- HDMI monitörde HMI'ı ve SCADA'ya OPC UA'sı olan bir hat kontrolcüsü
- Servo sürücüler için bir EtherCAT master
- Modbus, CAN, OPC UA ve MQTT arasında bir ağ geçidi

Kataloğda kartın sayfası: [Raspberry Pi 5](https://ctrl32.com/hardware/boards/raspberry-pi-5/)

![Raspberry Pi 5 - pin haritası: ctrl32'de her GPIO'nun işlevi](pinout/pinout.png)

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
| USB | USB-C |  |
| Besleme | USB-C PD 5 V / 5 A |  |
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

| Dosya | Ne |
|---|---|
| [pinout/pinout.svg](pinout/pinout.svg) | pin haritası, vektörel (ayrıca [PNG](pinout/pinout.png)) |
| [raspberry-pi-5-mechanical-drawing.pdf](datasheets/raspberry-pi-5-mechanical-drawing.pdf) | Raspberry Pi 5 mechanical drawing |
| [raspberry-pi-5-rp1-peripherals.pdf](datasheets/raspberry-pi-5-rp1-peripherals.pdf) | RP1 peripherals |
| [raspberry-pi-5-3d.zip](3d/raspberry-pi-5-3d.zip) | 3D model (GLB, zip olarak) |
| [NOTICE](https://github.com/ctrl32/hardware/blob/main/NOTICE.md) | fotoğrafların, şemaların ve modellerin nereden geldiği |

## Sonraki adımlar

- [ctrl32 belgeleri](https://ctrl32.com/docs/) - editör, diller, her blok
- [Editörü indirin](https://ctrl32.com/download/)
- Tüm test edilmiş kartlar
- Raspberry Pi 4 Model B
- Raspberry Pi 3 Model B+
- [Linux runtime](https://ctrl32.com/docs/linux-runtime/) - ne yaptığı ve sınırları

