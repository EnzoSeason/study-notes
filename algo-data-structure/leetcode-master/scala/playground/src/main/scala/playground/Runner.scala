package playground

object Runner extends App {
  val solution = Solution

  val values1: Array[Any] = Array(0)
  println(solution.isValidBST(Tree(values1).build()))
}
