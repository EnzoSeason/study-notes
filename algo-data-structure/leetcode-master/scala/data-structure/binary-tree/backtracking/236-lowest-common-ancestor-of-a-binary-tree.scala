/**
 * Definition for a binary tree node.
 * class TreeNode(var _value: Int) {
 *   var value: Int = _value
 *   var left: TreeNode = null
 *   var right: TreeNode = null
 * }
 */

object Solution {
  def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode): TreeNode = {
    if (root == null || root == p || root == q) root
    else {
      val left = lowestCommonAncestor(root.left, p, q)
      val right = lowestCommonAncestor(root.right, p, q)

      if (left != null && right != null) root
      else if (left != null && right == null) left
      else if (left == null && right != null) right
      else null
    }
  }
}