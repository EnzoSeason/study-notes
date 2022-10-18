package playground

import scala.annotation.tailrec

object Solution {
  def canConstruct(ransomNote: String, magazine: String): Boolean = {
    var cache = Array.fill(26)(0)

    for (c <- magazine)  {
      cache(c.toInt - 'a'.toInt) += 1
    }

    for (c <- ransomNote) {
      val i = c.toInt - 'a'.toInt
      if (cache(i) == 0) return false
      cache(i) -= 1
    }

    true
  }
}