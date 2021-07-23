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
                    self.bfs(i, j)
                    count += 1
        return count
