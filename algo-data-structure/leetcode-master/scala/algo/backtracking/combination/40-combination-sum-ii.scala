object Solution {

  import scala.collection.mutable

  def combinationSum2(candidates: Array[Int], target: Int): List[List[Int]] = {
    val result = mutable.Stack[List[Int]]()
    val cache = mutable.Stack[Int]()
    val sortedCandidates = candidates.sorted // sort in the order ASC

    def backtracking(startAt: Int): Unit = {
      val localSum = cache.sum

      if (localSum == target) {
        result.push(cache.toList)
        return
      }
      if (localSum > target) {
        return
      }

      // check to sum before backtracking
      for (i <- startAt until sortedCandidates.length if sortedCandidates(i) + localSum <= target) {
        if (i > startAt && candidates(i) != candidates(i - 1)) {
          cache.push(sortedCandidates(i))
          backtracking(i)
          cache.pop()
        }
      }
    }

    backtracking(0)
    result.toList
  }
}