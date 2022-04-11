## Pattern Matching

Pattern matching in Scala is similar to `switch` in other languages.

```scala
val x = 1
val desc = x match {
  case 1 => "One"
  case 2 => "Two"
  case _ => "Something else" // wild card
}
```

but, it can do much more.

### Decompose value

```scala
case class Person(name: String, age: Int)

val bob = Person("Bob", 18)

val greeting = bob match {
  case Person(name, age) if age < 21 => s"I'm $name, I can't drink beer."
  case Person(name, age) => $"I'm $name, I'm $age years old."
  case _ => $"I don't know who I am."
}
```

There are some rules:

- `cases` are matched **in order**.
- The type of the returned value of Pattern Matching is the **lowest common ancestor** of all the cases' type.
- Pattern Matching works directly with `case class`.

### Patterns

In Scala, the patterns can be used in pattern matching are as followed.

- **Constant**

  Such as `Int`, `String`, `Boolean`, etc. And the singleton **object**.

- **Wild card**: `_`

- **Variable**

  ```scala
  val match = x match {
    case var => s"$x matches $var"
  }
  ```

- **Tuple and nested tuple**

  ```scala
  val tuple = (1, (2, 3))

  val match = tuple match {
    case (1, (2, 3)) => "exact"
    case (_, (2, num)) => "partial"
  }
  ```

- **`case` class**: constructor pattern

- **`List`**

  ```scala
  val list = List(1, 2, 3)
  val listMatching = list match {
    case List(1, _, _) => "A list that starts with 1"
    case List(1, _*) => "A list that starts with 1, too" // list of arbitrary length
    case 1 +: List() =>  "A list that starts with 1, too" // infix pattern
    case List(1, 2) :+ 3 => "A list that ends with 3" // infix pattern
  }
  ```

- **Type specifier**

  ```scala
  val unknown: Any = 1
  val unknownMatch = unknown match {
    case list: List[Int] => "A list of integers"
    case _ => "any type"
  }
  ```

- **Name binding**: We can give a pattern a name so that it's easier to reuse it.

  ```scala
  val nameBindingMatch = list match {
    case startWithOne @ List(1, _*) => "A list that starts with 1"
  }
  ```

- **Multiple cases**

  ```scala
  val multiMatch = list match {
    case List() | List(1, _*) => "A list that starts with 1 or empty"
  }
  ```

Attention: Scala **DOES NOT** check the generic type during matching because of JVM.

That means `List[Int]` and `List[String]` are the same in pattern matching. They are just `List`.