package playground


object Solution {

  import scala.collection.mutable

  def invertTree(root: TreeNode): TreeNode = {
    if (root == null) return root

    val cache = mutable.Queue[TreeNode](root)
    while (cache.nonEmpty) {
      val levelSize = cache.size
      for (_ <- 0 until levelSize) {
        val node = cache.dequeue()

        val tmp = node.left
        node.left = node.right
        node.right = tmp

        if (node.left != null) cache.enqueue(node.left)
        if (node.right != null) cache.enqueue(node.right)
      }
    }

    root
  }
}