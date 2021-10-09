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

        while fast and fast.next:
            #  verify if there has a circle
            #  fast_move = 2 * slow_move
            slow = slow.next
            fast = fast.next.next

            if fast is slow:
                #  There is a circle.
                #  reset the slow to the head, and
                #  fast_move = slow_move
                slow = head
                while slow is not fast:
                    slow = slow.next
                    fast = fast.next
                return slow

        return None