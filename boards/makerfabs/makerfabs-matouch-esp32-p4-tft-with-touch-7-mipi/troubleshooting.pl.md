---
title: 'Makerfabs MaTouch ESP32-P4 7": rozwiązywanie problemów'
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

# Rozwiązywanie problemów

| Objaw | Przyczyna | Rozwiązanie |
|---|---|---|
| Port COM się nie pojawia | Kabel przewodzi tylko zasilanie albo brakuje sterownika CH340 | Użyj kabla USB-C do transmisji danych; zainstaluj sterownik CH340 (WCH CH341SER); spróbuj innego portu USB. |
| Płytka uruchamia się ponownie, gdy pojawia się ekran | Zasilacz nie udźwignie podświetlenia | Użyj zasilacza 5 V / 2 A lub zasilanego huba USB. |
| Ekran pozostaje ciemny po zapisaniu runtime | Na płytce nie ma jeszcze projektu | Wgraj projekt (F5); płytka bez projektu nic nie pokazuje na szkle. |
| Dotyk nie reaguje albo reaguje w złym miejscu | Orientacja projektu różni się od sposobu zamontowania płytki | Ustaw orientację na stronie HMIview i wgraj ponownie. |
| Sieć nie startuje | Brak serwera DHCP albo brak połączenia na porcie | Sprawdź diody link przy gnieździe; ustaw stały adres na stronie płytki; dla Wi-Fi sprawdź nazwę sieci i hasło. |
| CAN milczy | Brak transceivera, brak terminacji 120 omów albo inna prędkość transmisji | Sprawdź transceiver na GPIO20 / GPIO21, rezystor 120 omów na obu końcach magistrali i tę samą prędkość na każdym węźle. |
| Wartość Modbus RTU pozostaje na 0 | Zamienione A i B, zły unit lub prędkość albo brak pinu DE | Zamień A i B; sprawdź unit, prędkość i parzystość; sprawdź, czy DE jest podłączony i wskazany. |

Panel **Messages** edytora i **bufor diagnostyczny** płytki (Online → Diagnostics) mówią, co runtime zdecydował i dlaczego - przeczytaj je najpierw.

---

[← Przykładowe projekty](examples/README.pl.md) | [Przegląd](README.pl.md)
