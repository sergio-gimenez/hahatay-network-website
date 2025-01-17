---
title: "How to set up an antenna for the first time?"
date: 2024-02-12
---

1. Connect the antenna to the power source. Plug the adapter into the power source and connect the POE input on the adapter to the antenna.
2. Connect the antenna to the computer via Ethernet.
3. Configure the connection with a fixed IP address.
![image](https://github.com/aucoop/hahatay-community-network/assets/79020335/132b21aa-e0d5-49a2-90de-c1340e440ca3)

4. Access the antenna configuration by entering its IP address (default is 192.168.20.1). Enter the default username and password (ubnt). Set the country to Spain and the language to English.
![image](https://github.com/aucoop/hahatay-community-network/assets/79020335/1a50a403-3871-43a7-959f-0e9b0c8c40a6)

5. In the wireless tab, configure the antenna as either an Access Point or a Station. Depending on whether the antenna is set up as an Access Point or Station, it will have a specific configuration:

*Access Point*
- Assign an SSID to the Access Point (it should be the same on both antennas that are connecting).
- Optionally, manually choose a frequency to avoid interference in case of multiple connections.
![image](https://github.com/aucoop/hahatay-community-network/assets/79020335/a64f221c-b2f5-4f6a-998d-be6bf401b72b)

*Station*
- Provide the SSID of the Access Point to which it needs to connect. If the other antenna is powered on, you can search for the SSID by clicking on "Select."
![image](https://github.com/aucoop/hahatay-community-network/assets/79020335/0a835b7b-c924-4872-95f7-38a2a9206868)

Note: To save the changes, click on "Change," and then on "Apply" before switching tabs.
The first time you make a change, it will prompt you to change the default password. Please change the password to your preferred one.

6. In both cases (Access Point and Station), configure the antenna as 14x14 (1x1) 23 dBi.

7. Add WPA2 security and set a passphrase (the passphrase must be the same on both antennas for a connection).

8. In the network tab, set the IP address of the antenna. In the case of the station for link 3, the IP would be 192.168.10.15.
![image](https://github.com/aucoop/hahatay-community-network/assets/79020335/138e7bd6-b1fb-464f-a0d2-84897921da9a)

9. After changing the IP, you will need to reassign an IP address to your computer to access the configuration.
![image](https://github.com/aucoop/hahatay-community-network/assets/79020335/23bc3911-54d4-4482-a38c-39b2e5f62db1)

10. To enhance the connection, set the output power to the maximum in the "Advanced" tab. In the wireless tab, uncheck "Calculate EIRP Limit" and increase the Output Power slider to 25 dBm.
![image](https://github.com/aucoop/hahatay-community-network/assets/79020335/dfa782fc-479f-412f-8d74-539922a850be)
![image](https://github.com/aucoop/hahatay-community-network/assets/79020335/ee941cbc-4e57-4156-b872-9e60ccc6fe56)

