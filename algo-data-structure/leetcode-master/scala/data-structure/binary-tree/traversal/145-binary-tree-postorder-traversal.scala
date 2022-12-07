class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object SolutionRec {
    def postorderTraversal(root: TreeNode): List[Int] = {
        if (root == null) Nil
        else postorderTraversal(root.left) ::: postorderTraversal(root.right) ::: root.value :: Nil
    }
}

object SolutionIter {

  import scala.collection.mutable

  def postorderTraversal(root: TreeNode): List[Int] = {
    if (root == null) return Nil

    val stack = mutable.Stack[TreeNode](root)
    var result = List[Int]()

    while (stack.nonEmpty) {
      val node = stack.pop()
      result :+= node.value

      // Attention: we push left then right
      if (node.left != null) stack.push(node.left)
      if (node.right != null) stack.push(node.right)
    }

    // result keeps the order 
    //      -> midd :: right :: left
    // we need left :: right :: midd
    // Therefore, we need to reverse the result.
    result.reverse
  }
}