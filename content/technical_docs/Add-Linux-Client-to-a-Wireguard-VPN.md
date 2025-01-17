---
title: "Add Linux Client to a Wireguard VPN"
date: 2023-04-22
---

Login ssh into server:

Install wireguard:

```bash
sudo apt install wireguard
```

Move into the `wireguard` directory:

```bash
sudo su
cd /etc/wireguard
```

Copy the Wireguard config file into a `wg0.conf` file. To do so, run the following command with your proper wireguard conf file:

```bash
echo "
[Interface]  
PrivateKey = XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
Address = 10.0.0.7/24
DNS = 1.1.1.1,1.0.0.1


[Peer]
PublicKey = XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
PresharedKey = XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
AllowedIPs = 0.0.0.0/0, ::/0
PersistentKeepalive = 25
Endpoint = wg.server.com:51820" > /etc/wireguard/wg0.conf
```

Now, enable the wireguard interface `wg0`, so the server can connect to the VPN.

```bash
sudo wg-quick up wg0
```

In Ubuntu 20.04 I found a problem with `resolvconf` [Ref](https://superuser.com/questions/1500691/usr-bin-wg-quick-line-31-resolvconf-command-not-found-wireguard-debian)

Creating this simlink solves the error: 

```bash
ln -s /usr/bin/resolvectl /usr/local/bin/resolvconf
```

### Starting a VPN Client Automatically

[_Source_](https://techoverflow.net/2021/07/02/how-to-autostart-wireguard-using-systemd-wg-quick/)

If you’ve added a wg-quick config, e.g. /etc/wireguard/wg0.conf, you can enable autostarting it on system boot using systemd:

```
sudo systemctl enable --now wg-quick@wg0
```

If you have started Wireguard with this config manually before, you need to shut it down first or systemd will not be able to start it !



