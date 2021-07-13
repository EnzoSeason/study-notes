# Proxy

A proxy forwards requests and responses.

A proxy is used for:

- Load balancing: let multiple machines work together.

- health check: remove crashed machine

- security: protect the source server

- filter the data

- cache

## Attributes

- Via: the **host name** or **domain name** of all proxy machines.

  ```code
  Via: proxy1, proxy2
  ```

- X-Forwarded-For: All the IP addresses of request machine, **client** (the leftest one) and **proxy machines**.

- X-Real-IP: the IP address of the **client**.

## The PROXY protocol

PROXY + ip address type + request ip address + response ip address + request port + response port + \r\n

```code
PROXY TCP4 1.1.1.1 2.2.2.2 55555 80\r\n
```

The client is `1.1.1.1:55555`.


## HTTP cache with Proxy

Server-side

![client-proxy-cache](https://raw.githubusercontent.com/EnzoSeason/study-notes/main/http/img/server-proxy-cache.png)


client-side:

![server-proxy-cache.png](https://raw.githubusercontent.com/EnzoSeason/study-notes/main/http/img/client-proxy-cache.png)
