# Map, FlatMap, Filter

Scala can create a **list** as followed.

```scala
val list = List(1, 2, 3)
```

## Map

`map` manipulates **each element** in the list.

```scala
val mappedList = list.map((element: Int) => element + 1)
println(mappedList) // List(2, 3, 4)
```

## FlatMap

`flatMap` flattens lists into one list.

```scala
val toPair = (element: Int) => List(element, element + 1)
val flatMappedList = list.flatMap(toPair)
println(flatMappedList) // List(1, 2, 2, 3, 3, 4)
```

Combining `map` and `flatMap` can **replace nested loops**. For example, we want a combination of two lists.

```scala
val chars = List('a', 'b', 'c')
val numbers = List(1, 2, 3)
val combinations = chars.flatMap(c => numbers.map(n => s"$c$n"))
println(combinations) // List(a1, a2, a3, b1, b2, b3, c1, c2, c3)
```

## For Comprehensions

Although `map` and `flatMap` are powerful, they're hard to read. `for-comprehension` improves readability.

```scala
val forCombinations = for {
  c <- chars
  n <- numbers
} yield s"$c$n"

println(forCombinations) // List(a1, a2, a3, b1, b2, b3, c1, c2, c3)
```

We can use `filter` inside `for-comprehension`, too.

```scala
val evenForCombinations = for {
  c <- chars
  n <- numbers if n % 2 == 0
} yield s"$c$n"

println(evenForCombinations) // List(a2, b2, c2)
```

It's equivalent to:

```scala
val evenCombinations = chars.flatMap(c => numbers.filter(n => n % 2 == 0).map(n => s"$c$n"))

println(evenCombinations)
```

## Exercises

Create a collection which contains AT MOST one element.

```scala
abstract class Maybe[+T] {
  def map[B](fn: T => B): Maybe[B]

  def flatMap[B](fn: T => Maybe[B]): Maybe[B]

  def filter(fn: T => Boolean): Maybe[T]
}

case object MaybeNot extends Maybe[Nothing] {
  override def map[B](fn: Nothing => B): Maybe[B] = MaybeNot

  override def flatMap[B](fn: Nothing => Maybe[B]): Maybe[B] = MaybeNot

  override def filter(fn: Nothing => Boolean): Maybe[Nothing] = MaybeNot
}

case class Just[+T](value: T) extends Maybe[T] {
  override def map[B](fn: T => B): Maybe[B] = Just(fn(value))

  override def flatMap[B](fn: T => Maybe[B]): Maybe[B] = fn(value)

  override def filter(fn: T => Boolean): Maybe[T] = {
    if (fn(value)) this
    else MaybeNot
  }
}
```

The test results are as followed.

```scala
val just3 = Just(3)

println(just3) // Just(3)

println(just3.map(_ * 2)) // Just(6)

println(just3.flatMap(el => Just(s"$el is cool"))) // Just(3 is cool)

println(just3.filter(_ % 2 == 0)) // MayBeNothing
```
