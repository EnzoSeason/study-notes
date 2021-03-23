# Stack and Queue

## Stack

Stack is a **linear list** limited by the rule **FILO** (First In Last Out).

We can use **array** or **linked list** to implement this data structure.

```python
class ArrayStack:
    def __init__(self, n):
        self.items = []
        self.n = n
        self.count = 0
    
    def push(item) -> bool:
        '''
        Add the item to the end of the array
        O(1)
        '''
        if self.count == self.n:
            return False
        self.items.append(item)
        self.count += 1
        return True
    
    def pop(item):
        '''
        return the last item of the array
        O(1)
        '''
        if self.count == 0:
            return None
        self.count -= 1
        return self.item[self.count]
```

```python
class LinkedNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedListStack:
    def __init__(self, n):
        self.head = LinkedNode(None)
        self.n = n
        self.count = 0
    
    def push(self, item) -> bool:
        '''
        Add item to the first node in the linked list
        O(1)
        '''
        if self.count == self.n:
            return False
        new_node = LinkedNode(item)
        new_node.next = self.head.next
        self.head.next = new_node
        self.count += 1
        return True
    
    def pop(self):
        '''
        return the val of the first node in the linked list
        O(1)
        '''
        if self.head.next is None:
            return None
        tmp = self.head.next
        self.head.next = tmp.next
        tmp.next = None
        return tmp.val
```

Problems:

- [227. Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii/)

- [224. Basic Calculator](https://leetcode.com/problems/basic-calculator/)