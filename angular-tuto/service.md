#  Service

The service is injected into the component.

```typescript
import { LogService } from 'LogService';

@Component({
    // ...
    providers: [LogService]
})
export class myComponent {
    constructor(
        logService: LogService
    ){}
}
```

# #  Hierarchical Injector

1. If the service is injected into a component (`providers: [myService]`), the **this component and its children** can use this service.

2. If the service is injected into a child component (`providers: [myService]`), again, Angular will create a new instance of the service for this child component. Avoid doing it !

# #  Injectable

If a service want to be injected by other service, add `@Injectable`.

In Angular 6+, It's better to use:

```typescript
@Injectable({
    providedIn: 'root'
})
```

The advantages are:

* The whole App create one instance of the service.

* Services can be loaded lazily and redundant code can be removed automatically.
