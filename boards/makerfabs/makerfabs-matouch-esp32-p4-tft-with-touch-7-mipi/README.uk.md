---
title: Makerfabs MaTouch ESP32-P4 7"
slug: makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi
sidebar_position: 10
hardware: /hardware/boards/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/
image: img/board-01.jpg
image_alt: Плата Makerfabs MaTouch ESP32-P4 7 дюймів із сенсорним дисплеєм 1024x600
tags:
- esp32-p4
- display
- touch
- hmi
- ethernet
- makerfabs
---

# Makerfabs MaTouch ESP32-P4 7"

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32-P4](https://img.shields.io/badge/chip-ESP32--P4-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a) ![CAN: 1](https://img.shields.io/badge/CAN-1-7c3aed) ![HMI: 1024x600](https://img.shields.io/badge/HMI-1024x600-0891b2)

![Плата Makerfabs MaTouch ESP32-P4 7 дюймів із сенсорним дисплеєм 1024x600](img/board-01.jpg)

Makerfabs MaTouch ESP32-P4 7" - це повна сенсорна панель на одній платі: MIPI-дисплей 1024 x 600 з ємнісним сенсором, двоядерний ESP32-P4 з 32 МБ PSRAM, Ethernet і Wi-Fi 6 через ESP32-C6. З ctrl32 це HMI і PLC в одному - екрани, намальовані в редакторі, працюють на склі, поруч працює програма релейної схеми, а ті самі значення доходять до будь-якого браузера (WEBview), пристроїв Modbus, CAN і MQTT.

**Підходить для:**

- Панель оператора на обладнанні з власною логікою
- Панель керування розумним будинком або будівлею на стіні
- Шлюз Modbus / CAN з екраном

Сторінка плати в каталозі: [Makerfabs MaTouch ESP32-P4 7"](https://ctrl32.com/hardware/boards/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/)

![Makerfabs MaTouch ESP32-P4 7" - карта пінів: функція кожного GPIO в ctrl32](pinout/pinout.png)

## Що ctrl32 може на цій платі

<!-- capabilities:start -->
| Функція | На цій платі | Примітки |
|---|---|---|
| Чип | ESP32-P4 (ESP32-P4NRW32) |  |
| Пам'ять | 16 MB flash, 32 MB PSRAM |  |
| Розмір програми | 4096 змінних, 512 аварійних сигналів, 512 блоків | редактор перевіряє перед завантаженням |
| Цифрові входи / виходи | 12 вільних GPIO | див. карту пінів |
| Аналогові входи | через I2C АЦП (ADS1115) |  |
| Ethernet | так - IP101GRI |  |
| Wi-Fi | Wi-Fi 6 (2.4 GHz) |  |
| CAN (TWAI) | 1 | потрібен зовнішній трансивер |
| Modbus RTU (RS-485) | так | на вільних пінах, потрібен зовнішній трансивер |
| Modbus TCP | клієнт і сервер |  |
| MQTT | так (також TLS) | виявлення в Home Assistant |
| WEBview | так | сторінка оператора в будь-якому браузері |
| Дисплей / сенсор (HMI) | 7" 1024x600, GT911 |  |
| USB | USB-C (CH340K USB-UART, Native USB) |  |
| Живлення | 5 V USB (4.0–5.25 V), 3.7 V Li-Po / Li-Ion |  |
<!-- capabilities:end -->

### Що не підтримується

- Камера (SC2336 на MIPI CSI) - ctrl32 виконує машинний зір лише в 64-бітному Linux runtime.
- Аудіокодек, мікрофон і вихід на динамік.
- Bluetooth модуля ESP32-C6.
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
| [makerfabs-matouch_esp32-p4_tft_with_touch_7_v1.2.pdf](schematics/makerfabs-matouch_esp32-p4_tft_with_touch_7_v1.2.pdf) | MaTouch ESP32-P4 TFT with Touch 7“ V1.2 |
| [makerfabs-matouch-p4-7-display-datasheet.pdf](datasheets/makerfabs-matouch-p4-7-display-datasheet.pdf) | 7" 1024x600 MIPI display AML070JGI50 datasheet |
| [makerfabs-matouch-p4-es8311-datasheet.pdf](datasheets/makerfabs-matouch-p4-es8311-datasheet.pdf) | ES8311 audio codec datasheet |
| [esp32-p4-datasheet.pdf](datasheets/esp32-p4-datasheet.pdf) | ESP32-P4 datasheet (pre-release) |
| [makerfabs-matouch-p4-sc2336-camera-datasheet.pdf](datasheets/makerfabs-matouch-p4-sc2336-camera-datasheet.pdf) | SC2336 2 MP MIPI camera module datasheet |
| [NOTICE](https://github.com/ctrl32/hardware/blob/main/NOTICE.md) | звідки фото, схеми та моделі |

## Що далі

- [Документація ctrl32](https://ctrl32.com/docs/) - редактор, мови, кожен блок
- [Завантажте редактор](https://ctrl32.com/download/)
- Усі перевірені плати
- Makerfabs MaTouch Lite ESP32-S3 3.95" - молодша сестра
- [Панель керування розумним будинком на MaTouch ESP32-P4](https://ctrl32.com/examples/smart-home-control-panel-on-an-esp32-p4-7-touch-display/) - повний приклад в інтернеті

