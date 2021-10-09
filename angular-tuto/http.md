#  HTTP

use `HttpClient` of `@angular/common/http`

The date received is saved as an `Observable`

```typescript
import{ HttpClient } from '@angular/common/http';

@Injectable({provided In: 'root'})
export class AService {
    constructor(private http: HttpClient) {}

    aFunc() {
        // basic request
        this.http.get('/url');

        // manipulate response (Observable)
        this.http.get('/url').pipe(
            map(item => {
                // to do something
                return item;
            })
        ):

        // set the type of the respose.
        this.http.get<Item>('/url');
    }
}
```

```typescript
this.aService.aFunc().subscribe(
    response => {
        // data is saved in response
        this.data = response;
    },
    error => {
        // deal with error
    }
)
```

# #  Request / Response setting

# # #  Set request header

```typescript
this.http.get(
    '/url',
    {
        headers: new HttpHeaders({'my-header': 'foo'})
    }
)
```

# # #  Set request Query Params

```typescript
const params = new HttpParams();
params.append('my-key', 'my-value');
params.append('you-key', 'you-value');
this.http.get(
    '/url',
    {
        headers: new HttpHeaders({'my-header': 'foo'}),
        params: params
    }
)
```

Which is equal to `/url?my-key=my-value&you-key=you-value`.

# # #  Set response observe

```typescript
this.http.get(
    '/url',
    {
        observe: 'body' //default
    }
)
```

Other `observe`:

* `response`: return the whole response
* `event`: return the all the events received during Http request

# # #  set response Type

```typescript
this.http.get(
    '/url',
    {
        observe: 'body', //default
        responseType: 'text'
    }
)
```

# #  Interceptor

To add extra information to every http request, we use Interceptor

1. create a Interceptor as a Service

    ```typescript
    export class AuthInterceptorService implements HttpInterceptor {
        intercept(req: HttpRequest<any>, next: HttpHandler) {
            // do something to the request
            const modifiedReq = req.clone({
                headers: req.headers.append('Auth', 'abcd')
            });
            return next.handle(modifiedReq);
        }
    }
    ```

2. register the Interceptor

    ```typescript
    @NgModule({
        // ...
        providers: [
            {
                provide: HTTP_INTERCEPTORS, // in @angular package
                useClass: AuthInterceptorService,
                multi: true, // allow using angular default interceptor
            }
        ]
    })
    export class AppModule {}
    ```

