/**
 * Definition for a binary tree node.
 * class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
 *   var value: Int = _value
 *   var left: TreeNode = _left
 *   var right: TreeNode = _right
 * }
 */
object SolutionRec {
  def isSymmetric(root: TreeNode): Boolean = {
    if (root == null) return true
    isSame(root.left, root.right)
  }

  def isSame(t1: TreeNode, t2: TreeNode): Boolean = {
    if (t1 == null && t2 == null) true
    else if (t1 == null || t2 == null) false
    else if (t1.value != t2.value) false
    else isSame(t1.left, t2.right) && isSame(t1.right, t2.left)
  }
}

object SolutionIter {

  import scala.collection.mutable

  def isSymmetric(root: TreeNode): Boolean = {
    if (root == null) return true

    val cache = mutable.Stack[(TreeNode, TreeNode)]((root.left, root.right))
    while (cache.nonEmpty) {
      val (first, last) = cache.pop()

      if (first == null && last == null) null
      else if (first == null || last == null) return false
      else if (first.value != last.value) return false
      else {
        cache.push((first.left, last.right))
        cache.push((first.right, last.left))
      }
    }
    true
  }
}