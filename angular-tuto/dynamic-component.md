#  Dynamic component

 To create a dynamic component, such as a popup, use `*ngIf`:

```typescript
@Compoent({
    seletor: 'popup',
    // ...
})
export class PopupComponent {
    @Input() message = "";
    @Output() onClose = new EventEmitter<void>();

    onCloseFn () {
        this.close.emit()
    }
}
```

```html
<popup
    *ngIf="hasError"
    [message]="some error"
    (onClose)="closePopup()">
</popup>
```

```typescript
closePopup() {
    this.hasError = false;
}
```
