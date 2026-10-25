---
title: 'Olimex ESP32-PoE: sorun giderme'
slug: troubleshooting
sidebar_position: 90
image: img/board-01.jpg
image_alt: Olimex ESP32-PoE
tags:
- esp32
- ethernet
- poe
- olimex
- troubleshooting
---

# Sorun giderme

| Belirti | Neden | Çözüm |
|---|---|---|
| COM portu görünmüyor, port seçici boş kalıyor | Kablo yalnızca güç taşıyor ya da CH340 sürücüsü eksik | Bir veri kablosu kullanın; CH340 sürücüsünü (WCH CH341SER) kurun; başka bir USB portu deneyin. |
| Flash runtime bağlanırken duruyor | Portu başka bir program tutuyor | Seri monitörü veya portu açık tutan diğer aracı kapatın, sonra yeniden deneyin. |
| Kart birkaç saniyede bir yeniden başlıyor | Ethernet başlarken USB portu akımı sağlayamıyor | Beslemeli bir USB hub ya da en az 1 A'lik 5 V'luk bir adaptör kullanın veya kartı PoE ile (USB olmadan) çalıştırın. |
| Ağ açılmıyor | DHCP sunucusu yok ya da portta bağlantı yok | Soketteki bağlantı LED'lerini kontrol edin; Ethernet sayfasında sabit bir adres ayarlayın; switch'in başka bir portunu deneyin. |
| Kart .local adıyla bulunamıyor | Ağ mDNS'i (multicast) engelliyor | Kartın IP adresini kullanın - yönlendiricinin istemci listesi ve editörün Find devices özelliği onu gösterir. |
| PoE kablosu takıldığında USB bağlantısı kopuyor veya PC hata veriyor | Yalıtılmamış bir kartta USB ve PoE aynı anda bağlı | Hemen birini çıkarın. Önce USB üzerinden yükleyin, sonra PoE ile çalıştırın - ya da ESP32-PoE-ISO kullanın. |
| GPIO34 - GPIO39 üzerindeki bir çıkış hiçbir şey yapmıyor | Bu pinler yalnızca giriştir | Çıkışı GPIO33, GPIO4 veya GPIO5'e taşıyın. |
| Bir Modbus değeri 0'da kalıyor | Cihaz adresi, unit veya register yanlış ya da cihaz başka bir alt ağda | Cihazın IP'sini ve unit'ini cihaz ağacında, register'ı cihazın kılavuzunda kontrol edin; cihaza PC'den ping atın. |

Editörün **Messages** bölmesi ve kartın **tanılama arabelleği** (Online → Diagnostics), runtime'ın neye ve neden karar verdiğini söyler - önce onları okuyun.

---

[← Örnek projeler](examples/README.tr.md) | [Genel bakış](README.tr.md)
