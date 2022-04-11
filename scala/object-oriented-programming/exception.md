## Exception

### Throwing an exception

Throwable classes extend the Throwable class.

**Exception** and **Error** are the subtype of **Throwable**.

```scala
throw new NullPointerException
```

### Catching an exception

```scala
val potentialFail = try {
  // your codes
} catch {
  case e: RuntimeException => println("Runtime Exception")
  case _: Throwable => println("Got some other kind of Throwable exception")
} finally {
  // The codes will be executed.
}
```

- `finally` is optional. It doesn't effect the return. It's used for **side effects**, such as logging.

### Defining your own exception

```scala
class MyException extends Exception
```
