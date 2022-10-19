package playground

import scala.annotation.tailrec

object Solution {
  def reverseStr(s: String, k: Int): String = {
    @tailrec
    def reverse(s: String, needToReverse: Boolean, history: String): String = {
      val subStr = if (needToReverse) s.take(k).reverse else s.take(k)
      if (s.length < k) history + subStr
      else reverse(s.drop(k), !needToReverse, history + subStr)
    }
    reverse(s, true, "")
  }
}