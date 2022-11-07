package playground


object Solution {

  import scala.collection.mutable

  def isSubtree(root: TreeNode, subRoot: TreeNode): Boolean = {
    val cache = mutable.Stack[TreeNode](root)

    while (cache.nonEmpty) {
      val node = cache.pop()
      if (isSame(node, subRoot)) return true
      if (node != null) {
        cache.push(node.left)
        cache.push(node.right)
      }
    }

    false
  }

  def isSame(p: TreeNode, q: TreeNode): Boolean = {
    if (p == null && q == null) true
    else if (p == null || q == null) false
    else if (p.value != q.value) false
    else isSame(p.left, q.left) && isSame(p.right, q.right)
  }
}