# Recursion

## Overstack

It's a very common problem when we use the recursion.

```scala
def factorial(num: Int): Int = {
  if (num == 1) num
  else num * factorial(num)
}

println(factorial(5))
```

Here is the recursion stack.

```
factorial(5)
5 * factorial(4)
5 * (4 * factorial(3))
5 * (4 * (3 * factorial(2)))
5 * (4 * (3 * (2 * factorial(1))))
5 * (4 * (3 * (2 * 1)))
5 * (4 * (3 * 2))
5 * (4 * 6)
5 * 24
120
```

To optimise that, we use the **tail recursion**.

## Tail recursion

1. The tail recursion is the tail call itself.

2. The tail call is the function ONLY returns the call of another function.

```scala
def factorialOpt(num: Int, accumlator: BigInt): BigInt = {
  if (num == 1) accumlator
  else factorialOpt(num - 1, num * accumlator)
}

println(factorialOpt(5, 1))
```

Here is the recursion stack.

```
factorialOpt(5, 1)
factorialOpt(4, 5)
factorialOpt(3, 20)
factorialOpt(2, 60)
factorialOpt(1, 120)
120
```

See, tail recursion saves half of the memory and the time, which means reduce the both time and space complicity.

Actually, we cache the previous result in the parameter, `accumlator`, so that we optimise the recursion.

To indicate a tail recurion in Scala, we use `@tailrec`

```scala
@tailrec
def factorialOpt(num: Int, accumlator: BigInt): BigInt = {
  if (num == 1) accumlator
  else factorialOpt(num - 1, * num accumlator)
}
```