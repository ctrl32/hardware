---
title: 'Makerfabs MaTouch ESP32-P4 7": Home dashboard örneği'
slug: home-dashboard
sidebar_position: 10
hardware: /hardware/boards/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/
image: img/screen.jpg
image_alt: Makerfabs MaTouch ESP32-P4 7" home dashboard örneğinin operatör sayfası
tags:
- esp32-p4
- display
- touch
- hmi
- ethernet
- makerfabs
- example
---

# Home dashboard

Koyu buzlu cam tarzında, tüm ev için bir kontrol paneli - oda başına ısıtma, PV ve bataryalı enerji, aydınlatma, garaj ve hava durumu - arkasında simüle edilmiş bir ev ile.

**İndir:** [home-dashboard.prj32](home-dashboard.prj32) - ctrl32 editöründe açın (**File → Open**).

## Ne yapar

Evin fotoğrafları üzerinde altı ekran, her biri bir dizi buzlu cam kart:

- **Home** - saat, hava durumu, odalar, alarm ve senaryolar.
- **Weather** - bugün ve sonraki günler.
- **Climate** - altı oda, her biri sıcaklığı, ayar değeri ve ısıtmasıyla;
  ısı pompası ve sıcak su tankı.
- **Energy** - PV çıkışı, evin yükü, batarya ve şebeke, günün kWh'si.
- **Lights** - odaların lambaları ve senaryoları.
- **Access** - garaj kapısı, araç şarj cihazı, alarm.

**SIM** programı evin kendisidir: dış sıcaklık günü, PV çıkışı güneşi
izler, yükün sabah ve akşam tepeleri vardır, odalar histerezisle ayar
değerlerine kadar ısınır. Gerçek bir evi sürmek için onun
değişkenlerini Modbus, MQTT veya CAN cihazlarınızla değiştirin.

## Ekranlar

**Ana sayfa**

![Panonun Home ekranı: saat, hava durumu, odalar, alarm ve senaryolar](img/home.jpg)

**İklim**

![Climate ekranı: sıcaklıkları ve ayar değerleriyle altı oda](img/climate.png)

**Enerji**

![Energy ekranı: PV, ev yükü, batarya ve şebeke](img/energy.jpg)

## Açın ve çalıştırın

1. `home-dashboard.prj32` dosyasını editörde açın.
2. Olduğu gibi çalıştırın - ev simüle edilmiştir; gerçek bir ev için SIM programının değişkenlerini kendi cihazlarınızla değiştirin.
3. PC'de denemek için **simülasyonu** (araç çubuğu) çalıştırın ya da karta yükleyin - bkz. [Runtime'ı kurun](../../install.tr.md).

## Ne görmelisiniz

Ana ekran saat, hava durumu ve odalarla açılır; simüle edilen gün
ilerledikçe değerler değişir. Bir odanın ayar değerine dokunmak onu
değiştirir ve oda o değere kadar ısınır.


---

[← Örnek projeler](../README.tr.md) | [Genel bakış](../../README.tr.md)
