# Advanced Type

## Type Guards

* check basic type of JavaScript: `typeof a === 'string'`
* check the property of object (same in JS): `pro in obj === true`
* check class (same in JS): `obj instanceof OneClass === true`

### User-Defined Type Guards

```typescript
function isFish(pet: Fish | Bird): pet is Fish {
  return (pet as Fish).swim !== undefined;
}
```

`pet is Fish` is our type predicate in this example. A predicate takes the form `parameterName is Type`, where parameterName must be the name of a parameter from the current function signature.

```typescript
// Both calls to 'swim' and 'fly' are now okay.
let pet = getSmallPet();

if (isFish(pet)) {
  pet.swim();
} else {
  pet.fly();
}
```

## Index properties

With index types, you can get the compiler to check code that uses dynamic property names of definded type.

```typescript
interface ErrorContainer {
    [prop: string]: string
}

const error: ErrorContainer = {
    typeError: 'type error',
    httpError: 'network error'
}
```

## Function overload

```typescript
function add(a: number, b: number): number;
function add(a: string, b: string): string;
function add(a: string, b: number): string;
function add(a: number, b: string): string;
function add(a: number | string, b: number | string) {
    if (typeof a === 'string' || typeof b === 'string') {
        return a.toString() + b.toString();
    }
    return a + b;
}

add('1', 2);
```

## Optional Chain

`a?.b`: get `b` after checking `a` is `null` or `undefinded`

## ??

`const a = b ?? 'DEFAULT'`: if `b` is `null` or `undefinded`, a will be `'DEFAULT'`
