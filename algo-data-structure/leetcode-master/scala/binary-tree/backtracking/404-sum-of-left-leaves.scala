/**
 * Definition for a binary tree node.
 * class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
 *   var value: Int = _value
 *   var left: TreeNode = _left
 *   var right: TreeNode = _right
 * }
 */
object SolutionRec {
  def sumOfLeftLeaves(root: TreeNode): Int = {
    if (root == null) return 0

    val left = sumOfLeftLeaves(root.left)
    val right = sumOfLeftLeaves(root.right)

    if (root.left != null && root.left.left == null && root.left.right == null) {
      root.left.value + left + right
    } else {
      left + right
    }
  }
}

object SolutionIter {

  import scala.collection.mutable

  def sumOfLeftLeaves(root: TreeNode): Int = {
    if (root == null) return 0

    var leftLeavesSum = 0
    val stack = mutable.Stack[TreeNode](root)
    while (stack.nonEmpty) {
      val node = stack.pop()
      
      if (node.left != null && node.left.left == null && node.left.right == null) {
        leftLeavesSum += node.left.value
      }
      if (node.left != null) stack.push(node.left)
      if (node.right != null) stack.push(node.right)
    }
    
    leftLeavesSum
  }
}