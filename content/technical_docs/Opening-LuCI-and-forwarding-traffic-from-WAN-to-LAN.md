---
title: "Opening LuCI and forwarding traffic from WAN to LAN"
date: 2024-02-12
---

First, I found very interesting [this video](https://www.youtube.com/watch?v=UvniZs8q3eU) to understand how firewalls and uptables work.

## Enabling Access to LuCI from Backhaul Network

In order to access LuCI from the backhaul network (through the WAN interface of the router) we need to set Input tule of Wan Zone on Firewall to `accept`. 

In `Network` > `Firewall`you should change it and see something like this:
![image](https://github.com/aucoop/hahatay-community-network/assets/79020335/0be68a72-227a-4d17-80d2-6ca154870488)
![image](https://user-images.githubusercontent.com/42917235/219714170-9d797f61-59af-447e-ade7-16c238d42481.png)

## Enabling Traffic forwarding from Backhaul Network to other Local Networks

In order to let traffic flow from the backhaul network to the several local subnetworks in the community networks, we need to also enable forwarding from `wan` to `lan` zones, as shown in the picture below.

![image](https://user-images.githubusercontent.com/42917235/219714237-9c54295f-ef2e-4049-8115-094db45f5c22.png)
Finally, in the backhaul rotuer (`router-red-comunitaria` router in our case) is mandatory to set a static routing rule. 

Go to `Network` > `Routing` and add the necessary IPs.

![image](https://user-images.githubusercontent.com/42917235/219714237-9c54295f-ef2e-4049-8115-094db45f5c22.png)

## If you are using LiteBeam antennas
Select the WDS (Transparent Bridge Mode). This allows the PtP link act as a super long Ethernet cord essentially.
![image](https://github.com/aucoop/hahatay-community-network/assets/79020335/7e5e893e-2c3c-46ee-992d-251f6835e6ae)

For more details see: [How to set up an antenna for the first](https://github.com/aucoop/hahatay-community-network/wiki/How-to-set-up-an-antenna-for-the-first-time%3F)

