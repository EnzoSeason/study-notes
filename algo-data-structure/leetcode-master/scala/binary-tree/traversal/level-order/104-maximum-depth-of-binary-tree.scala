/**
 * Definition for a binary tree node.
 * class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
 *   var value: Int = _value
 *   var left: TreeNode = _left
 *   var right: TreeNode = _right
 * }
 */

object Solution {

  import scala.collection.mutable

  def maxDepth(root: TreeNode): Int = {
    if (root == null) return 0

    val queue = mutable.Queue[TreeNode](root)
    var depth = 0

    while (queue.nonEmpty) {
      val levelSize = queue.size
      depth += 1
      for (_ <- 0 until levelSize) {
        val node = queue.dequeue()

        if (node.left != null) queue.enqueue(node.left)
        if (node.right != null) queue.enqueue(node.right)
      }
    }

    depth
  }

}

object SolutionRec {
    def maxDepth(root: TreeNode): Int = {
        if (root == null) 0
        else Math.max(maxDepth(root.left), maxDepth(root.right)) + 1
    }
}