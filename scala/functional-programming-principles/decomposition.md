# Decomposition

If we want to add a new method in **a base class**, we need to add it in **all sub-classes**. It's very anonying. There are some ways to solve it.

## Type test & Type cast (discouraged)

We can create a method depended on **types**. Different types have different actions.

```scala
def isInstanceOf[T]: Boolean
def asInstanceOf[T]: T
```

Scala discoruage it because it's ugly and potentially **unsafe**. Type cast can be not always protected by Type test.

## Object-Oriented Decomposition

It means different sub-classes have different implementations for a method.

```scala
trait Expr {
  def eval: Int
}

class Number(val n: Int) extends Expr {
  def eval = n
}

class Sum(val e1: Expr, val e2: Expr) extends Expr {
  def eval = e1.eval + e2.eval
}
```

> `val n` means `n` is public and immutable. If we remove `val`, then `n` is private.

It's easy for adding a new data structure, like adding a class `Prod`.

However,it's hard to add a new method. For example, we want a `print` method for all the `Expr`.

## Functional Decomposition - Pattern Matching

First, we need to define the **case classes**. Case class is the normal class with more functionalities.

```scala
case class Number(n: Int) extends Expr
case class Sum(e1: Expr, e2: Expr) extends Expr
```

> In `Number`, `n` equals to `val n`. It's public and immutable.

Then, pattern matching.

```scala
def eval(e: Expr): Int = e match {
  case Number(n) => n
  case Sum(e1, e2) => eval(e1) + eval(e2)
}
```

Patterns are constructed from:

- Constructors, e.g. `Number`, `Sum`
- Variables
- Wildcard, `_`
- Constants
- Type Tests, e.g. `n: Number` for testing whether the input is a `Number`.

### What do patterns match?

- Constructors `C(p1, ..., pn)`:

  It matches all the values of the type `C` (or a subtype) that are constructed with the arguements `p1, ..., pn`

- Variable `x`:

  It matches **any value**, and **binds** the name of the variable with the value.

- Constant `c`:

  It equals to `== c`.

## Exercise

```scala
trait Expr
case class Var(name: String) extends Expr
case class Sum(e1: Expr, e2: Expr) extends Expr
case class Prod(e1: Expr, e2: Expr) extends Expr
```

```scala
def printExpr(e: Expr) = e match {
  case Var(x) => x
  case Sum(e1, e2) => s"${printExpr(e1) + printExpr(e2)}"
  case Prod(e1, e2) => s"${printHelper(e1) * printHelper(e2)}"
}

def printHelper(e: Expr) = e match {
  case expr: Sum => s"(${printExpr(expr)})" // add parentheses
  case _ => printExpr(e)
}
```

```scala
val expr = Prod(Sum(Var("a"), Var("b")), Var("c"))
printExpr(expr) // (a + b) * c
```
