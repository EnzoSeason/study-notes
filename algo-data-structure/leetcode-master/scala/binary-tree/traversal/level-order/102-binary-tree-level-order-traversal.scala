class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {

  import scala.collection.mutable

  def levelOrder(root: TreeNode): List[List[Int]] = {
    if (root == null) return Nil

    val queue = mutable.Queue[TreeNode](root)
    var result = List[List[Int]]()

    while (queue.nonEmpty) {
      val levelSize = queue.size
      var levelValues = List[Int]()

      for (_ <- 0 until levelSize) {
        val node = queue.dequeue()
        levelValues :+= node.value

        if (node.left != null) queue.enqueue(node.left)
        if (node.right != null) queue.enqueue(node.right)
      }

      result :+= levelValues
    }

    result
  }
}