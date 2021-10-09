#  Red Black Tree

The performance of the Binary Search Tree isn't stable. The worst time complexity is `O(n)` (The tree becomes a linked list).

To solve this problem, we need to **balance** the tree. It avoids turning a tree into a list.


# #  Balanced Binary Tree

For any node in a Binary Tree, the **difference of the height** of its **left child tree** and that of its **right child** must be smaller or equal to `1`.

For example, [AVL Tree](https://en.wikipedia.org/wiki/AVL_tree) is a balanced binary tree.


# #  Red Black Tree

A red–black tree is a special type of **binary search tree**.

Red Black Tree isn't a balanced binary tree. However, it still can avoid turning a tree into a list. It's widely used in the industry.

To create a R-B Tree, some rule should be followed.

1. Each node is either red or black.

2. All `NIL` leaves are considered **black**. (`NIL` node's value is `None`).

3. If a node is **red**, then **both its children** are **black**.

4. Every **path** from a given node to any of **its descendant NIL leaves** goes through the **same** number of **black** nodes.

5. Optional: The **root** is **black**.

According to the rule `4`, if we remove all the red nodes and connect all the black nodes. The height of the new tree must at the level `logn` (between log<sub>2</sub>n and log<sub>4</sub>n).

Because of the rule `3`, the heigth of R-B must at the level `logn`, too (between 2log<sub>2</sub>n and 2log<sub>4</sub>n).

We can say, the R-B tree is stable. The time complexity is always `O(logn)`.