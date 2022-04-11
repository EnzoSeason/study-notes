## Data Types

Because every variable in Dart refers to an `object`— _an instance of a class_ —you can usually use constructors to initialize variables.

The Dart language has special support for the following:

- Numbers (`int`, `double`)
- Strings (`String`)
- Booleans (`bool`)
- Lists (`List`)
- Sets (`Set`)
- Maps (`Map`)
- Runes (`Runes`; often replaced by the `characters` API)
- Symbols (`Symbol`)
- The value null (`Null`)

Some other types also have special roles in the Dart language:

- `Object`: The superclass of all Dart classes except Null.
- `Future` and `Stream`: Used in asynchrony support.
- `Iterable`: Used in for-in loops and in synchronous generator functions.
- `Never`: Indicates that an expression can never successfully finish evaluating. Most often used for functions that always throw an exception.
- `dynamic`: Indicates that you want to disable static checking. Usually you should use `Object` or `Object?` instead.
- `void`: Indicates that a value is never used. Often used as a return type.

### Number

Both `int` and `double` are subtypes of `num`.

- `int`:

  - On native platforms, values can be from -2<sup>63</sup> to 2<sup>63</sup> - 1

  - On the web, integer values are represented as JavaScript numbers (64-bit floating-point values with no fractional part) and can be from -2<sup>53</sup> to 2<sup>53</sup> - 1.

- `double`: 64-bit (double-precision) floating-point numbers, as specified by the IEEE 754 standard.

Here’s how you turn a string into a number:

```dart
var one = int.parse('1');
var onePointOne = double.parse('1.1');
```

### String

A Dart string (String object) holds a sequence of UTF-16 code units.

You can put the value of an expression inside a string by using `${expression}`. If the expression is an identifier, you can skip the `{}`.

```dart
var s = 'string interpolation';

assert('Dart has $s');
assert('Dart has ${s.toUpperCase()}');
```

To get the string corresponding to an object, Dart calls the object’s `toString()` method.

You can concatenate strings using adjacent string literals or the + operator:

### Boolean

Dart’s type safety means that you can’t use code like `if (nonbooleanValue)` or `assert (nonbooleanValue)`. Instead, explicitly check for values, like this:

```dart
// Check for an empty string.
var fullName = '';
assert(fullName.isEmpty);

// Check for zero.
var hitPoints = 0;
assert(hitPoints <= 0);

// Check for null.
var unicorn;
assert(unicorn == null);

// Check for NaN.
var iMeantToDoThis = 0 / 0;
assert(iMeantToDoThis.isNaN);
```

### List

In Dart, arrays are `List` objects, so most people just call them lists.

```dart
var list = [1, 2, 3];
```

> Dart infers that list has type `List<int>`. If you try to add non-integer objects to this list, the analyzer or runtime raises an error.

To create a list that’s a compile-time constant, add const before the list literal:

```dart
var constantList = const [1, 2, 3];
// constantList[1] = 1; // This line will cause an error.
```

The `spread operator (...)` and the `null-aware spread operator (...?)` provide a concise way to insert multiple values into a collection.

```dart
var list = [1, 2, 3];
var list2 = [0, ...list];
assert(list2.length == 4);

// If the list may be null, use ...?

var list;
var list2 = [0, ...?list];
assert(list2.length == 1);
```

Dart also offers collection `if` and collection `for`, which you can use to build collections using conditionals (if) and repetition (for).

```dart
// if
var nav = [
  'Home',
  'Furniture',
  'Plants',
  if (promoActive) 'Outlet'
];

// for
var listOfInts = [1, 2, 3];
var listOfStrings = [
  '#0',
  for (var i in listOfInts) '#$i'
];
assert(listOfStrings[1] == '#1');
```

### Set

A set in Dart is an **unordered** collection of **unique** items.

```dart
var halogens = {'fluorine', 'chlorine', 'bromine', 'iodine', 'astatine'};
```

> Dart infers that halogens has the type `Set<String>`. If you try to add the wrong type of value to the set, the analyzer or runtime raises an error.

To create an empty set, use {} preceded by a type argument, or assign {} to a variable of type Set:

```dart
var names = <String>{};
// Set<String> names = {}; // This works, too.
// var names = {}; // Creates a map, not a set.
```

Same as `List`, `Set` works with

- `spread operator (...)` and the `null-aware spread operator (...?)`

- collection `if` and collection `for`

### Map

A map is an object that associates keys and values. Both keys and values can be any type of object. Each key occurs only once, but you can use the same value multiple times.

```dart
// gifts has the type Map<String, String>
var gifts = {
  // Key:    Value
  'first': 'partridge',
  'second': 'turtledoves',
  'fifth': 'golden rings'
};

// nobleGases has the type Map<int, String>
var nobleGases = {
  2: 'helium',
  10: 'neon',
  18: 'argon',
};
```

You can create the same objects using a Map constructor:

```dart
var gifts = Map<String, String>();
gifts['first'] = 'partridge';
gifts['second'] = 'turtledoves';
gifts['fifth'] = 'golden rings';

var nobleGases = Map<int, String>();
nobleGases[2] = 'helium';
nobleGases[10] = 'neon';
nobleGases[18] = 'argon';
```

> If you come from a language like C## or Java, you might expect to see new Map() instead of just Map(). In Dart, the new keyword is optional.

If you look for a key that isn’t in a map, you get a `null` in return.

Use `.length` to get the number of key-value pairs in the map.

Same as `List`, `Map` works with

- `spread operator (...)` and the `null-aware spread operator (...?)`

- collection `if` and collection `for`

### Runes and grapheme clusters

Runes expose the Unicode code points of a string. Dart can hanlder special character, such as emoji.

### Symbols

A Symbol object represents an operator or identifier declared in a Dart program. To get the symbol for an identifier, use a symbol literal, which is just `#` followed by the identifier:

```dart
#radix
#bar
```
