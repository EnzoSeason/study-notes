from typing import List


class Solution:
    """
    https://leetcode.com/problems/spiral-matrix-ii/
    """

    def generateMatrix1(self, n: int) -> List[List[int]]:
        """
        Idea: keep the inteval **immutable**.
        In this solution, I set it **left close, right open**
        """

        left, right, top, bottom = 0, n - 1, 0, n - 1
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        num = 1

        while left <= right and top <= bottom:

            if left == right and top == bottom:
                matrix[top][left] = num
                return matrix

            #  go right
            for j in range(left, right):
                matrix[top][j] = num
                num += 1

            #  go down
            for i in range(top, bottom):
                matrix[i][right] = num
                num += 1

            #   go left
            for j in range(right, left, -1):
                matrix[bottom][j] = num
                num += 1

            #  go top
            for i in range(bottom, top, -1):
                matrix[i][left] = num
                num += 1

            left += 1
            right -= 1
            top += 1
            bottom -= 1

        return matrix

    def generateMatrix2(self, n: int) -> List[List[int]]:
        """
        use dx, dy to make the moves
        """

        matrix = [[0 for _ in range(n)] for _ in range(n)]
        num = 1
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        i, j, d = 0, 0, 0
        while num <= n * n:
            matrix[i][j] = num

            #  update
            num += 1
            #  n % n == 0, -1 % n == n - 1
            #  It can find out if next move is out of bounds.
            #  This trick is used in circular queue.
            next_i = (i + dx[d]) % n
            next_j = (j + dy[d]) % n
            if matrix[next_i][next_j] != 0:
                #  change direction
                d = (d + 1) % 4
            i += dx[d]
            j += dy[d]

        return matrix


if __name__ == "__main__":
    s = Solution()
    print(s.generateMatrix1(3))
    print(s.generateMatrix2(3))