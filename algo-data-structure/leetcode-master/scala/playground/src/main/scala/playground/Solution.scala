package playground

object Solution {

  import scala.collection.mutable

  def binaryTreePaths(root: TreeNode): List[String] = {
    if (root == null) return List[String]()

    val result = mutable.ListBuffer[String]()
    val previousPaths = mutable.Stack[List[Int]](List())
    val stack = mutable.Stack[TreeNode](root)

    while (stack.nonEmpty) {
      val node = stack.pop()
      val prevPath = previousPaths.pop()

      if (node.left == null && node.right == null) {
        result.append((prevPath :+ node.value).mkString("->"))
      }

      if (node.right != null) {
        stack.push(node.right)
        previousPaths.push(prevPath :+ node.value)
      }
      if (node.left != null) {
        stack.push(node.left)
        previousPaths.push(prevPath :+ node.value)
      }
    }

    result.toList
  }
}