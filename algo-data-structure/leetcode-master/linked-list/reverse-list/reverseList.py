from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    https://leetcode.com/problems/reverse-linked-list/
    """

    def reverseList_iter(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        while curr:
            # next_node = curr.next
            # curr.next = prev
            # prev, curr = curr, next_node
            curr.next, prev, curr = prev, curr, curr.next


        return prev
    

    def reverseList_re(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        return self.reverseList_worker(prev, curr)
    
    def reverseList_worker(self, prev: Optional[ListNode], curr: Optional[ListNode]) -> ListNode:
        if not curr:
            return prev
        next_node = curr.next
        curr.next = prev
        return self.reverseList_worker(curr, next_node)
