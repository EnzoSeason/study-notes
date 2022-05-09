# Variance

Say `C[T]` is a parameterized type, and `A` and `B` are the types that `A <: B`. There are 3 possible relateships of `C[A]` and `C[B]`.

- `C[A] <: C[B]`: `C` is **covariant**.
- `C[A] >: C[B]`: `C` is **contravariant**.
- No relationship: `C` is **nonvariant**.

In Scala, we can declare these relationships by:

- `class C[+A]`: `C` is **covariant**.
- `class C[-A]`: `C` is **contravariant**.
- `class C[A]`: `C` is **nonvariant**.

## Typing rules for Function

If `A2 <: A1` and `B1 <: B2`, then

```scala
A1 => B1 <: A2 => B2
```

For example,

```scala
trait Fruit
class Apple extends Fruit
class Orange extends Fruit

type FtoO = Fruit => Orange
type AtoF = Apple => Fruit
```

We can find out that `FtoO <: AtoF`.

So the functions are **contravariant in parameters**, and **covariant in returns**.

```scala
trait Function1[-T, +U] {
  def apply(x: T): U
}
```

For example, the following function won't pass the type check because the parameters are covariant.

```scala
trait List[+T] {
  def prepend(elem: T): List[T] = ::(elem, this)
}

apples.prepend(Orange) // It's not reasonable to add an orange to apples.
```

To fix it, we need another type so that `T` is lower bound.

```scala
trait List[+T] {
  def prepend[U >: T](elem: U): List[U] = ::(elem, this)
}

apples.prepend(Orange) // Apples list becomes fruit list.
```

The need for a **lower bound** was essentially to decouple the parameter of the class and the parameter of the newly created object.

Using an **extension** method sidesteps the problem and leads to the same result.

```scala
extension [T](x: T) {
  def :: (xs: List[T]): List[T] = ::(x, xs)
}
```

The compiler will also instantiate **the type T to be a supertype** of the type of the element that we prepend and the type of the tail that we pass here.
