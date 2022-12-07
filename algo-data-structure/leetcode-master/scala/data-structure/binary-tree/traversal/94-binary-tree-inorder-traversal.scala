class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object SolutionRec {
    def inorderTraversal(root: TreeNode): List[Int] = {
        if (root == null) Nil
        else inorderTraversal(root.left) ::: root.value :: Nil ::: inorderTraversal(root.right)
    }
}

object SolutionIter {

  import scala.collection.mutable

  def inorderTraversal(root: TreeNode): List[Int] = {
    val stack = mutable.Stack[TreeNode]()
    var result = List[Int]()
    var curr = root

    while (curr != null || stack.nonEmpty) {
      if (curr != null) {
        stack.push(curr)
        curr = curr.left
      } else {
        curr = stack.pop()
        result :+= curr.value
        curr = curr.right
      }
    }

    result
  }
}