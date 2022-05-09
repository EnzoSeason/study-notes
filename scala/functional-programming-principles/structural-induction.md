# Structural Induction

## Referential Transparency

**A function left hand side is equivalent to its right hand side.**

That works because pure functional programs don't have side effects.

## Structural Induction

The principle of structural induction is analogous to **natural induction**.

To prove the property `P(xs)` for all lists `xs`:

- show that `P(Nil)` holds (base case)

- for a list `xs` and an element `x`, show the induction step:

  if `P(xs)` holds, then `P(x :: xs)` holds, too.

### Example

We know that

```scala
Nil + xs = xs // (1)
(x :: xs1) ++ ys = x :: (xs1 + ys) // (2)
```

To prove:

```scala
(xs ++ ys) ++ zs = xs + (ys ++ zs)
```

#### Base case: `Nil`

For the left-hand side,

```scala
(Nil ++ ys) ++ zs
= ys ++ zs // by (1)
```

For the right-hand side,

```scala
Nil ++ (ys ++ zs)
= ys ++ zs // by (1)
```

The left-hand side and the right-hand side are equaled. This case is established.

#### Induction step: `x :: xs`

In this case, we suppose that:

```scala
(xs ++ ys) ++ zs = xs ++ (ys ++ zs) // (3)
```

To prove:

```scala
((x :: xs) ++ ys) ++ zs = (x :: xs) ++ (ys ++ zs)
```

For the left-hand side,

```scala
((x :: xs) ++ ys) ++ zs
= (x :: (xs ++ ys)) ++ zs // by (2)
= x :: ((xs ++ ys) ++ zs) // by (2)
= x :: (xs ++ (ys ++ zs)) // by (3)
```

For the right-hand side,

```scala
(x :: xs) ++ (ys ++ zs)
= x :: (xs ++ (ys ++ zs)) // by (2)
```

The left-hand side and the right-hand side are equaled. This case is established.

#### result

Since **Base case: `Nil`** and **Induction step: `x :: xs`** are established, the prove is done.
