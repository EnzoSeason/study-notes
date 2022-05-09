# Tuples and Generic Methods

## Tuple

```scala
val pair = ("apple", 42)
val (fruit, price) = pair
```

Tuple can be used in pattern match. For example, we implement **merge sort**.

```scala
def merge(xs: List[Int], ys: List[Int]): List[Int] = {
  (xs, ys) match {
    case (Nil, ys) => ys
    case (xs, Nil) => xs
    case (x :: xrs, y :: yrs) => {
      if (x < y) x :: merge(xrs, ys)
      else y :: merge(xs, yrs)
    }
  }
}

def msort(xs: List[Int]): List[Int] = xs match {
  case Nil => Nil
  case x :: Nil => xs
  case _ => {
    val (l1, l2) = xs.splitAt(xs.length / 2)
    merge(msort(l1), msort(l2))
  }
}
```

## Generic Method

If we want to **merge sort** the elements other than `Int`, we need to create a generic method.

```scala
def merge(xs: List[T], ys: List[T])(lt: (T, T) => Boolean): List[T] = {
  (xs, ys) match {
    case (Nil, ys) => ys
    case (xs, Nil) => xs
    case (x :: xrs, y :: yrs) => {
      if (lt(x, y)) x :: merge(xrs, ys)
      else y :: merge(xs, yrs)
    }
  }
}

def msort(xs: List[T])(lt: (T, T) => Boolean): List[T] = xs match {
  case Nil => Nil
  case x :: Nil => xs
  case _ => {
    val (l1, l2) = xs.splitAt(xs.length / 2)
    merge(msort(l1)(lt), msort(l2)(lt))
  }
}
```

```scala
// merge sort numbers
val nums = 1 :: 4 :: 5 :: 3 :: Nil
msort(nums)((x: Int, y: Int) => x < y)
// shorter version is okay
msort(nums)((x, y) => x < y)

// merge sort strings
val fruits = List("apple", "orange", "banana")
msort(fruits)((x: String, y: String) => x.compareTo(y) < 0)
```
