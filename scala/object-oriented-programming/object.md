## Object

Scala doesn't have the "class-level" functionality (the attributes or methods with `static` keyword). Instead, It uses a special class with `object` keyword.

```scala
object Person {
  val N_EYES = 2
}

println(Person.N_EYES)
```

Attention: `object` class doesn't receive parameters.

### Singleton

`object` creates the **singleton**.

```scala
val mary = Person
val paul = Person
println(mary == paul) // true
```

### Companions

```scala
object Person {
  // "class-level" functionality
  val N_EYES = 2
}
class Person {
  // "instance-level" functionality
}
```

We defines "class-level" functionality in `object` and "instance-level" functionality in `class`.

The **factory method** in design patterns is widely used in Scala.

```scala
object Person {
  // factory method
  apply(mother: Person, father: Person): Person = new Person(mother.name + father.name)
}
class Person(val name: String)

val mother = new Person("Mary")
val father = new Person("Jack")
val kid = Person(mother, father)
```

### Scala Application

The scala application is a `object` class with `def main(args: Array[String])`. This function serves as an entry point for JVM to run the codes inside it.

```scala
object Demo {
  def main(args: Array[String]): Unit = {
     // your codes
  }
}
```

We can also simply inherit `App`.

```scala
object Demo extends App {
  // your codes
}
```
