#  Generic

# #  Generic Types

```typescript
function identity<T>(arg: T): T {
  return arg;
}

let myIdentity: <T>(arg: T) => T = identity; // ok
let myIdentity: <U>(arg: U) => U = identity; // ok
let myIdentity: { <T>(arg: T): T } = identity; // ok

interface GenericIdentityFn {
  <T>(arg: T): T;
}
let myIdentity: GenericIdentityFn = identity; // ok
```

# #  Generic Constraints

extends interface

```typescript
interface HasLength {
    length: number
}

function count<T extends HasLength>(element: T): number {
    return element.length;
}
```

# #  Using Type Parameters in Generic Constraints

keyof

```typescript
function getProperty<T, K extends keyof T>(obj: T, key: K) {
  return obj[key];
}
```

# #  Generic Classes

```typescript
function getProperty<T, K extends keyof T>(obj: T, key: K) {
  return obj[key];
}
```