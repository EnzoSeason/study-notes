# Functional Random Generators

In this article, we study the generator.

```scala
trait Generator[+T]:
  def generate(): T
```

We create an `integer` generator as followed:

```scala
val integers = new Generator[Int]:
  val rand = java.util.Random()
  def generate() = rand.nextInt()
```

## Creating generators

The question is, can we create other generators based on `integers`? The answer is yes.

```scala
val booleans = new Generator[Boolean]:
  def generate() = intergers.generate() > 0

val pairs = new Generator[(Int, Int)]:
  def generate() = (intergers.generate(), intergers.generate())
```

## Creating generators with For-comprehension

The next question is, can we use **for-comprehension** to replace `new` syntax?

The answer is yes. As we known, **for-comprehension** can be used by any class which implements `map`, `flatMap` and `withFilter` methods. Let's add extensions to `Generator`.

```scala
trait Generator[+T]:
  def generate(): T

extension [T, U](g: Generator[T])
  def map(f: T => U) = new Generator[U]:
    def generate() = f(g.generate())

  def flatMap(f: T => Generator[U]) = new Generator[U]:
    def generate() = f(g.generate()).generate()
```

Now, the generators can be written in a more elegent way.

```scala
val booleans: Generator[Boolean] =
  for x <- integers yield x > 0

def pairs: Generator[(Int, Int)] =
  for
    x <- integers
    y <- integers
  yield (x, y)
```

## List generator

```scala
def lists: Generator[List[Int]] =
  for
    isEmpty <- booleans
    list <-
      if isEmpty then emptyList
      else nonEmptyList
  yield list

def emptyList = single(Nil)

def nonEmptyList: Generator[List[Int]] =
  for
    head <- integers
    tail <- lists
  yield head :: tail
```

By the way:

```scala
def single[T](x: T) = new Generator[T]:
  def generate() = x
```

## Tree generator

```scala
enum Tree:
  case Node(left: Tree, right: Tree)
  case Leaf(x: Int)
```

```scala
def trees: Generator[Tree] =
  for
    isLeaf <- booleans
    tree <- if isLeaf then leaves else nodes
  yield tree

def leaves: Generator[Tree.Leaf] =
  for
    x <- integers
  yield Tree.Leaf(x)

def nodes: Generator[Tree.Node] =
  for
    left <- nodes
    right <- nodes
  yield Tree.Node(left, right)
```

## Random Testing Function

```scala
def test[T](g: Generator[T], runTimes: Int = 100)
           (test: T => Boolean): Unit =
  for i <- 0 until runTimes do
    val sample = g.generate()
    assert(test(sample), s"failed for $sample")
  println(s"passed for $runTime tests")
```

Use it

```scala
test(lists) {
  l => l.length >= 0
}
```
