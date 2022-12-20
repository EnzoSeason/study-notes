package playground

object Solution {

  import scala.collection.mutable

  def subsetsWithDup(nums: Array[Int]): List[List[Int]] = {
    val sortedNums = nums.sorted
    val result = mutable.Set[List[Int]]()
    val cache = mutable.Stack[Int]()

    def backtracking(startAt: Int): Unit = {
      result.add(cache.reverse.toList)

      for (i <- startAt until sortedNums.length) {
        cache.push(sortedNums(i))
        backtracking(i + 1)
        cache.pop()
      }
    }

    backtracking(0)
    result.toList
  }
}