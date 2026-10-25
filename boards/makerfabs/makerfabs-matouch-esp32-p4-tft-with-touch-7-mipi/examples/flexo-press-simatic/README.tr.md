---
title: 'Makerfabs MaTouch ESP32-P4 7": Flexo press on a SIMATIC örneği'
slug: flexo-press-simatic
sidebar_position: 10
hardware: /hardware/boards/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/
image: img/screen.png
image_alt: Makerfabs MaTouch ESP32-P4 7" flexo press on a simatic örneğinin operatör sayfası
tags:
- esp32-p4
- display
- touch
- hmi
- ethernet
- makerfabs
- example
---

# Flexo press on a SIMATIC

Bir SIMATIC S7-1200 ile kontrol edilen sekiz renkli bir flekso baskı makinesinin HMI'ı - hareket eden bandıyla makine, on altı baskı servosu, register, kurutucular, reçete olarak işler ve tanılama, S7 protokolü üzerinden.

**İndir:** [flexo-press-simatic.prj32](flexo-press-simatic.prj32) - ctrl32 editöründe açın (**File → Open**).

## Ne yapar

Açık renkli bir endüstriyel panelde altı sayfa:

- **Overview** - üzerinde bandın hareket ettiği bir çizim olarak makine,
  ünitelerin senkron lambaları, kurutucu sıcaklıkları, bant gerginlikleri
  ve rulo uzunlukları; START (onaylı), STOP, JOG, RESET.
- **Sections** - on altı baskı servosu: klişe silindirleri ve
  aniloks merdaneleri, senkronda, arıza, hız, etkin.
- **Register** - her ünitenin register hatası ve düzeltme.
- **Heating** - kurutma odaları ve köprü kurutucu.
- **Jobs** - panelde tutulan bir **reçete** olarak iş: yükle, kaydet,
  sil.
- **Diagnostics** - alarmlar, PLC bağlantısı ve hız ile gerginliğin bir
  trendi.

Panel bir **SIMATIC S7-1200** ile **+7** (S7 protokolü, ISO-on-TCP)
üzerinden konuşur: PLC'nin durum bloğu DB100'ü her 100 ms'de okur ve
ayar değerlerini ve komutlarını DB101'e yazar - PLC'de başka bir şey
gerekmez. **Demo modunda** (varsayılan olarak açık) SIM programı
makineyi panelin kendisinde çalıştırır.

## Ekranlar

**Genel bakış**

![Overview sayfası: hareket eden bant, gerginlikler ve kurutucularla makine çizimi](img/overview.png)

**Üniteler**

![Sections sayfası: durumlarıyla on altı baskı servosu](img/sections.png)

**İşler**

![Jobs sayfası: panelde tutulan bir reçete olarak iş](img/jobs.png)

## Açın ve çalıştırın

1. `flexo-press-simatic.prj32` dosyasını editörde açın.
2. Demo modunda olduğu gibi çalıştırın; bir PLC ile adresini +7 sayfasında ayarlayın ve iki veri bloğunu DB100 / DB101 oluşturun.
3. PC'de denemek için **simülasyonu** (araç çubuğu) çalıştırın ya da karta yükleyin - bkz. [Runtime'ı kurun](../../install.tr.md).

## Ne görmelisiniz

Genel bakış demo modunda açılır. START'a basın ve onaylayın: hat hızlanır,
bant çizimin üzerinde hareket eder ve gerginlikler oturur. Diagnostics
sayfasında demo modunu kapatın ve PLC'nin adresini ayarlayın - panel
artık gerçek makineyi gösterir.


---

[← Örnek projeler](../README.tr.md) | [Genel bakış](../../README.tr.md)
