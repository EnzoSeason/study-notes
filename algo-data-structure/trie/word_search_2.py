from typing import List


class Solution:
    def __init__(self):
        self.res = set()
        self.trie_root = {}
        self.EOF = "# "
        self.dx = [-1, 1, 0, 0]
        self.dy = [0, 0, -1, 1]

    def dfs(
        self,
        board: List[List[str]],
        visited: List[List[bool]],
        i: int,
        j: int,
        prefix: str,
        trie_node: dict,
    ) -> None:
        if self.EOF in trie_node:
            self.res.add(prefix)
        
        #  end conditions
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        if visited[i][j]:
            return
        
        if board[i][j] not in trie_node:
            return

        #  prepare date
        #  increase prefix
        prefix += board[i][j]
        #   go deeper in the trie
        trie_node = trie_node[board[i][j]]
        #  mark the visited char
        visited[i][j] = True
        #  divide and conquer
        for orientation in range(4):
            x = i + self.dx[orientation]
            y = j + self.dy[orientation]
            self.dfs(board, visited, x, y, prefix, trie_node)
        #  recover the data
        visited[i][j] = False

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if len(words) == 0 or len(board) == 0 or len(board[0]) == 0:
            return []

        #  build Trie
        for word in words:
            word = word.lower()
            node = self.trie_root
            for char in word:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node[self.EOF] = self.EOF

        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                self.dfs(board, visited, i, j, "", self.trie_root)

        return list(self.res)


if __name__ == "__main__":
    board = [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"],
    ]
    words = ["oath", "pea", "eat", "rain"]
    s = Solution()
    print(s.findWords(board, words))
