package playground

object Solution {

  import scala.collection.mutable

  def combinationSum(candidates: Array[Int], target: Int): List[List[Int]] = {
    val result = mutable.Stack[List[Int]]()
    val cache = mutable.Stack[Int]()
    val sortedCandidates = candidates.sorted

    def backtracking(startAt: Int): Unit = {
      val localSum = cache.sum

      if (localSum == target) {
        result.push(cache.toList)
        return
      }
      if (localSum > target) {
        return
      }

      for (i <- startAt until sortedCandidates.length if sortedCandidates(i) + localSum <= target) {
        cache.push(sortedCandidates(i))
        backtracking(i)
        cache.pop()
      }
    }

    backtracking(0)
    result.toList
  }
}