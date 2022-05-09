# For-comprehension

## Query with For

Suppose that we have a database books, represented as a list of `Book`.

```scala
case class Book(title: String, authors: List[String])

val books: List[Book] = List(
  Book(title = "Intro", authors = List("Bird", "Jack"))
  Book(title = "Apple", authors = List("Jobs", "Cook"))
)
```

- To find the titles of books whose author's name is "Bird":

  ```scala
  for {
    b <- books
    a <- b.authors
    if a.toLowerCase == "bird"
  } yield b.title
  ```

- To find the names of the authors who write at least two books.

  ```scala
  for {
    b1 <- books
    b2 <- books
    if b1 != b2
    a1 <- b1.authors
    a2 <- b2.authors
    if a1.toLowerCase == a2.toLowerCase
  } yield a1
  ```

  However, it causes a **duplication problem**. For example, f an author writes 2 books, `a`, `b`, his names will be printed 2 times. Because there are 2 combinations, `(a, b), (b, a)`.

  To solve this problem, there are two ways.

  - use `Set` instead of `List`

    ```scala
    for {
      b1 <- books.toSet
      b2 <- books
      if b1 != b2
      a1 <- b1.authors
      a2 <- b2.authors
      if a1.toLowerCase == a2.toLowerCase
    } yield a1
    ```

  - use `distinct` method

    ```scala
    val authors = for {
      b1 <- books
      b2 <- books
      if b1.title < b2.title
      a1 <- b1.authors
      a2 <- b2.authors
      if a1.toLowerCase == a2.toLowerCase
    } yield a1

    authors.distinct
    ```

## Translation of For

For-comprehension is a syntax surgar for higher-order-functions. It can be translated in **higher-order-functions**

- map

  ```scala
  for x <- e1 yield e2
  // equivalent
  e2.map(x => e2)
  ```

- filter

  ```scala
  for x <- e1 if f yield e2
  // equivalent
  for x <- e1.withFilter(f) yield e2
  ```

- flatMap

  ```scala
  for x <- e1; y <- e2 yield e3
  // equivalent
  e1.flatMap(x => for y <- e2 yield e3)
  ```

So the following for-comprehension,

```scala
for {
  b <- books
  a <- b.authors
  if a.toLowerCase == "bird"
} yield b.title
```

It can be translated into,

```scala
book.flatMap(
  b => b.authors.withFilter(a => a.toLowerCase == "bird")
        .map(a => b.title))
```

In conclusion, all the class that support the method

- `map`
- `flatMap`
- `withFilter`

can use **for-comprehension**.
