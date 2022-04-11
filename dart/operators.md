## Operators

### Arithmetic operators

| Operator | Meaning                                               |
| -------- | ----------------------------------------------------- |
| ~/       | Divide, returning an **integer** result               |
| %        | Get the remainder of an **integer** division (modulo) |

### Equality and relational operators

To test whether two objects x and y represent the same thing, use the `==` operator.

1. If _x_ or _y_ is null, return true if both are null, and false if only one is null.
2. Return the result of invoking the == method on x with the argument y. (That’s right, operators such as `==` are methods that are invoked on their first operand.)

### Type test operators

| Operator | Meaning                                            |
| -------- | -------------------------------------------------- |
| as       | Typecast                                           |
| is       | True if the object has the specified type          |
| is!      | True if the object doesn’t have the specified type |

Use the as operator to cast an object to a particular type if and only if you are sure that the object is of that type. Example:

```dart
(employee as Person).firstName = 'Bob';
```

> If employee is null or not a Person, the first example throws an exception.

If you aren’t sure that the object is of type T, then use is T to check the type before using the object.

```dart
if (employee is Person) {
  // Type check
  employee.firstName = 'Bob';
}
```

### Assignment operators

```dart
// Assign value to a
a = value;
// Assign value to b if b is null; otherwise, b stays the same
b ??= value;
```

### Cascade notation

Cascades (`..`, `?..`) allow you to make a sequence of operations on the same object.

```dart
var paint = Paint()
  ..color = Colors.black
  ..strokeCap = StrokeCap.round
  ..strokeWidth = 5.0;


// The previous example is equivalent to this code
var paint = Paint();
paint.color = Colors.black;
paint.strokeCap = StrokeCap.round;
paint.strokeWidth = 5.0;
```

If the object that the cascade operates on can be null, then use a null-shorting cascade (`?..`) for the first operation.

```dart
var button = querySelector('#confirm') // Get an object.
  ?..text = 'Confirm' // Use its members.
  ..classes.add('important')
  ..onClick.listen((e) => window.alert('Confirmed!'));

// The previous code is equivalent to the following:

var button = querySelector('#confirm');
button?.text = 'Confirm';
button?.classes.add('important');
button?.onClick.listen((e) => window.alert('Confirmed!'));
```
