# Exception

We can define the exception class.

```scala
class BadInput(msg: String) extends Exception(msg)
```

to use it,

```scala
throw BadInput("missing data")
```

We use `try catch` to handle exceptions.

```scala
def validatedInput(): String =
  try getInput()
  catch
    case BadInput(msg) =>
      println(msg)
      validatedInput()
    case ex: Exception =>
      println("fatal error")
      throw ex
```

## Shortcoming of try/catch

- They don't show up in the **types** of functions that throw them.

- They don't work in **parallel computations** where we want to communicate an exception from one thread to another.

## `Try` Type

To overcome the shortage of try/catch, we come up with `Try`.

It resembles to `Option`

```scala
abstract class Try[+T]
case class Success[+T](x: T) extends Try[T]
case class Failure(ex: Exception) extends Try[Nothing]
```
