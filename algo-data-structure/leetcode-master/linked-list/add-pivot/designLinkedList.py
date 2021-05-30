class MyNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.pivot = MyNode()

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list.
        If the index is invalid, return -1.
        """
        curr = self.pivot.next
        i = 0

        while curr and i != index:
            i += 1
            curr = curr.next

        return curr.val if curr else -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node of the linked list.
        """
        node = MyNode(val)
        head = self.pivot.next

        self.pivot.next = node
        node.next = head

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node = MyNode(val)

        p = self.pivot
        while p.next:
            p = p.next
        p.next = node

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list, the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        """
        node = MyNode(val)
        prev = self.pivot
        i = 0

        while prev.next and i != index:
            prev = prev.next
            i += 1

        if prev:
            if prev.next:
                node.next = prev.next
            prev.next = node

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        prev = self.pivot
        i = 0

        while prev.next and i != index:
            prev = prev.next
            i += 1

        if prev:
            if prev.next:
                prev.next = prev.next.next
            else:
                prev.next = None
