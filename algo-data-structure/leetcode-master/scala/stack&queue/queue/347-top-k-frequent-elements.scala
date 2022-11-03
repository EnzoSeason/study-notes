object SolutionPriorityQueue {
  import scala.collection.mutable

  def topKFrequent(nums: Array[Int], k: Int): Array[Int] = {
    // build the frequency map
    // key: num, value: frequency
    val freqMap = mutable.Map[Int, Int]()
    for (num <- nums) {
      freqMap += (num -> (freqMap.getOrElse(num, 0) + 1))
    }

    // build the priority queue
    // The priority queue here is a Min Heap. The number in the first pair has the lowest frequency.
    val priorityQueue = mutable.PriorityQueue[(Int, Int)]()(Ordering.by[(Int, Int), Int](_._2).reverse)
    for (pair <- freqMap) {
      priorityQueue.enqueue(pair)
      if (priorityQueue.size > k)
        priorityQueue.dequeue()
    }

    priorityQueue.map(_._1).toArray
  }
}

object SolutionMapReduce {
  // It's similar to WordCount problem. 
  def topKFrequent(nums: Array[Int], k: Int): Array[Int] = {
    nums
      .map((_, 1))
      .groupBy(_._1)
      .map {
        case (num, freqMap) => (num, freqMap.map(_._2).sum)
      }
      .toArray.sortBy(_._2).reverse
      .take(k)
      .map(_._1)
  }
}