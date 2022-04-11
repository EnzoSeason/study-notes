## Collection

Demo: [collection-demo](./collection-demo/)

### Vector: `Vec<T>`

- A collection of the **same** data type.

- The elements are stored in order.

- The elements are added or removed dynamically.

  > An array has a fixed size.

- It's stored on the heap.

### HashMap: `HashMap<K, V>`

- It stores the data in key-value pair.

- All the key or value must have the same type.

#### Update a key-value pair

- override the existing one

  ```rust
   scores.insert(String::from("Blue"), 25);
  ```

- create a new pair if it doesn't exist

  ```rust
  scores.entry(String::from("Green")).or_insert(50);
  ```

- modify the pair based on current state

  ```rust
  let blue_team_score = scores.entry(String::from("Blue")).or_insert(0);
  *blue_team_score += 10;
  ```
