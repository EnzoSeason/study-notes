from typing import List


class Solution:
    def __init__(self) -> None:
        self.dx = [-1, 1, 0, 0]
        self.dy = [0, 0, -1, 1]
        self.grid = []
        self.visited = set()
        self.res = []

    def dfs(self, x: int, y: int, prev: list) -> None:
        if x < 0 or x >= len(self.grid) or y < 0 or y >= len(self.grid[0]):
            return

        if (x, y) in self.visited:
            return

        if self.grid[x][y] == 9:
            print(prev)
            self.res.append(prev)
            return

        if self.grid[x][y] != 1:
            return

        for i in range(4):
            self.visited.add((x, y))
            self.dfs(x + self.dx[i], y + self.dy[i], prev + [(x, y)])
            self.visited.remove((x, y))

    def minPath(self, grid: List[List[int]]) -> int:
        self.grid = grid

        self.dfs(0, 0, [])
        return min(self.res) if self.res else -1


if __name__ == "__main__":
    grid = [
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1],
        [0, 0, 0, 0, 9],
    ]

    s = Solution()
    print(s.minPath(grid))