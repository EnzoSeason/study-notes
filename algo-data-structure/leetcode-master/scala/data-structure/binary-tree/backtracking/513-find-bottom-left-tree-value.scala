/**
 * Definition for a binary tree node.
 * class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
 *   var value: Int = _value
 *   var left: TreeNode = _left
 *   var right: TreeNode = _right
 * }
 */
object SolutionRec {
  def findBottomLeftValue(root: TreeNode): Int = {
    var maxDepth = -1
    var result = 0
    
    def bottomFinder(node: TreeNode, depth: Int): Unit = {
      if (node.left == null && node.right == null && depth > maxDepth) {
        maxDepth = depth
        result = node.value
      }
      if (node.left != null) bottomFinder(node.left, depth + 1)
      if (node.right != null) bottomFinder(node.right, depth + 1)
    }
    
    bottomFinder(root, 0)
    result
  }
}

object SolutionIter {

  import scala.collection.mutable

  def findBottomLeftValue(root: TreeNode): Int = {
    if (root == null) return 0

    val queue = mutable.Queue[TreeNode](root)
    var result: Int = 0
    while (queue.nonEmpty) {
      val levelSize = queue.size
      result = queue.head.value
      for (_ <- 0 until levelSize) {
        val node = queue.dequeue()
        if (node.left != null) queue.enqueue(node.left)
        if (node.right != null) queue.enqueue(node.right)
      }
    }
    result
  }
}