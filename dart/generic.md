## Generics

### Why use generics?

Generics are often required for **type safety**, but they have more benefits than just allowing your code to run:

- Properly specifying generic types results in **better generated code**.

- You can use generics to **reduce code duplication**.

## Using collection literals

List, set, and map literals can be parameterized.

```dart
var names = <String>['Seth', 'Kathy', 'Lars'];
var uniqueNames = <String>{'Seth', 'Kathy', 'Lars'};
var pages = <String, String>{
  'index.html': 'Homepage',
  'robots.txt': 'Hints for web robots',
  'humans.txt': 'We are people, not machines'
};
```

### Using parameterized types with constructors

To specify one or more types when using a constructor, put the types in angle brackets (`<...>`) just after the class name.

```dart
var nameSet = Set<String>.from(names);

var views = Map<int, View>();
```

### Restricting the parameterized type

When implementing a generic type, you might want to limit the types that can be provided as arguments, so that the argument must be a subtype of a particular type. You can do this using `extends`.

```dart
class Foo<T extends Object> {
  // Any type provided to Foo for T must be non-nullable.
}
```
