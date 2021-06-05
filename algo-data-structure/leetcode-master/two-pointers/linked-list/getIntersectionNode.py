class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    https://leetcode.com/problems/intersection-of-two-linked-lists/
    """

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a, b = headA, headB

        while True:
            if a == b:
                return a
            a = a.next if a else headB
            b = b.next if b else headA