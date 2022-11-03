package playground

object Solution {
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