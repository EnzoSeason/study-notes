object SolutionCacheMap1 {
  def groupAnagrams(strs: Array[String]): List[List[String]] = {
    var cache = Map[Map[Char, Int], List[String]]()
    var result = List[List[String]]()

    for (s <- strs) {
      var localCache = Map[Char, Int]()
      for (c <- s) {
        localCache.get(c) match {
          case Some(count) => localCache = localCache + (c -> (count + 1))
          case None => localCache = localCache + (c -> 1)
        }
      }
      cache.get(localCache) match {
        case Some(l) => cache = cache + (localCache -> (s :: l))
        case None => cache = cache + (localCache -> (s :: Nil))
      }
    }
    
    cache.values.toList
  }
}

object SolutionCacheMap2 {
  def groupAnagrams(strs: Array[String]): List[List[String]] = {
    var cache = Map[String, List[String]]()

    for (s <- strs) {
      val key = s.toList.sorted.toString()
      cache.get(key) match {
        case Some(l) => cache = cache + (key -> (s :: l))
        case None => cache = cache + (key -> (s :: Nil))
      }
    }

    cache.values.toList
  }
}