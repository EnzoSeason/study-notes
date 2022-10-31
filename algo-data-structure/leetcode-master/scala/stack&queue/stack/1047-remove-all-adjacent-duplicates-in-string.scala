object Solution {
  def removeDuplicates(s: String): String = {
    val stack = scala.collection.mutable.Stack[Char]()

    for (c <- s) {
      if (stack.nonEmpty && stack.top == c) stack.pop()
      else stack.push(c)
    }

    stack.mkString.reverse
  }
}