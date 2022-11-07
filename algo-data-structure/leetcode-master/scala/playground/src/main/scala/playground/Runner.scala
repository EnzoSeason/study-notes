package playground

object Runner extends App {
  val solution = Solution

  val values1: Array[Any] = Array(3,4,5,1,2,null,null,null,null,0)
  val values2: Array[Any] = Array(4,1,2)
  println(solution.isSubtree(Tree(values1).build(), Tree(values2).build()))
}
