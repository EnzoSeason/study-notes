# Compound Data Type

## Array

- It is collection of **same data type**.

- Its elements are stored **in order**.

- It is stored in **contiguous memory**.

- It has a **fixed length**.

```rust
// create a char array
let letters = ['a', 'b', 'c'];
```

```rust
// define an array than contains 5 i32 integer.
let nums: [i32; 5];

// initialize the array with 0.
nums = [0; 5];
```

To get the length of an array, use `len()`:

```rust
let len: usize = nums.len();
```

> The size `usize` is based on the processor. For 32-bit processor, it's 4 btypes. For 64-bit processor, it's 8 btypes.

### Multidimensional Array

```rust
// create a two dimensional array with the size of 3 * 2
let map = [[1, 2, 3], [4, 5, 6]];

// define a three dimensional array with the size of 3 * 4 * 2
let store: [[[i32; 3]; 4]; 2]

// initialize the store with 0
store = [[[0; 3]; 4]; 2]
```

## Tuple

- It groups items of **mixed data types**.

- Its elements are **ordered**.

- It is stored in **fixed length**, **contiguous memory**.

- Data types of elements must be known at **compile time**.

```rust
let stuff: (u8, f32, char) = (1, 3.14, 'a');
let first_item = stuff.0;
```

### Destruction

```rust
let (a, b, c) = stuff;
```
