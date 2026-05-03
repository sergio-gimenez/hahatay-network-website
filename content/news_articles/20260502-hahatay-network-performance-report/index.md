---
title: "Hahatay Network: Progress Report on Connectivity and Usage (January 2025 – April 2026)"
date: 2026-05-02T10:00:00Z
authors:
  - "sergio-gimenez"
categories:
  - "news"
tags:
  - "isoc"
  - "ctuc"
  - "monitoring"
  - "network"
---

One year into the [Internet Society Foundation's Connecting the Unconnected grant](../20250828-hahatay-isoc-cunc-grant-winner/), we are sharing an interim progress report on the Hahatay community network in Gandiol, Senegal. The data covers January 2025 through April 2026 and shows a network that has improved significantly — and also one that went through real growing pains before reaching its current stability.

## The short version

- Download speed increased by **161%**, from 6.54 Mbps to 17.08 Mbps
- Average cost per person per month decreased by an estimated **35%**, approaching the 40% target
- The number of daily users grew, with peaks of **80 unique clients** in a single day
- The network went through a turbulent transition period in mid-2025, but has stabilized clearly in 2026

## Connectivity: faster and more stable

At the start of 2025, the network operated under constrained conditions. Average download speed was 6.54 Mbps and upload was 0.89 Mbps.

After infrastructure upgrades carried out during 2025, the network reached an average download speed of **17.08 Mbps** and an average upload speed of **4.01 Mbps** in the January–April 2026 period. The highest recorded download speed in the dataset was 21.27 Mbps.

{{< figure src="01_speed_timeseries.png" caption="Download and upload speed over the reporting period" >}}

The improvement was not linear. After the infrastructure upgrade, the network went through a period of instability — with latency peaks above 1,000 ms and packet loss above 40% at certain points. This reflects the complexity of upgrading capacity while the network was actively used and its architecture was being adjusted.

{{< figure src="02_latency_packetloss.png" caption="Latency and packet loss over time" >}}

By early 2026, the situation had improved clearly:

- Average latency fell to **102 ms**
- Average packet loss stayed below **1%**
- Variability decreased substantially

This tells us that the technical work carried out during late 2025 was effective.

## Growing demand across sites

The usage data tells a story of steady adoption.

{{< figure src="03_site_wifi_clients_timeseries.png" caption="Daily unique Wi-Fi clients by site" >}}

**Sunukeur** is the main hub, with an average of 23.9 unique clients per active day and a single-day peak of 70. **Aminata** and **Keru-Jiggen** show moderate but consistent growth. The highest aggregate daily total across all monitored sites reached **80 unique clients** in a single day.

Session data gives additional insight into intensity of use. Sunukeur reached 669 sessions in a single day; aggregate sessions peaked at 683. These numbers indicate that people are not just connecting occasionally — they are using the network repeatedly throughout the day.

## Cost per person: approaching the target

The grant set a target of reducing the average monthly cost of connectivity per person by **40%**. Based on the monthly YAS business plan cost (173.79 USD) and the growth in monitored daily users, the current estimate shows a **35.2% reduction** — from 7.20 USD/person/month at baseline to 4.66 USD/person/month in the stabilized 2026 period.

The target is within reach but has not yet been fully achieved. Continued growth in user adoption will help close this gap.

## How demand is distributed

Traffic is not evenly spread across sites. Sunukeur carries the highest sustained load, with average daily WAN traffic around 3.15 Mbps and peaks above 4 Mbps. Keru-Jiggen and Defaratt show lower but consistent activity.

{{< figure src="01_site_traffic_timeseries.png" caption="Average daily WAN traffic by site" >}}

{{< figure src="03_hourly_profile.png" caption="Speed and latency by hour of day" >}}

The hourly profile shows a typical shared-network pattern: faster and lower-latency at night and early morning, slower during midday and afternoon when demand peaks. This is a sign that the network is being genuinely used — and that future capacity planning will need to account for concentrated demand.

## What comes next

This is an interim report. The monitoring system is still being improved, and the final report will include more complete site-level data and more detailed metric coverage. A number of issues with stale device records, naming inconsistencies, and incomplete site visibility have already been corrected, and further improvements are in progress.

The overall picture is positive: the network has moved from a limited and less stable system toward a more robust and more widely used infrastructure. The work ahead continues to focus on capacity, sustainability, and the monitoring improvements needed to understand demand in greater detail.

---

*This report is part of the documentation produced for the [Internet Society Foundation's Connecting the Unconnected program](https://www.isocfoundation.org/). Full monitoring data and methodology are available in the project repository.*
