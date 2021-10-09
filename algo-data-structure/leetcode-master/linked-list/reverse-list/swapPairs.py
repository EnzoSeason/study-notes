from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    https://leetcode.com/problems/swap-nodes-in-pairs/
    """

    def swapPairs(self, head: ListNode) -> ListNode:
        pivot = ListNode()
        pivot.next = head

        prev, curr = pivot, head
        while curr and curr.next:
            a = prev.next
            b = curr.next
            # swap
            # next_node = b.next
            # b.next = a (firt element)
            # prev.next, a.next = b, next_node (the rest)
            b.next, prev.next, a.next = a, b, b.next
            prev, curr = a, a.next

        return pivot.next