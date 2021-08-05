from typing import Generator, List, Tuple
from collections import deque


class Solution:
    """
    https://leetcode.com/problems/making-a-large-island/

    1. label all the islands' groups. The label number starts from 2.
    2. find the max island after the connection


    Both DFS and BFS can be used to label the groups.
    """

    def __init__(self) -> None:
        self.grid = []
        self.directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        self.N = 0

    def move(self, node: Tuple[int]) -> Generator[Tuple[int], None, None]:
        for d in self.directions:
            x, y = node[0] + d[0], node[1] + d[1]
            if 0 <= x < self.N and 0 <= y < self.N:
                yield x, y

    def bfs(self, start: Tuple[int], flag: int) -> int:
        queue = deque([start])
        count = 0

        while queue:
            i, j = queue.popleft()

            if self.grid[i][j] != 1:
                continue

            self.grid[i][j] = flag
            count += 1

            for x, y in self.move((i, j)):
                if self.grid[x][y] != 1:
                    continue
                queue.append((x, y))

        return count
    
    def dfs(self, start: Tuple[int], flag: int) -> int:
        i, j = start
        
        if self.grid[i][j] != 1:
            return 0

        self.grid[i][j] = flag
        res = 1
        for node in self.move(start):
            res += self.dfs(node, flag)
        return res
        
    def largestIsland(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.N = len(grid)
        area = {0: 0}

        flag = 2
        for i in range(self.N):
            for j in range(self.N):
                if self.grid[i][j] == 1:
                    area[flag] = self.bfs((i, j), flag)
                    flag += 1

        res = max(area.values())
        for i in range(self.N):
            for j in range(self.N):
                if self.grid[i][j] == 0:
                    neighbours = set(self.grid[x][y] for x, y in self.move((i, j)))
                    res = max(res, sum(area[neighbour] for neighbour in neighbours) + 1)

        return res
