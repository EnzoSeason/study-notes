package playground

object Solution {

  import scala.collection.mutable

  def subsets(nums: Array[Int]): List[List[Int]] = {
    val result = mutable.Stack[List[Int]]()
    val cache = mutable.Stack[Int]()

    def backtracking(i: Int): Unit = {
      result.push(cache.reverse.toList)

//      if (i == nums.length) {
//        return
//      }

      for (j <- i until nums.length) {
        cache.push(nums(j))
        backtracking(j + 1)
        cache.pop()
      }
    }

    backtracking(0)
    result.toList
  }
}