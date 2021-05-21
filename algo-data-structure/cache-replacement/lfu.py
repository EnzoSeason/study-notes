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
        self.count = 0

    def _remove(self, node: LinkedNode) -> None:
        prev_node, next_node = node.prev, node.next
        prev_node.next = next_node
        if next_node:
            next_node.prev = prev_node
        self.count -= 1

    def _pop(self) -> None:
        p = self.head
        while p.next is not None:
            p = p.next
        p.prev.next = None
        self.count -= 1

    def _insert(self, node: LinkedNode) -> None:
        if self.capacity == 0:
            return

        if self.count == self.capacity:
            self._pop()

        p = self.head
        while p.next is not None:
            curr_node = p.next
            if node.freq >= curr_node.freq:
                curr_node.prev.next = node
                node.prev = curr_node.prev
                node.next = curr_node
                curr_node.prev = node
                self.count += 1
                return
            p = p.next

        p.next = node
        node.prev = p
        self.count += 1

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
        p = self.head

        while p is not None:
            if p.key == key:
                p.freq += 1
                p.val = value
                self._remove(p)
                self._insert(p)
                return
            else:
                p = p.next

        new_node = LinkedNode(key, value)
        self._insert(new_node)

    def __str__(self) -> str:
        text = "list: \n"
        p = self.head.next
        while p is not None:
            text += "val:{}, freq: {} \n".format(p.val, p.freq)
            p = p.next
        return text


if __name__ == "__main__":
    lfu = LFUCache(2)

    lfu.put(1, 1)
    print(lfu)

    lfu.put(2, 2)
    print(lfu)

    print(lfu.get(1))
    print(lfu)

    lfu.put(3, 3)
    print(lfu)

    print(lfu.get(2))
    print(lfu)

    print(lfu.get(3))
    print(lfu)

    lfu.put(4, 4)
    print(lfu)

    print(lfu.get(1))
    print(lfu)

    print(lfu.get(3))
    print(lfu)

    print(lfu.get(4))
    print(lfu)
