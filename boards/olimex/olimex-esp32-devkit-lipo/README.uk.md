---
title: Olimex ESP32-DevKit-LiPo
slug: olimex-esp32-devkit-lipo
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-devkit-lipo/
image: img/board-01.jpg
image_alt: Плата Olimex ESP32-DevKit-LiPo з двома штирьовими роз'ємами та роз'ємом micro-USB
tags:
- esp32
- wifi
- battery
- olimex
---

# Olimex ESP32-DevKit-LiPo

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32](https://img.shields.io/badge/chip-ESP32-334155) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a)

![Плата Olimex ESP32-DevKit-LiPo з двома штирьовими роз'ємами та роз'ємом micro-USB](img/board-01.jpg)

Olimex ESP32-DevKit-LiPo - це відкрита плата розробника на ESP32 з Wi-Fi, усіма GPIO модуля на двох роз'ємах і зарядним пристроєм Li-Po, який підтримує її роботу, коли зникає живлення. З ctrl32 це невеликий Wi-Fi PLC: програма релейної схеми в чипі, входи та виходи на її пінах, сторінка оператора в будь-якому браузері (WEBview), Modbus TCP і MQTT.

**Підходить для:**

- Wi-Fi контролер для кімнати, теплиці або насоса
- Реєстратор даних із резервним акумулятором, що публікує через MQTT
- Вивчення ctrl32 на макетній платі

Сторінка плати в каталозі: [Olimex ESP32-DevKit-LiPo](https://ctrl32.com/hardware/boards/olimex-esp32-devkit-lipo/)

![Olimex ESP32-DevKit-LiPo - карта пінів: функція кожного GPIO в ctrl32](pinout/pinout.png)

## Що ctrl32 може на цій платі

<!-- capabilities:start -->
| Функція | На цій платі | Примітки |
|---|---|---|
| Чип | ESP32 (ESP32-WROOM-32E-N4) |  |
| Пам'ять | 4 MB flash |  |
| Розмір програми | 128 змінних, 32 аварійних сигналів, 128 блоків | редактор перевіряє перед завантаженням |
| Цифрові входи / виходи | 19 вільних GPIO | 4 з них лише входи |
| Аналогові входи | 6 на чипі (ADC1) | GPIO32, GPIO33, GPIO34, GPIO35, GPIO36, GPIO39 |
| Ethernet | ні |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 - на вільних пінах | потрібен зовнішній трансивер |
| Modbus RTU (RS-485) | так - на вільних пінах | потрібен зовнішній трансивер |
| Modbus TCP | клієнт і сервер |  |
| MQTT | так | виявлення в Home Assistant |
| WEBview | так | сторінка оператора в будь-якому браузері |
| Дисплей / сенсор (HMI) | ні | сторінка оператора - WEBview |
| USB | Micro-USB (CH340 USB-UART) |  |
| Живлення | 5 V USB, 3.7 V Li-Po / Li-Ion |  |
<!-- capabilities:end -->

### Що не підтримується

- Bluetooth - ESP32 його має, ctrl32 його не використовує.
- Входи контролю акумулятора та живлення (GPIO35 / GPIO39) у ctrl32 є вільними пінами, а не індикатором заряду.

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
- Olimex ESP32-S3-DevKit-Lipo - та сама ідея з ESP32-S3 і PSRAM

