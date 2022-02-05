# Trait

Demo: [trait-demo](./trait-demo/)

It's similar to **Interface** in other languages. It describes an ability by containing a collection of methods.

For example, we've the `struct` data types.

```rust
struct Satelite {
    name: String,
    velocity: f64,
}

struct SpaceStation {
    name: String,
    crew_size: u32,
}
```

We can create a `trait` to print out their information.

```rust
trait Describable {
    fn describe(&self) -> String;
}
```

Finally, we implement it for each `struct`.

```rust
impl Describable for Satelite {
    fn describe(&self) -> String {
        format!("{} is travelling at {} km/s", self.name, self.velocity)
    }
}

impl Describable for SpaceStation {
    fn describe(&self) -> String {
        format!("{} has a crew of {}", self.name, self.crew_size)
    }
}
```

## Default trait implementation

As we can see, the method in `trait` was not implemented. Actually, We can implement it.

```rust
trait Describable {
    fn describe(&self) -> String {
        "Hello".to_string()
    }
}
```

Then, the `impl Describable for Satelite` and `impl Describable for SpaceStation` can choose to override it or not.

## Derive trait

Derive trait provides **default implementations** for severval common traits, which are:

- `Eq`
- `PartialEq`
- `Ord`
- `PartialOrd`
- `Clone`
- `Copy`
- `Hash`
- `Default`
- `Debug`

For example, we want to compare between 2 satelites using `==` and `>`.

```rust
#[derive(PartialEq, PartialOrd)]
struct Satelite {
    name: String,
    velocity: f64,
}
```

- `PartialEq` decides `==` only if all the fields are equal.

- `PartialOrd` decides `>` just using the first field.