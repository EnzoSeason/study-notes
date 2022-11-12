/**
 * Definition for a binary tree node.
 * class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
 *   var value: Int = _value
 *   var left: TreeNode = _left
 *   var right: TreeNode = _right
 * }
 */
object SolutionRec {
  def isSameTree(p: TreeNode, q: TreeNode): Boolean = {
      if (p == null && q == null) true
      else if (p == null || q == null) false
      else if (p.value != q.value) false
      else isSameTree(p.left, q.left) && isSameTree(p.right, q.right)
  }
}

object SolutionIter {

  import scala.collection.mutable

  def isSameTree(p: TreeNode, q: TreeNode): Boolean = {
    val cache = mutable.Stack[(TreeNode, TreeNode)]((p, q))

    while (cache.nonEmpty) {
      val (first, last) = cache.pop()

      if (first == null && last == null) null
      else if (first == null || last == null) return false
      else if (first.value != last.value) return false
      else {
        cache.push((first.left, last.left))
        cache.push((first.right, last.right))
      }
    }
    
    true
  }
}