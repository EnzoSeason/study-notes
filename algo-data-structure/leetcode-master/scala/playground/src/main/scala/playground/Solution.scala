package playground


// Definition for singly-linked list.
class ListNode(_x: Int = 0, _next: ListNode = null) {
  var next: ListNode = _next
  var x: Int = _x
}

object Solution {
  def removeElements(head: ListNode, target: Int): ListNode = {
    val dummyHead = new ListNode(0, head)
    var prev = dummyHead

    while (prev.next != null) {
      val curr = prev.next
      if (curr.x == target) {
        prev.next = curr.next
        curr.next = null
      } else {
        prev = prev.next
      }
    }

    dummyHead.next
  }
}