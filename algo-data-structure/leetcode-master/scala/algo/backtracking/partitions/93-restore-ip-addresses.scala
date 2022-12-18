object Solution {

  import scala.collection.mutable

  def restoreIpAddresses(s: String): List[String] = {
    if (s.length < 4 || s.length > 12) return Nil

    val result = mutable.Stack[String]()
    val cache = mutable.Stack[String]()

    def backtracking(startAt: Int): Unit = {
      if (cache.length > 4) {
        return
      }

      if (startAt == s.length && cache.length == 4) {
        result.push(cache.reverse.mkString("."))
        return
      }

      for (endAt <- startAt until startAt + 3 if endAt < s.length && isValidNumber(startAt, endAt)) {
        cache.push(s.substring(startAt, endAt + 1))
        backtracking(endAt + 1)
        cache.pop()
      }
    }

    def isValidNumber(start: Int, end: Int): Boolean = {
      if (start != end && s(start) == '0') return false
      if (s.substring(start, end + 1).toInt > 255) false
      else true
    }

    backtracking(0)
    result.toList
  }
}