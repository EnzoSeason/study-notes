object SolutionPMT {
  def repeatedSubstringPattern(s: String): Boolean = {
    val pmt = Array.fill(s.length)(0)

    var j = 0
    for (i <- 1 until s.length) {
      while (j > 0 && s(i) != s(j)) j = pmt(j - 1)

      if (s(i) != s(j)) pmt(i) = 0
      else {
        j += 1
        pmt(i) = j
      }
    }

    val n = s.length
    pmt.last != 0 && n % (n - pmt.last) == 0
  }
}

object SolutionNext {
  def repeatedSubstringPattern(s: String): Boolean = {
    val nextTable = Array.fill(s.length + 1)(-1)

    var j = -1
    for (i <- 0 until s.length) {
      while (j >= 0 && s(i) != s(j)) j = nextTable(j)
      j += 1
      nextTable(i + 1) = j
    }

    val n = s.length
    nextTable.last != 0 && n % (n - nextTable.last) == 0
  }
}