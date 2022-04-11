## Module

Demo: [module-guessing](./module-guessing/)

### Standard Library

To use a module in the standard library:

```rust
use std::thread; // import the module
```

All the rust programs import `std::prelude` automatically. That's why we can use `String` which lives in the standard library without importing it.

### Crates

Crates represent a collection of Rust code files.

[crates.io](https://crates.io/) is the Rust community’s crate registry.

To install a crate, simple add it in `Cargo.toml`.

```rust
[dependencies]
rand = "0.8.4"
```

Then use it, and launch `cargo run`.

```rust
use rand::prelude::*;
```
