class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    https://leetcode.com/problems/linked-list-cycle-ii/
    """

    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        
        #  find the cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast is slow:
                break

        #  return None if there is no cycle
        if not fast or not fast.next:
            return None
        
        #  find the entry of the cycle
        slow = head
        while slow is not fast:
            slow = slow.next
            fast = fast.next
        return slow