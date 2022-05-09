# Map

```scala
val romanNumerals = Map("I" -> 1, "V" -> 5, "X" -> 10)
```

The syntax `key -> value` is just another way to write the pair `(key, value)`.

- `Map` is the subclass of `Iterable`.

  ```scala
  romanNumerals.map((x, y) => (y, x))
  ```

- `Map` is function.

  ```scala
  romanNumerals("I") // 1
  ```

  However, it will throw an error if the key is not found. The better way to query is:

  ```scala
  romanNumerals.get("I") // Some(1)
  romanNumerals.get("aaa") // None
  ```

  > `Some` and `None` are the subclass of `Option`.


## Updating a Map

- `m + (k -> v)`
- `m ++ kvs`
