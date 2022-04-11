## Linked List

There are 3 basic types of linked list:

- singly linked list

- circular linked list

- doubly linked list

### singly linked list

Singly linked list is composed by **nodes**.

Each node has 2 parts:

- data

- pointer: It points to the next node.

There are 2 special nodes.

- head node: It's the first node in the linked list. Usually, we set the head node as a **node without data** to make sure a linked list has **ONE** node at least.

- tail node: It's the last node. It points to *Null*.

Different from Array, Singly linked list is good at inserting and deleting an item. The time complexity is O(1). But it's terrible to find one. The time complexity is O(n).

### circular linked list

It's a special singly linked list. The tail node points to the head node.

### doubly linked list

It's a special singly linked list, too. Each node has **2 pointers** which point to the **previous node and next node**.

It's widely used in practice. It makes inserting and deleting easier.

For exemple, we use doubly linked list to create LRU Caching.

In the exemple, cache is a doubly linked list. **Head node is a node without data**. Tail node is the least used node. We remove the tail when the cache is full.

```python
class LinkedNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
        
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = LinkedNode(None, None)
    
    def _move_to_head(self,pointer: LinkedNode) -> None:
        pointer.next = self.head.next
        if self.head.next is not None:
            self.head.next.prev = pointer
        self.head.next = pointer
        pointer.prev = self.head
    
    def _remove(self, pointer: LinkedNode) -> LinkedNode:
        prev_node = pointer.prev
        next_node = pointer.next
        prev_node.next = next_node
        if next_node is not None:
            next_node.prev = prev_node
        
        return pointer
        
        

    def get(self, key: int) -> int:
        pointer = self.head.next
        
        while pointer is not None:
            if pointer.key == key:
                pointer = self._remove(pointer)
                self._move_to_head(pointer)
                return pointer.val
            
            pointer = pointer.next
        
        return -1
    
    def put(self, key: int, value: int) -> None:
        pointer = self.head.next
        tail = None
        
        while pointer is not None:
            if pointer.key == key:
                pointer = self._remove(pointer)
                self._move_to_head(pointer)
                pointer.val = value
                return None
            if pointer.next is None:
                tail = pointer
            pointer = pointer.next
        
        after_head = LinkedNode(key, value)
        self._move_to_head(after_head)
        self.capacity -= 1
        
        if self.capacity < 0:
            before_tail = tail.prev
            before_tail.next = None
            tail.prev = None
            self.capacity = 0
        
        return None
```

There are some typical problems.

- [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

- [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)

- [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)

- [Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)

- [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)