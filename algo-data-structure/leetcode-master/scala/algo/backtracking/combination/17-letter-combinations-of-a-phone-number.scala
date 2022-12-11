object Solution {

  import scala.collection.mutable

  def letterCombinations(digits: String): List[String] = {
    val mapping = Map[Char, List[Char]](
      '2' -> List('a', 'b', 'c'),
      '3' -> List('d', 'e', 'f'),
      '4' -> List('g', 'h', 'i'),
      '5' -> List('j', 'k', 'l'),
      '6' -> List('m', 'n', 'o'),
      '7' -> List('p', 'q', 'r', 's'),
      '8' -> List('t', 'u', 'v'),
      '9' -> List('w', 'x', 'y', 'z')
    )
    val result = mutable.Stack[String]()
    val cache = mutable.Stack[Char]()

    def backtracking(startAt: Int): Unit = {
      if (startAt == digits.length) {
        result.push(cache.reverse.mkString)
        return
      }
      val letters = mapping(digits(startAt))
      for (c <- letters) {
        cache.push(c)
        backtracking(startAt + 1)
        cache.pop()
      }
    }

    // Main Program
    
    if (digits.isEmpty) return List()
    
    backtracking(0)
    result.toList
  }
}