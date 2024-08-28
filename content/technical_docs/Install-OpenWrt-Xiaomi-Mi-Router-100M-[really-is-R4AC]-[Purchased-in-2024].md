---
title: "Install OpenWrt Xiaomi Mi Router 100M [really is R4AC] [Purchased in 2024]"
date: 2024-01-15
---

Probado y validado que este router: https://www.pccomponentes.com/xiaomi-mi-router-4a-router-ac1200  se puede flashear con OpenWrt.



Referencia: https://forum.openwrt.org/t/xiaomi-mi-router-4a-r4ac-new-revision/83365/20



Pasos a seguir:

Go to http://192.168.31.1/ and set up the router

Use [OpenWRTInvasion](https://github.com/acecilia/OpenWRTInvasion) to get a root-shell

Imagen a descargar: https://downloads.openwrt.org/releases/22.03.3/targets/ramips/mt76x8/openwrt-22.03.3-ramips-mt76x8-xiaomi_mi-router-4c-squashfs-sysupgrade.bin

Actualizar desde LuCi con: https://downloads.openwrt.org/releases/22.03.3/targets/ramips/mt76x8/openwrt-22.03.3-ramips-mt76x8-xiaomi_mi-router-4a-100m-squashfs-sysupgrade.bin

Saldrá un diálogo, pero marcar force upgrade (se quejará, pero da igual), también marcar do not keep settings y actualizar. Tarda un rato, tener paciencia con el router