---
title: "Install OpenWrt Xiaomi Router (1GB)"
date: 2023-03-01
---

Visit this link to get to the documentation for [OpenWRT Xiaomi 1GB](https://openwrt.org/inbox/toh/xiaomi/xiaomi_mi_router_4a_gigabit_edition), and this link for going to the [Repo Exploit OpenWRT](https://github.com/acecilia/OpenWRTInvasion)

```bash
git clone [Repo Exploit OpenWRT](https://github.com/acecilia/OpenWRTInvasion)
```

> **IMPORTANT**: Connect through Ethernet, as OpenWRT installation will disable WiFi per default

> **IMPORTANT**: Make sure the snapshot used to update the firmware is image and not initramfs. You will be able to see that by getting into the Xiaomi 


# Setting up default configuration of router
Make sure router is in default state (after configuring it initially). I followed this manual here https://manuals.plus/xiaomi/router-4a-gigabit-edition-manual. Make sure router is using default IP 192.168.31.1. I stetted up region as Spain because Senegal was not available, and you also need to accept Terms and Conditions (as always).

# Setting up your environment

To set up the environment be sure to be in the directory where you have cloned OpenWRT exploit, then proceed as follows:

```
cd OpenWRTInvasion/
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

# Running the exploit and accessing the router

When I ran the exploit, the prompts were different as per other users in Github. For example, I was not asked for the Stok value, but only the IP.

```
python3 remote_command_execution_vulnerability.py
```

Easiest way to get into the server will be:
```
telnet 192.168.31.1
```

# Installing new firmware

Download the firmware version for that Router model. 
 
> **IMPORTANT**: Make sure the snapshot used to update the firmware is image and not initramfs. You will be able to see that by getting into the Xiaomi

```
curl --insecure [link_to_snapshot] > /tmp/sysupgrade.bin
```

We used the following link (https://downloads.openwrt.org/releases/22.03.3/targets/ramips/mt7621/openwrt-22.03.3-ramips-mt7621-xiaomi_mi-router-4a-gigabit-squashfs-sysupgrade.bin) and it worked. If it does not work for you, read the documentation to make sure you use the correct link in order to prevent bricking the device. As said in the beginning, the image has to be a sys-upgrade image. 

```
curl --insecure https://downloads.openwrt.org/releases/22.03.3/targets/ramips/mt7621/openwrt-22.03.3-ramips-mt7621-xiaomi_mi-router-4a-gigabit-squashfs-sysupgrade.bin > /tmp/sysupgrade.bin
```

Install and reboot

```
mtd -r write /tmp/sysupgrade.bin OS1
```

# Get through SSH to router and install LuCI

```
ssh root@192.168.1.1
```

Make sure that LuCI and the required packages for SSL encryption are installed with the following commands.

```
opkg update
opkg list-installed
```

If they are not installed, proceed as follows:

```
opkg install luci
opkg update
opkg install luci-ssl
/etc/init.d/uhttpd restart
```

Now reload LuCI interface and verify that you are using HTTPS.