from typing import List


class SolutionDFS:
    """
    https://leetcode.com/problems/number-of-islands/

    using DFS
    When a "1" is met, set all the "1" around it to "0".
    """

    def __init(self) -> None:
        self.grid = None
        self.m = 0
        self.n = 0

    def floodfill(self, i: int, j: int) -> None:
        if i < 0 or i >= self.m or j < 0 or j >= self.n:
            return

        if self.grid[i][j] != "1":
            return

        self.grid[i][j] = "0"
        self.floodfill(i - 1, j)
        self.floodfill(i + 1, j)
        self.floodfill(i, j - 1)
        self.floodfill(i, j + 1)

    def numIslands(self, grid: List[List[str]]) -> int:
        self.m = len(grid)
        if self.m == 0:
            return 0
        self.n = len(grid[0])
        self.grid = grid

        count = 0
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == "1":
                    self.floodfill(i, j)
                    count += 1

        return count