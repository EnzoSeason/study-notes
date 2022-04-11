# Case class

`case` class adds a lot of useful features to the normal class. It is handy to build lightweight data structures.

```scala
case Person(name: String, age: Int)

val jim = new Person("Jim", 34)
```

The features are as followed:

1. Class parameters are fields.

   ```scala
   jim.name // It works
   ```

2. It's sensible to `toString`.

   ```scala
   println(jim.toString) // output: Person(Jim, 34)
   println(jim) // It's same as the previous line.
   ```

3. `equals` is implemented.

   ```scala
   val jim2 = new new Person("Jim", 34)
   println(jim == jim2) // true
   ```

4. `copy` is very useful.

   ```scala
   // copy jim and set age to 13
   val jim3 = jim.copy(age = 13)
   ```

5. Case classes have **[companion objects](./object.md#Companions)**

   ```scala
   val mary = Person("Mary", 20)
   ```

6. Case classes are serializable.

   It's very useful in the framework **Akka**.

7. Case classes have extractor patterns.

   It means they can be used in **pattern matching**.

We can also create `case object`.

```scala
case object Cat
```
