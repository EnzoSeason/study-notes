# Object Oriented Programming

## Basic

```scala
class Person(name: String) // constructor

val person = new Person("John")
```

### Parameters vs Fields

**Class parameters** can't be accessed by `.` because they aren't **class fields**. For example, `person.name` isn't working.

To create a class field, we need to use `val` or `var`.

```scala
class Person(name: String, val age: Int)

val person = new Person("John", 26)
println(person.age) // works. Because age is a class field.
```

### Body

```scala
class Person(name: String, val age: Int) {
  // body

  // fields
  val x: Int = 2

  // methods
  def greet(name: String): Unit = println($"Hi $name.")
  // Overloading
  def greet(): Unit = println($"I'm ${this.name}. I'm ${this.age} years old.")
}

val person = new Person("John", 26)
println(person.x) // works.
```

- When **an instance is initialized**, all the codes in the body are run.
- `val` Values in the body are class **fields**.
- `this` points to **both class fields and methods**.
- In general, **overloading methods works** in Scala except one case, which is two methods have **the same name and parameters** but **return different types** of data.

### Immutability

Immutability is very important in Functional Programming.

When you need to **modify the contents of an instance**, you **create a new instance**.

```scala
class Counter(val num: Int) {
  def increase(n: Int = 1) = new Counter(this.num + n)
  def decrease(n: Int = 1) = new Counter(this.num - n)
}
```