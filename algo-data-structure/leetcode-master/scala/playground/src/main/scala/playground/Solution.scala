package playground

object Solution {
  def commonChars(words: Array[String]): List[String] = {
    val globalCache = Array.fill(26)(0)
    var result = List[String]()

    // init cache
    for (c <- words.head) {
      globalCache(c.toInt - 'a'.toInt) += 1
    }

    // update cache
    for (word <- words.tail) {
      val localCache = Array.fill(26)(0)
      for (c <- word) {
        localCache(c.toInt - 'a'.toInt) += 1
      }
      for (i <- 0 until 26) {
        globalCache(i) = math.min(globalCache(i), localCache(i))
      }
    }

    // generate the result from the cache
    for (i <- 0 until 26) {
      val count = globalCache(i)
      for (_ <- 0 until count) {
        val charCode = i + 'a'.toInt
        result :+= charCode.toChar.toString
      }
    }

    result
  }
}