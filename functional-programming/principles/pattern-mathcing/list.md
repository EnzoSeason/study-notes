# List

```scala
val fruits = List("apple", "banana", "orange")
val nums = List(1, 2 ,3)
val diag3 = List(List(1, 0, 0), List(0, 1, 0), List(0, 0, 1))
val empty = List()
```

There are some important features:

- List is **homogeneous**. All the elements in the list have the same type.
- List is **immutable**.
- List is **recursive**.

List contains 2 types of cells:

- Cons-cell: It has a `head` which is the value, and `tail` which is the rest of the list.

- Nil: It's an empty cell.

## List patterns

- `Nil`: the constant `Nil`
- `x :: xs`: It matches the head is `x` and the tail is `xs`.
- `List(p1, ..., pn)`: same as `p1 :: ... :: pn :: Nil`

For example,

- `1 :: 2 :: xs`: It matches the list that first 2 elements are `1` and `2`

- `List(1, 2 :: xs)`: same as `1 :: 2 :: xs`

- `x :: Nil`: It matches a list whose length is 1.

- `List(x)`: same as `x :: Nil`

## Sorting a List

We use **insertion sort**.

```scala
def isort(xs: List[Int]): List[Int] = xs match {
  case List() => List()
  case y :: ys => insert(y, isort(ys))
}

def insert(x: Int, xs: List[Int]): List[Int] = xs match {
  case List() => List(x)
  case y :: ys => {
    if (x < y) x :: xs // insert x to the head of xs, and return
    else y :: insert(x, ys) // y is the head, keep inserting x
  }
}
```

Time complexity: `O(n^2)`. 

We need to traverse the entire list, and for each element, we need to move other elements before inserting it.
