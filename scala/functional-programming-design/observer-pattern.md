# Observer pattern

The **subscriber**s listen to **publisher**s. Once there is a change,
publishers will notify subscribers.

```scala
trait Subscriber {
  def handle(publisher: Publisher): Unit
}

trait Publisher {
  private subscribers: Set[Subscriber] = Set()

  def subscribe(subscriber: Subscriber): Unit = {
    subscribers += subscriber
  }

  def unsubscribe(subscriber: Subscriber): Unit = {
    subscribers -= subscriber
  }

  def publish(): Unit = {
    subscribers.foreach(_.handle(this))
  }
}
```

Observer pattern provides a eazy way to **decouple** the view from state. However, it has some downsides.

- Forces imperative style. A lot of functions return `Unit` type.
- Concurrency makes things more complicated.

These downsides cause bugs.
