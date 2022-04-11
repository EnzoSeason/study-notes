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

  There are 2 ways to use stack in this problem.
  
  - use **two stacks**, one for numbers, one for operations. 
  
    use **two loops**. The first loop reads digitals and deals with the `*` and `/` operations. The second one deals with the rest and returns the result


  - use **one stack for number**. The number can be positive and negative

    use **2 global variables**, previous number and previous operator. 
    
    use **one loop**, we always deal with the previous case and update these two variable. 
    
    DO NOT forget the last char in the string.


- [224. Basic Calculator](https://leetcode.com/problems/basic-calculator/)

## Queue

Queue is a limited **linear list**, too. The rule is **FIFO** (First In First Out).

We can use **array** or **linked list** to implement this data structure.

```python
class ArrayQueue:
    def __init__(self, n):
        self.items = []
        self.n = n
        self.head = 0 # index of the first item
        self.tail = 0 # index after the last item
    
    def enqueue(self, item) -> bool:
        if self.tail == self.n:
            if self.head == 0:
                # Queue is full.
                return False
            for i in range(self.head, self.n):
                self.items[i - self.head] = self.items[i]
            self.tail = self.n - self.head
            self.head = 0
        
        self.items[self.tail] = item
        self.tail += 1
        return True
    
    def dequeue(self):
        if self.head == self.tail:
            return None
        item = self.items[self.head]
        self.head += 1
        return item
```

```python
class LinkedNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedListQueue:
    def __init__(self, n):
        self.head = LinkedNode(None) # node before the first node
        self.tail = self.head # node of the last node
        self.n = n
        self.count = 0
    
    def enqueue(self, item):
        if self.count == self.n:
            return False
        new_node = LinkedNode(item)
        self.tail.next = new_node
        self.tail = self.tail.next
        self.count += 1
        return True
    
    def dequeue(self):
        if self.count == 0:
            return None
        val = self.head.next.val
        self.head.next = self.head.next.next
        self.count -= 1
        return val
```

### Circular Queue

The circular queue is based on **array queue**. The tail of the queue is followed by the head.

It doesn't need to move data when the queue is "fake" full (`tail == n && head != 0`). 

> In practice, There is an empty space between the head and the tail. It helps to define the conditions of full queue and empty queue.

Two edge cases are important to a queue.

- The queue is full.

- The queue is empty.

For a normal array queue, these 2 are:

- Full: `tail == n`

- Empty: `head == tail`

For the circular array queue, these 2 are:

- Full: `(tail + 1) % n == head`

  > We use `(tail + 1) % n` to move `tail` to the next position. It's the same for `head`.

  > `(a + 1) % n ` solves the special case. When `a == n - 1`, the next position of `a` should be `0`.

- Empty: `head == tail`

```python
class CircularArrayQueue:
    def __init__(self, n):
        self.items = []
        self.n = n
        self.head = 0 # index of the first item
        self.tail = 0 # index after the last item
    
    def enqueue(self, item):
        if (self.tail + 1) % self.n == self.head:
            return False
        self.items[self.tail] = item
        self.tail = (self.tail + 1) % self.n
        reture True
    
    def dequeue(self):
        if self.tail == self.head:
            return None
        val = self.items[self.head]
        self.head = (self.head + 1) % n
```

The circular queue is widely used in **pools**, such as connection pool of database, **message queue**, **concurrency**, etc. It controls the distribution of the resource.

