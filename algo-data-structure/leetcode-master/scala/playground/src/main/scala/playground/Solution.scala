package playground

import scala.annotation.tailrec

object Solution {
  def isValid(s: String): Boolean = {
    val matchingTable = Map(
      ')' -> '(',
      ']' -> '[',
      '}' -> '{'
    )

    val stack = scala.collection.mutable.Stack[Int]()

    for (c <- s) {
      matchingTable.get(c) match {
        case Some(value) => {
          if (stack.nonEmpty && stack.top == value) stack.pop()
          else return false
        }
        case None => stack.push(c)
      }
    }

    stack.isEmpty
  }
}