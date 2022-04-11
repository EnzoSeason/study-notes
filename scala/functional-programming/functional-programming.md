## Functional Programming

**All scala functions are objects**. They just have the method `apply` so that we can call them as calling a function.

To be specific, Scala provides 22 function traits to make it happen.

```scala
trait Function1[-A, +B] {
  def apply(element: A): B
}
```

> Function1 indicates it takes one parameter. Function2 takes 2, etc.

So, we can create a function (an instance of a class which inherits `Function1`, `Function2`, etc) as followed.

```scala
val stringToInt: Function[Any, Nothing] = new Function1[String, Int] {
  override def apply(str: String): Int = str.toInt
}

val res = stringToInt("3") + 4 // output: 7
```

> Here, we use [Anonymous class](./inheritance.md#Anonymous-class) to create an instance.

### Function Type

`(A, B) => R` is equivalent to `Function2[A, B, R]`.

### Anonymous Function

We can transform `stringToInt` function into an **anonymous function** or **lambda function**.

```scala
val res = (str: String) => str.toInt
```

We can define **Function Type** of the value.

```scala
val res: String => Int = str => str.toInt
```

- Multiple parameters

  ```scala
  val adder = (a: Int, b: Int) => a + b
  // to explicitize function type
  val adder: (Int, Int) => Int = (a, b) => a + b

  // run
  println(adder(1, 2)) // output: 3
  ```

- No parameters

  ```scala
  val returnTwo = () => 2
  // to explicitize function type
  val returnTwo: () => Int = () => 2

  // run
  println(returnTwo()) // output: 2
  ```

  > Attention: We need `()` to call an anonymous function.

#### Useful Syntactic Sugar

- One parameter

  ```scala
  val counter: Int => Int = x => x + 1
  // nicer
  val niceCounter: Int => Int = _ + 1
  ```

- Multiple parameters

  ```scala
  val adder: (Int, Int) => Int = (a, b) => a + b
  // nicer
  val niceAdder: (Int, Int) => Int = _ + _
  ```

In order to use these syntactic sugar, **Function Type** MUST be **explicit**.
