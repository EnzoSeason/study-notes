/**
 * Definition for a binary tree node.
 * class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
 *   var value: Int = _value
 *   var left: TreeNode = _left
 *   var right: TreeNode = _right
 * }
 */
object SolutionRec { // it's DFS, too.
  def invertTree(root: TreeNode): TreeNode = {
    if (root == null) return root

    val tmp = root.left
    root.left = root.right
    root.right = tmp

    invertTree(root.left)
    invertTree(root.right)

    root
  }
}

object SolutionDFS {

  import scala.collection.mutable

  def invertTree(root: TreeNode): TreeNode = {
    if (root == null) return root

    val cache = mutable.Stack[TreeNode](root)
    while (cache.nonEmpty) {
      val node = cache.pop()

      val tmp = node.left
      node.left = node.right
      node.right = tmp

      if (node.left != null) cache.push(node.left)
      if (node.right != null) cache.push(node.right)
    }

    root
  }
}

object SolutionBFS {

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