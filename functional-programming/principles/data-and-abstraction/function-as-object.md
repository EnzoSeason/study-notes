# Function as Object

An **anonymous function** such as

```scala
(x: Int) => x * x
```

is expanded to an **anonymous class**

```scala
new Function1[Int, Int]{
  def apply(x: Int) = x * x
}
```

This class is thought of as a **block** that **defines and instantiates** a local class.

```scala
{
  class $anonfun() extends Function1[Int, Int] {
    def apply(x: Int) = x * x
  }
  $anonfun()
}
```

It's very useful.

For example, it makes **passing functions as parameters** possible. Function parameter will translate to **anonymous function**, then to **anonymous class**, and finally **be instantiates** as an object.
