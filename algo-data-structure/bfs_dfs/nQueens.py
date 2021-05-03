from typing import List

# leetcode 51
class Solution1:
    def __init__(self) -> None:
        self.result = []
        self.col = set()
        self.left_diag = set()
        self.right_diag = set()

    def _dfs(self, row: int, n: int, current_res: List[int]) -> None:
        if row == n:
            self.result.append(current_res)
            return
        for col in range(n):
            if (
                col not in self.col
                and row + col not in self.left_diag
                and row - col not in self.right_diag
            ):
                self.col.add(col)
                self.left_diag.add(row + col)
                self.right_diag.add(row - col)

                self._dfs(row + 1, n, current_res + [col])

                self.col.remove(col)
                self.left_diag.remove(row + col)
                self.right_diag.remove(row - col)

    def nQueens(self, n: int) -> List[List[str]]:
        self._dfs(0, n, [])
        print(self.result)

        return [["." * i + "Q" + "." * (n - i - 1) for i in case] for case in self.result]

# leetcode 52
class Solution2:
    def __init__(self):
        self.result = 0
    
    def _dfs(self, row: int, n: int, cols: List[int], left_diags: List[int], right_diags: List[int]) -> None:
        if row == n:
            self.result += 1
        
        for col in range(n):
            if (col not in cols and row + col not in left_diags and row - col not in right_diags):
                self._dfs(row+1, n, cols + [col], left_diags + [row + col], right_diags + [row - col])
    
    def totalNQueens(self, n: int) -> int:
        self._dfs(0, n, [], [], [])
        return self.result


if __name__ == "__main__":
    s1 = Solution1()
    print(s1.nQueens(4))

    s2 = Solution2()
    print(s2.totalNQueens(4))
