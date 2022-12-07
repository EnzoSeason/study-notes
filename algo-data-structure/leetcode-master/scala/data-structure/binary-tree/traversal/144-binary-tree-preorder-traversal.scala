class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object SolutionRec {
  def preorderTraversal(root: TreeNode): List[Int] = {
    if (root == null) Nil
    else root.value :: preorderTraversal(root.left) ::: preorderTraversal(root.right)
  }
}

object SolutionIter {

  import scala.collection.mutable

  def preorderTraversal(root: TreeNode): List[Int] = {
    if (root == null) return Nil

    val stack = mutable.Stack[TreeNode](root)
    var result = List[Int]()

    while (stack.nonEmpty) {
      val node = stack.pop()
      result :+= node.value

      // push right node before left node
      // because stack needs to pop left one first
      if (node.right != null) stack.push(node.right)
      if (node.left != null) stack.push(node.left)
    }

    result
  }
}