object SolutionMapCache {
  def isAnagram(s: String, t: String): Boolean = {
    var cache = Map[Char, Int]()

    for (c <- s) {
      cache.get(c) match {
        case Some(count) => cache = cache + (c -> (count + 1))
        case None => cache = cache + (c -> 1)
      }
    }

    for (c <- t) {
      cache.get(c) match {
        case Some(count) => {
          if (count == 1) cache = cache - c
          else cache = cache + (c -> (count - 1))
        }
        case None => return false
      }
    }

    cache.size == 0
  }
}

object SolutionArrayCache {
  def isAnagram(s: String, t: String): Boolean = {
    // 如果两个字符串的长度不等，直接返回false
    if (s.length != t.length) return false
    
    val record = new Array[Int](26) // 记录每个单词出现了多少次
    
    // 遍历字符串，对于s字符串单词对应的记录+=1，t字符串对应的记录-=1
    for (i <- 0 until s.length) {
      record(s(i) - 97) += 1
      record(t(i) - 97) -= 1
    }
    
    // 如果不等于则直接返回false
    for (i <- 0 until 26) {
      if (record(i) != 0) {
        return false
      }
    }
    
    // 如果前面不返回false，说明匹配成功，返回true，return可以省略
    true
  }
}