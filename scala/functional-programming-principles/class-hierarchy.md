# Class hierarchy

## abstract class

Abstract class can leave the **methods unimplemented**. However, it can't be instanced.

## Superclass vs Subclass

Subclass **extends** superclass.

If no superclass is given, `Object` from `java.lang` is default superclass.

The **direct or indirect** superclass of `C` is call the **base class** of `C`.

## Object

`Object` defines a **singleton**, and it's a **value** so that:

- There's no other instances.

- It doesn't take variables.

```scala
object Person {
  val N_EYES = 2
}

val mary = Person
val paul = Person
println(mary == paul) // true
```

### Companion class/object

An object and a class can have the same name.

`Object` plays the role similar to **static class definition**.

```scala
object Person {
  // factory method
  def apply(mother: Person, father: Person): Person = new Person(mother.name + father.name)
}
class Person(val name: String)

val mother = new Person("Mary")
val father = new Person("Jack")
val kid = Person(mother, father)
```

### Programs

We can create an `Object` that contains `main` function, and it will be acted as a **program**.

```scala
Object Hello {
  def main(args: Array[string]): Unit = println("Hello, world")
}
```

```code
> scala Hello
```

Another way is using `@main` to create a function.

```scala
@main def birthday(name: String, age: Int) = {
  println(s"Happy birthday, $name! $age years old.")
}
```

```code
> scala birthday Peter 11
```
