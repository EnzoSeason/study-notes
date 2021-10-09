class Solution:
    """
    https://leetcode.com/problems/longest-palindromic-substring/

    dp[i][j]: if s[i:j+1] is palindromic.
    """

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[True if i == j else False for j in range(n)] for i in range(n)]
        start, end = 0, 0

        #  make sure dp[i + 1][j - 1] is calculated
        #  before processing dp[i][j]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    if j - i == 1 or dp[i + 1][j - 1]:
                        dp[i][j] = True
                        if j - i > end - start:
                            start = i
                            end = j

        return s[start : end + 1]


class SolutionTwoPointers:
    """
    https://leetcode.com/problems/palindromic-substrings/
    """

    def longestPalindrome(self, s: str) -> str:
        res = ""

        for i in range(len(s)):

            res = max(
                res,
                self.palindromeRange(s, i, i),  #  set s[i] as search center
                self.palindromeRange(
                    s, i, i + 1
                ),  #  set s[i], s[i] + 1 as search center.
                key=len,
            )

        return res

    def palindromeRange(self, s: str, i: int, j: int) -> str:
        start, end = i, i

        while i >= 0 and j < len(s) and s[i] == s[j]:
            start, end = i, j
            i -= 1
            j += 1

        return s[start : end + 1]
