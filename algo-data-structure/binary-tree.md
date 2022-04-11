## Binary Tree

### Tree

- nodes:

  There are 3 common types, **parent** node, **child** node and **sibling** node.

  The node that has no child is **leaf** node.

  The node that has no parent is **root** node.

- Height of the node _i_:

  It's the **max number of edge** from the node _i_ to a **leaf** node

- Depth of the node _i_:

  It's the **number of edge** from the node _i_ to the **root** node.

- Level of the node: **Depth** of the node + 1

### Binary Tree

In binary tree, a node has, at most, 2 children.

- full binary tree:

  All the nodes, except **leaf nodes**, have 2 children.

- complete binary tree:

  1. All the nodes, except those in **last 2 levels**, have 2 children.

  2. The leaf nodes are positioned as **left** as possible.

#### Advantage of complete binary tree.

If we save a tree in the **array** and we suppose that the node _i_ is saved in `arr[i]`, then its **left node** is saved in `arr[2*i]` and its **right** node is saved in `arr[2*i+1]`.

If the binary tree is complete, then the array, except the `arr[0]`, is **full**. Otherwise, there must have an index `i, i>0` that `arr[i] is None`.

### Traversing a binary tree

There are **4 orders** to traverse a binary tree.

- Pre Order:

  mid -> left -> right

  ```python
  def pre_order(node):
      if node is None: return
      print(node.val)
      pre_order(node.left)
      pre_order(node.right)
  ```

- In Order:

  left -> mid -> right

  ```python
  def in_order(node):
      if node is None: return
      in_order(node.left)
      print(node.val)
      in_order(node.right)
  ```

- Post Order:

  left -> right -> mid

  ```python
  def post_order(node):
      if node is None: return
      post_order(node.left)
      post_order(node.rigth)
      print(node.val)
  ```

- level order

  It's different from previous orders. It traverse the tree level by level, from left to right.

  ```python
  def level_order(root):
      queue.append(root)
      while len(queue) != 0:
          node = queue.pop(0)
          print(node.val)
          if node.left is not None:
              queue.append(node.left)
          if node.right is not None:
              queue.append(node.right)
  ```

The time complexity of all of them is `O(n)`.

### Binary Search Tree

It's a special binary tree, built for searching.

For any node in the binary tree, all the nodes in its left child tree are smaller than it, those in its right child tree are greater than it.

#### Find a node

```python
def find(self, val: int) -> Optional[LinkedNode]:
    node = self.root
    while node.val != val and node is not None:
        if node.val > val: node = node.left
        if node.val < val: node = node.right
    return node
```

#### Insert a node

```python
def insert(self, val: int) -> None:
    node = self.root
    if node is None:
        self.root = LinkedNode(val)
        return

    parent = None
    while node is not None:
        parent = node
        node = node.left if node.val > val else node.right
    if parent.val > val:
        parent.left = LinkedNode(val)
    else:
        parent.right = LinkedNode(val)
```

#### Delete a node

```python
def delete(val: int) -> Optional[LinkedNode]:
    node = self.root
    parent = None
    while node.val != val and node is not None:
        parent = node
        if node.val > val: node = node.left
        if node.val < val: node = node.right

    if node is None: return

    ## case 1: The node has 2 children
    ## replace the node with the right min node
    if node.left is not None and node.right is not None:
        right_parent = node
        right_min_node = node.right
        while right_min_node.left is not None:
            right_parent = right_min_node
            right_min_node = right_min_node.left
        ## replace the node with the right min node
        node.val, right_min_node.val = right_min_node.val, node.val
        ## prepare for deleting right min node
        parent, node = right_parent, right_min_node

    ## case 2: The node has one child or no child
    child = node.left if node.left is not None else node.right
    
    ## remove node
    if parent is None:
        self.root = child
        return node
    if parent.left is node:
        parent.left = None
        return node
    if parent.right is node:
        parent.right = None
        return node
```

#### Features

- Its `InOrder` traverse returns a **orderd** list.

- Time complexity

  - If the binary search is complete, then the number of comparaison is the **height** of the tree. The time complexity is `O(logn)`.

  - The worst case is all the node have only left / right child. It becomes a **linked list**. The time complexity is `O(n)`.

#### Binary Search Tree vs Hash Table

- Order:

  Hash Table has't an order.

  Binary Search Tree's `InOrder` traverse returns a **orderd** list.

- Performance (Stability of the time complexity)

  Hash Table need **increase / decrease the size**, and it may meet **hash collision**. Its time complexity isn't stable.

  Binary Search Tree's time complexity depends on whether the tree is **complete** or not. It's not stable, either.

- Complexity of data structure.

  Hash table is more complex than Binary Search Tree. We need to consider the **hash function, hash collision, increasement / decreasement of size**. While, for Binary Search Tree, we just need to know whether the tree is complete.

  Usually, extra complexity costs extra time and space. Date structure should be as simple as possible.
