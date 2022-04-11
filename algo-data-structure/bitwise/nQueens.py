class Solution:
    """
    https://leetcode.com/problems/n-queens-ii/submissions/
    using bits to stock cols, left_diags and right_diags
    """

    def __init__(self):
        self.result = 0
        ##  n represents the length of the board.
        self.n = 0
        ## Mark represents a row in the board.
        ##  Mark is 000001..1. There are (n - 1) `1`.
        self.mask = 0

    def _dfs(self, row: int, cols: int, left_diags: int, right_diags: int) -> None:
        """
        - row represents the index of current row
        - cols, left_diags, right_diags represent the postions attacked by the queens
        0 means safe, 1 means attacked
        """
        if row >= self.n:
            self.result += 1
            return
        ## get the available positions in the current row
        ## First, get the all the available positions by cols | left_diags | right_diags
        ##  Then, reverse the meaning, 1 means safe and 0 means attacked
        ## Finally, remove the useless 1 in the high postions, which are out of the board range.
        postions = (~(cols | left_diags | right_diags)) & self.mask
        ##  If postions is not 0, it's means there has safe place.
        while postions:
            ##  get the lowest 1
            safe_place = postions & -postions

            ## check the next row
            self._dfs(
                row + 1,
                cols | safe_place,  ## set safe_place attacked
                (left_diags | safe_place) << 1,  ## left shift for the next row
                (right_diags | safe_place) >> 1,  ## right shift for the next row
            )

            ## remove the lowest 1
            postions &= postions - 1

    def totalNQueens(self, n: int) -> int:
        if n < 1:
            return 0
        self.n = n
        ##  Mark is 000001..1. There are (n - 1) `1`
        self.mask = (1 << n) - 1
        self._dfs(0, 0, 0, 0)
        return self.result


if __name__ == "__main__":
    s = Solution()
    print(s.totalNQueens(4))