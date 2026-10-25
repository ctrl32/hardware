---
title: 'Olimex ESP32-GATEWAY: обладнання та підключення'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-GATEWAY - карта пінів
tags:
- esp32
- ethernet
- gateway
- olimex
---

# Обладнання та підключення

## Що вам потрібно

- Olimex ESP32-GATEWAY.
- USB-C кабель для даних - для завантаження та живлення (5 В).
- Кабель Ethernet і вільний порт у вашій мережі.
- ПК з [редактором ctrl32](https://ctrl32.com/download/) (Windows).
- Приклад all-in-one використовує власну кнопку (GPIO34) і світлодіод (GPIO33) плати - більше нічого підключати не треба.

## Живлення

| Джерело | Де | Примітка |
|---|---|---|
| USB 5 В | роз'єм USB-C | живлення та програмування |

## Карта пінів

![Olimex ESP32-GATEWAY - карта пінів](pinout/pinout.png)

| GPIO | Функція в ctrl32 | Примітка |
|---|---|---|
| 2 | SPI MOSI | ⚠ strapping-пін |
| 5 | Ethernet PHY power (LAN8710A) | ⚠ зайнято платою |
| 6 | SPI-flash модуля | ⚠ зайнято платою |
| 7 | SPI-flash модуля | ⚠ зайнято платою |
| 8 | SPI-flash модуля | ⚠ зайнято платою |
| 9 | SPI-flash модуля | ⚠ зайнято платою |
| 10 | SPI-flash модуля | ⚠ зайнято платою |
| 11 | SPI-flash модуля | ⚠ зайнято платою |
| 13 | free (SPI CS line) |  |
| 14 | SPI SCLK |  |
| 15 | SPI MISO | ⚠ strapping-пін |
| 16 | I2C SCL |  |
| 17 | Ethernet 50 MHz clock (LAN8710A) | ⚠ зайнято платою |
| 18 | Ethernet MDIO (LAN8710A) | ⚠ зайнято платою |
| 19 | Ethernet RMII TXD0 (LAN8710A) | ⚠ зайнято платою |
| 21 | Ethernet RMII TX_EN (LAN8710A) | ⚠ зайнято платою |
| 22 | Ethernet RMII TXD1 (LAN8710A) | ⚠ зайнято платою |
| 23 | Ethernet MDC (LAN8710A) | ⚠ зайнято платою |
| 25 | Ethernet RMII RXD0 (LAN8710A) | ⚠ зайнято платою |
| 26 | Ethernet RMII RXD1 (LAN8710A) | ⚠ зайнято платою |
| 27 | Ethernet RMII CRS_DV (LAN8710A) | ⚠ зайнято платою |
| 32 | I2C SDA |  |
| 33 | free (LED0 line) | ADC1 |
| 34 | вільний - кнопка плати | ⚠ лише вхід, ADC1 |

20-контактний роз'єм **EXT** виводить вільні піни та лінії I2C / SPI.
Світлодіод плати на GPIO33, а її кнопка на GPIO34 (лише вхід). Вільних
пінів залишається мало: більше входів/виходів підключається через Modbus
TCP або мікросхеми I2C.

## Безпека

- Плата не призначена для функцій безпеки. Аварійна зупинка, дверний
  вимикач або світлова завіса підключаються апаратно, ніколи через
  програму.
- Піни GPIO працюють на 3,3 В. Сигнал 24 В потребує оптрона або
  перетворювача рівнів; котушка реле потребує драйвера (релейний модуль
  його має).

---

[← Огляд](README.uk.md) | [Огляд](README.uk.md) | [Встановлення runtime →](install.uk.md)
