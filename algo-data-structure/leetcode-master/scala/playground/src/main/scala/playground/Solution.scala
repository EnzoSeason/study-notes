package playground

object Solution {

  import scala.collection.mutable

  def subsetsWithDup(nums: Array[Int]): List[List[Int]] = {
    val sortedNums = nums.sorted
    val result = mutable.Stack[List[Int]]()
    val cache = mutable.Stack[Int]()

    def backtracking(startAt: Int): Unit = {
      result.push(cache.reverse.toList)

      val visited = mutable.Set[Int]()
      for (i <- startAt until sortedNums.length if !visited(sortedNums(i))) {
        cache.push(sortedNums(i))
        visited.add(sortedNums(i))

        backtracking(i + 1)

        cache.pop()
      }
    }

    backtracking(0)
    result.toList
  }
}