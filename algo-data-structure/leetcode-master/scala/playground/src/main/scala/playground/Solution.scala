package playground


object Solution {

  import scala.collection.mutable

  def postorderTraversal(root: TreeNode): List[Int] = {
    if (root == null) return Nil

    val stack = mutable.Stack[TreeNode](root)
    var result = List[Int]()

    while (stack.nonEmpty) {
      val node = stack.pop()
      result :+= node.value

      if (node.left != null) stack.push(node.left)
      if (node.right != null) stack.push(node.right)
    }

    result.reverse
  }
}