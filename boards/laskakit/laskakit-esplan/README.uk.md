---
title: LaskaKit ESPlan
slug: laskakit-esplan
sidebar_position: 10
hardware: /hardware/boards/laskakit-esplan/
image: img/board-01.jpg
image_alt: Плата LaskaKit ESPlan з гніздом Ethernet, клемою RS-485 і клемою живлення
tags:
- esp32
- ethernet
- rs485
- modbus
- laskakit
---

# LaskaKit ESPlan

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32](https://img.shields.io/badge/chip-ESP32-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a)

![Плата LaskaKit ESPlan з гніздом Ethernet, клемою RS-485 і клемою живлення](img/board-01.jpg)

LaskaKit ESPlan - це промислова плата на ESP32: Ethernet 10/100, інтерфейс RS-485 із захистом і перемикним термінуванням, Wi-Fi та широкий діапазон живлення 7-40 В на гвинтовій клемі (або PoE з додатковим модулем). З ctrl32 вона стає Modbus RTU master або slave у шафі - програма релейної схеми в чипі, пристрої RS-485, які читаються й записуються, значення в Modbus TCP, MQTT і на її сторінці оператора (WEBview).

**Підходить для:**

- Modbus RTU master для лічильників, датчиків і приводів із живленням 24 В
- Шлюз Modbus RTU / TCP із власною логікою
- Автоматизація будівлі в шафі

Сторінка плати в каталозі: [LaskaKit ESPlan](https://ctrl32.com/hardware/boards/laskakit-esplan/)

![LaskaKit ESPlan - карта пінів: функція кожного GPIO в ctrl32](pinout/pinout.png)

## Що ctrl32 може на цій платі

<!-- capabilities:start -->
| Функція | На цій платі | Примітки |
|---|---|---|
| Чип | ESP32 (ESP32-WROOM-32E-N4) |  |
| Пам'ять | 4 MB flash |  |
| Розмір програми | 128 змінних, 32 аварійних сигналів, 128 блоків | редактор перевіряє перед завантаженням |
| Цифрові входи / виходи | 5 вільних GPIO | 2 з них лише входи |
| Аналогові входи | 2 на чипі (ADC1) | GPIO35, GPIO39 |
| Ethernet | так - LAN8720A |  |
| Power over Ethernet | IEEE 802.3af |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 - на вільних пінах | потрібен зовнішній трансивер |
| Modbus RTU (RS-485) | так |  |
| Modbus TCP | клієнт і сервер |  |
| MQTT | так | виявлення в Home Assistant |
| WEBview | так | сторінка оператора в будь-якому браузері |
| Дисплей / сенсор (HMI) | ні | сторінка оператора - WEBview |
| USB | USB-C (CH9102 USB-UART) |  |
| Живлення | 5 V USB, PoE |  |
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

