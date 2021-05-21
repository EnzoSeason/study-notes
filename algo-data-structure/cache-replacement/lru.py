class LinkedNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:
    """
    https://leetcode.com/problems/lru-cache/
    https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_recently_used_(LRU)

    using doubly linked list. 
    LinkedNode has both prev and next pointer 
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = LinkedNode(None, None)
        self.count = 0

    def _remove(self, node: LinkedNode) -> None:
        prev_node, next_node = node.prev, node.next
        prev_node.next = next_node
        if next_node:
            next_node.prev = prev_node

    def _moveToHead(self, node: LinkedNode) -> None:
        first_node = self.head.next
        self.head.next = node
        node.prev = self.head
        if first_node:
            first_node.prev = node
            node.next = first_node

    def get(self, key: int) -> int:
        p = self.head.next
        while p is not None:
            if p.key == key:
                self._remove(p)
                self._moveToHead(p)
                return p.val
            else:
                p = p.next
        return -1

    def put(self, key: int, value: int) -> None:
        p = self.head
        last_node = self.head
        count = 0
        
        while p is not None:
            if p.key == key:
                p.val = value
                self._remove(p)
                self._moveToHead(p)
                return
            else:
                last_node = p
                p = p.next
                count += 1

        new_node = LinkedNode(key, value)
        self._moveToHead(new_node)
        if count > self.capacity:
            last_node.prev.next = None