# Evaluations & Operators

## Class and Substitutions

Now suppose that we have a class definition,

```scala
class C(x1, ..., xn) {
  // ...
  def f(y1, ..., yn) = b
  // ...
}
```

Question: How is the following expression evaluated?

```scala
C(v1, ..., vn).f(w1, ..., wn)
```

Answers:

```scala
Rational(1, 2).numer // 1
```

```scala
Rational(1, 2).less(Rational(2, 3))
// Rational(1, 2).numer * Rational(2, 3).denom < Rational(2, 3).numer * Rational(1, 2).denom
// 1 * 3 < 2 * 2
// true
```

## Extension

**Methods** that do NOT need to access the interals of the class can be defined as **extension methods**.

```scala
extension(r: Rational)
  def min(s: Rational): Rational = {
    if (s.less(r)) s
    else r
  }
  def abs: Rational = Rational(r.numer.abs, r.denom)
```

## Operators

How to implement the operators, such as `+`, `*`, etc, for the class?

```scala
extension(r: Rational)
  def + (s: Rational): Rational = r.add(s)
  def * (s: Rational): Rational = r.mul(s)
```

Now, we can call them:

```scala
val r = Rational(1, 2)
val s = Rational(2, 3)

r.+(s)
r.*(s)
```

An operator method with a **single parameter** can be used as an infix operator.

```scala
r + s // equals to r.+(s)
r * s // equals to r.*(s)
```

If it's an **alphanumeric** method with a single parameter, we need to add `infix` keyword.

```scala
extension(r: Rational)
  infix def min(s: Rational): Rational = {
    if (s.less(r)) s
    else r
  }

r min s // equals to r.min(s)
```
