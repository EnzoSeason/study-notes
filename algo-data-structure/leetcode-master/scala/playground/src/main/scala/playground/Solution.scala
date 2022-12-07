package playground

object Solution {
  def convertBST(root: TreeNode): TreeNode = {
    var acc = 0

    def sumNodeValue(node: TreeNode): Unit = {
      if (node == null) return

      sumNodeValue(node.right)

      node.value += acc
      acc = node.value

      sumNodeValue(node.left)
    }

    sumNodeValue(root)
    root
  }
}