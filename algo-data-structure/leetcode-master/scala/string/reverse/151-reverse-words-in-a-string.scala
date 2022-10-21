object SolutionCache {
  def reverseWords(s: String): String = {
    var cache = List[String]()

    var i = 0
    while (i < s.length) {
      while (i < s.length && s(i) == ' ') i+= 1
      
      var j = i
      while (j < s.length && s(j) != ' ') j+= 1

      if (i != j) cache ::= s.substring(i, j)
      i = j
    }
    cache.mkString(" ")
  }
}

object SolutionInPlace {
  def reverseWords(s: String): String = {
    val cleanSentence = removeExtraSpace(s.toArray)
    reverseInPlace(cleanSentence, 0, cleanSentence.length - 1)

    var i = 0
    while (i < cleanSentence.length) {
      var j = i
      while (j < cleanSentence.length && cleanSentence(j) != ' ') j += 1
      reverseInPlace(cleanSentence, i, j - 1)

      i = j + 1
    }

    cleanSentence.mkString
  }

  def reverseInPlace(sentence: Array[Char], beginIndex: Int, endIndex: Int): Unit = {
    var left = beginIndex
    var right = endIndex
    while (left < right) {
      val tmp = sentence(left)
      sentence(left) = sentence(right)
      sentence(right) = tmp

      left += 1
      right -= 1
    }
  }

  def removeExtraSpace(sentence: Array[Char]): Array[Char] = {
    var slow = 0
    var fast = 0

    while (sentence(fast) == ' ') fast += 1

    while (fast < sentence.length) {
      if (fast > 0 && sentence(fast - 1) == ' ' && sentence(fast) == ' ') fast += 1
      else {
        sentence(slow) = sentence(fast)
        slow += 1
        fast += 1
      }
    }

    if (slow > 0 && sentence(slow - 1) == ' ') sentence.take(slow - 1)
    else sentence.take(slow)
  }
}