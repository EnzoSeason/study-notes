from typing import List


class Solution:
    """
    https://leetcode.com/problems/spiral-matrix-ii/

    Idea: keep the inteval **immutable**.
    In this solution, I set it **left close, right open**
    """

    def generateMatrix1(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        num = 1

        i, j, turn = 0, 0, 0
        while i <= n - 1 - turn and j <= n - 1 - turn:
            if i == n - 1 - turn and j == n - 1 - turn:
                matrix[i][j] = num
                return matrix
            # go right
            while j < n - 1 - turn:
                matrix[i][j] = num
                num += 1
                j += 1

            # go down
            while i < n - 1 - turn:
                matrix[i][j] = num
                num += 1
                i += 1

            # go left
            while j > 0 + turn:
                matrix[i][j] = num
                num += 1
                j -= 1

            # go top
            while i > 0 + turn:
                matrix[i][j] = num
                num += 1
                i -= 1

            i += 1
            j += 1
            turn += 1
        
        return matrix
    

    def generateMatrix2(self, n: int) -> List[List[int]]:
        left, right, top, bottom = 0, n - 1, 0, n - 1
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        num = 1

        while left <= right and top <= bottom:
            
            if left == right and top == bottom:
                matrix[top][left] = num
                return matrix
            
            # go right
            for j in range(left, right):
                matrix[top][j] = num
                num += 1
            
            # go down
            for i in range(top, bottom):
                matrix[i][right] = num
                num += 1
            
            # go left
            for j in range(right, left, -1):
                matrix[bottom][j] = num
                num += 1
            
            # go top
            for i in range(bottom, top, -1):
                matrix[i][left] = num
                num += 1
            
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        
        return matrix


if __name__ == "__main__":
    s = Solution()
    # print(s.generateMatrix1(3))
    print(s.generateMatrix2(3))