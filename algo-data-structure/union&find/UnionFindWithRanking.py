class UnionFind:
    """
    Union Find with ranking

    Union Find is also called disjoint-set, merge–find set
    """

    def __init__(self, n: int) -> None:
        #  all the set are seperated, the parents are themselves.
        self.parents = [i for i in range(n)]
        #  The init ranks for all the parents are 0.
        self.ranks = [0 for _ in range(n)]

    def find(self, i: int) -> int:
        root = i
        while root != self.parents[root]:
            root = self.parents[root]
        #  compress the path
        #  set the parent of all the children to root
        while i != root:
            self.parents[i], i = root, self.parents[i]
        return root

    def union(self, p: int, q: int) -> None:
        p_root = self.find(p)
        q_root = self.find(q)

        #  the root has higher rank is the new root.
        if p_root != q_root:
            if self.ranks[p_root] > self.ranks[q_root]:
                self.parents[q_root] = p_root
            elif self.ranks[p_root] < self.ranks[q_root]:
                self.parents[p_root] = q_root
            else:
                self.parents[p_root] = q_root
                self.ranks[q_root] += 1