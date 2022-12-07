/**
 * Definition for a binary tree node.
 * class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
 *   var value: Int = _value
 *   var left: TreeNode = _left
 *   var right: TreeNode = _right
 * }
 */
object Solution {
  def buildTree(preorder: Array[Int], inorder: Array[Int]): TreeNode = {
    if (preorder.isEmpty) return null

    val root = new TreeNode(preorder.head)
    val idx = inorder.indexOf(root.value)

    root.left = buildTree(preorder.slice(1, idx + 1), inorder.take(idx))
    root.right = buildTree(preorder.drop(idx + 1), inorder.drop(idx + 1))
    
    root
  }
}