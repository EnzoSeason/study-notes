/**
 * Definition for a Node.
 * class Node(var _value: Int) {
 *   var value: Int = _value
 *   var left: Node = null
 *   var right: Node = null
 *   var next: Node = null
 * }
 */

object Solution {

  import scala.collection.mutable

  def connect(root: Node): Node = {
    if (root == null) return root

    val queue = mutable.Queue[Node](root)

    while (queue.nonEmpty) {
      val levelSize = queue.size
      for (i <- 0 until levelSize) {
        val node = queue.dequeue()
        node.next = if (i == levelSize - 1) null else queue.head

        if (node.left != null) queue.enqueue(node.left)
        if (node.right != null) queue.enqueue(node.right)
      }
    }

    root
  }

}