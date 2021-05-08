from typing import List


class Solution:
    def _dfs(self, board: List[List[str]], board_idx: List[int], word: str) -> bool:

        # end conditions
        if len(word) == 0:
            return True

        [i, j] = board_idx

        if i < 0 or i == len(board) or j < 0 or j == len(board[0]):
            return False

        if board[i][j] != word[0]:
            return False

        # prepare date
        original_char = board[i][j]
        board[i][j] = "#"
        # divide & conquer
        top = self._dfs(board, [i - 1, j], word[1:])
        bottom = self._dfs(board, [i + 1, j], word[1:])
        left = self._dfs(board, [i, j - 1], word[1:])
        right = self._dfs(board, [i, j + 1], word[1:])
        # recover data
        board[i][j] = original_char

        return top or bottom or left or right

    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(word) == 0:
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if self._dfs(board, [i, j], word):
                    return True

        return False


if __name__ == "__main__":
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "SEE"
    s = Solution()
    print(s.exist(board, word))
