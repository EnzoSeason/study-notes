object SolutionStack {
  def build(s: String): String = {
    val stack = new Array[Char](s.length)
    var i = 0

    for (char <- s) {
      // Attention:
      // "#" is a String, while '#' is a Char.
      if (char != '#') {
        stack(i) = char
        i += 1
      } else {
        if (i > 0) i -= 1
      }
    }
    stack.take(i).mkString
  }

  def backspaceCompare(s: String, t: String): Boolean = {
    build(s) == build(t)
  }
}

object SolutionTwoPointers {
  def moveTo(s: String, startAt: Int): Int = {
    var skipCount = 0
    var i = startAt

    while (i >= 0) {
      if (s.charAt(i) == '#') {
        skipCount += 1
        i -= 1
      } else if (skipCount > 0) {
        skipCount -= 1
        i -= 1
      } else {
        return i
      }
    }
    i
  }

  def backspaceCompare(s: String, t: String): Boolean = {
    var tailS = s.length - 1
    var tailT = t.length - 1

    while (tailS >= 0 || tailT >= 0) {
      tailS = moveTo(s, tailS)
      tailT = moveTo(t, tailT)

      if ((tailS >= 0) != (tailT >= 0)) return false

      if (tailS >= 0 && tailT >= 0 && s.charAt(tailS) != t.charAt(tailT)) return false

      tailS -= 1
      tailT -= 1
    }
    true
  }
}

