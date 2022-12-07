/**
 * Definition for a binary tree node.
 * class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
 *   var value: Int = _value
 *   var left: TreeNode = _left
 *   var right: TreeNode = _right
 * }
 */
object Solution {
  def convertBST(root: TreeNode): TreeNode = {
    var acc = 0
    
    def sumNodeValue(node: TreeNode): Unit = {
      if (node == null) return
      
      sumNodeValue(node.right)
      
      node.value += acc
      acc = node.value
      
      sumNodeValue(node.left)
    }
    
    sumNodeValue(root)
    root
  }
}