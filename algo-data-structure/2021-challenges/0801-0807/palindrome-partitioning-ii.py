class SolutionDFS:
    """
    https://leetcode.com/problems/palindrome-partitioning-ii/

    DFS + caching
    """

    def __init__(self) -> None:
        self.s = ""
        self.palindrome_memo = []
        self.cut_memo = []

    def is_palindrome(self, start: int, end: int) -> bool:
        l, r = start, end - 1

        if l >= r:
            return True

        if self.palindrome_memo[l][r] is not None:
            return self.palindrome_memo[l][r]

        self.palindrome_memo[l][r] = self.s[l] == self.s[r] and self.is_palindrome(
            start + 1, end - 1
        )
        return self.palindrome_memo[l][r]

    def dfs(self, start: int, end: int, prev_count: int) -> int:
        if start == end or self.is_palindrome(start, end):
            return 0

        if self.cut_memo[start] is not None:
            return self.cut_memo[start]

        count = prev_count
        for i in range(start + 1, end):
            if self.is_palindrome(start, i):
                count = min(count, self.dfs(i, end, prev_count) + 1)
        self.cut_memo[start] = count
        return count

    def minCut(self, s: str) -> int:
        self.s = s
        #  if s[i:j] is a palindrome
        self.palindrome_memo = [[None for _ in range(len(s))] for _ in range(len(s))]
        #  the nb of cut in s[i:]
        self.cut_memo = [None for _ in range(len(s))]

        return self.dfs(0, len(s), len(s) - 1)


class SolutionDP:
    def minCut(self, s: str) -> int:
        n = len(s)
        cut_dp = [0 for _ in range(n)]
        palindrome_dp = [[False for _ in range(n)] for _ in range(n)]

        #  build palindrome_dp
        for end in range(n):
            for start in range(end + 1):
                if s[start] == s[end]:
                    if end - start <= 2 or palindrome_dp[start + 1][end - 1]:
                        palindrome_dp[start][end] = True

        #  build cut_dp
        for end in range(n):
            count = n
            for start in range(end + 1):
                if palindrome_dp[start][end]:
                    count = min(count, cut_dp[start - 1] + 1) if start > 0 else 0
            cut_dp[start] = count

        return cut_dp[n - 1]