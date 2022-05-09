# Scala syntax summary

## Type

- Type = SimplyType | FunctionType

- FunctionType = SimplyType `=>` Type | (`[Types]`) `=>` Type

## Expression

- **identifier**: `x`, `isGood`, etc.

- **literal**: `1`, `2.1`, `"hello"`, etc.

- **function application**: `sqrt(2)`, etc.

- **operator application**: `-x`, `x + y`, etc.

- **selection**: `math.abs`, `point.x`, etc.

- **conditional expression**: `if (condition) ... else ...`

- **block**: `{ val a = 1; println(a)}`

- **anonymous function**: `x => x + 1`

## Definition

A **definition** can be:

- function type: `def square(x) = x * x`

- value type: `val y = square(2)`

A **parameter** can be:

- call-by-value: `(x: Int)`
- call-by-name: `(y: => Int)`
