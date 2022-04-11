## Reference

Playground: [reference](./reference/)

### Borrowing references: `&`

Since passing the variable directly into a function will cause **ownship** problem, we pass **a reference of the variable** to avoid that.

```rust
fn main() {
    let message = String::from("Hello");
    print_message(&message); // passing the reference of message
    println!("{}", message); // message has the ownship so that it still exists.
}

fn print_message(message: &String) {
    println!("{}", message);
}
```

### Mutable reference: `&mut`

We can **create a mutable reference**, and pass it to the function so that the function can modify the **mutable variable**.

```rust
fn main() {
    let mut message = String::from("Hello");

    let message_ref = &mut message;
    update(message_ref);
    // equivalent to: update(&mut message);

    println!("{}", message);
}

fn update(message: &mut String) {
    message.push_str(", world!");
}
```

#### Restriction

We can create **ONLY ONE** mutable reference for a mutable variable.

However, we can createa as many reference as we want for a immutable variable.

### Slice

We can use the reference to choose the slice we want.

```rust
let message = String::from("Hello, world!");

let last_word = &message[7..12];
println!("{}", last_word); // world
```

- Attention: The length is in **bytes**. A character like emoji can take more than one byte.

We can also apply slice to an array.

```rust
let nums = [1, 2, 3, 4, 5];

let inner_nums = &nums[..2];
println!("{:?}", inner_nums); // [1, 2]
```

### Slices in function

We can let the function **get/return a slice**.

```rust
fn main() {
    let message = "Hello World";
    let first_world = get_first_world(&message);
    println!("{}", first_world); // Hello
}


fn get_first_world(message: &str) -> &str {
    let bytes = message.as_bytes();

    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            return &message[0..i];
        }
    }

    return message;
}
```

- `&String` points to **the data structure on the stack**, which contains the infomation like the pointer pointed to the first character of the string lived on the heap, string length, capacity, etc.

- `&str` contains:

  - The **pointer** pointed to the first character of the string lived on the heap.

  - The length of the slice.

#### Deref Coercion

`&String` can be passed into a function as `&str`, while `&str` can't be treated as `&String`.

```rust
let message = String::from("Hello World");
let first_world = get_first_world(&message); // OK

fn get_first_world(message: &str) -> &str {
  message
}
```

### Dereference Operator: `*`

`&a` means the **pointer** of the **variable** `a`.

`*p` means the **variable** pointed by the **pointer** `p`.
