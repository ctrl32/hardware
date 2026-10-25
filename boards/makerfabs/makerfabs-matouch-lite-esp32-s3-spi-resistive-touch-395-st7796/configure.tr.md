---
title: Makerfabs MaTouch Lite ESP32-S3 3.95" kartını ctrl32 editöründe yapılandırın
slug: configure
sidebar_position: 40
image: img/configure-01-board.png
image_alt: Editörde Makerfabs MaTouch Lite ESP32-S3 3.95" kart sayfası
tags:
- esp32-s3
- display
- touch
- hmi
- wifi
- makerfabs
---

# Kartı yapılandırın

## Kart sayfası

Cihaz ağacında karta çift tıklayın. Sayfa kartın neler taşıdığını ve her pini gösterir: boş bir pin tek tıkla bir değişken alır - bir giriş, bir çıkış ya da analog yetenekli bir pinde analog bir giriş.

![Kart sayfası: boş pinler ve her birinin yapabildikleri](img/configure-01-board.png)

## Ağ

Kart Wi-Fi ağınıza bağlanır: cihaz ağacının **WiFi** sayfasını açın ve
ağın adını ve parolasını yazın (örnekte yer tutucular vardır). Sabit bir
adres kart sayfasında, **Network** bölümünde ayarlanır.


## Girişler, çıkışlar ve değişkenler

Programın her sinyali bir **değişkendir**. Bir pindeki değişken pini okur veya sürer; analog bir değişken ona neyin bağlı olduğunu (bir gerilim, 4-20 mA, bir termistör) ve birim cinsinden aralığını söyler.

![all-in-one örneğinin değişkenleri](img/configure-03-variables.png)

## İletişim

**Modbus TCP.** Ağdaki bir cihaz **Ethernet → Modbus TCP master** altında eklenir; register'ları değişken olur.

**Modbus RTU / RS-485.** Kartta RS-485 alıcı-vericisi yoktur ve örneğin G/Ç'sinin yanında bunun için yeterli boş pin de yoktur; Modbus cihazlarına Wi-Fi üzerinden Modbus TCP ile ulaşılır.

**CAN.** ESP32-S3'te bir CAN denetleyicisi (TWAI) vardır. Kartta alıcı-verici yoktur: 3,3 V'luk bir alıcı-verici modülünü iki boş pine bağlayın ve bunları kart sayfasında adlandırın (**Bus pins**); örnek GPIO6 / GPIO7 kullanır.

**MQTT.** Kart seçilen değişkenleri bir broker'a yayınlar; Home Assistant modunda broker bunları kendiliğinden bulur ve *write* olarak işaretlenen bir değişken oradan ayarlanabilir.

![MQTT sayfası: broker ve yayınlanan değişkenler](img/configure-05-mqtt.png)

## Ekran ve dokunmatik

Cam 320 x 480'dir, monte edildiği haliyle dikey; HMIview sayfası resmi
döndürür (dokunmatik de onu izler) ve açılış ekranını ayarlar. Rezistif
dokunmatik sıkı basmayı gerektirir - butonları en az 40 px yüksekliğinde
çizin.

![HMIview ayarları: projenin üzerine çizdiği ekran](img/configure-04-display.png)

## WEBview

Kart operatör sayfasını ağdaki her tarayıcıya sunar - kartın adresini açın. Sayfa editörde bir ekran gibi çizilir.

![WEBview sayfası ayarları](img/configure-06-webview.png)

---

[← Runtime'ı kurun](install.tr.md) | [Genel bakış](README.tr.md) | [Örnek projeler →](examples/README.tr.md)
