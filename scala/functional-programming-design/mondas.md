# Monads

A monad `M` is a parametric type `M[T]` with 2 operations:

- `flatMap`
- `unit`

that have to satisfy some laws.

```scala
extension [T, U](m: M[T])
  def flatMap(f: T => M[U]): M[U]

def unit[T](x: T): M[U]
```

## Examples of Monads

- List: `unit(x) = List(x)`
- Set: `unit(x) = Set(x)`
- Option: `unit(x) = Some(x)`

## Monad Laws

- Associativity

  ```scala
  m.flatMap(f).flatMap(g) == m.flatMap(f(_).flatMap(g))
  ```

- Left unit

  ```scala
  unit(x).flatMap(f) == f(x)
  ```

- Right unit

  ```scala
  m.flatMap(unit) == m
  ```

## Significance of the laws for `For-comprehension`

1. Associativity says that one can "inline" nested.

   ```scala
   for
     y <- for x <- m; y <- f(x) yield y
     z <- g(y)
   yield z

   // equivalent to

   for x <- m; y <- f(x); z <- g(y)
   yield z
   ```

2. Right unit says

   ```scala
   for x <- m yield x

   // equivalent to

   m
   ```
