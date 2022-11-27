/**
 * Definition for a binary tree node.
 * class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
 *   var value: Int = _value
 *   var left: TreeNode = _left
 *   var right: TreeNode = _right
 * }
 */

/**
  * Preorder: Tracking the Min and Max during the recursion
  */
object Solution1 {
  def isValidBST(root: TreeNode): Boolean = {
    searchTree(root, Long.MinValue, Long.MaxValue)
  }

  def searchTree(node: TreeNode, minValue: Long, maxValue: Long): Boolean = {
    if (node == null)
      return true

    if (node.value <= minValue || node.value >= maxValue)
      return false

    val leftCheck = searchTree(node.left, minValue, node.value)
    val rightCheck = searchTree(node.right, node.value, maxValue)
    leftCheck && rightCheck
  }
}

/**
  * Inorder: Tracking the left Max
  */
object Solution2 {
  var leftMax = Long.MinValue
  
  def isValidBST(root: TreeNode): Boolean = {
    if (root == null)
      return true
    
    if (!isValidBST(root.left))
      return false
    
    if (root.value <= leftMax)
      return false
    
    leftMax = root.value
    isValidBST(root.right)
  }
}

/**
  * Inorder: The list's order must be ASC.
  */
object Solution3 {

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
