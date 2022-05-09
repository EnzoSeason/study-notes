# Call-by-value vs Call-by-name

There are two ways to calculate **parameters** of the function.

## Call-by-value

The parameters are **calculated before** being passed into the function.

## Call-by-name

The parameters are **not calculated before** being passed into the function.

## Scala example

```scala
// call-by-name
def x = fn()
// fn() is runed once x is called.

// call by value
val y = fn()
// fn() is runed immediately.
```

## Scala settings

In scala, the **call-by-value** is the default setting.

We can also set the **call-by-name**, simply prepend `=>` to parameter's data type.

```scala
def calculate(input: => Int) = input * 37
```
