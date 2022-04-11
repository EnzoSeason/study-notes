## Packaging

The classes in the **same package** are visiable to each other, and **accessable by their names**.

The classes in the **different packages** are not accessable unless we **import** them or use the **fully qualified name**.

```scala
package prj1.demo1

import prj2.demo2

object Demo1 extends App {
  val demo2 = new Demo2Test
  val demo3 = new prj3.Demo3Test
}
```

### Package Object

It's created for **universal constants or methods** for a package.

Each package has only **ONE** package object.

### Import

```scala
import java.util.Date

val date = new Date
```

If you want to use `java.sql.Date` at the same time, there are 2 ways.

1. use **fully qualified name**

   ```scala
   val sqlDate = new java.sql.Date(2021, 12, 28)
   ```

2. use **aliasing**

    ```scala
    import java.sql.{Date => SqlDate}
    ```
  
#### Multiple Imports

You can import **multiple classes from the same package** by:

```scala
import zoo.{Cat, Dog}
```

#### Default Imports

- `java.lang`: `String`, `Object`, `Exception`, etc
- `scala`: `Int`, `Nothing`, `Function`, etc
- `scala.Predef`: `println`, `???`, etc