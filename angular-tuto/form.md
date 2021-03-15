# Form

* [template-driven](#template-driven)
* [reactive](#reactive)

## Template-driven

### Set up

use `ngModel` in the built-in Angular Directive: `FormsModule`

In HTML:

1. we need `form`, `input`, `button`

2. bind local ref to `form`, and assign it as `ngForm`

    ```html
    #myForm="ngForm"
    ```

3. bind submit function to `ngSubmit`.

    ```html
    <form #myForm="ngForm" (ngSubmit)="onSubmit()">
    ```

4. bind `ngModel` to `input`, and add `name` attribute

    ```html
    <input name="email" ngModel/>
    ```

```html
<form #myForm="ngForm" (ngSubmit)="onSubmit()">
    <input name="email" ngModel/>
    <button type="submit">Submit</button>
</form>
```

In Component.ts:

```typescript
@Compoent({
    // ...
})
export class AComponent {
    @ViewChild('myForm') myForm: NgForm;

    onSubmit(){}
}
```

### Validation

By default, Angular disables HTML5 validation, and uses [its validators](https://angular.io/api/forms/Validators), like:

* required
* email
* ...

```html
<input name="email" ngModel email required/>
```

To show error message:

1. bind the local ref of `input` with `ngModel`, like what is done to `form`

2. use `ngIf` to check if the `input` is validated

```html
<input #email="ngModel" name="email" ngModel email required/>
<span *ngIf="email.invalid && email.touched">wrong email</span>
```

```css
input.ng-invalid.ng-touched {
    border: 1px solid red;
}
```

### Grouping Form Control

We can control a group of inputs:

```html
<form #myForm="ngForm" (ngSubmit)="onSubmit()">
    <div #myGroupCtrl="ngModelGroup" ngModelGroup="userData">
        <!-- some <input /> -->
    </div>
    <!-- show ngModelGroup error -->
    <p *ngIf="myGroupCtrl.invalid">user data is invalid.</p>
</form>
```

```typescript
@ViewChild('myForm') myForm: NgForm;

// the data of ngModelGroup is saved in myForm
const myGroup = this.myForm.value.userData
```

### Set value of Form

We set some form fields without affecting other fields by using `ngForm.form.patchValue()`.

```typescript
@ViewChild('myForm') myForm: NgForm;

// the data of ngModelGroup is saved in myForm
this.myForm.form.patchValue({
    userData: {
        // data of ngModelGroup
    },
    email: 'my@email.com',
    // other form fields
});
```

### Use value of Form

All the data in `ngForm` is in `ngForm.value`.

### Reset form

reset the form concludes:

* clear the data
* clear the states, like valid, touched, etc

```typescript
@ViewChild('myForm') myForm: NgForm;

this.myForm.reset()
```

### Bonus: Two way binding

A very useful method:

```html
<input #email="ngModel"
    name="email"
    [(ngModel)]="email"
    email required/>
```

```typescript
export class AComponent {
    email = "";
}
```

## Reactive

### Set up

use `formGroup` in `@angular/forms`.

```html
<form [formGroup]="signupForm">
    <input formControlName="username">
    <input formControlName="email">
</form>
```

```typescript
this.signupForm = new FormGroup({
    'username': new FormControl(null ),
    'email': new FormControl(null)
});
```

To submit form, just bind the `onSubmit()` to `ngSubmit`.

```html
<form [formGroup]="signupForm" (ngSubmit)="onSubmit()">
</form>
```

```typescript
onSubmit(){
    // do something with this.signupForm
}
```

### Validation

In `FormGroup`:

```typescript
{
    'username': new FormControl(null, Validators.required),
    'email': new FormControl(null, [Validators.required, Validators.email]),
}
```

To show error message:

```html
<input formControlName="email">
<span *ngIf="signupForm.get('email').invalid && signupForm.get('email').touched">Email error</span>
```

To add the validation to dynamic form field, use `formArray`:

```html
<div formArrayName="newFields">
    <button (onClick)="addNewFieldCtrl()"></button>
    <div *ngFor="let newFormCtrl of getNewFormCtrl(); let i = index">
        <input [formControlName]="i">
    </div>
</div>
```

```typescript
addNewFieldCtrl() {
    const ctrl = new FormControl(null, Validators.required);
    (this.signupForm.get('newFields') as FormArray).push(ctrl);
}

getNewFormCtrl() {
    return (this.signupForm.get('newFields') as FormArray).controls;
}
```

To create custom validator:

```typescript
forbiddenNames = ['admin', 'user'];

forbiddenName(ctrl: FormControl): {[s: string]: boolean} {
    if (this.forbiddenNames.includes(ctrl.value)) {
        return {'isForbiddenName': true}
    }
    return null;
}

{
    'username': new FormControl(
        null,
        [Validators.required, this.forbiddenName.bind(this)])
}
```

`isForbiddenName` can be accessed by `this.signupForm.get('username').errors['isForbiddenName']`.

There are two Observables: `valueChanges` and `stateChanges`. They listen to the changes in `form`.

```typescript
this.signupForm.valueChanges.subscribe(
    value => console.log(value )
);
```
