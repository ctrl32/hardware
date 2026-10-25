---
title: Raspberry Pi 5
slug: raspberry-pi-5
sidebar_position: 10
hardware: /hardware/boards/raspberry-pi-5/
image: img/board-01.jpg
image_alt: Плата Raspberry Pi 5, вигляд згори
tags:
- raspberry-pi
- linux
- hmi
- opc-ua
- ethercat
---

# Raspberry Pi 5

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: Linux](https://img.shields.io/badge/chip-Linux-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a) ![CAN: 1](https://img.shields.io/badge/CAN-1-7c3aed)

![Плата Raspberry Pi 5, вигляд згори](img/board-01.jpg)

Raspberry Pi 5 виконує Linux runtime ctrl32 - найбільшу ціль ctrl32: десятки тисяч змінних, HMI на HDMI-моніторі, сервер OPC UA для SCADA, приводи EtherCAT, CAN і RS-485 через HAT або USB-адаптери та машинний зір із камерою. Редактор встановлює runtime через мережу; після цього Pi запускає його під час кожного завантаження.

**Підходить для:**

- Контролер лінії з HMI на HDMI-моніторі та OPC UA до SCADA
- EtherCAT master для сервоприводів
- Шлюз між Modbus, CAN, OPC UA і MQTT

Сторінка плати в каталозі: [Raspberry Pi 5](https://ctrl32.com/hardware/boards/raspberry-pi-5/)

![Raspberry Pi 5 - карта пінів: функція кожного GPIO в ctrl32](pinout/pinout.png)

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
| Живлення | USB-C PD 5 V / 5 A |  |
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

| Файл | Що |
|---|---|
| [pinout/pinout.svg](pinout/pinout.svg) | карта пінів, векторна (також [PNG](pinout/pinout.png)) |
| [raspberry-pi-5-mechanical-drawing.pdf](datasheets/raspberry-pi-5-mechanical-drawing.pdf) | Raspberry Pi 5 mechanical drawing |
| [raspberry-pi-5-rp1-peripherals.pdf](datasheets/raspberry-pi-5-rp1-peripherals.pdf) | RP1 peripherals |
| [raspberry-pi-5-3d.zip](3d/raspberry-pi-5-3d.zip) | 3D-модель (GLB, у zip) |
| [NOTICE](https://github.com/ctrl32/hardware/blob/main/NOTICE.md) | звідки фото, схеми та моделі |

## Що далі

- [Документація ctrl32](https://ctrl32.com/docs/) - редактор, мови, кожен блок
- [Завантажте редактор](https://ctrl32.com/download/)
- Усі перевірені плати
- Raspberry Pi 4 Model B
- Raspberry Pi 3 Model B+
- [Linux runtime](https://ctrl32.com/docs/linux-runtime/) - що він робить і його обмеження

