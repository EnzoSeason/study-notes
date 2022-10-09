# Higher-order List Function

## Mapping

```scala
extension [T](xs: List[T])
  def map[U](f: T => U): List[U] = xs match {
    case Nil => xs
    case head :: tails => f(head) :: tails.map(f)
  }
```

In fact, the actual definition of `map` is more complicated.

To use it:

```scala
def scaleList(xs: List[Double], factor: Double) = {
  xs.map(x => x * factor)
}
```

Now, we can use `map` to simplify some functions.

```scala
def squareListOld(xs: List[Int]): List[Int] = xs match {
  case Nil => Nil
  case y :: ys => y * y :: squareListOld(ys)
}

// new square list
def squareList(xs: List[Int]): List[Int] = {
  xs.map(x => x * x)
}
```

## Filtering

```scala
extension [T](xs: List[T])
  def filter(p: T => Boolean): List[T] = xs match {
    case Nil => xs
    case head :: tails => {
      if (p(head)) head :: tails.filter(p)
      else tails.filter(p)
    }
  }
```

## Reducing

We are going to simplify the following function.

```scala
def sum(xs: List[Int]): Int = xs match {
  case Nil => 0
  case y :: ys => y + sum(ys)
}
```

### reduceLeft

```code
       op
      / \
     .   x1
    .
   /
  op
 / \
xn  xn-1
```

```scala
def sum(xs: List[Int]): Int = {
  (0 :: xs).reduceLeft((x, y) => x + y)
}
```

### reduceRight

```code
   op
  / \
x1   .
       .
        \
         op
        /  \
       xn-1 xn
```

### foldLeft

`foldLeft` is similar to `reduceLeft`. But It takes an **accumulator**.

```code
       op
      / \
     .   xn
    .
   /
  op
 / \
z  x1
```

```scala
def sum(xs: List[Int]): Int = {
  xs.foldLeft(0)((x, y) => x + y)
}
```

Interesting fact: We can use `foldLeft` to reverse a list.

```scala
def reverse[T](xs: List[T]): List[T] = {
  xs.foldLeft(List[T]())((xs, x) => x :: xs)
}
```

### foldRight

```code
   op
  / \
  xn  .
       .
        \
         op
         / \
        x1  z
```

Attention: In some cases, `foldRight` can't be replaced by `foldLeft`.

```scala
def concat[T](xs: List[T], initList: List[T]): List[T] = {
  xs.foldRight(initList)((x, foldedXs) => foldedXs :: x)
}
```

If we use `foldLeft`, the first fold is to put a `List[Int]` and an `Int` in a list, the type won't work out.

#### Exercise for foldRight

```scala
def mapFun[T, U](xs: List[T], f: T => U): List[U] = {
  xs.foldRight(List[U]())((y, ys) => f(y) :: ys)
}
```

```scala
def lengthFun[T](xs: List[T]): Int = {
  xs.foldRight(0)((y, n) => n + 1)
}
```
