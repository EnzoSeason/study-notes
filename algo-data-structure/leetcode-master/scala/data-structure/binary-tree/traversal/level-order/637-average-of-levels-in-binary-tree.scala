class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}


object Solution {

  import scala.collection.mutable

  def averageOfLevels(root: TreeNode): Array[Double] = {
    if (root == null) return Array[Double]()

    val queue = mutable.Queue[TreeNode](root)
    val result = mutable.ArrayBuffer[Double]()

    while (queue.nonEmpty) {
      val levelSize = queue.size
      var levelSum = 0.0
      for (_ <- 0 until levelSize) {
        val node = queue.dequeue()
        levelSum += node.value

        if (node.left != null) queue.enqueue(node.left)
        if (node.right != null) queue.enqueue(node.right)
      }
      result += levelSum / levelSize
    }
    
    result.toArray
  }
}