package playground

object Solution {

  import scala.collection.mutable

  def pathSum(root: TreeNode, targetSum: Int): List[List[Int]] = {
    if (root == null) return Nil

    val result = mutable.ListBuffer[List[Int]]()
    val stack = mutable.Stack[(TreeNode, List[Int])]((root, List[Int]()))
    while (stack.nonEmpty) {
      val (node, prev) = stack.pop()
      if (node.left == null && node.right == null && node.value + prev.sum == targetSum) {
        result.append(prev :+ node.value)
      }

      if (node.right != null) stack.push((root.right, prev :+ node.value))
      if (node.left != null) stack.push((root.left, prev :+ node.value))
    }

    result.toList
  }
}