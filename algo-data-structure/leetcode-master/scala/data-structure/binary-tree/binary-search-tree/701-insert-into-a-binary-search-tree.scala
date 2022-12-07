/**
 * Definition for a binary tree node.
 * class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
 *   var value: Int = _value
 *   var left: TreeNode = _left
 *   var right: TreeNode = _right
 * }
 */
object SolutionRec1 {
  def insertIntoBST(root: TreeNode, value: Int): TreeNode = {
    if (root == null) new TreeNode(value)
    else {
      if (root.value > value) root.left = insertIntoBST(root.left, value)
      else root.right = insertIntoBST(root.right, value)
      root
    }
  }
}

object SolutionRec2 {
  def insertIntoBST(root: TreeNode, value: Int): TreeNode = {
    if (root == null) new TreeNode(value)
    else {
      insert(root, value)
      root
    }
  }

  def insert(node: TreeNode, value: Int): Unit = {
    if (node.value > value) {
      if (node.left == null) {
        node.left = new TreeNode(value)
      } else insert(node.left, value)
    } else {
      if (node.right == null) {
        node.right = new TreeNode(value)
      } else insert(node.right, value)
    }
  }
}

object SolutionIter {
  def insertIntoBST(root: TreeNode, value: Int): TreeNode = {
    if (root == null) return new TreeNode(value)

    var prev: TreeNode = null
    var curr = root
    while (curr != null) {
      prev = curr
      if (curr.value > value) curr = curr.left
      else curr = curr.right
    }

    val leaf = new TreeNode(value)
    if (prev.value > value) prev.left = leaf
    else prev.right = leaf

    root
  }
}