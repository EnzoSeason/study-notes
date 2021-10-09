class Solution:
    """
    https://leetcode.com/problems/longest-palindromic-subsequence/

    dp[i][j]: the lenght of longest palindromic subsequence in s[i:j+1]
    """

    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[1 if i == j else 0 for i in range(n)] for j in range(n)]

        #  make sure dp[i + 1][j - 1] is calculated
        #  before processing dp[i][j]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][-1]