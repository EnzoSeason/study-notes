## Tuple & Map

### Tuple

`Tuple` is immutable. It's just like that in Python.

```scala
val tuple = (1, "Hello")
```

To access member, Tuple has `_1` and `_2`

```scala
println(tuple._1) // 1
println(tuple._2) // Hello
```

We can copy a tuple, and replace the elements in copy.

```scala
println(tuple.copy(_2 = "Hi")) // (1, "Hi")
```

### Map

`Map` is the data structure that has `key` - `value`

```scala
val bank: Map[String, Int] = Map(("Jack", 100), "Jay" -> 200)
```

> `"Jay" -> 200` is equivalent to ("Jay", 200)

#### Basic operations

- check if the `key` exists

  ```scala
  println(bank.contains("Jack")) // true
  ```

- visit the `value` by `key`

  ```scala
  println(bank("Jack")) // 100
  ```

- add a pair

  Since `Map` is immutable, we need to create a new map.

  ```scala
  val newClient = "Mary" -> 300
  val newBank = bank + newClient
  ```

#### Functionals

- `map`

  ```scala
  val newBank = bank.map(pair => pair._1.toLowerCase() -> pair._2)
  ```

- `filterKeys`

  ```scala
  val jBank = bank.view.filterKeys(key => key.startsWith("J")).toMap;
  ```

- `mapValues`

  ```scala
  val richBank = bank.view.mapValues(value => value + 100).toMap;
  ```

### Conversion to other collections

- `toList`:

  ```scala
  bank.toList // List((Jack,100), (Alice,100))
  ```

- `toMap`:

  ```scala
  val list = List(("Dan", 100))
  println(list.toMap) // Map(Dan -> 100)
  ```

- `groupBy`: It transforms a list to map.

  ```scala
  val names = List("Jack", "Jay", "May", "Mark")
  val nameGroup = names.groupBy(name => name.charAt(0))
  // HashMap(J -> List(Jack, Jay), M -> List(May, Mark))
  ```
