---
title: Olimex ESP32-PoE-ISO
slug: olimex-esp32-poe-iso
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-poe-iso/
image: img/board-01.jpg
image_alt: Плата Olimex ESP32-PoE-ISO з гніздом Ethernet і ізольованим живленням PoE
tags:
- esp32
- ethernet
- poe
- isolated
- olimex
---

# Olimex ESP32-PoE-ISO

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32](https://img.shields.io/badge/chip-ESP32-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a)

![Плата Olimex ESP32-PoE-ISO з гніздом Ethernet і ізольованим живленням PoE](img/board-01.jpg)

Olimex ESP32-PoE-ISO - це ESP32-PoE з гальванічно розв'язаним живленням Power-over-Ethernet: один мережевий кабель живить її та передає дані, а ПК може залишатися підключеним через USB, поки плата працює від PoE. З ctrl32 це компактний PLC для шафи - програма релейної схеми в чипі, сторінка оператора в будь-якому браузері (WEBview), Modbus TCP до лічильників і модулів вводу/виводу та MQTT до Home Assistant.

**Підходить для:**

- Невеликий PLC у шафі з живленням від PoE-комутатора
- Шлюз Modbus TCP, що читає лічильники й публікує їх через MQTT
- Домашня автоматизація - кімната або котельня на одному кабелі

Сторінка плати в каталозі: [Olimex ESP32-PoE-ISO](https://ctrl32.com/hardware/boards/olimex-esp32-poe-iso/)

![Olimex ESP32-PoE-ISO - карта пінів: функція кожного GPIO в ctrl32](pinout/pinout.png)

## Що ctrl32 може на цій платі

<!-- capabilities:start -->
| Функція | На цій платі | Примітки |
|---|---|---|
| Чип | ESP32 (ESP32-WROOM-32E-N4) |  |
| Пам'ять | 4 MB flash |  |
| Розмір програми | 128 змінних, 32 аварійних сигналів, 128 блоків | редактор перевіряє перед завантаженням |
| Цифрові входи / виходи | 6 вільних GPIO | 3 з них лише входи |
| Аналогові входи | 4 на чипі (ADC1) | GPIO33, GPIO34, GPIO35, GPIO36 |
| Ethernet | так - LAN8710A |  |
| Power over Ethernet | IEEE 802.3af |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 - на вільних пінах | потрібен зовнішній трансивер |
| Modbus RTU (RS-485) | так - на вільних пінах | потрібен зовнішній трансивер |
| Modbus TCP | клієнт і сервер |  |
| MQTT | так | виявлення в Home Assistant |
| WEBview | так | сторінка оператора в будь-якому браузері |
| Дисплей / сенсор (HMI) | ні | сторінка оператора - WEBview |
| USB | Micro-USB (CH340T USB-UART) |  |
| Живлення | 5 V USB, 3.7 V Li-Po / Li-Ion, PoE |  |
<!-- capabilities:end -->

### Що не підтримується

- Bluetooth - ESP32 його має, ctrl32 його не використовує.
- Слот microSD - ctrl32 зберігає програму та екрани у власній flash-пам'яті чипа.
- Вхід акумулятора працює як власна функція плати; ctrl32 не читає рівень заряду.

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
- [Olimex ESP32-PoE](../olimex-esp32-poe/README.uk.md) - та сама плата без ізольованого живлення
- Olimex ESP32-POE2 - наступне покоління

