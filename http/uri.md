#  URI (Uniform Resource Locator)

URI = URL & URN.

Since URL is so popular, sometimes, we make URI = URL.

# #  URI format

```code
scheme :// host:port /path ?query # fragment
```

- scheme: It can be http, https, ftp, file, ...

- host: It can be **domain name** or **IP address**.

- port (optional): If the port is omitted, a default port will be applied. For `http`, it's **80**, `https` is **443**.

- path: It starts with `/`.

- query: It's in `key-value` format, starts with `?`, connects the items by `&`. For example, `?name=jack&age=10`

- fragment: It's only used by the client. The browser won't send it to the server.

# #  URI Encoding

URI uses **ASCII** code.

1. It converts non-ASCII codes or special characters into **hexadecimal byte**, and add `%` before it.

    For exemple, space is `%20`.

2. Use `encodeURL()`.

   It encodes a URI by replacing each instance of certain characters by one, two, three, or four escape sequences representing the **UTF-8 encoding** of the character.

   ```javascript
   const uri = 'https://mozilla.org/?x=шеллы';
    const encoded = encodeURI(uri);
    console.log(encoded);
    // expected output: "https://mozilla.org/?x=%D1%88%D0%B5%D0%BB%D0%BB%D1%8B"
   ```