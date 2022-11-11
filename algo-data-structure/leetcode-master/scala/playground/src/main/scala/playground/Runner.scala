package playground

object Runner extends App {
  val solution = Solution

  val values1: Array[Any] = Array(1,2,3,null,5)
  println(solution.binaryTreePaths(Tree(values1).build()))
}
