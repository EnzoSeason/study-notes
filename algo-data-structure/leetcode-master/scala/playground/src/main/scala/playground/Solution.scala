package playground


object Solution {

  import scala.collection.mutable

  def isSymmetric(root: TreeNode): Boolean = {
    if (root == null) return true

    val cache = mutable.Queue[(TreeNode, TreeNode)]((root.left, root.right))
    while (cache.nonEmpty) {
      cache.dequeue() match {
        case (null, null) =>
        case (_, null) => return false
        case (null, _) => return false
        case (left, right) =>
          if (left.value != right.value) return false
          cache.enqueue((left.left, right.right))
          cache.enqueue((left.right, right.left))
      }
    }
    true
  }
}