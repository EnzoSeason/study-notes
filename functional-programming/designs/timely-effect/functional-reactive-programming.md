# Functional reactive programming

- Reactive programming:

  Reacting to **sequences of events** that happen in **time**.

- Functional view:

  Aggregating an event sequence into a **signal**.

  Signal is a **value** that changes over **time**.

  Therefore, we can **create a new signal based on existing one** instead of changing a mutable state.

## Basic signal operations

- obtain the value of the signal at the current time.

  ```scala
  mouseMove() // It returns the current position of the mouse.
  ```

- create a signal based on other signals.

  For example, we want to create a signal that indicates if the mouse is in the rectangle defined by `LL` and `UR`.

  ```scala
  def isInRectangle(LL: Position, UR: Position): Signal[Boolean] =
    Signal {
      val pos = mouseMove() // get mouse's current position
      LL <= pos && pos <= UR
    }
  ```

  To use it:

  ```scala
  val s = isInRectangle(L, R)
  s() // the current value
  s() // It may return a different value than the previous one.
  ```

## Constant signal

```scala
val s3 = Signal(3) // It's a signal than always returns 3.
```

## Signal variable

```scala
val x = Signal.Var[Int](0) // It's a signal than always returns 0.

x() = 3 // The signal is updated. Now, it always returns 3.
```
