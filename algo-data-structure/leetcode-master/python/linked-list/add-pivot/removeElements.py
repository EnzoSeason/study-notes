class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    https://leetcode.com/problems/remove-linked-list-elements/

    add a pivot before the head.
    """

    def removeElements(self, head: ListNode, val: int) -> ListNode:
        pivot = ListNode(-1, head)
        prev = pivot

        while prev.next:
            curr = prev.next
            if curr.val == val:
                prev.next = curr.next
                curr.next = None
            else:
                prev = prev.next

        return pivot.next