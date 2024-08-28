---
title: "Monitor the Community Network with Zabbix"
date: 2023-03-26
---

## Zabbix installation

Run the docker-compose that suits you better: https://github.com/zabbix/zabbix-docker.git. In our case, running the ubuntu-mysql version.

Video reference:
* [Zabbix - Open Source, Self Hosted Server, Network, and Device monitoring system with power!](https://www.youtube.com/watch?v=ec2G1PeLS5k)

## Network Devices

Monitoring OpenWrt devices and Linux Servers and apply discovery rules, so zabbix discovers network equipment automatically:

Video reference:
* (Zabbix - Monitoring and Alerting with [@AwesomeOpenSource](https://www.youtube.com/channel/UCwFpzG5MK5Shg_ncAhrgr9g)

## Servers that host Docker containers

Requisites:

* Install `zabbix-agent2` ([Download page](https://www.zabbix.com/download?zabbix=6.4&os_distribution=alma_linux&os_version=9&components=agent_2&db=&ws=))
* Download `zabbix_get` in the zabbix repository with `apt install zabbix_get`

Video Reference:
* [Simple Docker Container Monitoring With ZABBIX](https://www.youtube.com/watch?v=QNdsWp_X9-c)

TL;DR:
* Add `Server` conf in `/etc/zabbix/zabbix_agent2.conf`
* Check logs in `tail -f /var/log/zabbix/zabbix_agent2.log`
* Add the `zabbix` user to the docker group with `gpasswd -a zabbix docker`
* Test that docker information can be accessed through the Docker API with: `zabbix_get -s 192.168.10.4 -k docker.info`