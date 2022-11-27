package playground

object Solution {

  def isValidBST(root: TreeNode): Boolean = {
    val nodes = inorderSearch(root)

    if (nodes.length <= 1)
      return true

    for (i <- 1 until nodes.length) {
      if (nodes(i - 1).value >= nodes(i).value)
        return false
    }

    true
  }

  def inorderSearch(node: TreeNode): List[TreeNode] = {
    if (node == null) Nil
    else {
      inorderSearch(node.left) ::: List(node) ::: inorderSearch(node.right)
    }
  }
}