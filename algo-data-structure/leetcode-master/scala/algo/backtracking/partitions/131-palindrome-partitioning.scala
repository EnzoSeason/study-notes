object Solution {

  import scala.collection.mutable

  def partition(s: String): List[List[String]] = {
    val result = mutable.Stack[List[String]]()
    val cache = mutable.Stack[String]()

    def backtracking(startAt: Int): Unit = {
      if (startAt == s.length) {
        result.push(cache.reverse.toList)
        return
      }

      for (endAt <- startAt until s.length if isPalindrome(startAt, endAt)) {
        val word = s.substring(startAt, endAt + 1)
        cache.push(word)
        backtracking(endAt + 1)
        cache.pop()
      }
    }

    def isPalindrome(left: Int, right: Int): Boolean = {
      var (i, j) = (left, right)
      while (i < j) {
        if (s(i) != s(j)) return false
        i += 1
        j -= 1
      }
      true
    }

    backtracking(0)
    result.toList
  }
}