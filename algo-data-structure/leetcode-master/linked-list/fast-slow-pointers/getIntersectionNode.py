# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    https://leetcode.com/problems/intersection-of-two-linked-lists/
    """

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a = headA
        b = headB

        while a is not b:
            a = a.next if a is not None else headB
            b = b.next if b is not None else headA

        return a