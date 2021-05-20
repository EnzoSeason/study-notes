from typing import List


class SolutionDFS:
    """
    https://leetcode.com/problems/number-of-islands/

    using DFS
    When a "1" is met, set all the "1" around it to "0".
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