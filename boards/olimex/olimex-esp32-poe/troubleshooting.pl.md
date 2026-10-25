---
title: 'Olimex ESP32-PoE: rozwiązywanie problemów'
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

# Rozwiązywanie problemów

| Objaw | Przyczyna | Rozwiązanie |
|---|---|---|
| Port COM się nie pojawia, selektor portów pozostaje pusty | Kabel przewodzi tylko zasilanie albo brakuje sterownika CH340 | Użyj kabla do transmisji danych; zainstaluj sterownik CH340 (WCH CH341SER); spróbuj innego portu USB. |
| Flash runtime zatrzymuje się podczas łączenia | Port zajmuje inny program | Zamknij monitor portu szeregowego lub inne narzędzie, które trzyma port otwarty, i spróbuj ponownie. |
| Płytka uruchamia się ponownie co kilka sekund | Port USB nie daje wystarczającego prądu, gdy startuje Ethernet | Użyj zasilanego huba USB lub zasilacza 5 V o prądzie co najmniej 1 A albo uruchom płytkę na PoE (bez USB). |
| Sieć nie startuje | Brak serwera DHCP albo brak połączenia na porcie | Sprawdź diody link przy gnieździe; ustaw stały adres na stronie Ethernet; spróbuj innego portu switcha. |
| Płytki nie da się znaleźć po nazwie .local | Sieć blokuje mDNS (multicast) | Użyj adresu IP płytki - pokazuje go lista klientów routera i Find devices w edytorze. |
| USB się rozłącza lub PC zgłasza błąd po podłączeniu kabla PoE | USB i PoE podłączone jednocześnie do płytki, która nie jest izolowana | Natychmiast odłącz jedno z nich. Najpierw wgraj przez USB, potem pracuj na PoE - albo użyj ESP32-PoE-ISO. |
| Wyjście na GPIO34 do GPIO39 nic nie robi | Te piny są tylko wejściami | Przenieś wyjście na GPIO33, GPIO4 lub GPIO5. |
| Wartość Modbus pozostaje na 0 | Adres urządzenia, unit lub rejestr jest zły albo urządzenie jest w innej podsieci | Sprawdź IP i unit urządzenia w drzewie urządzeń oraz rejestr w instrukcji urządzenia; spinguj urządzenie z PC. |

Panel **Messages** edytora i **bufor diagnostyczny** płytki (Online → Diagnostics) mówią, co runtime zdecydował i dlaczego - przeczytaj je najpierw.

---

[← Przykładowe projekty](examples/README.pl.md) | [Przegląd](README.pl.md)
