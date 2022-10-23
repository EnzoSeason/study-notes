object Solution {
  def strStr(haystack: String, needle: String): Int = {
    val nextTable = getNextTable(needle)

    var i = 0
    var j = 0
    while (i < haystack.length && j < needle.length) {
      while (j >= 0 && haystack(i) != needle(j)) {
        j = nextTable(j)
      }

      j += 1
      i += 1
    }

    if (j == needle.length) i - j
    else -1
  }

  /**
   * Create a next table
   * for the word we need to find in the string
   *
   * In a word: NextTable = -1 :: PartialMatchTable
   * E.g. word = "aabaaf", pmt = Array(-1, 0, 1, 0, 1, 2, 0)
   * It's easier to build the array (j = nextTable(j) instead of j = pmt(j - 1))
   */
  def getNextTable(word: String): Array[Int] = {
    val nextTable = Array.fill(word.length + 1)(-1)

    var j = -1
    for (i <- 0 until word.length) {
      while (j >= 0 && word(i) != word(j)) {
        j = nextTable(j)
      }

      j += 1
      nextTable(i + 1) = j
    }

    nextTable
  }
}