---
title: Olimex ESP32-P4-PC kartını ctrl32 editöründe yapılandırın
slug: configure
sidebar_position: 40
image: img/configure-01-board.png
image_alt: Editörde Olimex ESP32-P4-PC kart sayfası
tags:
- esp32-p4
- ethernet
- ups
- olimex
---

# Kartı yapılandırın

## Kart sayfası

Cihaz ağacında karta çift tıklayın. Sayfa kartın neler taşıdığını ve her pini gösterir: boş bir pin tek tıkla bir değişken alır - bir giriş, bir çıkış ya da analog yetenekli bir pinde analog bir giriş.

![Kart sayfası: boş pinler ve her birinin yapabildikleri](img/configure-01-board.png)

## Ağ

Ethernet portu kendiliğinden başlar ve adresini yönlendiricinizden alır
(DHCP). Sabit bir adres kart sayfasında, **Network** bölümünde ayarlanır.
Kartta Wi-Fi yoktur.


## Girişler, çıkışlar ve değişkenler

Programın her sinyali bir **değişkendir**. Bir pindeki değişken pini okur veya sürer; analog bir değişken ona neyin bağlı olduğunu (bir gerilim, 4-20 mA, bir termistör) ve birim cinsinden aralığını söyler.

![all-in-one örneğinin değişkenleri](img/configure-03-variables.png)

## İletişim

**Modbus TCP.** Ağdaki bir cihaz **Ethernet → Modbus TCP master** altında eklenir; register'ları değişken olur.

**Modbus RTU / RS-485.** Kartta RS-485 alıcı-vericisi yoktur: 3,3 V'luk bir alıcı-verici modülünü boş EXT1 pinlerine (TX, RX ve yön pini DE) bağlayın ve bunları kart sayfasında adlandırın - ctrl32 bu hatta bir Modbus RTU master veya slave olur.

**CAN.** ESP32-P4'te bir CAN denetleyicisi (TWAI) vardır. Kartta alıcı-verici yoktur: 3,3 V'luk bir CAN alıcı-verici modülünü iki boş EXT1 pinine bağlayın ve bunları kart sayfasında adlandırın (**Bus pins**).

**MQTT.** Kart seçilen değişkenleri bir broker'a yayınlar; Home Assistant modunda broker bunları kendiliğinden bulur ve *write* olarak işaretlenen bir değişken oradan ayarlanabilir.

![MQTT sayfası: broker ve yayınlanan değişkenler](img/configure-05-mqtt.png)

## WEBview

Kart operatör sayfasını ağdaki her tarayıcıya sunar - kartın adresini açın. Sayfa editörde bir ekran gibi çizilir.

![WEBview sayfası ayarları](img/configure-06-webview.png)

---

[← Runtime'ı kurun](install.tr.md) | [Genel bakış](README.tr.md) | [Örnek projeler →](examples/README.tr.md)
