/**
 * Definition for a binary tree node.
 * class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
 *   var value: Int = _value
 *   var left: TreeNode = _left
 *   var right: TreeNode = _right
 * }
 */
object SolutionRec {

  import scala.collection.mutable.ListBuffer

  def binaryTreePaths(root: TreeNode): List[String] = {
    if (root == null) List[String]("")
    else {
      val result = ListBuffer[String]()
      pathBuilder(root, List[Int](), result)
      result.toList
    }
  }

  def pathBuilder(node: TreeNode, previous: List[Int], paths: ListBuffer[String]): Unit = {
    if (node.left == null && node.right == null) {
      val path = (previous :+ node.value).mkString("->")
      paths.append(path)
    }
    else {
      val current = previous :+ node.value
      if (node.left != null) pathBuilder(node.left, current, paths)
      if (node.right != null) pathBuilder(node.right, current, paths)
    }
  }
}

object SolutionIter {

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