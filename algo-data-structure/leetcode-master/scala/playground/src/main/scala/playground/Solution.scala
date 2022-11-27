package playground

object Solution {
  var minDiff = Int.MaxValue
  var leftMax: TreeNode = null

  def getMinimumDifference(root: TreeNode): Int = {
    search(root)
    minDiff
  }

  def search(node: TreeNode): Unit = {
    if (node == null)
      return

    search(node.left)

    if (leftMax != null)
      minDiff = Math.min(minDiff, Math.abs(node.value - leftMax.value))
    leftMax = node

    search(node.right)
  }
}