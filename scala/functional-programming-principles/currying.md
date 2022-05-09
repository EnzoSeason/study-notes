# Currying

In the previous lecture, [higher order function](higher-order-function.md), we have created a `sum` function.

```scala
def sum(fn: Int => Int, x: Int, n: Int): Int = {
  def loop(x: Int, acc: Int): Int = {
    if (x > n) acc
    else loop(x + 1, acc + fn(x))
  }
  loop(x, 0)
}
```

```scala
def sumInts(a: Int, b: Int) = sum(x => x, a, b)
def sumSquare(a: Int, b: Int) = sum(x => x * x, a, b)
```

We notice that `a` and `b` is passed unchanged to each function. The question is, can we avoid this replication?

## Currying

```scala
def sum(fn: Int => Int): (Int, Int) => Int = {
  def sumF(x: Int, n: Int): Int = {
    if (x > n) 0
    else fn(x) + sumF(x + 1, n)
  }
  sumF
}
```

```scala
def sumInts = sum(x => x)
sumInts(1, 10)

def sumSquare = sum(x => x * x)
sumSquare(1, 10)
```

Currying is very common in Functional Programming. Scala has a syntax sugar for it.

```scala
def sum(fn: Int => Int)(x: Int, n: Int) = {
  if (x > n) 0
  else fn(x) + sum(fn)(x + 1, n)
}
```

### Function Type

Question: What's the type of `sum`.

It's `(Int => Int) => (Int, Int) => Int`.

Notice that Function Type assoicates to the **right**.

`Int => Int => Int` equals to `Int => (Int => Int)`

### Exercise

Let's generalise `sum` function to `mapReduce`.

```scala
def mapReduce(mapper: Int => Int, reducer: (Int, Int) => Int, initValue: Int)(x: Int, n: Int) = {
  def recur(x: Int): Int = {
    if (x > n) initValue
    else reducer(mapper(x), recur(x + 1))
  }
  recur(x)
}
```

Now, the `sum` is:

```scala
def sum(fn: Int => Int) = mapReduce(fn, (x, y) => x + y, 0)

// Other functions that we can create
def product(fn: Int => Int) = mapReduce(fn, (x, y) => x * y, 0)
```
