/**
 * Definition for a Node.
 * class Node(var _value: Int) {
 *   var value: Int = _value
 *   var children: List[Node] = List()
 * }
 */

object SolutionRec {
  def maxDepth(root: Node): Int = {
    if (root == null) 0
    else {
      var depth = 0
      for (child <- root.children) {
        depth = Math.max(maxDepth(child), depth)
      }
      depth + 1
    }
  }
}

object SolutionQueue {

  import scala.collection.mutable

  def maxDepth(root: Node): Int = {
    if (root == null) return 0

    val queue = mutable.Queue[Node](root)
    var depth = 0

    while (queue.nonEmpty) {
      val levelSize = queue.size
      depth += 1
      for (_ <- 0 until levelSize) {
        val node = queue.dequeue()
        for (child <- node.children) {
          if (child != null) queue.enqueue(child)
        }
      }
    }

    depth
  }
}