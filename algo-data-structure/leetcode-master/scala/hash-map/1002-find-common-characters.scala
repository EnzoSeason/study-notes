object SolutionArrayCache {
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

object SolutionMapCache {
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
      
      // init the local cache
      for (c <- word) {
        localCache.get(c) match {
          case Some(value) => localCache += (c -> (value + 1))
          case None => localCache += (c -> 1)
        }
      }
      
      // compare the local cache with the global one
      for ((k, v) <- cache) {
        localCache.get(k) match {
          case Some(value) => cache += (k -> Math.min(value, v))
          case None => cache -= k
        }
      }
    }
    
    // generate the result
    for ((k, v) <- cache) {
      for (_ <- 0 until v) {
        result :+= k.toString
      }
    }

    result
  }
}