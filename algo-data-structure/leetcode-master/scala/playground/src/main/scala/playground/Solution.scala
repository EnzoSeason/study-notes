package playground

import scala.annotation.tailrec

object Solution {
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