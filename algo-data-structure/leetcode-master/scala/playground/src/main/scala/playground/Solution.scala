package playground

object Solution {
  def deleteNode(root: TreeNode, key: Int): TreeNode = {
    if (root == null) return null

    if (root.value == key) {
      if (root.left == null && root.right == null) {
        // delete the current node (leaf)
        return null
      }
      else if (root.left != null && root.right == null) {
        // replace the current node by the left sub tree
        return root.left
      }
      else if (root.left == null && root.right != null) {
        // replace the current node by the right sub tree
        return root.right
      }
      else {
        var leaf = root.right
        while (leaf.left != null) leaf = leaf.left
        // set the leftest leaf as the current node
        leaf.left = root.left
        return root.right
      }
    }

    if (root.value > key) {
      root.left = deleteNode(root.left, key)
    }

    if (root.value < key) {
      root.right = deleteNode(root.right, key)
    }

    root
  }
}