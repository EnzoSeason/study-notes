from typing import Tuple


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    https://leetcode.com/problems/reverse-nodes-in-k-group/
    """

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        pivot = ListNode()
        pivot.next = head

        prev = pivot
        while prev.next:
            #  make sure there are, at least, k nodes left
            tail = prev.next
            for _ in range(k):
                if not tail:
                    return pivot.next
                tail = tail.next

            #   reverse sub linked list
            sub_head, sub_tail = self.reverse(prev, k)

            #  connect reversed linked list
            prev.next = sub_head

            #   update prev
            prev = sub_tail

        return pivot.next

    def reverse(self, pivot: ListNode, k) -> Tuple[ListNode, ListNode]:
        sub_tail = pivot.next

        #   reverse
        prev, curr = pivot, pivot.next
        i = 0
        while i < k and curr:
            curr.next, prev, curr = prev, curr, curr.next
            i += 1

        #  update tail.next
        sub_tail.next = curr

        return prev, sub_tail