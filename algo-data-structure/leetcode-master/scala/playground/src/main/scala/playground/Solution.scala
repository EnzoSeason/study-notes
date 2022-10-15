package playground

object Solution {
  def commonChars(words: Array[String]): List[String] = {
    val sortedWords = words.sortBy(_.length)
    var cache = Map[Char, Int]()
    var result = List[String]()

    // init the cache with the first word
    for (c <- sortedWords.head) {
      cache.get(c) match {
        case Some(value) => cache += (c -> (value + 1))
        case None => cache += (c -> 1)
      }
    }

    for (i <- 1 until sortedWords.length) {
      val word = sortedWords(i)
      var localCache = Map[Char, Int]()
      for (c <- word) {
        localCache.get(c) match {
          case Some(value) => localCache += (c -> (value + 1))
          case None => localCache += (c -> 1)
        }
      }
      for ((k, v) <- cache) {
        localCache.get(k) match {
          case Some(value) => cache += (k -> Math.min(value, v))
          case None => cache -= k
        }
      }
    }

    for ((k, v) <- cache) {
      for (_ <- 0 until v) {
        result :+= k.toString
      }
    }

    result
  }
}