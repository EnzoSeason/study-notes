from typing import List


class Solution:
    """
    https://leetcode.com/problems/n-queens/
    """

    def __init__(self) -> None:
        self.result = []

    def dfs(
        self,
        row: int,
        cols: List[int],
        left_diags: List[int],
        right_diags: List[int],
    ) -> None:
        if row == self.n:
            self.result.append(cols)

        for i in range(self.n):
            if (
                i not in cols
                and i + row not in left_diags
                and i - row not in right_diags
            ):
                self.dfs(
                    row + 1,
                    cols + [i],
                    left_diags + [i + row],
                    right_diags + [i - row],
                )

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        self.dfs(0, [], [], [])

        return [
            ["." * col + "Q" + "." * (n - col - 1) for col in board]
            for board in self.result
        ]
