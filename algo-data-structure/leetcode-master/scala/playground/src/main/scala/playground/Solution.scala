package playground

object Solution {

  import scala.collection.mutable

  def subsets(nums: Array[Int]): List[List[Int]] = {
    val result = mutable.Stack[List[Int]]()
    val cache = mutable.Stack[Int]()

    def backtracking(i: Int): Unit = {
      if (i == nums.length) {
        result.push(cache.reverse.toList)
        return
      }
      backtracking(i + 1)
      cache.push(nums(i))
      backtracking(i + 1)
      cache.pop()
    }

    backtracking(0)
    result.toList
  }
}