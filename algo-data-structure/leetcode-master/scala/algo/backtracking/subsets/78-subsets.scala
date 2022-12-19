object Solution1 {

  import scala.collection.mutable

  def subsets(nums: Array[Int]): List[List[Int]] = {
    val result = mutable.Stack[List[Int]]()
    val cache = mutable.Stack[Int]()

    def backtracking(i: Int): Unit = {
      if (i == nums.length) {
        result.push(cache.reverse.toList)
        return
      }
      // don't pick the current number
      backtracking(i + 1)
      // pick the current number
      cache.push(nums(i))
      backtracking(i + 1)
      cache.pop()
    }

    backtracking(0)
    result.toList
  }
}

object Solution2 {

  import scala.collection.mutable

  def subsets(nums: Array[Int]): List[List[Int]] = {
    val result = mutable.Stack[List[Int]]()
    val cache = mutable.Stack[Int]()

    def backtracking(i: Int): Unit = {
      result.push(cache.reverse.toList)
      
    //  if (i == nums.length) {
    //    return
    //  }
      
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