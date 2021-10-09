class DLinkedNode:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:
    """
    use 2 dummy nodes: head and tail

    + get: O(1)
    + put: O(1)
    """
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = dict()
        self.head, self.tail = DLinkedNode(), DLinkedNode()  #   dummy node

        self.head.next, self.tail.prev = self.tail, self.head

    def _add(self, node: DLinkedNode) -> None:
        """
        add the node to the head
        """
        first = self.head.next

        self.head.next = node
        node.prev = self.head

        node.next = first
        first.prev = node

    def _remove(self, node: DLinkedNode) -> DLinkedNode:
        """
        remove the node
        """
        node.prev.next = node.next
        node.next.prev = node.prev

        node.prev, node.next = None, None
        return node

    def get(self, key: int) -> int:
        node = self.cache.get(key, None)

        if not node:
            return -1

        node = self._remove(node)
        self._add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key, None)

        if not node:
            node = DLinkedNode(key, value)
            self.cache[key] = node
            self._add(node)
            self.size += 1

            if self.size > self.capacity:
                tail = self._remove(self.tail.prev)
                self.size -= 1
                del self.cache[tail.key]
        else:
            node.val = value
            node = self._remove(node)
            self._add(node)
