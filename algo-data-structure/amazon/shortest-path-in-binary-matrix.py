from typing import List
from collections import deque
import heapq


class SolutionBFSLayers:
    """
    https://leetcode.com/problems/shortest-path-in-binary-matrix/

    The depth of search is the length of the min path.
    """

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1
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

        if grid[0][0] != 0 or grid[max_row][max_col] != 0:
            return -1

        queue = deque([(0, 0)])
        visited = set()
        dist = 1

        while queue:
            nb_nodes = len(queue)
            for _ in range(nb_nodes):
                x, y = queue.popleft()

                if (x, y) in visited:
                    continue

                if (x, y) == (max_row, max_row):
                    return dist

                visited.add((x, y))

                for d in directions:
                    i, j = x + d[0], y + d[1]
                    if not (0 <= i <= max_row and 0 <= j <= max_row):
                        continue
                    if grid[i][j] != 0:
                        continue
                    if (i, j) in visited:
                        continue
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
        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1
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

        if grid[0][0] != 0 or grid[max_row][max_col] != 0:
            return -1

        queue = deque([(0, 0, 1)])  # x, y, dist
        visited = set()

        while queue:
            x, y, dist = queue.popleft()

            if (x, y) in visited:
                continue

            if (x, y) == (max_row, max_col):
                return dist

            visited.add((x, y))

            for d in directions:
                i, j = x + d[0], y + d[1]
                if not (0 <= i <= max_col and 0 <= j <= max_col):
                    continue
                if grid[i][j] != 0:
                    continue
                if (i, j) in visited:
                    continue

                queue.append((i, j, dist + 1))

        return -1


class SolutionDijkstra:
    """
    Dijkstra is based on BFS.

    Instead of poplefting in a queue, poping the top of the minHeap.
    minHeap is created according to the distance from the current node to the start.
    """

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1
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

        if grid[0][0] != 0 or grid[max_row][max_col] != 0:
            return -1

        queue = priority_queue = [(1, (0, 0))]
        visited = set()
        dist = 1

        while queue:
            distance, cell = heapq.heappop(priority_queue)

            if cell in visited:
                continue

            if cell == (max_row, max_col):
                return distance

            visited.add(cell)

            for row_difference, col_difference in directions:
                new_row = cell[0] + row_difference
                new_col = cell[1] + col_difference
                if not (0 <= new_row <= max_row and 0 <= new_col <= max_col):
                    continue
                if grid[new_row][new_col] != 0:
                    continue

                if (new_row, new_col) in visited:
                    continue
                entry = (distance + 1, (new_row, new_col))
                heapq.heappush(priority_queue, entry)

        return -1


class SolutionAStar:
    """
    A* is based on BFS.

    Instead of poplefting in a queue, poping the top of the minHeap.
    minHeap is created according to the "total" distance, d:

    d = estimated_distance + current_distance

    estimated_distance is the "direct" path from current node to the end, regardless the blocks.
    Whether it's L1 or L2 distance depends on the context.

    current_distance is the path from the current node to the start.
    """

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1
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

        # Check that the first and last cells are open.
        if grid[0][0] or grid[max_row][max_col]:
            return -1

        # Set up the A* search.
        visited = set()
        # Entries on the priority queue are of the form
        # (total distance estimate, distance so far, (cell row, cell col))
        priority_queue = [(1 + max(max_row, max_col), 1, (0, 0))]

        while priority_queue:
            estimate, distance, cell = heapq.heappop(priority_queue)

            if cell in visited:
                continue

            if cell == (max_row, max_col):
                return distance

            visited.add(cell)

            for row_difference, col_difference in directions:
                new_row = cell[0] + row_difference
                new_col = cell[1] + col_difference
                if not (0 <= new_row <= max_row and 0 <= new_col <= max_col):
                    continue
                if grid[new_row][new_col] != 0:
                    continue

                if (new_row, new_col) in visited:
                    continue
                estimate = max(max_row - new_row, max_col - new_col) + distance + 1
                entry = (estimate, distance + 1, (new_row, new_col))
                heapq.heappush(priority_queue, entry)

        # There was no path.
        return -1