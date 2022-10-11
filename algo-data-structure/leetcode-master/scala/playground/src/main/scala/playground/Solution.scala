package playground

object Solution {
  def findAnagrams(s: String, p: String): List[Int] = {
    if (s.length < p.length) return List[Int]()

    val target = p.toList.sorted
    var result = List[Int]()

    var i = 0
    while (i + target.length < s.length) {
      val subList = s.slice(i, i + target.length).toList.sorted
      if (subList == target) result = i :: result
      i += 1
    }

    result.reverse
  }
}