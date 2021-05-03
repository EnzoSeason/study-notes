from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        visited = []
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c != ".":
                    visited.extend([(c, i), (j, c), (i // 3, j // 3, c)])
        print(visited)
        return len(visited) == len(set(visited))


if __name__ == "__main__":
    s1 = Solution()
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
    print(s1.isValidSudoku(board))