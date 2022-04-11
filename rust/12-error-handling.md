## Error handling

Demo: [error-handling](./error-handling/)

In Rust, there are 2 types of error.

| Recoverable                | Unrecoverable                |
| -------------------------- | ---------------------------- |
| Example: file not found    | Example: index out of bounds |
| Handle with `Result<T, E>` | Handle with `panic!`         |

`panic!` stop the program immediately and provide feedback.

### `Result<T, E>` enum

Similar to `Option<T>`, `Result<T, E>` wraps the value. It provides `Ok` and `Err` to make sure the error is catched.

```rust
enum Result<T, E> {
    Ok(T),
    Err(E)
}
```

It's included in `prelude` so we don't need to import it explictly.

To handle the error, we can use `match`.

```rust
// fs::read_to_string returns a Result
let result = fs::read_to_string("hello.txt");

let contents = match result {
    Ok(contents) => contents,
    Err(e) => panic!("There was a problem reading the file: {:?}", e),
};
```

### Propagating errors

Sometimes, we want to propagate the errors from low level to high level, then deal with it. For example, we create a `read_file` function and call it.

```rust
fn read_file(file_name: &str) -> Result<String, io::Error> {
    let result = match fs::read_to_string(file_name) {
        Ok(string) => string,
        Err(error) => return Err(error),
    };
    Ok(result)
}

fn main() {
    let file_string = read_file("src/test.txt");
    let contents = match file_string {
        Ok(contents) => contents,
        Err(e) => panic!("There was a problem reading the file: {:?}", e),
    };
    println!("{}", contents);
}
```

We've writen `match` 2 times. There is a way to prograte it. We don't handle with the error in `read_file` function, only in the `main` function.

```rust
fn read_file(file_name: &str) -> Result<String, io::Error> {
    let result = fs::read_to_string(file_name)?;
    Ok(result)
}
```

> Attention: It only works with the function returns a Result.
