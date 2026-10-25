---
title: Olimex ESP32-S3-DevKit-Lipo
slug: olimex-esp32-s3-devkit-lipo
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-s3-devkit-lipo/
image: img/board-01.jpg
image_alt: Плата Olimex ESP32-S3-DevKit-Lipo з двома роз'ємами USB-C і штирьовими роз'ємами
tags:
- esp32-s3
- wifi
- psram
- battery
- olimex
---

# Olimex ESP32-S3-DevKit-Lipo

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32-S3](https://img.shields.io/badge/chip-ESP32--S3-334155) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a)

![Плата Olimex ESP32-S3-DevKit-Lipo з двома роз'ємами USB-C і штирьовими роз'ємами](img/board-01.jpg)

Olimex ESP32-S3-DevKit-Lipo - це відкрита плата на ESP32-S3 з 8 МБ flash, 8 МБ PSRAM, Wi-Fi, двома портами USB-C і зарядним пристроєм Li-Po. S3 з PSRAM - еталонний чип ctrl32: програма релейної схеми повного розміру, сторінка оператора в будь-якому браузері (WEBview), Modbus TCP і MQTT з TLS - усе через Wi-Fi.

**Підходить для:**

- Wi-Fi PLC із запасом для зростання - 512 змінних, TLS до хмарного брокера
- Контролер із резервним акумулятором, що працює далі під час вимкнення живлення
- Розробка власної плати на ESP32-S3

Сторінка плати в каталозі: [Olimex ESP32-S3-DevKit-Lipo](https://ctrl32.com/hardware/boards/olimex-esp32-s3-devkit-lipo/)

![Olimex ESP32-S3-DevKit-Lipo - карта пінів: функція кожного GPIO в ctrl32](pinout/pinout.png)

## Що ctrl32 може на цій платі

<!-- capabilities:start -->
| Функція | На цій платі | Примітки |
|---|---|---|
| Чип | ESP32-S3 (ESP32-S3-WROOM-1-N8R8) |  |
| Пам'ять | 8 MB flash, 8 MB PSRAM |  |
| Розмір програми | 512 змінних, 128 аварійних сигналів, 1024 блоків | редактор перевіряє перед завантаженням |
| Цифрові входи / виходи | 21 вільних GPIO | див. карту пінів |
| Аналогові входи | 9 на чипі (ADC1) | GPIO1, GPIO2, GPIO4, GPIO5, GPIO6, GPIO7, GPIO8, GPIO9, GPIO10 |
| Ethernet | ні |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 - на вільних пінах | потрібен зовнішній трансивер |
| Modbus RTU (RS-485) | так - на вільних пінах | потрібен зовнішній трансивер |
| Modbus TCP | клієнт і сервер |  |
| MQTT | так (також TLS) | виявлення в Home Assistant |
| WEBview | так | сторінка оператора в будь-якому браузері |
| Дисплей / сенсор (HMI) | ні | сторінка оператора - WEBview |
| USB | USB-C (CH340X USB-UART, Native USB) |  |
| Живлення | 5 V USB, 3.7 V Li-Po / Li-Ion |  |
<!-- capabilities:end -->

### Що не підтримується

- Bluetooth - ESP32-S3 його має, ctrl32 його не використовує.
- Входи контролю акумулятора та живлення (GPIO5 / GPIO6) у ctrl32 є вільними пінами, а не індикатором заряду.

## Посібник

| Крок | Сторінка |
|---|---|
| 1 | [Обладнання та підключення](hardware.uk.md) - що вам потрібно, живлення, карта пінів |
| 2 | [Встановлення runtime](install.uk.md) - редактор, плата, перше завантаження |
| 3 | [Налаштування](configure.uk.md) - мережа, ввід/вивід, зв'язок |
| 4 | [Приклади проєктів](examples/README.uk.md) - усе, що вміє плата, готове до відкриття |
| - | [Усунення несправностей](troubleshooting.uk.md) |

## Файли

-

## Що далі

- [Документація ctrl32](https://ctrl32.com/docs/) - редактор, мови, кожен блок
- [Завантажте редактор](https://ctrl32.com/download/)
- [Усі перевірені плати](../../README.uk.md)
- [Olimex ESP32-DevKit-LiPo](../olimex-esp32-devkit-lipo/README.uk.md) - версія з класичним ESP32

