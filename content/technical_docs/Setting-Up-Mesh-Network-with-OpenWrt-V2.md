---
title: "Setting Up Mesh Network with OpenWrt V2"
date: 2023-03-16
---

Very good Tutorial to understand and deploy mesh networks with OpenWrt: [Video](https://www.youtube.com/watch?v=vVoZppb_FR0). Very recommended to understand what is a mesh network and how to deploy them.
  * **[UNTESTED]** Repo for automating steps shown in the video by using bash scripts: [Github repo](https://github.com/onemarcfifty/openwrt-mesh) 

## Master Node Router
### Install Dependencies for Mesh Networks

* Remove package your current basic ssl package. In our case, it was `wpad-basic-wolfssl`. If it is not the package it is installed in your current version, try to install the wpad package and it will raise a compatibility issue with the one you need to uninstall.
```bash
opkg remove pad-basic-wolfssl
```
* Install package `wpad-mesh-openssl`
```bash
opkg install wpad-mesh-openssl
```

  * Please, be connected via ethermet because uninstalling/installing this package disconnects Wifi

* Perform a reboot in order to apply changes

### Configure the Mesh

* Remove all previous APs Networks. As it can be seen in the picture, you should leave only `radio0` and `radio1`. 

![image](https://user-images.githubusercontent.com/26599092/218439004-986be7ea-c627-43f3-a5ff-8e8ed07bc44c.png)

* Click on `Add` button on the `MediaTek MT76x8 802.11bgn` (usually `radio0`) in order to deploy the mesh network in the 2.4GHz band.

* Select in Interface configuration/general Setup `802.11s` and Interface Configuration/Wireless Security `WPA3_SAE` encryption. Set a password and **click Save and Apply**.

![image](https://user-images.githubusercontent.com/26599092/218439239-344d2751-ae63-4ebb-b1d6-bee912926efd.png)
![image](https://user-images.githubusercontent.com/26599092/218439281-f43cea16-40f5-47d4-b62d-87c019967c96.png)

## Dumb Access Point Router

* Go to *Interfaces > LAN* and set `DHCP Client` on the protocol. Click *Save* and *Save and Apply*.

![image](https://user-images.githubusercontent.com/26599092/218454682-d4cabf72-ba5c-411e-924e-9035f7b0e933.png)
![image](https://user-images.githubusercontent.com/26599092/218455330-c5aa2833-ab86-49bc-a8db-f772afcc68fc.png)

  * Click on the red option that says *Keep settings* the blue option for some reason failed to me.

### Remove Unnecessary Stuff
----

**For some reason, when disabling services, the AP hangs and does not work. Avoiding this step for now**

----
The recommended video deletes the unnecessary stuff, but we have skipped this step:
"Since we are configuring a dumb AP, we don't need router capabilities. In order to do so, we will disable some services:"


* Connect LAN ports of the routers to each other. (90 seconds to connect the routers) 
* Check the new IP address of the dumb AP in the *Overview > Status > Active DHCP Leases*
* Delete *WAN* and *WAN6* interfaces we will not use.
* If watching the video, skip the setting up of WAN as LAN port. I believe that's not supported in the `Linksys 2500v4` router.
* Go to *Network > Firewall* and delete all zones. (`lan -> wan` and `wan ->` by default).

### Install Dependencies for Mesh Networks

* Remove package `wpad-basic-wolfssl`
* Install package `wpad-mesh-openssl`
  * Please, be connected via ethermet because uninstalling/installing this package disconects wifi
* Perform a reboot in order to apply changes

### Configure the Mesh

* Remove all previous APs Networks. You should leave only `radio0` and `radio1`.
* Click on `Add` button on the `MediaTek MT76x8 802.11bgn` (usually `radio0`) in order to deploy the mesh network in the 2.4GHz band.
* **Make sure you are in the same band and channel than the Master Node**
* Select `802.11s` and `WPA3_SAE` encryption. Set a password and click Save and Apply.

### Add new AP into the Mesh Network

* For this router, it looks like both Master and AP need to be rebooted in order to properly see each other

* Now go to *Network > Diagnostics* and make sure that from the AP you can ping `192.168.1.1` and `openwrt.org`.

## Turn Both Devices into Wifi AP's

* Go to *Network > Wireless*, select the 2.4 GHz band again and add an Access Point network with the desired user and password, all the access points need to have the same name, in order to see all the mesh as one network.
There is no need to put the mesh and the access points in different channels, even if the video says so.

In order to see if the configuration is working you can connect the router master and slave in different locations. Connect to the master and using a power measure app, go towards the other router. You will be able to see how the power decreases while you walk away form the first router. And in the moment of the handover the power will increase again (meaning you are now connected to the second router), and will reach the max power when you get to the second router.
