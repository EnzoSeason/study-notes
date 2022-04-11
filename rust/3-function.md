## Function

```rust
fn say_sum(a: u8, b: u8) {
  println!("sum is {}", a + b);
}

fn say_number(num: i32) {
  println!("number is {}", num);
}

let x = 1;
let y = 2;

// Compiler figures out x and y should be u8.
// Now, x and y are u8.
say_sum(x, y);

// Error, x is u8, not i32.
say_number(x);
```

### Statement vs Expression

A statement performs an action **without return**. In Rust, it **ends with `;`**.

```rust
let a = 1;
```

On the other hand, An expression **returns** values. It does **not ends with `;`**.

```rust
let sum = 1 + 2;
// It's a statement while 1 + 2 is an expression.
```

### Function return

```rust
fn square(x: i32) -> i32 {
  x * x
}
```

It's possible to return multiply values by using **tuple**.

```rust
fn square(x: i32) -> (i32, i32) {
  return (x, x * x);
}

println!("Square result is {:?}", square(2));
```

If a function returns nothing, it returns `Unit` type by default, represented by `()`.

```rust
fn no_return_value() -> () { // returns Unit type
  // TODO
}
```
