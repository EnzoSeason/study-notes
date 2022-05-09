# Contextual abstractions

We are trying to implement `sort` function.

```scala
def sort(xs: List[Int]): List[Int] = {
  ...
  if (x < y)
  ...
}
```

And then, we want to make it **general**. But the problem is, how to implement the comparasion `<` ?

The question is using **currying**to pass a `lessThan` function.

```scala
def sort(xs: List[T])(lessThan: (T, T) => Boolean): List[T] = {
  ...
  if lessThan(x, y)
  ...
}
```

## Ordering

In fact, we can use `Ordering` in Scala standard library to do the same thing.

```scala
def sort(xs: List[T])(ord: Ordering[T]): List[T] = {
  ...
  if ord.lt(x, y)
  ...
}
```

To use it, we can do as followed.

```scala
sort(ints)(Ordering.Int)
sort(strings)(Ordering.String)
```

`Ordering.Int` and `Ordering.String` are implemented as followed:

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

## Implicit Parameters

It's cumbersome to write `Ordering.Int` because `Int` always uses it and never uses other orderings.

Therefore, Scala has **implicit parameters**.

```scala
def sort[T](xs: List[T])(implicit ord: Ordering[T]): List[T] = ...
```

So than, we can simply call `sort(ints)`. The compiler will figure out which ordering to use.

```scala
// The compiler will parse the call in following steps
// 1
sort(ints)
// 2
sort[Int](ints)
// 3
sort[Int](ints)(Ordering.Int)
```

## Context Bounds

We use **context bounds** to simplify **implicit parameters**.

```scala
def sort[T: Ordering](xs: List[T]): List[T] = ...
```

It's the same as the previous definition. It tells us the general type has ordering.

## Implicit Query

At any point in a program, one can query an implicit value of a given type by calling the implicitly operation:

```scala
implicitly[Ordering[Int]]
// equal to
implicitly[Ordering[Int]](Ordering.Int)
```

Note that implicitly is not a special keyword, it is defined as a library operation:

```scala
def implicitly[T](implicit value: T): T = value
```

## Conclusion

We've introduced a way to do **type-directed programming**,with the help of a language mechanism that **infers values from types**.

The idea is that there has to be a **unique (or at least most specific) instance** that matches the queried type for it to be used by the compiler.

Instance is searched in the enclosing **lexical scope** (imports, parameters, inherited members, as well as normal definitions), and then if that doesn't give a match in the **companion objects** that are associated with the queried type.
