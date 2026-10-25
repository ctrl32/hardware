---
title: Raspberry Pi 3 Model B+ üzerine ctrl32 runtime kurulumu
slug: install
sidebar_position: 30
image: img/install-03-prepare.png
image_alt: ctrl32 editörü Raspberry Pi 3 Model B+ kartını hazırlıyor
tags:
- raspberry-pi
- linux
- hmi
- opc-ua
- install
---

# ctrl32 runtime'ı kurun

ctrl32 Linux runtime, karttaki projenizi çalıştıran programdır - PLC döngüsü, monitördeki ekran, WEBview, OPC UA ve veri yolları. Editör onu ağ üzerinden kurar; hiçbir Linux komutu yazılmaz.

## 1. microSD kartı yazın

Raspberry Pi Imager ile karta **Raspberry Pi OS Lite (64-bit)** yazın.
*Lite* bilinçli bir seçimdir: runtime ekranı kendisi çizer ve masaüstüne
ihtiyaç duymaz. Yazmadan önce Imager'ın ayarlarında şunları belirleyin:

- ağda tanıyacağınız bir **ana bilgisayar adı (hostname)**,
- bir **kullanıcı** ve onun **parolası**,
- **SSH etkin**,
- Wi-Fi'ı yalnızca Pi kabloya bağlı olmayacaksa.

Kartı Pi'ye takın, Ethernet'i ve monitörü bağlayın ve açın.

![Raspberry Pi 3 Model B+](img/board-01.jpg)

## 2. Projeyi oluşturun

ctrl32 editörünü başlatın ve **New project** (Ctrl+N) seçin. Projenin **adını** yazın, **Linux** altında **Raspberry Pi** seçin ve **Create project**'e basın.

![Raspberry Pi seçili New project sihirbazı](img/install-02-new-project.png)

Bunun yerine hazır örnekle başlamak için [all-in-one projesini](examples/all-in-one/README.tr.md) açın (**File → Open**).

## 3. Kartı hazırlayın

**Online → Prepare a Linux device** seçeneğini seçin. Kartın **adresini**, 1. adımdaki **kullanıcıyı** ve **parolayı** yazın ve **Look at the device**'a basın: editör oturum açar, kartın ne olduğunu okur ve ne yapacağını listeler - bakmak hiçbir şeyi değiştirmez. Ardından **Prepare it**'e basın: editör runtime'ı kopyalar, onu bir servis olarak kurar, başlatır ve yanıt verene kadar bekler. Bundan sonra kart runtime'ı her açılışta başlatır.

![Prepare a Linux device: kartın ne olduğu ve editörün atacağı adımlar](img/install-03-prepare.png)

**Do not ask for the password again** işaretli kalsın: editör karta kendi anahtarını koyar ve sonraki ziyaretler için yalnızca adres yeterlidir. Parola bir kez kullanılır ve asla saklanmaz.

Planın altında **Operating system of this device**, projeye değil Pi'ye
ait olanları tutar: CAN HAT (SPI üzerindeki her CAN çipi için bir satır),
bir RS-485 HAT için seri portun serbest bırakılması, I2C, sabit bir adres ve
EtherCAT için gerçek zamanlı çekirdek. Pi'nizde olanları işaretleyin;
işaretlenen her satır bir adımdır ve Pi yalnızca bir açılış ayarı
değiştiğinde yeniden başlar.

## 4. Projeyi karta yükleyin

Kartın adresini araç çubuğunun port seçicisine yazın ve yükleme butonuna basın (F5). Runtime projeyi yükler ve ekran monitörde belirir.

![Araç çubuğu: port seçici ve Download butonu](img/install-05-download.png)

## 5. Çalıştığını kontrol edin

- **ONLINE** (fiş simgesi) basamaklarda, değişkenlerde ve ekranda canlı değerleri gösterir.
- **WEBview**: aynı ağdaki bir tarayıcıda `http://<adres>:8080`.
- **OPC UA**: `opc.tcp://<adres>:4840` - her değişken bir düğümdür, `ns=1;s=<ad>`.

![Çalışan merdiven programı - yeşil, akımın aktığı yerdir](img/install-06-running.png)

| Port | Orada ne çalışır |
|---|---|
| 8080 | WEBview, program yükleme, cihazın bulunması |
| 4840 | OPC UA sunucusu |
| 3232 | editörün online bağlantısı |

Bir şey çalışmıyor mu? Bkz. [Sorun giderme](troubleshooting.tr.md).

*Ekran görüntüleri: ctrl32 editörü 1.07.*

---

[← Donanım ve kablolama](hardware.tr.md) | [Genel bakış](README.tr.md) | [Yapılandırma →](configure.tr.md)
