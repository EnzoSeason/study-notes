# Collections

## Vector

If the length of a vector is smaller or equal than **32**, it's an **array**. If not, it's an **array of arrays**, and each sub-array has the length of 32.

Once a sub-array is changed (created a new one to replace the old one), all its parents need to be changed, too.

### Operations on Vector

```scala
val nums = Vector(1, 2, -3)
val people = Vector("Bob", "Peter")
```

Vector doesn't support `::` operator. Instead, it supports:

- `x +: xs`: add the element `x` at the **front** of `xs`
- `xs :+ x`: add the element `x` at the **end** of `xs`

## Hierarchy

```code
        Iterable
      /    |   |
     Seq  Set Map
    /   \
 List   Vector
```

## Array and String

`Array` and `String` are classes in Java, they are not the subclass of `Seq`. But they support the same operators as `Seq`.

```scala
val xs: Array[Int] = Array(1, 2, 3)
xs.map(x => x * 2)

val ys: String = "Hello"
ys.filter(_.isUpper)
```

## Ranges

It's a subclass of `Seq`.

```scala
val r: Range = 1 until 3 // 1, 2
val s: Range = 1 to 3 // 1, 2, 3

1 until 10 by 2
6 to 1 by -1
```

## More operations

- zip

  ```scala
  val a = List(1, 2, 3)
  val b = List("a", "b")

  a.zip(b) // List((1, "a"), (2, "b"))
  ```

- flatMap

  It takes a function `f` that **returns itself a collection**, and apply `f` to each element, and then **concatenate** all the results.

  ```scala
  val a = List(1, 2, 3)
  val toPair = (element: Int) => List(element, element + 1)

  a.flatMap(toPair) // List(1, 2, 2, 3, 3, 4)
  ```

We can combine the operations.

```scala
val chars = List('a', 'b', 'c')
val numbers = List(1, 2, 3)

val combinations = chars.flatMap(c => numbers.map(n => s"$c$n"))
// List(a1, a2, a3, b1, b2, b3, c1, c2, c3))
```

### 3 ways to implement Scalar Product

```scala
def scalarProduct(xs: Vector[Int], ys: Vector[Int]): Int = {
  xs.zip(ys).map(xy => xy._1 * xy._2).sum
}
```

The element in the list returned by `zip` is a `tuple`. Therefore, we have other way.

```scala
def scalarProduct(xs: Vector[Int], ys: Vector[Int]): Int = {
  xs.zip(ys).map((x, y) => x * y).sum
}
```

Note that there's some automatic decomposition going on here. `xs.zip(ys)` gives a list of pairs.

Map takes a pair, but here the lambda with parts to the map is a function of two parameters.

Behind the scenes, the compiler will automatically decompose the pair and put the first half in `x` and the second half in `y`.

To be more elegant, we can use `_`.

```scala
def scalarProduct(xs: Vector[Int], ys: Vector[Int]): Int = {
  xs.zip(ys).map(_ * _).sum
}
```
