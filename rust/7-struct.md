# Struct

Demo: [struct-demo](./struct-demo/)

- It groups multiple items of **mixed data types**.

- Each item in a struct has a **name**.

```rust
struct Shuttle {
    name: String,
    crew_size: u16,
    fuel: f64,
}
```

To use `struct` data type:

```rust
// create a variable
let car = Shuttle {
    name: String::from("Car"),
    crew_size: 11,
    fuel: 1.0,
};

// access a field of the variable
println!("{}", car.name);
```

## Struct Update syntax

We can create another `Shuttle` by using the existing one.

```rust
let bus = Shuttle {
    name: String::from("Bus"),
    ..car
};
```

Be careful, `name` must be a new `String` because of the **ownship**.

```rust
let bus = Shuttle {
    ..car
};
// Error: The name's ownship on car is moved to bus. Car has no name.
```

## Struct Method

```rust
impl Shuttle {
    fn get_name(&self) -> &str {
        &self.name
    }
}
```

- The methods are written inside `impl`, not `struct`.

- The first parameter of the method **must** be the reference of the structure itself, `&self`.

We can implement a "setter" function, too.

```rust
impl Shuttle {
    fn add_fuel(&mut self, amount: f64) {
        self.fuel += amount;
    }
}
```

## Associated function

Associated function lives with `struct`, too. But, it **hasn't `&self` parameter**. So it can't access the fields in `struct`.

It's commonly used for "constructor".

```rust
impl Shuttle {
    fn new(name: &str) -> Shuttle {
      Shuttle {
          name: String::from(name),
          crew_size: 0,
          fuel: 0.0,
      }
  }
}

// use the new function in Shuttle
let ship = Shuttle::new("Ship");
```

## Tuple Struct

It's just alike the normal `tuple`, but it also has a name like `struct`.

```rust
struct Color(u8, u8, u8);

// use it
let red = Color(255, 0, 0);

// access the first item
println!("{}", red.0); // same as a tuple

// pass a reference of Color variable to a function
fn get_red_value(color: &Color) -> u8 {
    color.0
}
```
