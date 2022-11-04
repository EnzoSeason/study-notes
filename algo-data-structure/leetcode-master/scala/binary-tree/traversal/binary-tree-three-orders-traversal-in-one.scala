object Solution {

  import scala.collection.mutable

  def traversal(root: TreeNode)(order: String): List[Int] = {
    if (root == null) return Nil

    val stack = mutable.Stack[TreeNode](root)
    var result = List[Int]()

    def preorder(): Unit = {
      val node = stack.pop()

      if (node.right != null) stack.push(node.right) // right
      
      if (node.left != null) stack.push(node.left) // left
      
      stack.push(node) // mid
      stack.push(null) // mark as visited
    }

    def postorder(): Unit = {
      val node = stack.pop()

      stack.push(node) // mid
      stack.push(null)
      
      if (node.right != null) stack.push(node.right) // right
      
      if (node.left != null) stack.push(node.left) // left
    }

    def inorder(): Unit = {
      val node = stack.pop()

      if (node.right != null) stack.push(node.right) // right
      
      stack.push(node) // mid
      stack.push(null)
      
      if (node.left != null) stack.push(node.left) // left
    }
    
    while (stack.nonEmpty) {
      if (stack.top == null) {
        stack.pop()
        
        val node = stack.pop()
        result :+= node.value
      } else {
        order match {
          case "preorder" => preorder()
          case "postorder" => postorder()
          case "inorder" => inorder()
        }
      }
    }

    result
  }
}