# Enum

Demo: [enum-demo](./enum-demo/)

Enum is a data type with **multiple possible variants**.

```rust
enum Command {
    Clear,
    DrawLine(f64, f64), // enum can hold other data structure.
    DrawShape(Shape),   // enum can hold custom struct, too.
}
```

## Match operation

Match operation is very useful in Rust. It's similar to `switch` in other languages.

```rust
let my_shape = Shape::Rectangle(3.0, 4.0);

match my_shape {
    Shape::Circle(radius) => println!("Circle with radius {}", radius),
    Shape::Rectangle(width, height) => {
        println!("Rectangle with width {} and height {}", width, height)
    }
}
```

`_` is the default placehold if none of the conditions is matched.

```rust
let my_number: u8 = 1;
let res = match my_number {
    1 => "one",
    2 => "two",
    _ => "unknown",
};
```

## Enums method

We can implement **enum method** in the same way for `struct`.

```rust
impl Shape {
    fn area(&self) -> f64 {
        match *self {
            Shape::Circle(r) => 3.14 * (r * r),
            Shape::Rectangle(x, y) => x * y,
        }
    }
}
```

## `Option<T>` enum

`Option<T>` enum makes sure **null-safety**. It wraps the value that **might be present or not**.

```rust
enum Option<T> {
    Some(T), // might have value
    None   // None value
}
```

It's so useful that some data type implements it directly. For example, an **array**:

```rust
let nums = [1, 2, 3];
let my_num = nums[5]; // Error: index out of bounds
let my_num = nums.get(5); // OK. get() returns an Option enum. Here is None.
```

We can use `match` to get the value in the `Option`.

```rust
let res = match my_num {
    Some(n) => n,
    None => &0,
};
```

If we only care about a specific option,

```rust
match my_num {
    Some(1) => println!("One"),
    _ => (), // Do nothing
}
```

we can use the syntax sugar: `if let`:

```rust
if let Some(1) = my_num {
    println!("One");
}
```
