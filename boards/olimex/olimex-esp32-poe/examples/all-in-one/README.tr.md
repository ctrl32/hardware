---
title: 'Olimex ESP32-PoE: All-in-one örneği'
slug: all-in-one
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-poe/
image: img/screen.png
image_alt: Olimex ESP32-PoE all-in-one örneğinin operatör sayfası
tags:
- esp32
- ethernet
- poe
- olimex
- example
---

# All-in-one

Kartın butonu, operatör sayfası ve Home Assistant ile kontrol edilen bir pompa; bir seviye girişi, bir çalışma zamanlayıcısı, bir seviye alarmı ve bir Modbus TCP enerji sayacıyla.

**İndir:** [all-in-one.prj32](all-in-one.prj32) - ctrl32 editöründe açın (**File → Open**).

## Ne yapar

Program küçük bir pompa kontrolcüsüdür - çoğu makinenin biçimi:

- **Start**, kartın butonundan (BUT1), operatör sayfasındaki **Start**
  butonundan ya da MQTT üzerinden Home Assistant'tan gelir.
- **Stop**, **Stop** butonundan, düşük seviyeden ya da çalışma
  süresinin dolmasından gelir - mühürleme GPIO33'teki çıkışı bırakır.
- **Seviye**, GPIO35 üzerinde analog bir giriştir (0 - 3,3 V, 0 - 100 %
  aralığına ölçeklenir). %10'un altında pompa durur ve bir alarm
  verilir; %15'in üzerinde yeniden başlayabilir (histerezis).
- **Çalışma süresi** sayfada dakika olarak ayarlanır ve elektrik
  kesintisinde korunur (kalıcı bir değişken).
- Ağdaki bir **Modbus TCP** enerji sayacı şebeke gerilimini verir
  (register 0, input register'lar, 192.168.1.60 adresinde unit 1 -
  bunu kendi sayacınıza göre değiştirin). 253 V'un üzerinde bir alarm
  verilir.
- **CAN** (GPIO4 / GPIO36 üzerinde bir alıcı-verici) seviyeyi ve pompa
  durumunu her 100 ms'de 0x181 çerçevesinde gönderir ve 0x201'de bir
  ayar değeri alır.
- **MQTT** seviyeyi, pompa durumunu ve gerilimi bir Home Assistant
  broker'ına yayınlar; broker bunları kendiliğinden bulur (discovery);
  pompa Home Assistant'tan başlatılabilir.
- **WEBview** operatör sayfasını - pompayı, seviyeyi, trendini ve
  alarmları - ağdaki her tarayıcıya sunar.

## Program

![Örneğin merdiven programı](img/ladder.png)

## Operatör sayfası

![Simülasyonda çalışan operatör sayfası](img/screen.png)

## Açın ve çalıştırın

1. `all-in-one.prj32` dosyasını editörde açın.
2. Adresleri (Modbus cihazı, MQTT broker'ı) kendi ağınızınkilerle değiştirin.
3. PC'de denemek için **simülasyonu** (araç çubuğu) çalıştırın ya da karta yükleyin - bkz. [Runtime'ı kurun](../../install.tr.md).

## Ne görmelisiniz

Potansiyometre açıkken BUT1'e basın: GPIO33'teki röle devreye girer ve
sayfadaki pompa LED'i yanar. Potansiyometreyi %10'un altına çevirin:
pompa durur ve alarm tabloda belirir. Home Assistant'ta kart seviyesi,
pompası ve gerilimiyle görünür.


---

[← Örnek projeler](../README.tr.md) | [Genel bakış](../../README.tr.md)
