from typing import List


class Solution:
    def isValid(self, row: int, col: int, board: List[List[str]], target: str) -> bool:
        n = len(board)
        for idx in range(n):
            if board[idx][col] == target:
                return False
            if board[row][idx] == target:
                return False
            if board[3 * (row // 3) + idx % 3][3 * (col // 3) + idx % 3] == target:
                return False
        return True

    def isSolved(self, board: List[List[str]]) -> bool:
        n = len(board)
        for row in range(n):
            for col in range(n):
                if board[row][col] == ".":
                    for i in range(1, 10):
                        new_char = str(i)
                        if self.isValid(row, col, board, new_char):
                            board[row][col] = new_char
                            if self.isSolved(board):
                                return True
                            else:
                                board[row][col] = "."
                    return False
        return True

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if board is None or len(board) == 0:
            return
        print(self.isSolved(board))
        print(board)


if __name__ == "__main__":
    s = Solution()
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    s.solveSudoku(board)
