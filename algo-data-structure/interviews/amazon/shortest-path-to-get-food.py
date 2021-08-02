from typing import List, Tuple
import heapq


class Solution:
    """
    use BFS

    apply dijkstra by using min heap.
    min heap is sorted by the distance from current node to the start.
    """

    def bfs(self, grid: List[List[str]], start: Tuple[int]) -> int:
        queue = []
        heapq.heappush(queue, (0, start))
        visited = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            count, cell = heapq.heappop(queue)
            if grid[cell[0]][cell[1]] == "#":
                return count
            if grid[cell[0]][cell[1]] == "X":
                continue
            if cell in visited:
                continue

            visited.add(cell)
            for d in directions:
                new_cell = (cell[0] + d[0], cell[1] + d[1])
                if not (
                    0 <= new_cell[0] < len(grid) and 0 <= new_cell[1] < len(grid[0])
                ):
                    continue
                if new_cell in visited:
                    continue
                heapq.heappush(queue, (count + 1, new_cell))

    def getFood(self, grid: List[List[str]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "*":
                    start = (i, j)
                    break
        return self.bfs(grid, start) if self.bfs(grid, start) else -1