# Function

## Basic function

```scala
def aFunction(a: String, b: Int): String =
  a + " " + b

// or using a code block

def otherFunction(a: String, b: Int): String = {
  a + " " + b
}

// call the function

println(aFunction("Hello", 1))
```

## Recursion function

In functional programming, we **avoid using the iteration** because it causes the side effects. We should use **recursion** instead.

```scala
def aRepeatFunction(word: String, count: Int): String = {
  if (count == 1) word
  else word + aRepeatFunction(word, count - 1)
}
```

## Function with side effects

For now, the function doesn't cause side effects. However, It can. It must return a `Unit` type.

```scala
def aFunctionWithSideEffects(a: Int): Unit = println(a)
```

## Nested function

Scala allows us to define nested function.

```scala
def outerFunction(num: Int): Int = {
  def innerFunction(a: Int, b: Int) = a + b
  innerFunction(num, num - 1)
}
```

## Call-by-value vs Call-by-name

```scala
def calledByValue(x: Long): String = println(x)

def calledByName(x: => Long): String = println(x)
```

The difference between two functions is `=>`.

- **Call-by-value**: The parameter is calculated **before** being passed into the function.

- **Call-by-name**: The parameter is calculated **after** being passed into the function.

**Call-by-name** is used to **delay** the calculation. It's useful in **lazy** actions. That means if the **Call-by-name** parameter isn't used, it won't be calculated.
