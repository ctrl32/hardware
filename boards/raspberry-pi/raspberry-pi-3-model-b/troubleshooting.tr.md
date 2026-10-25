---
title: 'Raspberry Pi 3 Model B+: sorun giderme'
slug: troubleshooting
sidebar_position: 90
image: img/board-01.jpg
image_alt: Raspberry Pi 3 Model B+
tags:
- raspberry-pi
- linux
- hmi
- opc-ua
- troubleshooting
---

# Sorun giderme

| Belirti | Neden | Çözüm |
|---|---|---|
| Look at the device bağlanamıyor | SSH kapalı, adres yanlış ya da PC başka bir ağda | Imager'ın ayarlarında SSH'yi etkinleştirin ve kartı yeniden yazın; adrese PC'den ping atın. |
| Prepare kurulum önermiyor | ctrl32 runtime Pi'de zaten kurulu | Kurulu bir runtime, port seçicide Pi'nin adresiyle Flash runtime kullanılarak güncellenir. |
| Proje yüklendikten sonra monitör siyah kalıyor | Monitör açılıştan sonra bağlandı ya da projede ekran yok | Monitörü Pi'yi açmadan önce bağlayın; projeye bir ekran ekleyin. |
| WEBview açılmıyor | Yanlış port | http://<adres>:8080 adresini açın - runtime 8080 portunda sunar. |
| USB-RS485 adaptörü kayboluyor | Düşük gerilim - adaptör çok zayıf | Resmi 27 W'lık adaptörü kullanın. |
| CAN sessiz kalıyor | HAT'in sürücüsü yüklenmemiş, sonlandırma yok ya da bit hızı farklı | HAT'i Prepare a Linux device içinde işaretleyin; veri yolunun iki ucunda 120 ohm'luk bir direnç; her düğümde aynı bit hızı. |
| Bir OPC UA istemcisi hiçbir değişken görmüyor | Değişken sunucunun dışında tutuluyor ya da bir güvenlik duvarı 4840 portunu engelliyor | Değişken listesindeki OPC UA işaretini kontrol edin; 4840 portunu açın. |

Editörün **Messages** bölmesi ve kartın **tanılama arabelleği** (Online → Diagnostics), runtime'ın neye ve neden karar verdiğini söyler - önce onları okuyun.

---

[← Örnek projeler](examples/README.tr.md) | [Genel bakış](README.tr.md)
