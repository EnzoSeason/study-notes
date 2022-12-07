object Solution {
  def strStr(haystack: String, needle: String): Int = {
    val pmt = getPMT(needle)

    var i = 0
    var j = 0
    while (i < haystack.length && j < needle.length) {
      while (j > 0 && haystack(i) != needle(j)) {
        j = pmt(j - 1)
      }
      if (haystack(i) == needle(j)) {
        j += 1
      }
      i += 1
    }

    if (j == needle.length)  i - j
    else -1
  }

  /**
   * Create a Partial Match Table (PMT)
   * for the word we need to find in the string
   * 
   * pmt(i) indicates
   * word.substring(i + 1 - next(i), i + 1) is equal to 
   * word.substring(0, next(i))
   * E.g. word = "aabaaf", pmt = Array(0, 1, 0, 1, 2, 0)
   */
  def getPMT(word: String): Array[Int] = {
    val pmt = Array.fill(word.length)(0)

    var j = 0
    for (i <- 1 until word.length) {
      while (j > 0 && word(i) != word(j)) {
        j = pmt(j - 1)
      }
      // Either there is no same char in the previous sub-string (j == 0), or there is (word(i) == word(j))
      // If there is, that means word.substring(i - j, i + 1) is equal to word.substring(0, j + 1)
      // Therefore, pmt(i) = j + 1
      if (word(i) == word(j)) {
        j += 1
        pmt(i) = j
      } else {
        pmt(i) = 0
      }
    }

    pmt
  }
}