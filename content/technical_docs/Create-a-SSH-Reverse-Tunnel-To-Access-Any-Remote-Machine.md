---
title: "Create a SSH Reverse Tunnel To Access Any Remote Machine"
date: 2023-02-04
---

How to access any machine through reverse SSH tunneling.

Things needed:

* **Restricted Machine**: Machine unaccessible remotely that we want to have access.
* **Public Machine**: A machine that can be accessed from anywhere. That might be because it uses a public IP or because it has a Dynamic DNS service such as [DuckDNS](http://www.duckdns.org/).
* **Client** to access the remote machine: Any machine that has internet access and SSH.

From **restricted machine** acces **public machine**:

```bash
ssh PublicMachineUsername@publicIPaddress -R 5555:localhost:22
```

SSH to Public IP machine from the client:

```bash
ssh PublicMachineUsername@publicIPaddress
```

Use reverse SSH:

```bash
ssh -p 5555 RestrictedMachineUsername@localhost
```

----

specific case

From **restricted machine** access **public machine**:

```bash
ssh PublicMachineUsername@publicIPaddress -R 5555:localhost:22
```

SSH to Public IP machine:

```bash
ssh PublicMachineUsername@publicIPaddress
```

Use reverse SSH:

```bash
ssh -p 5555 user@localhost
```

