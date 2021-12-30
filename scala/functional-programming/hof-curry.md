# HOF & Curry

## High Order Function (HOF)

The function that either **takes functions as parameters** or **returns functions as results** is High Order Function (HOF).

For example,

```scala
/** It runs given times of given function.*/
def nTimes(fn: Int => Int, times: Int, value: Int): Int = {
  if (times <= 0) value
  else nTimes(fn, times - 1, fn(value))
}

val plusOne = (x: Int) => x + 1
println(nTimes(plusOne, 10, 1)) // plusOne runs 10 times, so the result is 11.
```

To make HOF more powerful, we should think in Functional Programming. In this case, it's strange that passes `value` to the function. We can return a function instead of `Int`.

```scala
def nTimesBuilder(fn: Int => Int, times: Int): (Int => Int) = {
  if (times <= 0) (value: Int) => value
  else (value: Int) => nTimesBuilder(fn, times - 1)(fn(value))
}

val plusOne = (x: Int) => x + 1
val tenTimes = nTimesBuilder(plusOne, 10)
println(tenTimes(1)) // output: 11
```

## Currying

Currying is the technique of converting a function that **takes multiple arguments into a sequence of functions** that each takes a **single argument**.

```scala
val addBuilder: Int => (Int => Int) = a => b => a + b
println(addBuilder(1)(2)) // output: 3
```

Scala can define a **function** with **multiple parameter lists**. It's also currying.

```scala
def add(a: Int)(b: Int): Int = a + b
println(add(1)(2)) // output: 3
```
