---
title: 'Olimex ESP32-P4-PC: All-in-one örneği'
slug: all-in-one
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-p4-pc/
image: img/screen.png
image_alt: Olimex ESP32-P4-PC all-in-one örneğinin operatör sayfası
tags:
- esp32-p4
- ethernet
- ups
- olimex
- example
---

# All-in-one

Start / stop'lu bir motor çıkışı, bir çalışma zamanlayıcısı, bir Modbus RTU sıcaklığı, CAN çerçeveleri, bir Modbus TCP sayacı, MQTT ve tarayıcıda operatör sayfası.

**İndir:** [all-in-one.prj32](all-in-one.prj32) - ctrl32 editöründe açın (**File → Open**).

## Ne yapar

Program küçük bir makine kontrolcüsüdür - çoğu makinenin biçimi:

- **Start** şunlardan gelir: GPIO14 üzerindeki buton, operatör sayfasındaki **Start** veya MQTT üzerinden Home Assistant.
- **Stop**, **Stop**'tan, düşük seviyeden ya da çalışma süresinin dolmasından gelir - mühürleme **GPIO2** üzerindeki çıkışı bırakır.
- **Çalışma süresi** dakika olarak ayarlanır ve elektrik kesintisinde korunur.
- **Seviye** sayfada ayarlanan bir değişkendir (kartta boş analog pin kalmamıştır).
- Kartın RS-485'indeki bir **Modbus RTU** sensörü sıcaklığı verir (unit 1, input register 1).
- **CAN** seviyeyi ve çıkış durumunu her 100 ms'de 0x181 çerçevesinde gönderir ve 0x201 çerçevesinde bir ayar değeri alır.
- Ağdaki bir **Modbus TCP** enerji sayacı güç talebini verir (192.168.1.60 - bunu kendi sayacınıza göre değiştirin).
- **MQTT** değerleri bir Home Assistant broker'ına yayınlar; broker bunları kendiliğinden bulur; çıkış Home Assistant'tan da başlatılabilir.
- **WEBview** operatör sayfasını ağdaki her tarayıcıya sunar.

## Program

![Örneğin merdiven programı](img/ladder.png)

## Operatör sayfası

![Simülasyonda çalışan operatör sayfası](img/screen.png)

## Açın ve çalıştırın

1. `all-in-one.prj32` dosyasını editörde açın.
2. Adresleri (Modbus cihazı, MQTT broker'ı) kendi ağınızınkilerle değiştirin.
3. PC'de denemek için **simülasyonu** (araç çubuğu) çalıştırın ya da karta yükleyin - bkz. [Runtime'ı kurun](../../install.tr.md).

## Ne görmelisiniz

GPIO14 üzerindeki butona basın: GPIO2 üzerindeki çıkış devreye girer ve sayfadaki LED'i yanar. Çalışma süresi dolunca kendiliğinden kapanır. Home Assistant'ta kart değerleriyle görünür.


---

[← Örnek projeler](../README.tr.md) | [Genel bakış](../../README.tr.md)
