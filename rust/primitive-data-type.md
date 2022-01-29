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

## Bitwise operations

```rust
let value = 0b1111_0101u8;

println!("The value is {}", value); // The value is 245
println!("The value is {:08b}", value); // The value is 11110101
```

- `0b` indicates it's a binary bits.

- `_` helps us read, doesn't affect the value itself.

- `u8` indicates it's a unsigned 8-bits integer.

The operations are as followed.

- **NOT**

  It reverses. `0` to `1` and `1` to `0`.

  ```rust
  let new_val = !value;
  println!("The value is {:08b}", value); // The value is 11110101
  println!("The new value is {:08b}", new_val); // The value is 00001010
  ```

- **AND**

  If two values are `1`, then return `1`, else `0`.

  We use **AND**:

  - **clear** the value of a bit.

    ```rust
    let new_val = value & 0b1111_1110;
    println!("The value is {:08b}", value); // The value is 11110101
    println!("The new value is {:08b}", new_val); // The value is 11110100

    // The value of the first bit is removed.
    ```

  - **check** the value of a bit.

    ```rust
    let new_val = value & 0b0000_0001;
    println!("The value is {:08b}", value); // The value is 11110101
    println!("The new value is {:08b}", new_val); // The value is 00000001

    // There has value on the first bit.
    ```

- **OR**

  If two values are `0`, then return `0`, else `1`.

  We use **OR**:

  - **set** the value of a bit.

    ```rust
    let new_val = value | 0b0000_0010;
    println!("The value is {:08b}", value); // The value is 11110101
    println!("The new value is {:08b}", new_val); // The value is 11110111

    // The second bit is set to 1.
    ```

- **XOR**

  If two values are different, then return `1`, else `0`.

    ```rust
    let new_val = value ^ 0b1111_0100;
    println!("The value is {:08b}", value); // The value is 11110101
    println!("The new value is {:08b}", new_val); // The value is 00000001

    // The second bit is set to 1.
    ```

- **SHIFT**

  Shift the bits to left or right. If the bits are out of range, then we lose it.

  ```rust
  // value:   00010111
  let mut new_val = value << 4;
  // new_val: 01110000
  new_val = new_val >> 2;
  // new_val: 00011100
  ```
