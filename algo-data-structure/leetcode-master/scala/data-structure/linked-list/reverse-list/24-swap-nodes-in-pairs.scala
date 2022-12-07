// Definition for singly-linked list.
class ListNode(_x: Int = 0, _next: ListNode = null) {
  var next: ListNode = _next
  var x: Int = _x
}

object SolutionIter {
  def swapPairs(head: ListNode): ListNode = {
    val dummyHead = new ListNode(0, head)

    var prevNode = dummyHead

    var firstNode = dummyHead.next
    if (firstNode == null) return head

    var secondNode = firstNode.next
    if (secondNode == null) return head

    while (firstNode != null && secondNode != null) {
      val nextNode = secondNode.next

      prevNode.next = secondNode
      secondNode.next = firstNode
      firstNode.next = nextNode

      prevNode = firstNode
      firstNode = nextNode
      if (nextNode != null) secondNode = nextNode.next
      else secondNode = null
    }

    dummyHead.next
  }
}

object SolutionRec {
  def swapPairs(head: ListNode): ListNode = {
    if (head == null || head.next == null) return head

    val secondNode = head.next
    val swappedPairs = swapPairs(secondNode.next)

    secondNode.next = head
    head.next = swappedPairs
    
    secondNode
  }
}