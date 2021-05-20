from typing import List


class SolutionDFS:
    """
    https://leetcode.com/problems/number-of-islands/

    using DFS:

    When a "1" is met, set all the "1" around it to "0".

    Count the "1" we meet.
    """

    def __init__(self) -> None:
        self.grid = None
        self.visited = set()
        self.m = 0
        self.n = 0
        self.dx = [-1, 1, 0, 0]
        self.dy = [0, 0, -1, 1]

    def floodfill(self, i: int, j: int) -> int:
        if i < 0 or i >= self.m or j < 0 or j >= self.n:
            return 0

        if (i, j) in self.visited or self.grid[i][j] == "0":
            return 0

        self.visited.add((i, j))
        for type in range(4):
            self.floodfill(i + self.dx[type], j + self.dy[type])
        return 1

    def numIslands(self, grid: List[List[str]]) -> int:
        self.m = len(grid)
        if self.m == 0:
            return 0
        self.n = len(grid[0])
        self.grid = grid

        return sum([self.floodfill(i, j) for j in range(self.n) for i in range(self.m)])


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


if __name__ == "__main__":
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]

    s_uf = SolutionUF()
    print(s_uf.numIslands(grid))
