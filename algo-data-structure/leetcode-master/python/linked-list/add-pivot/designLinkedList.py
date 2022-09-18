class MyNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:
    """
    https://leetcode.com/problems/design-linked-list/
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.pivot = MyNode()
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list.
        If the index is invalid, return -1.
        """
        if index < 0 or index >= self.size:
            return -1

        curr = self.pivot.next
        for _ in range(index):
            curr = curr.next            
        
        return curr.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. 
        After the insertion, the new node will be the first node of the linked list.
        """
        node = MyNode(val)
        head = self.pivot.next

        self.pivot.next = node
        node.next = head

        self.size += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        p = self.pivot
        while p.next:
            p = p.next
        p.next = MyNode(val)

        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. 
        If index equals to the length of linked list, the node will be appended to the end of linked list. 
        If index is greater than the length, the node will not be inserted.
        """
        if index < 0 or index > self.size:
            return

        node = MyNode(val)
        prev = self.pivot

        for _ in range(index):
            prev = prev.next

        if prev.next:
            node.next = prev.next
        prev.next = node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.size:
            return

        prev = self.pivot
        for _ in range(index):
            prev = prev.next

        if prev.next:
            prev.next = prev.next.next
        else:
            prev.next = None
        self.size -= 1