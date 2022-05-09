# Lazy list

We want to **avoid computing** the elements of a sequence **until they are needed** for the evaluation result. Here, "needed" means the `head` or `tail` of the list is called.

Therefore, the lazy list is created.

## Defining a lazy list

- `LazyList.empty`: Similar to `Nil` in the list
- `LazyList.cons` or `#::`: Similar to `::` in the list

```scala
val xs = LazyList.cons(1, LazyList.cons(2, LazyList.empty))
```

We can also use `LazyList` as a factory.

```scala
val xs = LazyList(1, 2)
```

We can use `to` function to translate a list to a lazy list.

```scala
val xs = (0 until 1000).to(LazyList)
```

## Example: TailLazyList

```scala
trait TailLazyList[+A] extends Seq[A]:
  def isEmpty: Boolean
  def head: A
  def tail: TailLazyList[A]

object TailLazyList:
  def cons[T](hd: T, tl :=> TailLazyList[T]) = 
    new TailLazyList[T]:
      def isEmpty = false
      def head = hd
      def tail = tl
      override def toString = "TailLazyList(" + hd + ", ?)"
  
  def empty = new TailLazyList[Nothing]:
    def isEmpty = true
    def head = throw NoSuchElementException("Empty list has no head")
    def tail = throw NoSuchElementException("Empty list has no tail")
    override def toString = "TailLazyList()"
```