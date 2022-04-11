## Status Code

- 1××: Indicating an intermediate state of protocol processing
- 2××：Success
- 3××：Redirection
- 4××：Request error
- 5××：Server error

### 2××

- 200 OK

- 204 No Content: The response has **no body**.

- 206 Partial Content: The response has **partial body**.

   Usually, it has `Content-Range`. For exemple, `Content-Range: bytes 0-99/2000`. It means get first 100 bytes of 2000 bytes.

### 3××

- 301 Moved Permanently:

   The source no longer exists. we need to switch to a new URL.

- 302 Found:

   The source exists, but we need to use another URL to visit it.

> Both 301 and 302 have `Location` that indicts the redirect URL.

- 304 Not Modified

  It's not of redirection. It's for **caching**.

### 4××

- **400 Bad Request**:

   It's the general request error.

- **403 Forbidden**:

  The client has no right to visit.

- **404 Not Found**:

  The source requested is not found in the server.

- 405 Method Not Allowed: i.e. `POST` isn't allowed.

- 406 Not Acceptable: The source doesn't meet request.

- 408 Request Timeout


### 5××

- **500 Internal Server Error**:

  It's general server error, similar to 400.

- **501 Not Implemented**:
  
  The service is beening developed.


- **502 Bad Gateway**:

  The error code returned by the **gateway** or **proxy**.

- **503 Service Unavailable**:

   The service is busy, unavailable for now. It has `Retry-after`.