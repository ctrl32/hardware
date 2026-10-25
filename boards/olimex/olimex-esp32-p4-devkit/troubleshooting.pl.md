---
title: 'Olimex ESP32-P4-DevKit: rozwiązywanie problemów'
slug: troubleshooting
sidebar_position: 90
image: img/board-01.jpg
image_alt: Olimex ESP32-P4-DevKit
tags:
- esp32-p4
- ethernet
- olimex
- troubleshooting
---

# Rozwiązywanie problemów

| Objaw | Przyczyna | Rozwiązanie |
|---|---|---|
| Port COM się nie pojawia, selektor portów pozostaje pusty | Kabel przewodzi tylko zasilanie albo brakuje sterownika USB | Użyj kabla do transmisji danych; zainstaluj sterownik układu USB płytki; spróbuj innego portu USB. |
| Flash runtime zatrzymuje się podczas łączenia | Port zajmuje inny program | Zamknij monitor portu szeregowego lub inne narzędzie, które trzyma port otwarty, i spróbuj ponownie. |
| Płytka uruchamia się ponownie co kilka sekund | Port USB nie daje wystarczającego prądu | Użyj zasilanego huba USB lub zasilacza 5 V o prądzie co najmniej 1 A. |
| Sieć nie startuje | Brak serwera DHCP albo brak połączenia na porcie | Sprawdź diody link przy gnieździe; ustaw stały adres na stronie płytki; spróbuj innego portu switcha. |
| Płytki nie da się znaleźć po nazwie .local | Sieć blokuje mDNS (multicast) | Użyj adresu IP płytki - pokazuje go lista klientów routera i Find devices w edytorze. |
| Wyjście nic nie robi | Pin jest tylko wejściem albo wskazano zły pin | Sprawdź pin na stronie płytki - piny tylko wejściowe są oznaczone; przenieś wyjście na wolny pin I/O. |
| Wartość Modbus pozostaje na 0 | Adres urządzenia, unit lub rejestr jest zły | Sprawdź IP i unit urządzenia w drzewie urządzeń oraz rejestr w instrukcji urządzenia. |

Panel **Messages** edytora i **bufor diagnostyczny** płytki (Online → Diagnostics) mówią, co runtime zdecydował i dlaczego - przeczytaj je najpierw.

---

[← Przykładowe projekty](examples/README.pl.md) | [Przegląd](README.pl.md)
