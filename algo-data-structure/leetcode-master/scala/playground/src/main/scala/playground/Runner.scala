package playground

object Runner extends App {
  val solution = Solution

  val values1: Array[Any] = Array(1,null,5,3)
  println(solution.getMinimumDifference(Tree(values1).build()))
}
