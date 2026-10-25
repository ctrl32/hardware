---
title: 'Makerfabs MaTouch ESP32-P4 7": sorun giderme'
slug: troubleshooting
sidebar_position: 90
image: img/board-01.jpg
image_alt: Makerfabs MaTouch ESP32-P4 7"
tags:
- esp32-p4
- display
- touch
- hmi
- ethernet
- makerfabs
- troubleshooting
---

# Sorun giderme

| Belirti | Neden | Çözüm |
|---|---|---|
| COM portu görünmüyor | Kablo yalnızca güç taşıyor ya da CH340 sürücüsü eksik | Bir USB-C veri kablosu kullanın; CH340 sürücüsünü (WCH CH341SER) kurun; başka bir USB portu deneyin. |
| Ekran açılırken kart yeniden başlıyor | Besleme arka aydınlatmayı taşıyamıyor | 5 V / 2 A'lik bir adaptör ya da beslemeli bir USB hub kullanın. |
| Runtime yazıldıktan sonra ekran karanlık kalıyor | Kartta henüz proje yok | Projeyi karta yükleyin (F5); projesi olmayan bir kart camda hiçbir şey göstermez. |
| Dokunmatik tepki vermiyor ya da yanlış yerde tepki veriyor | Projenin yönü, kartın monte edildiği biçimden farklı | Yönü HMIview sayfasında ayarlayın ve yeniden yükleyin. |
| Ağ açılmıyor | DHCP sunucusu yok ya da portta bağlantı yok | Soketteki bağlantı LED'lerini kontrol edin; kart sayfasında sabit bir adres ayarlayın; Wi-Fi için ağ adını ve parolayı kontrol edin. |
| CAN sessiz kalıyor | Alıcı-verici yok, 120 ohm sonlandırma yok ya da bit hızı farklı | GPIO20 / GPIO21 üzerindeki alıcı-vericiyi, veri yolunun iki ucundaki 120 ohm direnci ve her düğümde aynı bit hızını kontrol edin. |
| Bir Modbus RTU değeri 0'da kalıyor | A ile B yer değiştirmiş, unit veya baud hızı yanlış ya da DE pini eksik | A ile B'yi yer değiştirin; unit'i, baud hızını ve pariteyi kontrol edin; DE'nin bağlı ve adlandırılmış olduğunu kontrol edin. |

Editörün **Messages** bölmesi ve kartın **tanılama arabelleği** (Online → Diagnostics), runtime'ın neye ve neden karar verdiğini söyler - önce onları okuyun.

---

[← Örnek projeler](examples/README.tr.md) | [Genel bakış](README.tr.md)
