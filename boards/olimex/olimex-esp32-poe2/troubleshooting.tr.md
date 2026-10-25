---
title: 'Olimex ESP32-POE2: sorun giderme'
slug: troubleshooting
sidebar_position: 90
image: img/board-01.jpg
image_alt: Olimex ESP32-POE2
tags:
- esp32
- ethernet
- poe
- psram
- olimex
- troubleshooting
---

# Sorun giderme

| Belirti | Neden | Çözüm |
|---|---|---|
| COM portu görünmüyor, port seçici boş kalıyor | Kablo yalnızca güç taşıyor ya da USB sürücüsü eksik | Bir veri kablosu kullanın; kartın USB çipinin sürücüsünü kurun; başka bir USB portu deneyin. |
| Flash runtime bağlanırken duruyor | Portu başka bir program tutuyor | Seri monitörü veya portu açık tutan diğer aracı kapatın, sonra yeniden deneyin. |
| Kart birkaç saniyede bir yeniden başlıyor | USB portu akımı sağlayamıyor | Beslemeli bir USB hub ya da en az 1 A'lik 5 V'luk bir adaptör kullanın. |
| Ağ açılmıyor | DHCP sunucusu yok ya da portta bağlantı yok | Soketteki bağlantı LED'lerini kontrol edin; kart sayfasında sabit bir adres ayarlayın; switch'in başka bir portunu deneyin. |
| Kart .local adıyla bulunamıyor | Ağ mDNS'i (multicast) engelliyor | Kartın IP adresini kullanın - yönlendiricinin istemci listesi ve editörün Find devices özelliği onu gösterir. |
| Bir çıkış hiçbir şey yapmıyor | Pin yalnızca giriş ya da yanlış pin belirtilmiş | Kart sayfasında pini kontrol edin - yalnızca giriş olan pinler işaretlidir; çıkışı boş bir G/Ç pinine taşıyın. |
| Bir Modbus değeri 0'da kalıyor | Cihaz adresi, unit veya register yanlış | Cihazın IP'sini ve unit'ini cihaz ağacında, register'ı cihazın kılavuzunda kontrol edin. |
| PoE kablosu takıldığında USB bağlantısı kopuyor veya PC hata veriyor | Yalıtılmamış bir kartta USB ve PoE aynı anda bağlı | Hemen birini çıkarın. Önce USB üzerinden yükleyin, sonra PoE ile çalıştırın. |
| 24 V / 12 V çıkışı kapalı kalıyor | Kart USB'den çalışıyor - çıkışlar yalnızca PoE'den gelir | Kartı PoE (802.3at) ile besleyin. |

Editörün **Messages** bölmesi ve kartın **tanılama arabelleği** (Online → Diagnostics), runtime'ın neye ve neden karar verdiğini söyler - önce onları okuyun.

---

[← Örnek projeler](examples/README.tr.md) | [Genel bakış](README.tr.md)
