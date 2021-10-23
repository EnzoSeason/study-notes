# Class

Dart is an object-oriented language with classes and mixin-based inheritance. Every object is an instance of a class, and all classes except `Null` descend from Object.

Extension methods are a way to add functionality to a class without changing the class or creating a subclass.

Mixin-based inheritance means that although every class (except for the top class, Object?) has exactly one superclass, a class body can be reused in multiple class hierarchies.

## Using class members

- Use a dot (`.`) to refer to an instance variable or method
- Use `?.` instead of `.` to avoid an exception when the leftmost operand is null

```dart
var p = Point(2, 2);

// Get the value of y.
assert(p.y == 2);

// Invoke distanceTo() on p.
double distance = p.distanceTo(Point(4, 4));

// If p is non-null, set a variable equal to its y value.
var a = p?.y;
```

## Using constructors

1. You can create an object using a constructor. Constructor names can be either `ClassName` or `ClassName.identifier`.

2. The keyword `new` is optional.

3. Some classes provide **constant constructors**. To create a compile-time constant using a constant constructor, put the const keyword before the constructor name.

   ```dart
   var a = const ImmutablePoint(1, 1);
   var b = const ImmutablePoint(1, 1);

   assert(identical(a, b)); // They are the same instance!
   ```

   If a constant constructor is outside of a constant context and is invoked without const, it creates a **non-constant** object.

   ```dart
   var a = const ImmutablePoint(1, 1); // Creates a constant
   var b = ImmutablePoint(1, 1); // Does NOT create a constant

   assert(!identical(a, b)); // NOT the same instance!
   ```

## Instance variables

All uninitialized instance variables have the value `null`.

All instance variables generate an implicit getter method. _Non-final_ instance variables and `late final`· instance variables without initializers also generate an implicit setter method.

```dart
class Point {
  double? x; // Declare instance variable x, initially null.
  double? y; // Declare y, initially null.
}

void main() {
  var point = Point();
  point.x = 4; // Use the setter method for x.
  assert(point.x == 4); // Use the getter method for x.
  assert(point.y == null); // Values default to null.
}
```

Instance variables can be `final`, in which case they must be set exactly once.

```dart
class ProfileMark {
  final String name;
  final DateTime start = DateTime.now();

  ProfileMark(this.name);
}
```

## Constructors

```dart
class Point {
  double x = 0;
  double y = 0;

  // Syntactic sugar for setting x and y
  // before the constructor body runs.
  Point(this.x, this.y);

  // which is equal to
  /*
  Point(double x, double y) {
    this.x = x;
    this.y = y;
  }
  */
}
```

### Default constructors

If you don’t declare a constructor, a default constructor is provided for you. The default constructor has **no arguments** and invokes the **no-argument constructor** in the superclass.

### Constructors aren’t inherited

Subclasses don’t inherit constructors from their superclass.

### Named constructors

Use a named constructor to **implement multiple constructors** for a class or to provide extra clarity:

```dart
const double xOrigin = 0;
const double yOrigin = 0;

class Point {
  double x = 0;
  double y = 0;

  Point(this.x, this.y);

  // Named constructor
  Point.origin()
      : x = xOrigin,
        y = yOrigin;
}
```

### Invoking a non-default superclass constructor

The order of execution is as follows:

1. initializer list
2. superclass’s no-arg constructor
3. main class’s no-arg constructor

If the superclass doesn’t have an unnamed, no-argument constructor, then you must manually call one of the constructors in the superclass. Specify the superclass constructor after a colon (`:`), just before the constructor body (if any).

```dart
class Person {
  String? firstName;

  Person.fromJson(Map data) {
    print('in Person');
  }
}

class Employee extends Person {
  // Person does not have a default constructor;
  // you must call super.fromJson(data).
  Employee.fromJson(Map data) : super.fromJson(data) {
    print('in Employee');
  }
}

void main() {
  var employee = Employee.fromJson({});
  print(employee);
  // Prints:
  // in Person
  // in Employee
  // Instance of 'Employee'
}
```

### Initializer list

Besides invoking a superclass constructor (`super`), you can also initialize instance variables before the constructor body runs. Separate initializers with commas.

```dart
// Initializer list sets instance variables before
// the constructor body runs.
Point.fromJson(Map<String, double> json)
    : x = json['x']!,
      y = json['y']! {
  print('In Point.fromJson(): ($x, $y)');
}
```

### Redirecting constructors

Sometimes a constructor’s only purpose is to redirect to another constructor in the same class. A redirecting constructor’s body is empty, with the constructor call (using this instead of the class name) appearing after a colon (`:`).

```dart
class Point {
  double x, y;

  // The main constructor for this class.
  Point(this.x, this.y);

  // Delegates to the main constructor.
  Point.alongXAxis(double x) : this(x, 0);
}
```

### Constant constructors

If your class produces objects that **never change**, you can make these objects compile-time constants.

To do this, define a **const constructor** and make sure that **all instance variables are final**.

```dart
class ImmutablePoint {
  static const ImmutablePoint origin = ImmutablePoint(0, 0);

  final double x, y;

  const ImmutablePoint(this.x, this.y);
}
```

### Factory constructors

Use the `factory` keyword when implementing a constructor that **doesn’t always create a new instance** of its class.

For example, a factory constructor might return an instance from a cache, or it might return an instance of a subtype.

Another use case for factory constructors is initializing a final variable using logic that can’t be handled in the initializer list.

In the following example, the `Logger` factory constructor returns objects from a cache, and the `Logger.fromJson` factory constructor initializes a final variable from a JSON object.

```dart
class Logger {
  final String name;
  bool mute = false;

  // _cache is library-private, thanks to
  // the _ in front of its name.
  static final Map<String, Logger> _cache =
      <String, Logger>{};

  factory Logger(String name) {
    return _cache.putIfAbsent(
        name, () => Logger._internal(name));
  }

  factory Logger.fromJson(Map<String, Object> json) {
    return Logger(json['name'].toString());
  }

  Logger._internal(this.name);

  void log(String msg) {
    if (!mute) print(msg);
  }
}
```
