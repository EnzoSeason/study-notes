## Basic

### Variable

```dart
var name = 'Bob';
// or
String name = 'Bob';
```

Follows the style guide recommendation of using `var`, rather than `type annotations`, for local variables.

#### Null safety

Variables can’t contain null unless you say they can.

```dart
// x can be null.
int? x;
// You must initialize the values of non-nullable variables before you use them.
int y = 0;
```

You don’t have to initialize a local variable where it’s declared, but you do need to assign it a value **before it’s used**.

#### Final and const

- A final variable can be set only once.

- A const variable is a compile-time constant.

Const variables are implicitly final.

Although a final object cannot be modified, its fields can be changed. In comparison, a const object and its fields cannot be changed: they’re immutable.

#### Late variables

There has two use cases:

- Declaring a non-nullable variable that’s initialized after its declaration.

- Lazily initializing a variable.
