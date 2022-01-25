# Primitive data type

## Variable

By default, variables in Rust are **immutable**.

However, we can create a mutable variable.

```rust
let mut x = "hello";
```

## Integer

There are 2 types:

- **sign**: Both positive and negative integer

- **unsigned**: Only positive integer

For example, 8-bit integer represents 2<sup>8</sup> = 256 possible values.

- `u8`: It represents the value **between 0 and 255**.

- `i8`: It represents the value **between -128 and 127**.

The default integer is `i32`.

## Floating-point

Rust has 2 types of Floating-point:

- `f32`:

  It represents **6 to 9** significant decimal digits of precison.

- `f64`:

  It represents **15 to 17** significant decimal digits of precison.

The default float is `f64`.

## Arithmetic operations

Rust can do arithmetic operations, such as `+`, `-`, `*`, `/`, `%`.

Rust can't do them between different types of data.

```rust
let a = 10;
let b = 3.0;

let c = a / b; // error
```

We can **cast between 2 different number types**.

```rust
let a = 3 as f64; // 3.0
let b = 3.9 as i32 // 3
```

## Formatting print

```rust
let a = 10.0;
let b = 3.0;

let c = a / b;
```

- **Rounding** the number

  ```rust
  println!("c is {:.3}", c);
  // c is 3.333
  ```

- **Padding** the display

  ```rust
  // 8 chars before dot, padding with 0
  println!("c is {:08.3}", c);
  // c is 0003.333
  ```

- **indicating** the values' indexes

  ```rust
  println("a is {1}, and b is {0}", b, a);
  // a is 10.0, and b is 3.0
  ```
