---
title: "Redundant Synchronised Local Pi Hole DNS Setup"
date: 2023-04-22
---

In order to have DNS redundancy, it is interesting to have more than one DNS server. The [gravity-sync](https://github.com/vmstan/gravity-sync) utility allows you to have two synchronised pihole instances in very simple ways.

* Follow their [tutorial step by step](https://github.com/vmstan/gravity-sync/wiki#setup-steps) to make it work.
* Also, a [nice but a bit old video](https://youtu.be/IFVYe3riDRA) to understand why gravity-sync is used for.

This has been tested and validated using two instances of pihole running both in a docker container using the example docker-comopse.

Another goal, also, was to overcome the _Maximum number of concurrent DNS queries reached (max:150)_ error, coming mostly from routers of the community network. Having two piholes might help two split the DNS queries in two instances, but might be not enough.

Follow [this post](https://discourse.pi-hole.net/t/resolved-maximum-number-of-concurrent-dns-queries-reached/60970/2) to increase max DNS forward limit and the minimum time-to-live settings for cached lookups. This seems to solve the warning.