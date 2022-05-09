# Options

An **option** is a wrapper for a value that **might be present or not**.

```scala
sealed abstract class Option[+A]

// The class Some wraps a concrete value
case class Some[+A](x: A) extends Option[+A]

// The class None is a singleton for absent value
case object None extends Option[Nothing]
```

For example

```scala
val myOption: Option[Int] = Some(1)
val noOption: Option[Int] = None
```

## Unsafe API

Option is very useful for **unsafe APIs**. It does the **Null check** for us.

If we **work with unsafe APIs**:

```scala
def unsafeMethod(): String = null
val result = Option(unsafeMethod()) // Some or None
```

Option makes sure we receive either `Some` or `None`. What's more, we can define a default value with the chained method, `orElse`.

```scala
def backupMethod(): String = "default"
val result = Option(unsafeMethod()).orElse(backupMethod())
```

If we **design unsafe APIs**, we always return **Option**.

```scala
def unsafeMethod(): Option[String] = None
def def backupMethod(): Option[String] = Some("default")
```

So that, we can better use them:

```scala
val result = unsafeMethod() orElse backupMethod()
```

## Functions on Option

```scala
val numOption: Option[Int] = Some(1)
```

- `isEmpty`

  ```scala
  println(numOption.isEmpty) // false
  ```

- `map`

  ```scala
  println(numOption.map(num => num * 2)) // Some(2)
  ```

- `flatMap`

  ```scala
  println(numOption.flatMap(num => Option(num * 10))) // Some(10)
  ```

- `filter`

  ```scala
  println(numOption.filter(num => num > 10)) // None
  ```

- `get`: It gets the value of `Option`. Avoid using it.

## Exercise

Create a `connection` if `host` and `port` are given.

```scala
val config: Map[String, String] = Map(
  "host" -> "127.0.0.1",
  "port" -> "8080"
)

class Connection {
  def connect() = "Connected"
}
object Connection {
  val random = new Random(System.nanoTime())

  def apply(host: String, port: String) = {
    if (random.nextBoolean()) Some(new Connection)
    else None
  }
}
```

### Normal call

```scala
val host = config.get("host")
val port = config.get("port")
val connection: Option[Connection] = {
  if (!host.isEmpty && !port.isEmpty)
    Connection(host.get, port.get)
  else None
}

val status = connection.map(conn => conn.connect())
status.foreach(println)
```

### Chained call

```scala
val status = config
  .get("host")
  .flatMap(
    host => config
      .get("port")
      .flatMap(port =>
        Connection(host, port)))
  .map(conn => conn.connect())

status.foreach(println)
```

### For Comprehensions call

```scala
val status = for {
  host <- config.get("host")
  port <- config.get("port")
  conn <- Connection(host, port)
} yield conn.connect()

status.foreach(println)
```
