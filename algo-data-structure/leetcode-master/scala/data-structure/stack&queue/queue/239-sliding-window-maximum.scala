object Solution {
  def maxSlidingWindow(nums: Array[Int], k: Int): Array[Int] = {
    val maxHeap = MaxHeap()

    // init max heap
    for (i <- 0 until k) {
      maxHeap.add(nums(i))
    }

    var slow = 0
    var fast = k
    val result = new Array[Int](nums.length - k + 1)
    result(0) = maxHeap.top

    while (fast < nums.length) {
      maxHeap.remove(nums(slow))
      maxHeap.add(nums(fast))

      slow += 1
      fast += 1
      result(slow) = maxHeap.top
    }

    result
  }

  case class MaxHeap() {

    import scala.collection.mutable

    private val _queue = mutable.ArrayBuffer[Int]()

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