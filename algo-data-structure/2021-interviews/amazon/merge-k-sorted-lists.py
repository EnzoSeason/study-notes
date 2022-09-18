from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    use the idea of Merge sort
    
    split into ListNodes, then merge into a list
    """
    
    def split(self, lists: List[ListNode], start: int, end: int) -> ListNode:
        if start == end - 1:
            return lists[start]
        mid = start + (end - start) // 2
        l1 = self.split(lists, start, mid)
        l2 = self.split(lists, mid, end)
        return self.merge(l1, l2)

    def merge(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2

        if not l2:
            return l1

        if l1.val < l2.val:
            l1.next = self.merge(l1.next, l2)
            return l1

        l2.next = self.merge(l1, l2.next)
        return l2

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        return self.split(lists, 0, len(lists))