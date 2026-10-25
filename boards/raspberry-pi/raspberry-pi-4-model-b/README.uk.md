---
title: Raspberry Pi 4 Model B
slug: raspberry-pi-4-model-b
sidebar_position: 10
hardware: /hardware/boards/raspberry-pi-4-model-b/
image: img/board-01.jpg
image_alt: Плата Raspberry Pi 4 Model B, вигляд згори
tags:
- raspberry-pi
- linux
- hmi
- opc-ua
- ethercat
---

# Raspberry Pi 4 Model B

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: Linux](https://img.shields.io/badge/chip-Linux-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a) ![CAN: 1](https://img.shields.io/badge/CAN-1-7c3aed)

![Плата Raspberry Pi 4 Model B, вигляд згори](img/board-01.jpg)

Raspberry Pi 4 Model B виконує Linux runtime ctrl32 - найбільшу ціль ctrl32: десятки тисяч змінних, HMI на HDMI-моніторі, сервер OPC UA для SCADA, приводи EtherCAT, CAN і RS-485 через HAT або USB-адаптери та машинний зір із камерою. Редактор встановлює runtime через мережу; після цього Pi запускає його під час кожного завантаження.

**Підходить для:**

- Контролер лінії з HMI на HDMI-моніторі та OPC UA до SCADA
- EtherCAT master для сервоприводів
- Шлюз між Modbus, CAN, OPC UA і MQTT

Сторінка плати в каталозі: [Raspberry Pi 4 Model B](https://ctrl32.com/hardware/boards/raspberry-pi-4-model-b/)

![Raspberry Pi 4 Model B - карта пінів: функція кожного GPIO в ctrl32](pinout/pinout.png)

## Що ctrl32 може на цій платі

<!-- capabilities:start -->
| Функція | На цій платі | Примітки |
|---|---|---|
| Чип | Linux |  |
| Розмір програми | 20480 змінних, 4096 аварійних сигналів, 40960 блоків | редактор перевіряє перед завантаженням |
| Цифрові входи / виходи | через модулі вводу/виводу | Modbus, CANopen, EtherCAT |
| Ethernet | так |  |
| Wi-Fi | Wi-Fi 5 (2.4 + 5 GHz) |  |
| CAN | через CAN HAT або USB-адаптер | SocketCAN, до 4 шин |
| Modbus RTU (RS-485) | так | USB-адаптер або HAT |
| Modbus TCP | клієнт і сервер |  |
| MQTT | так (також TLS) | виявлення в Home Assistant |
| WEBview | так | сторінка оператора в будь-якому браузері |
| Сервер OPC UA | так |  |
| EtherCAT master | так | на другому порту Ethernet |
| Дисплей (HMI) | HDMI або панель DSI | або без дисплея з WEBview |
| USB | USB-C |  |
| Живлення | 5 V USB |  |
<!-- capabilities:end -->

### Що не підтримується

- 40-контактний роз'єм GPIO як входи/виходи програми - входи та виходи йдуть через модулі вводу/виводу (Modbus RTU / TCP, CANopen, EtherCAT); роз'єм виводить шини HAT.
- Bluetooth.
- Робочий стіл - runtime сам малює екран; потрібна система - Raspberry Pi OS Lite.

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
- [Raspberry Pi 5](../raspberry-pi-5/README.uk.md)
- Raspberry Pi 3 Model B+
- [Linux runtime](https://ctrl32.com/docs/linux-runtime/) - що він робить і його обмеження

