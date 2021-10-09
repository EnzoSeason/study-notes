#  Redirection

The **301 / 302** is a redirection response. In its headers, there is a key, `Location`, its value is the **redirection URI**.

The redirection URI can be "absolue", which contains scheme, host:port, path and query. It can also be "relative". It has only the **path and query**.

```code
Location: /index.html
```

# #  redirection status codes

- 301: Moved Permanently

- 302: Moved Temporarily
