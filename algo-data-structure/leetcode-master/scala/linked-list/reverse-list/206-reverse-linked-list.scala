class ListNode(_x: Int = 0, _next: ListNode = null) {
  var next: ListNode = _next
  var x: Int = _x
}

object SolutionTwoPointers {
  def reverseList(head: ListNode): ListNode = {
    var prev: ListNode = null
    var curr = head

    while (curr != null) {
      val next = curr.next
      curr.next = prev

      prev = curr
      curr = next
    }
    prev
  }
}

object SolutionRecursion {
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