/**
 * Definition for a binary tree node.
 * class TreeNode(var _value: Int) {
 *   var value: Int = _value
 *   var left: TreeNode = null
 *   var right: TreeNode = null
 * }
 */

object SolutionRec {
  def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode): TreeNode = {
    if (root == null) null
    else if (root.value > p.value && root.value > q.value) {
      val left = lowestCommonAncestor(root.left, p, q)
      if (left != null) left
      else root
    } else if (root.value < p.value && root.value < q.value) {
      val right = lowestCommonAncestor(root.right, p, q)
      if (right != null) right
      else root
    } else root
  }
}