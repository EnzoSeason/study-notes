package playground

// Definition for singly-linked list.
class ListNode(_x: Int = 0, _next: ListNode = null) {
  var next: ListNode = _next
  var x: Int = _x
}

object Solution {
  def reverseList(head: ListNode): ListNode = {
    def reverse(prev: ListNode, curr: ListNode): ListNode = {
      if (curr == null) prev
      else {
        val next = curr.next
        curr.next = prev
        reverse(curr, next)
      }
    }
    reverse(null, head)
  }
}