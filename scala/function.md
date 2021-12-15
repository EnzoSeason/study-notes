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