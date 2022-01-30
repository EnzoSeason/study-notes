# Ownership

## Scope

`{}` defines a scope.

The variable defined in a scope can't be accessed by the outside of the scope.

## Shadowing

In Rust, the variable is immutable by default.

However, we can shadow the variable.

```rust
let a = "Hello";
let a = 1; // shadowing. It works.
a = 1; // Error. The variable is immutable
```

Shadowing can be used in different scopes.

```rust
let a = "Hello";
{
  let a = 1;
  println!(a); // 1
}
println!(a); // Hello
```

## Program Memory

Program memory which holds the data is divided into 2 section, **stack and heap**.

### Stack

- Values are stored in **sequential order**.

- Stack follows the rule, **FILO** (First In Last Out).

So that, Stack has the features:

- Data can be accessed **quickly**

- Stack itself is **small in size**.

- The items in stack have **fixed size**.

The data type:

- Integer
- Floating point
- Boolean
- Char
- Array
- Tuple

has a **fixed size**, so they live in the stack.

### Heap

- Size is **big and dynamic**.

- The items in heap have **no order**.

- The access of data in heap is **slower** than that in stack.

To access a item in a heap, we need a **pointer**.

## String

There are 2 string types in Rust.

| String Literal                       | String Type                      |
| ------------------------------------ | -------------------------------- |
| Hard-coded                           | Allocated on the heap            |
| Immutable                            | Mutable                          |
| Must be known before the compilation | Dynamically generated at runtime |

```rust
let a = "hello"; // String Literal
let message = String::from("hello"); // String Type
```

`message` lives on the **stack**, and it contains the information like the **pointer** to the first letter, string length, capacity, etc. While all the letters of `hello` live on the **heap**.

**String Type** makes it easy to modify the string.

## Ownership

Although the size of the heap is huge, it's not infinite. We need to release the unused memory. The common ways are:

- Manully release. (C, C++)
- Garbage Collection, clean up the memory automatically. (Java, C#, Python, etc)

Rust uses the **ownership**. Variable are responsible for freeing their own resource. The rules are:

1. A value is **owned, and only owned** by ONE variable.

2. Once the variable is **out of the scope**, the value is dropped.

> **Ownship** is a VERY IMPORTANT concept. Rust developer should keep it in mind.

## Move, Clone

### Move

```rust
let outer_message: String;

{
    let message = String::from("hello");
    outer_message = message;
    println!("{}", message); // Error
}

println!("{}", outer_message); // hello
```

In other languages, `outer_message` and `message` should both point to _hello_ who lives in the heap.

However, because of the **ownership**: A value is **owned, and only owned** by ONE variable. `outer_message` owns _hello_ and `message` no longer exists.

### Clone

```rust
let outer_message: String;
let outer_num: i32;

{
    let message = String::from("hello");
    let num = 1;

    outer_message = message.clone();
    outer_num = num;
    println!("{}", message); // Error
}

println!("{}", outer_message); // hello
```

To solve the error appeared in the previous section, we use `clone()` for cloning a value that lives on the **heap**.

> The value lives on the **stack** is cloned by default.

## Transferring ownship

```rust
fn main() {
    let message = String::from("Ownership is cool!");
    update_message(message);
    println!("{}", message); // Error
}

fn update_message(old_message: String) {
    println!("{}", old_message);
}
```

In this example, the **ownship** is transferred from `message` to `old_message`. That's why we have the error.

One way to solve it is passing `message.clone()` instead of `message`.
