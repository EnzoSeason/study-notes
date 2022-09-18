from typing import Deque, Generator, List, Tuple
from collections import deque


class Solution:
    """
    https://leetcode.com/problems/shortest-bridge/

    use DFS to paint/visit one of the two islands
    use BFS to expand the search zone on the sea
    """

    def bfs(self, queue: Deque[Tuple[int]]) -> int:
        step = 0
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for x, y in self.move(i, j):
                    if self.grid[x][y] == 1:
                        return step
                    if self.grid[x][y] == 0:
                        self.grid[x][y] = -1
                        queue.append((x, y))
            step += 1

    def dfs(self, i: int, j: int, queue: Deque[Tuple[int]]) -> None:
        self.grid[i][j] = -1
        queue.append((i, j))

        for x, y in self.move(i, j):
            if self.grid[x][y] == 1:
                self.dfs(x, y, queue)

    def move(self, i: int, j: int) -> Generator[Tuple[int], None, None]:
        for d in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            x, y = i + d[0], j + d[1]
            if 0 <= x < self.N and 0 <= y < self.N:
                yield x, y

    def start(self) -> Tuple[int]:
        for i in range(self.N):
            for j in range(self.N):
                if self.grid[i][j] == 1:
                    return i, j

    def shortestBridge(self, grid: List[List[int]]):
        self.grid = grid
        self.N = len(grid)
        queue = deque([])

        self.dfs(*self.start(), queue)
        return self.bfs(queue)