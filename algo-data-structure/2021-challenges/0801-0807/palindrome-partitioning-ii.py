class Solution:
    """
    https://leetcode.com/problems/palindrome-partitioning-ii/

    DFS + caching
    """
    
    def is_palindrome(self, start: int, end: int) -> bool:
        l, r = start, end - 1

        if l >= r:
            return True

        if self.is_cut[l][r] is not None:
            return self.is_cut[l][r]

        self.is_cut[l][r] = self.s[l] == self.s[r] and self.is_palindrome(
            start + 1, end - 1
        )
        return self.is_cut[l][r]

    def dfs(self, start: int, end: int, prev_count: int) -> int:
        if start == end or self.is_palindrome(start, end):
            return 0

        if self.cut_count[start][end - 1] is not None:
            return self.cut_count[start][end - 1]

        count = prev_count
        for i in range(start + 1, end):
            if self.is_palindrome(start, i):
                count = min(count, self.dfs(i, end, prev_count) + 1)
        self.cut_count[start][end - 1] = count
        return count

    def minCut(self, s: str) -> int:
        self.s = s
        self.is_cut = [[None for _ in range(len(s))] for _ in range(len(s))]
        self.cut_count = [[None for _ in range(len(s))] for _ in range(len(s))]

        return self.dfs(0, len(s), len(s) - 1)