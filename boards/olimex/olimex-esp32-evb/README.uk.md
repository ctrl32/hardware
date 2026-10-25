---
title: Olimex ESP32-EVB
slug: olimex-esp32-evb
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-evb/
image: img/board-01.jpg
image_alt: Плата Olimex ESP32-EVB з двома реле, гніздом Ethernet і клемою CAN
tags:
- esp32
- ethernet
- can
- relay
- olimex
---

# Olimex ESP32-EVB

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32](https://img.shields.io/badge/chip-ESP32-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a) ![CAN: 1](https://img.shields.io/badge/CAN-1-7c3aed) ![HMI: 240x320](https://img.shields.io/badge/HMI-240x320-0891b2)

![Плата Olimex ESP32-EVB з двома реле, гніздом Ethernet і клемою CAN](img/board-01.jpg)

Olimex ESP32-EVB - це плата на ESP32, створена для керування: два реле (10 А / 250 VAC), CAN-трансивер, Ethernet і Wi-Fi на одній платі. З ctrl32 це готовий PLC - реле та кнопка є змінними програми релейної схеми, CAN спілкується з приводами та вузлами вводу/виводу, а сторінка оператора працює в будь-якому браузері (WEBview). Додатковий сенсорний дисплей 2,8" на роз'ємі UEXT перетворює її на невелику панель.

**Підходить для:**

- Релейний контролер - опалення, насоси, освітлення - з Ethernet
- CAN master для приводу або вузлів вводу/виводу CANopen
- Термостат або невелика панель із додатковим дисплеєм 2,8"

Сторінка плати в каталозі: [Olimex ESP32-EVB](https://ctrl32.com/hardware/boards/olimex-esp32-evb/)

![Olimex ESP32-EVB - карта пінів: функція кожного GPIO в ctrl32](pinout/pinout.png)

## Що ctrl32 може на цій платі

<!-- capabilities:start -->
| Функція | На цій платі | Примітки |
|---|---|---|
| Чип | ESP32 (ESP32-WROOM-32E-N4) |  |
| Пам'ять | 4 MB flash |  |
| Розмір програми | 128 змінних, 32 аварійних сигналів, 128 блоків | редактор перевіряє перед завантаженням |
| Цифрові входи / виходи | 6 вільних GPIO | 2 з них лише входи |
| Аналогові входи | 4 на чипі (ADC1) | GPIO32, GPIO33, GPIO34, GPIO36 |
| Ethernet | так - LAN8710A |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 |  |
| Modbus RTU (RS-485) | так - на вільних пінах | потрібен зовнішній трансивер |
| Modbus TCP | клієнт і сервер |  |
| MQTT | так | виявлення в Home Assistant |
| WEBview | так | сторінка оператора в будь-якому браузері |
| Дисплей / сенсор (HMI) | - 240x320, - |  |
| USB | Micro-USB (CH340T USB-UART) |  |
| Живлення | 5 V USB, 3.7 V Li-Po / Li-Ion |  |
<!-- capabilities:end -->

### Що не підтримується

- Bluetooth.
- ІЧ-приймач і передавач - ctrl32 не використовує їх на цій платі.
- Слот microSD - ctrl32 зберігає програму та екрани у власній flash-пам'яті чипа.

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
- [Olimex ESP32-PoE](../olimex-esp32-poe/README.uk.md) - Ethernet і Power over Ethernet

