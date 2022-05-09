# Recap: Functions and Pattern Matching

## Case class

Representation of JSON

```scala
abstract class JSON
object JSON {
  case class Seq(elems: List[JSON]) extends JSON
  case class Obj(props: Map[String, JSON]) extends JSON
  case class Num(num: Double) extends JSON
  case class Str(str: String) extends JSON
  case class Bool(b: Boolean) extends JSON
  case object Null extends JSON
}
```

The previous `object` can be written in `enum`.

```scala
enum JSON {
  case Seq(elems: List[JSON])
  case Obj(props: Map[String, JSON])
  case Num(num: Double)
  case Str(str: String)
  case Bool(b: Boolean)
  case Null
}
```

## Pattern matching

The string representation of JSON data.

```scala
def show(json: JSON): String = json match {
  case JSON.Seq(elems) => {
    elems.map(show).mkString("[", ",", "]")
  }
  case JSON.Obj(props) => {
    props.map((k, v) => s"\"${k}\": ${show(v)}")
      .mkString("{", ",", "}")
  }
  case JSON.Num(num) => num.mkString
  case JSON.Str(str) => s"\"${str}\""
  case JSON.Bool(b) => b.toString
  case JSON.Null => "null"
}
```

## Collections

```code
        Iterable
      /    |   |
     Seq  Set Map
    /
 List
```

All the collections shares some common functions.

The core functions are:

- `map`

  ```scala
  extension [T](xs: List[T])
    def map(U)(f: T => U): List[U] = xs match {
      case Nil => Nil
      case head :: tails => f(head) :: map(tails)
    }
  ```

- `flatMap`

  ```scala
  extension [T](xs: List[T])
    def flatMap(U)(f: T => List[U]): List[U] = xs match {
      case Nil => Nil
      case head :: tails => f(head) ++ flatMap(tails)
    }
  ```

  > xs.flatmap(f) = xs.map(f).flatten

- `filter`

and the reduce functions:

- `foldLeft`
- `foldRight`

## For-comprehension

It simplifies the combinations of core method, `map`, `flatMap`, `filter`.

Instead of:

```scala
(1 until n)
  .flatMap(i => (1 until i)
    .filter(j => isPrime(i + j))
    .map(j => (i, j)))
```

We can write:

```scala
for {
  i <- 1 until n
  j <- 1 until i
  if isPrime(i + j)
} yield (i, j)
```

What's more, we can **apply pattern matching in for-comprehension**.

```scala
def props(x: JSON): List[(String, JSON)] = x match {
  case JSON.Obj(props) => props.toList
  case _ => Nil
}

// get all french phone numbers in the json.
for {
  // If the prop name is "phoneNumber" and its value is a JSON.Seq, get it
  case ("phoneNumber", JSON.Seq(numberInfos)) <- props(json) 
  numberInfo <- numberInfos
  // If the prop name is "number" and its value is a JSON.Number, get it
  case ("number", JSON.Number(number)) <- props(numberInfo)
  if number.startWith("33")
} yield number
```
