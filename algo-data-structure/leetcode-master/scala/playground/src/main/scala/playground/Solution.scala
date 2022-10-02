package playground

// Definition for singly-linked list.
class ListNode(_x: Int = 0, _next: ListNode = null) {
  var next: ListNode = _next
  var x: Int = _x
}

object Solution {
  def swapPairs(head: ListNode): ListNode = {
    if (head == null || head.next == null) return head

    val secondNode = head.next
    val swappedPairs = swapPairs(secondNode.next)

    secondNode.next = head
    head.next = swappedPairs

    secondNode
  }
}