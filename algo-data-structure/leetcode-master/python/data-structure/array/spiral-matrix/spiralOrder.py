from typing import List


class Solution:
    """
    https://leetcode.com/problems/spiral-matrix/
    """

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        i, j = 0, 0
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        d = 0
        res = []
        visited = [[False for _ in range(n)] for _ in range(m)]

        for _ in range(m * n):
            res.append(matrix[i][j])
            visited[i][j] = True

            next_i = (i + dx[d]) % m
            next_j = (j + dy[d]) % n
            if visited[next_i][next_j]:
                d = (d + 1) % 4
            i += dx[d]
            j += dy[d]

        return res