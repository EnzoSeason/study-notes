## Iifetime

Demo: [lifetime-demo](./lifetime-demo/)

```rust
let a;
{
    let b = 1;
    a = &b
}
println!("{}", a); // ERROR
```

This error is caused by **lifetime**. When we try to print `a`, the **reference** of `b`, `b` is out of its lifetime.

To solve this problem, we need to let `b` have the same lifetime as `a`.

```rust
let a;
let b = 1;
{
    a = &b
}
println!("{}", a); // OK
```

### Lifetime annotation syntax

We can use the **lifetime annotation syntax** to tell the compilor the lifetime of a **reference**.

Lifetime annotation syntax is similar to **gerneric**.

```rust
fn longer_string<'a>(string_1: &'a str, string_2: &'a str) -> &'a str {
    if string_1.len() > string_2.len() {
        string_1
    } else {
        string_2
    }
}
```

`'a` is the **lifetime annotation syntax**. It means the **three reference**, `string_1`, `string_2` and _return value_, have the same lifetime.

### Lifetime elision rules

At the beginning of Rust, we must write the lifetime explictly for the reference. So far, we've some elision rules to make development easier.

1. Each input parameter, which is a reference, is assigned **its own lifetime**.

   `func(name_1: &str, name_2: &str)` means:

   `func<'a, 'b>(name_1: &'a str, name_2: &'b str)`

2. If there is ONE input lifetime, this lifetime is the output lifetime, too.

   `func(name_1: &str) -> &str` means:

   `func<'a>(name_1: &'a str) -> &'a str`

3. If there is `&self` or `&mut self` input lifetime, then its lifetime will be the output lifetime, too.

   `func($self, name_1: &str) -> &str` means:

   `func<'a, 'b>(&'a self, name_1: &'b str) -> &'a str`

### Struct lifetime

If a `struct` owns a reference, we need a lifetime on it.

```rust
struct Person<'a> {
    name: &'a str,
}
```

To implement a method:

```rust
impl<'a> Person<'a> {
    fn greet(&self, msg: &str) -> &str {
        println!("{} says {}", self.name, msg);
        self.name
    }
}
```

According to the third lifetime elision rules, the _returned reference_ has the same lifetime as `&self`.

If we want to return `msg`, we need to write the lifetime explictly.

```rust
impl<'a> Person<'a> {
    fn greet<'b>(&self, msg: &'b str) -> &'b str {
        println!("{} says {}", self.name, msg);
        msg
    }
}
```

### Static lifetime `'static`

The static lifetime indicates the reference is available for **entire duration of program**.

For example, the **string literal** has the static lifetime.

```rust
let s: &'static str = "Hello";
```

It can be also used as a **trait bound**, _i.e._ `<T: Display + 'static>`.
