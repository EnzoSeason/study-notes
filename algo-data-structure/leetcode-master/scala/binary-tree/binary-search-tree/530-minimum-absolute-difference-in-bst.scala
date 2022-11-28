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
object Solution {
  def getMinimumDifference(root: TreeNode): Int = {
    var minDiff = Int.MaxValue
    var prevNode: TreeNode = null

    def inorderSearch(node: TreeNode): Unit = {
      if (node == null)
        return

      inorderSearch(node.left)

      if (prevNode != null)
        minDiff = Math.min(minDiff, Math.abs(node.value - prevNode.value))
      
      prevNode = node
      inorderSearch(node.right)
    }

    inorderSearch(root)
    minDiff
  }
}