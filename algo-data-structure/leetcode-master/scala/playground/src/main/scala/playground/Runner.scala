package playground

object Runner extends App {
  val solution = Solution

  val values = Array(1,null,2,3)
  println(solution.traversal(Tree(values).build())("inorder"))
}
