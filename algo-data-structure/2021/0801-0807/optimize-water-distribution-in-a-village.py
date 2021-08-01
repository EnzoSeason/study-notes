from typing import List


class UnionFind:
    def __init__(self, n: int) -> None:
        self.parents = [i for i in range(n)]

    def find(self, p) -> int:
        root = p
        while root != self.parents[root]:
            root = self.parents[root]

        while p != root:
            self.parents[p], p = root, self.parents[p]

        return root

    def union(self, p: int, q: int) -> None:
        p_root = self.find(p)
        q_root = self.find(q)
        self.parents[p_root] = q_root


class Solution:
    """
    https://leetcode.com/problems/optimize-water-distribution-in-a-village/

    It's the Minimum Spanning Tree or MST of a graph.

    We need to find a subset of edges which connects all the nodes of the graph with the minimum possible total weight.

    Tricks: create a virtual node to connect all the nodes. The edges represents the building cost.
    """

    def minCostToSupplyWater(
        self, n: int, wells: List[int], pipes: List[List[int]]
    ) -> int:
        uf = UnionFind(n + 1)
        for i in range(len(wells)):
            pipes.append([0, i + 1, wells[i]])
        pipes.sort(key=lambda x: x[2])
        cost = 0

        for pipe in pipes:
            start, end = pipe[0], pipe[1]
            if uf.find(start) != uf.find(end):
                uf.union(start, end)
                cost += pipe[2]

        return cost