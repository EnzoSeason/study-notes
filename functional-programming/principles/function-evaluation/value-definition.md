# Value Definition

- `val` indicates **call-by-value**

  For example

  ```scala
  val y = square(2)
  ```

  From now on, `y` is `4`, not `square(2)`.

- `def` indicates **call-by-name**

```scala
def loop: Boolean = loop

def x = loop // OK, call-by-name

val y = loop // inifinite loop, call-by-value
```
