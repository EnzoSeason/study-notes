## Function

Dart is a true object-oriented language, so even functions are objects and have a type, `Function`.

This means that functions can be assigned to variables or passed as arguments to other functions.

You can also call an instance of a Dart class as if it were a function.

```dart
bool isNoble(int atomicNumber) {
  return _nobleGases[atomicNumber] != null;
}
```

For functions that contain just one expression, you can use a shorthand syntax:

```dart
bool isNoble(int atomicNumber) => _nobleGases[atomicNumber] != null;
```

The `=>` expr syntax is a shorthand for `{ return expr; }`.

### Parameters

#### Named parameters

When defining a function, use `{param1, param2, …}` to specify named parameters:

```dart
void enableFlags({bool? bold, bool? hidden}) {...}
```

When calling a function, you can specify named parameters using `paramName: value`. For example:

```dart
enableFlags(bold: true, hidden: false);
```

Although named parameters are a kind of optional parameter, you can annotate them with **required** to indicate that the parameter is mandatory — that users must provide a value for the parameter. For example:

```dart
const Scrollbar({Key? key, required Widget child})
```

#### Optional positional parameters

Wrapping a set of function parameters in `[]` marks them as optional positional parameters:

```dart
String say(String from, String msg, [String? device]) {
  var result = '$from says $msg';
  if (device != null) {
    result = '$result with a $device';
  }
  return result;
}
```

#### Default parameter values

Your function can use `=` to define default values for both named and positional parameters.

The default values must be **compile-time constants**. If no default value is provided, the default value is `null`.

```dart
// Sets the [bold] and [hidden] flags ...
void enableFlags({bool bold = false, bool hidden = false}) {...}

// You can also pass lists or maps as default values.
void doStuff(
    {List<int> list = const [1, 2, 3],
    Map<String, String> gifts = const {
      'first': 'paper',
      'second': 'cotton',
      'third': 'leather'
    }}) {
  print('list:  $list');
  print('gifts: $gifts');
}
```

### Functions as first-class objects

You can pass a function as a parameter to another function. For example:

```dart
void printElement(int element) {
  print(element);
}

var list = [1, 2, 3];

// Pass printElement as a parameter.
list.forEach(printElement);
```

You can also assign a function to a variable, such as:

```dart
var loudify = (msg) => '!!! ${msg.toUpperCase()} !!!';
assert(loudify('hello') == '!!! HELLO !!!');
```

### Anonymous functions

```dart
() { ... }

// or

() => ...
```

#### Lexical scope

Dart is a **lexically scoped language**, which means that the scope of variables is determined statically, simply by the layout of the code.

#### Lexical closures

A closure is a function object that has access to variables in its lexical scope, even when the function is used outside of its original scope.

```dart
/// Returns a function that adds [addBy] to the
/// function's argument.
Function makeAdder(int addBy) {
  return (int i) => addBy + i;
}

void main() {
  // Create a function that adds 2.
  var add2 = makeAdder(2);

  // Create a function that adds 4.
  var add4 = makeAdder(4);

  assert(add2(3) == 5);
  assert(add4(3) == 7);
}
```

#### Return values

All functions return a value. If no return value is specified, the statement `return null;` is implicitly appended to the function body.
