#  DNS

It maps **Domain name** to **IP address**.

1. Root DNS Server

   It returns IP address of "com", "org", "io", etc.

2. Top-level DNS Server

   In `com` Top-level DNS Server, we can find `apple.com`.

3. Authoritative DNS Serve

   In `apple.com` Authoritative DNS Serve, we can find `www.apple.com`.

```conf
server {
    listen 80;                       # 监听80端口
    server_name  time.geekbang.org;  # 主机名是time.geekbang.org
    ...
}
```

# #  Caching

Once we visited a website, its **IP address** is cached.

1. Browser

2. Operation System

   OS can not only cache the **IP address** of websites, but also that of **local files**. In `hosts` file, we can custom the domain name of **local files**.

3. DNS

   There are third-party DNS, too. It helps reduce the pressure of main DNS server. There are "8.8.8.8" (Google), "4.2.2.1" (Microsoft), etc.

   ```conf
   resolver 8.8.8.8 valid=30s;  # 指定Google的DNS，缓存30秒
   ```

# #  Load balancing based on domain name

If the server of "buy.tv" need maintain, we can switch to another server by telling DNS, mapping "buy.tv" to new server's IP address "4.5.6.7" instead of current IP address "1.2.3.4".

**One domain name** is mapped with **multiple server machines**.

What's more, we can create domain name of inner services. For example, we can create "mysql.inner.app" is for MySQL database service.


