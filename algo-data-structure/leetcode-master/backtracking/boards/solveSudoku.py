from typing import List


class Solution:
    """
    https://leetcode.com/problems/sudoku-solver/
    """

    def __init__(self) -> None:
        self.board = []

    def isValid(self, row: int, col: int, target: int) -> bool:
        for idx in range(len(self.board)):
            if self.board[idx][col] == str(target):
                return False
            if self.board[row][idx] == str(target):
                return False
            box_row, box_col = (row // 3) * 3 + idx // 3, (col // 3) * 3 + idx % 3
            if self.board[box_row][box_col] == str(target):
                return False
        return True
    
    def getPlace(self) -> List[int]:
        for row in range(len(self.board)):
            for col in range(len(self.board)):
                if self.board[row][col] == ".":
                    return [row, col]
        return [-1, -1]
    
    def isSolved(self) -> bool:
        row, col = self.getPlace()
        
        if row == -1 and col == -1:
            ## The board is completed.
            return True
        
        for i in range(1, 10):
            if self.isValid(row, col, i):
                self.board[row][col] = str(i)
                if self.isSolved():
                    return True
                else:
                    self.board[row][col] = "."
        return False

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if board is None or len(board) == 0:
            return
        self.board = board
        self.isSolved()