---
title: Makerfabs MaTouch Lite ESP32-S3 3.95"
slug: makerfabs-matouch-lite-esp32-s3-spi-resistive-touch-395-st7796
sidebar_position: 10
hardware: /hardware/boards/makerfabs-matouch-lite-esp32-s3-spi-resistive-touch-395-st7796/
image: img/board-01.jpg
image_alt: Плата Makerfabs MaTouch Lite ESP32-S3 із сенсорним дисплеєм 3,95 дюйма
tags:
- esp32-s3
- display
- touch
- hmi
- wifi
- makerfabs
---

# Makerfabs MaTouch Lite ESP32-S3 3.95"

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32-S3](https://img.shields.io/badge/chip-ESP32--S3-334155) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a) ![CAN: 1](https://img.shields.io/badge/CAN-1-7c3aed) ![HMI: 320x480](https://img.shields.io/badge/HMI-320x480-0891b2)

![Плата Makerfabs MaTouch Lite ESP32-S3 із сенсорним дисплеєм 3,95 дюйма](img/board-01.jpg)

Makerfabs MaTouch Lite - це недорога сенсорна панель: дисплей 3,95" 320 x 480 з резистивним сенсором на ESP32-S3 з PSRAM і Wi-Fi. З ctrl32 це HMI і PLC в одному - екрани, намальовані в редакторі, на склі, поруч програма релейної схеми, ті самі значення в будь-якому браузері (WEBview), Modbus TCP, CAN і MQTT. Резистивний сенсор працює і в рукавичках.

**Підходить для:**

- Невелика панель оператора на обладнанні, якою керують у рукавичках
- Настінний термостат або кімнатний регулятор
- CAN-дисплей для транспортного засобу або приводу

Сторінка плати в каталозі: [Makerfabs MaTouch Lite ESP32-S3 3.95"](https://ctrl32.com/hardware/boards/makerfabs-matouch-lite-esp32-s3-spi-resistive-touch-395-st7796/)

![Makerfabs MaTouch Lite ESP32-S3 3.95" - карта пінів: функція кожного GPIO в ctrl32](pinout/pinout.png)

## Що ctrl32 може на цій платі

<!-- capabilities:start -->
| Функція | На цій платі | Примітки |
|---|---|---|
| Чип | ESP32-S3 (esp32s3_wroom_1_n16r8) |  |
| Пам'ять | 16 MB flash, 8 MB PSRAM |  |
| Розмір програми | 512 змінних, 128 аварійних сигналів, 512 блоків | редактор перевіряє перед завантаженням |
| Цифрові входи / виходи | 4 вільних GPIO | див. карту пінів |
| Аналогові входи | 4 на чипі (ADC1) | GPIO4, GPIO5, GPIO6, GPIO7 |
| Ethernet | ні |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 | потрібен зовнішній трансивер |
| Modbus RTU (RS-485) | так | на вільних пінах, потрібен зовнішній трансивер |
| Modbus TCP | клієнт і сервер |  |
| MQTT | так (також TLS) | виявлення в Home Assistant |
| WEBview | так | сторінка оператора в будь-якому браузері |
| Дисплей / сенсор (HMI) | 3.95" 320x480, NS2009 |  |
| USB | USB-C (CH340K USB-UART, Native USB) |  |
| Живлення | 5 V USB (4.0–5.25 V), 3.7 V Li-Po / Li-Ion |  |
<!-- capabilities:end -->

### Що не підтримується

- Bluetooth.
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
- [Makerfabs MaTouch ESP32-P4 7"](../makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/README.uk.md) - старша сестра

