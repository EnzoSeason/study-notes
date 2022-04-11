## Try

A `Try` is a wrapper for **a computation that might fail**.

```scala
sealed abstract class Try[+T]
case class Failure[+T](t: Throwable) extends Try[+T]
case class Success[+T](value: T) extends Try[+T]
```

### Usage

Suppose that we have a method that throws an error.

```scala
def unsafeMethod(): String = throw new RuntimeException("No string")
```

We can use `Try` to catch it.

```scala
val potentialFail = Try(unsafeMethod())
println(potentialFail)
// Failure(java.lang.RuntimeException: No string)
```

There is a sytex sugar.

```scala
val potentialFail = Try {
  unsafeMethod()
}
```

#### Utilities

- `isSuccess` / `isFailure`

  ```scala
  println(potentialFail.isSuccess) // false
  ```

- `orElse`

  ```scala
  val fallbackTry = Try(unsafeMethod())
    .orElse(Try(backupMethod()))
  ```

  Syntax sugar is:

  ```scala
  val fallbackTry = Try {
    unsafeMethod()
  } orElse Try {
    backupMethod()
  }

  println(fallbackTry) // Success(A default string)
  ```

- `map`, `flatMap`, `filter`

#### API Design

If your codes might throw an error, wrap them with `Try`.

```scala
def betterUnsafeMethod(): Try[String] = Try {
  throw new RuntimeException("No string")
}

def betterBackupMethod(): Try[String] = Try {
  "A default string"
}
```

So, we can use it better.

```scala
val betterTry = betterUnsafeMethod() orElse betterBackupMethod()
```
