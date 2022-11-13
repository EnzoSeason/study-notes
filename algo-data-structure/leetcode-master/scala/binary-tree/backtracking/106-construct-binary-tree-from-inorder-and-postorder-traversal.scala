/**
 * Definition for a binary tree node.
 * class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
 *   var value: Int = _value
 *   var left: TreeNode = _left
 *   var right: TreeNode = _right
 * }
 */
object Solution {
  def buildTree(inorder: Array[Int], postorder: Array[Int]): TreeNode = {
    if (postorder.isEmpty) return null

    val root = new TreeNode(postorder.last)
    val idx = inorder.indexOf(root.value)

    root.left = buildTree(inorder.take(idx), postorder.take(idx))
    root.right = buildTree(inorder.drop(idx + 1), postorder.slice(idx, postorder.length - 1))
    
    root
  }
}