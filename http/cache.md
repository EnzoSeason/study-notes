# Cache

The response can be cached at the **client side**. In response header, `Cache-Control` controls the cache.

- max-age: the available duration
- no-store: the reponse can't be cached
- no-cache: before using cache, ask server to check if it can be used.
- must-revalidate: After expiring, ask server to check if it can be used in the future.

## When the cache is used

When we click `backward`.

If we refresh the web, the browser will send the request with `Cache-Control: max-age=0`. (`Ctrl + F5` will add `Cache-Control: no-cache`.)

## Use the cache

1. `if-Modified-Since` and `Last-modified`

   The previous response will set `Last-modified`, a timestamp.
   The current request will put it in `if-Modified-Since`. If there is no update, the server will return a **304 Not Modified** response.

2. `If-None-Match` and `ETag`

   The previous response will set `ETag`, a unique resource identifier.
   The current request will put it in `If-None-Match`. If there is matched, the server will return a **304 Not Modified** response.