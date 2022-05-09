# Generic

## Generic class

A class (or trait) can have multiple generic types.

> `object` can't have generic types.

```scala
class MyNode[T]
```

## Generic method

```scala
object MyList {
  def first[T]: MyNode[T] = ???
}

val firstNode = MyList.first[Int]
```

## Variance Problem

```scala
class Animal
class Cat extends Animal
class Dog extends Animal
```

### Covariance

```scala
class CovariantList[+T]

val catList: CovariantList[Animal] = new CovariantList[Cat]
```

The generic type in the class' **declaration** can be the **super type** of the class' **instance**.

### Invariance

```scala
class InvariantList[T]

val animalList: InvariantList[Animal] = new InvariantList[Animal]
```

The generic type in the class' **declaration** must be **exact type** of the class' **instance**.

### Contravariance

```scala
class ContravariantList[-T]

val trainerList: ContravariantList[Cat] = new ContravariantList[Animal]
```

The generic type in the class' **declaration** can be the **sub type** of the class' **instance**.

> The trainers of _Animal_ are those of _Cat_, too.

## Bounded Type

There are 2 types of bounds:

- Super bound `<:`

  ```scala
  class Cage[T <: Animal](animal: T)

  val cage = new Cage(new Animal)
  ```

  It means the type `T` should be `Animal` or its **sub-types**, such as `Cat` and `Dog`.

- Lower bound `>:`

  ```scala
  class CatTraining[T >: Cat](animal: T)

  val catTraining = new CatTraining(new Animal)
  ```

  It means the type `T` should be `Cat` or its super-types, like `Animal`.

Bounded Type help solve the variance problem.

The problem is if we have a class `class MyList[+T]`, then:

```scala
val myList: MyList[Animal] = new MyList[Cat]
myList.add(new Dog) // Does it work?
```

The answer is yes. Because `myList` is a list of `Animal` even if we initialize it as a list of `Cat`.

To implment `add` method, we need to use **bounded type**.

```scala
class MyList[+T] {
  // def add[T](element: T): MyList[T] = ???
  // Error. Because Nothing is sub-type of all the types.
  // The solution is as followed.
  def add[SupT >: T](element: SupT): MyList[SupT] = ???
}
```
