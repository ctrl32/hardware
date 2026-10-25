---
title: Olimex ESP32-GATEWAY
slug: olimex-esp32-gateway
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-gateway/
image: img/board-01.jpg
image_alt: Плата Olimex ESP32-GATEWAY з гніздом Ethernet і роз'ємом USB-C
tags:
- esp32
- ethernet
- gateway
- olimex
---

# Olimex ESP32-GATEWAY

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32](https://img.shields.io/badge/chip-ESP32-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a)

![Плата Olimex ESP32-GATEWAY з гніздом Ethernet і роз'ємом USB-C](img/board-01.jpg)

Olimex ESP32-GATEWAY - це компактна плата на ESP32 з Ethernet 100 Мбіт і Wi-Fi - досить мала для розподільчої коробки. З ctrl32 це шлюз із власною логікою: пристрої Modbus TCP читаються й публікуються через MQTT, у чипі працює програма релейної схеми, а її сторінка оператора - в будь-якому браузері (WEBview).

**Підходить для:**

- Шлюз Modbus TCP - MQTT із власною логікою
- Невеликий контролер у розподільчій коробці, на Ethernet
- Домашня автоматизація - читання лічильників, комутація через модулі вводу/виводу Modbus

Сторінка плати в каталозі: [Olimex ESP32-GATEWAY](https://ctrl32.com/hardware/boards/olimex-esp32-gateway/)

![Olimex ESP32-GATEWAY - карта пінів: функція кожного GPIO в ctrl32](pinout/pinout.png)

## Що ctrl32 може на цій платі

<!-- capabilities:start -->
| Функція | На цій платі | Примітки |
|---|---|---|
| Чип | ESP32 (ESP32-WROOM-32E-N4) |  |
| Пам'ять | 4 MB flash |  |
| Розмір програми | 128 змінних, 32 аварійних сигналів, 128 блоків | редактор перевіряє перед завантаженням |
| Цифрові входи / виходи | 3 вільних GPIO | 1 з них лише входи |
| Аналогові входи | 2 на чипі (ADC1) | GPIO33, GPIO34 |
| Ethernet | так - LAN8710A |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 - на вільних пінах | потрібен зовнішній трансивер |
| Modbus RTU (RS-485) | так - на вільних пінах | потрібен зовнішній трансивер |
| Modbus TCP | клієнт і сервер |  |
| MQTT | так | виявлення в Home Assistant |
| WEBview | так | сторінка оператора в будь-якому браузері |
| Дисплей / сенсор (HMI) | ні | сторінка оператора - WEBview |
| USB | USB-C (CH340 USB-UART) |  |
| Живлення | 5 V USB |  |
<!-- capabilities:end -->

### Що не підтримується

- Bluetooth - ESP32 його має, ctrl32 його не використовує.
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

