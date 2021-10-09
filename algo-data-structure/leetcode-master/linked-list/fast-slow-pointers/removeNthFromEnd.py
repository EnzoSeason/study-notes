class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    https://leetcode.com/problems/remove-nth-node-from-end-of-list/
    """

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        pivot = ListNode()
        pivot.next = head

        #  init the interval between slow and fast
        slow, fast = pivot, pivot
        for _ in range(n):
            if not fast:
                return pivot.next
            fast = fast.next
        
        #  move the fast pointer to the tail
        #  remove the node pointed by slow
        while fast.next:
            slow = slow.next
            fast = fast.next

        if slow.next:
            slow.next = slow.next.next
        else:
            slow.next = None

        return pivot.next