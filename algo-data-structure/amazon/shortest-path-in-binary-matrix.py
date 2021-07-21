from typing import List
from collections import deque


class SolutionBFSLayers:
    """
    https://leetcode.com/problems/shortest-path-in-binary-matrix/

    The depth of search is the length of the min path.
    """
    
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        directions = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]

        if grid[0][0] != 0 or grid[M - 1][N - 1] != 0:
            return -1

        queue = deque([(0, 0)])
        visited = {(0, 0)}
        dist = 1

        while queue:
            nb_nodes = len(queue)
            for _ in range(nb_nodes):
                x, y = queue.popleft()

                if (x, y) == (M - 1, N - 1):
                    return dist

                for d in directions:
                    i, j = x + d[0], y + d[1]
                    if not (0 <= i < M and 0 <= j < N):
                        continue
                    if grid[i][j] != 0:
                        continue
                    if (i, j) in visited:
                        continue
                    visited.add((i, j))
                    queue.append((i, j))
            dist += 1

        return -1

class SolutionBFS:
    """
    calculate the length of the min path during the BFS

    The element in queue is (x, y, min_distance_to_start)
    min_distance_to_start includes the start, which means is at least 1.
    """
    
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        if grid[0][0] != 0 or grid[M - 1][N - 1] != 0:
            return -1
        
        queue = deque([(0, 0, 1)]) # x, y, dist
        visited = {(0, 0)}
        
        while queue:
            x, y, dist = queue.popleft()

            if (x, y) == (M - 1, N - 1):
                return dist

            for d in directions:
                i, j = x + d[0], y + d[1]
                if not (0 <= i < M and 0 <= j < N):
                    continue
                if grid[i][j] != 0:
                    continue
                if (i, j) in visited:
                    continue
                visited.add((i, j))
                queue.append((i, j, dist + 1))
        
        return -1