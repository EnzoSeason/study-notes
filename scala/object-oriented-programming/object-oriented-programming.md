## Object Oriented Programming

### Basic

```scala
class Person(name: String) // constructor

val person = new Person("John")
```

#### Parameters vs Fields

**Class parameters** can't be accessed by `.` because they aren't **class fields**. For example, `person.name` isn't working.

To create a class field, we need to use `val` or `var`.

```scala
class Person(name: String, val age: Int)

val person = new Person("John", 26)
println(person.age) // works. Because age is a class field.
```

#### Body

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

#### Immutability

Immutability is very important in Functional Programming.

When you need to **modify the contents of an instance**, you **create a new instance**.

```scala
class Counter(val num: Int) {
  def increase(n: Int = 1) = new Counter(this.num + n)
  def decrease(n: Int = 1) = new Counter(this.num - n)
}
```

### Operators

All operators in Scala are **methods**.

```scala
val num = 1 + 2
val num = 1.+(2) // equivalent
```

Therefore, we can override or create an operator.

```scala
class Person(val: name) {
  def worksWith(person: Person): String = s"${this.name} works with ${person.name}."

  def +(person: Person): String = s"${this.name} works with ${person.name}."
}

val jack = new Person("Jack")
val paul = new Person("Paul")

println(jack + paul) // Jack works with Paul.
println(jack worksWith paul) // Jack works with Paul.
```

There is a very special method in Scala Class, `apply`.

```scala
class Person(val: name) {
  def apply(): String = s"I'm ${this.name}."
  def apply(val greeting: String): String = s"$greeting, I'm ${this.name}."
}

val mary = new Person("Mary")

mary.apply() // I'm Mary.
mary() // I'm Mary.

mary.apply("Hi")  // Hi, I'm Mary
mary("Hi")  // Hi, I'm Mary
```

`apply` method breaks the barrier between OOP and Functional Programming. So it's heavily used in Scala.

### Notation

```scala
class Person(val name: String) {
  // infix notation
  def worksWith(person: Person): String = s"${this.name} works with ${person.name}."
  // prefix notation
  def unary_!(): String = s"${name.toUpperCase()}!"
  // postfix notation
  def isAlive(): Boolean = true;
  // apply
  def apply(): String = s"I'm ${this.name}."
}
```

- **Infix notion**

  ```scala
  jack.worksWith(paul)
  jack worksWith paul // equivalent
  ```

  It only works on the method with **ONE parameter**.

- **prefix notion**

  ```scala
  jack.unary_!()
  !jack // equivalent
  ```

  It only works with `+`, `-`, `~`, `!`.

- **postfix notation**

  ```scala
  jack.isAlive()
  jack isAlive // equivalent
  ```

  It only works on the method with **NO parameters**.

- **apply**

  The special method let us call the instance of a class as a function.
