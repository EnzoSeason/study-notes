# Binary Tree

## Tree

- nodes:

  There are 3 common types, **parent** node, **child** node and **sibling** node.

  The node that has no child is **leaf** node.

  The node that has no parent is **root** node.

- Height of the node *i*:

  It's the **max number of edge** from the node *i* to a **leaf** node

- Depth of the node *i*:

  It's the **number of edge** from the node *i* to the **root** node.

- Level of the node: **Depth** of the node + 1

## Binary Tree

In binary tree, a node has, at most, 2 children.

- full binary tree:

  All the nodes, except **leaf nodes**, have 2 children.

- complete binary tree:
  
  1. All the nodes, except those in **last 2 levels**, have 2 children.

  2. The leaf nodes are positioned as **left** as possible.

### Advantage of complete binary tree.

If we save a tree in the **array** and we suppose that the node *i* is saved in `arr[i]`, then its **left node** is saved in `arr[2*i]` and its **right** node is saved in `arr[2*i+1]`.

If the binary tree is complete, then the array, except the `arr[0]`, is **full**. Otherwise, there must have an index `i, i>0` that `arr[i] is None`.

## Traversing a binary tree

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
