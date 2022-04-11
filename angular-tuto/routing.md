## Routing

Basic syntax:

```typescript
import { Routes } from '@angular/router';

const routes: Routes = [
    {
        path: 'my-component',
        component: myComponent,
    },
];

@NgModule({
    // ...
    imports: [
        RouterModule.forRoot(routes),
        // ...
    ]
})
```

```html
<!-- angular built-in directive -->
<route-outlet></route-outlet>
```

### Navigation

#### `<a> link`

The link can be added like: `<a href="/my-component">`. But, Angular will rebuild the page when the user clicks on that,  since Angular will send a request to the server. Not good :(.

It's better use: 

* `<a routerLink="/my-component">`

* `<a [routerLink]="['/my-component']">`

Besides, using `routerLinkActive` and `routerLinkActiveOptions` can style the link.

#### router

```typescript
import { Router } from '@angular/router';

export class oneComponent {
    constructor(
        private router: Router,
    ){}

    someFn() {
        this.router.navigate(['/my-component']);
    }
}
```

For now, the route is absolute. We can use relative route, too.

```typescript
import { Router, ActivatedRoute } from '@angular/router';

export class oneComponent {
    constructor(
        private router: Router,
        private route: ActivatedRoute
    ){}

    someFn() {
        this.router.navigate(
            ['my-component'],
            { relativeTo: this.route }
        );
    }
}
```

#### route parameters

We can pass `id` to the route: 

```typescript
const routes: Routes = [
    {
        path: 'my-component/:id',
        component: myComponent,
    },
];
```

To fetch `id`, we can:

* snapShot of route:

    ```typescript
    import { ActivatedRoute } from '@angular/router';

    export class oneComponent {
        constructor(
            private route: ActivatedRoute
        ){}

        someFn() {
            const id = this.route.snapshot.params['id'];
        }
    }
    ```

    The problem is, the route might be changed. We need read it asynchronically.

* Observable of route:

    ```typescript
    this.route.params.subscribe(
        params => {
            const id = params['id'];
        }
    );
    ```

**Query Parameters and Fragments** can be used in router:

For example, url is `prefix/my-component?userId=1#new`

* `<a> link`:

    ```html
    <a [routeLink]="['/my-component']"
       [queryParams]="{userId: '1'}"
       [fragment]="'new'"
    ></a>
    ```

* router:

    ```typescript
    this.router.navigate(
        ['/my-component'],
        {queryParams: {userId: '1'}},
        fragment: 'new'
    );
    ```

To get them:

* snapShot of route:

    ```typescript
    const queryParams = this.route.snapshot.queryParams;
    const fragment = this.route.snapshot.fragment;
    ```

* Observable of route:

    ```typescript
    this.route.queryParams.subscribe();
    this.route.fragment.subscribe();
    ```

There an useful option:

* queryParamsHandling:

    preserve or override the queryParams of parent route.

    ```typescript
    this.router.navigate(
        ['my-component'],
        {
            relativeTo: this.route,
            queryParamsHandling: 'preserve'
        }),
    ```

### wildcard and redirection

```typescript
const routes: Routes = [
    // all the other routes
    {
        path: '**', // match all the routes
        redirectTo: '/not-found'
    }
];
```

Here, it shows that **the ordre in the array routes** matters ! Angular reads the routes from top to bottom.

If the the path `**` is placed at top, all the rest of the routes won't work.

### Route Guards

A Guard can be added to check if a route can be accessed.

1. Create a **Guard Service**

    ```typescript
    @Injectable()
    export class AuthGuard implements CanActivate {

        constructor(
            private authService: AuthService,
            private router: Router) {}

        canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): Observable<boolean> | Promise<boolean> | boolean {
            if (somthing) {
                // logged in so return true
                return this.authService.isAuthenticated();
            } else {
                this.router.navigate(['login ']);
                return this.authService.isNotAuthenticated();
            }
        }
    }
    ```

2. Inject it into module

    ```typescript
    @NgModule({
        // ...
        providers: [
            AuthService,
            AuthGard
        ]
    })
    export class AppModule {}
    ```

3. Use Guard in Routes

    ```typescript
    const routes: Routes = [
        {
            path: 'my-component',
            component: MyComponent,
            canActivate: [AuthGuard],
        }
    ]
    ```

Besides,

* `canActivateChild` add Guard to the component and its children.
* `canDeactivate` is a guard for leaving a route.

### Static data in route

We can pass static data of route.

```typescript
    const routes: Routes = [
        {
            path: 'my-component',
            component: MyComponent,
            data: { message: 'some messages' }
        }
    ]
```

```typescript
const data = this.route.snapshot['data'];
// or
this.route.data.subscribe();
```

### Dynamic data in route

We can create a **Service** which implements `Resolver` to deal with dynamic data in route.

```typescript
    const routes: Routes = [
        {
            path: 'my-component',
            component: MyComponent,
            resolve: { myResolve: MyResolve }
        }
    ]
```

```typescript
this.route.data.subscribe(
    data => {
        this.data = data['myResolve'];
    }
)
```

`MyResolve` looks like:

```typescript
@Injectable()
export class MyResolve implements Resolve<SomeType> {

    constructor(
        private someServer: SomeService
    ) {}

    resolve(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): Observable<SomeType> | Promise<SomeType> | SomeType {
        return this.someService.getSomething();
    }
}
```