---
title: "Add a new device to OpenWisp"
date: 2025-09-18
---

# Install OpenWisp

The routers should be able to acces to your openwisp domain. In our case they couldn’t and our solution was to manually write it in the router’s hosts list.

```
vim /etc/hosts
```

Under the localhost we write the following:  
	

```
192.168.10.155 openwisp.gandiol.hahatay.network
```

> [!Note]  
> This was our half-baked solution but ideally we should find why the master router is not giving the others the DNS. 
 
> [!IMPORTANT]  
> After this step, it would be safe to double check if now the router reaches the domain. If not, a reboot may be needed.

The following step is to check if the router has any openwisp package installed.

```
opkg list-installed | grep openwisp
```

If not, install it.

```
opkg update
opkg install openwisp-config
opkg install openwisp-monitoring
```

This installs the newest version that the software of the router can manage.

Once installed, some edit is needed in the openwisp configuration file.

```
vim /etc/config/openwisp
```

We can erase its content and write the following instead (this was what we needed, but many other options can be configured here)

```
config controller 'http'
        option url 'https://openwisp.gandiol.hahatay.network'
	option verify_ssl '0'
    	option shared_secret 'shared-secret-of-the-organization'
    	option management_interface 'eth0.2'
	option uuid ''
    	option key ''
```

Here we edit: the url of our domain, the verify\_ssl option (0 in our case, we did not have verification), the shared\_secret (this is obtained in your openwisp interface, going to the configuration of the organization to which the device will belong, creating a new one if needed), the management\_interface (which depends on the router and version of openWRT, it can be checked in luci-\>interfaces, if it is a master it will be something like ‘wan’ or ‘eth0.2’ and if it is a slave it will normally be ‘br-lan’) and the uuid and key which will be given by the software once the agent is activated.

Finally, we activate the agent.

```
/etc/init.d/openwisp-config restart
```

> [!IMPORTANT]  
> Depending on the version of openwisp, it may be *openwisp\_config*.

If everything has worked out correctly, we may now see the device in our openwisp. If something is not working we can check what is happening.

```
logread | grep openwisp
```

