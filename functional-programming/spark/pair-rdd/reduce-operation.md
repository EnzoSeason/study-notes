# Reduce operations

Reduce operations include `fold`, `aggregate`, which are from Scala collection.

- `foldLeft`

  ```scala
  def foldLeft[B](z: B)(f: (B, A) => B): B
  ```

  > It's the popular choice for reduction in Scala collection.

- `foldRight`

  ```scala
  def foldRight[B](z: B)(f: (A, B) => B): B
  ```

- `fold`

  ```scala
  def fold[B](z: B)(f: (B, B) => B): B
  ```

- `aggregate`

  ```scala
  def aggregate[B](z: => B)(seqop: (B, A) => B, combop: (B, B) => B)
  ```

  This function combines `foldLeft` and `fold`.

  - `seqop`: Sequential operation

  - `combop`: Combination operation

Reduction operations **walk through collections** and **combine neighboring elements together** to **produce a single combined result**.

## Reduce operation in RDD

`foldLeft` and `foldRight` are not in Spark. So, Spark has:

- `fold`

- `aggregate`

`aggregate` is the popular choice.
