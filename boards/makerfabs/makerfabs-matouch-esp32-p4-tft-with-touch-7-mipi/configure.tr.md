---
title: Makerfabs MaTouch ESP32-P4 7" kartını ctrl32 editöründe yapılandırın
slug: configure
sidebar_position: 40
image: img/configure-01-board.png
image_alt: Editörde Makerfabs MaTouch ESP32-P4 7" kart sayfası
tags:
- esp32-p4
- display
- touch
- hmi
- ethernet
- makerfabs
---

# Kartı yapılandırın

## Kart sayfası

Cihaz ağacında karta çift tıklayın. Sayfa kartın neler taşıdığını ve her pini gösterir: boş bir pin tek tıkla bir değişken alır - bir giriş, bir çıkış ya da analog yetenekli bir pinde analog bir giriş.

![Kart sayfası: boş pinler ve her birinin yapabildikleri](img/configure-01-board.png)

## Ağ

Ethernet portu kendiliğinden başlar ve adresini yönlendiricinizden alır
(DHCP). ESP32-C6'nın Wi-Fi'ı cihaz ağacının **WiFi** sayfasında ayarlanır -
ağ adı ve parola. Sabit bir adres kart sayfasında, **Network** bölümünde
ayarlanır.


## Girişler, çıkışlar ve değişkenler

Programın her sinyali bir **değişkendir**. Bir pindeki değişken pini okur veya sürer; analog bir değişken ona neyin bağlı olduğunu (bir gerilim, 4-20 mA, bir termistör) ve birim cinsinden aralığını söyler.

![all-in-one örneğinin değişkenleri](img/configure-03-variables.png)

## İletişim

**Modbus TCP.** Ağdaki bir cihaz **Ethernet → Modbus TCP master** altında eklenir; register'ları değişken olur.

**Modbus RTU / RS-485.** Kartta RS-485 alıcı-vericisi yoktur: 3,3 V'luk bir alıcı-verici modülünü boş pinlere (TX, RX ve yön pini DE) bağlayın ve bunları kart sayfasında adlandırın - örnek GPIO4 / GPIO5 / GPIO32 kullanır. ctrl32 bu hatta bir Modbus RTU master veya slave olur.

**CAN.** ESP32-P4'te bir CAN denetleyicisi (TWAI) vardır. Kartta CAN alıcı-vericisi yoktur: 3,3 V'luk bir alıcı-verici modülünü iki boş pine bağlayın ve bunları kart sayfasında adlandırın (**Bus pins**) - örnek GPIO20 / GPIO21 kullanır. CANopen cihazları, ham CAN çerçeveleri ve araç veri yolları (J1939) hepsi bunun üzerinde çalışır.

**MQTT.** Kart seçilen değişkenleri bir broker'a yayınlar; Home Assistant modunda broker bunları kendiliğinden bulur ve *write* olarak işaretlenen bir değişken oradan ayarlanabilir.

![MQTT sayfası: broker ve yayınlanan değişkenler](img/configure-05-mqtt.png)

## Ekran ve dokunmatik

Proje, camın kendi çözünürlüğü olan 1024 x 600'de çizilir. HMIview sayfası
yönü (monte edildiği gibi ya da döndürülmüş - dokunmatik de onu izler),
WEBview tuvalinin boyutunu ve açılış ekranını ayarlar. Dokunmatik ayar
gerektirmez: GT911 denetleyicisi kartın parçasıdır.

![HMIview ayarları: projenin üzerine çizdiği ekran](img/configure-04-display.png)

## WEBview

Kart operatör sayfasını ağdaki her tarayıcıya sunar - kartın adresini açın. Sayfa editörde bir ekran gibi çizilir.

![WEBview sayfası ayarları](img/configure-06-webview.png)

---

[← Runtime'ı kurun](install.tr.md) | [Genel bakış](README.tr.md) | [Örnek projeler →](examples/README.tr.md)
