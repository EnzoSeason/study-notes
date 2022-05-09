# Enum

Here is a hierarchy of classes.

```scala
trait Expr
object Expr {
  case class Var(s: String) extends Expr
  case class Sum(e1: Expr, e2: Expr) extends Expr
  case class Prod(e1: Expr, e2: Expr) extends Expr
}
```

Note that there are **no methods** in these definitions. All we've done is define some **base trait** and **case classes** that extend the base trait and thus defined in particular cases how data of the case trait can be constructed and pattern matched upon.

**Pure data** definitions like these are called **algebraic data types** or **ADTs** for short. ADTs are quite pervasive in functional programming.

**Enum** is the shorter expression for **ADT**.

```scala
enum Expr {
  case Var(s: String)
  case Sum(e1: Expr, e2: Expr)
  case Prod(e1: Expr, e2: Expr)
}
```

## Pattern matching on ADT

Since `enum` contains **case classes**, it can be used in pattern matching.

```scala
def show(e: Expr): String = e match {
  case Expr.Var(x) => x
  case Expr.Sum(e1, e2) => s"${show(e1) + show(e2)}"
  case Expr.Prod(e1, e2) => s"${show(e1) * show(e2)}"
  _ => "Not an expression"
}
```

## More fun with Enum

`Enum` has some predefined functions.

- `value(index)` returns a **case class** indicated by `index`.

- `ordinal` returns the `index` of a **case class** in `enum`.

```scala
enum Direction(val dx: Int, val dy: Int) {
  case Right extends Direction(1, 0)
  case Up extends Direction(0, 1)
  case Left extends Direction(-1, 0)
  case Down extends Direction(0, -1)

  def leftTurn = Direction.value((ordinal + 1) % 4)
}
```

```scala
val r = Direction.Right
val u = r.leftTurn // Up
val v = (u.dx, u.dy) // (0, 1)
```

Actually, we can transform `enum` into normal class.

```scala
class Direction(val dx: Int, val dy: Int) {
  // implement value() and ordinal
  // ...
  def leftTurn = Direction.value((ordinal + 1) % 4)
}
object Direction {
  val Right = new Direction(1, 0)
  val Up = new Direction(0, 1)
  val Left = new Direction(-1, 0)
  val Down = new Direction(0, -1)
}
```

## Domain Modeling

`enum` can combines **simple cases and parameterized cases**.

```scala
enum PayMethod {
  case CreditCard(kind: Card, number: Int, expires: Date)
  case PayPal(email: String)
  case Cash
}

enum Card {
  case Visa, MasterCard, Amex
}
```
