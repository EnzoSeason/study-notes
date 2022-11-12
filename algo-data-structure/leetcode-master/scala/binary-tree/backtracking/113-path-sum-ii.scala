/**
 * Definition for a binary tree node.
 * class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
 *   var value: Int = _value
 *   var left: TreeNode = _left
 *   var right: TreeNode = _right
 * }
 */
object SolutionRec {

  import scala.collection.mutable

  def pathSum(root: TreeNode, targetSum: Int): List[List[Int]] = {
    if (root == null) return Nil
    
    val result = mutable.ListBuffer[List[Int]]()

    def pathFinder(node: TreeNode, prev: List[Int]): Unit = {
      if (node.left == null && node.right == null && node.value + prev.sum == targetSum) {
        result.append(prev :+ node.value)
      }

      if (node.left != null) pathFinder(node.left, prev :+ node.value)
      if (node.right != null) pathFinder(node.right, prev :+ node.value)
    }

    pathFinder(root, List[Int]())
    result.toList
  }
}

object SolutionIter {

  import scala.collection.mutable

  def pathSum(root: TreeNode, targetSum: Int): List[List[Int]] = {
    if (root == null) return Nil

    val result = mutable.ListBuffer[List[Int]]()
    val stack = mutable.Stack[(TreeNode, List[Int])]((root, List[Int]()))
    while (stack.nonEmpty) {
      val (node, prev) = stack.pop()
      if (node.left == null && node.right == null && node.value + prev.sum == targetSum) {
        result.append(prev :+ node.value)
      }

      if (node.right != null) stack.push((node.right, prev :+ node.value))
      if (node.left != null) stack.push((node.left, prev :+ node.value))
    }

    result.toList
  }
}