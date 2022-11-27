/**
 * Definition for a binary tree node.
 * class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
 *   var value: Int = _value
 *   var left: TreeNode = _left
 *   var right: TreeNode = _right
 * }
 */

/**
  * Inorder: The list order of BST must be ASC.
  */
object Solution {
  def getMinimumDifference(root: TreeNode): Int = {
    val nodes = inorderSearch(root)
    
    if (nodes.length < 2)
      return 0
    
    var minDiff = Int.MaxValue;
    for (i <- 1 until nodes.length) {
      val diff = Math.abs(nodes(i - 1).value - nodes(i).value)
      minDiff = Math.min(minDiff, diff)
    }
    
    minDiff
  }

  def inorderSearch(node: TreeNode): List[TreeNode] = {
    if (node == null) Nil
    else {
      inorderSearch(node.left) ::: List(node) ::: inorderSearch(node.right)
    }
  }
}

/**
  * Inorder: Tracking the left max
  */
object Solution2 {
  var minDiff = Int.MaxValue
  var leftMax: TreeNode = null

  def getMinimumDifference(root: TreeNode): Int = {
    search(root)
    minDiff
  }

  def search(node: TreeNode): Unit = {
    if (node == null)
      return

    search(node.left)
    
    if (leftMax != null)
      minDiff = Math.min(minDiff, Math.abs(node.value - leftMax.value))
    leftMax = node

    search(node.right)
  }
}