package playground


object Solution {

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