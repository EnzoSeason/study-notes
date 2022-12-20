object Solution1 {
  // result is a Set instead of a Stack

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

object Solution2 {
  // use sorted numbers
  // skip used number by comparing with the previous one

  import scala.collection.mutable

  def subsetsWithDup(nums: Array[Int]): List[List[Int]] = {
    val sortedNums = nums.sorted
    val result = mutable.Stack[List[Int]]()
    val cache = mutable.Stack[Int]()

    def backtracking(startAt: Int): Unit = {
      result.push(cache.reverse.toList)

      for (
        i <- startAt until sortedNums.length
        if i == startAt || sortedNums(i) != sortedNums(i - 1)
      ) {
        cache.push(sortedNums(i))
        backtracking(i + 1)
        cache.pop()
      }
    }

    backtracking(0)
    result.toList
  }
}
