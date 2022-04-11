## String

```scala
val str: String = "abcde,efg"
```

Scala accesses the `String` class of Java.

### Useful functions

- `charAt`: `str.charAt(1)` returns `b`.

- `subString`: `str.subString(1, 3)` returns `bc`.

- `split`: `str.split(",")` returns a **list** which contains `abcd` and `efg`.

- `startWith`: `str.startWith("abc")` returns `true`.

- `replace`: `str.replace(",", ";")` returns `abcde;efg`.

- `toLowerCase` and `toUpperCase`

### Interpolation

```scala
val name: String = "Jack"
val age: Int = 5
```

- `s` interpolator

   ```scala
   val message = s"It's $name. I'll be turning ${age + 1} years old."
   ```

- `f` interpolator: It can define the format.


   ```scala
   val speed: Float = 1.2f
   val message = f"$name%s's speed is $speed%2.2f meters per hour."
   ```

- `raw` interpolator

   ```scala
   val rawTxt = raw"change line \n"
   ```