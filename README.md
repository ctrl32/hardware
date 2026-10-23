# ctrl32 hardware

**Tested boards for ctrl32 - setup guides, pin maps, schematics and example projects.**

![A home dashboard made in ctrl32, running on the Makerfabs MaTouch ESP32-P4 7-inch board](boards/makerfabs/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/examples/home-dashboard/img/screen.jpg)

ctrl32 turns an ESP32 board or a Raspberry Pi into a PLC with its own HMI: ladder, FBD and Structured Text programs, screens on the board's display and in any browser (WEBview), Modbus RTU / TCP, CANopen, MQTT, OPC UA and EtherCAT - built in one editor and downloaded over USB or the network.

[Download the editor](https://ctrl32.com/download/) · [Documentation](https://ctrl32.com/docs/) · [Hardware catalog](https://ctrl32.com/hardware/) · [These guides on the web](https://ctrl32.com/docs/hardware/)

## Tested boards

Each board has a guide of its own - what ctrl32 does on it, the wiring, the first upload, the setup in the editor step by step - and an **all-in-one** example project that uses everything the board can do.

| | Board | Chip | Interfaces |
|---|---|---|---|
| <img src="boards/laskakit/laskakit-esplan/img/board-01.jpg" width="160" alt="LaskaKit ESPlan"> | [LaskaKit ESPlan](boards/laskakit/laskakit-esplan/README.md) | ESP32 | Ethernet, RS-485 |
| <img src="boards/makerfabs/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/img/board-01.jpg" width="160" alt="Makerfabs MaTouch ESP32-P4 7&quot;"> | [Makerfabs MaTouch ESP32-P4 7"](boards/makerfabs/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/README.md) | ESP32-P4 | Ethernet, CAN, RS-485, HMI 1024x600 |
| <img src="boards/makerfabs/makerfabs-matouch-lite-esp32-s3-spi-resistive-touch-395-st7796/img/board-01.jpg" width="160" alt="Makerfabs MaTouch Lite ESP32-S3 3.95&quot;"> | [Makerfabs MaTouch Lite ESP32-S3 3.95"](boards/makerfabs/makerfabs-matouch-lite-esp32-s3-spi-resistive-touch-395-st7796/README.md) | ESP32-S3 | CAN, RS-485, HMI 320x480 |
| <img src="boards/olimex/olimex-esp32-devkit-lipo/img/board-01.jpg" width="160" alt="Olimex ESP32-DevKit-LiPo"> | [Olimex ESP32-DevKit-LiPo](boards/olimex/olimex-esp32-devkit-lipo/README.md) | ESP32 | - |
| <img src="boards/olimex/olimex-esp32-evb/img/board-01.jpg" width="160" alt="Olimex ESP32-EVB"> | [Olimex ESP32-EVB](boards/olimex/olimex-esp32-evb/README.md) | ESP32 | Ethernet, CAN, HMI 240x320 |
| <img src="boards/olimex/olimex-esp32-gateway/img/board-01.jpg" width="160" alt="Olimex ESP32-GATEWAY"> | [Olimex ESP32-GATEWAY](boards/olimex/olimex-esp32-gateway/README.md) | ESP32 | Ethernet |
| <img src="boards/olimex/olimex-esp32-p4-devkit/img/board-01.jpg" width="160" alt="Olimex ESP32-P4-DevKit"> | [Olimex ESP32-P4-DevKit](boards/olimex/olimex-esp32-p4-devkit/README.md) | ESP32-P4 | Ethernet |
| <img src="boards/olimex/olimex-esp32-p4-pc/img/board-01.jpg" width="160" alt="Olimex ESP32-P4-PC"> | [Olimex ESP32-P4-PC](boards/olimex/olimex-esp32-p4-pc/README.md) | ESP32-P4 | Ethernet |
| <img src="boards/olimex/olimex-esp32-poe/img/board-01.jpg" width="160" alt="Olimex ESP32-PoE"> | [Olimex ESP32-PoE](boards/olimex/olimex-esp32-poe/README.md) | ESP32 | Ethernet |
| <img src="boards/olimex/olimex-esp32-poe-iso/img/board-01.jpg" width="160" alt="Olimex ESP32-PoE-ISO"> | [Olimex ESP32-PoE-ISO](boards/olimex/olimex-esp32-poe-iso/README.md) | ESP32 | Ethernet |
| <img src="boards/olimex/olimex-esp32-poe2/img/board-01.jpg" width="160" alt="Olimex ESP32-POE2"> | [Olimex ESP32-POE2](boards/olimex/olimex-esp32-poe2/README.md) | ESP32 | Ethernet |
| <img src="boards/olimex/olimex-esp32-s3-devkit-lipo/img/board-01.jpg" width="160" alt="Olimex ESP32-S3-DevKit-Lipo"> | [Olimex ESP32-S3-DevKit-Lipo](boards/olimex/olimex-esp32-s3-devkit-lipo/README.md) | ESP32-S3 | - |
| <img src="boards/raspberry-pi/raspberry-pi-3-model-b/img/board-01.jpg" width="160" alt="Raspberry Pi 3 Model B+"> | [Raspberry Pi 3 Model B+](boards/raspberry-pi/raspberry-pi-3-model-b/README.md) | Linux | Ethernet, CAN, RS-485 |
| <img src="boards/raspberry-pi/raspberry-pi-4-model-b/img/board-01.jpg" width="160" alt="Raspberry Pi 4 Model B"> | [Raspberry Pi 4 Model B](boards/raspberry-pi/raspberry-pi-4-model-b/README.md) | Linux | Ethernet, CAN, RS-485 |
| <img src="boards/raspberry-pi/raspberry-pi-5/img/board-01.jpg" width="160" alt="Raspberry Pi 5"> | [Raspberry Pi 5](boards/raspberry-pi/raspberry-pi-5/README.md) | Linux | Ethernet, CAN, RS-485 |

## What is in a board's folder

| | |
|---|---|
| `README.md` | the overview: photo, the capability table, the pin map, the steps |
| `hardware.md`, `install.md`, `configure.md`, `troubleshooting.md` | the guide, one page per step |
| `examples/` | the example projects - open them in the ctrl32 editor |
| `pinout/` | the pin map (SVG and PNG) |
| `schematics/`, `datasheets/`, `3d/` | the maker's schematic, KiCad project, datasheets and 3D model |

## Suggest a board

Want a board tested? Open an issue with the board's name and a link to its maker's page. A board gets a guide here once it runs ctrl32 on our test bench.

## Licence

Texts, pin maps and screenshots: [CC BY 4.0](LICENSE). Example projects: [MIT](LICENSE). The makers' photos, schematics and models belong to their makers - see [NOTICE](NOTICE.md).
