package playground

import scala.annotation.tailrec

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
   * Create a Partial Match Table (PMT)
   * for the word we need to find in the string
   *
   * In a word: NextTable = -1 :: PartialMatchTable
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