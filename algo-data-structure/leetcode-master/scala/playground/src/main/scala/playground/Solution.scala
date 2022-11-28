package playground

object Solution {
  def getMinimumDifference(root: TreeNode): Int = {
    var minDiff = Int.MaxValue
    var prevNode: TreeNode = null

    def inorderSearch(node: TreeNode): Unit = {
      if (node == null)
        return

      inorderSearch(node.left)

      if (prevNode != null)
        minDiff = Math.min(minDiff, Math.abs(node.value - prevNode.value))

      prevNode = node
      inorderSearch(node.right)
    }

    inorderSearch(root)
    minDiff
  }
}