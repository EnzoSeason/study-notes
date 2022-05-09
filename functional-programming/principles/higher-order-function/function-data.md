# Function and Data

In this article, we will explain **how functions create and encapsulate data**.

## Class

In Scala, we create a data structure using [class](https://docs.scala-lang.org/tour/classes.html).

## Data Abstraction

The ability to **choose different implementations of the data without affecting clients** is data abstraction.

For example, we have 3 ways to implement `numer` and `denom` of the class `Rational`.

```scala
class Rational(var x: Int, var y: Int) {
  private def gcd(a: Int, b: Int): Int = {
    if (b == 0) a
    else gcd(b, a % b)
  }
  // implemention 1: run gcd whenever numer or denom is called.
  def numer = x / gcd(x, y)
  def numer = y / gcd(x, y)
}
```

```scala
class Rational(var x: Int, var y: Int) {
  private def gcd(a: Int, b: Int): Int = {
    if (b == 0) a
    else gcd(b, a % b)
  }
  // implemention 2: run gcd only one time when the instance of the class is created
  private val g = gcd(x, y)
  def numer = x / g
  def denom = y / g
}
```

```scala
class Rational(var x: Int, var y: Int) {
  private def gcd(a: Int, b: Int): Int = {
    if (b == 0) a
    else gcd(b, a % b)
  }
  // implemention 3: run gcd only one time when the instance of the class is created, and get the numer's and demon's value
  private val g = gcd(x, y)
  val numer = x / g
  val denom = y / g
}
```

## Self reference

`this` is the self reference using in a class. It references to the class's attributes and methods.

## Precondition vs Assert

- Precondition enforce the condition on the caller of the function. We use `require()` in Scala.

  ```scala
  class Rational(var x: Int, var y: Int) {
    require(y > 0, "Denominator must be positive.")
  }
  ```

- Assert is used to check the codes.

  ```scala
  val x = sqrt(y)
  assert(x >= 0)
  ```

## Constructor

### Primary constructor

It's in the definition of the class.

```scala
class Rational(var x: Int, var y: Int) {}
```

- It takes all the parameters.
- It runs all the statements in the class body.

### Auxiliary constructors

The other constructors besides the primary one.

It's defined by `this()`.

```scala
class Rational(var x: Int, var y: Int) {
  def this(x: Int) = {
    this(x, 1)
  }
}
```
