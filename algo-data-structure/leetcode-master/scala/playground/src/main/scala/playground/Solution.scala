package playground

// Definition for singly-linked list.
class ListNode(_x: Int = 0, _next: ListNode = null) {
  var next: ListNode = _next
  var x: Int = _x
}

object Solution {
  def removeNthFromEnd(head: ListNode, n: Int): ListNode = {
    val dummyHead = new ListNode(-1, head)
    var fast = dummyHead
    var slow = dummyHead

    for (_ <- 0 to n) {
      if (fast == null) return dummyHead.next
      fast = fast.next
    }

    while(fast.next != null) {
      slow = slow.next
      fast = fast.next
    }

    val removedNode = slow.next
    slow.next = if (removedNode != null) removedNode.next else null
    head
  }
}