# HTTP message

HTTP message is composed by:

1. start line

2. header

3. CRLF (empty line)

4. body

## Start line

### Request line

It is composed by:

`Method` `URL` `Version`

```code
GET / HTTP/1.1
```

### Response line

`Version` `code` `reason`

```code
HTTP/1.1 200 OK
```

or

```code
HTTP/1.1 404 Not Found
```

## Header

Header contains the info in **key-value** format. There are some rule.

- Key is insensible to the case. `Host` is equal to `host`.
- `_` and `\s` is not allowed in the key. `-` is ok.
- There is no space before `:`.
- The order of header is meaningless.

### fields

There are 4 classes of header.

- common fields

  It exists in all kinds of http message.

  - `Data`: the **creation time** of http message.

- request fields

  - `Host`: It's **only** the required request fields in `HTTP/1.1`.

  - `User-Agent`: the client who sends the request.

- response fields

  - `Server`: 

- body fields:

   It's a part of the **common fields**.

   - `Content-Length`: the length of the `body`. If this header is not set, the body is sent separately. We need to add `Transfer-Encoding:chuncked`.
