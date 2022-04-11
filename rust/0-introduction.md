# Rust for Solana

[Quest 1: Introduction to Rust for Solana](https://www.youtube.com/playlist?list=PLeShFtA-ZIOVo7H59Gq-LA0Go1EiUs-vk)

## Install Rust

Use [rustup](https://www.rust-lang.org/tools/install) to install.

## Hello world project

1. Use `cargo new hello-world --bin` to initialize the project.

2. Use `cargo run` to build to project. The built project is under `/target`, and it shouldn't be committed to git.

Demo: [hello-world](./hello-world/)

## Common concepts

### [Variables and Immutability](https://doc.rust-lang.org/book/ch03-01-variables-and-mutability.html)

By default, variables in Rust are **immutable**.

However, we can create a mutable variable.

```rust
let mut x = "hello";
```

### [Data Type](https://doc.rust-lang.org/book/ch03-02-data-types.html)

We can create a variable, and add a type annotation.

```rust
let x: i32 = 8;
```

Although we can create a mutable variable, we can NOT change its type once it's created.

There are 3 basic data types:

- **number**

  It contains `i32`, `u32`, `f64`, etc.

  The default integer is `i32` and default float is `f64`.

  ```rust
  let integer = 3; // i32
  let float = 3.14; // f64
  ```

- **string**

  ```rust
  let a_str = "hello";
  ```

- **boolean**

  ```rust
  let is_rust_cool = true;
  ```

Other useful types are:

- **tuple**

  ```rust
  let my_tuple = (1, "cool", true); // create a tuple

  println!("{}", my_tuple.0); // access a member of the tuple

  let (a, b, c) = my_tuple; // deconstruct a tuple
  ```

- **array**

  ```rust
  let my_array = [1, 2, 3];
  println!("{}", my_array[0]); // 1
  ```

  ```rust
  let my_filled_array = [1; 3];
  println!("{:?}", my_filled_array); // [1, 1, 1]
  ```

  The type of `my_filled_array` can be explict as `[i32; 10]`

### [Control flow](https://doc.rust-lang.org/book/ch03-05-control-flow.html)

#### Condition

```rust
let num = 1

if num == 2 {
  // do something
} else if num == 1 {
  // do something else
} else {
  // do something anyway...
}
```

#### Loop

- `while`:

  ```rust
  let mut counter = 0;
  while counter < 10 {
      println!("{}", counter);
      counter += 1;
  }
  ```

- `loop`: It's `while true`

  ```rust
  let mut counter = 0;
  loop {
      println!("{}", counter);
      counter += 1;
      if counter == 10 {
          break;
      }
    }
  ```

- `for`:

  ```rust
  for i in 0..10 {
      println!("{}", i);
  }
  ```

  `for` can be applied on the `iterator`.

  ```rust
  let my_array = [1, 2, 3, 4, 5];
  for i in my_array {
      println!("{}", i);
  }
  ```

### [Pattern Matching](https://doc.rust-lang.org/book/ch06-02-match.html)

```rust
let x = 2;
match x {
    1 => println!("one"),
    2 => println!("two"),
    _ => println!("something else"),
}
```

`match` can be more complicated and useful.

```rust
let x = true;
let y = false;

// match a tuple
// It's much better than if conditions.
match (x, y) {
    (true, true) => println!("true and true"),
    (true, false) => println!("true and false"),
    (false, true) => println!("false and true"),
    _ => println!("something else"),
}
```
