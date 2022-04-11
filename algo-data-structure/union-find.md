# Union & Find

Unon & Find is a **tree** data structure, which deals with **finding an elements** in the sets and **unioning the disjoint sets**.

- Union: union 2 sub-sets
- Find: find the sub-set of an element.
  > It can be used to verify whether 2 elements are in the same set.

## Node

The node in Unon & Find has an attribute, **parent**.

Unon & Find is create by the **array**.

```python
parent_node = self.parent[curr_node]
```

## Initialization

Unon & Find is initialized by an array, `parent`.

The **parents** of initial elements are **themselves**.

```python
class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent = [i for i in range(n)]
```

## Find the root

```python
def findRoot(self, i: int) -> int:
    root = i
    while root != self.parent[root]:
        root = self.parent[root]
    return root
```

## Compress the path

To improve the performance, reduce the depth of the tree, we compress the path while finding the root.

We set **all the nodes under** a node as its **direct children**. It's the recommended way.

```python
def findRoot(self, i: int) -> int:
    root = i
    while root != self.parent[root]:
        root = self.parent[root]
    # compress the path
    # point sub-nodes to the root directly
    while i != root:
        self.parent[i], i = root, self.parent[i]
    return root
```

## union

Union 2 sets.

```python
def union(self, p: int, q: int) -> None:
    p_root = self.findRoot(p)
    q_root = self.findRoot(q)
    # p_root.parent = q_root
    self.parent[p_root] = q_root
```

We can compress the path here if we didn't do it in the `findRoot`.
However, we need to use another array, `rank`. It keeps the depth of the nodes.

We always attach **smaller** rank tree **under** root of **high** rank tree.

```python
def __init__(self, n: int) -> None:
    self.parent = [i for i in range(n)]
    self.ranks = [0 for _ in range(n)]

def union(self, p: int, q: int) -> None:
    p_root = self.findRoot(p)
    q_root = self.findRoot(q)

    if p_root != q_root:
        if self.ranks[p_root] > self.ranks[q_root]:
            # q_root.parent = p_root
            self.parent[q_root] = p_root
        elif  self.ranks[p_root] < self.ranks[q_root]:
            # p_root.parent = q_root
            self.parent[p_root] = q_root
        else:
            # p_root.parent = q_root
            self.parent[p_root] = q_root
            self.ranks[p_root] += 1

```

## [Full implementation](https://github.com/EnzoSeason/study-notes/blob/main/algo-data-structure/union&find/UnionFind.py)
