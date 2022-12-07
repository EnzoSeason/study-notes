object Solution {
  def minWindow(s: String, t: String): String = {
    if (s.length < t.length) return ""

    val target = collection.mutable.Map[Char, Int]()
    for (char <- t) {
      target(char) = target.getOrElse(char, 0) + 1
    }

    val slidingWindow = collection.mutable.Map[Char, Int]()
    var minLen = Int.MaxValue
    var start = 0
    var end = 0

    var left = 0
    var right = 0
    var matchCount = 0

    while (right < s.length) {
      slidingWindow(s(right)) = slidingWindow.getOrElse(s(right), 0) + 1
      if (target.contains(s(right)) && slidingWindow(s(right)) == target(s(right))) {
        matchCount += 1
      }

      while (left <= right && matchCount == target.size) {
        if (right - left + 1 < minLen) {
          minLen = right - left + 1
          start = left
          end = right
        }
        slidingWindow(s(left)) -= 1
        if (target.contains(s(left)) && slidingWindow(s(left)) < target(s(left))) {
          matchCount -= 1
        }
        left += 1
      }

      right += 1
    }

    if (minLen != Int.MaxValue) s.slice(start, end + 1)
    else ""
  }
}