object Solution {
  def maxSlidingWindow(nums: Array[Int], k: Int): Array[Int] = {
    val monoQueue = MonotonePriorityQueue()

    // init max heap
    for (i <- 0 until k) {
      monoQueue.add(nums(i))
    }

    var slow = 0
    var fast = k
    val result = new Array[Int](nums.length - k + 1)
    result(0) = monoQueue.top

    while (fast < nums.length) {
      monoQueue.remove(nums(slow))
      monoQueue.add(nums(fast))

      slow += 1
      fast += 1
      result(slow) = monoQueue.top
    }

    result
  }

  /**
    * The elements in this queue are are in desc order.
    * We only care about the head of this queue.
    */
  case class MonotonePriorityQueue() {
    import scala.collection.mutable

    private var _queue = mutable.ArrayBuffer[Int]()

    def add(elem: Int): Unit = {
      while (_queue.nonEmpty && _queue.last < elem) {
        _queue.remove(_queue.length - 1)
      }
      _queue.append(elem)
    }

    def remove(elem: Int): Unit = {
      if (_queue.nonEmpty && _queue.head == elem) {
        _queue.remove(0)
      }
    }

    def top: Int = _queue.head
  }
}