# Parent-Child Components

Connection betweent Parent Component and Child Component

## Data binding

### Pass data from *Parent* component to *Child* component

* In parent component:

    ```html
    <child [parentData]="data"></child>
    ```

    ```typescript
    export class Parent {
        data: string
    }
    ```

* In child component

    ```typescript
    import { Input } from "@angular/core";

    export class Child {
        // "parentData" is the property name of element <child>
        @Input("parentData") data: string;
    }
    ```

### Pass data from *Child* component to *Parent* component

* In parent component

    ```html
    <child (getChildData)="getChildData($event)"></child>
    ```

    ```typescript
    export class Parent {
        getChildData(data: string) {
            // TODO
        }
    }
    ```

* In child component

    ```typescript
    import { Output } from "@angular/core";

    export class Child {
        @Output("getChildData") dataEmitter = new EventEmitter<string>();

        someFn(data: string) {
            // doing somthing
            this.dataEmitter.emit(data);
        }
    }

## Local Reference

get the **DOM Element**.

* use function

    ```html
    <input #input />
    <button (click)="getInput(input)"></button>
    ```

    ```typescript
    getInput(input: HTMLInputElement) {}
    ```

* use @ViewChild

    ```html
    <input #input></input>
    ```

    ```typescript
    import { ViewChild, ElementRef } from "@angular/core";

    @ViewChild("input") inputRef: ElementRef;
    ```

    > If `inputRef` is used in `ngOnInit`, use `@ViewChild("input", {static: true})`.

    > If `{static: false}` (by default), it's available after `ngAfterInit`

## Html binding

pass html from Parent to Child

* In Parent:

    ```html
    <child>
        <input />
    </child>
    ```

* In Child

    ```html
    <!-- somthing else -->
    <div>
        <ng-content #content></ng-content>
    </div>
    <!-- somthing else-->
    ```

To get the DOM element in the content, use `@ContentChild`.

The way of using it is the same as the way of using `@ViewChild`.

```typescript
import { ContentChild, ElementRef } from "@angular/core";

@ContentChild("input") inputRef: ElementRef;
```

## View Encapsulation

```typescript
@Component({
    // ...
    encapsulation: ViewEncapsulation.Emulated
})
```

* Emulated: (default), Component's CSS rules is only applied to this component.

* Native: Same as *Emulated*, but using shadow DOM

* None: Component's CSS rules is applied globally.

## Cross components Data passing

If the data needed to be sent to other components without parent-child relation, use `Subject`.

`Subject` is an `Observable` with `next()` function. While `next()` can emit a new value to the `Subject`.

In Service:

```typescript
export class DataService {
    dataSubject = new Subject<string>();
}
```

In Component A, the data is sent.

```typescript
this.dataService.dataSubject.next('data');
```

While, in Component B, the data can be received.

```typescript
this.dataService.dataSubject.subscribe(
    data => this.data = data
);
```
