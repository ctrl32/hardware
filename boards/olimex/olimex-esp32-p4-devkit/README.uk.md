---
title: Olimex ESP32-P4-DevKit
slug: olimex-esp32-p4-devkit
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-p4-devkit/
image: img/board-01.jpg
image_alt: Плата Olimex ESP32-P4-DevKit з гніздом Ethernet і штирьовими роз'ємами
tags:
- esp32-p4
- ethernet
- olimex
---

# Olimex ESP32-P4-DevKit

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32-P4](https://img.shields.io/badge/chip-ESP32--P4-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a)

![Плата Olimex ESP32-P4-DevKit з гніздом Ethernet і штирьовими роз'ємами](img/board-01.jpg)

Olimex ESP32-P4-DevKit - це невелика відкрита плата з ESP32-P4 - найшвидшим ESP32, двоядерним 400 МГц із 32 МБ PSRAM - і Ethernet 100 Мбіт. Вона не має Wi-Fi: це дротовий контролер. З ctrl32 на ній працюють найбільші програми, які може виконати ESP32 - 4096 змінних - зі сторінкою оператора в будь-якому браузері (WEBview), Modbus TCP і MQTT з TLS.

**Підходить для:**

- Дротовий PLC з великою програмою та багатьма пристроями Modbus
- Шлюз зі складною логікою між Modbus TCP і MQTT
- Розробка власної плати на P4

Сторінка плати в каталозі: [Olimex ESP32-P4-DevKit](https://ctrl32.com/hardware/boards/olimex-esp32-p4-devkit/)

![Olimex ESP32-P4-DevKit - карта пінів: функція кожного GPIO в ctrl32](pinout/pinout.png)

## Що ctrl32 може на цій платі

<!-- capabilities:start -->
| Функція | На цій платі | Примітки |
|---|---|---|
| Чип | ESP32-P4 (ESP32-P4NRW32) |  |
| Пам'ять | 16 MB flash, 32 MB PSRAM |  |
| Розмір програми | 4096 змінних, 512 аварійних сигналів, 1024 блоків | редактор перевіряє перед завантаженням |
| Цифрові входи / виходи | 11 вільних GPIO | див. карту пінів |
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
| Живлення | 5 V USB, PoE |  |
<!-- capabilities:end -->

### Що не підтримується

- Роз'єми дисплея MIPI DSI і камери CSI - у ctrl32 ця плата працює без дисплея (сторінка оператора - WEBview).
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

-

## Що далі

- [Документація ctrl32](https://ctrl32.com/docs/) - редактор, мови, кожен блок
- [Завантажте редактор](https://ctrl32.com/download/)
- [Усі перевірені плати](../../README.uk.md)
- [Makerfabs MaTouch ESP32-P4 7"](../../makerfabs/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/README.uk.md) - ESP32-P4 із сенсорним екраном 7"

