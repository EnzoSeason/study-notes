package playground

case class Tree(values: Array[Any]) {

  import scala.collection.mutable

  def build(): TreeNode = {
    if (values == null || values.isEmpty) return null

    val root = TreeNode(values(0).toString.toInt)
    val queue = mutable.Queue[TreeNode](root)

    var i = 1
    while (queue.nonEmpty) {
      val node = queue.dequeue()
      if (node != null) {
        val left =
          if (i >= values.length || values(i) == null) null
          else TreeNode(values(i).toString.toInt)
        val right =
          if (i + 1 >= values.length || values(i + 1) == null) null
          else TreeNode(values(i + 1).toString.toInt)

        node.left = left
        node.right = right

        queue.enqueue(left)
        queue.enqueue(right)
        i += 2
      }
    }

    root
  }
}
