/**
 * Definition for a binary tree node.
 * class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
 *   var value: Int = _value
 *   var left: TreeNode = _left
 *   var right: TreeNode = _right
 * }
 */
object Solution {
  def constructMaximumBinaryTree(nums: Array[Int]): TreeNode = {
    if (nums.isEmpty) return null

    val maxValue = nums.max
    val idx = nums.indexOf(maxValue)

    val root = new TreeNode(maxValue)
    root.left = constructMaximumBinaryTree(nums.take(idx))
    root.right = constructMaximumBinaryTree(nums.drop(idx + 1))

    root
  }
}