from typing import List
from collections import deque


class Solution:
    """
    BFS
    """

    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque([])
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        fresh_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                if grid[i][j] == 1:
                    fresh_count += 1

        if fresh_count == 0:
            return 0

        count = -1
        while queue:
            count += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()

                if grid[x][y] == 1:
                    grid[x][y] = 2
                    fresh_count -= 1

                for i in range(4):
                    next_x, next_y = x + dx[i], y + dy[i]
                    if 0 <= next_x < m and 0 <= next_y < n:
                        if grid[next_x][next_y] == 1 and (next_x, next_y) not in queue:
                            queue.append((next_x, next_y))

        return count if fresh_count == 0 else -1