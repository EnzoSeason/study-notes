class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent = [i for i in range(n)]

    def findRoot(self, i: int) -> int:
        root = i
        while root != self.parent[root]:
            root = self.parent[root]
        while i != root:
            self.parent[i], i = root, self.parent[i]
        return root

    def union(self, p: int, q: int) -> None:
        p_root = self.findRoot(p)
        q_root = self.findRoot(q)
        self.parent[p_root] = q_root

    def nbOfSets(self) -> int:
        n = len(self.parent)
        return sum([1 if i == self.parent[i] else 0 for i in range(n)])