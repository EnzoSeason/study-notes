# Set

`Set` is the subclass of `Iterable`.

```scala
val fruits = Set("apple", "banana")
val s = (1 until 6).toSet

s.map(_ + 2)
fruits.filter(_.startWith("app"))
```

1. `Set` is **unordered**.

2. `Set`'s elements are **unique**.

3. `contains` function is very useful in `Set`

   ```scala
   s.contains(1) // true
   ```
  
## Exercise

```scala
def meetQueen(col: Int, intercept: Int, queens: List[Int]): Boolean = queens match {
  case Nil => false
  case q :: others => {
    q == col || (q - col).abs == intercept || meetQueen(col, intercept + 1, others)
  }
}

def queens(n: Int) = {
  def playQueens(k: Int): Set[List[Int]] = {
    if (k == 0) Set(List())
    else {
      for (
        queens <- playQueens(k - 1);
        col <- 0 until n
        if !meetQueen(col, 1, queens)
      ) yield col :: queens
    }
  }
  playQueens(n)
}
```
