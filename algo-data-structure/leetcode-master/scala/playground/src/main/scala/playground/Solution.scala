package playground

object Solution {
  def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode): TreeNode = {
    var node = root
    while (node != null) {
      if (node.value > p.value && node.value > q.value) {
        node = node.left
      } else if (node.value < p.value && node.value < q.value) {
        node = node.right
      } else {
        return node
      }
    }
    null
  }
}