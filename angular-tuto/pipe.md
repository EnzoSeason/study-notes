#  Pipe

Basic pipe: my-pipe.pipe.ts

```typescript
import { PipeTransform } from '@angular/cores';

@Pipe({
    name: 'myPipe'
})
export class MyPipe implements  PipeTransform {
    transform(value: any) {
        return value;
    }
}
```

To use it:

```html
<p>{{ something | myPipe }}</p>
```

To pass the arguments to pipe:

```typescript
import { PipeTransform } from '@angular/cores';

@Pipe({
    name: 'myPipe'
})
export class MyPipe implements  PipeTransform {
    transform(value: any, argA: string, argB: string) {
        return value;
    }
}
```

```html
<p>{{ something | myPipe:'foo':'toto ' }}</p>
```

# #  Data changes

Pipe reruns ONLY the input of the pipe changes. So, changing the data of the page won't rerun the pipe.

Angular does that to improve the performance. However, we can override it, but it's not recommanded.

```typescript
@Pipe({
    name: 'myPipe',
    pure: false
})
```
