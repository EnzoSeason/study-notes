class MyQueue() {
  import scala.collection.mutable

  private val _stack = mutable.Stack[Int]()
  private val _cacheStack = mutable.Stack[Int]()

  def push(x: Int): Unit = {
    _stack.push(x)
  }

  def pop(): Int = {
    if (_cacheStack.nonEmpty) _cacheStack.pop()
    else {
      while (_stack.nonEmpty) {
        _cacheStack.push(_stack.pop())
      }
      _cacheStack.pop()
    }
  }

  def peek(): Int = {
    var result = pop()
    _cacheStack.push(result)
    result
  }

  def empty(): Boolean = _stack.isEmpty && _cacheStack.isEmpty
}