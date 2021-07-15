from typing import List
from collections import defaultdict


class SolutionDFS:
    def __init__(self) -> None:
        self.n = 0
        self.adj_list = defaultdict(list)
        self.visited = set()

    def dfs(self, node) -> None:
        self.visited.add(node)

        for vertex in self.adj_list[node]:
            if vertex not in self.visited:
                self.dfs(vertex)

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        for edge in edges:
            self.adj_list[edge[0]].append(edge[1])
            self.adj_list[edge[1]].append(edge[0])

        count = 0
        for node in range(n):
            if node in self.visited:
                continue

            self.dfs(node)
            count += 1

        return count


class UF:
    def __init__(self, n: int) -> None:
        self.parent = [i for i in range(n)]

    def find_root(self, i: int) -> int:
        root = i
        #  find root
        while root != self.parent[root]:
            root = self.parent[root]
        #  update UF
        while i != root:
            self.parent[i], i = root, self.parent[i]

        return root

    def union(self, p: int, q: int) -> None:
        p_root = self.find_root(p)
        q_root = self.find_root(q)
        self.parent[p_root] = q_root


class SolutionUF:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UF(n)

        for edge in edges:
            uf.union(edge[0], edge[1])

        roots = set()
        for i in range(n):
            roots.add(uf.find_root(i))

        return len(roots)