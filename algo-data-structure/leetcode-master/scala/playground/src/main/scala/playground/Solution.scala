package playground

object Solution {

  import scala.collection.mutable

  def permute(nums: Array[Int]): List[List[Int]] = {
    val result = mutable.Stack[List[Int]]()
    val cache = mutable.Stack[Int]()

    def backtracking(): Unit = {
      if (cache.length == nums.length) {
        result.push(cache.reverse.toList)
        return
      }
      for (item <- nums if !cache.contains(item)) {
        cache.push(item)
        backtracking()
        cache.pop()
      }
    }

    backtracking()
    result.toList
  }
}