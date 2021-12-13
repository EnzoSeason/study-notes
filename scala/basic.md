# Basic

## Values

```scala
val x: Int = 42
```

- `val` means **immutable**.

  It's like `const` or `final` in other language.

- `Int` is optional.

  The compiler can infer that the type of variable is `Int`.

## Variables

```scala
var aVariable: Int = 4
aVariable = 5
```

- `var` defines **variable**.

  We can assign a new value to it.

  Changing Variables is **side effects** in functional programming.

In functional programming, we prefer `Values` over `Variable` because `Values` are immutable, and they won't cause side effects.

## Types

- `Boolean`

  It only has 2 values, `true` or `false`.

- `Char`, `String`

  `Char` is the single character. It's written between the **single quotes**.

  ```scala
  val aChar: Char = 'c'
  ```

- `Int`, `Short`, `Long`

  They all represent the number.

  `Short` presents **2 btyes**, 16 bits, 2<sup>16</sup>.

  `Int` presents **4 btyes**, 32 bits, 2<sup>32</sup>.

  `Long` presents **8 btyes**, 64 bits, 2<sup>64</sup>.

- `Double`

  It represents float number.