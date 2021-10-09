from typing import Any


class LinkedNode:
    def __init__(self, key, val) -> None:
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        self.hash_next = None
    
    def __repr__(self) -> str:
        return '{}: {}'.format(self.key, self.val)

class LinkedHashMap:
    '''
    The data is stocked in two-way linked list.
    It uses hash table to find an item, uses chaining to deal with collision.
    When it reaches the max capacity, The least recently uesd (LRU) item is removed.
    '''
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.count = 0
        self.hash_table = {}
        self.head = LinkedNode(None, None)
    
    def _remove_node(self, node) -> LinkedNode:
        prev_node = node.prev
        next_node = node.next
        
        prev_node.next = next_node
        next_node.prev = prev_node

        node.prev = None
        node.next = None
        return node
    
    def _remove_first_node(self) -> None:
        #  remove it from linked list
        first_node = self.head.next
        first_node.prev = None
        self.head.next = first_node.next
        if first_node.next is not None:
            first_node.next.prev = self.head
        first_node.next = None
        #  remove it from hash table
        hash_key = hash(first_node.key)
        p = self.hash_table[hash_key]
        q = p.hash_next
        while q is not None:
            if q.prev is None and q.val is not None:
                p.hash_next = q.hash_next
                q.hash_next = None
            p = p.hash_next
            q = q.hash_next

    def _move_to_tail(self, node) -> None:
        if node.next is None: return
        next_node = node.next
        #  remove node
        node = self._remove_node(node)
        #  add node to the tail
        while next_node.next is not None:
            next_node = next_node.next
        next_node.next = node
        node.prev = next_node
    
    def get(self, key) -> Any:
        hash_key = hash(key)
        if hash_key not in self.hash_table:
            return None
        
        val = None
        h = self.hash_table[hash_key]
        while h is not None:
            if h.key == key:
                val = h.val
                self._move_to_tail(h)
                break
            h = h.hash_next
        return val

    def delete(self, key) -> Any:
        hash_key = hash(key)
        if hash_key not in self.hash_table:
            return None
        
        val = None
        h = self.hash_table[hash_key]
        while h is not None:
            if h.key == key:
                val = h.val
                if h.hash_next is not None:
                    h.hash_next = h.hash_next.hash_next
                h.hash_next = None
                self._remove_node(h)
                break
            h = h.hash_next
        return val
    
    def put(self, key, val) -> None:
        new_node = LinkedNode(key, val)
        #  update hash table
        hash_key = hash(key)
        if hash_key in self.hash_table:
            h = self.hash_table[hash_key]
            while h is not None:
                if h.key == key: #  the item exists
                    h.val = val
                    self._move_to_tail(h)
                    return
                h = h.hash_next
            h.hash_next = new_node
        else:
            self.hash_table[hash_key] = LinkedNode(None, None)
            self.hash_table[hash_key].hash_next = new_node
        
        #  update linked list
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = new_node
        new_node.prev = p
        self.count += 1
        #  remove LRU
        if (self.count > self.capacity):
            self._remove_first_node()
            self.count -= 1
    
    def __repr__(self) -> str:
        val = 'vals: '
        p = self.head.next
        while p is not None:
            val = val + str(p.val) + ', '
            p = p.next
        return val

if __name__ == '__main__':
    m = LinkedHashMap(3)
    print(m.capacity)
    #  test add
    m.put(3, 11)
    print(m)
    m.put(1, 12)
    print(m)
    #  test update
    m.put(3, 21)
    print(m)
    #  test get
    val = m.get(1)
    print(val)
    print(m)
    #  test LRU
    m.put(5, 23)
    print(m)
    m.put(2, 22)
    print(m)
    #  test delete
    node = m.delete(5)
    print(node)
    print(m)