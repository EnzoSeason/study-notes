# Body

![data-type-headers](./img/data-type-headers.png)

## Data type and Encoding

Http Body uses **MIME type** as data type. 

> MIME is Multipurpose Internet Mail Extensions.

There are some categories.

- **text**: text/html, text/css, text/plain, ...

- **image**: image/gif, image/jpeg, image/png, ...

- **audio/video**: audio/mpeg, video/mp4, ...

- **application**: application/json, application/javascript, application/pdf

  If we don't know the type of "application", we use `application/octet-stream`


What's more, we need to know **Encoding type**.

There are 3 kinds.

- **gzip**: it's the most popular one.

- **deflate**

- **br**

## Data type headers

Once a http message has **MIME type** and **Encoding type**, we can seed it.

At client side, we need to add **Accept** to tell the server what kind of data is accepted.

```code
Accept: text/html,application/xml,image/webp,image/png
Accept-Encoding: gzip, deflate, br
```

At server side, the server will add the data type to the headers.

```code
Content-Type: text/html
Content-Encoding: gzip
```

If Encoding is not added, the message won't be compressed at server side, or compressed message won't be accepted.

## Language encoding

The **Unicode character set** that follows the **UTF-8 character encoding** is the standard character set on the Internet.

We set `Accept-Charset` or `Content-Type` in the headers.

```code
// client side

Accept-Language: zh-CN, zh, en
Accept-Charset: gbk, utf-8
```

```code
// server side

Content-Language: zh-CN
Content-Type: text/html; charset=utf-8
```

However, language and charactor set can be detected by both browser and server. Therefore, Only `Accept-Language` will be set at client side, and `Content-Type` is set by the server.

## Priority

Since a browser can accept multiple types of data, we can set the priority by `q`

```code
Accept: text/html,application/xml;q=0.9,*/*;q=0.8
```

That means `text/html` (q = 1.0) > `application/xml` (q = 0.9) > `*/*` (q = 0.8).

## Vary

```code
Vary: Accept-Encoding,User-Agent,Accept
```

That means the server sent the response according to `Accept-Encoding`, `User-Agent` and `Accept` in the resquest headers.