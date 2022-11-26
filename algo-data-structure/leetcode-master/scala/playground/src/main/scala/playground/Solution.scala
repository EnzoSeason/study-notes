package playground

object Solution {
  def mergeTrees(root1: TreeNode, root2: TreeNode): TreeNode = {
    if (root1 == null && root2 == null) null
    else if (root1 == null) root2
    else if (root2 == null) root1
    else {
      val node = new TreeNode()
      node.value = root1.value + root2.value
      node.left  = mergeTrees(root1.left, root2.left)
      node.right = mergeTrees(root1.right, root2.right)
      node
    }
  }
}