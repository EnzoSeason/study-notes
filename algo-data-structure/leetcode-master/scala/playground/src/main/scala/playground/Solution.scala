package playground

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