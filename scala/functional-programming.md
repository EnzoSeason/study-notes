# Functional Programming

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

## Function Type

`(A, B) => R` is equivalent to `Function2[A, B, R]`.

## Anonymous Function


