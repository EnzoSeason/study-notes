# Generic

Demo: [generic-demo](./generic-demo/)

## Generic struct

```rust
// create a generic struct
struct Rectangle<T, U> {
    width: T,
    height: U,
}

// use it
let rect = Rectangle {
    width: 30,
    height: 50.0,
};
```

## Generic method

```rust
impl<T, U> Rectangle<T, U> {
    fn get_width(&self) -> &T {
        &self.width
    }
}

print!("rect's width is {}", rect.get_width());
```

Since we don't know where the type `T` lives, stack or heap, it's safer to return a reference so that we can avoid transfering the ownship.

What's more, we can implement the methods for specific `Rectangle`.

```rust
impl Rectangle<f64, f64> {
    fn area(&self) -> f64 {
        self.width * self.height
    }
}

let rect_f64 = Rectangle {
    width: 30.0,
    height: 50.0,
};
println!("rect2's area is {}", rect_f64.area());
```

## Generic function

```rust
fn get_bigger<T: PartialOrd>(first: T, second: T) -> T {
    if first > second {
        first
    } else {
        second
    }
}

println!("The bigger one is {}", get_bigger(10, 20));
```

`<T: PartialOrd>` makes sure the type `T` can be compared.


