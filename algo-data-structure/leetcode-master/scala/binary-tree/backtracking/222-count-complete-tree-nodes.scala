/**
 * Definition for a binary tree node.
 * class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
 *   var value: Int = _value
 *   var left: TreeNode = _left
 *   var right: TreeNode = _right
 * }
 */

object SolutionNormalBinaryTree {
  // Time complexit: O(n)

  def countNodes(root: TreeNode): Int = {
    if (root == null) 0
    else countNodes(root.left) + countNodes(root.right) + 1
  }
}

object SolutionCompleteBinaryTree {

  // Hint:
  // Nb of nodes of a perfect binary tree = 2^depth - 1

  def countNodes(root: TreeNode): Int = {
    // This function traverses level by level (O(logN)),
    // and on each level, it calculates the depth of the leftest sub branch (O(logN)).
    // Therefore, the time complexity is O(logN * logN)

    if (root == null) return 0

    val left = getLeftDepth(root.left)
    val right = getLeftDepth(root.right)

    if (left == right) {
      // left sub tree is perfect binary tree
      // Nb of nodes = root + left sub tree + right sub tree
      1 + (Math.pow(2, left).toInt - 1) + countNodes(root.right)
    } else {
      // right sub tree is perfect binary tree
      // Nb of nodes = root + left sub tree + right sub tree
      1 + (Math.pow(2, right).toInt - 1) + countNodes(root.left)
    }
  }

  def getLeftDepth(root: TreeNode): Int = {
    // Time complexity: O(logN)

    if (root == null) 0
    else 1 + getLeftDepth(root.left)
  }
}

