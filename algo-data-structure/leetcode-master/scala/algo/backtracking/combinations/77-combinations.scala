object Solution {

  import scala.collection.mutable

  def combine(n: Int, k: Int): List[List[Int]] = {
    val result = mutable.Stack[List[Int]]()
    val acc = mutable.Stack[Int]()

    def backtracking(startAt: Int): Unit = {
      if (acc.length == k) {
        result.push(acc.toList)
      } else {
        for (i <- startAt to n - (k - acc.length) + 1) {
          acc.push(i)
          backtracking(i + 1)
          acc.pop()
        }
      }
    }

    backtracking(1)
    result.toList
  }
}