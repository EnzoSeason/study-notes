/**
 * Definition for a binary tree node.
 * class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
 *   var value: Int = _value
 *   var left: TreeNode = _left
 *   var right: TreeNode = _right
 * }
 */
object Solution {
  def findMode(root: TreeNode): Array[Int] = {
    var prevNode: TreeNode = null
    var maxCount = 0
    var count = 0
    var result = List[Int]()

    def inorderSearch(node: TreeNode): Unit = {
      if (node == null)
        return

      inorderSearch(node.left)

      if (prevNode == null) {
        count = 1
      } else if (prevNode.value == node.value) {
        count += 1
      } else {
        count = 1
      }
      prevNode = node

      if (count == maxCount) {
        result :+= node.value
      }

      if (count > maxCount) {
        maxCount = count
        result = node.value :: Nil
      }

      inorderSearch(node.right)
    }

    inorderSearch(root)
    result.toArray
  }
}