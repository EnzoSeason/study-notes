/**
 * Definition for a Node.
 * class Node(var _value: Int) {
 *   var value: Int = _value
 *   var children: List[Node] = List()
 * }
 */

object Solution {

  import scala.collection.mutable

  def levelOrder(root: Node): List[List[Int]] = {
    if (root == null) return Nil

    val queue = mutable.Queue[Node](root)
    var result = List[List[Int]]()

    while (queue.nonEmpty) {
      val levelSize = queue.size
      var levelValues = List[Int]()
      
      for (_ <- 0 until levelSize) {
        val node = queue.dequeue()
        levelValues :+= node.value
        
        for (child <- node.children) {
          queue.enqueue(child)
        }
      }
      
      result :+= levelValues
    }
    
    result
  }
}