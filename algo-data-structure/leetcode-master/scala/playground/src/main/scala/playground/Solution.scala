package playground

object Solution {
  def twoSum(nums: Array[Int], target: Int): Array[Int] = {
    var cache = Map[Int, Int]()

    for (i <- 0 until nums.length) {
      cache.get(target - nums(i)) match {
        case Some(j) => return Array(j, i)
        case _ => cache += (nums(i) -> i)
      }
    }
    Array[Int]()
  }
}