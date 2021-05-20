# Union & Find

Unon & Find is a **tree** data structure, which deals with **finding an elements** in the sets and **unioning the disjoint sets**.

- Union: union 2 sub-sets
- Find: find the sub-set of an element.
  > It can be used to verify whether 2 elements are in the same set.


## Node

The node in Unon & Find has an attribute, **parent**.

Unon & Find is create by the **array**. A node is represented as followed.

```python
node[idx] = parent_idx
```

## Initialization

Unon & Find is initialized by an array, `roots`.

The **parents** of initial elements are **themselves**.

```python
class UnionFind:
    def __init__(self, n: int) -> None:
        self.roots = [i for i in range(n)]
```

## Find the root

```python
def findRoot(self, i: int) -> int:
    root = i
    while root != self.roots[root]:
        root = self.roots[root]
    return root
```

## Compress path

To improve the performance, reduce the rank (the depth of the tree), we compress the path while finding the root.

```python
def findRoot(self, i: int) -> int:
    root = i
    while root != self.roots[root]:
        root = self.roots[root]
    # compress the path
    # point sub-nodes to the root directly
    while i != root:
        self.root[i], i = root, self.root[i]
    return root
```

## isConnected

Verify if 2 sets is connected.

```python
def isConnected(self, p: int, q: int) -> bool:
    return self.findRoot(p) == self.findRoot(q)
```

## union

Union 2 sets.

```python
def union(self, p: int, q: int) -> None:
    p_root = self.findRoot(p)
    q_root = self.findRoot(q)
    # p.parent = q
    self.roots[p_root] = q_root
```
