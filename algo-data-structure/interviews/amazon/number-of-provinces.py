from collections import defaultdict
from typing import List


class SolutionDFS:
    def __init__(self) -> None:
        self.adj_matrix = []
        self.n = 0
        self.visited = set()
        self.res = 0

    def dfs(self, i: int) -> None:
        if i in self.visited:
            return

        self.visited.add(i)

        for j in range(self.n):
            if self.adj_matrix[i][j] == 1 and i != j:
                self.dfs(j)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.adj_matrix = isConnected
        self.n = len(isConnected)

        count = 0
        for i in range(self.n):
            if i not in self.visited:
                self.dfs(i)
                count += 1
        return count


class UF:
    def __init__(self, n: int) -> None:
        self.parents = [i for i in range(n)]

    def find(self, i: int) -> int:
        root = i
        # find root
        while root != self.parents[root]:
            root = self.parents[root]
        # update parents
        while i != root:
            self.parents[i], i = root, self.parents[i]

        return root

    def union(self, p: int, q: int) -> None:
        """
        union the groups which contain p or q.
        set q_root as the new root.
        """
        p_root = self.find(p)
        q_root = self.find(q)
        self.parents[p_root] = q_root


class SolutionUF:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UF(n)

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1 and i != j:
                    uf.union(i, j)

        count = 0
        for i in range(len(uf.parents)):
            if i == uf.parents[i]:
                count += 1
        return count