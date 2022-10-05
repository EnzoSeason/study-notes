// Definition for singly-linked list.
class ListNode(_x: Int = 0, _next: ListNode = null) {
  var next: ListNode = _next
  var x: Int = _x
}

object Solution {
  def getIntersectionNode(headA: ListNode, headB: ListNode): ListNode = {
    var pA = headA
    var pB = headB

    while (pA != pB) {
      pA = if (pA == null) headB else pA.next
      pB = if (pB == null) headA else pB.next
    }

    pA
  }
}