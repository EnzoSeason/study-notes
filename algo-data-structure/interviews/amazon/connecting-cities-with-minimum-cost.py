from typing import List


class UnionFind:
    """
    Union Find with ranking

    Union Find is also called disjoint-set, merge–find set
    """
    
    def __init__(self, n: int) -> None:
        self.parents = [i for i in range(n)]
        self.ranks = [0 for _ in range(n)]

    def find(self, i: int) -> int:
        root = i
        while root != self.parents[root]:
            root = self.parents[root]
        while i != root:
            self.parents[i], i = root, self.parents[i]
        return root

    def union(self, p: int, q: int) -> None:
        p_root = self.find(p)
        q_root = self.find(q)

        if p_root != q_root:
            if self.ranks[p_root] > self.ranks[q_root]:
                self.parents[q_root] = p_root
            elif self.ranks[p_root] < self.ranks[q_root]:
                self.parents[p_root] = q_root
            else:
                self.parents[p_root] = q_root
                self.ranks[q_root] += 1


class Solution:
    """
    If we model the cities and connections as a graph, 
    each connection is an edge (undirected) and 
    each city is a node of the graph. 
    
    We need to find a subset of edges which connects all the nodes of the graph with the minimum possible total weight. 
    
    This is by definition the Minimum Spanning Tree or MST of a graph.
    """
    
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        """
        Params:
          n: number of cities
          connections: weighted edges
            connections[i] = [from, to, weight_of_edge]
        """
        
        uf = UnionFind(n + 1)
        #  sort connections by the weight of the edge
        connections.sort(key=lambda x: x[2])
        total = 0
        cost = 0

        for conn in connections:
            p = conn[0]
            q = conn[1]

            if uf.find(p) == uf.find(q):
                continue
            
            #  union two set
            uf.union(p, q)
            cost += conn[2]
            total += 1

        return cost if total == n - 1 else -1