/**
 * Definition for a binary tree node.
 * class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
 *   var value: Int = _value
 *   var left: TreeNode = _left
 *   var right: TreeNode = _right
 * }
 */
object Solution {
  def sortedArrayToBST(nums: Array[Int]): TreeNode = {
    val rootIdx = nums.length / 2
    if (rootIdx >= 0 && rootIdx < nums.length) {
      val root = new TreeNode(nums(rootIdx))
      root.left = sortedArrayToBST(nums.take(rootIdx))
      root.right = sortedArrayToBST(nums.drop(rootIdx + 1))
      root
    } else null
  }
}