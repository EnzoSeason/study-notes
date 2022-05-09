# Sequences

Sequence is a general interface for data structure that:

- have an **order**
- can be **indexed**

```scala
trait Seq[+A] {
  def head: A
  def tail: Seq[A]
}
```

## Seq

Here is some codes of using `Seq` in Scala

```scala
val seq = Seq(1, 2, 3)

println(seq) // List(1, 2, 3)

println(seq.reverse) // List(3, 2, 1)

println(seq(0)) // 1. apply() of Seq is findAt()

println(seq ++ Seq(4, 5)) // List(1, 2, 3, 4, 5) concat

println(Seq(7, 9, 8).sorted) // List(7, 8, 9)
```

## List

`List` inherits `LinearSeq`. `LinearSeq` has some features:

- The methods, such as `head`, `tail` and `isEmpty`, are `O(1)`.

- The majority methods, such as `lenght`, `reverse`, are `O(n)`.

Here is some codes for usage.

```scala
val list = List(1, 2, 3)

val prepend = 0 +: list
println(prepend) // List(0, 1, 2, 3)

val append = list :+ 4
println(append) // List(1, 2, 3, 4)

val listString = list.mkString("-") // It makes a string from the list.
print(listString) // 1-2-3

val apple5 = List.fill(5)("apple")
println(apple5) // List(apple, apple, apple, apple, apple)
```

## Range

`Range` inherits `IndexSeq`.

`Range` is very useful for iteration.

```scala
val range = 0 until 10 // 0 is included and 10 is not.
range.foreach(println)
```

## Vector

It's the **default implementation for immutable sequence**.

It's

- very efficient for **constant** indexed read and write. `O(logn)`

- easy to append and prepend.

  ```scala
  val num = Vector.empty :+ 1 :+ 2
  println(num) // Vector(1, 2)
  ```

- good performance for large sizes

## Array

`Array` in Scala is equivalent to that in Java.

It:

- can be manually **constructed with predefinded length**

  ```scala
  val arrNum = Array.ofDim[Int](3)
  arrNum.foreach(println) // 0, 0, 0

  val arrStr = Array.ofDim[String](3)
  arrStr.foreach(println) // null, null, null
  ```

- can be **mutated**

  ```scala
  arrNum(0) = 2
  arrNum.foreach(println) // 2, 0, 0
  ```

We can transform `Array` to `Seq`. It's called **implicit conversion**.

```scala
val seqNum: Seq[Int] = arrNum
println(seqNum) // ArraySeq(2, 0, 0)
```
