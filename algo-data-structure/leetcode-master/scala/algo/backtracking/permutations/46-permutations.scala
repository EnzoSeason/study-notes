object Solution1 {

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

object Solution2 {

  import scala.collection.mutable

  def permute(nums: Array[Int]): List[List[Int]] = {
    val result = mutable.Stack[List[Int]]()
    val cache = mutable.Stack[Int]()

    def backtracking(visited: Array[Boolean]): Unit = {
      if (cache.length == nums.length) {
        result.push(cache.reverse.toList)
        return
      }
      for (i <- 0 until nums.length if !visited(i)) {
        cache.push(nums(i))
        visited(i) = true

        backtracking(visited)

        cache.pop()
        visited(i) = false
      }
    }

    backtracking(Array.fill(nums.length)(false))

    result.toList
  }
}
