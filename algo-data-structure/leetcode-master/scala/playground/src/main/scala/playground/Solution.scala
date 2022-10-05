package playground

// Definition for singly-linked list.
class ListNode(_x: Int = 0, _next: ListNode = null) {
  var next: ListNode = _next
  var x: Int = _x
}

object Solution {
  def detectCycle(head: ListNode): ListNode = {
    var fast = head
    var slow = head

    while (fast != null && fast.next != null) {
      slow = slow.next
      fast = fast.next.next

      if (fast == slow) {
        slow = head
        while (slow != fast) {
          slow = slow.next
          fast = fast.next
        }
        return slow
      }
    }
    null
  }
}