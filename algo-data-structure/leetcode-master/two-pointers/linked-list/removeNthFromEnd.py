class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    https://leetcode.com/problems/remove-nth-node-from-end-of-list/    
    """

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        pivot = ListNode
        pivot.next = head
        prev = pivot

        #  init the interval
        curr = head
        for _ in range(n):
            if not curr:
                return head
            curr = curr.next
        
        #  move the interval
        while curr:
            prev = prev.next
            curr = curr.next
        
        #  remove the node
        curr = prev.next
        if curr:
            prev.next = curr.next
        
        return pivot.next