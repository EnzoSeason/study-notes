class MyStack() {

  private val _queue = scala.collection.mutable.Queue[Int]()

  def push(x: Int): Unit = {
    _queue.enqueue(x)
  }

  def pop(): Int = {
    for (_ <- 0 until _queue.size - 1) {
      _queue.enqueue(_queue.dequeue())
    }

    _queue.dequeue()
  }

  def top(): Int = {
    val result = pop()
    _queue.enqueue(result)
    result
  }

  def empty(): Boolean = _queue.isEmpty

}