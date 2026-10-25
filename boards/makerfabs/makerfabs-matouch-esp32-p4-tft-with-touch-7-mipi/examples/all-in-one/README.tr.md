---
title: 'Makerfabs MaTouch ESP32-P4 7": All-in-one örneği'
slug: all-in-one
sidebar_position: 10
hardware: /hardware/boards/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/
image: img/screen.png
image_alt: Makerfabs MaTouch ESP32-P4 7" all-in-one örneğinin operatör sayfası
tags:
- esp32-p4
- display
- touch
- hmi
- ethernet
- makerfabs
- example
---

# All-in-one

Dokunmatik ekrandan, iki butondan ve Home Assistant'tan kontrol edilen bir motor; bir basınç göstergesi, Modbus RTU sıcaklığına göre çalışan bir fan, bir Modbus TCP güç sayacı, CAN çerçeveleri, bir trend ve alarmlarla.

**İndir:** [all-in-one.prj32](all-in-one.prj32) - ctrl32 editöründe açın (**File → Open**).

## Ne yapar

Program küçük bir makine kontrolcüsüdür:

- **Start**, GPIO47 üzerindeki bir butondan, ekrandaki **Start**'tan
  ya da MQTT üzerinden Home Assistant'tan gelir; **Stop**, GPIO48
  üzerindeki bir butondan, ekrandaki **Stop**'tan ya da basıncın
  **CAN** üzerinden gelen ayar değerinin (çerçeve 0x201) üzerine
  çıkmasından gelir.
- Mühürleme, **GPIO33** üzerindeki motor çıkışını sürer; bir sayaç
  başlatma sayısını elektrik kesintisinde de korur.
- **Basınç**, I2C veri yolundaki bir **ADS1115** üzerinden analog bir
  giriştir (1:4 bölücüyle 0-10 V, 0-10 bar) ve her 100 ms'de CAN
  üzerinden gönderilir (çerçeve 0x181).
- **Sıcaklık** bir **Modbus RTU** sensöründen gelir (unit 1, input
  register 1, 0,1 °C); bir fan onu histerezisle izler.
- Bir **Modbus TCP** sayacı güç talebini verir.
- Camda üç **ekran**: genel bakış, bir trend ve alarmlar; her
  tarayıcıda daha basit bir sayfa (WEBview).

## Program

![Örneğin merdiven programı](img/ladder.png)

## Operatör sayfası

![Simülasyonda çalışan operatör sayfası](img/screen.png)

## Açın ve çalıştırın

1. `all-in-one.prj32` dosyasını editörde açın.
2. Adresleri (Modbus cihazı, MQTT broker'ı) kendi ağınızınkilerle değiştirin.
3. PC'de denemek için **simülasyonu** (araç çubuğu) çalıştırın ya da karta yükleyin - bkz. [Runtime'ı kurun](../../install.tr.md).

## Ne görmelisiniz

Camda genel bakış açılır. **Start**'a basın: motor LED'i yanar ve
başlatma sayacı artar. Gösterge basıncı gösterir, Trend ekranı onu
sıcaklıkla birlikte çizer ve basınç 8 bar'ı aştığında Alarms ekranında
bir alarm belirir.


---

[← Örnek projeler](../README.tr.md) | [Genel bakış](../../README.tr.md)
