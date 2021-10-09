from typing import List
from collections import deque


class Solution:
    def __init__(self) -> None:
        self.visited = []
        self.grid = []
        self.dx = [-1, 1, 0, 0]
        self.dy = [0, 0, -1, 1]

    def dfs(self, x: int, y: int) -> None:
        if x < 0 or x >= len(self.grid) or y < 0 or y >= len(self.grid[0]):
            return

        if self.visited[x][y] or self.grid[x][y] == "0":
            return

        self.visited[x][y] = True

        for i in range(4):
            self.dfs(x + self.dx[i], y + self.dy[i])

    def bfs(self, x: int, y: int) -> None:
        queue = deque([(x, y)])
        while queue:
            x, y = queue.popleft()
            self.visited[x][y] = True

            for d in range(4):
                i = x + self.dx[d]
                j = y + self.dy[d]
                if i < 0 or i >= len(self.grid) or j < 0 or j >= len(self.grid[0]):
                    continue
                if self.visited[i][j] or self.grid[i][j] == "0":
                    continue

                queue.append((i, j))

    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        self.grid = grid
        self.visited = [[False for _ in range(n)] for _ in range(m)]

        count = 0
        for i in range(m):
            for j in range(n):
                if self.grid[i][j] == "1" and not self.visited[i][j]:
                    #  self.dfs(i, j)
                    self.bfs(i, j)
                    count += 1
        return count


class SolutionUF:
    """
    https://leetcode.com/problems/number-of-islands/

    using Union & Find:

    The number of islands is the number of the sets.
    """

    def __init__(self) -> None:
        self.dx = [-1, 1, 0, 0]
        self.dy = [0, 0, -1, 1]

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])

        uf = UnionFind(grid)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    for type in range(4):
                        x = i + self.dx[type]
                        y = j + self.dy[type]
                        if 0 <= x < m and 0 <= y < n and grid[x][y] == "1":
                            uf.union(i * n + j, x * n + y)

        print(uf.parent)
        return uf.nbOfSets()


class UnionFind:
    def __init__(self, grid: List[List[str]]) -> None:
        m, n = len(grid), len(grid[0])
        self.parent = [
            i * n + j if grid[i][j] == "1" else -1 for i in range(m) for j in range(n)
        ]
        print(self.parent)

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
