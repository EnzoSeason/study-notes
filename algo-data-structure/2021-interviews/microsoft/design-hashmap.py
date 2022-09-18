from typing import Optional


class Node:
    def __init__(self, key: Optional[int] = None, value: Optional[int] = None) -> None:
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:
    """
    https://leetcode.com/problems/design-hashmap/solution/

    Hash function:
        hash_key = key % N (N is the length of the list of linked lists.)

    Hash collision:
      If two different keys generate a same hask key, we add a new node at the end of linked list.
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.N = 2069
        self.hash_map = [Node()] * self.N

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hash_key = key % self.N
        node = self.hash_map[hash_key]

        while node.next:
            p = node.next
            if p.key == key:
                p.value = value
                return
            node = node.next

        node.next = Node(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hash_key = key % self.N
        node = self.hash_map[hash_key]

        while node.next:
            p = node.next
            if p.key == key:
                return p.value
            node = node.next

        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hash_key = key % self.N
        node = self.hash_map[hash_key]

        while node.next:
            p = node.next
            if p.key == key:
                node.next = p.next
                return
            node = node.next