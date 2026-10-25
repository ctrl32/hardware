---
title: Olimex ESP32-POE2
slug: olimex-esp32-poe2
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-poe2/
image: img/board-01.jpg
image_alt: Плата Olimex ESP32-POE2 з гніздом Ethernet і виходами живлення
tags:
- esp32
- ethernet
- poe
- psram
- olimex
---

# Olimex ESP32-POE2

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32](https://img.shields.io/badge/chip-ESP32-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a)

![Плата Olimex ESP32-POE2 з гніздом Ethernet і виходами живлення](img/board-01.jpg)

Olimex ESP32-POE2 - це наступне покоління ESP32-PoE: ESP32 з 8 МБ PSRAM, Ethernet і Power over Ethernet за IEEE 802.3at, яке живить і ваші польові пристрої - виходи 24 В або 12 В, 5 В і 3,3 В, до 25 Вт від мережевого кабелю. З ctrl32 це PLC у шафі, що живиться одним кабелем: логіка релейної схеми, WEBview, Modbus TCP і MQTT, з повним розміром програми класичного ESP32 з PSRAM.

**Підходить для:**

- PLC у шафі, що живить свої датчики й невеликий релейний модуль від PoE
- Шлюз Modbus TCP з MQTT до Home Assistant
- Автоматизація будівлі з одним кабелем на кімнату

Сторінка плати в каталозі: [Olimex ESP32-POE2](https://ctrl32.com/hardware/boards/olimex-esp32-poe2/)

![Olimex ESP32-POE2 - карта пінів: функція кожного GPIO в ctrl32](pinout/pinout.png)

## Що ctrl32 може на цій платі

<!-- capabilities:start -->
| Функція | На цій платі | Примітки |
|---|---|---|
| Чип | ESP32 (ESP32-WROVER-E-N4R8) |  |
| Пам'ять | 4 MB flash, 8 MB PSRAM |  |
| Розмір програми | 512 змінних, 128 аварійних сигналів, 1024 блоків | редактор перевіряє перед завантаженням |
| Цифрові входи / виходи | 5 вільних GPIO | 3 з них лише входи |
| Аналогові входи | 3 на чипі (ADC1) | GPIO34, GPIO36, GPIO39 |
| Ethernet | так - LAN8710A |  |
| Power over Ethernet | IEEE 802.3at |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 - на вільних пінах | потрібен зовнішній трансивер |
| Modbus RTU (RS-485) | так - на вільних пінах | потрібен зовнішній трансивер |
| Modbus TCP | клієнт і сервер |  |
| MQTT | так | виявлення в Home Assistant |
| WEBview | так | сторінка оператора в будь-якому браузері |
| Дисплей / сенсор (HMI) | ні | сторінка оператора - WEBview |
| USB | USB-C |  |
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
- [Olimex ESP32-PoE](../olimex-esp32-poe/README.uk.md) - перше покоління
- [Olimex ESP32-PoE-ISO](../olimex-esp32-poe-iso/README.uk.md) - з ізольованим живленням PoE

