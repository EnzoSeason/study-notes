package playground

object Solution {
  def findAnagrams(s: String, p: String): List[Int] = {
    if (s.length < p.length) return List[Int]()

    val target = Array.fill(26)(0)
    val search = Array.fill(26)(0)
    var result = List[Int]()

    for (i <- 0 until p.length) {
      search(s.charAt(i).toInt - 'a'.toInt) += 1
      target(p.charAt(i).toInt - 'a'.toInt) += 1
    }

    for (i <- 0 until (s.length - p.length - 1)) {
      if (search.sameElements(target)) result ::= i

      if (i + p.length == s.length) return result.reverse

      search(s.charAt(i).toInt - 'a'.toInt) -= 1
      search(s.charAt(i + p.length) - 'a'.toInt) += 1
    }

    result.reverse
  }
}