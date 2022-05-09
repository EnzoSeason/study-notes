# Subtyping

## Type bounds

- `S <: T`: `S` is the **subtype** of `T`
- `S >: T`: `S` is the **supertype** of `T`

```scala
def show1[S <: IntSet](set: S) = ???
def show2[S >: NonEmpty <: IntSet](set: S) = ???
```

## Covariance

We know that `NonEmpty <: IntSet`, whether `List[NonEmpty] <: List[IntSet]` ? The answer is yes. This relateship is **covariance**.

`List` can be covariant, but all the class can have it? The answer is **no**. For example, `Array` can't.

```java
// java
NonEmpty[] a = new NonEmpty[]{new NonEmpty(1, new Empty())};
IntSet[] b = a; // Pass, a and b point to the same value.
b[0] = new Empty(); // Error
```

Because `NonEmpty <: IntSet`, we can create `b`. Since `IntSet` has can be empty, we assign an empty to it. However, `NonEmpty` can't be empty. So, we get an error.

Now, we know `Array` can't be covariant.

```scala
val a: Array[NonEmpty] = Array(NonEmpty(1, Empty()))
val b: Array[IntSet] = b // Error, Array can't have covariance.
```

Roughly speaking, a type that **accepts mutations** of its element should NOT be covariant.

### Liskov Substitution Principle

If `A <: B`, then everything that can be done with a value of type `B` should be done with a value of type `A`.
