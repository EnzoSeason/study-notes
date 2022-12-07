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

  def largestValues(root: TreeNode): List[Int] = {
    if (root == null) return Nil

    val queue = mutable.Queue[TreeNode](root)
    var result = List[Int]()

    while (queue.nonEmpty) {
      val levelSize = queue.size
      var levelMax = Int.MinValue

      for (_ <- 0 until levelSize) {
        val node = queue.dequeue()
        levelMax = if (node.value > levelMax) node.value else levelMax

        if (node.left != null) queue.enqueue(node.left)
        if (node.right != null) queue.enqueue(node.right)
      }

      result :+= levelMax
    }

    result
  }

}