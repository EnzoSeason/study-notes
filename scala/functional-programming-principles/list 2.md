# Lists

- Type: `List[T]`

- Construction:

  ```scala
  val fruit = List("apple", "banana", "orange")
  val nums = 1 :: 2 :: Nil
  ```

- Decomposition

  ```scala
  val apple = fruit.head
  ```

  - The most useful functions: `nums.head`, `nums.tail`, `nums.isEmpty`
  - `nums.length`
  - `nums.last`, `nums.init`: the opposite of `nums.head`, `nums.tail`
  - `nums.take(n)`: get first `n` nodes
  - `nums.drop(n)`: get the rest after drop the first `n` nodes.
  - `nums(i)`: get the _i<sup>th</sup>_ node. It equals to `nums.apply(i)`

- Creating a new list

  - `xs ::: ys` or `xs ++ ys`: concat 2 lists, and return a new one
  - `xs.reverse`: return a reversed `xs`
  - `xs.update(i, x)`: update the _i<sup>th</sup>_ node by `x`, and return a new one

- Finding a node

  - `xs.indexOf(x)`: return the index of `x` in `xs`. `-1` if not found.
  - `xs.contains(x)`: Same as `xs.indexOf(x) >= 0`
