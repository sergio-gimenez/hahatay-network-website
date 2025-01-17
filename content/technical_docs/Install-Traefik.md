---
title: "Install Traefik"
date: 2023-04-01
---

Trafik is a reverse proxy and load balancer. It is used to redirect all the traffic to the specific service only using the well known ports. It also allows to use signed certificates for the running services via Let's encrypt, that means nothing will complain about not trusting the site. 

In order to set up  and understand this, was very helpful to see this video: [Put Wildcard Certificates and SSL on EVERYTHING - Traefik Tutorial](https://www.youtube.com/watch?v=liV3c9m_OX8)

The steps to have traefik working are the following:

* Create the `data/` directory

  ```
  mkdir data
  cd data
  ```

* Create the `acme.json` file where the certificates will be stored.

  ```source
  touch acme.json
  chmod 600 acme.json
  ```

* Create a `config.yml`file that will filled in by traefik later.

  ```source
  touch config.yml
  ```

* Create the `traefik.yml` file where the configuration will be stored.

  ```source
  touch traefik.yml
  ```

* Edit the `traefik.yml` and compy the following content:

  ```yaml
  api:
    dashboard: true
    debug: true
  <!-- log:
    level: DEBUG -->
  entryPoints:
    http:
      address: ":80"
    https:
      address: ":443"
  serversTransport:
    insecureSkipVerify: true
  providers:
    docker:
      endpoint: "unix:///var/run/docker.sock"
      exposedByDefault: false
    file:
      filename: /config.yml
  certificatesResolvers:
    cloudflare:
      acme:
        email: YOUR_MAIL
        storage: acme.json
        dnsChallenge:
          provider: cloudflare
          resolvers:
            - "1.1.1.1:53"
            - "1.0.0.1:53"
  ```

  * Make sure you add the `YOUR_MAIL` address (the cloudfare) address.
  * As it can be seen, this configuration file assumes that your domain is managed by cloudfare. If you want to use another provider, you can change the provider name to the one you want (and make sure what `resolvers` use).

* Make sure also you fill in the following environment variables in the `docker-compose.yml` file:

  ```yaml
      environment:
      # CF_API_EMAIL, CF_API_KEY - The Global API Key needs to be used, not the Origin CA Key
      - CF_API_EMAIL=${CLOUDFARE_EMAIL}
      - CF_API_KEY=${CLOUDFARE_API_KEY}
  ```

Make sure you create an external network by typing:

```
docker network create proxy
```

Spin the docker container and check if everything went fine by checking the logs (`docker logs traefik --follow`) or by checking the dashboard traefik.intranet-hahatay.org and see the connection secure green lock.


