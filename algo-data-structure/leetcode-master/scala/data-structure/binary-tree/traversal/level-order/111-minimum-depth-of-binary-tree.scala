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

  def minDepth(root: TreeNode): Int = {
    if (root == null) return 0

    val queue = mutable.Queue[TreeNode](root)
    var depth = 0

    while (queue.nonEmpty) {
      val levelSize = queue.size
      depth += 1

      for (_ <- 0 until levelSize) {
        val node = queue.dequeue()

        if (node.left == null && node.right == null) return depth

        if (node.left != null) queue.enqueue(node.left)
        if (node.right != null) queue.enqueue(node.right)
      }
    }

    depth
  }

}

object SolutionRec {
    def minDepth(root: TreeNode): Int = {
        if (root == null) 0
        else {
            val leftMinDepth = minDepth(root.left)
            val rightMinDepth = minDepth(root.right)
            if (leftMinDepth == 0 || rightMinDepth == 0) leftMinDepth + rightMinDepth + 1
            else Math.min(leftMinDepth, rightMinDepth) + 1
        }
    }
}