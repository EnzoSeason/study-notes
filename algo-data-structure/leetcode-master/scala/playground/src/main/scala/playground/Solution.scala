package playground

import scala.annotation.tailrec

object Solution {
  def reverseStr(s: String, k: Int): String = {
    s.grouped(k)
      .zipWithIndex
      .map {
        case (subStr, index) => if (index % 2 == 0) subStr.reverse else subStr
      }
      .mkString
  }
}