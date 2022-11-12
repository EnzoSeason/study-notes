/**
 * Definition for a binary tree node.
 * class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
 *   var value: Int = _value
 *   var left: TreeNode = _left
 *   var right: TreeNode = _right
 * }
 */
object SolutionRec {
  def hasPathSum(root: TreeNode, targetSum: Int): Boolean = {
    if (root == null) false
    else if (root.left == null && root.right == null && root.value == targetSum) true
    else hasPathSum(root.left, targetSum - root.value) || hasPathSum(root.right, targetSum - root.value)
  }
}

object SolutionIter {

  import scala.collection.mutable

  def hasPathSum(root: TreeNode, targetSum: Int): Boolean = {
    if (root == null) return false

    val stack = mutable.Stack[(TreeNode, Int)]((root, 0))
    while (stack.nonEmpty) {
      val (node, prevSum) = stack.pop()
      
      if (node.left == null && node.right == null && node.value + prevSum == targetSum) return true
      
      if (node.right != null) stack.push((node.right, prevSum + node.value))
      if (node.left != null) stack.push((node.left, prevSum + node.value))
    }
    false
  }
}