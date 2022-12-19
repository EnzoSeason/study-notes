object Solution {

  import scala.collection.mutable

  def combinationSum3(k: Int, n: Int): List[List[Int]] = {
    val result = mutable.Stack[List[Int]]()
    val cache = mutable.Stack[Int]()

    def backtracking(startAt: Int): Unit = {
      if (cache.sum > n) return
      
      if (cache.length == k && cache.sum == n) {
        result.push(cache.toList)
      }
      else {
        for (i <- startAt to 9) {
          cache.push(i)
          backtracking(i + 1)
          cache.pop()
        }
      }
    }

    backtracking(1)
    result.toList
  }
}