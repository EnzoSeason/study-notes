# Higher order function

Functional languages treats function as _first-class value_. It means a function can be used as **a parameter and a return**.

The function that **takes functions as parameters** and **returns functions as results** is **higher-order-function**.

## Function type

```scala
def foo(fn: Int => Int) = ???

def bar(fn: (Boolean, Double) => List[String]) = ???
```

## Exercise

```scala
def sum(fn: Int => Int, x: Int, n: Int): Int = {
  def loop(x: Int, acc: Int): Int = {
    if (x > n) acc
    else loop(x + 1, acc + fn(x))
  }
  loop(x, 0)
}

def sumInts(a: Int, b: Int) = sum(x => x, a, b)
def sumSquare(a: Int, b: Int) = sum(x => x * x, a, b)
```