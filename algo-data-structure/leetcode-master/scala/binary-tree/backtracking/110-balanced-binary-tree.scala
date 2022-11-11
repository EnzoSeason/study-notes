/**
 * Definition for a binary tree node.
 * class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
 *   var value: Int = _value
 *   var left: TreeNode = _left
 *   var right: TreeNode = _right
 * }
 */
object Solution {
  def isBalanced(root: TreeNode): Boolean = balanceCounter(root) != -1

  def balanceCounter(root: TreeNode): Int = {
    if (root == null) return 0
    
    val left = balanceCounter(root.left)
    if (left == -1) return -1
    
    val right = balanceCounter(root.right)
    if (right == -1) return -1
    
    if (Math.abs(left - right) > 1) -1
    else Math.max(left, right) + 1
  }
}