package playground


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