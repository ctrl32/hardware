---
title: Olimex ESP32-P4-PC
slug: olimex-esp32-p4-pc
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-p4-pc/
image: img/board-01.jpg
image_alt: Плата Olimex ESP32-P4-PC з гніздом Ethernet, портами USB і роз'ємом HDMI
tags:
- esp32-p4
- ethernet
- ups
- olimex
---

# Olimex ESP32-P4-PC

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32-P4](https://img.shields.io/badge/chip-ESP32--P4-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a)

![Плата Olimex ESP32-P4-PC з гніздом Ethernet, портами USB і роз'ємом HDMI](img/board-01.jpg)

Olimex ESP32-P4-PC - це невеликий комп'ютер на ESP32-P4 - двоядерному 400 МГц із 32 МБ PSRAM - з Ethernet 100 Мбіт, чотирма USB-хостами, HDMI, аудіо та акумулятором Li-Po, який підтримує роботу під час вимкнення живлення. З ctrl32 це дротовий контролер із найбільшою програмою, яку виконує ESP32 - 4096 змінних - зі сторінкою оператора в будь-якому браузері (WEBview), Modbus TCP, MQTT з TLS і CAN або RS-485 на вільних пінах його роз'єму.

**Підходить для:**

- Дротовий PLC, що переживає вимкнення живлення на власному акумуляторі
- Шлюз зі складною логікою між Modbus TCP, CAN і MQTT
- Контролер у корпусі з живленням від PoE (з розширенням)

Сторінка плати в каталозі: [Olimex ESP32-P4-PC](https://ctrl32.com/hardware/boards/olimex-esp32-p4-pc/)

![Olimex ESP32-P4-PC - карта пінів: функція кожного GPIO в ctrl32](pinout/pinout.png)

## Що ctrl32 може на цій платі

<!-- capabilities:start -->
| Функція | На цій платі | Примітки |
|---|---|---|
| Чип | ESP32-P4 (ESP32-P4NRW32) |  |
| Пам'ять | 16 MB flash, 32 MB PSRAM |  |
| Розмір програми | 4096 змінних, 512 аварійних сигналів, 1024 блоків | редактор перевіряє перед завантаженням |
| Цифрові входи / виходи | 15 вільних GPIO | див. карту пінів |
| Аналогові входи | через I2C АЦП (ADS1115) |  |
| Ethernet | так - IP101GRI |  |
| Wi-Fi | ні |  |
| CAN (TWAI) | 1 - на вільних пінах | потрібен зовнішній трансивер |
| Modbus RTU (RS-485) | так - на вільних пінах | потрібен зовнішній трансивер |
| Modbus TCP | клієнт і сервер |  |
| MQTT | так (також TLS) | виявлення в Home Assistant |
| WEBview | так | сторінка оператора в будь-якому браузері |
| Дисплей / сенсор (HMI) | ні | сторінка оператора - WEBview |
| USB | USB-C (Native USB) |  |
| Живлення | 5 V USB, 3.7 V Li-Po / Li-Ion, PoE |  |
<!-- capabilities:end -->

### Що не підтримується

- Вихід HDMI і роз'єми MIPI DSI / CSI - у ctrl32 ця плата працює без дисплея (сторінка оператора - WEBview).
- Порти USB-хоста й аудіовихід.
- Слот microSD - ctrl32 зберігає програму та екрани у flash-пам'яті плати.

## Посібник

| Крок | Сторінка |
|---|---|
| 1 | [Обладнання та підключення](hardware.uk.md) - що вам потрібно, живлення, карта пінів |
| 2 | [Встановлення runtime](install.uk.md) - редактор, плата, перше завантаження |
| 3 | [Налаштування](configure.uk.md) - мережа, ввід/вивід, зв'язок |
| 4 | [Приклади проєктів](examples/README.uk.md) - усе, що вміє плата, готове до відкриття |
| - | [Усунення несправностей](troubleshooting.uk.md) |

## Файли

| Файл | Що |
|---|---|
| [pinout/pinout.svg](pinout/pinout.svg) | карта пінів, векторна (також [PNG](pinout/pinout.png)) |
| [olimex-esp32-p4-pc-schematic.pdf](schematics/olimex-esp32-p4-pc-schematic.pdf) | ESP32-P4-PC schematic Rev C |
| [esp32-p4-pc-rev-c-kicad.zip](schematics/esp32-p4-pc-rev-c-kicad.zip) | KiCad project |
| [olimex-esp32-p4-pc-user-manual.pdf](datasheets/olimex-esp32-p4-pc-user-manual.pdf) | ESP32-P4-PC user manual |
| [NOTICE](https://github.com/ctrl32/hardware/blob/main/NOTICE.md) | звідки фото, схеми та моделі |

## Що далі

- [Документація ctrl32](https://ctrl32.com/docs/) - редактор, мови, кожен блок
- [Завантажте редактор](https://ctrl32.com/download/)
- [Усі перевірені плати](../../README.uk.md)
- [Olimex ESP32-P4-DevKit](../olimex-esp32-p4-devkit/README.uk.md) - той самий ESP32-P4 на меншій платі

