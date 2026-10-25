---
title: 'Raspberry Pi 5: rozwiązywanie problemów'
slug: troubleshooting
sidebar_position: 90
image: img/board-01.jpg
image_alt: Raspberry Pi 5
tags:
- raspberry-pi
- linux
- hmi
- opc-ua
- ethercat
- troubleshooting
---

# Rozwiązywanie problemów

| Objaw | Przyczyna | Rozwiązanie |
|---|---|---|
| Look at the device nie może się połączyć | SSH jest wyłączone, adres jest zły albo PC jest w innej sieci | Włącz SSH w ustawieniach Imagera i zapisz kartę ponownie; spinguj adres z PC. |
| Prepare nie proponuje instalacji | Runtime ctrl32 jest już zainstalowany na Pi | Zainstalowany runtime aktualizuje się przez Flash runtime z adresem Pi w selektorze portów. |
| Monitor pozostaje czarny po wgraniu | Monitor podłączono po starcie albo projekt nie ma ekranu | Podłącz monitor przed włączeniem Pi; dodaj ekran do projektu. |
| WEBview się nie otwiera | Zły port | Otwórz http://<adres>:8080 - runtime działa na porcie 8080. |
| Adapter USB-RS485 znika | Zbyt niskie napięcie - zasilacz jest za słaby | Użyj oficjalnego zasilacza 27 W. |
| CAN milczy | Sterownik nakładki nie jest załadowany, brak terminacji albo inna prędkość transmisji | Zaznacz nakładkę w Prepare a Linux device; rezystor 120 omów na obu końcach magistrali; ta sama prędkość na każdym węźle. |
| Klient OPC UA nie widzi zmiennych | Zmienna jest wyłączona z serwera albo zapora blokuje port 4840 | Sprawdź zaznaczenie OPC UA na liście zmiennych; otwórz port 4840. |

Panel **Messages** edytora i **bufor diagnostyczny** płytki (Online → Diagnostics) mówią, co runtime zdecydował i dlaczego - przeczytaj je najpierw.

---

[← Przykładowe projekty](examples/README.pl.md) | [Przegląd](README.pl.md)
