---
title: 'Makerfabs MaTouch ESP32-P4 7": Car cockpit örneği'
slug: car-cockpit
sidebar_position: 10
hardware: /hardware/boards/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/
image: img/screen.png
image_alt: Makerfabs MaTouch ESP32-P4 7" car cockpit örneğinin operatör sayfası
tags:
- esp32-p4
- display
- touch
- hmi
- ethernet
- makerfabs
- example
---

# Car cockpit

Bir J1939 araç veri yolunda bir gösterge paneli - hız ve devir göstergeleri, vites, yakıt, soğutma sıvısı, uyarı lambaları, veri yolundaki kontrol üniteleri, sözcüklerle aktif arıza kodu ve sürücünün ayarları.

**İndir:** [car-cockpit.prj32](car-cockpit.prj32) - ctrl32 editöründe açın (**File → Open**).

## Ne yapar

7" camda beş ekran:

- **Cockpit** - hız ve devir göstergeleri, vites, yakıt, soğutma sıvısı
  ve akü, kilometre sayacı ve yolculuk, saat, sinyaller ve uyarı
  lambaları.
- **Engine** - motorun değerleri ayrıntılı olarak.
- **Bus** - **J1939** ağı: panelin düğümü, motor, şanzıman ve frenler
  ve yanıt verip vermedikleri, DM1 lambaları, parametre grubuyla
  birlikte her sinyal.
- **Faults** - alarm listesi ve motorun aktif arıza kodu (SPN / FMI /
  sayı) ile sözcüklerle anlamı.
- **Settings** - demo modu, birimler, hız uyarısı, kırmızı bölge,
  soğutma sıvısı ve yakıt uyarıları, servis aralığı.

İletişim, kartın CAN'i üzerinde **SAE J1939**'dur (GPIO47 / GPIO48
üzerinde 3,3 V'luk bir alıcı-verici, 250 kbit/s): motor, şanzıman ve
frenler parametre gruplarını yayınlar ve panel onları okur - bir
değerin gelmesi için program gerekmez. **Demo modunda** (varsayılan
olarak açık) SIM programı bir sürüş döngüsü yürütür: kalkış, vites
değiştirme, seyir, frenleme, duruş - ve arada bir arıza.

## Ekranlar

**Kokpit**

![Cockpit ekranı: hız ve devir göstergeleri, vites, yakıt, soğutma sıvısı ve uyarı lambaları](img/cockpit.png)

**Veri yolu**

![J1939 Bus ekranı: kontrol üniteleri ve panelin okuduğu sinyaller](img/bus.png)

**Arızalar**

![Faults ekranı: alarm listesi ve aktif arıza kodu](img/faults.png)

## Açın ve çalıştırın

1. `car-cockpit.prj32` dosyasını editörde açın.
2. Demo modunda olduğu gibi çalıştırın; bir araçta CAN alıcı-vericisini GPIO47 / GPIO48'e bağlayın ve Settings ekranında demo modunu kapatın.
3. PC'de denemek için **simülasyonu** (araç çubuğu) çalıştırın ya da karta yükleyin - bkz. [Runtime'ı kurun](../../install.tr.md).

## Ne görmelisiniz

Gösterge paneli demo modunda açılır: ibreler sürüş döngüsü boyunca
hareket eder, vites değişir, sinyaller yanıp söner. Settings ekranında
demo modunu kapatın ve veri yolunu bağlayın - göstergeler artık aracı
gösterir.


---

[← Örnek projeler](../README.tr.md) | [Genel bakış](../../README.tr.md)
