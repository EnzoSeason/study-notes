# Type class

In the [previous lesson](./contextual-abstractions.md), we have met **type class**.

```scala
trait Ordering[T] {
  def compare(a1: T, a2: T): Int
}

object Ordering {
  implicit val Int: Ordering[Int] =
    new Ordering[Int] {
      def compare(x: Int, y: Int) =
        if (x < y) -1 else if (x > y) 1 else 0
    }
  implicit val String: Ordering[String] =
    new Ordering[String] {
      def compare(s: String, t: String) = s.compareTo(t)
  }
}
```

`Ordering` is a type class. It has 2 parts:

- a `trait`
- an `Object` with `implicit` values.

## Retroactive extension

Type classes support retroactive extension.

It means we can **extend a data type** with new operations **without changing the original definition** of the data type.

For example, we have a class.

```scala
case class Rational(num: Int, denom: Int)
```

We want to compare rationals. We don't have to change this class. We define an implicit instance of type `Ordering[Rational]`:

```scala
object RationalOrdering {
  implicit val orderingRational: Ordering[Rational] =
    new Ordering[Rational] {
      def compare(q: Rational, r: Rational): Int =
        q.num * r.denom - r.num * q.denom
    }
}
```

## Conditional implicit definitions

For now, we can create **implicit value (`val`)** and pass **implicit parameters**. Can we create a **implicit function**? The answer is yes.

For example, we try to order a list.

```scala
implicit def orderingList[A](implicit ord: Ordering[A]): Ordering[List[A]] =
  new Ordering[List[A]] {
    def compare(xs: List[A], ys: List[A]) =
      (xs, ys) match {
        case (x :: xsTail, y :: ysTail) =>
          val c = ord.compare(x, y)
          if (c != 0) c else compare(xsTail, ysTail)
        case (Nil, Nil) => 0
        case (_, Nil)   => 1
        case (Nil, _)   => -1
      }
  }
```

```scala
val xss = List(List(1, 2, 3), List(1), List(1, 1, 3))
sort(xss)
// List(List(1), List(1, 1, 3), List(1, 2, 3))
```

```scala
// The compiler will parse the call in following steps
// For the record, the sort is defined as followed.
def sort[T](xs: List[T])(implicit ord: Ordering[T]): List[T] = ???

// 1
sort(xss)
// 2
sort[List[Int]](xss)
// 3
sort[List[Int]](xss)(orderingList(Ordering.Int))
```
