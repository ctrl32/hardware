---
title: Install the ctrl32 runtime on the Olimex ESP32-P4-PC
slug: install
sidebar_position: 30
image: img/install-04-flash-runtime.png
image_alt: The ctrl32 editor writing the runtime to the Olimex ESP32-P4-PC
tags:
- esp32-p4
- ethernet
- ups
- olimex
- install
---

# Install the ctrl32 runtime

The runtime is the program on the board that runs your project - the PLC cycle, the screens, the communication. It goes on the board once; after that every change of the project is a download that rewrites nothing but the project.

## 1. Connect the board

Connect the board to the PC with the USB cable. The USB-C connector is the ESP32-P4's own USB (serial and JTAG) - no
driver is needed on Windows 10 and 11.

![Olimex ESP32-P4-PC](img/board-01.jpg)

## 2. Create the project

Start the ctrl32 editor and choose **New project** (Ctrl+N). Type the project's **name**, pick **Olimex ESP32-P4-PC** in the list of boards (under **Olimex**) and press **Create project**.

![The New project wizard with the Olimex ESP32-P4-PC picked](img/install-02-new-project.png)

To start from the ready example instead, open the [all-in-one project](examples/all-in-one/README.md) (**File → Open**).

## 3. Write the runtime

Pick the board's COM port in the toolbar's port picker, click the board in the device tree and press **Flash runtime**. The editor writes the runtime, reads it back and verifies it; it takes about a minute and the board restarts. This is done once - and again only when the editor brings a new runtime line.

![The Flash runtime dialog with the runtime for the Olimex ESP32-P4-PC](img/install-04-flash-runtime.png)

## 4. Download the project

Press the download button in the toolbar (F5). The editor builds the project, writes it into the board's inactive program slot, verifies it and only then switches - a failed download leaves the running program untouched.

![The toolbar: the port picker and the Download button](img/install-05-download.png)

## 5. Check that it runs

Press **ONLINE** (the plug icon beside the port picker) to watch the program on the board: what conducts is green, every variable carries its live value. Without a board at hand the same view comes from the **simulation** (the toolbar button beside ONLINE).

![The ladder program running - green is power flowing](img/install-06-running.png)

Something does not work? See [Troubleshooting](troubleshooting.md).

*Screenshots: ctrl32 editor 1.07.*

---

[← Hardware and wiring](hardware.md) | [Overview](README.md) | [Configure →](configure.md)
