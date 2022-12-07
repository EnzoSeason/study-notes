object Solution {
  import scala.util.{Failure, Success, Try}
  
  def evalRPN(tokens: Array[String]): Int = {
    val stack = scala.collection.mutable.Stack[Int]()
    val operations = Set("+", "-", "*", "/")

    for (token <- tokens) {
      if (operations contains token) {
        val secondNum = stack.pop()
        val firstNum = stack.pop()
        val result = token match {
          case "+" => firstNum + secondNum
          case "-" => firstNum - secondNum
          case "*" => firstNum * secondNum
          case "/" => firstNum / secondNum
        }
        stack.push(result)
      } else {
        Try(token.toInt) match {
          case Success(num) => stack.push(num)
          case Failure(exception) =>
        }
      }
    }

    stack.pop()
  }
}

object SolutionRec {
  def evalRPN(tokens: Array[String]): Int = {
    // global variables
    val operations = Set("+", "-", "*", "/")
    var index = tokens.length

    // postorder traversal
    def eval(): Int = {
      index -= 1
      val token = tokens(index)
      if (operations contains token) {
        val secondNum = eval()
        val firstNum = eval()
        token match {
          case "+" => firstNum + secondNum
          case "-" => firstNum - secondNum
          case "*" => firstNum * secondNum
          case "/" => firstNum / secondNum
        }
      } else token.toInt
    }

    eval()
  }
}