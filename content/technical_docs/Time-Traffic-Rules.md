---
title: "Time Traffic Rules"
date: 2025-09-18
---

## Block the exit to internet

In order to block the exit to internet on all the the routers form the main router, we created a rule on **Network** -> **Firewall** -> **Traffic Rules** with the following parameters shown in the image.
![Captura de pantalla 2025-01-29 125312](https://github.com/user-attachments/assets/6da877e4-7dcc-45f4-a394-45780c5be38e)

This way, the main router, which has the exit to internet on the WAN exit, blocks the IPs we add from internet and, at the same time, allows us to acces the local network besides the rule.

### Depending the hour
On one haned, if what we wanted is to block the internet on certain hours of the day we would go to **Time Restrictions** and specify the hours where the rule aplies. In the photo, is an example which blocks the internet from 23:00 to 08:00.
![Captura de pantalla 2025-01-29 125342](https://github.com/user-attachments/assets/3d54882c-83ad-4fbd-88c8-474d81aac151)

### Depending the day
On the other hand, if we wanted to block the internet on certain days, we would specify it similarly. In the photo, is an example where the internet is blocked on Saturday and Sunday.
![Captura de pantalla 2025-01-29 125359](https://github.com/user-attachments/assets/65c9cb2d-c08a-4fe1-96af-295af4369d22)