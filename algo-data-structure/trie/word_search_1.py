from typing import List


class Solution:
    def _dfs(
        self,
        board: List[List[str]],
        visited: List[List[bool]],
        board_idx: List[int],
        word: str,
    ) -> bool:

        ## end conditions
        if len(word) == 0:
            return True

        [i, j] = board_idx

        if i < 0 or i == len(board) or j < 0 or j == len(board[0]):
            return False

        if board[i][j] != word[0]:
            return False
        
        if visited[i][j]:
            return False

        ## prepare date
        visited[i][j] = True
        ## divide & conquer
        top = self._dfs(board, visited, [i - 1, j], word[1:])
        bottom = self._dfs(board, visited, [i + 1, j], word[1:])
        left = self._dfs(board, visited, [i, j - 1], word[1:])
        right = self._dfs(board, visited, [i, j + 1], word[1:])
        ## recover data
        visited[i][j] = False

        return top or bottom or left or right

    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(board) == 0 or len(board[0]) == 0:
            return False
        if len(word) == 0:
            return False

        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if self._dfs(board, visited, [i, j], word):
                    return True

        return False


if __name__ == "__main__":
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "SEE"
    s = Solution()
    print(s.exist(board, word))
