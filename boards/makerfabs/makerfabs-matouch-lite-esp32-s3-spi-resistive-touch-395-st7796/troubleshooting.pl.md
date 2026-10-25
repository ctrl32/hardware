---
title: 'Makerfabs MaTouch Lite ESP32-S3 3.95": rozwiązywanie problemów'
slug: troubleshooting
sidebar_position: 90
image: img/board-01.jpg
image_alt: Makerfabs MaTouch Lite ESP32-S3 3.95"
tags:
- esp32-s3
- display
- touch
- hmi
- wifi
- makerfabs
- troubleshooting
---

# Rozwiązywanie problemów

| Objaw | Przyczyna | Rozwiązanie |
|---|---|---|
| Port COM się nie pojawia, selektor portów pozostaje pusty | Kabel przewodzi tylko zasilanie albo brakuje sterownika USB | Użyj kabla do transmisji danych; zainstaluj sterownik układu USB płytki; spróbuj innego portu USB. |
| Flash runtime zatrzymuje się podczas łączenia | Port zajmuje inny program | Zamknij monitor portu szeregowego lub inne narzędzie, które trzyma port otwarty, i spróbuj ponownie. |
| Płytka uruchamia się ponownie co kilka sekund | Port USB nie daje wystarczającego prądu | Użyj zasilanego huba USB lub zasilacza 5 V o prądzie co najmniej 1 A. |
| Płytka nie łączy się z Wi-Fi | Zła nazwa sieci lub hasło albo sieć wyłącznie 5 GHz | Sprawdź nazwę i hasło na stronie WiFi; ESP32 łączy się tylko z sieciami 2,4 GHz. |
| Płytki nie da się znaleźć po nazwie .local | Sieć blokuje mDNS (multicast) | Użyj adresu IP płytki - pokazuje go lista klientów routera i Find devices w edytorze. |
| Wyjście nic nie robi | Pin jest tylko wejściem albo wskazano zły pin | Sprawdź pin na stronie płytki - piny tylko wejściowe są oznaczone; przenieś wyjście na wolny pin I/O. |
| Wartość Modbus pozostaje na 0 | Adres urządzenia, unit lub rejestr jest zły | Sprawdź IP i unit urządzenia w drzewie urządzeń oraz rejestr w instrukcji urządzenia. |
| CAN milczy | Brak terminacji 120 omów albo inna prędkość transmisji | Załóż rezystor 120 omów na obu końcach magistrali; ustaw tę samą prędkość transmisji na każdym węźle. |
| Wartość Modbus RTU pozostaje na 0 | Zamienione A i B albo zły unit, prędkość lub parzystość | Zamień A i B; sprawdź unit, prędkość i parzystość urządzenia. |

Panel **Messages** edytora i **bufor diagnostyczny** płytki (Online → Diagnostics) mówią, co runtime zdecydował i dlaczego - przeczytaj je najpierw.

---

[← Przykładowe projekty](examples/README.pl.md) | [Przegląd](README.pl.md)
