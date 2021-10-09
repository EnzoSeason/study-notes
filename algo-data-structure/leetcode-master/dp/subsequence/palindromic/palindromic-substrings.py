class SolutionDP:
    """
    https://leetcode.com/problems/palindromic-substrings/

    dp[i][j]: if s[i:j+1] is palindromic.
    """

    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[True if i == j else False for j in range(n)] for i in range(n)]
        res = n

        #  make sure dp[i + 1][j - 1] is calculated
        #  before processing dp[i][j]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    if j - i == 1 or dp[i + 1][j - 1]:
                        dp[i][j] = True
                        res += 1
        return res


class SolutionTwoPointers:
    """
    https://leetcode.com/problems/palindromic-substrings/
    """

    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            res += self.count(s, i, i) #  set s[i] as search center
            res += self.count(s, i, i + 1) #  set s[i], s[i] + 1 as search center.

        return res

    def count(self, s: str, i: int, j) -> int:
        res = 0
        while i >= 0 and j < len(s) and s[i] == s[j]:
            res += 1
            i -= 1
            j += 1
        return res