## Generic

Demo: [generic-demo](./generic-demo/)

### Generic struct

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

### Generic method

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

### Generic function

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

### Box type

It stores the data on the **heap** instead of stack.

Box itself lives on the stack. It has a **pointer** which points to the data on the heap.

```rust
use std::mem;

let car = Shuttle {
    name: String::from("Car"),
    crew_size: 11,
    fuel: 1.0,
};
println!("The memory used on stack for a car: {} bytes", mem::size_of_val(&car));
// The memory used on stack for a car: 40 bytes

let boxed_car = Box::new(car);
println!("The memory used on stack for a boxed car: {} bytes", mem::size_of_val(&boxed_car));
// The memory used on stack for a boxed car: 8 bytes

println!("The memory used on heap for a boxed car: {} bytes", mem::size_of_val(&*boxed_car));
// The memory used on heap for a boxed car: 40 bytes
```

#### Smart pointer

The **pointer** kept by the `Box` has more functionality than reference.

`Box<T>` has the **ownship** to the data that it points to. That means once `Box<T>` is out of the scope, the data in heap is dropped.

```rust
println!("{}", boxed_car.crew_size); // OK. No problem.
println!("{}", car.crew_size);// Error, car lost its ownship. The ownership is transferred to boxed_car.
```

#### Use cases of `Box`

- Store the type whose size can't be known at compile time, such as a **recursive data type**.

- Move a large amount of data **from stack to heap** quickly.