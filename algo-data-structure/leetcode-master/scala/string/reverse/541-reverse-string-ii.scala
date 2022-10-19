import scala.annotation.tailrec

object SolutionRec {
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

object SolutionFunc {
  def reverseStr(s: String, k: Int): String = {
    // s = "abcdefg", k = 2
    s.grouped(k) // Iterator ["ab", "cd", "ef", "g"]
      .zipWithIndex // Iterator [("ab", 0), ("cd", 1), ("ef", 2), ("g", 3)]
      .map {
        case (subStr, index) => 
          if (index % 2 == 0) subStr.reverse else subStr
      }
      .mkString
  }
}