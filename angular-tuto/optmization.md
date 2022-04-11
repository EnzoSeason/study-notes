## Angular Modules & Optimizing Angular Apps

### Understanding NgModule

```typescript
@NgModule({
    declarations:[], // the components, directives, pipes we created
    imports: [], // the modules we used
    exports: [], // export the modules we declared
    providers: [], // the services we used
    bootstrap: [] //—the root component that Angular creates and inserts into the index.html host web page.
})
export class AppModule {}
```

NgModules can't communcate with each other, unless we import / export them.

In AppRoutingModule:

```typescript
const appRoutes: Routes = [
    // ...
];

@NgModule({
    imports: [RouteModule.forRoot(appRoutes)],
    exports: [RouteModule]
})
export class AppRoutingModule {}
```

### Feature Module

Split codes into feature modules. The key point is defining the correct routes.

In ChildRoutingModule:

```typescript
const routes: Routes = [
    // ...
];
@NgModule({
    imports: [RouteModule.forChild(routes)],
    exports: [RouteModule]
})
export ChildRoutingModule
```

### Lazy Loading

Lazy Loading improves the performance. **It makes initial  load faster.**  

The key point is the configuration of routes.

In AppRoutingModule:

```typescript
const appRoutes: Routes = [
    { path: '', redirectTo: '/child', pathMatch: 'full' },
    {
        path: 'child',
        loadChildren: () => import('./child/child.module.ts').then(m => m.ChildModule)
    }
]
```

And, DO NOT import `ChildModule` in `AppModule`.

In ChildRoutingModule:

```typescript
const routes: Routes = [
    {
        path: '',
        component: ChidComponent
    }
]
```

Now, `ChildModule` is created ONLY when it is visited.

However, we can preload lazy loading. The initial bundles are still small. Angular just preload the related modules of current visited module. **It makes subsequent load faster.**  

In AppRoutingModule:

```typescript
@NgModule({
    imports: [RouteModule.forRoot(
        appRoutes,
        {preloadingStrategy: PreloadAllModules})],
    exports: [RouteModule]
})
export class AppRoutingModule {}
```

#### IMPORTANT

If the service is provided in a Lazy Loaded module, the instance of service is created lazily, too. It might cause bugs: you have **create another instance of service**.

The best practice of providing service:

```typescript
@Injectable({
    providedIn: 'root'
})
```

It makes sure that only one instance of service is created in entire App.

### AoT (Ahead-of-Time) vs JiT (Just-in-Time)

Angular parses the project to HTML, CSS, JavaScript DOM operation. There are two way to do:

* JiT: parse the project in runtime, good for dev
* AoT: parse the project before runing, good for production.