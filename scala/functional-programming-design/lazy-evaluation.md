# Lazy Evaluation

In the [previous session](./lazy-list.md), the tail of Lazy list will be re-calculated each time it is called.

This problem can be avoided if we **store the result of the first evaluation of tail** and **reuse the stored result**.

This optimization is sound since the tail expression will **produce the same result each time it is evaluated**.

This evaluation is called **lazy evaluation**. By far, we have 3 evaluations.

- **strict evaluation**

  It's for normal parameters and `val` definition (a.k.a. by-value).

- **by-name evaluation**

  Everything is recomputed.

- **lazy evaluation**

## Lazy Evaluation in Scala

```scala
lazy val x = expr
```

For example,

```scala
def expr = {
  val x = { println("x"); 1}
  lazy val y = { println("y"); 1}
  def z = { println("z"); 1}
  z + y + x + z + y + x
}

lazy val res = expr
// The console will print. (explain where the print is triggered.)
// x (val x = { println("x"); 1})
// z (def z = { println("z"); 1})
// y (+ y)
// z (+ z)
```

## RealWorld LazyList

In the previous session, the lazy list has only a lazy tail. However, in the real world, the lazy list has a lazy head, tail and empty.

```scala
class LazyList[+T](init :=> State[T]) {
  lazy val state: State[T] = init
}

enum State[T]{
  case Empty
  case Cons(hd: T, tl: LazyList[T])
}
```
