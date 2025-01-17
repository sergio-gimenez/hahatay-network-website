---
title: "OpenWrt: Force Routers in the Network use a Local DNS Server"
date: 2024-01-24
---

_Note: This wiki page is very inspired on this [oldish OpenWrt Forum post](https://forum.openwrt.org/t/correct-way-to-set-dns-server/34019/24)._

Long story short, we would like all the traffic from the community network to use our local DNS server and I would like to stop any clients from overriding the DNS with a custom one like Google's (8.8.8.8).

### Set Up WAN

1. Go to `Network` > `Interfaces` > `WAN`.
2. Click `Edit`.
3. Select the `Advanced Settings` tab and uncheck `Use DNS servers advertised by peer`.
4. In the box below, enter the Local DNS Servers `192.168.10.4` and `192.168.10.5`.
5. Click the `Save` button.

![image](https://user-images.githubusercontent.com/42917235/218449522-d61efd2c-a9ad-42a4-b303-32618c005734.png)


### Set Up LAN

1. Go to `Network` > `Interfaces` > `LAN`
2. Under `DHCP Server`, go to `Advanced Options` and set `DHCP-Options` to `6,192.168.10.4,192.168.10.5`.
    * *This advertises different DNS servers to clients. This is what the DHCP server will advertise as NameServer to the hosts (clients). If you don't use it, the router itself will be advertised and will cache and forward the queries to the upstream NameServers.*
3. Click the `Save` button.

![image](https://user-images.githubusercontent.com/42917235/218449541-4a5e90fc-ef0f-4614-88ee-ec869a492d04.png)


### Set Up DHCP & DNS

1. Go to `Network` > `DHCP and DNS`.
2. Under `General Settings` select the `Resolv and Hosts Files` tab ensure the `Ignore resolve file` is unchecked.
3. Click the `Save` button.

![image](https://user-images.githubusercontent.com/42917235/218449576-f9e4f71e-e856-448d-b455-8f3ddcad195d.png)


### Set Up Firewall

1. Go to `Network` > `Firewall`
2. Under the `Port Forwards` tab, click `Add` and enter `Force DNS` under `New port forward` section
3. Set the `Protocol to TCP+UDP`
4. Set `Source zone` to `WAN` **
5. Set `External port` to `53`
6. Set `Destination zone` to `lan` **
7. Set `Internal port` to `53`
8. Click the `Add` button
9. Once it's added to the list open it back up by clicking the `Edit` button
10. Change the `Source zone` from `wan` to `lan`
11. Click the 'Save & Apply' button
    * ****** *If you're unable to set the exact zones simply select anything as you can change it in step 9*

![image](https://user-images.githubusercontent.com/42917235/218449631-232f3a59-6c84-4e57-a777-287a5f6d974b.png)

The firewall rule should look like the following:

![image](https://user-images.githubusercontent.com/42917235/218449656-eaa0ef72-9339-433e-bfbf-a88c452c38b4.png)


Afterwards, save and apply all the changes. Finally, reboot the router by heading to `System` > `Reboot`






