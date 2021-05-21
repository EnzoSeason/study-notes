class LinkedNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.next = None
        self.prev = None

class LFUCache:

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.head = LinkedNode(None, None)

    def get(self, key: int) -> int:
        p = self.head
        while p is not None:
            if p.key == key:
                p.freq += 1
                self._remove(p)
                self._insert(p)
                return p.val
            else:
                p = p.next
        return -1
        

    def put(self, key: int, value: int) -> None:
        count = 0
        p = self.head
        last_node = self.head
        
        while p.next is not None:
            if p.key == key:
                p.freq += 1
                p.val = value
                self._remove(p)
                self._insert(p)
                return
            else:
                last_node = p
                p = p.next
                count += 1
        
        new_node = LinkedNode(key, value)
        self._insert(new_node)
        if count > self.capacity:
            last_node.prev.next = None


        