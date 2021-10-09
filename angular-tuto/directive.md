#  Directive

* Attribute directive:

    Affect **ONLY the element it is added to**, such as `[ngClass]`, `[ngStyle]`

* Structural directive:

    Affect **a whole area in DOM**, such as: `*ngIf`, `*ngFor`

Syntax:

```typescript
@Directive({
    selector: '[appDirective]'
})
export class myDirective {}
```

```html
 <div appDirective></div>
```

# #  Attribute directive

`ElementRef` lets the attribute directive access the element.

```typescript
import { ElementRef } from '@angular/core';

constructor(elementRef: ElementRef) {}
```

* Using `Renderer2` from `@angular/core` to manipulate DOM is better than modifying DOM Element directly. Because we don't know if we can access the DOM.

    ```typescript
    import { ElementRef, Renderer2 } from '@angular/core';

    constructor(
        elementRef: ElementRef,
        render: Renderer2) {}
    ```

* `@HostListener` listens to the DOM Event.

    ```typescript
    @HostListener('mouseenter') mouseEnter(event: Event) {
        // TODO
    }
    ```

* `@HostBinding` binds the element's property

    ```typescript
    @HostBinding('style.backgroundColor') backgroundColor: string;
    ```

* `@Input` can be used in Directive. It is used as that in `@Component`.

# #  Structural directive

```html
<div *ngIf=[isOdd]></div>
```

is equal to

```html
<ng-template [ngIf]="isOdd"><ng-template>
```

# # #  Create a structural directive

```typescript
import { TemplateRef,ViewContainerRef } from '@angular/core';

@Input() set unless(condition) {
    // this func executes once the property is changed
    if (!condition) {
        this.vcRef.createEmbeddedView(this.templateRef);
    } else {
        this.vcRef.clear()
    }
}


constructor(
    templateRef: TemplateRef<any>, // access the ng-template
    vcRef: ViewContainerRef, // mainpulate the view
    ) {}

```
